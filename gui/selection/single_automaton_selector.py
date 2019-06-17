from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, BooleanProperty


class SelectableAutomatonLabel(BoxLayout):
    text = StringProperty()
    selected = BooleanProperty(False)

    def on_checkbox_active(self, value):
        self.selected = value


class SingleAutomatonSelector(Popup):
    selected = StringProperty()

    def __init__(self, **kwargs):
        super(SingleAutomatonSelector, self).__init__(**kwargs)
        app = App.get_running_app()
        for a in app.open_automata:
            self.ids.list.add_widget(SelectableAutomatonLabel(text=a["name"]))

    def on_confirm(self):
        for option in self.ids.list.children:
            if option.selected:
                self.selected = option.text
        self.dismiss()
