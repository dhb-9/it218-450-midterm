# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring, invalid-name
import os
import sys
from decimal import Decimal

from unittest.mock import patch, MagicMock
import pytest

from app.__init__ import App  # Use app.__init__ instead of app.init


# Add the parent directory to the sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def setup_environment():
    with patch.dict(os.environ, {"ENVIRONMENT": "test", "LOG_LEVEL": "DEBUG"}):
        yield

@patch("builtins.input", side_effect=["add", "10", "20", "exit"])
@patch("app.__init__.get_plugin")
@patch("app.__init__.HistoryManager")
def test_run_add_command(mock_history_manager, mock_get_plugin, mock_input, setup_environment):
    mock_command = MagicMock()
    mock_command_instance = MagicMock()
    mock_command_instance.execute.return_value = Decimal("30")
    mock_command.return_value = mock_command_instance
    mock_get_plugin.return_value = mock_command

    history_manager_instance = mock_history_manager.return_value

    App.start()

    mock_get_plugin.assert_called_once_with("add")
    mock_command_instance.execute.assert_called_once()
    history_manager_instance.add_record.assert_called_once_with("add", Decimal("10"), Decimal("20"), Decimal("30"))

@patch("builtins.input", side_effect=["history", "exit"])
@patch("app.__init__.HistoryManager")
def test_run_history_command(mock_history_manager, mock_input, setup_environment, capsys):
    history_manager_instance = mock_history_manager.return_value
    history_manager_instance.history_df = "Test History DataFrame"

    App.start()

    history_manager_instance.load_history.assert_called_once()

    captured = capsys.readouterr()
    assert "Test History DataFrame" in captured.out

@patch("builtins.input", side_effect=["clear", "exit"])
@patch("app.__init__.HistoryManager")
def test_run_clear_command(mock_history_manager, mock_input, setup_environment):
    history_manager_instance = mock_history_manager.return_value

    App.start()

    history_manager_instance.clear_history.assert_called_once()

@patch("builtins.input", side_effect=["delete", "exit"])
@patch("app.__init__.HistoryManager")
def test_run_delete_command(mock_history_manager, mock_input, setup_environment):
    history_manager_instance = mock_history_manager.return_value

    App.start()

    history_manager_instance.delete_history.assert_called_once()
