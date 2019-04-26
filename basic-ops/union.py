def __union_events(automata, result):
    # Private method for unioning events
    all_events = set()
    cont_events = set()
    obs_events = set()
    for a in automata:
        events = a["events"]
        all_events = all_events.union(set(events["all"]))
        cont_events = cont_events.union(set(events["controllable"]))
        obs_events = obs_events.union(set(events["observable"]))
    result["events"] = {
        "all": list(all_events),
        "controllable": list(cont_events),
        "observable": list(obs_events)
    }

def union(automata):
    '''Composes two or more finite state automata.

    Specifically, the union operation synchronizes all of the automata on their
    common events, allowing private events regardless.

    Note
    ____
    Any data on bad states or transitions will be not be included in the
    resulting automaton

    Parameters
    ----------
    automata : array of dictionaries
        Array of all of the automata which should be composed

    Yields
    ------
    JSON
        The resulting composed automaton

    Examples
    --------
    Assumes a list of file names of JSON automata exists.

    >>> import json
    >>> automata = [] * len(filenames)
    >>> if filenames:
    >>>     for i in range(len(filenames)):
    >>>         with open(filename[i], 'w') as f:
    >>>             json.dump(automata[i], f)
    >>> union(filenames)
    {
        # Dictionary for an automaton
    }
    '''
    result = {
        "states": {
            "all": [],
            "initial": [],
            "bad": []
        },
        "transitions": {
            "all": [],
            "bad": []
        }
    }
    # First, get all events in the new automaton by unioning sets
    __union_events(automata, result)
