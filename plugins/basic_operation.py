from calculator.calculator import Calculator


def register(plugin_manager):
    plugin_manager.register_command("add")
    plugin_manager.register_command("subtract")
    plugin_manager.register_command("multiply")
    plugin_manager.register_command("divide")
