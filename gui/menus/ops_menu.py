from kivy.app import App
from kivy.uix.screenmanager import Screen
from gui.selection.single_automaton_selector import SingleAutomatonSelector
from gui.selection.observer_selector import ObserverSelector
from gui.popups.name_automaton_popup import NameAutomatonPopup
from kivy.properties import ObjectProperty

# Operations
from basic_ops.determinize import determinize


class OpsMenu(Screen):
    current_op = ObjectProperty()

    def determinize(self):
        # SEQUENCE: get single automaton, get observer, perform action
        popup = SingleAutomatonSelector()
        popup.bind(on_dismiss=self.det_get_observer)
        popup.open()

    def det_get_observer(self, instance):
        name = instance.selected
        app = App.get_running_app()
        selected = [x for x in app.open_automata if x["name"] == name]
        if len(selected) != 0:
            selected = selected[0]
            print("Selected the automaton...")
            popup = ObserverSelector(selected)
            popup.bind(on_dismiss=lambda obs_selector:
                       self.det_perform_operation(obs_selector, selected))
            popup.open()

    def det_perform_operation(self, instance, automaton):
        observer = instance.selected
        if len(observer) != 0:
            observer = observer[0]
            new_automaton = determinize(automaton, observer)
            popup = NameAutomatonPopup(automaton=new_automaton)
            popup.open()
