"""Tests for app module."""
from apps import __version__


def test_version() -> None:
    """Test the app version."""
    assert __version__ == "0.1.0"