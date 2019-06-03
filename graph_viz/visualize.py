from graphviz import Digraph
from graph_viz.event_legend import generate_event_legend
from basic_ops.helpers.string_helpers import extract_state, extract_event


def __identify_secret(automaton, state):
    """Identifies the observers for which the state is a secret state and
    returns a string describing the indexes of those observers.

    Parameters
    ----------
    automaton : dict
        The automaton for which to find secret states
    state : str
        The string representing the current (possibly secret) state

    Returns
    -------
    str
        String representing all observers for which the state is secret
    """
    # First, check if the automaton has a special "secrets" section which
    # specifies what states have what secrets
    if "secrets" in automaton["states"]:
        secrets = automaton["states"]["secrets"]
        if state in secrets:
            return "\n" + secrets[state]
        else:
            return ""
    # Otherwise, just figure out which agents marked the state.
    else:
        marked = ""
        marked_list = automaton["states"]["marked"]
        for i in range(len(marked_list)):
            if state in marked_list[i]:
                marked += str(i) + ", "

        if len(marked) == 0:
            return marked
        return "\nSecret for agent(s): " + marked[:-2]


def visualize(automaton, location=None, view=True):
    """Turns an automaton into a viewable PDF and saves it to the location.
    It also opens the default PDF viewer.

    Parameters
    ----------
    automaton : dict
        The dictionary representing the automaton
    location : str
        The path with which to save the automaton's image
    view : bool
        Whether or not to show the visualized image

    Returns
    -------
    None
    """
    dot = Digraph(automaton["name"])

    # Add all states
    for state in automaton["states"]["all"]:
        secret = __identify_secret(automaton, state)

        if "v2" in automaton["states"] and state in automaton["states"]["v2"]:
            if state in automaton["states"]["bad"]:
                dot.node(state, label=state+secret, shape="box", color="red")
            else:
                dot.node(state, label=state+secret, shape="box", color="black")
        else:
            if state in automaton["states"]["bad"]:
                dot.node(state, label=state+secret, shape="ellipse", color="red")
            else:
                dot.node(state, label=state+secret, shape="ellipse", color="black")

    for state in automaton["states"]["initial"]:
        invisible = state + "-invisible"
        dot.node(invisible, style="invis")
        dot.edge(invisible, state)

    for k, v in automaton["transitions"]["all"].items():
        from_state = extract_state(k)
        event = extract_event(k)
        for to_state in v:
            dot.edge(from_state, to_state, label=event)

    dot.body.append(generate_event_legend(automaton["events"]))
    if location is not None:
        dot.render(location, view=view)
    else:
        dot.render(view=view)