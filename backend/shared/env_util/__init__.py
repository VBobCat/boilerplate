import json
import os
from pathlib import Path

from dotenv import load_dotenv

FALSEY_STRINGS = ('0', 'false', 'off', 'no', 'none', 'null')


def initenv(base_dir: Path | os.PathLike[str] | str):
    if not isinstance(base_dir, Path):
        base_dir = Path(base_dir)
    env_path = base_dir / '.env'
    if env_path.exists() and env_path.is_file():
        load_dotenv(env_path)


def getenv(key: str, default: str = None):
    os_var = os.getenv(key)
    if os_var is not None:
        return os_var
    return default


def getenv_bool(key: str, default: bool = None):
    envvar = str(getenv(key)).casefold().strip()
    return default if envvar is None else (bool(envvar) and envvar not in FALSEY_STRINGS)


def getenv_json(key: str, default=None):
    envvar = getenv(key)
    return default if envvar is None else json.loads(envvar)
