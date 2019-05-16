from copy import deepcopy
from basic_ops.helpers.string_helpers import extract_event, extract_state
from basic_ops.accessible import get_accessible


def get_controllable(automaton):
    """Gets the supremal controllable version of the automaton that avoids all
    bad states by removing only controllable transitions. It does not guarantee
    that the language is observable (that is, has the same control actions
    for all strings with the same appearance to the observer).
    In the process, this method calls get_accessible

    Parameters
    ----------
    automaton : dict
        The automaton for which to get the supremal controllable automaton

    Returns
    -------
    dict
        The supremal controllable automaton corresponding to the input
    """
    automaton = deepcopy(automaton)
    queue = automaton["states"]["bad"].copy()
    bad_trans = dict()

    # Deal with what happens when an initial state is bad
    for state in automaton["states"]["bad"]:
        if state in automaton["states"]["initial"]:
            automaton["states"]["initial"] = []

    while len(queue) > 0:
        curr = queue.pop(0)
        for k, v in automaton["transitions"]["all"].items():
            if v == curr:
                # This is a bad transition
                if extract_event(k) in automaton["events"]["controllable"][0]:
                    # We can simply remove the transition
                    bad_trans[k] = v
                else:
                    state = extract_state(k)
                    queue.append(state)

                    # If initial is bad, no controller possible
                    if state in automaton["states"]["initial"]:
                        automaton["states"]["initial"] = []

    # Remove all bad transitions
    for k, v in bad_trans.items():
        automaton["transitions"]["all"].pop(k)
    automaton["transitions"]["bad"] = bad_trans

    return get_accessible(automaton)