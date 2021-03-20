from tkinter import Frame, LabelFrame, Label, Spinbox, IntVar, N, S, W
from tkinter.font import Font
from typing import Callable


class ThrottleControls(Frame):
    """
      Container for controlling gear of RC vehicle
    """

    def __init__(self, parent: Frame = None, state: str = "normal",
                 set_throttle: Callable[[int], None] = lambda val: None,
                 font: Font = None):
        """
        :param parent: parent frame
        :param state: can be 'normal' or 'disabled', decides whether
        :param set_throttle: function for updating gear on RC vehicle
        :param font: font for the contained spinbox
        """
        Frame.__init__(self, parent)
        self.frame: LabelFrame = LabelFrame(parent, text="Throttle")

        throttle: IntVar = IntVar(value=0)

        def on_update():
            set_throttle(throttle.get())

        label_text: str = "Throttle control - scale from 0 to 1, 0 being off"
        Label(self.frame, justify="left", text=label_text, wraplength=150, anchor=N + W, width=21) \
            .grid(row=0, column=0, sticky=N + S + W)

        Spinbox(self.frame, from_=0, to_=1, increment=1, state=state, width=2,
                textvariable=throttle, command=on_update, font=font) \
            .grid(row=0, column=1, padx=5, pady=5)

    def grid(self, row: int = 0, column: int = 0, **kwargs) -> None:
        """
        Places the element in grid of parent frame

        :param row: row in parent frame
        :param column: column in parent frame
        """
        self.frame.grid(row=row, column=column, **kwargs)
