class CommandHandler(object):
    """
    Interface for handling registered commands in the system
    """

    def handle_command(self, command: str) -> bool:
        """
        Handles a command

        :param command: received command
        :return: True if command parsed and executed without error - False otherwise
        """
