from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from helper import screen_helper
from mainscreen import MainScreen

Window.size = (300, 500)

class WelcomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class Registration(Screen):
    pass

class SettingsScreen(Screen):
    pass

#Przełączanie screen
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(Registration(name='registration'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        screen = Builder.load_string(screen_helper)
        return screen

    #Łączenie wszystkich funkcji z funkcją build
    def on_add_folder_button_press(self):
        main_screen = self.root.get_screen('main')
        main_screen.add_folder(self)
        main_screen.show_popup()
        main_screen.change()

    #Powrót do MainScreen z sekcji ustawień
    def change_screen(self, screen_name):
        self.root.current = screen_name

if __name__ == "__main__":
    DemoApp().run()