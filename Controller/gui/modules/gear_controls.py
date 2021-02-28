from tkinter import Frame, LabelFrame, Label, Spinbox, IntVar, N, S, W
from tkinter.font import Font
from typing import Callable


class GearControls(Frame):
    """
    Container for controlling gear of RC vehicle
    """

    def __init__(self, parent: Frame = None, state: str = "normal",
                 set_gear: Callable[[int], None] = lambda val: None,
                 font: Font = None):
        """
        :param parent: parent frame
        :param state: can be 'normal' or 'disabled', decides whether
        :param set_gear: function for updating gear on RC vehicle
        :param font: font for the contained spinbox
        """
        Frame.__init__(self, parent)
        self.frame: LabelFrame = LabelFrame(parent, text="Gear")
        self.gear: IntVar = IntVar(value=1)

        label_text: str = "Controls the gear of the vehicle"

        def on_update():
            set_gear(self.gear.get())

        Label(self.frame, justify="left", text=label_text, wraplength=170, anchor=N+W, width=25) \
            .grid(row=0, column=0, sticky=N + S + W)

        Spinbox(self.frame, values=(1, 2, 3, 4), state=state, width=1, textvariable=self.gear,
                command=on_update, font=font).grid(row=0, column=1, padx=5, pady=5)

    def grid(self, row: int = 0, column: int = 0, **kwargs):
        """
        Places the element in grid of parent frame

        :param row: row in parent frame
        :param column: column in parent frame
        """
        self.frame.grid(row=row, column=column, **kwargs)
