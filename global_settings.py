import json
from cli.display.message import show_error


# The settings file for saving
settings_file = "settings.ini"

# The default settings
defaults = {
    "graphviz_file_type": "pdf",
    "graphviz_auto_vis": True
}
settings = None


def initialize():
    """Initializes the program's settings

    Returns
    -------
    None
    """
    global settings
    settings = defaults
    try:
        try:
            with open(settings_file, 'r') as f:
                # Load in the settings
                settings = json.load(f)

        except FileNotFoundError:
            with open(settings_file, 'w') as f:
                # Write new settings
                settings = defaults
                json.dump(settings, f)
    except Exception:
        show_error("Error reading/writing settings file.\n" +
                   "Reverting to defaults...")

    for k, v in defaults.items():
        if k not in settings:
            settings[k] = v


def update(setting, value):
    """Updates the setting with a new value

    Parameters
    ----------
    setting : str
        The setting to change
    value : any
        The new value for the setting

    Returns
    -------
    None
    """
    settings[setting] = value
    try:
        with open(settings_file, 'w') as f:
            # Write new settings
            json.dump(settings, f)
    except FileNotFoundError:
        show_error("Error writing settings file.\n" +
                   "Changes are only saved for this session.")
