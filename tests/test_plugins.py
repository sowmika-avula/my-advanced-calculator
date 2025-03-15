from calculator.plugin_manager import PluginManager
import pytest
import importlib

def test_register_command():
    pm = PluginManager()
    pm.register_command("test_command")
    assert "test_command" in pm.commands

def test_get_operation():
    pm = PluginManager()
    pm.operations["test_op"] = lambda x, y: x + y
    assert pm.get_operation("test_op")(2, 3) == 5

def test_plugin_loading_error(monkeypatch, capsys):
    # Simulate invalid plugin directory
    monkeypatch.setattr(importlib, "import_module", lambda _: exec("raise ImportError"))

    pm = PluginManager()
    pm.load_plugins()

    captured = capsys.readouterr()
    assert "Error loading plugin" in captured.out
