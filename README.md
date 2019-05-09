# DESwiz

DESwiz is a discrete event system tool for working with finite state automata
and other systems. It has been designed as proof-of-concept for academic works
in theoretical computer science developed at Inria (Rennes, France) and Mount
Allison University (Sackville, Canada).

## Current Features

- Composing two automata with union and product operations
- Determinizing an automaton
- Verifying the JSON for an automaton to ensure it is a valid automaton, based on
the specification [here](https://github.com/gzinck/des/wiki/Input-Specification).
- Creation of an arena, as per *Leaking Secrets* (Ricker, Marchand, \&
Keroglou, 2019).

## Upcoming Features

- An interface to allow the user to work with the software. In its current state,
it only runs tests using python's unittest module, pulling in automata from JSON
files.

## Input Specification

Input for the program must be specified correctly in a text file, which is then passed into the program. For information on how to create the text file, see https://github.com/gzinck/des/wiki/Input-Specification
