"""Tests for utility functions and classes."""

import os
import pytest
from unittest.mock import patch
from importlib.metadata import PackageNotFoundError
from src.audio_scribe.utils import DependencyManager, complete_path

@pytest.fixture
def path_test_params(request):
    """Fixture for path completion test parameters."""
    return request.param

@pytest.mark.parametrize(
    "path_test_params",
    [
        # (input_text, directory_contents, expected_first_completion, state)
        ("test", ["test.txt", "test.wav"], "test.txt", 0),
        ("nope", ["test.wav"], None, 0),
        ("docs/", ["README.md", "notes.txt"], "docs/README.md", 0),
        ("", ["file1.wav", "file2.wav"], "file1.wav", 0),
    ],
    indirect=True
)
def test_complete_path(path_test_params, monkeypatch):
    """Test the path completion function.
    
    Tests path completion with different scenarios:
    - Partial match in current directory
    - No matches
    - Subdirectory matches
    - Empty input (list all)
    """
    input_text, directory_contents, expected, state = path_test_params

    # Create a mock listdir function
    def mock_listdir(_):
        return sorted(directory_contents)  # Ensure consistent ordering

    def mock_isdir(path):
        return path.endswith(("docs/", "folder/"))

    # Apply the mocks
    monkeypatch.setattr(os, "listdir", mock_listdir)
    monkeypatch.setattr(os.path, "isdir", mock_isdir)

    # Test the completion
    result = complete_path(input_text, state)
    assert result == expected

    # Test that subsequent states cycle through matches
    if state == 0 and len(directory_contents) > 1:
        next_result = complete_path(input_text, 1)
        assert next_result is not None
        assert next_result != result

def test_verify_dependencies_all_present():
    """Test dependency verification when all packages are present."""
    with patch("importlib.metadata.version", return_value="1.0.0"):
        assert DependencyManager.verify_dependencies() is True

def test_verify_dependencies_missing():
    """Test dependency verification with missing packages."""
    with patch("importlib.metadata.version") as mock_version:
        mock_version.side_effect = PackageNotFoundError("mock")
        assert DependencyManager.verify_dependencies() is False

def test_verify_dependencies_version_mismatch():
    """Test dependency verification with version mismatches."""
    with patch.dict(DependencyManager.REQUIRED_PACKAGES, {"torch": "2.0.0"}):
        with patch("importlib.metadata.version", return_value="1.0.0"):
            assert DependencyManager.verify_dependencies() is False

@pytest.mark.parametrize("package,version", [
    ("torch", None),
    ("pyannote.audio", None),
    ("openai-whisper", None),
    ("pytorch-lightning", None),
])
def test_required_packages_configuration(package, version):
    """Test the required packages configuration."""
    assert package in DependencyManager.REQUIRED_PACKAGES
    assert DependencyManager.REQUIRED_PACKAGES[package] == version