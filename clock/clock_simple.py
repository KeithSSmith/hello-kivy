from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

import time


class ClockSimple(Label):
    def update(self, *args):
        self.text = time.asctime()


class TimeApp(App):
    def build(self):
        clock_simple = ClockSimple()
        Clock.schedule_interval(clock_simple.update, 1)
        return clock_simple


if __name__ == "__main__":
    TimeApp().run()
