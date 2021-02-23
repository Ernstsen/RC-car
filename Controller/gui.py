from tkinter import *
from typing import Dict

from video import VideoViewer, StaticImageViewer


class GUI(Frame):
    """
    Class handling the graphics user interface of the application
    """

    def __init__(self, master=None, viewer: VideoViewer = StaticImageViewer(r"../unnamed.png"),
                 enabled: Dict[str, bool] = None):
        """
        Constructor for the graphics user interface

        :param master: master frame - from Frame constructor
        :param viewer: VideoViewer to display stream - defaults to static image
        :param enabled: map from strings to booleans for whether parts are enabled.
        If False for disabled, True for enabled and missing for non-displayed. Keys: 'misc, drive, gear, throttle'
        """
        # this will create a label widget
        Frame.__init__(self, master)

        self.master.title("Remote Vehicle Controller")
        self.master.resizable(width=FALSE, height=FALSE)
        self.version = "V0.1"
        self.img = None  # Initializes val img, containing placeholder for video stream
        self.drive: IntVar = IntVar()
        self.viewer = viewer

        if enabled is not None:
            self.enabled = enabled
        else:
            self.enabled: Dict[str, bool] = {
                "misc": True,
                "drive": True,
                "gear": True,
                "throttle": True
            }

        structure = self.build_frame_structure(master)

        self.draw_stream_window(structure)
        self.draw_misc_controls(structure)
        self.draw_drive_controls(structure)
        self.draw_gear_controls(structure)
        self.draw_throttle_controls(structure)
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
        frames["stream_window"].grid(row=0, column=0, rowspan=4, columnspan=5, sticky=NSEW, padx=padding, pady=padding)

        frames["misc_controls"] = Frame(root_frame)
        frames["misc_controls"].grid(row=4, column=0, sticky=NSEW, padx=padding, pady=padding)

        frames["drive_controls"] = Frame(root_frame)
        frames["drive_controls"].grid(row=0, column=5, sticky=NSEW, padx=padding, pady=padding)

        frames["gear_controls"] = Frame(root_frame)
        frames["gear_controls"].grid(row=2, column=5, sticky=NSEW, padx=padding, pady=padding)

        frames["throttle_controls"] = Frame(root_frame)
        frames["throttle_controls"].grid(row=3, column=5, sticky=NSEW, padx=padding, pady=padding)

        frames["info"] = Frame(root_frame)
        frames["info"].grid(row=4, column=5, sticky=NSEW, padx=padding, pady=padding)

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

    def draw_misc_controls(self, frames: Dict[str, Frame]) -> None:
        """
        Creates miscellaneous controls in frame 'misc_controls'

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        if "misc" not in self.enabled:
            return
        enabled: bool = self.enabled["misc"]
        state = ("active" if enabled else "disabled")

        frame: Frame = frames["misc_controls"]
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Miscellaneous Controls", width=250)
        misc_controls_frame.grid(row=0, column=0)
        Button(misc_controls_frame, text="Lights", state=state).grid(row=0, column=0)

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

        label_text = "This options controls the drive, and enables a user to choose between a high or low gearing " \
                     "between gearbox and wheels. Low gearing grants high torque and low speed, while High gearing " \
                     "grants the opposite tradeoff "

        Label(misc_controls_frame, width=35, wraplength=250, justify="left", state=state, text=label_text) \
            .grid(row=0, column=0)
        Radiobutton(misc_controls_frame, variable=self.drive, value=0, state=state, text="High gearing") \
            .grid(row=1, column=0)
        Radiobutton(misc_controls_frame, variable=self.drive, value=1, state=state, text="Low gearing") \
            .grid(row=2, column=0)

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

        Spinbox(misc_controls_frame, values=(1, 2, 3, 4), state=state).grid(row=0, column=0)

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
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Throttle")
        misc_controls_frame.grid(row=1, column=2)

        Spinbox(misc_controls_frame, values=(1, 2, 3, 4), state=state).grid(row=0, column=0)

    def draw_information(self, frames: Dict[str, Frame]) -> None:
        """
        Draws information part

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["info"]
        information_frame: LabelFrame = LabelFrame(frame, text="About", width=500, height=500)
        information_frame.grid(row=0, column=0, sticky=N + S + E + W)
        Label(information_frame, fg="grey", text="Author: Johannes Ernstsen", anchor=NW, width=35) \
            .grid(row=0, column=0, sticky=N + S + W)
        Label(information_frame, fg="grey", text="Ernstsen Software").grid(row=1, column=0, sticky=N + S + W)
        Label(information_frame, fg="grey", text=self.version).grid(row=2, column=0, sticky=N + S + E)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
