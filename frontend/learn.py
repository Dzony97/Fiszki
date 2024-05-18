from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class WordWidget(MDBoxLayout):
    def __init__(self, word1, word2, **kwargs):
        super(WordWidget, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = "200dp"
        self.flag = True
        self.word1 = word1
        self.word2 = word2

    #Przelaczanie slow z ang na pl
    def toggle_text(self):
        if self.flag:
            self.ids.words.text = self.word2
            self.ids.words.md_bg_color = (1, 0, 1, 1)
            self.flag = False
        else:
            self.ids.words.text = self.word1
            self.ids.words.md_bg_color = (0, 1, 1, 1)
            self.flag = True

class LearnScreen(Screen):

    #Dodawanie przyciskow ze slowami do nauki i ich tluamczenie
    def add_words(self, file1_name, file2_name):
        word_container = self.ids.word_container

        with open(file1_name, 'r', encoding="utf8") as file1, open(file2_name, 'r', encoding="utf8") as file2:
            words1 = file1.read().split(',')
            words2 = file2.read().split(',')

            for word1, word2 in zip(words1, words2):
                word1 = word1.strip()
                word2 = word2.strip()
                word_widget = WordWidget(word1, word2)
                word_widget.ids.words.text = word1
                word_container.add_widget(word_widget)

    #Czyszczenie ekranu learn
    def clear_word_container(self):
        word_container = self.ids.word_container
        word_container.clear_widgets()

class SecondContent(MDBoxLayout):
    pass

class SecondWordWidget(MDBoxLayout):
    text = ""
    def __init__(self, dialog, new_word, new_translate, **kwargs):
        super(SecondWordWidget, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = "200dp"
        self.flag = True
        self.dialog = dialog
        self.new_word = new_word
        self.new_translate = new_translate
    def second_toggle_text(self):

        if self.flag:
            self.ids.words_second.text = self.new_translate.text
            self.ids.words_second.md_bg_color = (1, 0, 1, 1)
            self.flag = False
        else:
            self.ids.words_second.text = self.new_word.text
            self.ids.words_second.md_bg_color = (0, 1, 1, 1)
            self.flag = True

class SecondLearnScreen(Screen):

    dialog = None

    # Okno popup odpowiadające za tworzenie nowych kart do nauki
    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Wpisz słowo:",
                type="custom",
                content_cls=SecondContent(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Hint",
                        on_release=self.close_popup
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Hint",
                        on_release= self.add_second_words
                    ),
                ],
            )
        self.dialog.open()

    def close_popup(self, dialog):
        self.dialog = self.dialog.dismiss()

    def add_second_words(self, *args):

        second_content = self.dialog.content_cls
        new_word = second_content.ids.new_word
        new_translate = second_content.ids.new_translate

        if len(new_word.text) == 0:
            new_word.hint_text = "Wprowadź słowo"
        elif len(new_translate.text) == 0:
            new_translate.hint_text = "Wprowadź tłumaczenie"
        else:
            words_widget = SecondWordWidget(self.dialog, new_word, new_translate)
            words_second = words_widget.ids.words_second
            words_second.text = new_word.text
            self.ids.words_container.add_widget(words_widget)
            self.dialog.dismiss()

