from kivy.app import App
from kivy.uix.button import Button

class Test (App):
    def build(self):
        return Button(text='olá')

Test().run()
