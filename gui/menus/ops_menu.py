from kivy.app import App
from kivy.uix.screenmanager import Screen
from gui.selection.single_automaton_selector import SingleAutomatonSelector
from gui.selection.observer_selector import ObserverSelector
from kivy.properties import ObjectProperty


class OpsMenu(Screen):
    current_op = ObjectProperty()

    def determinize(self):
        # SEQUENCE: get single automaton, get observer, perform action
        popup = SingleAutomatonSelector()
        popup.bind(on_dismiss=self.get_observer)
        popup.open()

    def get_observer(self, instance):
        name = instance.selected
        app = App.get_running_app()
        selected = [x for x in app.open_automata if x["name"] == name]
        if len(selected) != 0:
            selected = selected[0]
            print("Selected the automaton...")
            popup = ObserverSelector(selected)
            popup.open()

    def perform_operation(self):
        pass
