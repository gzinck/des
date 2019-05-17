def check_opacity(automaton, observer=0, secret=0):
    """Verifies current state opacity for the given automaton with respect to
    a certain agent's observability. That is, if every word leading to a bad
    state has another word with the same projection leading to a good state,
    the automaton is opaque.

    Parameters
    ----------
    automaton : dict
        The automaton for which to check for opacity
    observer : int
        The index of the observer which is examining the system
    secret : int
        The index of the secret set of states which must be opaque with respect
        to the observer

    Returns
    -------

    """