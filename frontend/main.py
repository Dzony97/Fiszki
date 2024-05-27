from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from helper import screen_helper
from mainscreen import MainScreen
from learn import LearnScreen, SecondLearnScreen
import requests
import json

Window.size = (300, 500)

class WelcomeScreen(Screen):
    pass

class LoginScreen(Screen):

    def login_user(self):

        username = self.ids.userlogin.text
        password = self.ids.psswd.text

        data = {
            "username": username,
            "password": password
        }

        headers = {'Content-Type': 'application/json'} # send data in format JSON
        response = requests.post("http://127.0.0.1:8000/api/token/login/", data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            token_data = response.json()
            token_access = token_data['access']
            token_refresh = token_data['refresh']
            self.manager.current = 'main'
            print('Success')
        else:
            print(f"Login Failed. Status Code: {response.status_code}, Response: {response.text}")


class Registration(Screen):
    def register_user(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        repeat_password = self.ids.repeat_password.text

        if password == repeat_password:
            data = {
                "username": username,
                "email": email,
                "password": password
            }
            headers = {'Content-Type': 'application/json'} # send data in format JSON
            response = requests.post("http://127.0.0.1:8000/api/register/", data=json.dumps(data), headers=headers)
            if response.status_code == 201:
                self.manager.current = 'login'
            else:
                print(f"Registration failed. Status Code: {response.status_code}, Response: {response.text}")
        else:
            print("Passwords do not match")

class SettingsScreen(Screen):
    pass

#Change screen
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

    #Connected all functions with function build
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

    #Calling the change function at application startup
    def on_start(self):
        self.root.get_screen('main').change()

    #Back to MainScreen from settings
    def change_screen(self, screen_name):
        self.root.current = screen_name

    #Change theme
    def lightdark(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    #Back to main from clear learn
    def handle_back_action(self):
        self.root.get_screen('learn').clear_word_container()
        self.change_screen('main')


if __name__ == "__main__":  
    DemoApp().run()