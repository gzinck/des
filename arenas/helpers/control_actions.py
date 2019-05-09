from itertools import combinations, chain
import basic_ops.helpers.string_helpers as str_helper


def get_valid_control_actions(automaton, state):
    """This gets all possible valid control actions for an automaton at a given
    state. That is, it finds all possible actions for the automaton from the
    current state and returns its power set as a list of tuples.

    Notes
    -----
    It does not include the empty set control action

    Parameters
    ----------
    automaton : dictionary
        The automaton for which to get valid control actions
    state : string
        The current state of the automaton

    Yields
    ------
    list of lists
        A list of possible control actions, which are in turn lists of events
        (strings) that are allowed

    Examples
    --------
    >>> print(get_valid_control_actions(automaton, "{q0, q1, q2}"))
    [["a"], ["b"], ["a", "b"]]
    """
    all_events = automaton["events"]["all"]  # TODO: SHOULD THIS BE CHANGED?
    valid_events = []
    for event in all_events:
        trans = str_helper.format_transition(state, event)
        if trans in automaton["transitions"]["all"]:
            valid_events.append(event)
    # Now that we have all events, get the power set
    all_actions = list(chain.from_iterable(
        combinations(valid_events, x) for x in range(1, len(valid_events) + 1)
    ))
    # Convert to lists
    return [list(x) for x in all_actions]
