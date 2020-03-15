from basic_ops.helpers.string_helpers import *


def add_clock_ticks(automaton, delta):
    """Adds clock ticks every delta events to the automaton, starting with
    adding a clock tick at the beginning.

    Parameters
    ----------
    automaton: dict
        The automaton to add clock ticks to
    delta: int
        The frequency of clock ticks, where delta is the number of events
        between ticks
    """
    all_events = automaton["events"]["all"]

    # First, add a clock tick at the beginning
    old_initial = automaton["states"]["initial"][0]

    # Give the new initial state a new name
    new_initial = "0"

    old_trans = automaton["transitions"]["all"]
    old_spec = automaton["transitions"]["specification"]
    new_trans = {}
    new_spec = {}
    new_states = set()

    # Step 1: put a transition from new initial to the old one

    new_trans[format_transition(new_initial, "tau")] = [set_since_tau(old_initial, 0)]

    # Add states
    new_states.add(new_initial)
    new_states.add(set_since_tau(old_initial, 0))

    # Step 2: add taus every delta events
    # We implement with BFS
    queue = [set_since_tau(old_initial, 0)]

    while len(queue) > 0:
        curr = queue.pop(0)
        curr_state = extract_state_without_since_tau(curr)
        curr_taucount = extract_since_tau(curr)

        if curr_taucount < delta:
            # Go through every event
            for event in all_events:
                # Check if transition exists
                trans = format_transition(curr_state, event)
                if trans in old_trans:
                    # Should add transition
                    nxt_state = set_since_tau(old_trans[trans][0], curr_taucount + 1)
                    new_trans[format_transition(curr, event)] = [nxt_state]

                    # Add to specification if needed
                    if trans in old_spec:
                        new_spec[format_transition(curr, event)] = [nxt_state]

                    # Add the state
                    if nxt_state not in new_states:
                        new_states.add(nxt_state)
                        queue.append(nxt_state)

        else:
            # If we need to have a tau, tau it up!
            nxt_state = set_since_tau(curr_state, 0)
            new_trans[format_transition(curr, "tau")] = [nxt_state]
            new_spec[format_transition(curr, "tau")] = [nxt_state]
            if nxt_state not in new_states:
                new_states.add(nxt_state)
                queue.append(nxt_state)

    return {
        "events": {
            "all": all_events + ["tau"],
            "controllable": automaton["events"]["controllable"],
            "observable": automaton["events"]["observable"]
        },
        "states": {
            "all": list(new_states),
            "initial": [new_initial],
            "marked": automaton["states"]["marked"],
            "bad": automaton["states"]["bad"],
        },
        "transitions": {
            "all": new_trans,
            "specification": new_spec,
            "bad": automaton["transitions"]["bad"]
        }
    }
