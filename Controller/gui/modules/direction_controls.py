from tkinter import Frame, LabelFrame, Label, N, S, W
from ..components import HorizontalSpinbox
from typing import Callable


class DirectionControls(Frame):
    """
      Container for controlling direction of RC vehicle
    """

    def __init__(self, parent: Frame = None, state: str = "normal",
                 set_direction: Callable[[int], None] = lambda val: None):
        """
        :param parent: parent frame
        :param state: can be 'normal' or 'disabled', decides whether
        :param set_direction: function for updating direction
        """
        Frame.__init__(self, parent)
        self.frame: LabelFrame = LabelFrame(parent, text="Throttle")

        direction_controls_frame: LabelFrame = LabelFrame(parent, text="Direction")
        direction_controls_frame.grid(row=0, column=0)

        label_text: str = "Controls vehicle direction"
        Label(direction_controls_frame, justify="left", text=label_text, wraplength=170, anchor=N + W, width=23) \
            .grid(row=0, column=0, sticky=N + S + W)

        HorizontalSpinbox(direction_controls_frame, from_=0, to_=2, start=1, increment=1, state=state,
                          on_update=set_direction).grid(row=0, column=1, padx=5, pady=5)

    def grid(self, row: int = 0, column: int = 0, **kwargs) -> None:
        """
        Places the element in grid of parent frame

        :param row: row in parent frame
        :param column: column in parent frame
        """
        self.frame.grid(row=row, column=column, **kwargs)
