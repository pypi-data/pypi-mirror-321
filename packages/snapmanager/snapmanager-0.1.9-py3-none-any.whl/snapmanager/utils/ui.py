"""UI utilities for VSS Restore Tool."""
import time
import threading
import signal
import logging
from typing import Optional, Dict, Any
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.spinner import Spinner
from rich import box

console = Console()

class UILogHandler(logging.Handler):
    """Log handler that sends logs to UIController."""
    
    def __init__(self, ui_controller):
        """Initialize log handler."""
        super().__init__()
        self.ui = ui_controller
        self.setLevel(logging.DEBUG)
    
    def emit(self, record):
        """Emit log record to UI."""
        try:
            msg = self.format(record)
            self.ui.print_message(msg)
        except Exception:
            self.handleError(record)

class UIController:
    """Controls UI elements, state and user interactions."""
    
    def __init__(self):
        """Initialize UI controller."""
        self.current_step = ""
        self.original_step = ""
        self.current_message = ""
        self.message_time = 0
        self.current_stage = None
        self.current_substage = None
        self.substage_message = None
        self.substage_buffer = {}
        self.completed_stages = []
        self.stage_order = []
        self.spinner = Spinner("dots")
        self.live = Live("", console=console, refresh_per_second=4, transient=True)
        self._stop_thread = False
        self._spinner_thread = None
        
        self.log_handler = UILogHandler(self)
        self.log_handler.setFormatter(logging.Formatter('%(message)s'))
        
        root_logger = logging.getLogger()
        root_logger.addHandler(self.log_handler)
        root_logger.setLevel(logging.DEBUG)
        
        signal.signal(signal.SIGINT, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle interrupt signal."""
        self._cleanup()
        console.print("\n[red]Operation aborted by user[/]")
        exit(1)
    
    def _cleanup(self):
        """Clean up resources."""
        self._stop_thread = True
        if self._spinner_thread:
            self._spinner_thread.join(timeout=0.2)
        if hasattr(self, 'live') and self.live.is_started:
            self.live.stop()
        
        logging.getLogger().removeHandler(self.log_handler)
    
    def _render_step(self) -> str:
        """Render current step status."""
        output = []
        now = time.time()
        symbol = self.spinner.render(time.time())
        
        for stage_name in self.stage_order:
            completed_stage = None
            for stage in self.completed_stages:
                if stage[0].endswith(stage_name + "[/]"):
                    completed_stage = stage
                    break
            
            if completed_stage:
                output.extend(completed_stage)
            elif stage_name == self.current_step:
                output.append(f"{symbol} [yellow]{self.original_step}[/]")
                if stage_name in self.substage_buffer:
                    for line in self.substage_buffer[stage_name]:
                        output.append(line)
                if self.current_substage:
                    substage_line = f"  {symbol} [yellow]{self.current_substage}[/]"
                    if self.substage_message:
                        dots = "." * ((int(now * 4) % 4))
                        substage_line += f": [yellow]{self.substage_message}{dots.ljust(3)}[/]"
                    output.append(substage_line)
                elif self.current_message and now - self.message_time < 2:
                    dots = "." * ((int(now * 4) % 4))
                    output[-1] += f": [yellow]{self.current_message}{dots.ljust(3)}[/]"
            elif stage_name in self.substage_buffer:
                output.append(f"[green]✓[/] [green]{stage_name}[/]")
                for line in self.substage_buffer[stage_name]:
                    output.append(line)
        
        return "\n".join(output) if output else ""

    def _update_spinner(self):
        """Update spinner in a separate thread."""
        while not self._stop_thread and self.live and self.live.is_started:
            self.live.update(self._render_step())
            time.sleep(0.1)
    
    def print_step_status(self, step_name: str, status: str = "pending", message: str = "") -> None:
        """Print step status with appropriate symbol."""
        if status == "pending":
            self.current_step = step_name
            self.original_step = step_name
            self.current_stage = step_name
            self.current_substage = None
            self.substage_message = None
            self.substage_buffer[step_name] = []
            if step_name not in self.stage_order:
                self.stage_order.append(step_name)
            
            if not self.live.is_started:
                self.live.start()
                self._stop_thread = False
                self._spinner_thread = threading.Thread(target=self._update_spinner)
                self._spinner_thread.daemon = True
                self._spinner_thread.start()
            
            if message:
                self.current_message = message
                self.message_time = time.time()
            return
        
        if status == "success":
            if step_name in self.substage_buffer and self.substage_buffer[step_name]:
                completed_output = [f"[green]✓[/] [green]{step_name}[/]"]
                completed_output.extend(self.substage_buffer[step_name])
                insert_pos = self.stage_order.index(step_name)
                if insert_pos >= len(self.completed_stages):
                    self.completed_stages.append(completed_output)
                else:
                    self.completed_stages.insert(insert_pos, completed_output)
            else:
                insert_pos = self.stage_order.index(step_name)
                if insert_pos >= len(self.completed_stages):
                    self.completed_stages.append([f"[green]✓[/] [green]{step_name}[/]"])
                else:
                    self.completed_stages.insert(insert_pos, [f"[green]✓[/] [green]{step_name}[/]"])
        elif status == "error":
            if step_name in self.substage_buffer and self.substage_buffer[step_name]:
                completed_output = [f"[red]✗[/] [red]{step_name}[/]" + (f": [red]{message}[/]" if message else "")]
                completed_output.extend(self.substage_buffer[step_name])
                insert_pos = self.stage_order.index(step_name)
                if insert_pos >= len(self.completed_stages):
                    self.completed_stages.append(completed_output)
                else:
                    self.completed_stages.insert(insert_pos, completed_output)
            else:
                insert_pos = self.stage_order.index(step_name)
                if insert_pos >= len(self.completed_stages):
                    self.completed_stages.append([f"[red]✗[/] [red]{step_name}[/]" + (f": [red]{message}[/]" if message else "")])
                else:
                    self.completed_stages.insert(insert_pos, [f"[red]✗[/] [red]{step_name}[/]" + (f": [red]{message}[/]" if message else "")])
        else:
            insert_pos = self.stage_order.index(step_name)
            if insert_pos >= len(self.completed_stages):
                self.completed_stages.append([f"[blue]ℹ[/] [blue]{step_name}[/]" + (f": [blue]{message}[/]" if message else "")])
            else:
                self.completed_stages.insert(insert_pos, [f"[blue]ℹ[/] [blue]{step_name}[/]" + (f": [blue]{message}[/]" if message else "")])
        
        if step_name == self.current_step:
            if step_name == self.current_stage:
                self.current_stage = None
            self.current_step = ""
            self.current_message = ""
            self.original_step = ""
            self.current_substage = None
            self.substage_message = None
    
    def print_substage(self, stage_name: str, substage_name: str, status: str = "pending", message: Optional[str] = None):
        """Print a substage status."""
        if status == "pending":
            if self.current_stage != stage_name:
                self.current_stage = stage_name
                if stage_name not in self.substage_buffer:
                    self.substage_buffer[stage_name] = []
            
            self.current_substage = substage_name
            self.substage_message = message
            self.message_time = time.time()
            
            if not self.live.is_started:
                self.live.start()
                self._stop_thread = False
                self._spinner_thread = threading.Thread(target=self._update_spinner)
                self._spinner_thread.daemon = True
                self._spinner_thread.start()
        elif status == "success":
            if stage_name == self.current_stage:
                substage_line = f"  [green]✓[/] [green]{substage_name}[/]"
                if stage_name not in self.substage_buffer:
                    self.substage_buffer[stage_name] = []
                if substage_line not in self.substage_buffer[stage_name]:
                    self.substage_buffer[stage_name].append(substage_line)
                    if self.current_substage == substage_name:
                        self.current_substage = None
                        self.substage_message = None
        elif status == "error":
            if stage_name == self.current_stage:
                error_line = f"  [red]✗[/] [red]{substage_name}[/]" + (f": [red]{message}[/]" if message else "")
                if stage_name not in self.substage_buffer:
                    self.substage_buffer[stage_name] = []
                if error_line not in self.substage_buffer[stage_name]:
                    self.substage_buffer[stage_name].append(error_line)
                    if self.current_substage == substage_name:
                        self.current_substage = None
                        self.substage_message = None
    
    def print_message(self, message: str) -> None:
        """Print a message."""
        if self.live and self.live.is_started:
            self.current_message = message
            self.message_time = time.time()
    
    def print_banner(self) -> None:
        """Print application banner."""
        console.print()
        console.print("[bold magenta]SnapManager[/] [dim]v0.1.6[/]")
        console.print("[dim]Makes VSS snapshot disks bootable in Google Cloud[/]")
        console.print()
    
    def print_operation_complete(self, duration: float, results: Optional[Dict[str, Any]] = None) -> None:
        """Print operation completion message with duration and optional results."""

        self._cleanup()
        
        for stage_output in self.completed_stages:
            console.print("\n".join(stage_output))
        
        minutes = int(duration / 60)
        seconds = int(duration % 60)
        
        console.print()
        if results and "Status" in results and results["Status"] == "Failed":
            console.print(Text("❌ Operation failed", style="red bold"))
            if "Error" in results:
                console.print(Text(f"Error: {results['Error']}", style="red"))
            if "Details" in results:
                console.print(Text(f"Details: {results['Details']}", style="red"))
        else:
            console.print(Text("Snapshot restored successfully", style="green bold"))
        
        console.print(Text(f"Duration: {minutes}m {seconds}s", style="white"))
        
        if results:
            console.print()
            for key, value in results.items():
                if key not in ["Error", "Details", "Status"]:
                    console.print(Text(f"{key}: ", style="cyan"), Text(str(value), style="white"))
    
    def print_results(self, results: Dict[str, Any]):
        """Print results in a table format."""
        with console.status("[bold green]Processing..."):
            for key, value in results.items():
                console.print(Text(f"{key}: ", style="cyan"), Text(str(value), style="white"))
    
    def __del__(self):
        """Ensure live display is stopped."""
        self._cleanup()
