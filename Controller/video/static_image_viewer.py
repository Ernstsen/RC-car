from tkinter import Label, PhotoImage

from .video_viewer import VideoViewer


class StaticImageViewer(VideoViewer):
    """
    Implementation of VideoViewer displaying a static image
    """

    def __init__(self, image_name: str):
        self.image_name: str = image_name
        self.label = None
        self.img = None

    def set_label(self, display_label: Label):
        self.label: Label = display_label

    def video_stream_loop(self) -> None:
        self.img: PhotoImage = PhotoImage(file=self.image_name)
        self.label.imgtk = self.img
        self.label.configure(image=self.img)
