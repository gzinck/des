from basic_ops.helpers.string_helpers import *
from arenas.helpers.state_helpers import find_next_state


def construct_arena_helper(automata, state, event_set, v2_trans, v2_visited):
    v1_visited = set()
    queue = [(state, event_set)]
    while len(queue) > 0:
        curr = queue.pop(0)
        state = curr[0]
        state_str = format_state(state)
        events = curr[1]
        events_str = format_state_set(events)

        curr_str = format_state([state_str, events_str])

        for event in events:
            nxt = find_next_state(automata, state, event)
            nxt_str = format_state(nxt)
            trans = format_transition(curr_str, event)

            if event in automata[0]["events"]["observable"][0]:
                # Then we go back to a v1
                v2_trans[trans] = [nxt_str]
                v1_visited.add(nxt_str)
            else:
                # Then we go to a v2 with same events_str
                nxt_str = format_state([nxt_str, events_str])
                v2_trans[trans] = [nxt_str]
                if nxt_str not in v2_visited:
                    v2_visited.add(nxt_str)
                    queue.append((nxt, events))