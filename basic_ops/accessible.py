from copy import deepcopy
from basic_ops.helpers.string_helpers import format_transition


def get_accessible(automaton):
    """Copies the automaton and prunes off any transitions/states which are not
    accessible from the initial state.

    Parameters
    ----------
    automaton : dictionary
        The automaton to remove unnecessary transitions/states

    Returns
    -------
    dictionary
        The resulting pruned, accessible automaton
    """
    automaton = deepcopy(automaton)
    events = automaton["events"]["all"]
    transitions = automaton["transitions"]["all"]
    queue = automaton["states"]["initial"].copy()
    accessible_states = set(queue)
    accessible_trans = dict()

    # Visit every state starting from initial
    while len(queue) > 0:
        curr = queue.pop(0)
        # Search for all accessible states from curr
        for event in events:
            trans = format_transition(curr, event)
            # If transition exists, add it and the state
            if trans in transitions:
                to = transitions[trans]
                accessible_trans[trans] = to
                if to not in accessible_states:
                    accessible_states.add(to)
                    queue.append(to)

    # Update the states
    automaton["states"]["all"] = sorted(accessible_states)
    automaton["states"]["marked"] = [
        [s for s in x if s in accessible_states]
        for x in automaton["states"]["marked"]
    ]
    # Deal with all the various possible types of states
    all_state_types = ["bad", "v1", "v2", "bad-v1", "bad-v2"]
    state_types = [x for x in all_state_types if x in automaton["states"]]
    for state_type in state_types:
        automaton["states"][state_type] = [
            x for x in automaton["states"][state_type] if x in accessible_states
        ]

    # Update the transitions
    automaton["transitions"]["all"] = accessible_trans
    # Deal with all various possible types of transitions
    all_trans_types = ["v1", "v2", "bad"]
    trans_types = [x for x in all_trans_types if x in automaton["transitions"]]
    for trans_type in trans_types:
        updated_trans = dict()
        for k, v in automaton["transitions"][trans_type].items():
            if k in accessible_trans:
                updated_trans[k] = v
        automaton["transitions"][trans_type] = updated_trans

    return automaton
