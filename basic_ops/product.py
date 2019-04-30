import helpers.product_helpers as helper

def product(automata):
    '''Composes two or more finite state automata.

    Specifically, the product operation synchronizes all of the automata on their
    common events and prevents any private events.

    Note
    ----
    Any data on bad states or transitions will be not be included in the
    resulting automaton.
    Also, all automata must have the same number of players in the system which
    have sets of controllable and observable events.
    TODO: add a verifier to ensure correct input.

    Parameters
    ----------
    automata : array of dictionaries
        Array of all of the automata which should be composed

    Yields
    ------
    dict
        The resulting composed automaton

    Examples
    --------
    Assume a list of file names of JSON automata exists, called filenames.

    >>> import json
    >>> automata = [{}] * len(filenames)
    >>> if filenames:
    >>>     for i in range(len(filenames)):
    >>>         with open(filenames[i], 'r') as f:
    >>>             automata[i] = json.load(f)
    >>> new_automaton = product(automata)
    >>> print(new_automaton)
    {
        # Dictionary for an automaton
    }
    '''
    new_automaton = {}
    # First, get all events in the new automaton by unioning sets
    new_automaton["events"] = helper.product_events(automata)
    # Then, update the transition function and add all of the states
    new_automaton.update(helper.product_transitions(automata, new_automaton["events"]["all"]))

    return new_automaton
