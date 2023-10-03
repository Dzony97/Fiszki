from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label

from helper import screen_helper


Window.size = (300, 500)

class Content(MDBoxLayout):
    pass

#Widget z okna popup
class CustomWidget(MDBoxLayout):
    text = ""

    def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs)
        self.size_hint_y = None  
        self.height = "48dp"

class WelcomeScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class Registration(Screen):
    pass

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.button_state = False

    dialog = None
    
    # Okno popup odpowiadające za tworzenie nowych folderów
    def show_popup(self):
        
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Hint",
                        on_release = self.close_popup
                    ),
                    MDFlatButton(
                        text="ADD",
                        theme_text_color="Hint",
                        on_release = self.add_folder
                    ),
                ],
            )
        self.dialog.open()


    #Funkcja do tworzenia folderów ze słowami
    def add_folder(self, *args):
        customwidget = CustomWidget()

        content = self.dialog.content_cls
        text_field = content.ids.text_field

        if len(text_field.text) > 13 or len(text_field.text) == 0: #zablokowanie zbyt dużej ilości znakó
            text_field.hint_text = "Wprowadź nazwę"
        else:
            custom_button = customwidget.ids.custom_button
            custom_button.text = text_field.text

            self.ids.my_container.add_widget(customwidget)
            self.dialog.dismiss()

    def close_popup(self, *args):
        self.dialog.dismiss()

    # Tłumaczenie naszego wyrazu w screen random
    def change(self, *args):

        random_button = self.ids.random

        if self.button_state:
            random_button.md_bg_color = [0, 0, 1, 1]  
            random_button.text = "Blue Text"
        else:
            random_button.md_bg_color = [1, 0, 0, 1]  
            random_button.text = "Red Text"

        self.button_state = not self.button_state

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