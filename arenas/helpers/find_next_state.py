import basic_ops.helpers.string_helpers as str_helper


def find_next_state(automata, state, event):
    """Gets the next state for the system composed of all automata in the
    parameter from the current state, given an event. It assumes that if
    the event is not defined in one of the automata, then that automaton
    simply does not progress to the next stage.

    Parameters
    ----------
    automata : list of dictionaries
        The automata for which to find the next state
    state : list
        The current states for each of the automata given as input
    event : string
        The event which progresses the system to the next state

    Yields
    ------
    list
        The next states for each of the automata, given the event

    Examples
    --------
    >>> print(find_next_state(automata, ["q1", "q3", "{q2, q5}"], "a"))
    ["q1", "q5", "{q6, q7}"]
    """
    next_state = [""] * len(automata)
    for i in range(len(automata)):
        transitions = automata[i]["transitions"]["all"]
        trans = str_helper.format_transition(state[i], event)
        # If a transition exists, add the next state. Else, stay in same state
        if trans in transitions:
            next_state[i] = transitions[trans]
        else:
            next_state[i] = state[i]
    return next_state
