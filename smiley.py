from sense_hat import SenseHat

class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    BLANK = (0, 0, 0)

    def __init__(self, complexion=None):
        self.sense_hat = SenseHat()
        self.my_complexion = complexion if complexion else self.YELLOW

        X = self.complexion()
        O = self.BLANK
        self.pixels = [
            O, X, X, X, X, X, X, O,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, X, O,
        ]

    def complexion(self):
        return self.my_complexion

    def dim_display(self, dimmed=True):
        self.sense_hat.low_light = dimmed

    def show(self):
        self.sense_hat.set_pixels(self.pixels)
