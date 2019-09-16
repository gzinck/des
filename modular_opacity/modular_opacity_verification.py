from basic_ops.opacity import check_opacity
from basic_ops.product import product


def check_modular_opacity(automata):
    """Verifies current state opacity for the modular system composed of the
    input automata. Assumes that the shared alphabet of the automata is a
    subset of the attacker's alphabet, and the attacker's alphabet is defined
    by the second (i.e., index 1, when zero indexed) observable alphabet. Only
    one set of secrets (i.e., marked states) will be checked (the 0th set).

    Parameters
    ----------
    automata : list
        The automata for which to check for opacity

    Returns
    -------
    bool
        Whether the set of modules is opaque
    """
    verified = []
    unverified = automata.copy()
    for a in automata:
        if a in unverified:
            unverified.remove(a)

            # Keep a list of all automata we can use to append to current one
            automata_to_add = unverified.copy()
            automata_to_add.fromlist(verified)

            verified.append(a)

            # Keep track of the large automaton we're building
            curr = a

            # Keep going until it's opaque
            while check_opacity(curr, 1) == False:
                if len(automata_to_add) == 0:
                    return False
                next = automata_to_add.pop(0)
                verified.append(next)
                unverified.remove(next)
                curr = product([curr, next])

    return True
