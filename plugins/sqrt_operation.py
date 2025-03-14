import math


def register(plugin_manager):
    plugin_manager.register_command("sqrt")
    plugin_manager.operations["sqrt"] = sqrt


def sqrt(number: float) -> float:
    return math.sqrt(number)
