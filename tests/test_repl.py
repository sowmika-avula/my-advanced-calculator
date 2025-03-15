from calculator.repl import CalculatorREPL
import pytest
from unittest.mock import Mock, patch

def test_repl_menu_command(capsys):
    repl = CalculatorREPL()
    repl.do_menu("")
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out

def test_repl_history_command(capsys):
    repl = CalculatorREPL()
    repl.do_history("")
    captured = capsys.readouterr()
    assert "Operation" in captured.out

def test_repl_exit_command(capsys):
    repl = CalculatorREPL()
    assert repl.do_exit("") is True

def test_repl_default_command(capsys):
    repl = CalculatorREPL()
    repl.default("2 + 3")
    captured = capsys.readouterr()
    assert "5" in captured.out

def test_repl_default_command_error(capsys):
    repl = CalculatorREPL()
    repl.default("invalid_expression")
    captured = capsys.readouterr()
    assert "Error" in captured.out
    assert "Exception block executed!" in captured.out

def test_repl_unsupported_operation(capsys):
    repl = CalculatorREPL()
    repl.default("2 ? 3")
    captured = capsys.readouterr()
    assert "Unsupported operator" in captured.out

def test_repl_plugin_operations(capsys):
    repl = CalculatorREPL()
    repl.default("2 power 3")
    captured = capsys.readouterr()
    assert "8" in captured.out

    repl.default("sqrt 16")
    captured = capsys.readouterr()
    assert "4" in captured.out

def test_do_clear_history(capsys):
    repl = CalculatorREPL()
    repl.default("2 + 3")  # Add a record
    repl.do_clear_history("")
    captured = capsys.readouterr()
    assert "History cleared" in captured.out
    assert repl.history_manager.history.empty

def test_do_save_history(capsys):
    repl = CalculatorREPL()
    repl.do_save_history("")
    captured = capsys.readouterr()
    assert "History saved" in captured.out

def test_do_load_history(capsys):
    repl = CalculatorREPL()
    repl.do_load_history("")
    captured = capsys.readouterr()
    assert "History loaded" in captured.out

def test_repl_unhandled_exception(capsys, mocker):
    repl = CalculatorREPL()
    mocker.patch.object(
        repl.plugin_manager,
        "get_operation",
        side_effect=TypeError("Test error")
    )
    repl.default("sqrt 16")
    captured = capsys.readouterr()
    assert "Error: Test error" in captured.out
    assert "Exception block executed!" in captured.out

def test_repl_unary_operation_error(capsys):
    repl = CalculatorREPL()
    repl.default("invalid 16")  # Unsupported operator
    captured = capsys.readouterr()
    assert "Unsupported operator: invalid" in captured.out

def test_repl_invalid_input_format(capsys):
    repl = CalculatorREPL()
    repl.default("invalid input format extra")  # 4 parts
    captured = capsys.readouterr()
    assert "Invalid input format" in captured.out

def test_main_entry_point():
    with patch("calculator.repl.CalculatorREPL") as mock_repl:
        with patch("calculator.logging_config.setup_logging"):
            import main
            main.main()
            mock_repl.return_value.cmdloop.assert_called_once()
