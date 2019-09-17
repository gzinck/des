def no_heuristic(automaton, unverified, verified):
    """Orders the automata to compose with the automaton with no heuristic (aside
    from prioritizing automata that have not been verified).

    Parameters
    ----------
    automaton : dict
        The automaton to consider
    unverified : list
        The list of unverified automata to consider composing with
    verified : list
        The list of verified automata to consider composing with

    Returns
    -------
    list
        An ordered list of automata to consider composing with
    """
    return [*unverified, *verified]

def most_shared_heuristic(automaton, unverified, verified):
    """Orders the automata to compose with the automaton by those that share the
    most events with the automaton.

    Parameters
    ----------
    automaton : dict
        The automaton to consider
    unverified : list
        The list of unverified automata to consider composing with
    verified : list
        The list of verified automata to consider composing with

    Returns
    -------
    list
        An ordered list of automata to consider composing with
    """
    events = set(automaton["events"]["all"])

    def sort_by_shared(a):
        other_events = set(a["events"]["all"])
        return len(events.intersection(events))

    unverified.sort(key = sort_by_shared, reverse = True)
    verified.sort(key = sort_by_shared, reverse = True)

    return [*unverified, *verified]

def least_new_heuristic(automaton, unverified, verified):
    """Orders the automata to compose with the automaton by those that introduce
    the fewest events to the automaton.

    Parameters
    ----------
    automaton : dict
        The automaton to consider
    unverified : list
        The list of unverified automata to consider composing with
    verified : list
        The list of verified automata to consider composing with

    Returns
    -------
    list
        An ordered list of automata to consider composing with
    """
    events = set(automaton["events"]["all"])

    def sort_by_least_new(a):
        other_events = set(a["events"]["all"])
        return len(other_events.difference(events))

    # Sort ascending by least new events introduced
    unverified.sort(key = sort_by_least_new)
    verified.sort(key = sort_by_least_new)

    return [*unverified, *verified]
