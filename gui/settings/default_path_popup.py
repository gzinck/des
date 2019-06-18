from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty, DictProperty

import global_settings


class DefaultPathPopup(Popup):
    default_path = StringProperty()

    def __init__(self, **kwargs):
        super(DefaultPathPopup, self).__init__(**kwargs)
        self.default_path = global_settings.settings["default_path"]

    def on_save(self):
        self.default_path = self.ids.file_chooser.path
        self.dismiss()
