from tkinter import Widget, Frame, NSEW, Label, Button, IntVar


class HorizontalSpinbox(Widget):
    """
    Horizontal spinbox widget
    """

    def __init__(self, master, from_=0, start=5, to_=10, increment=1, state="active"):
        super().__init__(master, "label")
        self.from_: int = from_
        self.to_: int = to_
        self.increment: int = increment
        self.state: str = state
        self.value: int = start
        self.valueVar: IntVar = IntVar(value=start)

        self.frame: Frame = Frame(master)
        Button(self.frame, text="left", command=self.decrement_func).grid(row=0, column=0)
        self.label: Label = Label(self.frame, textvariable=self.valueVar).grid(row=0, column=1)
        Button(self.frame, text="right", command=self.increment_func).grid(row=0, column=2)

    def grid(self, row=0, column=0, sticky=NSEW, **kw):
        self.frame.grid(row=row, column=column, sticky=sticky, **kw)

    def increment_func(self):
        if self.value < self.to_:
            self.value += 1
        self.valueVar.set(self.value)

    def decrement_func(self):
        if self.value > self.from_:
            self.value -= 1
        self.valueVar.set(self.value)
