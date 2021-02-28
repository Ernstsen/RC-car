from tkinter import Widget, Frame, NSEW, Label, Button, IntVar
from typing import Callable


class HorizontalSpinbox(Widget):
    """
    Horizontal spinbox widget
    """

    def __init__(self, master, from_=0, start=5, to_=10, increment=1, state="active",
                 on_update: Callable[[int], None] = lambda *args, **kwargs: None):
        super().__init__(master, "label")
        self.from_: int = from_
        self.to_: int = to_
        self.increment: int = increment
        self.state: str = state
        self.value: int = start
        self.valueVar: IntVar = IntVar(value=start)
        self.on_update: Callable = on_update

        self.frame: Frame = Frame(master)
        Button(self.frame, text="left", state=state, command=self.decrement_func).grid(row=0, column=0)
        self.label: Label = Label(self.frame, textvariable=self.valueVar).grid(row=0, column=1)
        Button(self.frame, text="right", state=state, command=self.increment_func).grid(row=0, column=2)

    def grid(self, row=0, column=0, sticky=NSEW, **kw):
        self.frame.grid(row=row, column=column, sticky=sticky, **kw)

    def update_value(self, value: int):
        self.valueVar.set(value)
        self.on_update(value)

    def increment_func(self):
        if self.value < self.to_:
            self.value += 1
        self.update_value(self.value)

    def decrement_func(self):
        if self.value > self.from_:
            self.value -= 1
        self.update_value(self.value)
