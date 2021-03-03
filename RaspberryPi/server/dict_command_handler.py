from typing import Callable, Dict, List

from .command_handler import CommandHandler


class DictCommandHandler(CommandHandler):
    """
    CommandHandler doing lookups in dictionary
    """

    def __init__(self, commands: Dict[str, Callable[[List[str]], None]]):
        self.commands = commands

    def handle_command(self, command: str) -> None:
        split: List[str] = command.split(";")
        self.commands[split[0]](split[1:])
