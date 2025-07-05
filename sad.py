from smiley import Smiley
from time import sleep

class Sad(Smiley):
    def __init__(self):
        super().__init__()
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eye_pixels = [10, 13, 18, 21]
        eye_color = self.BLANK if wide_open else self.YELLOW
        for pixel in eye_pixels:
            self.pixels[pixel] = eye_color

    def blink(self, delay=0.25):
        """
        Blink the eyes by momentarily "closing" them.
        """
        original = self.pixels[:]

        self.draw_eyes(wide_open=False)
        self.show()
        sleep(delay)

        self.pixels = original
        self.show()
        sleep(delay)
from sad import Sad

if __name__ == "__main__":
    face = Sad()
    face.show()
    face.blink(0.5)
