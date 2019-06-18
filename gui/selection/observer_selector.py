from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, DictProperty, NumericProperty, BooleanProperty, StringProperty


class ObserverLabel(BoxLayout):
    selected = BooleanProperty(False)
    text = StringProperty()
    g = StringProperty()
    ind = NumericProperty()

    def on_checkbox_active(self, value):
        self.selected = value


class ObserverSelector(Popup):
    selected = ListProperty()
    automaton = DictProperty()
    title = StringProperty()

    def __init__(self, automaton, title="Select an Observer", **kwargs):
        super(ObserverSelector, self).__init__(**kwargs)
        self.automaton = automaton
        self.title = title

        self.ids.list.add_widget(ObserverLabel(text="Global Controller", ind=0))
        for i in range(1, len(self.automaton["events"]["observable"])):
            self.ids.list.add_widget(
                    ObserverLabel(text="Agent " + str(i), ind=i))

    def on_confirm(self):
        for option in self.ids.list.children:
            if option.selected:
                self.selected.append(option.ind)
        print("Selected observer(s):", self.selected)
        self.dismiss()
