from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty, DictProperty

from json import dump
from graph_viz.visualize import visualize

import global_settings


class SaveAutomatonPopup(Popup):
    automaton = DictProperty()
    default_path = StringProperty()

    def __init__(self, **kwargs):
        super(SaveAutomatonPopup, self).__init__(**kwargs)
        self.default_path = global_settings.settings["default_path"]
        if "name" in self.automaton:
            self.ids.text_input.text = self.automaton["name"]

    def on_save(self):
        location = self.ids.file_chooser.path + "/" + self.ids.text_input.text
        if not global_settings.settings["default_path_set"]:
            global_settings.update("default_path", self.ids.file_chooser.path)

        with open(location + ".json", 'w') as f:  # writing JSON object
            dump(self.automaton, f, sort_keys=True, indent=4)

        visualize(self.automaton, location, view=False)
        self.dismiss()
