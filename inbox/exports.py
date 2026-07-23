from datetime import datetime
from pathlib import Path


EXPORTS_ROOT = Path("exports")


def timestamp_now():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def build_export_path(file_name, subfolder):
    export_dir = EXPORTS_ROOT / subfolder
    export_dir.mkdir(parents=True, exist_ok=True)
    return str(export_dir / file_name)
