import pytest
from hello import Hello


def test_get_message():
    assert Hello().get_message() == "Hello, World!"
