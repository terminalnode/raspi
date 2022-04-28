import random
import time

from sense_hat import SenseHat

class SenseLineDrawer:
    def __init__(self, fg=(0,50,0), bg=(50,0,0)):
        self.sense = SenseHat()

        # Variables indicating foreground/background color
        self.fg = fg
        self.bg = bg

        # Variables indicating position and if going in reverse
        self.x = 0
        self.xr = False
        self.y = 0
        self.yr = False

    def initialize_bg(self):
        for x in range(0,8):
            for y in range(0,8):
                self.sense.set_pixel(x, y, self.bg)

    def auto(self):
        while True:
            self.vdraw()
            self.hdraw()
            time.sleep(0.1)

    def auto_random(self):
        while True:
            if random.randint(0 , 100) < 5:
                self.vdraw()
            if random.randint(0, 100) < 10:
                self.hdraw()
            time.sleep(0.01)

    def vdraw(self):
        prev = self.x
        self.vinc()
        for y in range(0,8):
            self.sense.set_pixel(self.x, y, self.fg)
            if y == self.y: continue
            self.sense.set_pixel(prev, y, self.bg)

    def vinc(self):
        if self.x == 0 or self.x == 7:
            self.xr = not self.xr
        self.x = self.x + 1 if self.xr else self.x - 1

    def hdraw(self):
        prev = self.y
        self.hinc()
        for x in range(0,8):
            self.sense.set_pixel(x, self.y, self.fg)
            if x == self.x: continue
            self.sense.set_pixel(x, prev, self.bg)

    def hinc(self):
        if self.y == 0 or self.y == 7:
            self.yr = not self.yr
        self.y = self.y + 1 if self.yr else self.y - 1
