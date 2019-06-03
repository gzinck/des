from basic_ops.determinize import determinize
from arenas.helpers.control_actions import get_valid_control_actions
from arenas.helpers.state_helpers import check_marked_agents
from arenas.helpers.construct_arena_helpers import add_v2_transitions
from basic_ops.helpers.string_helpers import *


def construct_arena(automaton):
    """Constructs an arena from an automaton, as specified in (Ricker, Marchand,
    & Keroglou, 2019). The arena has the same form as a regular automaton,
    except with a few extra features. The "states" section has two extra lists:
    "v1" and "v2", which correspond to the two distinct types of states.
    The "transitions" section has two extra lists as well: "v1" and "v2", which
    are the two transition lists that exit out of the two sets of states,
    respectively.

    Note
    ----
    Any data on bad states or transitions will be not be included in the
    resulting automaton.
    Also, the automaton must have three entries in marked, observable, and
    controllable. The first is the controller's perspective, the second is the
    first agent's perspective, and the third is the second agent's perspective.
    Note that the two agents' events should be subsets of the controller's event
    set.
    TODO: add a verifier to ensure correct input.

    Parameters
    ----------
    automaton : dict
        The automaton for which to create an arena

    Returns
    -------
    dict
        The resulting arena

    Examples
    --------
    >>> arena = construct_arena(automaton)
    >>> print(arena)
    {
        # Dictionary for the arena with the added features specified above
    }
    """
    # Get the three observers
    all_events = automaton["events"]["all"]
    obs_events = automaton["events"]["observable"]
    all_automata = [
        determinize(automaton, i) for i in range(len(obs_events))
    ]
    all_automata.insert(0, automaton)

    bad_states = []

    # Get initial state. Since we determinized, each will only have one element.
    initial = [a["states"]["initial"][0] for a in all_automata]
    initial_str = format_state(initial)

    new_events = set()
    v1_trans = {}
    v2_trans = {}
    # Add initial state to a visited set and a queue
    v1_queue = [initial]
    v1_visited = {initial_str}
    v2_visited = set()
    # Keep track of secrets
    secrets = {}

    # Keep going through our queue of controller states until done
    while len(v1_queue) > 0:
        curr = v1_queue.pop(0)
        curr_str = format_state(curr)

        # Check if we have a bad state
        marked_obs = check_marked_agents(all_automata, curr)
        if len(marked_obs) != 0:
            bad_states.append(curr_str)
            secrets[curr_str] = format_all_observed_secrets(marked_obs)

        # Identify what events are accessible from here
        events = get_valid_control_actions(all_automata[0], curr[0], all_events)

        for event in events:
            # Add this event to the system
            event_str = format_state_set(event)
            new_events.add(event_str)

            # Add the transition from v1 to the state in v2
            trans = format_transition(curr_str, event_str)
            curr_v2_str = format_state([curr_str, event_str])
            v1_trans[trans] = [curr_v2_str]

            # If we haven't already visited this v2 state, start working on it!
            if curr_v2_str not in v2_visited:
                v2_visited.add(curr_v2_str)
                add_v2_transitions(all_automata, curr, event, v2_trans,
                                   v2_visited, v1_visited, v1_queue)

    # The language includes both the new event types we added and the events
    # already visible to the controller
    all_events = list(new_events.union(set(automaton["events"]["all"])))
    obs_events = list(new_events.union(set(obs_events[0])))

    return {
        "events": {
            "all": all_events,  # The events start off identical
            "controllable": [list(new_events)],  # In arena, control just new
            "observable": [obs_events]
        },
        "states": {
            "all": list(v1_visited.union(v2_visited)),
            "v1": list(v1_visited),
            "v2": list(v2_visited),
            "initial": [initial_str],
            "marked": [bad_states],
            "bad": bad_states,
            "secrets": secrets  # Indicates which agent sees what in composition
        },
        "transitions": {
            "all": {**v1_trans, **v2_trans},
            "v1": v1_trans,
            "v2": v2_trans,
            "bad": {}
        }
    }