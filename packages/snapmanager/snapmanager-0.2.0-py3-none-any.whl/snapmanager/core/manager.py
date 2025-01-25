"""VSS snapshot management."""
import logging
import time
import uuid
from typing import Dict, Any, Optional, Tuple

from snapmanager.core.types import RestoreConfig, StepResult
from snapmanager.core.vss import VSSService
from snapmanager.utils.compute import ComputeClient
from snapmanager.utils.ui import UIController
from snapmanager.utils.winrm import WinRMClient

logger = logging.getLogger(__name__)

class SnapManager:
    """Manages VSS snapshot operations."""
    
    def __init__(self, config: RestoreConfig):
        """Initialize snapshot manager."""
        self.config = config
        self.ui = UIController()
        self.compute = ComputeClient(config.project, config.zone, self.ui)
        self.vss = VSSService()
        self.vss.set_ui(self.ui)
        
        suffix = uuid.uuid4().hex[:8]
        self.disk_name = f"restored-{self.config.snapshot_name}-{suffix}"
        self.temp_vm_name = f"vss-temp-{suffix}"
        self.final_vm_name = f"restored-{self.config.snapshot_name}-{suffix}"
        
        self.stages = {
            "create_disk_from_snapshot": {
                "name": "Preparing Disk from Snapshot",
                "steps": [
                    ("create_disk", "Creating disk from snapshot", self._create_disk_from_snapshot),
                ]
            },
            "create_temp_vm": {
                "name": "Preparing Temporary VM",
                "steps": [
                    ("create_temp_vm", "Creating temporary VM", self._create_temp_vm),
                ]
            },
            "make_disk_bootable": {
                "name": "Making Disk Bootable",
                "steps": [
                    ("make_bootable", "Making disk bootable", self._make_bootable),
                    ("detach_disk", "Detaching disk from temporary VM", self._detach_disk),
                ]
            },
            "cleanup_temp_vm": {
                "name": "Cleaning Up",
                "steps": [
                    ("delete_temp_vm", "Deleting temporary VM", self._delete_temp_vm),
                ]
            },
            "create_restored_vm": {
                "name": "Creating Restored VM",
                "steps": [
                    ("create_restored_vm", "Creating restored VM", self._create_restored_vm),
                ]
            }
        }
    
    def _create_disk_from_snapshot(self) -> StepResult:
        """Create disk from snapshot."""
        try:
            operation = self.compute.create_disk_from_snapshot(self.disk_name, self.config.snapshot_name)
            if not operation:
                return StepResult(success=False, message="Failed to create disk")
            
            # Wait for the operation to complete
            result = self.compute.wait_for_operation(operation)
            if not result.get("success", False):
                error_msg = result.get("error", "Operation failed")
                if isinstance(error_msg, (list, tuple)):
                    error_msg = error_msg[0] if error_msg else "Operation failed"
                
                if isinstance(error_msg, str) and ("rate exceeded" in error_msg.lower() or "too frequent" in error_msg.lower()):
                    error_msg = (
                        "Rate limit exceeded for snapshot operations. "
                        "Please wait a few minutes before trying again."
                    )
                return StepResult(success=False, message=error_msg)
            
            return StepResult(
                success=True,
                results={
                    "Created Disk": self.disk_name,
                    "Status": "Ready for next stage"
                }
            )
        except Exception as e:
            error_msg = str(e)
            if "rate exceeded" in error_msg.lower() or "too frequent" in error_msg.lower():
                error_msg = (
                    "Rate limit exceeded for snapshot operations. "
                    "Please wait a few minutes before trying again."
                )
            return StepResult(success=False, message=f"Error: {error_msg}")
    
    def _create_temp_vm(self) -> StepResult:
        """Create a temporary VM with the restored disk attached."""
        try:
            operation = self.compute.create_temp_vm(
                name=self.temp_vm_name,
                machine_type="e2-standard-2",
                disk_name=self.disk_name,
                network=self.config.vpc_network,
                subnetwork=self.config.subnet,
                password="Admin123!"  # TODO: Make this configurable
            )
            
            result = self.compute.wait_for_operation(operation)
            if not result.get("success", False):
                error_msg = result.get("error", "Operation failed")
                if isinstance(error_msg, (list, tuple)):
                    error_msg = error_msg[0] if error_msg else "Operation failed"
                return StepResult(success=False, message=error_msg)
            
            return StepResult(success=True)
            
        except Exception as e:
            error_msg = str(e)
            return StepResult(success=False, message=f"Error: {error_msg}")

    def _make_bootable(self) -> StepResult:
        """Make the restored disk bootable."""
        try:
            vm = self.compute.get_instance(self.temp_vm_name)
            external_ip = vm.network_interfaces[0].access_configs[0].nat_i_p
            
            # Initialize VSS with VM's IP
            self.vss.winrm = WinRMClient(external_ip, ui_manager=self.ui)
            if not self.vss.winrm.wait_for_winrm():
                return StepResult(success=False, message="Failed to connect to VM via WinRM")
            
            # Run VSS operations
            self.vss.current_stage = "Making Disk Bootable"
            return self.vss.make_disk_bootable(self.temp_vm_name)
            
        except Exception as e:
            error_msg = str(e)
            return StepResult(success=False, message=f"Error: {error_msg}")
            
    def _detach_disk(self) -> StepResult:
        """Detach disk from temporary VM."""
        try:
            if self.ui:
                self.ui.print_step_status("Detaching disk from temporary VM")
                
            operation = self.compute.detach_disk(self.temp_vm_name, self.disk_name)
            if not operation:
                if self.ui:
                    self.ui.print_step_status("Detaching disk from temporary VM", "error", "Failed to detach disk")
                return StepResult(success=False, message="Failed to detach disk")
                
            # Wait for operation to complete
            result = self.compute.wait_for_operation(operation)
            if not result["success"]:
                if self.ui:
                    self.ui.print_step_status("Detaching disk from temporary VM", "error", f"Failed to detach disk: {result.get('error', 'Unknown error')}")
                return StepResult(success=False, message=f"Failed to detach disk: {result.get('error', 'Unknown error')}")
                
            if self.ui:
                self.ui.print_step_status("Detaching disk from temporary VM", "success")
            return StepResult(success=True)
            
        except Exception as e:
            error_msg = str(e)
            return StepResult(success=False, message=f"Error: {error_msg}")
            

    def _delete_temp_vm(self) -> StepResult:
        """Delete temporary VM."""
        try:
            operation = self.compute.delete_instance(self.temp_vm_name)
            if not operation:
                return StepResult(success=False, message="Failed to delete temporary VM")
                
            # Wait for operation to complete
            result = self.compute.wait_for_operation(operation)
            if not result.get("success", False):
                return StepResult(success=False, message=f"Failed to delete temporary VM: {result.get('error', 'Unknown error')}")
                
            return StepResult(success=True)
            
        except Exception as e:
            error_msg = str(e)
            return StepResult(success=False, message=f"Error: {error_msg}")

    def _create_restored_vm(self) -> StepResult:
        """Create the final restored VM."""
        try:
            operation = self.compute.create_restored_vm(
                name=self.final_vm_name,
                machine_type="e2-standard-2",
                boot_disk_name=self.disk_name,
                network=self.config.vpc_network,
                subnetwork=self.config.subnet,
                password=self.config.windows_password
            )
            
            result = self.compute.wait_for_operation(operation)
            if not result.get("success", False):
                error_msg = result.get("error", "Operation failed")
                if isinstance(error_msg, (list, tuple)):
                    error_msg = error_msg[0] if error_msg else "Operation failed"
                return StepResult(success=False, message=error_msg)
                
            return StepResult(
                success=True,
                results={
                    "Created Disk": self.disk_name,
                    "Restored VM": self.final_vm_name
                }
            )
            
        except Exception as e:
            error_msg = str(e)
            return StepResult(success=False, message=f"Error: {error_msg}")
    
    def run_stage(self, stage_id: str, stage: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """Run a stage of the restore process."""
        stage_results = {}
        
        try:
            if self.ui:
                self.ui.print_step_status(stage["name"])
            
            for step_id, step_desc, step_func in stage["steps"]:
                result = step_func()
                if not result.success:
                    if self.ui:
                        self.ui.print_step_status(stage["name"], "error", result.message)
                    return False, {}
                
                if result.results:
                    stage_results.update(result.results)
            
            if self.ui:
                self.ui.print_step_status(stage["name"], "success")
            return True, stage_results
            
        except Exception as e:
            error_msg = str(e)
            if self.ui:
                self.ui.print_step_status(stage["name"], "error", error_msg)
            return False, {}
    
    def run(self) -> bool:
        """Run the VSS restore process."""
        self.ui.print_banner()
        
        start_time = time.time()
        all_results = {}
        
        # Run each stage
        for stage_id, stage in self.stages.items():
            success, results = self.run_stage(stage_id, stage)
            if not success:
                return False
            all_results.update(results)
        
        duration = time.time() - start_time
        self.ui.print_operation_complete(duration, all_results)
        
        return True
