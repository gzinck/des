from basic_ops.helpers.string_helpers import *
from arenas.helpers.state_helpers import find_next_state


def add_v2_transitions(automata, state, enabled_events, v2_trans, v2_visited, v1_visited, v1_queue):
    """Adds transitions leaving a given v2 state to v1 and v2 states. If it
    leads to another v2 state, then it adds that v2 state and continues adding
    that state's transitions.

    Parameters
    ----------
    automata : list of dictionaries
        The automata from which the arena is being constructed
    state : list of strings
        The strings representing the current state of each automaton
    enabled_events : set
        The events which are allowed from the current state
    v2_trans : dictionary
        The transitions leaving v2 states
    v2_visited : set
        A set of all visited v2 states (avoids recomputing states)

    Returns
    -------
    None
    """
    # Go through every v2 state we encounter
    queue = [(state, enabled_events)]
    while len(queue) > 0:

        # Turn this info in the queue into string format
        curr = queue.pop(0)
        state = curr[0]
        state_str = format_state(state)
        events = curr[1]
        events_str = format_state_set(events)

        # This is the string representing the current system state
        curr_str = format_state([state_str, events_str])

        # For every possible event that's allowed...
        for event in events:
            nxt = find_next_state(automata, state, event)
            # If this event doesn't actually do anything, ignore
            if nxt == state:
                continue
            # Else, add the transition
            nxt_str = format_state(nxt)
            trans = format_transition(curr_str, event)

            if event in automata[0]["events"]["observable"][0]:
                # Then we go back to a v1
                v2_trans[trans] = [nxt_str]
                if nxt_str not in v1_visited:
                    v1_visited.add(nxt_str)
                    v1_queue.append(nxt)
            else:
                # Then we go to a v2 with same events_str
                nxt_str = format_state([nxt_str, events_str])
                v2_trans[trans] = [nxt_str]
                if nxt_str not in v2_visited:
                    v2_visited.add(nxt_str)
                    queue.append((nxt, events))
