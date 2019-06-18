from kivy.uix.popup import Popup
from kivy.properties import StringProperty


class MessagePopup(Popup):
    title = StringProperty()
    message = StringProperty()