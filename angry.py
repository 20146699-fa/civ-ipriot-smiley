from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_eyes()
        self.draw_mouth()

    def draw_eyes(self):
        # Example of angry eyebrows
        self.pixels[10] = self.BLANK
        self.pixels[11] = self.BLANK
        self.pixels[14] = self.BLANK
        self.pixels[15] = self.BLANK

    def draw_mouth(self):
        # Frown mouth
        mouth = [49, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK


