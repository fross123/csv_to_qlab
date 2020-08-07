# CSV to QLAB

## Using the flask framework, it is possible to batch import MIDI cues into QLab from a .csv file.

## To run without docker:
- ensure you have python3 installed
- run pip3 install -r requirements.txt
- flask run

## To run with Docker:
- run:
    - docker image build -t csv_to_qlab
    - docker run -p 5001:5000 -d csv_to_qlab
- Go to http://localhost:5001/ in your browser

*qlab must be open in order for the messages to be sent.*

The Flask part of the app is created so that there is some kind of a user interface, the csv_convert.py file is the file handlining the import if you are looking to implement only that feature. Eventually the client will be able to send the messages, but currently the app only works when run on a local network.

Please note, this is a very new project. In it's current state, this program only works for MIDI cues and the MSC type. Eventually I will be adding options for OSC and other types that may be useful for batch importing.

In its current state, this program will accept an ip address of the qlab machine, the device ID for the MIDI cues(for now you will have to set all of the auto-generated cues to the same value), and a .csv file with rows **EXACTLY** as follows: Cue, Page, Name, Notes. You can download an example document from static/example_file, just be sure to export your spreadsheet as a .csv file, any other file types will be rejected. Make sure there are no extra empty rows as well.

Recomendations for future features are very welcome! Please [contact me](https://www.finlayrosssound.com/contact) if you have a recomendation or any questions. Thanks!
