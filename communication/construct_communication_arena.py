from basic_ops.helpers.string_helpers import *

def construct_communication_arena(automaton):
	"""Constructs an arena from an automaton, as specified in a tutorial in
	(Ricker, 2013). The arena has only one type of state and one type of
	transitions. Each state is a tuple: the actual state of the system, the
	first agent's guessed state of the system, the second, the third, etc.
	Each transition is a vector <a, a, a, ...> representing either that
	an event a has occurred and is observed by all agents that can observe
	the event, or some agent i has guessed that a has occurred. All agents
	that did not see (or guess) a see epsilon instead (or an underscore).

	Parameters
	----------
	automaton : dict
		The automaton for which to create an arena

	Returns
	-------
	dict
		The resulting arena
	"""
	all_events = automaton["events"]["all"]
	obs_events = automaton["events"]["observable"]
	num_agents = len(obs_events)
	original_trans = automaton["transitions"]["all"]

	events = set()
	transitions = {}

	# Get the initial state. Should have (num_agents + 1)
	initial = [automaton["states"]["initial"][0] for i in range(num_agents + 1)]
	initial_str = format_state(initial)
	visited = {initial_str}
	queue = [initial]

	# Keep going through the states until no more states to generate
	while len(queue) > 0:
		curr = queue.pop(0)
		curr_str = format_state(curr)

		# Go through every possible event that is possible from this state
		for event in all_events:
			# Find all agents who can observe the event.
			# Should always include the first agent (i.e., the actual system).
			agent_observation = [event in obs for obs in [[event]] + obs_events]

			# First, see if we can go to the next state in actual system
			trans = format_transition(curr[0], event)
			if trans in original_trans:
				# Then, add the transition
				nxt_state = []
				trans_event = []
				success = True # Stop if going to inconsistent state
				for i in range(num_agents + 1):
					if agent_observation[i]:
						trans = format_transition(curr[i], event)
						if trans in original_trans:
							# Note: transitions are assumed deterministic
							nxt_state += [original_trans[trans][0]]
						else:
							success = False # Reached inconsistent state
							break
						trans_event += [event]
					else:
						nxt_state += [curr[i]]
						trans_event += ["_"]
				
				# If not an inconsistent state, add it
				if success:
					nxt_state_str = format_state(nxt_state)
					trans_event_str = format_event_vector(trans_event)
					events.add(trans_event_str)

					# Add the transition
					trans = format_transition(curr_str, trans_event_str)
					transitions[trans] = [nxt_state_str]

					# If we haven't already visited this state, add to queue
					if nxt_state_str not in visited:
						visited.add(nxt_state_str)
						queue += [nxt_state]
			
			# Now, do all the guessing!
			for i in [x for x in range(num_agents + 1) if not agent_observation[x]]:
				nxt_state = curr.copy()
				trans_event = ["_"] * (num_agents + 1)
				
				# Replace this guy's state and event
				trans_event[i] = event
				trans = format_transition(curr[i], event)
				if trans in original_trans:
					nxt_state[i] = original_trans[trans][0]
					nxt_state_str = format_state(nxt_state)
					trans_event_str = format_event_vector(trans_event)

					# Add the event to the automaton
					events.add(trans_event_str)
					
					# Now, add the transition
					trans = format_transition(curr_str, trans_event_str)
					transitions[trans] = [nxt_state_str]

					# Check if not visited
					if nxt_state_str not in visited:
						visited.add(nxt_state_str)
						queue += [nxt_state]

	# Now, we have all states and transitions.
	return {
		"events": {
			"all": list(events),
			"controllable": [list(events)],
			"observable": [list(events)]
		},
		"states": {
			"all": list(visited),
			"initial": [initial_str],
			"marked": [],
			"bad": [],
			"secrets": []
		},
		"transitions": {
			"all": transitions,
			"bad": {}
		}
	}
