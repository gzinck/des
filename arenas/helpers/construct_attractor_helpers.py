def mark_bad_v2s(attractor):
    """Adds bad-v2 states to the attractor—that is, v2 states which lead to
    bad-v1 states.

    Parameters
    ----------
    attractor : dictionary
        The attractor, which is essentially an arena but with more bad states

    Returns
    -------
    boolean
        Whether or not there were any extra bad-v2 added
    """
    bad_added = False
    all_trans = attractor["transitions"]["v2"]
    for v2_state in attractor["states"]["v2"]:

        # Don't worry about this state if already bad
        if v2_state in attractor["states"]["bad-v2"]:
            continue

        nxt_options = [v for k, v in all_trans.items() if v2_state in k]

        # If there are no transitions, we're fine
        if len(nxt_options) == 0:
            continue

        # Go through every transition, if one leads to bad, we're not ok
        is_bad = False
        for nxt_set in nxt_options:
            for nxt in nxt_set:
                if nxt in attractor["states"]["bad-v1"]:
                    is_bad = True

        # If no good options, this is a bad state
        if is_bad:
            attractor["states"]["bad-v2"].append(v2_state)
            bad_added = True
    return bad_added


def mark_bad_v1s(attractor):
    """Adds bad-v1 states to the attractor—that is, v1 states for which all
    control decisions lead to bad-v2 states.

    Parameters
    ----------
    attractor : dictionary
        The attractor, which is essentially an arena but with more bad states

    Returns
    -------
    boolean
        Whether or not there were any extra bad-v1s added
    """
    bad_added = False
    all_trans = attractor["transitions"]["v1"]
    for v1_state in attractor["states"]["v1"]:

        # Don't worry about this state if already bad
        if v1_state in attractor["states"]["bad-v1"]:
            continue

        nxt_options = [v for k, v in all_trans.items() if v1_state in k]

        # If there are no transitions, we're fine
        if len(nxt_options) == 0:
            continue

        # Go through every transition, if one does not lead to bad, we're happy
        all_bad = True
        for nxt_set in nxt_options:
            for nxt in nxt_set:
                if nxt not in attractor["states"]["bad-v2"]:
                    all_bad = False

        # If no good options, this is a bad state
        if all_bad:
            attractor["states"]["bad-v1"].append(v1_state)
            bad_added = True
    return bad_added
