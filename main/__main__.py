def run_random():
    from sense.SenseRandom import SenseRandom
    SenseRandom().run()


def run_line(random=False):
    from sense.SenseLineDrawer import SenseLineDrawer
    sld = SenseLineDrawer()
    if random:
        sld.auto_random()
    else:
        sld.auto()


def turn_off_sense():
    """Turn off all pixels on the display."""
    from sense_hat import SenseHat
    SenseHat().clear()


if __name__ == "__main__":
    print("Running main")
    run_line(random=True)
