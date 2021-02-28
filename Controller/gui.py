from tkinter import *
from tkinter.font import Font
from typing import Dict, List

from gui import MiscControlSpec
from gui.components import HorizontalSpinbox
from gui.modules import MiscControlsModule
from vehicle_control import Controller, ControllerSimulator
from video import VideoViewer, StaticImageViewer


class GUI(Frame):
    """
    Class handling the graphics user interface of the application
    """

    def __init__(self, master=None,
                 viewer: VideoViewer = StaticImageViewer(r"../unnamed.png"),
                 enabled: Dict[str, bool] = None,
                 controller: Controller = ControllerSimulator(),
                 misc_controls: List[MiscControlSpec] = None):
        """
        Constructor for the graphics user interface

        :param master: master frame - from Frame constructor
        :param viewer: VideoViewer to display stream - defaults to static image
        :param enabled: map from strings to booleans for whether parts are enabled.
        :param controller: object allowing interfacing with the RC vehicle
        :param misc_controls: list of MiscControlSpecs to be rendered in misc_controls section

        If False for disabled, True for enabled and missing for non-displayed.
        Keys: 'misc, drive, gear, throttle', 'direction'
        """
        # this will create a label widget
        Frame.__init__(self, master)

        self.master.title("Remote Vehicle Controller")
        self.master.resizable(width=FALSE, height=FALSE)
        self.version = "V0.1"
        self.img = None  # Initializes val img, containing placeholder for video stream
        self.drive: IntVar = IntVar(value=0)
        self.gear: IntVar = IntVar(value=1)
        self.throttle: IntVar = IntVar(value=0)
        self.viewer = viewer
        self.controller = controller
        self.spinbox_font = Font(family="Helvetica", size=36)

        if enabled is not None:
            self.enabled = enabled
        else:
            self.enabled: Dict[str, bool] = {
                "misc": True,
                "drive": True,
                "gear": True,
                "throttle": True,
                "direction": True
            }

        structure = self.build_frame_structure(master)

        self.draw_stream_window(structure)
        self.draw_misc_controls(structure, misc_controls)
        self.draw_drive_controls(structure)
        self.draw_gear_controls(structure)
        self.draw_throttle_controls(structure)
        self.draw_direction_controls(structure)
        self.draw_information(structure)

    @staticmethod
    def build_frame_structure(root_frame: Frame) -> Dict[str, Frame]:
        """
        builds application structure, in the form of frames in a grid.

        :param root_frame: the frame for the structure to reside in
        :return: the constructed structure
        """
        # noinspection PyDictCreation
        frames: Dict[str, Frame] = {}

        padding: int = 2

        frames["stream_window"] = Frame(root_frame)
        frames["stream_window"].grid(row=0, column=0, rowspan=5, columnspan=5, sticky=NSEW, padx=padding, pady=padding)

        frames["misc_controls"] = Frame(root_frame)
        frames["misc_controls"].grid(row=5, column=0, sticky=NSEW, padx=padding, pady=padding)

        frames["drive_controls"] = Frame(root_frame)
        frames["drive_controls"].grid(row=0, column=5, sticky=NSEW, padx=padding, pady=padding)

        frames["gear_controls"] = Frame(root_frame)
        frames["gear_controls"].grid(row=2, column=5, sticky=NSEW, padx=padding, pady=padding)

        frames["throttle_controls"] = Frame(root_frame)
        frames["throttle_controls"].grid(row=3, column=5, sticky=NSEW, padx=padding, pady=padding)

        frames["direction_controls"] = Frame(root_frame)
        frames["direction_controls"].grid(row=4, column=5, sticky=NSEW, padx=padding, pady=padding)

        frames["info"] = Frame(root_frame)
        frames["info"].grid(row=5, column=5, sticky=NSEW, padx=padding, pady=padding)

        return frames

    def draw_stream_window(self, frames: Dict[str, Frame]) -> None:
        """
        Fills frame with video-stream
        (For now simply some PNG, as a placeholder)

        Draws in frame 'stream_window'
        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame = frames["stream_window"]
        # Placeholder for video stream
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Video Stream")
        misc_controls_frame.grid(row=0, column=0)

        label = Label(misc_controls_frame)
        label.grid(row=0, column=0, columnspan=2, rowspan=2, padx=5, pady=5)
        self.viewer.set_label(label)
        self.viewer.video_stream_loop()

    def draw_misc_controls(self, frames: Dict[str, Frame], misc_controls: List[MiscControlSpec]) -> None:
        """
        Creates miscellaneous controls in frame 'misc_controls'

        :param frames: frames dictionary. Maps string to Frame
        :param misc_controls: list of MiscControlSpec to be rendered
        """
        if "misc" not in self.enabled or not misc_controls:
            return
        enabled: bool = self.enabled["misc"]
        state = ("active" if enabled else "disabled")

        frame: Frame = frames["misc_controls"]
        MiscControlsModule(master=frame, misc_controls=misc_controls, state=state).grid(row=0, column=0)

    def draw_drive_controls(self, frames: Dict[str, Frame]) -> None:
        """
        Creates controls for drive controls.
        Options are hi and lo, for high or low gearing.

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        if "drive" not in self.enabled:
            return
        enabled: bool = self.enabled["drive"]
        state = ("active" if enabled else "disabled")

        frame: Frame = frames["drive_controls"]
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Drive")
        misc_controls_frame.grid(row=0, column=2)

        def on_change():
            self.controller.set_drive(self.drive.get())

        label_text = "This options controls the drive, and enables a user to choose between a high or low gearing " \
                     "between gearbox and wheels. Low gearing grants high torque and low speed, while High gearing " \
                     "grants the opposite tradeoff "

        Label(misc_controls_frame, width=35, wraplength=250, justify="left", state=state, text=label_text) \
            .grid(row=0, column=0)
        Radiobutton(misc_controls_frame, variable=self.drive, value=0, state=state, command=on_change,
                    text="Low gearing").grid(row=1, column=0)
        Radiobutton(misc_controls_frame, variable=self.drive, value=1, state=state, command=on_change,
                    text="High gearing").grid(row=2, column=0)

    def draw_gear_controls(self, frames: Dict[str, Frame]) -> None:
        """
        Creates controls for gear controls.

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        if "gear" not in self.enabled:
            return
        enabled: bool = self.enabled["gear"]
        state = ("normal" if enabled else "disabled")
        frame: Frame = frames["gear_controls"]

        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Gear")
        misc_controls_frame.grid(row=1, column=2)

        label_text: str = "Controls the gear of the vehicle"

        def on_update():
            self.controller.set_gear(self.gear.get())

        Label(misc_controls_frame, justify="left", text=label_text, wraplength=170, anchor=NW, width=25) \
            .grid(row=0, column=0, sticky=N + S + W)

        Spinbox(misc_controls_frame, values=(1, 2, 3, 4), state=state, width=1, textvariable=self.gear,
                command=on_update, font=self.spinbox_font).grid(row=0, column=1, padx=5, pady=5)

    def draw_throttle_controls(self, frames: Dict[str, Frame]) -> None:
        """
        Creates controls for gear controls.

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        if "throttle" not in self.enabled:
            return
        enabled: bool = self.enabled["throttle"]
        state = ("normal" if enabled else "disabled")
        frame: Frame = frames["throttle_controls"]
        throttle_controls_frame: LabelFrame = LabelFrame(frame, text="Throttle")
        throttle_controls_frame.grid(row=0, column=0)

        def on_update():
            self.controller.set_gear(self.gear.get())

        label_text: str = "Throttle control - scale from 0 to 10, 0 being off"
        Label(throttle_controls_frame, justify="left", text=label_text, wraplength=170, anchor=NW, width=25) \
            .grid(row=0, column=0, sticky=N + S + W)

        Spinbox(throttle_controls_frame, from_=0, to_=10, increment=1, state=state, width=1,
                textvariable=self.throttle, command=on_update, font=self.spinbox_font) \
            .grid(row=0, column=1, padx=5, pady=5)

    def draw_direction_controls(self, frames: Dict[str, Frame]) -> None:
        """
        Creates controls for gear controls.

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        if "direction" not in self.enabled:
            return
        enabled: bool = self.enabled["direction"]
        state = ("normal" if enabled else "disabled")

        frame: Frame = frames["direction_controls"]
        direction_controls_frame: LabelFrame = LabelFrame(frame, text="Direction")
        direction_controls_frame.grid(row=0, column=0)

        label_text: str = "Controls vehicle direction"
        Label(direction_controls_frame, justify="left", text=label_text, wraplength=170, anchor=NW, width=23) \
            .grid(row=0, column=0, sticky=N + S + W)

        HorizontalSpinbox(direction_controls_frame, from_=0, to_=10, increment=1, state=state,
                          on_update=self.controller.set_direction).grid(row=0, column=1, padx=5, pady=5)

    def draw_information(self, frames: Dict[str, Frame]) -> None:
        """
        Draws information part

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["info"]
        information_frame: LabelFrame = LabelFrame(frame, text="About")
        information_frame.grid(row=0, column=0, sticky=N + S + E + W)
        Label(information_frame, fg="grey", text="Author: Johannes Ernstsen", anchor=NW, width=35) \
            .grid(row=0, column=0, sticky=N + S + W)
        Label(information_frame, fg="grey", text="Ernstsen Software").grid(row=1, column=0, sticky=N + S + W)
        Label(information_frame, fg="grey", text=self.version).grid(row=2, column=0, sticky=N + S + E)


if __name__ == "__main__":
    misc_controls_dict: List[MiscControlSpec] = [
        MiscControlSpec(display_name="Lights", method=lambda v: print(v), param_type=bool, row=0, column=0)
    ]
    gui = GUI(misc_controls=misc_controls_dict)
    gui.mainloop()
