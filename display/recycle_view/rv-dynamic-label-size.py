from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class CollapsingBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CollapsingBoxLayout, self).__init__(**kwargs)
        self._trigger_update_size = Clock.create_trigger(self._update_size)

    def on_children(self, *_):
        for c in self.children:
            c.bind(size=self._trigger_update_size)
        self._trigger_update_size()

    def _update_size(self, *_):
        if self.size_hint_y is None:
            self.height = max(c.height for c in self.children) if self.children else 0
        if self.size_hint_x is None:
            self.width = max(c.width for c in self.children) if self.children else 0


root = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    CollapsingBoxLayout:
        size_hint_y: None

        canvas.before:
            Color:
                rgba: 1, 0, 0, 0.2
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'Paragraph 1'
            size_hint_x: 0.2
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
        Label:
            canvas.before:
                Color:
                    rgba: 0, 1, 0, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_x: 0.8
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sollicitudin dignissim orci. Pellentesque laoreet magna quis augue dictum fringilla. Vivamus nec adipiscing nunc. Aliquam pharetra auctor justo vel rutrum. Sed sodales nulla sed odio fermentum, vel pulvinar nibh hendrerit. Phasellus a volutpat leo. Donec id hendrerit velit. Curabitur eget suscipit neque, nec tincidunt nulla. Donec feugiat, urna quis porttitor aliquet, nibh est laoreet ligula, vitae vestibulum leo purus quis ante. Maecenas magna nisi, molestie eu ipsum quis, tempor tempor turpis. Vivamus a fringilla enim. Quisque aliquam elit tortor, nec mollis tellus facilisis accumsan. Phasellus sagittis commodo mauris in vestibulum. Mauris sed ultrices enim.'
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None

    CollapsingBoxLayout:
        size_hint_y: None

        canvas.before:
            Color:
                rgba: 0, 0, 1, 0.2
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'Paragraph 2'
            size_hint_x: 0.2
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
        Label:
            canvas.before:
                Color:
                    rgba: 0, 1, 0, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_x: 0.8
            text: 'Duis egestas dui lobortis ante rutrum, nec consectetur arcu sollicitudin. Phasellus ut felis facilisis, eleifend odio malesuada, placerat odio. Etiam convallis non mi at tempor. Nunc gravida est magna, a hendrerit nulla condimentum a. Proin tristique velit quis dui convallis, vitae sodales nunc condimentum. In sollicitudin eros augue, sit amet blandit neque accumsan eu. Mauris non risus at nisl vestibulum dignissim quis non arcu. Integer ullamcorper felis eu neque viverra placerat. Vivamus magna quam, porta ac tincidunt a, imperdiet sed purus. Phasellus tempus ac neque vel accumsan. Pellentesque ligula justo, auctor eget aliquet ultricies, volutpat scelerisque ligula. Maecenas dictum velit id neque rhoncus fermentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur dictum enim nisl, ut elementum lectus viverra sit amet. Praesent vel tempor risus, at congue turpis. Praesent in justo lobortis, gravida lacus id, facilisis orci.'
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
''')


class TestApp(App):
    def build(self):
        lbl = Label(text=('hello this is some long long text! ' * 10), size_hint_y=None)
        lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        lbl.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        root.add_widget(lbl)
        return root


if __name__ == '__main__':
    TestApp().run()