from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.settings import SettingsWithSidebar

from settingsjson import gdax_api_settings_json, example_settings_json

Builder.load_string('''
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'open the settings!'
        font_size: 50
        on_release: app.open_settings()
''')


class Interface(BoxLayout):
    pass


class MainMenu(BoxLayout):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        b = Button(text="Settings", font_size=25, on_click=self.open_settings())
        layout.add_widget(b)
        return layout


class MainApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        return MainMenu()


class SettingsApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        setting = self.config.get('example', 'boolexample')
        return Interface()

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})

        config.setdefaults('gdax_api_settings', {
            'gdax_key': "Ax74...",
            'gdax_secret': "Tr73...",
            'gdax_passphrase': "L3e51..."})

    def build_settings(self, settings):
        settings.add_json_panel('GDAX API Settings',
                                self.config,
                                data=gdax_api_settings_json)
        settings.add_json_panel('Example Settings',
                                self.config,
                                data=example_settings_json)

    def on_config_change(self, config, section,
                         key, value):
        print(config, section, key, value)


if __name__ == "__main__":
    SettingsApp().run()
