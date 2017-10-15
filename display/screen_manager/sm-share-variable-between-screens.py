from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty

Builder.load_string("""
<ScreenManagement>:
    id: screen_manager
    LoginScreen:
        id: login_screen
        name: 'screen_1'
        manager: screen_manager
        menu_screen_text: menu_screen.ids.lbl2.text
    MenuScreen:
        id: menu_screen
        name: 'screen_2'
        manager: screen_manager
        login_screen_text: login_screen.ids.lbl1.text
        
<LoginScreen>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'I am LoginScreen'
        Label:
            id: lbl1
            text: root.menu_screen_text
        Button:
            text: 'Read'
            on_press: root.press_read()
        Button:
            text: 'Change'
            on_press:
                app.press_change()
                root.ids.lbl1.text = 'SharedVar is ' + str(app.MY_NUMBER)
        Button:
            text: 'Go to ScreenTwo'
            on_press:
                app.root.current = "screen_2"

<MenuScreen>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text: 'I am MenuScreen'
        Label:
            id: lbl2
            text: root.login_screen_text
        Button:
            text: 'Read'
            on_press: root.press_read()
        Button:
            text: 'Change'
            on_press:
                app.press_change()
                root.ids.lbl2.text = 'SharedVar is ' + str(app.MY_NUMBER)
        Button:
            text: 'Go to ScreenOne'
            on_press:
                app.root.current = "screen_1"
""")


class ScreenManagement(ScreenManager):
    pass


class LoginScreen(Screen):
    menu_screen_text = StringProperty('')

    def press_read(self):
        app = App.get_running_app()
        self.ids.lbl1.text = "SharedVar is " + str(app.MY_NUMBER)


class MenuScreen(Screen):
    login_screen_text = StringProperty('')

    def press_read(self):
        app = App.get_running_app()
        self.ids.lbl2.text = "SharedVar is now " + str(app.MY_NUMBER)


class HandSetApp(App):
    MY_NUMBER = 0

    def build(self):
        return ScreenManagement()

    def press_change(self):
        self.MY_NUMBER += 1


if __name__ == '__main__':
    HandSetApp().run()
