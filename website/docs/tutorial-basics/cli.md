---
sidebar_position: 4
---

# Command-Line Interface (CLI)

The CLI provides a cross-platform, terminal-based interface for sending CSV files to QLab. It's ideal for automation, scripting, batch processing, and remote/SSH sessions.

:::tip When to Use CLI vs GUI
- **Use CLI**: Automation, scripting, batch processing, remote/SSH sessions, cross-platform (Linux/Windows/Mac)
- **Use GUI**: Quick one-off imports, visual feedback preferred, Mac users
:::

## Installation

### Requirements
- Python 3.8 or later
- pip (Python package installer)

### Install CLI-Only (Recommended)
This installs just the CLI without GUI dependencies:

```bash
# Clone the repository
git clone https://github.com/fross123/csv_to_qlab.git
cd csv_to_qlab

# Install
pip install .
```

### Install with GUI Support
If you also want to run the GUI application from source:

```bash
pip install .[gui]
```

### Verify Installation
```bash
csv-to-qlab --help
```

## Basic Usage

### Simple Example
Send a CSV file to QLab running on the same machine:

```bash
csv-to-qlab show.csv 127.0.0.1 5
```

- `show.csv` - Path to your CSV file
- `127.0.0.1` - IP address of QLab machine
- `5` - QLab version (4 or 5)

### With Passcode
If your QLab workspace requires a passcode:

```bash
csv-to-qlab show.csv 192.168.1.100 5 --passcode 1234
```

## Output Modes

### Human-Readable Output (Default)
Shows a summary of successes and errors:

```bash
csv-to-qlab show.csv 127.0.0.1 5
```

Output:
```
✓ Successfully processed 55 cue(s)
```

### Verbose Mode
Shows detailed information during processing:

```bash
csv-to-qlab show.csv 127.0.0.1 5 --verbose
```

Output:
```
Sending CSV file: show.csv
QLab IP: 127.0.0.1
QLab version: 5
Using passcode: ****

✓ Successfully processed 55 cue(s)
```

### Quiet Mode
Suppresses success messages, only shows errors:

```bash
csv-to-qlab show.csv 127.0.0.1 5 --quiet
```

### JSON Output
Perfect for scripting and automation:

```bash
csv-to-qlab show.csv 127.0.0.1 5 --json
```

Output:
```json
{
  "success": [
    {
      "status": "ok",
      "message": "/reply/new: ..."
    }
  ],
  "errors": [],
  "has_errors": false
}
```

## Command-Line Arguments

### Positional Arguments (Required)
- `csv_file` - Path to CSV file containing cue data
- `ip` - IP address of QLab machine (e.g., 127.0.0.1 or 192.168.1.100)
- `qlab_version` - QLab version: either 4 or 5

### Optional Arguments
- `-p, --passcode PASSCODE` - QLab workspace passcode
- `-v, --verbose` - Enable verbose output
- `-q, --quiet` - Suppress success messages, only show errors
- `-j, --json` - Output results in JSON format
- `-h, --help` - Show help message and exit

## Automation Examples

### Batch Processing Multiple Files
Process multiple CSV files in sequence:

```bash
#!/bin/bash
for file in cues/*.csv; do
    csv-to-qlab "$file" 127.0.0.1 5 --quiet
    if [ $? -ne 0 ]; then
        echo "Error processing $file"
    fi
done
```

### Integration with Scripts
Use JSON output for programmatic processing:

```bash
#!/bin/bash
result=$(csv-to-qlab show.csv 127.0.0.1 5 --json)
has_errors=$(echo "$result" | jq -r '.has_errors')

if [ "$has_errors" = "true" ]; then
    echo "Errors occurred during processing"
    echo "$result" | jq -r '.errors[]'
    exit 1
fi

echo "Success!"
```

### Watch Directory for Changes
Automatically process CSV files when they appear in a directory:

```bash
#!/bin/bash
# Requires inotifywait (Linux) or fswatch (macOS)

# macOS
fswatch -o ~/cue_drops | while read; do
    for file in ~/cue_drops/*.csv; do
        csv-to-qlab "$file" 127.0.0.1 5 --quiet
        mv "$file" ~/cue_drops/processed/
    done
done
```

### Remote Execution via SSH
Run the CLI on a remote machine:

```bash
ssh user@server "csv-to-qlab /path/to/show.csv 127.0.0.1 5"
```

## Exit Codes

The CLI uses standard exit codes for automation:

- `0` - Success (no errors occurred)
- `1` - Error (file not found, processing errors, etc.)

Use in scripts:
```bash
if csv-to-qlab show.csv 127.0.0.1 5 --quiet; then
    echo "Success!"
else
    echo "Failed with exit code $?"
fi
```

## Troubleshooting

### Command Not Found
If `csv-to-qlab` command is not found after installation:

1. Check if pip's bin directory is in your PATH:
   ```bash
   python -m pip show csv-to-qlab
   ```

2. Try running directly:
   ```bash
   python -m app.cli show.csv 127.0.0.1 5
   ```

### Module Not Found Errors
Ensure python-osc is installed:

```bash
pip install python-osc
```

### Connection Errors
- Verify QLab is running on the target machine
- Check that OSC is enabled in QLab preferences
- Ensure the IP address is correct
- Verify network connectivity: `ping [IP_ADDRESS]`

### CSV Format Errors
- Ensure your CSV has the required columns (Number, Type, Name)
- Check that column headers match the [CSV Column Reference](/docs/reference/csv-columns)
- Verify the CSV is properly formatted (no extra quotes, commas, etc.)

## Development Mode

For development, install in editable mode:

```bash
# Clone and navigate to repository
git clone https://github.com/fross123/csv_to_qlab.git
cd csv_to_qlab

# Install in editable mode
pip install -e .

# Run directly from source
python app/cli.py show.csv 127.0.0.1 5
```

This allows you to modify the code and test changes immediately without reinstalling.

## Next Steps

- Learn about [CSV file formatting](/docs/tutorial-basics/prepare-csv-file)
- See [CSV Column Reference](/docs/reference/csv-columns) for all available properties
- Check out [automation examples](https://github.com/fross123/csv_to_qlab/tree/main/examples) (coming soon)
