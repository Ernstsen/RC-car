from tkinter import Frame, LabelFrame, Label, N, S, E, W, NW


class InformationFrame(Frame):
    """
    Frame for displaying information about the program
    """

    def __init__(self, parent: Frame = None, version: str = ""):
        """
        :param parent: parent frame
        """
        Frame.__init__(self, parent)

        self.frame: LabelFrame = LabelFrame(parent, text="About")
        Label(self.frame, fg="grey", text="Author: Johannes Ernstsen", anchor=NW, width=35) \
            .grid(row=0, column=0, sticky=N + S + W)
        Label(self.frame, fg="grey", text="Ernstsen Software").grid(row=1, column=0, sticky=N + S + W)
        Label(self.frame, fg="grey", text=version).grid(row=2, column=0, sticky=N + S + E)

    def grid(self, row: int = 0, column: int = 0, **kwargs) -> None:
        """
        Places the element in grid of parent frame

        :param row: row in parent frame
        :param column: column in parent frame
        """
        self.frame.grid(row=row, column=column, **kwargs)
