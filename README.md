# CSV to QLab

[![Tests](https://github.com/fross123/csv_to_qlab/workflows/Tests/badge.svg)](https://github.com/fross123/csv_to_qlab/actions)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A tool to send CSV files to QLab via OSC. Available as both a GUI application and command-line interface.

[📖 Full Documentation](https://fross123.github.io/csv_to_qlab/) | [🐛 Report Bug](https://github.com/fross123/csv_to_qlab/issues) | [💡 Request Feature](https://github.com/fross123/csv_to_qlab/issues)

## Features

✨ **Dual Interface** - GUI application for Mac and cross-platform CLI
📝 **Configuration-Driven** - Easy to extend with JSON-based OSC property definitions
🎯 **Comprehensive Support** - Supports all major QLab cue types and properties
🤖 **Automation Ready** - CLI with JSON output for scripting and batch processing
✅ **Well Tested** - 69 tests with 86% code coverage
📚 **Documented** - Extensive user and developer documentation

## Installation

### GUI Application (Mac only)

Download the latest release:
- [macOS 15 ARM](https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab-macOS15-ARM.dmg)
- [macOS 14 ARM](https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab-macOS14-ARM.dmg)
- [macOS 11+ Intel](https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab.dmg)

**Note:** I do not currently have an Apple Developer Certificate, so you'll see security warnings when opening the app. The code is open source and auditable. If you have concerns, you can build from source or use the CLI.

**Setup:**
1. Download and open the DMG
2. Drag the app to your Applications folder
3. Right-click the app and select "Open" to bypass Gatekeeper
4. QLab must be open on the receiving computer for messages to be received

### Command-Line Interface (Cross-platform)

The CLI works on Mac, Linux, and Windows - ideal for automation and scripting.

```bash
# Clone the repository
git clone https://github.com/fross123/csv_to_qlab.git
cd csv_to_qlab

# Install CLI-only (recommended)
pip install .

# Or install with GUI support
pip install .[gui]
```

**Basic Usage:**
```bash
# Send a CSV file to QLab
csv-to-qlab show.csv 127.0.0.1 5

# With passcode
csv-to-qlab show.csv 192.168.1.100 5 --passcode 1234

# JSON output for scripting
csv-to-qlab show.csv 127.0.0.1 5 --json

# See all options
csv-to-qlab --help
```

**When to Use GUI vs CLI:**
- **GUI**: Quick one-off imports, visual feedback, Mac users
- **CLI**: Automation, scripting, batch processing, remote/SSH sessions, cross-platform

## CSV File Format

### Required Columns
Every CSV file must have these three columns:

| Number | Type | Name |
|--------|------|------|
| 12 | audio | Cue 12 GO |
| 13 | video | Video Playback |

### Optional Columns

CSV to QLab supports a wide range of optional properties for all cue types:

**Global Properties** (all cue types):
- Notes, Color, Follow (Continue Mode)
- Armed, Flagged, Auto Load
- Duration, Pre Wait, Post Wait
- Target, File Target

**Audio/Video Cues:**
- Level, Rate, Pitch
- Loop, Infinite Loop
- Start Time, End Time
- Patch, Gang

**MIDI Cues:**
- MIDI Device ID, Message Type
- Control Number, Control Value
- Patch Channel, Patch Number
- MSC Command, Command Format

**Network Cues:**
- QLab 4: Message Type, OSC Cue Number, Command
- QLab 5: Network Patch Number/Channel, Custom String

**Fade Cues:**
- Fade opacity, Do opacity
- Fade and Stop Others

**[📖 Complete CSV Column Reference](https://fross123.github.io/csv_to_qlab/docs/reference/csv-columns)**

### Examples

- [Simple Example](https://github.com/fross123/csv_to_qlab/blob/main/app/static/example_file/simple.csv)
- [Full Example with Multiple Cue Types](https://github.com/fross123/csv_to_qlab/blob/main/app/static/example_file/example.csv)

## Documentation

**User Documentation:**
- [Installation Guide](https://fross123.github.io/csv_to_qlab/docs/tutorial-basics/installation)
- [Preparing CSV Files](https://fross123.github.io/csv_to_qlab/docs/tutorial-basics/prepare-csv-file)
- [Sending to QLab](https://fross123.github.io/csv_to_qlab/docs/tutorial-basics/send-to-qlab)
- [CLI Advanced Usage](https://fross123.github.io/csv_to_qlab/docs/tutorial-basics/cli-advanced)

**Developer Documentation:**
- [Architecture Overview](https://fross123.github.io/csv_to_qlab/docs/developer/architecture)
- [Adding Properties](https://fross123.github.io/csv_to_qlab/docs/developer/adding-properties)
- [OSC Config Schema](https://fross123.github.io/csv_to_qlab/docs/developer/osc-config-schema)
- [Testing Guide](https://fross123.github.io/csv_to_qlab/docs/developer/testing)
- [Building Releases](https://fross123.github.io/csv_to_qlab/docs/developer/building-releases)

## Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, improving documentation, or adding new cue properties.

### Getting Started

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/csv_to_qlab.git
   cd csv_to_qlab
   ```

3. **Set up development environment:**
   ```bash
   # Create virtual environment
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Install in editable mode
   pip install -e .
   ```

4. **Create a feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```

5. **Make your changes and test:**
   ```bash
   # Run tests
   pytest

   # Run with coverage
   pytest --cov=app --cov-report=html

   # Run spellcheck
   pyspelling -c .spellcheck.yml
   ```

6. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request** on GitHub

### Development Quick Start

**Run GUI from source:**
```bash
python app/application.py
```

**Run CLI from source:**
```bash
# After pip install -e .
csv-to-qlab path/to/file.csv 127.0.0.1 5

# Or run directly
python app/cli.py path/to/file.csv 127.0.0.1 5
```

**Run tests:**
```bash
pytest                           # All tests
pytest app/tests/test_cli.py    # Specific test file
pytest -v                        # Verbose output
pytest --cov=app                # With coverage
```

**Build documentation:**
```bash
cd website
npm install
npm run build
npm run serve  # Preview locally
```

### Adding New OSC Properties

Thanks to the configuration-driven architecture, adding new properties is easy - no Python code required!

1. Add the property to `app/qlab_osc_config.json`
2. Add tests to `app/tests/test_osc_config.py`
3. Update documentation in `website/docs/reference/csv-columns.md`

See the [Adding Properties Guide](https://fross123.github.io/csv_to_qlab/docs/developer/adding-properties) for detailed instructions.

### Building for Distribution

**macOS Application:**
```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller application.spec

# Output: dist/csv-to-qlab.app
```

See [Building Releases](https://fross123.github.io/csv_to_qlab/docs/developer/building-releases) for multi-architecture builds and DMG creation.

## Project Structure

```
csv_to_qlab/
├── app/
│   ├── application.py           # Flask GUI application
│   ├── cli.py                   # Command-line interface
│   ├── csv_parser.py            # Core CSV processing
│   ├── osc_config.py            # OSC configuration loader
│   ├── osc_server.py            # OSC response handler
│   ├── qlab_osc_config.json     # OSC property definitions
│   └── tests/                   # Test suite
├── website/                     # Documentation (Docusaurus)
├── setup.py                     # Package configuration
├── requirements.txt             # Python dependencies
└── application.spec             # PyInstaller config

```

## Testing

The project has comprehensive test coverage across all major components:

```bash
# Run all tests
pytest

# Run specific test categories
pytest app/tests/test_cli.py              # CLI tests
pytest app/tests/test_csv_parser.py       # CSV parsing tests
pytest app/tests/test_osc_config.py       # Configuration tests

# Run with coverage report
pytest --cov=app --cov-report=html

# View coverage
open htmlcov/index.html
```

**Test Coverage:** 86% (69 tests)

## Troubleshooting

**GUI won't open on Mac:**
- Right-click the app and select "Open"
- Go to System Preferences → Security & Privacy → Click "Open Anyway"

**CLI command not found:**
- Ensure pip's bin directory is in your PATH
- Try running: `python -m app.cli` instead

**Cues not appearing in QLab:**
- Verify QLab is running with a workspace open
- Check the IP address is correct (use `127.0.0.1` for local)
- Ensure firewall isn't blocking port 53000

**More help:** See [Troubleshooting Guide](https://fross123.github.io/csv_to_qlab/docs/tutorial-basics/send-to-qlab#troubleshooting)

## Credits

Created and maintained by [Finlay Ross](https://github.com/fross123)

Built with:
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [PyWebView](https://pywebview.flowrl.com/)
- [python-osc](https://pypi.org/project/python-osc/)
- [Docusaurus](https://docusaurus.io/)

## License

This project is licensed under the GNU General Public License v3.0 - see the [COPYING](COPYING) file for details.

## Feedback

Recommendations for future features are very welcome! Please:
- [Open an issue](https://github.com/fross123/csv_to_qlab/issues/new) for bugs or feature requests
- [Start a discussion](https://github.com/fross123/csv_to_qlab/discussions) for questions or ideas
- Contribute directly with a pull request

---

**Made with ❤️ for the theatre community**
