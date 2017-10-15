from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty


Builder.load_string("""
<MyLayout>:
    Button:
        text: "Get data"
        on_press: root.get_data()
    RecycleView:
        data: [{'text':"Id:{} Brand:{} Km:{}".format(id,name,km)} for id,name,km in root.rows]
        viewclass: "Label"
        RecycleBoxLayout:
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
""")

test_data = [{'id': 'id', 'name': 'unknown', 'km': 'available'}]


class MyLayout(BoxLayout):
    rows = ListProperty([("Id","Brand","Km")])
    def get_data(self):
        self.rows = test_data
        print(self.rows)


runTouchApp(MyLayout())
