# === Part 3: Refactoring (Flexible Colors) ===

# === STEP 1: Add complexion() method ===
# Location: smiley.py

def complexion(self):
    """
    Returns the default color for the smiley.
    """
    return self.YELLOW

# Now, replace any use of self.YELLOW in pixel definitions in the base or child classes
# with: self.complexion()

# === STEP 2: Constructor accepts complexion ===
# Location: smiley.py

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

# === STEP 3: Modify Sad to use BLUE ===
# Location: sad.py

class Sad(Smiley):
    def __init__(self):
        super().__init__(complexion=self.BLUE)  # Now appears blue
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

# === STEP 4: Leave Happy as default yellow ===
# Location: happy.py

class Happy(Smiley):
    def __init__(self):
        super().__init__()  # Uses default complexion (YELLOW)
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [41, 42, 43, 44, 45, 46]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [10, 13, 18, 21]
        eye_color = self.BLANK if wide_open else self.complexion()
        for pixel in eyes:
            self.pixels[pixel] = eye_color

# === STEP 5: Create Angry with RED color ===
# Location: angry.py

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_eyes()
        self.draw_mouth()

    def draw_eyes(self):
        # Angled brows (example)
        self.pixels[10] = self.BLANK
        self.pixels[11] = self.BLANK
        self.pixels[14] = self.BLANK
        self.pixels[15] = self.BLANK

    def draw_mouth(self):
        mouth = [49, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

# === STEP 6: Test in main.py ===

if __name__ == "__main__":
    from happy import Happy
    from sad import Sad
    from angry import Angry
    from time import sleep
    h = Happy()
    h.show()
    sleep(1)
    s = Sad()
    s.show()
    sleep(1)
    a = Angry()
    a.show()
    sleep(1)