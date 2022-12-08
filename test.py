import argparse
import pytest
from app import Url
from app import create_argument_parser 
from pathlib import Path

@pytest.fixture()
def argument_parser():
    return create_argument_parser()

def test_cli(argument_parser):
    parsed = argument_parser.parse_args([
        "--origin", "https://www.google.com",
        "--dest", ""
    ])
    assert parsed.origin is "https://www.google.com"

def test_validate_Url():
    assert Url("https://www.google.com") is "https://www.google.com"
    assert Url("https://www.google.com/directory/") is "https://www.google.com/directory/"
    assert Url("https://www.google.com/directory/file") is "https://www.google.com/directory/file"


def test_validate_Url_raise():
    with pytest.raises(ValueError):
        Url("https:/www.google.com")



