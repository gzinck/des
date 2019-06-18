from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty, DictProperty, StringProperty, BooleanProperty

from gui.popups.close_automaton_popup import CloseAutomatonPopup
from gui.popups.open_automaton_popup import OpenAutomatonPopup
from gui.popups.save_automaton_popup import SaveAutomatonPopup
from gui.settings.settings_popup import SettingsPopup


class OpenAutomaton(GridLayout):
    """This is a line in the OpenAutomata grid that displays an automaton's name
    and options for closing it and saving it.
    """
    name = StringProperty()
    automaton = DictProperty()
    open = BooleanProperty()

    def on_select(self):
        """When selecting the automaton, the application should make this the
        currently visible automaton.
        """
        app = App.get_running_app()
        app.current_automaton = self.automaton

    def on_save(self):
        """When clicking save, the automaton should open save dialog boxes.
        """
        popup = SaveAutomatonPopup(automaton=self.automaton)
        popup.open()

    def on_close(self):
        """When clicking close, the automaton should close the automaton.
        """
        popup = CloseAutomatonPopup(name=self.name)
        popup.open()


class OpenAutomata(GridLayout):
    """This is the class containing a list of all of the automata which are
    open.
    """
    def __init__(self, **kwargs):
        super(OpenAutomata, self).__init__(**kwargs)
        app = App.get_running_app()
        app.bind(open_automata=self.on_open_automata)
        app.bind(current_automaton=self.on_current_automaton)

    def on_open_automata(self, instance, value):
        self.clear_widgets()
        app = App.get_running_app()
        for item in app.open_automata:
            self.add_widget(OpenAutomaton(name=item["name"], automaton=item))

    def on_current_automaton(self, instance, value):
        for widget in self.children:
            if widget.name == value["name"]:
                widget.open = True
            else:
                widget.open = False


class FileMenu(Screen):
    def on_open(self, *args):
        popup = OpenAutomatonPopup()
        popup.open()

    def on_settings(self, *args):
        popup = SettingsPopup()
        popup.open()
