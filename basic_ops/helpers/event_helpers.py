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
    return {
        "all": list(set(events["all"]).intersection(allowed)),
        "controllable": [list(set(x).intersection(allowed)) for x in
                         events["controllable"]],
        "observable": [list(set(x).intersection(allowed)) for x in
                       events["observable"]]
    }
