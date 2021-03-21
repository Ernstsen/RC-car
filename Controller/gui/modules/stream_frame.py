import threading
from tkinter import Frame, LabelFrame, Label

try:
    from Controller.video import VideoViewer
except ModuleNotFoundError:
    from video import VideoViewer


class StreamFrame(Frame):
    """
    Container for video-stream display
    """

    def __init__(self, parent, viewer: VideoViewer):
        """
        :param parent: parent frame to render content in
        :param viewer: the viewer used in interfacing with stream source
        """
        Frame.__init__(self, parent)

        self.misc_controls_frame: LabelFrame = LabelFrame(parent, text="Video Stream")
        label = Label(self.misc_controls_frame)
        label.grid(row=0, column=0, columnspan=2, rowspan=2, padx=5, pady=5)
        viewer.set_label(label)
        stream_thread = threading.Thread(target=viewer.video_stream_loop)
        stream_thread.start()

    def grid(self, row=0, column=0, **kwargs):
        self.misc_controls_frame.grid(row=row, column=column, **kwargs)
