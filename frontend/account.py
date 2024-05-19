from kivy.uix.screenmanager import Screen
import requests
import json

class Registration(Screen):

    def register_user(self):
        username = self.ids.username.text
        email = self.ids.email.text
        password = self.ids.password.text
        repeat_password = self.ids.repeat_password.text
