from pathlib import Path


def ng_static_dir(base_dir: Path):
    options = [base_dir / 'ng_static', base_dir.parent / 'frontend/dist/frontend']
    return next((d for d in options if d.exists()), None)
