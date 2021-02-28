from tkinter import Frame, LabelFrame, Button
from typing import List

from Controller.gui import MiscControlSpec


class MiscControlsModule(Frame):
    """
    Display module for miscellaneous control options
    """

    def __init__(self, master: Frame, misc_controls: List[MiscControlSpec], state: str = "active"):
        """
        :param master: parent frame
        :param misc_controls: map between control names and MiscControlSpecs
        """
        Frame.__init__(self, master)
        self.misc_controls_frame: LabelFrame = LabelFrame(master, text="Miscellaneous Controls", width=250)
        for control in misc_controls:
            Button(self.misc_controls_frame, text=control.display_name, state=state) \
                .grid(row=control.row, column=control.column)

    def grid(self, row=0, column=0) -> None:
        """
        :param row: desired row for the module
        :param column: desired column for the module
        """
        self.misc_controls_frame.grid(row=row, column=column)
