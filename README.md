# CSV to QLAB

## To run on mac:
- download [csv_to_qlab.zip](https://github.com/fross123/csv_to_qlab/releases/latest/download/csv_to_qlab.zip) from the latest release
- unzip the foder
- open the app
    - *qlab must be open on the recieving computer in order for the messages to be recieved. It automatically picks the qlab workspace that is open and inserts the cues into the current folder.*

**Please note that I do not currently have an Apple Developer Certificate and therefore there will be some scary warnings when trying to run this application locally. It is entirely up to you to decide to run this application. If you have concerns with the bundled application releases, I suggest cloning or forking the repository.**


## How to format your csv file:
- 4 columns:
    - Cue
    - Page
    - Name
    - Notes
- Make sure to save your file in the .csv format. (Not Excel or Numbers)
- [Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/master/static/example_file/example.csv)


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

- The application was bundled for distribution using pyinstaller. To re-bundle, simply install pyinstaller:
```
python3 -m pip install pyinstaller
```
- Then run:
```
pyinstaller application.spec
```

:warning: | I slipped in some Big Sur vomit that Apple left all over, so building this way might not work if you are running on the new OS until pysintaller has a new release. The develomnet version of [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html) worked fine for me, but you have been warned.
------------ | -------------


Recomendations for future features are very welcome!