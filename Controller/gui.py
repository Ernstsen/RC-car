from tkinter import *

from typing import Dict


class GUI(Frame):
    """
    Class handling the graphics user interface of the application
    """

    def __init__(self, master=None):
        """
        Constructor for the graphics user interface

        :param master: master frame - from Frame constructor
        """
        # this will create a label widget
        Frame.__init__(self, master)

        self.master.title("Remote Vehicle Controller")
        self.master.resizable(width=FALSE, height=FALSE)
        self.version = "V0.1"
        self.img = None  # Initializes val img, containing placeholder for video stream
        self.drive: IntVar = IntVar()

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
        frames["stream_window"].grid(row=0, column=0, rowspan=4, columnspan=5, sticky=N + S + E + W, padx=padding,
                                     pady=padding)

        frames["misc_controls"] = Frame(root_frame)
        frames["misc_controls"].grid(row=4, column=0, sticky=N + S + E + W, padx=padding, pady=padding)

        frames["drive_controls"] = Frame(root_frame)
        frames["drive_controls"].grid(row=0, column=5, sticky=N + S + E + W, padx=padding, pady=padding)

        frames["gear_controls"] = Frame(root_frame)
        frames["gear_controls"].grid(row=2, column=5, sticky=N + S + E + W, padx=padding, pady=padding)

        frames["throttle_controls"] = Frame(root_frame)
        frames["throttle_controls"].grid(row=3, column=5, sticky=N + S + E + W, padx=padding, pady=padding)

        frames["info"] = Frame(root_frame)
        frames["info"].grid(row=4, column=5, sticky=N + S + E + W, padx=padding, pady=padding)

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
        self.img = PhotoImage(file=r"..\unnamed.png")
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Video Stream")
        misc_controls_frame.grid(row=0, column=0)
        Label(misc_controls_frame, image=self.img).grid(row=0, column=0, columnspan=2, rowspan=2, padx=5, pady=5)

    @staticmethod
    def draw_misc_controls(frames: Dict[str, Frame]) -> None:
        """
        Creates miscellaneous controls in frame 'misc_controls'

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["misc_controls"]
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Miscellaneous Controls", width=250)
        misc_controls_frame.grid(row=0, column=0)
        Button(misc_controls_frame, text="Lights").grid(row=0, column=0)

    def draw_drive_controls(self, frames: Dict[str, Frame]) -> None:
        """
        Creates controls for drive controls.
        Options are hi and lo, for high or low gearing.

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["drive_controls"]
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Drive")
        misc_controls_frame.grid(row=0, column=2)

        label_text = "This options controls the drive, and enables a user to choose between a high or low gearing " \
                     "between gearbox and wheels. Low gearing grants high torque and low speed, while High gearing " \
                     "grants the opposite tradeoff "

        Label(misc_controls_frame, width=35, wraplength=250, justify="left", text=label_text).grid(row=0, column=0)
        Radiobutton(misc_controls_frame, variable=self.drive, value=0, text="High gearing").grid(row=1, column=0)
        Radiobutton(misc_controls_frame, variable=self.drive, value=1, text="Low gearing").grid(row=2, column=0)

    @staticmethod
    def draw_gear_controls(frames: Dict[str, Frame]) -> None:
        """
        Creates controls for gear controls.

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["gear_controls"]
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Gear")
        misc_controls_frame.grid(row=1, column=2)

        Spinbox(misc_controls_frame, values=(1, 2, 3, 4)).grid(row=0, column=0)

    @staticmethod
    def draw_throttle_controls(frames: Dict[str, Frame]) -> None:
        """
        Creates controls for gear controls.

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["throttle_controls"]
        misc_controls_frame: LabelFrame = LabelFrame(frame, text="Throttle")
        misc_controls_frame.grid(row=1, column=2)

        Spinbox(misc_controls_frame, values=(1, 2, 3, 4)).grid(row=0, column=0)

    def draw_information(self, frames: Dict[str, Frame]) -> None:
        """
        Draws information part

        :type frames: frames dictionary. Maps string to Frame
        :param frames: frame dictionary
        """
        frame: Frame = frames["info"]
        information_frame: LabelFrame = LabelFrame(frame, text="About", width=500, height=500)
        information_frame.grid(row=0, column=0, sticky=N + S + E + W)
        Label(information_frame, fg="grey", text="Author: Johannes Ernstsen", width=35).grid(row=0, column=0,
                                                                                             sticky=N + S + W)
        Label(information_frame, fg="grey", text="Ernstsen Software").grid(row=1, column=0, sticky=N + S + W)
        Label(information_frame, fg="grey", text=self.version).grid(row=2, column=0, sticky=N + S + E)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
