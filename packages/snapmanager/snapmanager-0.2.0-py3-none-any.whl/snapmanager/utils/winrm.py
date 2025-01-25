"""Windows Remote Management (WinRM) implementation."""
import logging
import time
import socket
import base64
from dataclasses import dataclass
from typing import Optional

import winrm
from winrm.exceptions import WinRMOperationTimeoutError, WinRMTransportError

from snapmanager.core.types import StepResult
from snapmanager.utils.ui import UIController

logger = logging.getLogger(__name__)

@dataclass
class CommandResult:
    """Result of a command execution"""
    success: bool
    message: str = ""
    stdout: str = ""
    stderr: str = ""

def encode_powershell_command(command: str) -> str:
    """Encode PowerShell command in base64"""
    encoded = base64.b64encode(command.encode('utf-16-le')).decode('ascii')
    return encoded

class WinRMClient:
    """Client for Windows Remote Management operations"""
    
    def __init__(self, host: str, username: str = "Administrator", password: str = "Admin123!", ui_manager: Optional[UIController] = None):
        """Initialize WinRM client."""
        self.host = host
        self.username = username
        self.password = password
        self.session = None
        self.ui = ui_manager
        
        if ui_manager:
            self.log_handler = ui_manager.log_handler
            logger.addHandler(self.log_handler)
            logger.setLevel(logging.DEBUG)
    
    def _create_session(self):
        """Create a new WinRM session"""
        if not self.session:
            self.session = winrm.Session(
                target=self.host,
                auth=(self.username, self.password),
                transport="ntlm",
                server_cert_validation="ignore"
            )
    
    def check_port_open(self, max_attempts: int = 30) -> bool:
        """Check if WinRM port is open using socket connection"""
        logger.info(f"Checking if WinRM port is open on {self.host}...")
        
        for attempt in range(max_attempts):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((self.host, 5985))
                sock.close()
                
                if result == 0:
                    logger.info("WinRM port is open")
                    return True
                    
                logger.debug(f"Attempt {attempt + 1}/{max_attempts}: Port is not open yet")
                time.sleep(10)
                
            except Exception as e:
                logger.debug(f"Attempt {attempt + 1}/{max_attempts} failed: {str(e)}")
                time.sleep(10)
                
        logger.error("Timed out waiting for WinRM port to open")
        return False
    
    def wait_for_winrm(self, max_attempts: int = 30) -> bool:
        """Wait for WinRM to become available"""
        try:
            # First check if port is open
            if not self.check_port_open():
                return False
                
            logger.info("Waiting for WinRM service to become available...")
            test_command = "Write-Host 'WinRM is ready'"
            
            for attempt in range(max_attempts):
                try:
                    result = self.run_command(test_command)
                    if result.success:
                        logger.info("WinRM service is now available")
                        return True
                        
                except Exception as e:
                    logger.debug(f"Attempt {attempt + 1}/{max_attempts} failed: {str(e)}")
                    time.sleep(10)
                    
            logger.error("Timed out waiting for WinRM service")
            return False
            
        except Exception as e:
            logger.error(f"Error while waiting for WinRM: {str(e)}")
            return False
    
    def run_command(self, command: str, shell: str = "powershell") -> CommandResult:
        """Run a command using WinRM"""
        try:
            self._create_session()
            shell_id = self.session.protocol.open_shell()
            
            try:
                if shell == "powershell":
                    command = f"""
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
try {{
    {command}
}} catch {{
    Write-Error $_
    exit 1
}}
"""
                    encoded_command = encode_powershell_command(command)
                    command_id = self.session.protocol.run_command(
                        shell_id, 
                        'powershell.exe', 
                        ['-EncodedCommand', encoded_command]
                    )
                else:
                    command_id = self.session.protocol.run_command(shell_id, command)
                
                stdout, stderr, status_code = self.session.protocol.get_command_output(shell_id, command_id)
                self.session.protocol.cleanup_command(shell_id, command_id)
                
                success = status_code == 0
                stdout_str = stdout.decode('utf-8', errors='ignore')
                stderr_str = stderr.decode('utf-8', errors='ignore')
                
                if success:
                    logger.debug(f"Command succeeded with output: {stdout_str}")
                else:
                    logger.error(f"Command failed with error: {stderr_str}")
                    
                return CommandResult(
                    success=success,
                    message=stderr_str if not success else stdout_str,
                    stdout=stdout_str,
                    stderr=stderr_str
                )
                
            finally:
                self.session.protocol.close_shell(shell_id)
                
        except Exception as e:
            logger.error(f"Failed to execute command: {str(e)}")
            return CommandResult(
                success=False,
                message=str(e),
                stdout="",
                stderr=str(e)
            )
