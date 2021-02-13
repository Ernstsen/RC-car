# Reads stream from cam_streamer.py and displays it in window.
# This is technically the server- should be renamed when re-written
import io
import socket
import struct
from tkinter import *
from PIL import ImageTk, Image

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)
i = 1
# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')


root = Tk()
# Create a frame
app = Frame(root, bg="white")
app.grid()
# Create a label in the frame
lmain = Label(app)
lmain.grid()

try:
    # while True:
    def video_stream():
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(4))[0]
        if not image_len:
            raise Exception("stop loop, empty message received")
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)
        imgtk = ImageTk.PhotoImage(image=image)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, video_stream)

    video_stream()
    root.mainloop()
finally:
    connection.close()
    server_socket.close()


