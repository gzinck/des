from basic_ops.determinize import determinize
from basic_ops.coaccessible import get_coaccessible
from basic_ops.union import union


def create_leakage_automaton(automaton, observer=0, secret=0):
    """Gets the leakage automaton with respect to a certain observer and secret.

    Parameters
    ----------
    automaton : dict
        The automaton to use for creating the leakage automaton
    observer : int
        The index of the agent which is observing another agent
    secret : int
        The index of the agent's secret we want to consider

    Returns
    -------
    dict
        The leakage automaton
    """
    det = determinize(automaton, observer)

    # We don't want to worry about this agent's marked states; only every other
    # agent's marked states.
    marked = det["states"]["marked"]
    for i in [x for x in range(len(marked)) if x != secret]:
        marked[i] = []  # We're only considering a specific secret!

    acc = get_coaccessible(det)
    return union([automaton, acc])
