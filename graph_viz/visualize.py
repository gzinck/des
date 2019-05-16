from graphviz import Digraph
from graph_viz.event_legend import generate_event_legend


def visualize(automaton, location=None):
    """Turns an automaton into a viewable PDF.

    Parameters
    ----------
    automaton
    location

    Returns
    -------

    """
    dot = Digraph(automaton["name"])
    dot.body.append(generate_event_legend(automaton))
    if location is not None:
        dot.render(location, view=True)
    else:
        dot.render(view=True)