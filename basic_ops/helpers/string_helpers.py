from json import dumps


def get_states(states, chosen_so_far=[]):
    """A list of current states for multiple automata in a composed system (i.e.,
    a "macro-state") has some states which are non-deterministic: that is, the
    state might be ["q1", ["q2", "q3"]]. We want to find all distinct states,
    so we want ["q1", "q2"] and ["q1", "q3"]. This becomes a major task when
    there are many options for many automata, leading to a combinatorial
    explosion.

    Parameters
    ----------
    states : array of strings, or array of arrays of strings
        Array of all states (or possible states)

    Returns
    -------
    Array of arrays of strings
        All possible macro-states

    Examples
    --------
    >>> print(get_states(["q1", ["q2", "q3"]]))
    [["q1", "q2"], ["q1", "q3"]]
    """
    index = len(chosen_so_far)

    # Base case
    if index == len(states):
        return [chosen_so_far.copy()]

    macro_states = []
    for option in states[index]:
        chosen_so_far.append(option)
        macro_states.extend(get_states(states, chosen_so_far))
        chosen_so_far.pop()
    return macro_states


def format_state(states):
    """Creates a macro-state string containing all of the states passed in.

    Parameters
    ----------
    states : array of strings
        Array of all the states to put together

    Returns
    -------
    string
        The string representing the macro-state

    Examples
    --------
    >>> print(format_state(["q1"]))
    "(q1)"
    >>> print(format_state(["q1", "q2", "(q3, q4)"]))
    "(q1, q2, (q3, q4))"
    """
    str = "("
    for state in states:
        str += state + ", "
    str = str[0:-2]  # take off last comma
    str += ")"
    return str


def format_state_set(states):
    """Creates a macro-state string containing all of the states passed in as a
    set.

    Parameters
    ----------
    states : array of strings
        Array of all the states to put together

    Returns
    -------
    string
        The string representing the macro-state

    Examples
    --------
    >>> print(format_state(["q1"]))
    "(q1)"
    >>> print(format_state(["q1", "q2", "(q3, q4)"]))
    "{q1, q2, (q3, q4)}"
    """
    states.sort()
    str = "{"
    for state in states:
        str += state + ", "
    str = str[0:-2]  # take off last comma
    str += "}"
    return str


def format_transition(state, event):
    """Formats a state and event into the proper format for a transition,
    which is used as a key in the transition dictionary.

    Parameters
    ----------
    state : string
        The state the transition originates from
    event : string
        The event prompting the state change

    Returns
    -------
    string
        The string representing the transition's key for the dictionary

    Examples
    --------
    >>> print(format_transition("q1", "a"))
    "q1->a"
    >>> print(format_transition("(q1, q5)", "c"))
    "(q1, q5)->c"
    """
    return state + "->" + event


def extract_state(transition):
    """Extracts the name of the origin state given a string representing a
    transition.

    Parameters
    ----------
    transition : str
        A transition

    Returns
    -------
    str
        The corresponding state from the transition
    """
    return transition.split("->", 1)[0]


def extract_event(transition):
    """Extracts the name of the event given a string representing a
    transition.

    Parameters
    ----------
    transition : str
        A transition

    Returns
    -------
    str
        The corresponding event from the transition
    """
    return transition.split("->", 1)[1]


def pretty_print(automaton):
    """
    Formats an automaton in an attractive way and prints as text.

    Parameters
    ----------
    automaton : dict
        The automaton to print

    Returns
    -------
    None
    """
    print(dumps(automaton, sort_keys=True, indent=4))
