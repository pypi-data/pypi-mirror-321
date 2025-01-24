import filecmp
import shutil
import subprocess
import tempfile
from pathlib import Path

from minecraft_assets import get_asset_root


def compare_directories(dir1, dir2):
    """Compare two directories recursively to ensure they are identical.

    Returns (is_identical, mismatch_message)
    """
    dirs_cmp = filecmp.dircmp(dir1, dir2)

    if dirs_cmp.left_only or dirs_cmp.right_only or dirs_cmp.diff_files:
        msg = []
        if dirs_cmp.left_only:
            msg.append(f"Files only in {dir1}: {dirs_cmp.left_only}")
        if dirs_cmp.right_only:
            msg.append(f"Files only in {dir2}: {dirs_cmp.right_only}")
        if dirs_cmp.diff_files:
            msg.append(f"Different files: {dirs_cmp.diff_files}")
        return False, "\n".join(msg)

    for common_dir in dirs_cmp.common_dirs:
        is_identical, msg = compare_directories(Path(dir1) / common_dir, Path(dir2) / common_dir)
        if not is_identical:
            return False, msg

    return True, ""


def test_update_assets():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as temp_dir:
        script_dir = Path(temp_dir) / "script"
        target_dir = Path(temp_dir) / "target"

        # Copy update script to temporary location
        script_dir.mkdir()
        shutil.copy2(
            Path(__file__).parent.parent / "update-assets.sh", script_dir / "update-assets.sh"
        )

        # Make script executable
        (script_dir / "update-assets.sh").chmod(0o755)  # nosec S103

        # Run the update script with custom target directory
        subprocess.run(  # nosec S603
            ["./update-assets.sh", str(target_dir)], cwd=script_dir, check=True
        )

        # Get the reference asset directory
        reference_dir = Path(get_asset_root())

        # Compare directories
        is_identical, msg = compare_directories(reference_dir, target_dir)

        assert is_identical, f"Directories are not identical:\n{msg}"
