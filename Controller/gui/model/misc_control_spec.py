from typing import Callable


class MiscControlSpec(object):
    """
    Object specifying a misc. control to add to the graphics user interface
    """

    def __init__(self, display_name: str, on_change: Callable[[any], None], param_type: type,
                 row: int, column: int, description: str = None):
        """
        :param display_name: the name to be displayed in the GUI for this setting
        :param on_change: the method to be called upon change. Must atke exactly one argument of the type 'param_type'
        :param param_type: type of the parameter
        :param row: row to draw the control in
        :param column: column to draw the control in
        :param description: description to be displayed in the GUI - default is none
        """
        self.display_name: str = display_name
        self.on_change: callable = on_change
        self.param_type: type = param_type
        self.row = row
        self.column = column
        self.description: str = description
