---
sidebar_position: 1
---

# Install from Source Code

This method builds the software from the source code. You should be comfortable with the command line to use this method.


## Step 1: Install Python3
Check your current python version.
```bash
python3 --version
```

If you do not get ```python 3.9``` or higher, you should install the [latest version](https://www.python.org/downloads/) of python.

After install, you should also confirm that pip3 installed properly.

```bash
pip3 --version
```


## Step 2: Clone or fork the CSV to QLab repository.

Navigate to the directory you would like the code to be in:
```bash
cd Documents
```

Clone the repository:
```bash
git clone https://github.com/fross123/csv_to_qlab.git
```


## Step 3: [Create a Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

Navigate to the csv_to_qlab directory.
```bash
cd csv_to_qlab
```

Create the virtual environment.
```bash
python3 -m venv env
```

Activate the virtual environment.
```bash
source env/bin/activate
```

Confirm the python code used.
```bash
which python3
```

And you should get something like ```../csv_to_qlab/env/bin/python```.

:::tip
When you are done with the virtual environment the command is ```deactivate```
:::


## Step 4: Install the required dependencies
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```


## Step 5: Start the application
```bash
python3 application.py
```

:::tip
To exit type control+c.
:::