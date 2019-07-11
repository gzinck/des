def __make_event_list(events):
    """Makes a list of events separated by commas (string form)

    Parameters
    ----------
    events : list
        List of events to stringify

    Returns
    -------
    str
        The list of events (sorted)
    """
    events.sort()
    string = ""
    for event in events:
        string += event + ", "
    return string[:-2]


def generate_event_legend(events):
    """Generates a legend for events and returns a string in dot language.
    For more information, visit https://graphviz.readthedocs.io.

    Parameters
    ----------
    events : list
        Strings representing the possible events in the system

    Returns
    -------
    str
        The dot code for the events legend in the graph, which should be
        appended to the body of the graphviz document
    """
    legend_start = '''
        rankdir=LR
        node [shape=plaintext]
        subgraph cluster_01 {
            label = "Legend\n\nA state with an arrow to other states (i.e., 2->{3,4})\nindicates agent 2 has identified agent 3 and 4's secrets.\nThese secret states have double circle/square shapes.";
        '''
    legend_end = '}'

    legend_keys = 'key [label=<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">'

    # First, add the full language
    legend_keys += '<tr><td>∑</td>'
    legend_keys += '<td>' + __make_event_list(events["all"]) + '</td></tr>'

    counter = 2

    # Now, add the observable languages
    for i in range(len(events["observable"])):
        legend_keys += '<tr><td>∑{o,' + str(i) + '}</td>'
        legend_keys += '<td>' + __make_event_list(events["observable"][i]) + '</td></tr>'
        counter += 1

    for i in range(len(events["controllable"])):
        legend_keys += '<tr><td>∑{c,' + str(i) + '}</td>'
        legend_keys += '<td>' + __make_event_list(events["controllable"][i]) + '</td></tr>'
        counter += 1

    legend_keys += '</table>>]'

    return legend_start + legend_keys + legend_end
