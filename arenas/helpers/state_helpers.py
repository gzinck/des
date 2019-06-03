import basic_ops.helpers.string_helpers as str_helper


def find_next_state(automata, state, event):
    """Gets the next state for the system composed of all automata in the
    parameter from the current state, given an event. It assumes that if
    the event is not defined in one of the automata, then that automaton
    simply does not progress to the next stage.

    Notes
    -----
    Assumes that all automata in the parameter are deterministic

    Parameters
    ----------
    automata : list of dictionaries
        The automata for which to find the next state
    state : list
        The current states for each of the automata given as input
    event : string
        The event which progresses the system to the next state

    Returns
    -------
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
            next_state[i] = transitions[trans][0]
        else:
            next_state[i] = state[i]
    return next_state


def check_marked_agents(automata, states):
    """Assuming each automaton represents one agent's view of the system, this
    returns a list of agents for which its current state is a marked state
    from another agent's perspective

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

    Returns
    -------
    list
        List of tuples (agent A, agents B) representing that agent A can observe
        that all agents in B are in a marked state
    """
    automata = automata[1:]  # Ignore the initial real automaton
    states = states[1:]  # Ignore the initial real automaton
    observations = []
    # Go through each automaton's view (except the controller's)
    for index in range(1, len(automata)):
        curr_obs = []
        # Go through every other automaton's views
        for other_index in [x for x in range(1, len(automata)) if x != index]:
            # Check if the other automaton's state is marked from current
            # agent's perspective. Note the minus 1 because the first automaton
            # is useless.
            marked = automata[index]["states"]["marked"][other_index]
            if states[index] in marked:
                curr_obs.append(other_index)
        if len(curr_obs) > 0:
            observations.append(tuple([index, curr_obs]))
    return observations
