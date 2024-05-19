from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from helper import screen_helper
from mainscreen import MainScreen
from learn import LearnScreen, SecondLearnScreen
from account import Registration

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
sm.add_widget(LearnScreen(name='learn'))
sm.add_widget(SecondLearnScreen(name='secondlearn'))

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(screen_helper)
        return screen

    #Łączenie wszystkich funkcji z funkcją build
    def main_screen_function(self):
        main_screen = self.root.get_screen('main')
        main_screen.add_folder(self)
        main_screen.show_popup()
        main_screen.change()
        main_screen.translate()
        learn_screen = self.root.get_screen('learn')
        learn_screen.add_words()
        learn_screen.toggle_text()
        learn_screen.clear_word_container()
        second_learn_screen = self.root.get_screen('secondlearn')
        second_learn_screen.show_dialog()
        second_learn_screen.add_second_words()
        second_learn_screen.second_toggle_text()

    #Wywolanie funkcji change przy starcie aplikacji
    def on_start(self):
        self.root.get_screen('main').change()

    #Powrót do MainScreen z sekcji ustawień
    def change_screen(self, screen_name):
        self.root.current = screen_name

    #zmiana motywu 
    def lightdark(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    #Powrót do main i czyszczenie learn
    def handle_back_action(self):
        self.root.get_screen('learn').clear_word_container()
        self.change_screen('main')


if __name__ == "__main__":  
    DemoApp().run()