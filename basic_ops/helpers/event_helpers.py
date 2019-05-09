def intersect_events(automaton, alphabet):
    """Ensures that the automaton only has events in the provided alphabet.

    Parameters
    ----------
    automaton : dictionary
        The automaton to determinize
    alphabet : list
        The alphabet to intersect with the automaton's alphabets

    Returns
    -------
    dict
        The resulting events section of the automaton

    Examples
    --------
    >>> print(automaton)
    {
        ...
        {
            "all": ["a", "b", "c"],
            "controllable": [
                ["a", "b"]
            ],
            "observable": [
                ["a", "b", "c"]
            ],
            "attacker": ["a", "b"]
        }
        ...
    }
    >>> print(intersect_events(automaton, ["a"]))
    {
        "all": ["a"],
        "controllable": [
            ["a"]
        ],
        "observable": [
            ["a"]
        ],
        "attacker": ["a"]
    }
    """
    allowed = set(alphabet)
    events = automaton["events"]
    new_events = {}
    new_events["all"] = list(set(events["all"]).intersection(allowed))
    new_events["attacker"] = list(set(events["attacker"]).intersection(allowed))
    new_events["controllable"] = [list(set(x).intersection(allowed)) for x in events["controllable"]]
    new_events["observable"] = [list(set(x).intersection(allowed)) for x in events["observable"]]
    return new_events
