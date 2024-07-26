from app import index


def test_index():
    assert index() == "Hello World! This page has been visited times.1"
