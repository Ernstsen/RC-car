class CommandHandler(object):
    """
    Interface for handling registered commands in the system
    """

    def handle_command(self, command: str) -> None:
        """
        Handles a command

        :param command: received command
        """
