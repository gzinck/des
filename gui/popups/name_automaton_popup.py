from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import DictProperty, StringProperty

from tempfile import TemporaryDirectory


class NameAutomatonPopup(Popup):
    automaton = DictProperty()
    name = StringProperty()

    def __init__(self, **kwargs):
        super(NameAutomatonPopup, self).__init__(**kwargs)
        if "name" in self.automaton:
            self.ids.text_input.text = self.automaton["name"]

    def on_text(self, text):
        self.name = text
        app = App.get_running_app()
        all_names = [a["name"] for a in app.open_automata]
        all_names.append("")
        if self.name in all_names:
            self.ids.error.disabled = False
            self.ids.confirm.disabled = True
            self.ids.error.text = "The name is not valid or not unique."
        else:
            self.ids.error.disabled = True
            self.ids.confirm.disabled = False
            self.ids.error.text = "The name is valid."

    def on_confirm(self):
        app = App.get_running_app()
        self.automaton["name"] = str(self.name)
        with TemporaryDirectory() as temp_dir:
            app.temp_folders[self.name] = temp_dir
        a = dict(self.automaton)
        app.open_automata.append(a)
        app.current_automaton = a
        self.dismiss()
