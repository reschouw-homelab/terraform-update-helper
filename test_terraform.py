import terraform
import pytest

def test_is_available():
    assert(terraform.is_available())

def test_get_version():
    assert(isinstance(terraform.get_version(), str))
