from app.db import get_data

def test_get_data():
    assert get_data() == "dummy-data"

