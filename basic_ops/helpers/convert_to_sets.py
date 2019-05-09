def convert_to_sets(structure):
    """Converts all lists to sets in a complex data structure (recursively).
    This is useful when lists are really supposed to be unordered, but JSON
    prevents their use.

    Note
    ----
    Only supports complex data types composed of lists and dictionaries.
    Some lists are excluded: specifically, if it is a list of lists. This is
    the case for "controllable" and "observable" events in automata, which
    are really supposed to be lists of sets.

    Parameters
    ----------
    structure : complex data structure
        The structure with lists we want to convert to sets.

    Returns
    -------
    structure
        The converted structure

    Examples
    --------
    Typical usage:

    >>> structure = {
        "events": {
    		"all": ["a", "c"],
    		"controllable": [
    			["a"]
    		],
        },
        "states": {
            "all": ["q1", "q2", "q3"],
            "initial": ["q1"]
        }
    }
    >>> print(convert_to_sets(structure))
    {
        "events": {
            "all": ["a", "c"],
            "controllable": [
                {"a"}
            ],
        },
        "states": {
            "all": {"q1", "q2", "q3"},
            "initial": {"q1"}
        }
    }

    This can be used to compare two automata, where ordering of items
    does not matter:

    >>> assert convert_to_sets(automaton1) == convert_to_sets(automaton2)
    True
    """
    if isinstance(structure, list):
        # Then convert to a set
        new_struct = set()
        for item in structure:
            new_struct.add(convert_to_sets(item))
        return new_struct
    if isinstance(structure, dict):
        new_struct = {}
        for key, value in structure.items():
            # If the list has a child which is a list, do not convert
            # because Python will not allow it (also it is undesirable for
            # our uses)
            if len([x for x in value if isinstance(x, list)]) > 0:
                new_struct[key] = [convert_to_sets(x) for x in value]
            else:
                new_struct[key] = convert_to_sets(value)
        return new_struct
    return structure
