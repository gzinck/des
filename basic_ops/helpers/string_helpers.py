import pprint

def format_state(states):
    '''Creates a macro-state containing all of the states passed in.

    Parameters
    ----------
    states : array of strings
        Array of all the states to put together

    Yields
    ------
    string
        The string representing the macro-state

    Examples
    --------
    >>> print(format_state(["q1"]))
    "(q1)"
    >>> print(format_state(["q1", "q2", "(q3, q4)"]))
    "(q1, q2, (q3, q4))"
    '''
    str = "("
    for state in states:
        str += state + ", "
    str = str[0:-2] # take off last comma
    str += ")"
    return str

def format_transition(state, event):
    '''Formats a state and event into the proper format for a transition,
    which is used as a key in the transition dictionary.

    Parameters
    ----------
    state : string
        The state the transition originates from
    event : string
        The event prompting the state change

    Yields
    ------
    string
        The string representing the transition's key for the dictionary

    Examples
    --------
    >>> print(format_transition("q1", "a"))
    "q1->a"
    >>> print(format_transition("(q1, q5)", "c"))
    "(q1, q5)->c"
    '''
    return state + "->" + event

def pretty_print(automaton):
    '''
    Formats an automaton in an attractive way and prints as text.
    '''
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(automaton)
