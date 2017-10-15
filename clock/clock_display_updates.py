from __future__ import division
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.lang import Builder


Builder.load_string('''
<Ex28>:
    cols: 2
    canvas:
        Color:
            rgb: 0,0,1
        Rectangle:
            size: root.width,root.height
            pos: 0,0
        Color:
            rgb: 1, 0, 1
        Line:
            points: 0,root.height/2, root.width,root.height/2
            width: 5
        Line:
            points: root.width/2,0, root.width/2,root.height
            width: 5
        Color:
            rgb: .25, .25, .25
        Line:
            rectangle: 100,100, 200,150
            width: 5
        Line:
            rectangle: root.width/2+100,100, 200,150
            width: 5
        Line:
            rectangle: 100,root.height/2+100, 200,150
            width: 5
        Line:
            rectangle: root.width/2+100,root.height/2+100, 200,150
            width: 5
    Label:
        size_hint_y: .8
        text: '[size=32]'+str(root.counter1)+'[/size]'
        markup: True
    Label:
        size_hint_y: .8
        text: '[size=32]'+str(root.counter2)+'[/size]'
        markup: True
    Button:
        size_hint_y: .2
        text: '[size=32]1 Hertz[/size]'
        markup: True
        on_press: root.counter1=0
    Button:
        size_hint_y: .2
        text: '[size=32]2 Hertz[/size]'
        markup: True
        on_press: root.counter2=0
    Label:
        size_hint_y: .8
        text: '[size=32]'+str(root.counter3)+'[/size]'
        markup: True
    Label:
        size_hint_y: .8
        text: '[size=32]'+str(root.counter4)+'[/size]'
        markup: True
    Button:
        size_hint_y: .2
        text: '[size=32]3 Hertz[/size]'
        markup: True
        on_press: root.counter3=0
    Button:
        size_hint_y: .2
        text: '[size=32]4 Hertz[/size]'
        markup: True
        on_press: root.counter4=0
''')


class Ex28(GridLayout):
    counter1 = NumericProperty(0)
    counter2 = NumericProperty(0)
    counter3 = NumericProperty(0)
    counter4 = NumericProperty(0)

    def update1(self, dt): self.counter1 += 1

    def update2(self, dt): self.counter2 += 1

    def update3(self, dt): self.counter3 += 1

    def update4(self, dt): self.counter4 += 1


class Ex28App(App):
    def build(self):
        ex28 = Ex28()
        Clock.schedule_interval(ex28.update1, 1)
        Clock.schedule_interval(ex28.update2, 1 / 2)
        Clock.schedule_interval(ex28.update3, 1 / 3)
        Clock.schedule_interval(ex28.update4, 1 / 4)
        return ex28


if __name__ == '__main__':
    Ex28App().run()
