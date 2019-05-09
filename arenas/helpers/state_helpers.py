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


def check_marked_agents(automata, states):
    """Assuming each automaton represents one agent's view of the system, this
    returns true if there exists an automaton for which its current state is
    a marked state with respect to another agent's view. That is, the current
    state from one agent's perspective is certainly a secret state for another
    agent.

    Notes
    -----
    This excludes the first automaton, because the first is supposed to be the
    main view of the system. It checks if the current state for agent 1 is
    marked with respect to agent 2's secret states (and vice versa).

    Parameters
    ----------
    automata : list of dictionaries
        Three automata, including the controller's view of the system (ignored),
        the first agent's view, and the second agent's view

    states : list of strings
        The current state in each of the automata, respectively

    Yields
    ------
    boolean
        True if the resulting state in the arena should be marked.
    """
    for index in range(1, len(automata)):
        # Go through every other automaton's marked states (not the current one)
        for other_index in [x for x in range(1, len(automata)) if x != index]:
            # If it is marked
            marked = automata[index]["states"]["marked"][other_index]
            if states[index] in marked:
                return True
    return False
