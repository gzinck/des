from basic_ops.helpers.string_helpers import *


def add_communication(automaton, agent):
    # Events
    reg_events = automaton["events"]["all"]
    rec_events = [f'?{event}' for event in reg_events if event != "tau"]
    send_events = [f'!{event}' for event in reg_events if event != "tau"]

    # Transitions
    old_trans = automaton["transitions"]["all"]
    old_spec = automaton["transitions"]["specification"]
    new_trans = {}
    new_spec = {}

    # States
    new_states = set()
    new_states.add(automaton["states"]["initial"][0])

    # Start off the queue with the initial state
    # Doubled because the state has no annotations
    queue = [[automaton["states"]["initial"][0]] * 2]

    while len(queue) > 0:
        # The state and the state without any annotations
        curr, curr_no_annot = queue.pop(0)

        # Go through every event
        for event in reg_events:
            orig_trans = format_transition(curr_no_annot, event)
            if orig_trans in old_trans:
                nxt = old_trans[orig_trans][0]
                # Then add it to the new one
                trans = format_transition(curr, event)
                new_trans[trans] = [nxt]
                # Check if we need to do the same in the spec
                if orig_trans in old_spec:
                    new_spec[trans] = [nxt]

                # Add to the queue with the newly reachable state
                if nxt not in new_states:
                    queue.append([nxt, nxt])
                    new_states.add(nxt)
                # If observable, also add send
                if event in automaton["events"]["observable"][agent]:
                    new_t = format_transition(nxt, f'!{event}')
                    new_nxt = f'{nxt}!'
                    new_trans[new_t] = [new_nxt]
                    # Add to spec if we should
                    if orig_trans in old_spec:
                        new_spec[new_t] = [new_nxt]
                    # Add to the queue
                    if new_nxt not in new_states:
                        queue.append([new_nxt, nxt])
                        new_states.add(new_nxt)
                else:
                    new_t = format_transition(nxt, f'?{event}')
                    new_nxt = f'{nxt}?'
                    new_trans[new_t] = [new_nxt]
                    # Add to spec if we should
                    if orig_trans in old_spec:
                        new_spec[new_t] = [new_nxt]
                    # Add to the queue
                    if new_nxt not in new_states:
                        queue.append([new_nxt, nxt])
                        new_states.add(new_nxt)

    return {
        "events": {
            "all": reg_events + rec_events + send_events,
            "controllable": automaton["events"]["controllable"],
            "observable": automaton["events"]["observable"],
            "regular": reg_events,
            "receive": rec_events,
            "send": send_events
        },
        "states": {
            "all": list(new_states),
            "initial": automaton["states"]["initial"],
            "marked": automaton["states"]["marked"],
            "bad": automaton["states"]["bad"]
        },
        "transitions": {
            "all": new_trans,
            "specification": new_spec,
            "bad": automaton["transitions"]["bad"]
        }
    }


