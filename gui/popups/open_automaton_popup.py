from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty

from json import load, JSONDecodeError

from structure_validation.automaton_validator import validate
from gui.popups.name_automaton_popup import NameAutomatonPopup


class OpenAutomatonPopup(Popup):
    name = StringProperty()
    selected = ListProperty()

    def on_select(self, selection):
        self.selected = selection

    def open_automaton(self):
        for item in self.selected:
            # Attempt to load the file's JSON
            with open(item) as f:
                try:
                    curr = load(f)
                except JSONDecodeError:
                    print("Failed to read JSON")
                    return

            # Attempt to validate the automaton
            try:
                validate(curr)
                popup = NameAutomatonPopup(automaton=curr)
                popup.open()
            except ValueError as e:
                print("Automaton validation failure: " + str(e))