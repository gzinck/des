from copy import deepcopy
from itertools import chain
from basic_ops.helpers.string_helpers import extract_state
from basic_ops.accessible import get_accessible


def get_coaccessible(automaton):
    """Copies all states and transitions from the automaton that lead to a
    marked state (for any agent).

    Parameters
    ----------
    automaton : dict
        The automaton for which to extract the good transitions

    Returns
    -------
    dict
        The resulting pruned, coaccessible automaton
    """
    automaton = deepcopy(automaton)
    events = automaton["events"]["all"]
    transitions = automaton["transitions"]["all"]
    accessible_states = set(chain.from_iterable(automaton["states"]["marked"]))
    accessible_trans = dict()

    # Keep track of how many states we add on. If we add on none, stop!
    prv_len = 0
    curr_len = len(accessible_states)

    # Keep going until convergence
    while prv_len < curr_len:
        prv_len = curr_len
        # For every trans that goes to a marked state, add it
        for k, v in transitions.items():
            for s in v:
                if s in accessible_states:
                    from_state = extract_state(k)
                    if from_state not in accessible_states:
                        accessible_states.add(from_state)
                    if k in accessible_trans:
                        accessible_trans[k].append(s)
                    else:
                        accessible_trans[k] = [s]

        curr_len = len(accessible_states)

    # Update the states
    automaton["states"]["all"] = sorted(accessible_states)
    automaton["states"]["marked"] = [
        [s for s in x if s in accessible_states]
        for x in automaton["states"]["marked"]
    ]
    # Deal with all the various possible types of states
    all_state_types = ["bad", "initial", "v1", "v2", "bad-v1", "bad-v2"]
    state_types = [x for x in all_state_types if x in automaton["states"]]
    for state_type in state_types:
        automaton["states"][state_type] = [
            x for x in automaton["states"][state_type] if x in accessible_states
        ]
    # Update the transitions
    automaton["transitions"]["all"] = accessible_trans
    # Deal with all various possible types of transitions
    all_trans_types = ["v1", "v2", "bad"]
    trans_types = [x for x in all_trans_types if
                   x in automaton["transitions"]]
    for trans_type in trans_types:
        updated_trans = dict()
        for k, v in automaton["transitions"][trans_type].items():
            if k in accessible_trans:
                updated_trans[k] = v
        automaton["transitions"][trans_type] = updated_trans

    return get_accessible(automaton)
