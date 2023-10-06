
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

import random

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
            random_button.text = "test"
        else:
            random_button.md_bg_color = [1, 0, 0, 1]  
            random_button.text = (self.random)

        self.button_state = not self.button_state

    def random_word():
        with open('random.txt', 'r') as file:  
            slowa = file.read().split(',')
            slowo = random.choice(slowa)
            return slowo.strip()
        
    random = random_word()

class Content(MDBoxLayout):
    pass

#Widget z okna popup
class CustomWidget(MDBoxLayout):
    text = ""

    def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs)
        self.size_hint_y = None  
        self.height = "48dp"