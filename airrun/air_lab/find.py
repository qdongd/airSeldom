from airrun.air_lab.switch import Switch
from seldom.logging import log


class Find(Switch):
    def find_element(self, element):
        log.info(f"🔍︎find -> {element}")
        elem = self.poco(element)
        return elem
