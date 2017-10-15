from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior


items = [
    {"text": "white",    "selected": 'normal', "input_data": ["some","random","data"]},
    {"text": "lightblue","selected": 'normal', "input_data": [1,6,3]},
    {"text": "blue",     "selected": 'normal', "input_data": [64,16,9]},
    {"text": "gray",     "selected": 'normal', "input_data": [8766,13,6]},
    {"text": "orange",   "selected": 'normal', "input_data": [9,4,6]},
    {"text": "yellow",   "selected": 'normal', "input_data": [852,958,123]},
    {"text": "white",    "selected": 'normal', "input_data": ["some","random","data"]},
    {"text": "lightblue","selected": 'normal', "input_data": [1,6,3]},
    {"text": "blue",     "selected": 'normal', "input_data": [64,16,9]},
    {"text": "gray",     "selected": 'normal', "input_data": [8766,13,6]},
    {"text": "orange",   "selected": 'normal', "input_data": [9,4,6]},
    {"text": "yellow",   "selected": 'normal', "input_data": [852,958,123]}
]


class MyViewClass(RecycleDataViewBehavior, BoxLayout):

    text = StringProperty("")
    index = None

    def set_state(self,state,app):
        app.root.ids.rv.data[self.index]['selected'] = state

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(MyViewClass, self).refresh_view_attrs(rv, index, data)


class MyRecycleView(RecycleView):

    data = items

    def print_data(self,data):
        print([item['input_data'] for item in data if item['selected'] == 'down'])


class RVCheckbox(App):
    pass


if __name__ == "__main__":
    RVCheckbox().run()
