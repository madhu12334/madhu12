import shutil
import os
from datetime import datetime

def backup_directory(source_dir, dest_dir):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_folder = os.path.join(dest_dir, f"backup_{timestamp}")
        shutil.copytree(source_dir, backup_folder)
        print("Backup successful.")
    except Exception as e:
        print(f"Backup failed: {e}")

# Example usage
source_directory = '/path/to/source'
destination_directory = '/path/to/backup/destination'
backup_directory(source_directory, destination_directory)
