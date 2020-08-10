# CSV to QLAB

*Using a flask application, it is possible to batch import MIDI cues into QLab from a .csv file.*

## To run on mac:
- download the dist/csv_to_qlab.app folder
- open the app

*qlab must be open on the recieving computer in order for the messages to be recieved. It automatically picks the qlab workspace that is open and inserts the cues into the current folder.*

Please note, this is a very new project. Currently, this program only works for MIDI cues and the MSC type. Eventually I will be adding options for OSC and other types that may be useful for batch importing.

In its current state, this program will accept an ip address of the qlab machine, the device ID for the MIDI cues(for now you will have to set all of the auto-generated cues to the same value), and a .csv file with rows **EXACTLY** as follows: Cue, Page, Name, Notes. You can download an example document from static/example_file, just be sure to export your spreadsheet as a .csv file, any other file types will be rejected. Make sure there are no extra empty rows as well.

Recomendations for future features are very welcome! Please [contact me](https://www.finlayrosssound.com/contact) if you have a recomendation or any questions. Thanks!
