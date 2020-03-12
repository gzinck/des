import unittest
import basic_ops.helpers.convert_to_sets as converter
from structure_validation.automaton_validator import validate
import basic_ops.helpers.string_helpers as helper
import json
from asynchronous_communication.add_clock_ticks import add_clock_ticks


class TestAddClockTicks(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            "tests/asynchronous_communication/test_cases/t0_test.in"
        ]

        self.delta = [
            2
        ]

        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_add_clock_ticks(self):
        for i in range(len(self.automata)):
            ans = None
            with open(self.filenames[i][:-3] + ".out") as f:
                ans = json.load(f)

            result = add_clock_ticks(self.automata[i], self.delta[i])
            validate(result)

            # Print
            # helper.pretty_print(result)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(converter.convert_to_sets(result),
                             converter.convert_to_sets(ans))