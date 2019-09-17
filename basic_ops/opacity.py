from basic_ops.determinize import determinize

def check_opacity(automaton, observer=0):
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

    Returns
    -------
    list of bool
        Whether or not the automaton is opaque with respect to each set of
        secrets. If true, indicates that opacity holds with respect to those
        secrets
    """
    det = determinize(automaton, observer)
    return [len(m) == 0 for m in det["states"]["marked"]]

def check_opacity_already_determinized(automaton):
    """Verifies current state opacity for the given automaton, assuming that the
    automaton is already determinized. That is, if every word leading to a bad
    state has another word with the same projection leading to a good state,
    the automaton is opaque.

    Parameters
    ----------
    automaton : dict
        The automaton for which to check for opacity

    Returns
    -------
    list of bool
        Whether or not the automaton is opaque with respect to each set of
        secrets. If true, indicates that opacity holds with respect to those
        secrets
    """
    return [len(m) == 0 for m in automaton["states"]["marked"]]
