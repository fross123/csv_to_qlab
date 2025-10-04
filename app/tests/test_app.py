from pathlib import Path
from app.application import app


def test_home_page():
    """
    Test response from homepage.
    """
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_simple_csv():
    """
    Tests simple.csv submission. When qlab open, tests return.
    """
    resources = Path(__file__).parent.parent / "static" / "example_file"

    response = app.test_client().post(
        "/",
        data={
            "file": (resources / "simple.csv").open("rb"),
            "ip": "127.0.0.1",
            "passcode": "3420",
            "qlab-version": "5",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/success"


def test_example_csv():
    """
    Tests csv_test_doc.csv. When QLab is open, also tests return.
    """
    resources = Path(__file__).parent.parent / "static" / "example_file"

    response = app.test_client().post(
        "/",
        data={
            "file": (resources / "csv_test_doc.csv").open("rb"),
            "ip": "127.0.0.1",
            "passcode": "3420",
            "qlab-version": "5",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/success"


def test_ql4_csv():
    """
    Test .csv doc and test for previous versions of qlab.
    """
    resources = Path(__file__).parent.parent / "static" / "example_file"

    response = app.test_client().post(
        "/",
        data={
            "file": (resources / "csv_test_doc_qlab_4.csv").open("rb"),
            "ip": "127.0.0.1",
            "passcode": "3420",
            "qlab-version": "4",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/success"


def test_no_filename():
    """
    Ensure that files with no name are invalid.
    """
    response = app.test_client().post(
        "/",
        data={
            "file": "",
            "ip": "127.0.0.1",
        },
    )

    assert response.status_code == 400
