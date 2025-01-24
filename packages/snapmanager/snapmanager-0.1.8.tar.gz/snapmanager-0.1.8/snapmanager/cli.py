"""Command line interface for VSS restore tool."""
import argparse
import logging
import sys
from typing import Optional

from rich.console import Console
from rich.logging import RichHandler

from snapmanager.core.types import RestoreConfig
from snapmanager.core.manager import SnapManager
from snapmanager.utils.compute import generate_strong_password

logger = logging.getLogger(__name__)
console = Console()

def restore_command(args: argparse.Namespace) -> None:
    """Restore a VSS snapshot disk and make it bootable."""
    try:
        # Fixed values
        machine_type = "n1-standard2"
        windows_password = generate_strong_password()

        config = RestoreConfig(
            project=args.project,
            zone=args.zone,
            snapshot_name=args.snapshot,
            vpc_network=args.vpc_network,
            subnet=args.subnet,
            machine_type=machine_type,
            windows_password=windows_password
        )
        
        manager = SnapManager(config)
        success = manager.run()
        sys.exit(0 if success else 1)
        
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
        sys.exit(1)

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="SnapManager - Manage VSS snapshots in Google Cloud"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Restore command
    restore_parser = subparsers.add_parser(
        "restore", 
        help="Restore a VSS snapshot disk and make it bootable",
        description="Restore a VSS snapshot disk and create a new bootable VM instance from it."
    )
    restore_parser.add_argument(
        "--project",
        required=True,
        help="Google Cloud project ID where the snapshot and new VM will be created"
    )
    restore_parser.add_argument(
        "--zone",
        required=True,
        help="Google Cloud zone where the new VM will be created"
    )
    restore_parser.add_argument(
        "--vpc-network",
        required=True,
        help="VPC network to attach the new VM to"
    )
    restore_parser.add_argument(
        "--subnet",
        required=True,
        help="Subnet within the VPC network for the new VM"
    )
    restore_parser.add_argument(
        "--snapshot",
        required=True,
        help="Name of the VSS-enabled snapshot to restore from"
    )
    
    args = parser.parse_args()
    
    if args.command == "restore":
        restore_command(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
