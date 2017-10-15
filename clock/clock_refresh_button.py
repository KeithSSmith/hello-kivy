from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import time

Builder.load_string("""
<Button>:
    font_size: 25
    size_hint: 0, 0.1

<Label>:
    size_hint: 0.3, 0.1

<ButtonRefreshTime>:
    push_button_display_time: label_display_time
    orientation: 'vertical'
    padding: 30
    spacing: 10

    BoxLayout:
        Button:
            id: button_get_time
            text: "Get Time"
            pos_hint: {"x": 0, "y": .45}
            on_press: root.get_time()
        Label:
            id: label_display_time
            pos_hint: {"x": 0, "y": .45}
""")


class ButtonRefreshTime(Screen):
    def __init__(self, **kwargs):
        super(ButtonRefreshTime, self).__init__(**kwargs)
        self.push_button_display_time.text = time.asctime()

    def get_time(self):
        self.push_button_display_time.text = time.asctime()


class RefreshTime(App):
    def build(self):
        return ButtonRefreshTime()


if __name__ == "__main__":
    RefreshTime().run()
