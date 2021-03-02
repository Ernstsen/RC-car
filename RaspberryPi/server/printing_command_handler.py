from .command_handler import CommandHandler


class PrintingCommandHandler(CommandHandler):
    """
    Prints all received commands
    """

    def handle_command(self, command: str) -> None:
        print("COMMAND: " + command)
