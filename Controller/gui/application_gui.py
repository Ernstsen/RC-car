from tkinter import *
from tkinter.font import Font
from typing import Dict, List

try:
    from Controller.gui.model import MiscControlSpec
    from Controller.gui.modules import *
    from Controller.vehicle_control import VehicleControllerI, ControllerSimulator, StreamControllerI
    from Controller.video import VideoViewer, StaticImageViewer
except ModuleNotFoundError:
    from .model import MiscControlSpec
    from .modules import *
    from vehicle_control import VehicleControllerI, ControllerSimulator, StreamControllerI
    from video import VideoViewer, StaticImageViewer


class GUI(Frame):
    """
    Class handling the graphics user interface of the application
    """

    def __init__(self, master: Frame = None,
                 viewer: VideoViewer = StaticImageViewer(r"../unnamed.png"),
                 stream_controller: StreamControllerI = StreamControllerI(),
                 enabled: Dict[str, bool] = None,
                 controller: VehicleControllerI = ControllerSimulator(),
                 misc_controls: List[MiscControlSpec] = None):
        """
        Constructor for the graphics user interface

        default values does not communicate with other instances

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
        self.viewer: VideoViewer = viewer
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
        self.draw_cam_feed_controls(master, stream_controller)

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
        StreamFrame(frame, self.viewer).grid(sticky=N + S + E + W)

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
        MiscControlsModule(master=frame, misc_controls=misc_controls, state=state).grid(sticky=N + S + E + W)

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
        DriveControls(frame, state=state, set_drive=self.controller.set_drive).grid(sticky=N + S + E + W)

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
        GearControls(frame, state=state, set_gear=self.controller.set_drive, font=self.spinbox_font) \
            .grid(sticky=N + S + E + W)

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
        ThrottleControls(frame, state=state, set_throttle=self.controller.set_throttle, font=self.spinbox_font) \
            .grid(sticky=N + S + E + W)

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
        DirectionControls(frame, state=state, set_direction=self.controller.set_direction).grid(sticky=N + S + E + W)

    def draw_information(self, frames: Dict[str, Frame]) -> None:
        """
        Draws information part

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["info"]
        InformationFrame(frame, self.version).grid(sticky=N + S + E + W)

    def draw_cam_feed_controls(self, master: Frame, controller: StreamControllerI) -> None:
        top_bar = Menu(master)
        self.master.config(menu=top_bar)

        cam_controls_menu = Menu(top_bar, tearoff=0)

        cam_controls_menu.add_command(label="Start Streaming", command=controller.start_stream)
        cam_controls_menu.add_command(label="Stop Steaming", command=controller.stop_stream)
        top_bar.add_cascade(label="Video", menu=cam_controls_menu, underline=0)


if __name__ == "__main__":
    misc_controls_dict: List[MiscControlSpec] = [
        MiscControlSpec(display_name="Lights", on_change=lambda v: print(v), param_type=bool, row=0, column=0)
    ]
    gui = GUI(viewer=StaticImageViewer(r"../../unnamed.png"), misc_controls=misc_controls_dict)
    gui.mainloop()
