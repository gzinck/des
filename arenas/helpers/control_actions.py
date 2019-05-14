from itertools import combinations, chain
import basic_ops.helpers.string_helpers as str_helper


def get_valid_control_actions(automaton, state, all_events):
    """This gets all possible valid control actions for an automaton at a given
    state. That is, it finds all possible actions for the automaton from the
    current state and returns its power set as a list of tuples.
    Note that if there exist uncontrollable events that are defined, they must
    be part of each control action returned.

    Notes
    -----
    It does not include the empty set control action

    Parameters
    ----------
    automaton : dictionary
        The automaton for which to get valid control actions
    state : string
        The current state of the automaton

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
    # Check for valid controllable events for the controller
    cont_events = automaton["events"]["controllable"][0]
    valid_cevents = []
    for event in cont_events:
        trans = str_helper.format_transition(state, event)
        if trans in automaton["transitions"]["all"]:
            valid_cevents.append(event)

    # Check for valid uncontrollable events
    uncont_events = set(all_events).difference(set(cont_events))
    # print("CONT EVENTS:", cont_events)
    # print("UNCONT EVENTS:", uncont_events)
    # valid_ucevents = []
    # for event in uncont_events:
    #     trans = str_helper.format_transition(state, event)
    #     if trans in automaton["transitions"]["all"]:
    #         valid_ucevents.append(event)
    # Now that we have all events, get the power set
    all_actions = list(chain.from_iterable(
        combinations(valid_cevents, x) for x in range(0, len(valid_cevents) + 1)
    ))
    # Convert to lists
    # events = [list(x) + valid_ucevents for x in all_actions]
    events = [list(x) + list(uncont_events) for x in all_actions]
    return [x for x in events if len(x) > 0]
