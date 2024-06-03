from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
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

