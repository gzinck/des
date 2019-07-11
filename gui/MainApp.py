from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, DictProperty

from gui.menus.file_menu import FileMenu
from gui.automaton_display.automaton_view import AutomatonView
from gui.menus.ops_menu import OpsMenu


class Menus(ScreenManager):
    pass


class MainApp(App):
    """
    This is the class for the main application, storing global variables for the
    application.
    """
    open_automata = ListProperty()
    current_automaton = DictProperty()
    temp_folders = DictProperty()

    def build(self):
        self.title = 'DESwiz'


if __name__ == '__main__':
    MainApp().run()