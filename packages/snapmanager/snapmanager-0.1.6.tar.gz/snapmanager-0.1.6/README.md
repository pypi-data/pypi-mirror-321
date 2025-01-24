# SnapManager

Makes VSS snapshot disks bootable in Google Cloud.

## Installation

```bash
pip install snapmanager
```

## Usage

```bash
snapmanager --project YOUR_PROJECT \
           --zone ZONE \
           --vpc-network VPC_NETWORK \
           --subnet SUBNET \
           --snapshot SNAPSHOT_NAME
```

### Required Arguments

- `--project`: Google Cloud project ID
- `--zone`: Google Cloud zone (e.g., europe-west1-b)
- `--vpc-network`: VPC network name
- `--subnet`: Subnet name
- `--snapshot`: Name of the VSS snapshot to restore

## Features

- Makes VSS snapshot disks bootable in Google Cloud
- Handles Windows VSS snapshots
- Configures UEFI boot for restored disks
- Creates a new VM with the restored disk

## Requirements

- Python 3.8 or higher
- Google Cloud project with Compute Engine API enabled
- VSS snapshot in Google Cloud
- Network access to create temporary VM

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
