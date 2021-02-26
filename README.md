# CSV to QLAB

## To run on mac:
- download [csv_to_qlab.zip](https://github.com/fross123/csv_to_qlab/releases/latest/download/csv_to_qlab.zip) from the latest release
- unzip the foder
- open the app
    - *qlab must be open on the recieving computer in order for the messages to be recieved. It automatically picks the qlab workspace that is open and inserts the cues into the current folder.*

**Please note that I do not currently have an Apple Developer Certificate and therefore there will be some scary warnings when trying to run this application locally. It is entirely up to you to decide to run this application. If you have concerns with the bundled application releases, I suggest cloning or forking the repository.**


## How to format your csv file:
Starting with version 2021.1.0, you no longer need to be as precise about the order of your rows in your .csv file. You can now also add **any** type of cue, however some do require additional parameters.
<p><a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#workspaceidnew-cue_type" target="_blank">See permitted cue types.</a></p>
<p>Certain optional collumns below require numbers rather than text, please follow the links to see the most up to date options that are allowed for QLab.</p>

<p>Required Columns:</p>
<ul>
    <li>Number</li>
    <li>Type</li>
    <li>Name</li>
</ul>

<p>Optional Collumns:</p>
<ul>
    <li>Page (Will be added to notes)</li>
    <li>Name</li>
    <li>Notes</li>
    <li>Follow (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercontinuemode-number" target="_blank">Options</a>)</li>
    <li>Color (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercolorname-string" target="_blank">Options</a>)</li>
    <li>Collumns availible for "midi" cue type:</li>
    <ul>
        <li>Midi Cue Number</li>
        <li>Device ID</li>
        <li>Message Type (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbermessagetype-number-1" target="_blank">Options</a>)</li>
        <li>Command Format (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercommandformat-number" target="_blank">Options</a>)</li>
        <li>Command (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercommand-number" target="_blank">Options</a>)</li>
    </ul>
    <li>Collumns availible for "network" cue type:</li>
    <ul>
        <li>Message Type (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbermessagetype-number" target="_blank">Options</a>)</li>
        <li>OSC Cue Number (Only if using QLab Message Type)</li>
        <li>Command (Only if using QLab Message Type) (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numberqlabcommand-number" target="_blank">Options</a>)</li>
    </ul>
</ul>

- Make sure to save your file in the .csv format. (Not Excel or Numbers)
- [Full Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/master/static/example_file/example.csv)
- [Simple Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/master/static/example_file/simple.csv)


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

Recomendations for future features are very welcome!
