---
sidebar_position: 3
---

# Send to QLab

Follow these steps to send your prepared CSV file to QLab. Instructions are provided for both the GUI application and command-line interface.

## Prerequisites

Before sending your CSV file, make sure you have:

1. **QLab is running** - Open QLab with a workspace ready
2. **CSV file is prepared** - See [Prepare a CSV File](/docs/tutorial-basics/prepare-csv-file)
3. **Know your QLab version** - QLab 4 or 5
4. **Know the IP address** - See below

:::note QLab Version Support
CSV to QLab works with both QLab 4 and QLab 5, though some features are only available on QLab 5.
:::

### Finding the IP Address

You'll need the IP address of the machine running QLab:

- **Same computer**: Use `127.0.0.1` (localhost)
- **Different computer on network**:
  - **Mac**: System Preferences → Network → Look for "IP Address"
  - **Windows**: Open Command Prompt → Type `ipconfig` → Look for "IPv4 Address"
  - **Linux**: Terminal → Type `ip addr` or `ifconfig`

### OSC Passcode (Optional)

If your QLab workspace has an OSC passcode:
- Find it in QLab: Settings/Preferences → OSC → Passcode
- Make sure the passcode has full access to the workspace
- On QLab 5, you can also use the "no passcode" option

---

## Using the GUI Application

### 1. Open CSV to QLab

Launch the CSV to QLab application on your Mac.

### 2. Select QLab Version

Choose QLab 4 or 5 from the dropdown. QLab 5 handles some incoming messages slightly differently.

### 3. Enter Passcode (If Required)

If your QLab workspace uses an OSC passcode:
- Check the passcode checkbox
- Enter the passcode from QLab settings

:::tip
It's also possible to bypass this step in QLab 5 by allowing access with the "no passcode" option.
:::

### 4. Enter IP Address

Enter the IP address of the machine running QLab:
- `127.0.0.1` if running locally
- Network IP like `192.168.1.100` if on a different machine

### 5. Select Your CSV File

Click "Choose File" and select your prepared CSV file.

### 6. Submit

Click the submit button and keep the QLab workspace open.

### 7. Success!

You should see a success page and your cues will appear in QLab!

![Success Page](/img/funny-success-quote-1-picture-quote-1.jpg)

---

## Using the CLI

### Basic Usage

Open your terminal and run:

```bash
csv-to-qlab your-file.csv 127.0.0.1 5
```

Replace with your values:
- `your-file.csv` - Path to your CSV file
- `127.0.0.1` - IP address of QLab machine
- `5` - QLab version (4 or 5)

### With Passcode

If your QLab workspace requires a passcode:

```bash
csv-to-qlab your-file.csv 192.168.1.100 5 --passcode 1234
```

### Verbose Output

See detailed progress information:

```bash
csv-to-qlab your-file.csv 127.0.0.1 5 --verbose
```

Example output:
```
Sending CSV file: your-file.csv
QLab IP: 127.0.0.1
QLab version: 5

✓ Successfully processed 55 cue(s)
```

### JSON Output (For Automation)

Perfect for scripts and automation:

```bash
csv-to-qlab your-file.csv 127.0.0.1 5 --json
```

### More CLI Options

For advanced usage including batch processing, automation, and scripting, see the [CLI Advanced](/docs/tutorial-basics/cli-advanced) documentation.

---

## Troubleshooting

### No Cues Appearing in QLab

- Verify QLab is running and a workspace is open
- Check that the IP address is correct
- Ensure your firewall isn't blocking connections
- Try using `127.0.0.1` if running on the same machine

### Passcode Errors

- Double-check the passcode in QLab settings (Settings → OSC → Passcode)
- Ensure the passcode has full workspace access
- Try the "no passcode" option in QLab 5 if available

### CSV Format Errors

- Verify your CSV has the required columns: **Number**, **Type**, **Name**
- Check the [CSV Column Reference](/docs/reference/csv-columns) for proper formatting
- Try with a [simple example file](https://github.com/fross123/csv_to_qlab/blob/main/app/static/example_file/simple.csv) first

### Network Issues

- Ensure both machines are on the same network
- Test connectivity: `ping [IP_ADDRESS]`
- Check firewall settings on both machines
- Verify QLab's OSC settings allow incoming connections

### Connection Refused

- Make sure QLab is running before sending the CSV
- Check that OSC is enabled in QLab preferences
- Verify the port is 53000 (default for QLab)

---

## Next Steps

- Learn about [all available CSV columns](/docs/reference/csv-columns)
- Explore [CLI automation and batch processing](/docs/tutorial-basics/cli-advanced)
- Check out the [example CSV files](https://github.com/fross123/csv_to_qlab/tree/main/app/static/example_file)

:::tip
If you encounter an error not listed here, please submit an [issue on GitHub](https://github.com/fross123/csv_to_qlab/issues/new/choose). We're here to help!
:::
