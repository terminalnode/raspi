import random
import time

from sense_hat import SenseHat


class SenseLineDrawer:
    def __init__(self, fg=(0, 50, 0), bg=(50, 0, 0)):
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
        """Draw the entire grid in the background colour."""
        for x in range(0,8):
            for y in range(0,8):
                self.sense.set_pixel(x, y, self.bg)

    def auto(self):
        """Draw the lines automatically.

        Every tick the vertical and horizontal lines both progress.

        Each tick lasts for 0.1 seconds.
        """
        while True:
            self.vdraw()
            self.hdraw()
            time.sleep(0.1)

    def auto_random(self):
        """Draw the lines at random pace.

        Every tick there's a 5% chance of progressing the vertical line,
        and 10% chance of progressing the horizontal line.

        Each tick lasts for 0.01 seconds.
        """
        while True:
            if random.randint(0, 100) < 5:
                self.vdraw()
            if random.randint(0, 100) < 10:
                self.hdraw()
            time.sleep(0.01)

    def vdraw(self):
        """Draw a vertical line.

        Steps:
         - Overwrite the previous vertical line with background color.
         - Increment the x-coordinate.
         - Draw a new vertical line.
        """
        prev = self.x
        self.vinc()
        for y in range(0,8):
            self.sense.set_pixel(self.x, y, self.fg)
            if y == self.y: continue
            self.sense.set_pixel(prev, y, self.bg)

    def vinc(self):
        """Increase the vertical coordinate (x)

        If the x-coordinate is at the edges of the display, direction will also be reversed.
        """
        if self.x == 0 or self.x == 7:
            self.xr = not self.xr
        self.x = self.x + 1 if self.xr else self.x - 1

    def hdraw(self):
        """Draw a horizontal line.

        Steps:
         - Overwrite the previous horizontal line with background color.
         - Increment the y-coordinate.
         - Draw a new horizontal line.
        """
        prev = self.y
        self.hinc()
        for x in range(0,8):
            self.sense.set_pixel(x, self.y, self.fg)
            if x == self.x: continue
            self.sense.set_pixel(x, prev, self.bg)

    def hinc(self):
        """Increase the horizontal coordinate (y)

        If the y-coordinate is at the edges of the display, direction will also be reversed.
        """
        if self.y == 0 or self.y == 7:
            self.yr = not self.yr
        self.y = self.y + 1 if self.yr else self.y - 1
