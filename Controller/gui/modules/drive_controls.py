from tkinter import Frame, LabelFrame, Label, Radiobutton, IntVar
from typing import Callable


class DriveControls(Frame):
    """
    Container for controlling high/low drive
    """

    def __init__(self, parent: Frame = None, state: str = "active",
                 set_drive: Callable[[int], None] = lambda val: None):
        """
        :param parent: parent frame
        :param state: module state
        :param set_drive: function for updating drive on RC vehicle
        """
        Frame.__init__(self, parent)

        self.drive_controls_frame: LabelFrame = LabelFrame(parent, text="Drive")
        self.drive: IntVar = IntVar(0)

        def on_change():
            set_drive(self.drive.get())

        label_text = "This options controls the drive, and enables a user to choose between a high or low gearing " \
                     "between gearbox and wheels. Low gearing grants high torque and low speed, while High gearing " \
                     "grants the opposite tradeoff "

        Label(self.drive_controls_frame, width=35, wraplength=250, justify="left", state=state, text=label_text) \
            .grid(row=0, column=0)
        Radiobutton(self.drive_controls_frame, variable=self.drive, value=0, state=state, command=on_change,
                    text="Low gearing").grid(row=1, column=0)
        Radiobutton(self.drive_controls_frame, variable=self.drive, value=1, state=state, command=on_change,
                    text="High gearing").grid(row=2, column=0)

    def grid(self, row: int = 0, column: int = 0, **kwargs) -> None:
        """
        Places the element in grid of parent frame

        :param row: row in parent frame
        :param column: column in parent frame
        """
        self.drive_controls_frame.grid(row=row, column=column, **kwargs)
