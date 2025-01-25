"""VSS snapshot restore operations."""
import logging
import time
from typing import Dict, Any, List, Optional

from snapmanager.core.types import StepResult
from snapmanager.utils.ui import UIController
from snapmanager.utils.winrm import WinRMClient

logger = logging.getLogger(__name__)

class VSSService:
    """Service for VSS operations."""
    
    def __init__(self):
        """Initialize VSS service."""
        self.winrm = None
        self.ui = None
        self.current_stage = None  # Track current stage
        
        # Define VSS stages
        self.stages = {
            "make_disk_bootable": {
                "name": "Making Disk Bootable",
                "steps": [
                    ("check_disk", "Checking disk status", self._check_disk_status),
                    ("bring_online", "Bringing disk online", self._bring_disk_online),
                    ("configure_volume", "Configuring Windows volume", self._configure_windows_volume),
                    ("check_windows", "Checking Windows directory", self._check_windows_directory),
                    ("create_bcd", "Creating BCD store", self._create_bcd_store),
                    ("configure_system", "Configuring system volume", self._configure_system_volume),
                    ("verify_drives", "Verifying drives", self._verify_drives),
                    ("create_uefi", "Creating UEFI BCD configuration", self._create_uefi_bcd),
                ]
            }
        }
    
    def set_ui(self, ui: UIController):
        """Set UI manager."""
        self.ui = ui
        
        # Add log handler if UI manager is provided
        if ui:
            self.log_handler = ui.log_handler
            logger.addHandler(self.log_handler)
            logger.setLevel(logging.DEBUG)
            
    def __del__(self):
        """Clean up resources."""
        if hasattr(self, 'log_handler'):
            logger.removeHandler(self.log_handler)
    
    def _run_command(self, vm_name: str, command: str) -> StepResult:
        """Run a command on the VM."""
        try:
            if not self.winrm:
                self.winrm = WinRMClient(self.vm_ip, ui_manager=self.ui)
                
            # Wait for WinRM to be available
            if not self.winrm.wait_for_winrm():
                error_msg = "Failed to connect to WinRM"
                logger.error(error_msg)
                return StepResult(success=False, message=error_msg)
                
            result = self.winrm.run_command(command)
            return StepResult(
                success=result.success,
                message=result.message
            )
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Failed to run command: {error_msg}")
            return StepResult(success=False, message=f"Failed to run command: {error_msg}")
    
    def _run_diskpart_commands(self, vm_name: str, commands: List[str]) -> StepResult:
        """Run diskpart commands using a script file."""
        script = "\n".join(commands)
        script_path = "C:\\diskpart_script.txt"
        
        ps_script = f"""
try {{
    # Create script file
    $script = @"
{script}
"@
    [System.IO.File]::WriteAllText("{script_path}", $script)

    # Run diskpart and capture output
    $output = & diskpart /s "{script_path}" 2>&1
    $output = $output -join "`n"
    
    # Check for errors
    $error_patterns = @(
        "Access is denied",
        "No usable volumes were found",
        "The volume you selected is not valid",
        "The disk you specified is not valid",
        "The operation failed to complete",
        "The system cannot find the file specified",
        "There is no disk selected"
    )
    
    # Check for success patterns based on commands
    $success_patterns = @(
        "DiskPart successfully",
        "is now the selected disk",
        "successfully onlined",
        "successfully assigned"
    )
    
    $has_error = $false
    foreach ($pattern in $error_patterns) {{
        if ($output -match $pattern) {{
            $has_error = $true
            break
        }}
    }}
    
    # If no error found, check for success messages
    if (-not $has_error) {{
        $has_success = $false
        foreach ($pattern in $success_patterns) {{
            if ($output -match $pattern) {{
                $has_success = $true
                break
            }}
        }}
        # For list disk command, consider it success if we see disk list
        if ($output -match "Disk ###") {{
            $has_success = $true
        }}
        $has_error = -not $has_success
    }}
    
    # Delete script file
    if (Test-Path "{script_path}") {{
        Remove-Item -Path "{script_path}" -Force -ErrorAction SilentlyContinue
    }}
    
    # Return output based on success/failure
    if (-not $has_error) {{
        Write-Output $output
    }} else {{
        Write-Error $output
        exit 1
    }}
}} catch {{
    if (Test-Path "{script_path}") {{
        Remove-Item -Path "{script_path}" -Force -ErrorAction SilentlyContinue
    }}
    Write-Error "PowerShell error: $_"
    exit 1
}}
"""
        result = self._run_command(vm_name, ps_script)
        logger.debug(f"Diskpart command output: {result.message}")
        return result
    
    def _check_disk_status(self, vm_name: str) -> StepResult:
        """Check disk status using diskpart."""
        if self.ui:
            self.ui.print_substage(self.current_stage, "Checking disk status")
            
        commands = ["list disk"]
        result = self._run_diskpart_commands(vm_name, commands)
        
        # Parse disk status
        if result.success:
            lines = result.message.splitlines()
            for line in lines:
                if "Disk 1" in line and "Offline" in line:
                    if self.ui:
                        self.ui.print_substage(self.current_stage, "Checking disk status", "success", "Disk 1 is offline")
                    return result
                
        if self.ui:
            if result.success:
                self.ui.print_substage(self.current_stage, "Checking disk status", "success")
            else:
                self.ui.print_substage(self.current_stage, "Checking disk status", "error", result.message)
        return result
    
    def _bring_disk_online(self, vm_name: str) -> StepResult:
        """Bring the disk online using diskpart."""
        if self.ui:
            self.ui.print_substage(self.current_stage, "Bringing disk online")
            
        commands = [
            "select disk 1",
            "online disk"
        ]
        result = self._run_diskpart_commands(vm_name, commands)
        
        if not result.success and "already online" in result.message.lower():
            result.success = True
            result.message = "Disk is already online"
            
        if self.ui:
            if result.success:
                self.ui.print_substage(self.current_stage, "Bringing disk online", "success")
            else:
                self.ui.print_substage(self.current_stage, "Bringing disk online", "error", result.message)
        return result
    
    def _configure_windows_volume(self, vm_name: str) -> StepResult:
        """Configure Windows volume."""
        if self.ui:
            self.ui.print_substage(self.current_stage, "Configuring Windows volume")
            
        commands = [
            "select disk 1",
            "list volume",
            "select volume 2",
            "attributes volume clear hidden",
            "attributes volume clear readonly",
            "assign letter=E"
        ]
        result = self._run_diskpart_commands(vm_name, commands)
        
        if not result.success and "already has a drive letter" in result.message.lower():
            result.success = True
            result.message = "Drive letter is already assigned"
            
        if self.ui:
            if result.success:
                self.ui.print_substage(self.current_stage, "Configuring Windows volume", "success")
            else:
                self.ui.print_substage(self.current_stage, "Configuring Windows volume", "error", result.message)
        return result
    
    def _check_windows_directory(self, vm_name: str) -> StepResult:
        """Check if Windows directory exists."""
        logger.info(f"Checking Windows directory on VM '{vm_name}'")
        if self.ui:
            self.ui.print_substage(self.current_stage, "Checking Windows directory")
            
        command = "Test-Path E:\\Windows"
        result = self._run_command(vm_name, command)
        if self.ui:
            if result.success:
                self.ui.print_substage(self.current_stage, "Checking Windows directory", "success")
            else:
                self.ui.print_substage(self.current_stage, "Checking Windows directory", "error", result.message)
        return result
    
    def _create_bcd_store(self, vm_name: str) -> StepResult:
        """Create BCD store."""
        if self.ui:
            self.ui.print_substage(self.current_stage, "Creating BCD store")
            
        check_drive = "Get-PSDrive E -ErrorAction SilentlyContinue"
        result = self._run_command(vm_name, check_drive)
        if not result.success or "E" not in result.message:
            logger.error("Drive E: is not accessible")
            if self.ui:
                self.ui.print_substage(self.current_stage, "Creating BCD store", "error", "Drive E: is not accessible")
            return StepResult(success=False, message="Drive E: is not accessible")
            
        wait_command = "Start-Sleep -Seconds 5"
        self._run_command(vm_name, wait_command)
        
        check_windows = "if (-not (Test-Path 'E:\\Windows')) { Write-Error 'E:\\Windows folder not found'; exit 1 }"
        result = self._run_command(vm_name, check_windows)
        if not result.success:
            if self.ui:
                self.ui.print_substage(self.current_stage, "Creating BCD store", "error", "E:\\Windows folder not found")
            return result
            
        result = self._run_command(vm_name, "bcdboot E:\\Windows /s E: /f ALL")
        if not result.success:
            if self.ui:
                self.ui.print_substage(self.current_stage, "Creating BCD store", "error", result.message)
            return result
        
        if self.ui:
            self.ui.print_substage(self.current_stage, "Creating BCD store", "success")
        return StepResult(success=True)
    
    def _configure_system_volume(self, vm_name: str) -> StepResult:
        """Configure system volume."""
        logger.info(f"Configuring system volume on VM '{vm_name}'")
        if self.ui:
            self.ui.print_substage(self.current_stage, "Configuring system volume")
            
        commands = [
            "list disk",
            "list volume",
            "select volume 3",
            "assign letter=S"
        ]
        result = self._run_diskpart_commands(vm_name, commands)
        
        if not result.success:
            if self.ui:
                self.ui.print_substage(self.current_stage, "Configuring system volume", "error", result.message)
            return result
            
        wait_command = "Start-Sleep -Seconds 5"
        self._run_command(vm_name, wait_command)
        
        check_drives = """
if (-not (Test-Path 'E:\\Windows')) { Write-Error 'E:\\Windows folder not found'; exit 1 }
if (-not (Test-Path 'S:\\')) { Write-Error 'S: drive not found'; exit 1 }
"""
        result = self._run_command(vm_name, check_drives)
        if not result.success:
            if self.ui:
                self.ui.print_substage(self.current_stage, "Configuring system volume", "error", result.message)
            return result
            
        if self.ui:
            self.ui.print_substage(self.current_stage, "Configuring system volume", "success")
        return result
    
    def _verify_drives(self, vm_name: str) -> StepResult:
        """Verify drive configuration."""
        logger.info(f"Verifying drive configuration on VM '{vm_name}'")
        if self.ui:
            self.ui.print_substage(self.current_stage, "Verifying drives")
            
        command = "Get-Disk | Select Number, OperationalStatus, PartitionStyle; Get-Partition | Select DiskNumber, PartitionNumber, DriveLetter, Size, Type"
        result = self._run_command(vm_name, command)
        if self.ui:
            if result.success:
                self.ui.print_substage(self.current_stage, "Verifying drives", "success")
            else:
                self.ui.print_substage(self.current_stage, "Verifying drives", "error", result.message)
        return result
    
    def _create_uefi_bcd(self, vm_name: str) -> StepResult:
        """Create UEFI BCD configuration."""
        logger.info(f"Creating UEFI BCD configuration on VM '{vm_name}'")
        if self.ui:
            self.ui.print_substage(self.current_stage, "Creating UEFI BCD configuration")
            
        result = self._run_command(vm_name, "bcdboot E:\\Windows /s S: /f UEFI")
        if not result.success:
            if self.ui:
                self.ui.print_substage(self.current_stage, "Creating UEFI BCD configuration", "error", result.message)
            return result
        
        if self.ui:
            self.ui.print_substage(self.current_stage, "Creating UEFI BCD configuration", "success")
        return StepResult(success=True)
    
    def make_disk_bootable(self, vm_name: str) -> StepResult:
        """Make a disk bootable by running VSS operations."""
        try:
            logger.info(f"Starting VSS operations to make disk bootable on VM '{vm_name}'")
            stage = self.stages["make_disk_bootable"]
            self.current_stage = stage["name"]
            
            for step_id, step_desc, step_func in stage["steps"]:
                if self.ui:
                    self.ui.print_substage(self.current_stage, step_desc)
                    
                logger.info(f"Running VSS step: {step_desc}")
                result = step_func(vm_name)
                
                if not result.success:
                    logger.error(f"VSS step failed: {step_desc} - {result.message}")
                    if self.ui:
                        self.ui.print_substage(self.current_stage, step_desc, "error", result.message)
                    return result
                    
                logger.info(f"VSS step completed: {step_desc}")
                if self.ui:
                    self.ui.print_substage(self.current_stage, step_desc, "success")
            
            logger.info(f"Successfully completed all VSS operations on VM '{vm_name}'")
            return StepResult(success=True)
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Failed to make disk bootable on VM '{vm_name}': {error_msg}")
            return StepResult(success=False, message=f"VSS operation failed: {error_msg}")


"""VSS restore operations."""
from typing import Optional

class VSSRestore:
    def __init__(self, host: str, username: str, password: str):
        self.host = host
        self.username = username
        self.password = password

    def check_disk_status(self) -> StepResult:
        """Check disk status using diskpart."""
        # TODO: Implement actual disk check
        return StepResult(True, "Disk is online")

    def bring_disk_online(self) -> StepResult:
        """Bring disk online using diskpart."""
        # TODO: Implement actual disk online
        return StepResult(True, "Disk is already online")

    def configure_windows_volume(self) -> StepResult:
        """Configure Windows volume."""
        # TODO: Implement volume configuration
        return StepResult(True, "Windows volume configured")

    def check_windows_directory(self) -> StepResult:
        """Check Windows directory exists."""
        # TODO: Implement directory check
        return StepResult(True, "Windows directory found")

    def create_bcd_store(self, drive: str) -> StepResult:
        """Create BCD store."""
        # TODO: Implement BCD store creation
        return StepResult(True, f"BCD store created on {drive}")

    def configure_system_volume(self) -> StepResult:
        """Configure system volume."""
        # TODO: Implement system volume configuration
        return StepResult(True, "System volume configured")

    def verify_drives(self) -> StepResult:
        """Verify drive configuration."""
        # TODO: Implement drive verification
        return StepResult(True, "Drives verified")

    def create_uefi_bcd(self) -> StepResult:
        """Create UEFI BCD configuration."""
        # TODO: Implement UEFI BCD creation
        return StepResult(True, "UEFI BCD created")
