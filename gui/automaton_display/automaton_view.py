from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout

from graph_viz.visualize import visualize
import global_settings
import os


# class AutomatonView(ScrollView):
class AutomatonView(FloatLayout):
    def __init__(self, **kwargs):
        super(AutomatonView, self).__init__(**kwargs)
        app = App.get_running_app()
        app.bind(current_automaton=self.on_current_automaton)

    def on_current_automaton(self, instance, value):
        app = App.get_running_app()
        name = value["name"]
        if name in app.temp_folders:
            path = app.temp_folders[name] + "/" + name
            img_path = path + "." + global_settings.settings["graphviz_file_type"]
            if not os.path.isfile(path + "." + global_settings.settings["graphviz_file_type"]):
                img_path = visualize(value, path, view=False)
            self.ids.image.source = img_path
            self.ids.image.size = [1500, 1500]

    def on_zoom_out(self):
        curr_size = self.ids.image.size
        new_size = [int(old_size * 0.9) for old_size in curr_size]
        self.ids.image.size = new_size

    def on_zoom_in(self):
        curr_size = self.ids.image.size
        new_size = [int(old_size * 1.1) for old_size in curr_size]
        self.ids.image.size = new_size
