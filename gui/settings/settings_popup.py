from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout


from gui.settings.default_path_popup import DefaultPathPopup

import global_settings


class FileTypeDropDown(BoxLayout):
    file_type = StringProperty()

    def __init__(self, **kwargs):
        super(FileTypeDropDown, self).__init__(**kwargs)
        self.file_type = global_settings.settings["graphviz_file_type"]

    def on_text(self, text):
        self.file_type = text


class SettingsPopup(Popup):
    default_path = StringProperty()
    default_path_set = BooleanProperty()

    def __init__(self, **kwargs):
        super(SettingsPopup, self).__init__(**kwargs)
        self.default_path = global_settings.settings["default_path"]
        self.default_path_set = global_settings.settings["default_path_set"]
        self.update_btns()

    def on_choose_default_path(self):
        popup = DefaultPathPopup()
        popup.bind(on_dismiss=self.default_path_selected)
        popup.open()

    def default_path_selected(self, instance):
        self.default_path = instance.default_path

    def on_toggle_freeze_default_path(self):
        self.default_path_set = not self.default_path_set
        self.update_btns()

    def update_btns(self):
        if self.default_path_set:
            self.ids.freeze_default_btn.text = "Unfreeze"
        else:
            self.ids.freeze_default_btn.text = "Freeze"

    def on_save(self):
        global_settings.update("graphviz_file_type", self.ids.file_type_dropdown.file_type)
        global_settings.update("default_path_set", self.default_path_set)
        global_settings.update("default_path", self.default_path)
        self.dismiss()
