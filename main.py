from kivy.app import App
from kivy.uix.label import Label

class LucyApp(App):
    def build(self):
        return Label(text="Lucy is running on Android")

LucyApp().run()
