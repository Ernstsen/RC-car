from tkinter import *

from typing import Dict


class GUI(Frame):

    def __init__(self, master=None):
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
        # noinspection PyDictCreation
        frames: Dict[str, Frame] = {}

        frames["stream_window"] = Frame(root_frame)
        frames["stream_window"].grid(row=0, column=0, rowspan=4, columnspan=5)

        frames["misc_controls"] = Frame(root_frame)
        frames["misc_controls"].grid(row=4, column=0)

        frames["drive_controls"] = Frame(root_frame)
        frames["drive_controls"].grid(row=0, column=5)

        frames["gear_controls"] = Frame(root_frame)
        frames["gear_controls"].grid(row=2, column=5)

        frames["throttle_controls"] = Frame(root_frame)
        frames["throttle_controls"].grid(row=3, column=5)

        frames["info"] = Frame(root_frame)
        frames["info"].grid(row=4, column=5, sticky=N + S + E + W)

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

        Radiobutton(misc_controls_frame, variable=self.drive, value=0, text="Hi").grid(row=0, column=0)
        Radiobutton(misc_controls_frame, variable=self.drive, value=1, text="Lo").grid(row=1, column=0)

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
        Label(information_frame, fg="grey", text="Author: Johannes Ernstsen").grid(row=0, column=0, sticky=N + S + W)
        Label(information_frame, fg="grey", text="Ernstsen Software").grid(row=1, column=0, sticky=N + S + W)
        Label(information_frame, fg="grey", text="Version=" + self.version).grid(row=2, column=0, sticky=N + S + W)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
