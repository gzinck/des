# DESwiz

DESwiz is a discrete event system tool for working with finite state automata
and other systems. It has been designed as proof-of-concept for academic works
in theoretical computer science developed at Inria (Rennes, France) and Mount
Allison University (Sackville, Canada).

## Getting Started

Before using the application: 
- Make sure you have **Python 3.7** installed, as well as tkinter (which is typically bundled with python)
- If you want to visualize the graphs, the following is also necessary:
  - Install the graphviz python module using `pip install graphviz`
  - Install the graphviz application from https://www.graphviz.org/ and add the graphviz's bin to your PATH (for instance, on windows make sure `C:/Program Files (x86)/Graphviz2.38/bin/` is in your PATH)
    - For mac users with Homebrew installed https://brew.sh/, simply do `brew install graphviz` to install it with all dependencies

Run the application in the main directory as follows:

```
python3 main.py
```

Follow the on-screen instructions to interact with the command-line interface. Note that you will need input automata to provide the application—these should all be in separate files which you will need to load into the application after launch.

### Input Specification

Input for the program must be specified correctly in a text file, which is then passed into the program. For information on how to create the text file, see https://github.com/gzinck/des/wiki/Input-Specification

## Current Features

- Composing two automata with union and product operations
- Determinizing an automaton
- Verifying the JSON for an automaton to ensure it is a valid automaton, based on
the specification [here](https://github.com/gzinck/des/wiki/Input-Specification).
- Creation of an arena, as per *Leaking Secrets* (Ricker, Marchand, \&
Keroglou, 2019).
- An interface to allow the user to work with the software.

## Upcoming Features

- Performing the supervisory control algorithm on an arena with pre-defined bad states.
