#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime, timedelta
import shutil
import sys

downloads = Path.home() / "Downloads"
destination = Path.cwd()
cutoff = datetime.now() - timedelta(hours=72)

if not downloads.exists():
    print(f"Downloads folder not found: {downloads}")
    sys.exit(1)

moved = 0

for file_path in downloads.glob("*.mp4"):
    try:
        created_time = datetime.fromtimestamp(file_path.stat().st_birthtime)
    except AttributeError:
        # Fallback if creation time is unavailable
        created_time = datetime.fromtimestamp(file_path.stat().st_mtime)

    if created_time >= cutoff:
        target = destination / file_path.name

        # Avoid overwriting an existing file
        if target.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            counter = 1
            while target.exists():
                target = destination / f"{stem}_{counter}{suffix}"
                counter += 1

        shutil.move(str(file_path), str(target))
        print(f"Moved: {file_path.name} -> {target.name}")
        moved += 1

print(f"Done. Moved {moved} file(s).")