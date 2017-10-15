from kivy.uix.listview import ListView, ListItemButton
from kivy.app import App
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.clock import mainthread


beans = {}


class TeamsView(ListView):

    name = StringProperty()

    def __init__(self, **kwargs):
        super(TeamsView, self).__init__(**kwargs)
        self.fetch_teams_from_database()
        self.set_adapter()
        self.save_bean()

    def fetch_teams_from_database(self):
        self.teams = [
            {'team': 'Pogoń Szczecin', 'score': '55'},
            {'team': 'Arizona State', 'score': '32'},
            {'team': 'Idaho', 'score': '44'},
            {'team': 'Nebraska', 'score': '48'},
            {'team': 'Accrington Stanley', 'score': '2'},
            {'team': 'Nottingham Forest', 'score': '3'}
        ]

    def set_adapter(self):
        self.adapter = ListAdapter(
            data=self.teams,
            args_converter=self.args_converter,
            selection_mode='single',
            allow_empty_selection=True,
            cls=ListItemButton
        )

        self.adapter.bind(
            on_selection_change=self.on_selection_change)

    def args_converter(self, row_index, item):
        return {
            'text': item['team'],
            'size_hint_y': None,
            'height': 50
        }

    def on_selection_change(self, adapter):
        team_score, team_name = self.get_team(adapter)
        team_score = '[size=50]' + team_score + '[/size]'

        beans['score_grid'].ids[self.name + '_name'].text =\
            team_name + ' score:'
        beans['score_grid'].ids[self.name + '_score'].text =\
            team_score

    def get_team(self, adapter):
        try:
            for team in self.teams:
                if team['team'] in adapter.selection[0].text:
                    return team['score'], team['team']
        except IndexError:
            return '', ''

    @mainthread
    def save_bean(self):
        beans[self.name + 'list'] = self.proxy_ref


class ScoreGrid(GridLayout):

    def __init__(self, **kwargs):
        super(ScoreGrid, self).__init__(**kwargs)
        beans['score_grid'] = self.proxy_ref


class DictionaryDisplaySelection(App):
    pass


if __name__ == "__main__":
    DictionaryDisplaySelection().run()
