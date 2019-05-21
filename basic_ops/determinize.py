from basic_ops.helpers.event_helpers import intersect_events
from basic_ops.helpers.determinization_helpers import determinize_transitions


def determinize(automaton, alphabet=0):
    """Computes the determinized version of the automaton.
    That is, it first determines the initial macro-state, composed of the
    unobservable reach from the original intial state (with respect to the
    observable alphabet given, or the attacker alphabet if none given).
    From each state defined, if an event is defined from one of the states in
    the macro state, the subsequent state after the transition is the
    unobservable reach from the state(s) accessible by that event.

    Parameters
    ----------
    automaton : dictionary
        The automaton to determinize
    alphabet : list
        The alphabet which is considered "observable" when determinizing the
        automaton. If undefined, it equals the attacker's alphabet.

    Returns
    -------
    dict
        The resulting determinized automaton

    Examples
    --------
    >>> print(determinize(automaton, ["a", "b", "c"]))
    {
        # Dictionary for an automaton with only events a, b, and c
    }
    >>> print(determinize(automaton))
    {
        # Dictionary for an automaton with only events in attacker alphabet,
        # as defined in the automaton's data structure
    }
    """
    alphabet = automaton["events"]["observable"][alphabet]
    # First, get all events in the new automaton by intersecting sets
    events = intersect_events(automaton, alphabet)
    # Then, update the transition function and add all of the states
    transitions = determinize_transitions(automaton, alphabet)
    return {
        "events": events,
        **transitions
    }
