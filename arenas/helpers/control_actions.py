from itertools import combinations, chain
import basic_ops.helpers.string_helpers as str_helper
from basic_ops.helpers.determinization_helpers import get_unobservable_reach


def get_valid_control_actions(automaton, state, observable_events):
    """This gets all possible valid control actions for an automaton at a given
    state. That is, it finds all possible actions for the automaton from the
    unobservable reach of the current state and returns its power set as a list
    of tuples. Note than unobservable events will not be included in the sets,
    and all uncontrollable events that may occur at the state will be included
    in every set.

    Notes
    -----
    It does not include the empty set control action

    Parameters
    ----------
    automaton : dictionary
        The automaton for which to get valid control actions
    state : string
        The current state of the automaton
    observable_events : list of strings
        The events which are observable within the automaton

    Returns
    -------
    list of lists
        A list of possible control actions, which are in turn lists of events
        (strings) that are allowed

    Examples
    --------
    >>> print(get_valid_control_actions(automaton, "{q0, q1, q2}"))
    [["a", "u"], ["b", "u"], ["a", "b", "u"]]
    """
    # First, get all the places the automaton could be
    states = get_unobservable_reach(automaton, [state], observable_events)
    # Check for valid controllable events for the controller
    cont_events = automaton["events"]["controllable"][0]
    valid_cevents = []
    for state in states:
        for event in cont_events:
            trans = str_helper.format_transition(state, event)
            if trans in automaton["transitions"]["all"]:
                valid_cevents.append(event)

    # Check for valid uncontrollable events
    all_events = automaton["events"]["all"]
    uncont_events = set(all_events).difference(set(cont_events))
    valid_ucevents = []
    for state in states:
        for event in uncont_events:
            trans = str_helper.format_transition(state, event)
            if trans in automaton["transitions"]["all"]:
                valid_ucevents.append(event)

    # Now that we have all events, get the power set
    all_actions = list(chain.from_iterable(
        combinations(valid_cevents, x) for x in range(0, len(valid_cevents) + 1)
    ))

    # Convert to lists
    events = [list(x) + valid_ucevents for x in all_actions]
    return [x for x in events if len(x) > 0]
