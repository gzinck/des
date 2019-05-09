import basic_ops.helpers.string_helpers as helper
import basic_ops.helpers.state_helpers as state_helper


def union_events(automata):
    """Unions all of the events of multiple automata

    Parameters
    ----------
    automata : array of dictionaries
        Array of all of the automata which should be composed

    Yields
    ------
    dict
        Dictionary containing the union for all events, controllable events,
        and observable events.

    Examples
    --------
    >>> events = union_events([automaton1, automaton2, automaton3])
    >>> print(events)
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
    """
    if len(automata) < 2:
        raise Exception("Union requires at least two automata in a list as input.")

    # The number of players with different alphabets for observing/controlling
    num_players = len(automata[0]["events"]["controllable"])
    all_events = set()
    attacker_events = set()
    cont_events = [set()] * num_players
    obs_events = [set()] * num_players

    # For each automaton, add its events
    for a in automata:
        events = a["events"]
        all_events = all_events.union(set(events["all"]))
        attacker_events = all_events.union(set(events["attacker"]))

        # Add the controllable and observable events from each of the automata
        for i in range(num_players):
            cont_events[i] = cont_events[i].union(set(events["controllable"][i]))
            obs_events[i] = obs_events[i].union(set(events["observable"][i]))

    # Add the events to the result
    return {
        "all": list(all_events),
        # Extract the list of sets into a list of lists
        "controllable": [list(events) for events in cont_events],
        "observable": [list(events) for events in obs_events],
        "attacker": list(attacker_events)
    }


def union_transitions(automata, all_events):
    """Unions the transitions of multiple automata. That is, a transition is
    defined from a state if and only if all automata that have such an event
    defined have a transition defined. This also applies when only one
    automaton has a transition defined.

    This also generates the state space for the unioned automaton.

    Note
    ----
    Any data on bad states or transitions will be not be included in the
    resulting automaton.

    Parameters
    ----------
    automata : array of dictionaries
        Array of all of the automata which should be composed
    all_events : array of strings
        Array of all events that are defined for the automata (even those that
        are only defined in one of them)

    Yields
    ------
    dict
        All of the states and transitions that are defined in a composed union
        of the automata


    Examples
    --------
    In the case of an empty automaton
    >>> print(union_transitions(automaton))
    {
        "states": {
            "all": [],
            "initial": [],
            "bad": [],
            "marked": [[]]
        },
        "transitions": {
            "all": {},
            "bad": {}
        }
    }
    """
    # We'll compute marked states for each of the agents
    num_agents = len(automata[0]["states"]["marked"])
    marked = [[]] * num_agents  # The marked states init to empty

    # Get the initial states, mark them as visited (must convert to strings
    # in order to hash them)
    initial_states = state_helper.get_initial(automata)
    initial_strings = [helper.format_state(s) for s in initial_states]

    transitions = {}  # The transitions for the resulting automaton

    # Go through all states systematically
    queue = initial_states.copy()
    visited = set(initial_strings)

    # Keep going through queue until done
    while len(queue) > 0:
        curr = queue.pop(0)
        curr_str = helper.format_state(curr)

        # Add the state to marked, if needed, for each agent
        for agent in range(num_agents):
            if state_helper.check_marked(automata, curr, agent):
                marked[agent].append(curr_str)

        # Go through every event in alphabet
        for event in all_events:
            # Track if the transition does NOT exist in an automaton where it
            # should
            failure = False
            next_state = []
            for i in range(len(automata)):
                # Get the automaton and its state
                a = automata[i]
                prev_state = curr[i]

                # If the state should exist here
                if event in a["events"]["all"]:
                    # Then check if valid
                    transition = helper.format_transition(prev_state, event)
                    if transition in a["transitions"]["all"]:
                        next_state.append(a["transitions"]["all"][transition])
                    else:
                        failure = True  # Not defined
                else:
                    # Then we don't change states
                    next_state.append([prev_state])
            if not failure:
                # Get all possibilities (if nondeterministic)
                next_states = helper.get_states(next_state)
                # Get a string state for use with sets in python
                next_strings = [helper.format_state(nxt) for nxt in next_states]
                # When adding transitions, convert to string format
                transitions[helper.format_transition(helper.format_state(curr), event)] = next_strings
                for i in range(len(next_strings)):
                    if next_strings[i] not in visited:
                        # Then add this state to process next
                        queue.append(next_states[i])
                        visited.add(next_strings[i])
    return {
        "states": {
            "all": list(visited),
            "initial": [helper.format_state(s) for s in initial_states],
            "bad": [],
            "marked": marked
        },
        "transitions": {
            "all": transitions,
            "bad": {}
        }
    }
