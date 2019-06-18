from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty

from json import load, JSONDecodeError

from structure_validation.automaton_validator import validate
from gui.popups.name_automaton_popup import NameAutomatonPopup
from gui.popups.message_popup import MessagePopup

import global_settings


class OpenAutomatonPopup(Popup):
    name = StringProperty()
    selected = ListProperty()
    default_path = StringProperty()

    def __init__(self, **kwargs):
        super(OpenAutomatonPopup, self).__init__(**kwargs)
        self.default_path = global_settings.settings["default_path"]

    def on_select(self, selection):
        self.selected = selection

    def open_automaton(self):
        if not global_settings.settings["default_path_set"]:
            global_settings.update("default_path", self.ids.file_chooser.path)
        for item in self.selected:
            # Attempt to load the file's JSON
            with open(item) as f:
                try:
                    curr = load(f)
                except (JSONDecodeError, UnicodeDecodeError):
                    popup = MessagePopup(title="Error", message="Failed to read JSON")
                    popup.open()
                    return

            # Attempt to validate the automaton
            try:
                validate(curr)
                popup = NameAutomatonPopup(automaton=curr)
                popup.open()
            except ValueError as e:
                popup = MessagePopup(title="Error",
                                     message="Automaton validation failure: "
                                     + str(e))
                popup.open()
