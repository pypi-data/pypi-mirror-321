# minecraft-assets

Python wrapper for [PrismarineJS/minecraft-assets](https://github.com/PrismarineJS/minecraft-assets).

## Installation

This package requires Python 3.9 or higher, and supports Python versions up to 3.13.

First, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

Install the package:
```bash
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Usage

```python
from minecraft_assets import get_asset_root, get_asset_dir

# Get the root assets directory
assets_root = get_asset_root()
print(assets_root)  # Path to the root assets directory

# Get assets directory for a specific version
version_dir = get_asset_dir("1.20.4")
print(version_dir)  # Path to version-specific assets

# Will raise MinecraftVersionError if version doesn't exist
try:
    invalid_dir = get_asset_dir("9.99.99")
except MinecraftVersionError as e:
    print(f"Error: {e}")
```

The package provides functions to access Minecraft asset directories. Each version's directory contains the raw asset files from the corresponding Minecraft version.

## Development

This project uses:
- [ruff](https://github.com/astral-sh/ruff) for linting and formatting
- [pytest](https://docs.pytest.org/) for testing
- [setuptools](https://setuptools.pypa.io/) for building

### Updating Minecraft Assets

The package includes a script to update the Minecraft assets from the upstream repository:

```bash
# Make the script executable (first time only)
chmod +x update-assets.sh

# Run the script
./update-assets.sh

# Or specify a custom target directory
./update-assets.sh path/to/custom/dir
```

The script will:
1. Clone the PrismarineJS/minecraft-assets repository
2. Checkout the specified version (currently 1.13.0)
3. Copy the assets to the appropriate directory
4. Clean up temporary files

After running the script, commit the changes and update the version number accordingly.

### Make Commands

Remember to activate your virtual environment before running these commands:

```bash
make format     # Format code using ruff
make lint       # Run linting checks
make test       # Run tests
make clean      # Clean build artifacts and virtual environment
```

### Version Strategy

This package follows the version numbers of the upstream minecraft-assets repository, with the addition of release candidate suffixes (e.g., `1.21.0rc1`) during development. Once a version is thoroughly tested, it will be released with the matching version number from minecraft-assets. 

### Updating to a New Version

To update the package to track a new version of minecraft-assets, follow these steps:

1. Find the closest previous version
   ```bash
   # Example: For updating to 1.13.1, look for:
   # - 1.13.0 (closest)
   # - 1.12.x (fallback)
   git clone https://github.com/PrismarineJS/minecraft-assets.git
   cd minecraft-assets
   git tag | sort -V
   ```

2. Create a feature branch
   ```bash
   git checkout -b v1.13.1rc
   ```

3. Update version references:
   - In `update-assets.sh`:
     ```bash
     # Change MINECRAFT_ASSETS_VERSION
     MINECRAFT_ASSETS_VERSION="1.13.1"
     ```

   - In `src/minecraft_assets/__init__.py`:
     ```python
     __version__ = "1.13.1rc0"
     ```

   - In `tests/test_assets.py`:
     ```python
     SUPPORTED_VERSIONS = [
         # ... existing minecraft versions ...
         "1.21.5",  # Add newly supported Minecraft versions if needed
     ]
     ```

   - In `tests/test_version.py`:
     ```python
     def test_version():
         cleaned_version = __version__.split("rc")[0]
         assert cleaned_version == "1.13.1"
     ```

4. Run the update script:
   ```bash
   ./update-assets.sh
   ```

5. Test and commit changes:
   ```bash
   make test
   make lint
   git commit -am "Update to minecraft-assets 1.13.1rc0"
   git push origin v1.13.1rc
   ```

6. Once testing is complete:
   ```bash
   # Create release branch
   git checkout -b v1.13.1

   # Commit and push
   git push origin v1.13.1
   ```

7. Create a release on GitHub using the v1.13.1 tag

Remember to update the package version in your dependent projects after releasing.

### Building Distributions

To build both source distribution (sdist) and wheel distribution (bdist_wheel):

```bash
python -m build
```

This will create:
- A source distribution (.tar.gz) in the `dist/` directory
- A wheel distribution (.whl) in the `dist/` directory

### Validating Distribution Contents

To inspect the contents of the source distribution:
```bash
tar tzf dist/*.tar.gz  # List contents without extracting
# or
tar xzf dist/*.tar.gz -C /tmp  # Extract to /tmp for inspection
```

To inspect the wheel distribution (which is a ZIP file):
```bash
unzip -l dist/*.whl  # List contents without extracting
# or
unzip dist/*.whl -d /tmp  # Extract to /tmp for inspection
```

To clean all build artifacts and start fresh:
```bash
make clean
```

## License

See [LICENSE](LICENSE) for more information.
