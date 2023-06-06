import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget

kivy.require('1.11.1')


class SplashScreen(Widget):
    pass


class MyApp(App):
    def build(self):
        return SplashScreen()


if __name__ == '__main__':
    MyApp().run()
