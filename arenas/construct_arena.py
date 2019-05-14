from basic_ops.determinize import determinize
from arenas.helpers.control_actions import get_valid_control_actions
from arenas.helpers.state_helpers import find_next_state, check_marked_agents
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
    obs_events = automaton["events"]["observable"]
    controller = determinize(automaton, obs_events[0])
    agent1 = determinize(automaton, obs_events[1])
    agent2 = determinize(automaton, obs_events[2])
    all_automata = [automaton, controller, agent1, agent2]

    bad_states = []

    # Get initial state. Since we determinized, each will only have one element.
    initial = [a["states"]["initial"][0] for a in all_automata]
    initial_str = format_state(initial)

    new_events = set()
    v1_trans = {}
    v2_trans = {}
    # Add initial state to a visited set and a queue
    v1_queue = [initial]
    v2_queue = []
    v1_visited = {initial_str}
    v2_visited = set()

    # Keep going through our queue of controller states until done
    while len(v1_queue) > 0:
        curr = v1_queue.pop(0)
        curr_str = format_state(curr)

        # Check if we have a bad state
        if check_marked_agents(all_automata, curr):
            bad_states.append(curr_str)

        # Identify what events are accessible from here
        events = get_valid_control_actions(controller, curr[1])

        for event in events:
            # Add this event to the system
            event_str = format_state_set(event)
            new_events.add(event_str)

            # Add the transition from v1 to the state in v2
            trans = format_transition(curr_str, event_str)
            curr_v2_str = format_state([curr_str, event_str])
            v1_trans[trans] = [curr_v2_str]
            if curr_v2_str not in v2_visited:
                v2_visited.add(curr_v2_str)
                v2_queue.append((curr, event))

            # Deal with all of the things it leads to
            while len(v2_queue) > 0:
                curr_v2 = v2_queue.pop(0)

                # Extract the information
                curr_v2_state = curr_v2[0]
                curr_v2_sstr = format_state(curr_v2_state)
                curr_v2_events = curr_v2[1]
                curr_v2_estr = format_state_set(curr_v2_events)
                curr_v2_str = format_state([curr_v2_sstr, curr_v2_estr])

                # Find all the places that are accessible from v2
                for v2_event in curr_v2_events:
                    next_state = find_next_state(all_automata, curr_v2_state, v2_event)
                    next_sstr = format_state(next_state)
                    # Add the transition
                    trans = format_transition(curr_v2_str, v2_event)

                    # Identify which set it goes into
                    if v2_event in obs_events[0]:
                        # Then it goes to v1, as normal
                        v2_trans[trans] = [next_sstr]
                        if next_sstr not in v1_visited:
                            v1_visited.add(next_sstr)
                            v1_queue.append(next_state)
                    else:
                        # Then it goes to another state in v2, same event set
                        next_sstr = format_state([next_sstr, event_str])
                        v2_trans[trans] = [next_sstr]
                        if next_sstr not in v2_visited:
                            v2_visited.add(next_sstr)
                            v2_queue.append((curr, event))

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
            "bad": bad_states
        },
        "transitions": {
            "all": {**v1_trans, **v2_trans},
            "v1": v1_trans,
            "v2": v2_trans,
            "bad": {}
        }
    }
