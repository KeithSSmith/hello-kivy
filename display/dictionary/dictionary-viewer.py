from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class TableHeader(Label):
    pass


class TableRecord(Label):
    pass


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.fetch_data_from_database()
        self.display_scores()

    def fetch_data_from_database(self):
        self.data = [
            {'name': 'name', 'score': 'score', 'car': 'car'},
            {'name': 'John Cage', 'score': '1337', 'car': 'Fiat 126p'},
            {'name': 'Nick Cage', 'score': '777', 'car': 'Renault'},
            {'name': 'James May', 'score': '3', 'car': 'Caravan'},
            {'name': 'Richard Hammond', 'score': '8', 'car': 'Porsche'}
        ]

    def display_scores(self):
        self.clear_widgets()
        for i in range(len(self.data)):
            if i < 1:
                row = self.create_header(i)
            else:
                row = self.create_table_info(i)
            for item in row:
                self.add_widget(item)

    def create_header(self, i):
        first_column = TableHeader(text=self.data[i]['name'])
        second_column = TableHeader(text=self.data[i]['score'])
        third_column = TableHeader(text=self.data[i]['car'])
        return [first_column, second_column, third_column]

    def create_table_info(self, i):
        first_column = TableRecord(text=self.data[i]['name'])
        second_column = TableRecord(text=self.data[i]['score'])
        third_column = TableRecord(text=self.data[i]['car'])
        return [first_column, second_column, third_column]


class DictionaryViewerApp(App):
    pass


if __name__ == "__main__":
    DictionaryViewerApp().run()
