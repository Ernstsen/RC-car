# Reads stream from cam_streamer.py and displays it in window.
# This is technically the server- should be renamed when re-written
import io
import struct
import threading
import time
from tkinter import *

from PIL import ImageTk, Image

try:
    from Controller.communication.server_utilities import create_server
    from Controller.video.video_viewer import VideoViewer
except ModuleNotFoundError:
    from communication.server_utilities import create_server
    from .video_viewer import VideoViewer


# noinspection PyBroadException
class VideoStreamReceiver(VideoViewer):
    """
    class for handling the video-stream from the Raspberry Pi
    """

    def __init__(self, port: int = 8000):
        """
        :param port: port to be used when receiving video stream - must be free on this device, as a server is created
        """

        self.server_socket = create_server(port)
        self.display_label = None
        self.connection = None
        self.terminate = False

    def set_label(self, display_label: Label):
        self.display_label = display_label

    def video_stream_loop(self) -> bool:
        """
        The stream loop, which reads the loop and updates the label with the new images
        Does not terminate until an error occurs or self.terminate becomes True

        :return: False if an error occurs, True otherwise
        """
        # Accept a single connection and make a file-like object out of it
        self.connection = self.server_socket.accept()[0].makefile('rb')

        try:
            while True:
                elapsed = time.time()
                # Read the length of the image as a 32-bit unsigned int. If the length is zero, quit the loop
                image_len = struct.unpack('<L', self.connection.read(4))[0]
                if (not image_len) or self.terminate:
                    return True
                # Construct a stream to hold the image data and read the image data from the connection
                image_stream = io.BytesIO()
                image_stream.write(self.connection.read(image_len))
                # Rewind the stream, open it as an image with PIL and do some processing on it
                image_stream.seek(0)
                image = Image.open(image_stream)
                img_tk = ImageTk.PhotoImage(image=image)
                self.display_label.imgtk = img_tk
                self.display_label.configure(image=img_tk)
                print("Display took: " + str(elapsed - time.time()))
        except Exception:
            print("Something unexpected happened, causing the stream to crash")
            return False
        finally:
            self.connection.close()
            self.server_socket.close()


def run_test() -> None:
    """
    Creates a tkinter window and displays the stream inside it.
    """
    root = Tk()
    # Create a frame
    app = Frame(root, bg="white")
    app.grid()
    # Create a label in the frame
    label: Label = Label(app)
    label.grid()
    receiver = VideoStreamReceiver()
    receiver.set_label(label)

    stream_thread = threading.Thread(target=receiver.video_stream_loop)
    stream_thread.start()
    root.mainloop()


if __name__ == "__main__":
    run_test()
