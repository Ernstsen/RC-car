from tkinter import Label


class VideoViewer(object):
    """
    Displays stream in a label
    """

    def set_label(self, display_label: Label):
        """
        :param display_label: label used to display stream inside
        """

    ...

    def video_stream_loop(self) -> None:
        """
        The stream loop, which reads the loop and updates the label with the new images
        Does not terminate until an error occurs or self.terminate becomes True

        :return: False if an error occurs, True otherwise
        """

    ...
