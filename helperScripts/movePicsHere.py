#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime, timedelta
import shutil
import sys

# Source folder: ~/Downloads
downloads_dir = Path.home() / "Downloads"

# Destination folder: current working directory
destination_dir = Path.cwd()

# Allowed image extensions
allowed_extensions = {".png", ".jpeg", ".jpg", ".webp"}

# Files created/modified within last 24 hours
cutoff = datetime.now() - timedelta(hours=48)

if not downloads_dir.exists():
    print(f"Downloads folder not found: {downloads_dir}")
    sys.exit(1)

moved_count = 0

for file_path in downloads_dir.iterdir():
    if not file_path.is_file():
        continue

    if file_path.suffix.lower() not in allowed_extensions:
        continue

    # On many systems, true creation time is not portable.
    # st_mtime (last modified time) is the most reliable cross-platform choice.
    file_time = datetime.fromtimestamp(file_path.stat().st_mtime)

    if file_time >= cutoff:
        destination_path = destination_dir / file_path.name

        # Avoid overwriting existing files
        if destination_path.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            counter = 1
            while True:
                candidate = destination_dir / f"{stem}_{counter}{suffix}"
                if not candidate.exists():
                    destination_path = candidate
                    break
                counter += 1

        shutil.move(str(file_path), str(destination_path))
        print(f"Moved: {file_path} -> {destination_path}")
        moved_count += 1

print(f"\nDone. Moved {moved_count} file(s).")
