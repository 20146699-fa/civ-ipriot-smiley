from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)  # Red face
        self.draw_eyes()
        self.draw_mouth()

    def draw_eyes(self):
        # Angled angry eyebrows
        self.pixels[10] = self.BLANK   # above left eye
        self.pixels[13] = self.BLANK  # left eye
        self.pixels[18] = self.BLANK  # right eye
        self.pixels[21] = self.BLANK  # under right eye

    def draw_mouth(self):
        # Angry flat or downward mouth
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

if __name__ == "__main__":
    face = Angry()
    face.show()
    face.blink(0.5)
