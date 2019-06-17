from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty


class CloseAutomatonPopup(Popup):
    name = StringProperty()

    def close_automaton(self):
        app = App.get_running_app()
        app.open_automata = [a for a in app.open_automata if
                             a["name"] != self.name]