from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty, DictProperty

from json import dump


class SaveAutomatonPopup(Popup):
    automaton = DictProperty()

    def __init__(self, **kwargs):
        super(SaveAutomatonPopup, self).__init__(**kwargs)
        if "name" in self.automaton:
            self.ids.text_input.text = self.automaton["name"]

    def on_save(self):
        location = self.ids.file_chooser.path + "/" + self.ids.text_input.text

        # Make sure temp folder is not saved
        temp = self.automaton["temp"]
        del self.automaton["temp"]

        with open(location + ".json", 'w') as f:  # writing JSON object
            dump(self.automaton, f, sort_keys=True, indent=4)

        self.automaton["temp"] = temp

        # visualize(automaton, location, view=False)
        print("Saved to " + location)
        self.dismiss()
