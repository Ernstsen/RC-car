from tkinter import *


class GUI(Frame):

    def __init__(self, master=None):
        # this will create a label widget
        Frame.__init__(self, master)
        self.master.title("Remote Vehicle Controller")

        self.img = None  # Initializes val img, containing placeholder for video stream
        stream_frame = Frame(master)
        stream_frame.grid(row=0, column=0)
        self.draw_stream_window(stream_frame)

        misc_controls_frame_outer = Frame(master)
        misc_controls_frame_outer.grid(row=1, column=0)
        misc_controls_frame = LabelFrame(misc_controls_frame_outer, text="Miscellaneous Controls", width=250)
        misc_controls_frame.grid(row=0, column=0)
        Button(misc_controls_frame, text="Lights").grid(row=0, column=0)

    def draw_stream_window(self, frame: Frame) -> None:
        """
        Fills frame with video-stream
        (For now simply some PNG, as a placeholder)
        :param frame: frame to draw stream in
        """
        # Placeholder for video stream
        self.img = PhotoImage(file=r"..\unnamed.png")
        Label(frame, image=self.img).grid(row=0, column=0, columnspan=2, rowspan=2, padx=5, pady=5)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
