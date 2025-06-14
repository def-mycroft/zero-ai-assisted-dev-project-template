from __future__ import annotations

from pathlib import Path
import shutil


def _copytree(src: Path, dst: Path) -> None:
    """Copy ``src`` to ``dst`` ignoring git metadata."""
    ignore = shutil.ignore_patterns('.git', '__pycache__', '*.pyc', '*.pyo')
    shutil.copytree(src, dst, ignore=ignore)


def _replace_in_file(path: Path, old: str, new: str) -> None:
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return
    updated = text.replace(old, new)
    hy_old = old.replace('_', '-')
    hy_new = new.replace('_', '-')
    updated = updated.replace(hy_old, hy_new)
    if updated != text:
        path.write_text(updated, encoding='utf-8')


def duplicate_project(target_dir: Path, package_name: str) -> Path:
    """Duplicate this project to ``target_dir`` with a new package name.

    Parameters
    ----------
    target_dir:
        Destination directory for the new project.
    package_name:
        Desired package/module name for the new project.
    """
    src_root = Path(__file__).resolve().parents[1]
    target_dir = Path(target_dir)
    if target_dir.exists():
        raise FileExistsError(target_dir)

    _copytree(src_root, target_dir)

    old_pkg = target_dir / 'zero_aidev_framework'
    new_pkg = target_dir / package_name
    old_pkg.rename(new_pkg)

    for path in target_dir.rglob('*'):
        if path.is_file():
            if path.suffix in {'.py', '.toml', '.md'}:
                _replace_in_file(path, 'zero_aidev_framework', package_name)

    cli_link = target_dir / 'cli.py'
    if cli_link.exists():
        if cli_link.is_symlink() or cli_link.is_file():
            cli_link.unlink()
        elif cli_link.is_dir():
            shutil.rmtree(cli_link)
    cli_link.symlink_to(Path(package_name) / 'cli.py')

    return target_dir


__all__ = ['duplicate_project']
