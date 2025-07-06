from smiley import Smiley

class Sad(Smiley):
    def __init__(self):
        super().__init__(complexion=self.BLUE)  # Make it BLUE!
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [10, 13, 18, 21]
        eye_color = self.BLANK if wide_open else self.complexion()
        for pixel in eyes:
            self.pixels[pixel] = eye_color



from sad import Sad

if __name__ == "__main__":
    face = Sad()
    face.show()
    face.blink(0.5)
