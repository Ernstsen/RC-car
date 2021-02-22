# Video

The video module contains support for displaying image or video material as part of the user interface

``VideoViewer`` defines the interface to be used when handling images, or implementing own implementations of
image/video display to be used with the rest of the system

The implementations provided are

* ``StaticImageViewer`` which displays a provided image
* ``VideoStreamReceiver`` which receives a video-stream through a web-socket and displays the received imagery