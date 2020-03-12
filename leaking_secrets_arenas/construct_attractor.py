from leaking_secrets_arenas.helpers.construct_attractor_helpers import *
from copy import deepcopy


def construct_attractor(arena):
    """Constructs an attractor, as defined in Appendix 6.1 of "Opacity with
    powerful attackers" (Hélouët, Marchand, & Ricker, 2018). That is, it
    copies the input arena and creates three sets: "bad", "bad-v1", and "bad-v2"
    which represent all bad states in the arena, the bad v1 states, and bad v2
    states, respectively.
    A bad-v2 state is defined as a state for which all control actions (i.e.,
    all events) lead to a bad-v1 state.
    A bad-v1 state is either pre-defined by the input arena, or it is a state
    which has an event to a bad-v2 state.

    Parameters
    ----------
    arena : dictionary
        The arena for which to create an attractor

    Returns
    -------
    dictionary
        The attractor, which is essentially a copy of the arena with extra bad
        states.
    """
    attractor = deepcopy(arena)
    attractor["states"]["bad-v1"] = attractor["states"]["bad"]
    attractor["states"]["bad-v2"] = []

    # Keep iterating until not marking any more as bad
    keep_going = True
    while keep_going:
        keep_going = False
        keep_going += mark_bad_v2s(attractor)
        keep_going += mark_bad_v1s(attractor)

    bad = []
    bad.extend(attractor["states"]["bad-v1"])
    bad.extend(attractor["states"]["bad-v2"])
    attractor["states"]["bad"] = bad
    return attractor
