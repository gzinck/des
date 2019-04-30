def verify(automaton1, automaton2):
    '''DEPRICATED: DO NOT USE.
    This was designed to verify two automata were identical. The better way
    is to use convert_to_sets of each automata data structure and perform
    the equals operation to evaluate if the two are identical.
    '''
    tests = [[automaton1, automaton2], [automaton2, automaton1]]
    for test in tests:
        a1 = test[0]
        a2 = test[1]

        # Verify all types of states are identical
        state_types = ["all", "initial", "bad"]
        for state_type in state_types:
            if state_type in a1["states"]:
                for state in a1["states"][state_type]:
                    if state not in a2["states"][state_type]:
                        print("Missing state in", state_type, ":", state)
                        return False

        # Verify all types of alphabets are identical
        alphabets = ["all", "attacker", "bad"]
        for alphabet in alphabets:
            if alphabet in a1["events"]:
                for event in a1["events"][alphabet]:
                    if event not in a2["events"][alphabet]:
                        print("Missing event in", alphabet, ":", event)
                        return False

        # This covers the types of alphabets that are arrays of arrays
        more_alphabets = ["controllable", "observable"]
        for alphabet in more_alphabets:
            if alphabet in a1["events"]:
                if(len(a1["events"][alphabet]) != len(a2["events"][alphabet])):
                    print("Number of", alphabet, "alphabets is not identical")
                    return False
                for i in range(len(a1["events"][alphabet])):
                    for event in a1["events"][alphabet][i]:
                        if event not in a2["events"][alphabet][i]:
                            print("Missing event in", alphabet, ":", event)
                            return False

        # Verify all transitions are identical
        transition_types = ["all", "bad"]
        for t_type in transition_types:
            if t_type in a1["transitions"]:
                for key, value in a1["transitions"][t_type].items():
                    if key not in a2["transitions"][t_type]:
                        print("Missing transition in", t_type, ":", key)
                        return False
                    if a1["transitions"][t_type][key] != value:
                        print("Missing transition in", t_type, ":", key)
                        return False
    return True
