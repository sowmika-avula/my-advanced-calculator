# main.py
from calculator.repl import CalculatorREPL
from calculator.logging_config import setup_logging


def main():
    setup_logging()
    CalculatorREPL().cmdloop()


if __name__ == "__main__":
    main()
