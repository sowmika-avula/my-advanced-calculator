def register(plugin_manager):
    plugin_manager.register_command("power")
    plugin_manager.operations["power"] = power


def power(base: float, exponent: float) -> float:
    return base**exponent
