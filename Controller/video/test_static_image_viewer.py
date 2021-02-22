import unittest
from tkinter import Label

from . import StaticImageViewer


class TestStaticImageViewer(unittest.TestCase):
    def test_sets_image(self):
        viewer: StaticImageViewer = StaticImageViewer(r"../../unnamed.png")

        viewer.set_label(Label())
        self.assertIsNotNone(viewer.label, msg="Label was not set!")

        viewer.video_stream_loop()
        self.assertIsNotNone(viewer.label.imgtk, msg="Image was not set on label!")


if __name__ == '__main__':
    unittest.main()
