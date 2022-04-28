from sense_hat import SenseHat
import random
import time

class SenseRandom:
    def __init__(self, min_color=50, max_color=150):
        self.min_color = min_color
        self.max_color = max_color
        self.sense = SenseHat()
        self.initialize_random()

    def initialize_random(self):
        for x in range(0,8):
            for y in range(0,8):
                self.sense.set_pixel(x, y, self.random_color())

    def run(self):
        while True:
            time.sleep(0.01)
            self.sense.set_pixel(
                random.randint(0, 7),
                random.randint(0, 7),
                self.random_color(),
            )

    def random_color(self):
        return (
            random.randint(self.min_color, self.max_color),
            random.randint(self.min_color, self.max_color),
            random.randint(self.min_color, self.max_color),
        )