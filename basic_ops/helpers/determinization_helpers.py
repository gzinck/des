from basic_ops.helpers.string_helpers import format_transition, format_state_set
from basic_ops.helpers.state_helpers import check_marked_inverse

def get_unobservable_reach(automaton, states, alphabet):
    '''Gets all states that are accessible from some macro-state using
    unobservable events (i.e., events that are not part of the input alphabet).

    Parameters
    ----------
    automaton : dictionary
        The automaton for which we are looking for the unobservable reach
    states : list
        The list of states from which we are looking for unobservable events.
        These will all be included in the resulting unobservable reach
    alphabet : list
        The list of all events that are observable

    Yields
    ------
    list
        All states accessible from the provided states

    Examples
    --------
    >>> print(get_unobservable_reach(automaton, ["q1", "q2"], ["c"]))
    ["q1", "q2", "q3", "q4"]
    '''
    # The unobservable events are the difference between all and obs
    unobs_events = set(automaton["events"]["all"]).difference(set(alphabet))
    transitions = automaton["transitions"]["all"]
    accessible = set(states)
    queue = states.copy()

    # Do a BFS to find all accessible states
    while len(queue) > 0:
        curr = queue.pop(0)
        for event in unobs_events:
            # See if the transition exists
            trans = format_transition(curr, event)
            if trans in transitions:
                # See if we already reached the state
                destination = transitions[trans]
                for state in destination:
                    if state not in accessible:
                        accessible.add(state)
                        queue.append(state)
    return list(accessible)

def determinize_transitions(automaton, alphabet):
    '''Creates the transition function and state space for the determinized
    version (Det(A)) of the input automaton (A). That is, the initial
    macro-state of Det(A) is defined as the set containing the initial state of
    A and its unobservable reach. A transition to another macro-state is defined
    if there exists at least one transition from one of the states composing a
    macro-state, and it goes to a set containing the unobservable reaches of all
    reachable states from the previous macro-state's elements.

    Parameters
    ----------
    automaton : dictionary
        The automaton for which to find the determinized transitions and states
    alphabet : list
        The list of all events that are observable

    Yields
    ------
    dict
        All of the states and transitions that are defined in a composed union
        of the automata

    Examples
    --------
    In the case of an empty automaton
    >>> print(determinize_transitions(automaton))
    {
        "states": {
            "all": [],
            "initial": [],
            "bad": [],
            "marked": []
        },
        "transitions": {
            "all": {},
            "bad": {}
        }
    }
    '''
    # Get the old transitions
    old_transitions = automaton["transitions"]["all"]

    # First, get the initial state
    marked = []
    initial_state = get_unobservable_reach(automaton, automaton["states"]["initial"], alphabet)
    initial_state.sort()
    initial_state_str = format_state_set(initial_state)
    visited = set([initial_state_str])
    transitions = {}
    # If marked, make sure to mark this one. Note that it's the inverse marking
    # function because opacity requires at least one state to be unmarked to
    # maintain opacity.
    if check_marked_inverse(automaton, initial_state):
        marked.append(initial_state_str)

    # Go through the states
    queue = [initial_state]
    while len(queue) > 0:
        curr = queue.pop(0)
        curr_str = format_state_set(curr)
        # Find out what states are accessible
        for event in alphabet:
            next = set()
            # Check for transition with every state in the macro-state
            for state in curr:
                trans = format_transition(state, event)
                # If transition exists, add destination's unobservable reach to
                # next
                if trans in old_transitions:
                    next.update(get_unobservable_reach(automaton, old_transitions[trans], alphabet))
            # If the event is valid, then define it
            if len(next) > 0:
                # Get next in sorted form
                next = list(next)
                next.sort()
                next_str = format_state_set(next)
                # Add this transition
                trans = format_transition(curr_str, event)
                transitions[trans] = [next_str]
                # Add it to the queue, if not visited
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next)
                    # Check if should be marked, if so, add to marked.
                    if check_marked_inverse(automaton, next):
                        marked.append(next_str)

    return {
        "states": {
            "all": list(visited),
            "initial": [initial_state_str],
            "bad": [],
            "marked": marked
        },
        "transitions": {
            "all": transitions,
            "bad": {}
        }
    }
