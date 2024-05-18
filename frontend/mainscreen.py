import random

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from translator import translate_text

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

        if len(text_field.text) == 0: #zablokowanie zbyt dużej ilości znaków
            text_field.hint_text = "Wprowadź nazwę!"
        elif len(text_field.text) > 13:
            text_field.hint_text = "Za dużo znaków!"
        else:
            custom_button = customwidget.ids.custom_button
            custom_button.text = text_field.text

            self.ids.my_container.add_widget(customwidget)
            self.dialog.dismiss()

    def close_popup(self, dialog):
        self.dialog = self.dialog.dismiss()

    def change(self):
        # Wybieranie nowego losowego słowa
        self.ids.random.text = self.random_word()
        self.word = self.ids.random.text
        self.ids.random.md_bg_color = 0, 1, 1, 1
        self.flag = True

    #Tlumaczenie w random
    def translate(self):
    
        if self.flag:
            self.ids.random.text = translate_text(self.ids.random.text, 'PL')
            self.ids.random.md_bg_color = 1, 0, 1, 1
            self.flag = False
        else:
            self.ids.random.text = self.word
            self.ids.random.md_bg_color = 0, 1, 1, 1
            self.flag = True

    def random_word(self):
        with open('words/random.txt', 'r') as file:  
            slowa = file.read().split(',')
            slowo = random.choice(slowa)
            return slowo.strip()

class Content(MDBoxLayout):
    pass

#Widget z okna popup
class CustomWidget(MDBoxLayout):
    text = ""

    def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs)
        self.size_hint_y = None  
        self.height = "48dp"









