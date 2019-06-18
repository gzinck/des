from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, BooleanProperty, ListProperty


class MultiSelectableAutomatonLabel(BoxLayout):
    text = StringProperty()
    selected = BooleanProperty(False)

    def on_checkbox_active(self, value):
        self.selected = value


class MultipleAutomatonSelector(Popup):
    selected = ListProperty()

    def __init__(self, **kwargs):
        super(MultipleAutomatonSelector, self).__init__(**kwargs)
        app = App.get_running_app()
        for a in app.open_automata:
            self.ids.list.add_widget(MultiSelectableAutomatonLabel(text=a["name"]))

    def on_confirm(self):
        for option in self.ids.list.children:
            if option.selected:
                self.selected.append(option.text)
        self.dismiss()
