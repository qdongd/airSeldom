from airrun.config import AirTest


class Switch:
    """
    switch context by appium
    """

    def __init__(self, poco=AirTest.air_poco):
        self.poco = poco
