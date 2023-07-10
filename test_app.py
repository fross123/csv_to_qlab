import pytest
from pathlib import Path
from application import app


def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_simple_csv():
    # get the resources folder in the tests folder
    resources = Path(__file__).parent / "static" / "example_file"
    

    response = app.test_client().post('/', data={
        "file": (resources / "simple.csv").open("rb"),
        "ip": "10.0.0.64",
        "ql5-passcode": "3420",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/success"

def test_example_csv():
    # get the resources folder in the tests folder
    resources = Path(__file__).parent / "static" / "example_file"
    

    response = app.test_client().post('/', data={
        "file": (resources / "example.csv").open("rb"),
        "ip": "10.0.0.64",
        "ql5-passcode": "3420",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/success"


def test_no_filename():
    # get the resources folder in the tests folder
    response = app.test_client().post('/', data={
        "file": "",
        "ip": "10.0.0.64",
    })

    assert response.status_code == 400