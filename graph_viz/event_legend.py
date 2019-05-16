def generate_event_legend(events):
    legend_start = '''
        rankdir=LR
        node [shape=plaintext]
        subgraph cluster_01 {
            label = "Legend";
            key [label=<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">
                <tr><td align="right" port="i1">item 1</td></tr>
                <tr><td align="right" port="i2">item 2</td></tr>
                <tr><td align="right" port="i3">item 3</td></tr>
                <tr><td align="right" port="i4">item 4</td></tr>
                </table>>]
            key2 [label=<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">
                <tr><td port="i1">&nbsp;</td></tr>
                <tr><td port="i2">&nbsp;</td></tr>
                <tr><td port="i3">&nbsp;</td></tr>
                <tr><td port="i4">&nbsp;</td></tr>
                </table>>]
        '''
    legend_end = '}'

    legend_keys = 'key [label=<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">'
    legend_vals = 'key2 [label=<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">'

    # First, add the full language
    legend_keys += '<tr><td align="right" port="i1">∑</td></tr>'
    legend_vals += '<tr><td port="i1">' + str(events["all"]) + '</td></tr>'

    counter = 2

    # Now, add the observable languages
    for i in range(len(events["observable"])):
        legend_keys += '<tr><td align="right" port="i' + str(counter) + '">∑_{o,' + str(i) + '}</td></tr>'
        legend_vals += '<tr><td port="i' + str(counter) + '">' + str(events["observable"][i]) + '</td></tr>'
        counter += 1

    for i in range(len(events["controllable"])):
        legend_keys += '<tr><td align="right" port="i' + str(counter) + '">∑_{o,' + str(i) + '}</td></tr>'
        legend_vals += '<tr><td port="i' + str(counter) + '">' + str(events["controllable"][i]) + '</td></tr>'
        counter += 1

    legend_keys += '</table>>]'
    legend_vals += '</table>>]'

    return legend_start + legend_keys + legend_vals + legend_end
