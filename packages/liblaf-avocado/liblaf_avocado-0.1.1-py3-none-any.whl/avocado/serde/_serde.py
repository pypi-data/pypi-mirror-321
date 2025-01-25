import os
from collections.abc import Callable
from pathlib import Path
from typing import Any

import avocado as ac

_READERS: dict[str, Callable[..., Any]] = {
    ".json": ac.load_json,
    ".toml": ac.load_toml,
    ".yaml": ac.load_yaml,
    ".yml": ac.load_yaml,
}


_WRITERS: dict[str, Callable[..., None]] = {
    ".json": ac.save_json,
    ".toml": ac.save_toml,
    ".yaml": ac.save_yaml,
    ".yml": ac.save_yaml,
}


def serialize(
    fpath: str | os.PathLike[str], data: Any, *, ext: str | None = None
) -> None:
    fpath: Path = Path(fpath)
    if ext is None:
        ext = fpath.suffix
    if ext not in _WRITERS:
        msg: str = f"Unsupported file extension: {ext}"
        raise ValueError(msg)
    writer = _WRITERS[ext]
    fpath.parent.mkdir(parents=True, exist_ok=True)
    writer(fpath, data)


def deserialize(fpath: str | os.PathLike[str], *, ext: str | None = None) -> Any:
    fpath: Path = Path(fpath)
    if ext is None:
        ext = fpath.suffix
    if ext not in _READERS:
        msg: str = f"Unsupported file extension: {ext}"
        raise ValueError(msg)
    reader = _READERS[ext]
    return reader(fpath)
