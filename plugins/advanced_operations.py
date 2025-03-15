from calculator.calculator import Calculator


def register(plugin_manager):
    plugin_manager.register_command("power")
    plugin_manager.register_command("sqrt")
