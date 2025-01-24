"""Command line interface for VSS restore tool."""
import logging
import sys
from typing import Optional

import click
from rich.console import Console
from rich.logging import RichHandler

from snapmanager.core.types import RestoreConfig
from snapmanager.core.manager import SnapManager
from snapmanager.utils.ui import UIManager
from snapmanager.utils.compute import generate_strong_password

console = Console()

@click.command()
@click.option("--project", required=True, help="GCP project ID")
@click.option("--zone", required=True, help="GCP zone")
@click.option("--snapshot", required=True, help="Snapshot name")
@click.option("--vpc-network", required=True, help="VPC network name")
@click.option("--subnet", required=True, help="Subnet name")
def main(project: str, zone: str, snapshot: str, vpc_network: str, subnet: str):
    """Restore a VSS snapshot disk and make it bootable."""
    try:
        # Fixed values
        machine_type = "n1-standard2"
        windows_password = generate_strong_password()

        config = RestoreConfig(
            project=project,
            zone=zone,
            snapshot_name=snapshot,
            vpc_network=vpc_network,
            subnet=subnet,
            machine_type=machine_type,
            windows_password=windows_password
        )
        
        manager = SnapManager(config)
        success = manager.run()
        sys.exit(0 if success else 1)
        
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
