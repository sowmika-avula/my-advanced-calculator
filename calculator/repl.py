import cmd
import logging
from calculator.plugin_manager import PluginManager
from calculator.history_manager import HistoryManager
from calculator.calculator import Calculator

logger = logging.getLogger(__name__)


class CalculatorREPL(cmd.Cmd):
    prompt = "calc> "

    def __init__(self):
        super().__init__()
        logger.info("Initializing Calculator REPL")
        self.history_manager = HistoryManager()
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()
        self.calculator = Calculator()

    def do_menu(self, _: str) -> None:
        """List available commands."""
        logger.info("Displaying menu")
        print("Available commands:")
        for command in self.plugin_manager.commands:
            print(f"- {command}")
        print("- clear_history (Clear calculation history)")
        print("- history (Show calculation history)")
        print("- exit (Exit the calculator)")

    def do_history(self, _: str) -> None:
        """Show calculation history."""
        logger.info("Displaying history")
        print(self.history_manager.history)

    def do_clear_history(self, _: str) -> None:
        """Clear calculation history."""
        logger.info("Clearing history")
        self.history_manager.clear_history()
        print("History cleared")

    def do_save_history(self, _: str) -> None:
        """Save calculation history to file."""
        logger.info("Saving history to file")
        self.history_manager.save_history()
        print("History saved")

    def do_load_history(self, _: str) -> None:
        """Load calculation history from file."""
        logger.info("Loading history from file")
        self.history_manager.load_history()
        print("History loaded")

    def do_exit(self, _: str) -> bool:
        """Exit the REPL."""
        logger.info("Exiting calculator")
        print("Exiting...")
        return True

    def default(self, line: str) -> None:
        """Handle arithmetic operations."""
        logger.debug("Processing input: %s", line)
        try:
            parts = line.split()

            if len(parts) == 2:  # Unary operation (e.g., sqrt)
                operator_symbol, operand = parts
                operation = self.plugin_manager.get_operation(operator_symbol)
                if operation:
                    logger.info(
                        "Executing unary operation: %s %s", operator_symbol, operand
                    )
                    result = operation(float(operand))
                else:
                    logger.error("Unsupported operator: %s", operator_symbol)
                    raise ValueError(f"Unsupported operator: {operator_symbol}")

            elif len(parts) == 3:  # Binary operation
                left, operator_symbol, right = parts
                if operator_symbol in self.plugin_manager.commands:
                    logger.info(
                        "Executing plugin operation: %s %s %s",
                        left,
                        operator_symbol,
                        right,
                    )
                    operation = self.plugin_manager.get_operation(operator_symbol)
                    result = operation(float(left), float(right))
                else:
                    logger.info("Executing standard operation: %s", line)
                    result = self.calculator.evaluate_expression(line)

            else:
                logger.error("Invalid input format: %s", line)
                raise ValueError("Invalid input format")

            print(result)
            logger.info("Result: %s", result)
            self.history_manager.add_record(line, result)

        except (ValueError, ZeroDivisionError, TypeError) as error:
            logger.error("Error processing input: %s", error, exc_info=True)
            print(f"Error: {error}")
            print("Exception block executed!")


if __name__ == "__main__":
    CalculatorREPL().cmdloop()
