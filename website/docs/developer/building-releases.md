---
sidebar_position: 5
---

# Building Releases

This guide covers building distributable versions of CSV to QLab for macOS using PyInstaller.

:::info Intended Audience
This guide is for maintainers and contributors who need to build release versions of the GUI application. End users should download pre-built releases from [GitHub Releases](https://github.com/fross123/csv_to_qlab/releases).
:::

## Prerequisites

### System Requirements
- macOS (for building .app bundles)
- Python 3.8 or later
- Git

### Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fross123/csv_to_qlab.git
   cd csv_to_qlab
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install pyinstaller
   ```

## Building with PyInstaller

### Understanding `application.spec`

The `application.spec` file defines how PyInstaller bundles the application. Key sections:

**Data Files** (lines 9-12):
```python
datas=[
    ('app/static', 'static'),        # Web UI assets
    ('app/templates', 'templates'),  # Flask templates
    ('app/qlab_osc_config.json', '.'),  # OSC configuration (REQUIRED!)
]
```

**Application Settings** (lines 42-57):
- **name**: `csv-to-qlab.app`
- **icon**: `icon.icns` (must be in root directory)
- **console**: `False` (GUI application, not terminal)

:::warning Critical Files
The `qlab_osc_config.json` file **must** be included in the bundle, or the application won't be able to send OSC messages to QLab!
:::

### Build Process

1. **Verify you're in the project root:**
   ```bash
   pwd  # Should show .../csv_to_qlab
   ```

2. **Run PyInstaller:**
   ```bash
   pyinstaller application.spec
   ```

3. **Build output:**
   - **`dist/csv-to-qlab/`** - Intermediate build files
   - **`dist/csv-to-qlab.app/`** - Final macOS application bundle

4. **Build artifacts:**
   - **`build/`** - Temporary build files (can be deleted)
   - **`dist/`** - Final application bundle

### Testing the Build

Before distributing, thoroughly test the bundled application:

1. **Launch the app:**
   ```bash
   open dist/csv-to-qlab.app
   ```

2. **Verify functionality:**
   - Application launches without errors
   - All UI elements render correctly
   - File upload works
   - OSC messages send to QLab successfully
   - Error handling works properly

3. **Test with example files:**
   ```bash
   # Use the example CSV files in app/static/example_file/
   ```

4. **Check for missing resources:**
   - Look for "file not found" errors in Console.app
   - Verify all static assets load
   - Confirm templates render

### Common Build Issues

#### Missing Icon File
**Error:** `FileNotFoundError: icon.icns`

**Solution:** Ensure `icon.icns` exists in the project root:
```bash
ls icon.icns  # Should show the file
```

#### Missing OSC Config
**Symptom:** Application launches but fails to send cues

**Solution:** Verify `qlab_osc_config.json` is in the bundle:
```bash
# Check bundle contents
ls dist/csv-to-qlab.app/Contents/MacOS/qlab_osc_config.json
```

If missing, check `application.spec` line 12.

#### Import Errors
**Error:** `ModuleNotFoundError` when running bundled app

**Solution:** Add missing modules to `hiddenimports` in `application.spec`:
```python
hiddenimports=['module_name'],
```

## Creating Distribution Packages

### DMG Creation (macOS)

For official releases, package the .app into a DMG:

1. **Install create-dmg** (if not already installed):
   ```bash
   brew install create-dmg
   ```

2. **Create DMG:**
   ```bash
   create-dmg \
     --volname "CSV to QLab" \
     --window-pos 200 120 \
     --window-size 600 400 \
     --icon-size 100 \
     --app-drop-link 425 120 \
     "CSV-To-QLab.dmg" \
     "dist/csv-to-qlab.app"
   ```

3. **Test the DMG:**
   - Mount the DMG
   - Drag app to Applications
   - Launch and verify functionality

### Multi-Architecture Builds

For distributing to both Intel and Apple Silicon Macs:

**Intel Mac (x86_64):**
```bash
arch -x86_64 pyinstaller application.spec
```

**Apple Silicon (ARM):**
```bash
arch -arm64 pyinstaller application.spec
```

:::tip Build on Target Architecture
For best compatibility, build on the target architecture:
- Build Intel version on Intel Mac (or with Rosetta)
- Build ARM version on Apple Silicon Mac
:::

## Release Checklist

Before publishing a release:

- [ ] All tests passing (`pytest`)
- [ ] Version number updated in relevant files
- [ ] CHANGELOG.md updated
- [ ] Application builds without errors
- [ ] Bundled app tested on clean macOS installation
- [ ] Example CSV files work correctly
- [ ] Documentation updated
- [ ] Release notes written
- [ ] DMG created and tested
- [ ] GitHub release created with DMG attached

## GitHub Actions (Future)

:::note Automation Opportunity
Consider setting up GitHub Actions to automatically build releases for multiple architectures when tags are pushed. See `.github/workflows/` for existing CI/CD setup.
:::

## Troubleshooting Build Issues

### Clean Build
If you encounter persistent issues, try a clean build:

```bash
# Remove build artifacts
rm -rf build dist *.spec~

# Rebuild
pyinstaller application.spec
```

### Verbose Output
For debugging build issues:

```bash
pyinstaller --log-level DEBUG application.spec
```

### Check Dependencies
Ensure all dependencies are properly installed:

```bash
pip list | grep -E "Flask|pywebview|python-osc"
```

## Development Workflow

For rapid development and testing:

1. **Use the source directly** (not bundled):
   ```bash
   python app/application.py
   ```

2. **Only build when:**
   - Testing distribution-specific issues
   - Preparing for release
   - Verifying bundling of new resources

3. **Use editable install for CLI development:**
   ```bash
   pip install -e .
   ```

## Further Reading

- [PyInstaller Documentation](https://pyinstaller.org/en/stable/)
- [PyInstaller macOS Bundle](https://pyinstaller.org/en/stable/usage.html#macos-specific-options)
- [Code Signing macOS Apps](https://developer.apple.com/developer-id/) (for official distribution)

## Questions?

If you encounter issues building releases, please:
1. Check this documentation
2. Search [existing issues](https://github.com/fross123/csv_to_qlab/issues)
3. Open a [new issue](https://github.com/fross123/csv_to_qlab/issues/new) with build logs
