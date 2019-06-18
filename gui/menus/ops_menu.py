from kivy.app import App
from kivy.uix.screenmanager import Screen
from gui.selection.single_automaton_selector import SingleAutomatonSelector
from gui.selection.multiple_automaton_selector import MultipleAutomatonSelector
from gui.selection.observer_selector import ObserverSelector
from gui.popups.name_automaton_popup import NameAutomatonPopup
from gui.popups.message_popup import MessagePopup
from kivy.properties import ObjectProperty

# Operations
from basic_ops.determinize import determinize
from basic_ops.opacity import check_opacity
from basic_ops.union import union
from basic_ops.product import product
from basic_ops.accessible import get_accessible
from basic_ops.coaccessible import get_coaccessible


class OpsMenu(Screen):
    current_op = ObjectProperty()

    def determinize(self):
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

    def opacity_operation(self):
        popup = SingleAutomatonSelector()
        popup.bind(on_dismiss=self.opacity_get_observer)
        popup.open()

    def opacity_get_observer(self, instance):
        name = instance.selected
        app = App.get_running_app()
        selected = [x for x in app.open_automata if x["name"] == name]
        if len(selected) != 0:
            selected = selected[0]
            print("Selected the automaton...")
            popup = ObserverSelector(selected)
            popup.bind(on_dismiss=lambda obs_selector:
            self.opacity_perform_operation(obs_selector, selected))
            popup.open()

    def opacity_perform_operation(self, instance, automaton):
        observer = instance.selected
        if len(observer) != 0:
            observer = observer[0]
            result = check_opacity(automaton, observer)
            opaque = [i for i, x in enumerate(result) if x is True]
            not_opaque = [i for i, x in enumerate(result) if x is False]
            title = "Check Opacity Result"
            message = "With respect to the observer {},the system is opaque " \
                      "for the following secrets: {}.\nThe system is not " \
                      "opaque for the following secrets: {}"\
                .format(observer, opaque, not_opaque)
            popup = MessagePopup(title=title, message=message)
            popup.open()

    def union(self):
        popup = MultipleAutomatonSelector()
        popup.bind(on_dismiss=self.union_perform_operation)
        popup.open()

    def union_perform_operation(self, instance):
        selected_names = instance.selected
        app = App.get_running_app()
        selected = [x for x in app.open_automata if x["name"] in selected_names]
        if len(selected) > 1:
            new_automaton = union(selected)
            popup = NameAutomatonPopup(automaton=new_automaton)
            popup.open()
        elif len(selected) == 1:
            title = "Error"
            message = "You must select at least 2 automata to perform the " \
                      "union operation."
            popup = MessagePopup(title=title, message=message)
            popup.open()

    def product(self):
        popup = MultipleAutomatonSelector()
        popup.bind(on_dismiss=self.product_perform_operation)
        popup.open()

    def product_perform_operation(self, instance):
        selected_names = instance.selected
        app = App.get_running_app()
        selected = [x for x in app.open_automata if x["name"] in selected_names]
        if len(selected) > 1:
            new_automaton = product(selected)
            popup = NameAutomatonPopup(automaton=new_automaton)
            popup.open()
        elif len(selected) == 1:
            title = "Error"
            message = "You must select at least 2 automata to perform the " \
                      "product operation."
            popup = MessagePopup(title=title, message=message)
            popup.open()

    def accessible(self):
        popup = SingleAutomatonSelector()
        popup.bind(on_dismiss=self.accessible_perform_operation)
        popup.open()

    def accessible_perform_operation(self, instance):
        selected_name = instance.selected
        app = App.get_running_app()
        selected = [x for x in app.open_automata if x["name"] == selected_name]
        if len(selected) == 1:
            new_automaton = get_accessible(selected[0])
            popup = NameAutomatonPopup(automaton=new_automaton)
            popup.open()

    def coaccessible(self):
        popup = SingleAutomatonSelector()
        popup.bind(on_dismiss=self.coaccessible_perform_operation)
        popup.open()

    def coaccessible_perform_operation(self, instance):
        selected_name = instance.selected
        app = App.get_running_app()
        selected = [x for x in app.open_automata if x["name"] == selected_name]
        if len(selected) == 1:
            new_automaton = get_coaccessible(selected[0])
            popup = NameAutomatonPopup(automaton=new_automaton)
            popup.open()

