# CSV to QLAB

## To run on mac:
- download [csv_to_qlab.dmg](https://github.com/fross123/csv_to_qlab/releases/latest/download/CSV-To-QLab.dmg) from the latest release
- unzip the foder
- open the app
    - *qlab must be open on the recieving computer in order for the messages to be recieved.*

**Please note that I do not currently have an Apple Developer Certificate and therefore there will be some scary warnings when trying to run this application locally. It is entirely up to you to decide to run this application. If you have concerns with the bundled application releases, I suggest cloning or forking the repository.**


## How to format your csv file:

Some columns are required, some are optional.

### Required columns
- Number
- Type
- Name

| Number | Type | Name |
| ------ | ------ | ------ |
| 12 | start | Cue 12 GO |

### Optional Columns
<ul>
    <li>Notes</li>
    <li>Follow</li>
    <ul>
        <li>0 - No Follow</li>
        <li>1 - Auto-Continue</li>
        <li>2 - Auto-Follow</li>
    </ul>
    <li>Color (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercolorname-string" target="_blank">Options</a>)</li>
    <li>Columns available for "midi" cue type:</li>
    <ul>
        <li>MIDI Q Number</li>
        <li>MIDI Device ID</li>
        <li>MIDI Message Type</li>
        <li>MIDI Control Number</li>
        <li>MIDI Control Value</li>
        <li>MIDI Patch Channel</li>
        <li>MIDI Patch Number</li>
        <li>MIDI Q List</li>
        <ul>
            <li>1 - MIDI Voice Message ("Musical MIDI")</li>
            <li>2 - MIDI Show Control Message (MSC)</li>
            <li>3 - MIDI SysEx Message</li>
        </ul>
        <li>MIDI Command Format (<a href="https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-command-format-types" target="_blank">Options</a>)</li>
        <li>MIDI Command (<a href="https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-commands" target="_blank">Options</a>)</li>
    </ul>
    <li>Columns available for "network" cue type:</li>
    <ul>
        <li>QLab 5</li>
        <ul>
            <li>Network Patch Number</li>
            <li>Network Patch Channel</li>
            <li>Custom String</li>
        </ul>
        <li>QLab 4</li>
        <ul>
            <li>Message Type (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbermessagetype-number" target="_blank">Options</a>)</li>
            <li>OSC Cue Number (Only if using QLab Message Type)</li>
            <li>Command
                <ul>
                    <li>For QLab Messages (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numberqlabcommand-number" target="_blank">Options</a>)
                    </li>
                    <li>For an OSC message, you may now include a raw string in this column</li>
                </ul>
            </li>
        </ul>
    </ul>
</ul>

### Examples

- [Full Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/88bb34fb51fbb54c9e84db0c0361a7054d37f172/app/static/example_file/example.csv)

- [Simple Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/88bb34fb51fbb54c9e84db0c0361a7054d37f172/app/static/example_file/simple.csv)


## To run in development:
- clone or fork repository
- [create virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
- Install dependencies:
```
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```
- Run:
```
python3 application.py
```

- The application was bundled for distribution using pyinstaller. To re-bundle, install pyinstaller:
```
python3 -m pip install pyinstaller
```
- Then run:
```
pyinstaller application.spec
```


### If you want to run some tests:
- Install Pytest
```
pip install pytest
```

- Run Pytest
```
pytest
```

Recomendations for future features are very welcome!
