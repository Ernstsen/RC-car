from tkinter import Frame, LabelFrame, Label, Radiobutton, IntVar, Variable, E, W, NW
from typing import List, Dict

try:
    from Controller.gui.model import MiscControlSpec
except ModuleNotFoundError:
    from ..model import MiscControlSpec


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
        self.state: str = state
        self.misc_controls_frame: LabelFrame = LabelFrame(master, text="Miscellaneous Controls", width=250)
        self.state_variables: Dict[str, Variable] = {}
        Label(self.misc_controls_frame, width=92).grid(row=0, column=0, columnspan=len(misc_controls), sticky=E + W)
        for control in misc_controls:
            self.build_input_entity(control, self.misc_controls_frame) \
                .grid(row=control.row, column=control.column, sticky=NW)

    def grid(self, row=0, column=0, **kwargs) -> None:
        """
        :param row: desired row for the module
        :param column: desired column for the module
        """
        self.misc_controls_frame.grid(row=row, column=column, **kwargs)

    def build_input_entity(self, control: MiscControlSpec, parent: LabelFrame) -> LabelFrame:
        """
        Converts a spec into a widget
        :param control: the spec to be converted into the widget
        :param parent: parent frame
        :return: widget from given spec
        """
        frame = LabelFrame(parent, text=control.display_name)

        if control.description:
            Label(frame, width=35, wraplength=250, justify="left", state=self.state, text=control.description) \
                .grid(row=0, column=0)

        if control.param_type == bool:
            var = self.state_variables[control.display_name] = IntVar()

            def on_update():
                control.on_change(var.get() == 1)

            Radiobutton(frame, variable=var, value=0, state=self.state, command=on_update, text="Off") \
                .grid(row=1, column=0)
            Radiobutton(frame, variable=var, value=1, state=self.state, command=on_update, text="On") \
                .grid(row=2, column=0)
        return frame
