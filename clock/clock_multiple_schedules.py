from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import Screen

import time


Builder.load_string("""
<SelectableLabel>:
    padding: .2, .2
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (0, 1, 1, 1) if self.selected else (0.5, 0.5, 0.5, 1)
        Rectangle:
            pos: self.pos
            size: self.size

<ClockScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            id: clock_label
        BoxLayout:
            orientation: "horizontal"
            SelectableLabel:
                text: "Bitcoin"
                id: bitcoin_label
            SelectableLabel:
                text: "Litecoin"
                id: litecoin_label
            SelectableLabel:
                text: "Ethereum"
                id: ethereum_label
""")


class CoinSimple(Label):
    def __init__(self, coin, **kwargs):
        super(CoinSimple, self).__init__(**kwargs)
        self.text = coin

    # def update(self, coin):
    #     self.selected = true


class SelectableLabel(Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class ClockScreen(Screen):
    def __init__(self, **kwargs):
        super(ClockScreen, self).__init__(**kwargs)
        self.ids.clock_label.text = time.asctime()

    def update(self, *args):
        self.ids.clock_label.text = time.asctime()

    def bitcoin(self, *args):
        self.ids.bitcoin_label.selected = True
        Clock.schedule_once(self.bitcoin_off, 1/10)

    def bitcoin_off(self, *args):
        self.ids.bitcoin_label.selected = False

    def litecoin(self, *args):
        self.ids.litecoin_label.selected = True
        Clock.schedule_once(self.litecoin_off, 1 / 10)

    def litecoin_off(self, *args):
        self.ids.litecoin_label.selected = False

    def ethereum(self, *args):
        self.ids.ethereum_label.selected = True
        Clock.schedule_once(self.ethereum_off, 1 / 10)

    def ethereum_off(self, *args):
        self.ids.ethereum_label.selected = False


        # coin_simple = CoinSimple("Bitcoin")
        # btc = Clock.schedule_interval(coin_simple.update, 3)
        # ltc = Clock.schedule_interval(print("Litecoin"), 30)
        # eth = Clock.schedule_interval(print("Ethereum"), 10)
        # btc()
        # return clock_simple


class TimeApp(App):
    def build(self):
        clock_simple = ClockScreen()
        Clock.schedule_interval(clock_simple.update, 1)
        Clock.schedule_interval(clock_simple.bitcoin, 1/2)
        Clock.schedule_interval(clock_simple.litecoin, 1/3)
        Clock.schedule_interval(clock_simple.ethereum, 1/5)
        return clock_simple


if __name__ == "__main__":
    TimeApp().run()
