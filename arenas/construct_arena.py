from basic_ops.determinize import determinize
from arenas.helpers.control_actions import get_valid_control_actions
from arenas.helpers.state_helpers import find_next_state, check_marked_agents
import basic_ops.helpers.string_helpers as str_helper


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
    TODO: add a verifier to ensure correct input.

    Parameters
    ----------
    automaton : dict
        The automaton for which to create an arena

    Yields
    ------
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
    events = automaton["events"]
    controller = determinize(automaton, events["observable"][0])
    agent1 = determinize(automaton, events["observable"][1])
    agent2 = determinize(automaton, events["observable"][2])
    all_automata = [controller, agent1, agent2]

    bad_states = []
    # Get initial state
    initial = [
        controller["states"]["initial"],
        agent1["states"]["initial"],
        agent2["states"]["initial"]
    ]
    initial_str = str_helper.format_state(initial)

    new_events = set()
    v1_trans = {}
    v2_trans = {}
    # Add initial state to a visited set and a queue
    queue = [initial]
    v1_visited = set([initial_str])
    v2_visited = set()

    # Keep going through our queue until done
    while len(queue) > 0:
        curr = queue.pop(0)
        curr_str = str_helper.format_state(curr)

        # Check if we have a bad state
        if check_marked_agents(all_automata, curr):
            bad_states.append(curr_str)

        # Identify what events are accessible from here
        events = get_valid_control_actions(controller, curr[0])
        new_events = new_events.union(events)
        for event in events:
            # Add this event to the system
            event_str = str_helper.format_state_set(event)  # Turns it into a string
            events.add(event_str)

            # Add the transition from v1 to the state in v2
            trans = str_helper.format_transition(curr_str, event_str)
            currv2 = str_helper.format_state(curr_str, event_str)
            v1_trans[trans] = [currv2]
            v2_visited.add(currv2)

            # Find all the places that are accessible from v2
            for subevent in event:
                nextv1 = find_next_state(all_automata, curr, subevent)
                nextv1_str = str_helper.format_state(nextv1)
                # Add the transition
                trans = str_helper.format_transition(currv1, subevent)
                v2_trans[trans] = [nextv1_str]
                # If not visited, visit it
                if nextv1_str not in v1_visited:
                    v1_visited.add(nextv1_str)
                    queue.append(nextv1)

    # The language includes both the new event types we added and the events
    # already visible to the controller
    all_events = list(new_events.union(automaton["events"]["observable"][0]))
    cont_events = automaton["events"]["observable"].copy()

    # The controller can only control new ones
    cont_events[0] = list(new_events)
    return {
        "events": {
            "all": all_events,  # The events start off identical
            "controllable": cont_events,  # In arena, control whatever observe
            "observable": automaton["events"]["observable"].copy()
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
