# DESwiz

DESwiz is a discrete event system tool for working with finite state automata
and other systems. It has been designed as proof-of-concept for academic works
in theoretical computer science developed at Inria (Rennes, France) and Mount
Allison University (Sackville, Canada).

## Current Features

- Composing two automata with union and product operations

## Upcoming Features

- Checking to make sure that every time a user gives an automaton, it is
formatted appropriately

## Input Specification

An automaton should be passed to DESwiz using standard JSON format, which is
read in by standard python functions. Below is an example of the precise format
required, where lines starting with '//' are comments and should not be part of
the final specification.

Note that the states `q1, q2, q3` and events `a, b, c` are placeholders.

```
{
  // Firstly, describe the states in the automaton
  "states": {

    // All of the states
    "all": ["q1", "q2", "q3"],

    // Initial state(s)
    "initial": ["q1"],

    // Define which are marked, which is used as a secret state for opacity
    // problems.
    "marked": ["q1"],

    // Define which are bad, if any
    "bad": ["q1"]
  },

  // Secondly, describe the alphabet of events
  "events": {

    // Within this, we list all events defined (does not include epsilon by
    //   default)
    "all": ["a", "b", "c"],

    // Define which are controllable (must be a subset of "all")
    // This is a list of lists, with one entry for each player in the system
    "controllable": [
      ["a", "b"]
    ],

    // Define which are observable (must be a subset of "all")
    // This is a list of lists, with one entry for each player in the system
    "observable": [
      ["a", "b", "c"]
    ],

    "attacker": ["a", "b"]
  },

  // Thirdly, describe the transitions function delta
  "transitions": {

    // List all of the transitions
    "all": {
			"q1->a": ["q2"], // Indicates q1 has an a transition to q2
			"q2->a": ["q3", "q4"] // Multiple states indicates nondeterminism
		},

    // Define which are bad, if any
    "bad": {
			"q1->a": ["q2"]
		}
  }
}
```

Note that the above **must be valid JSON** for the code to run properly. If you
want to verify your JSON, try using https://jsonlint.com/.
