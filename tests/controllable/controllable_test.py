import unittest
import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
import json
from basic_ops.controllable import get_controllable


class TestControllable(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            "tests/controllable/controllable_test_cases/controllable_test_1.in"
        ]

        # First automaton for each test case
        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_controllable(self):
        """
        This ensures that all pre-built test cases work.
        """
        for i in range(len(self.automata)):
            # Get the answer
            ans = None
            with open(self.filenames[i][:-3] + ".out") as f:
                ans = json.load(f)

            # Get the arena for the appropriate automaton
            result = get_controllable(self.automata[i])

            # Print
            # helper.pretty_print(result["states"]["bad"])
            helper.pretty_print(result)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(converter.convert_to_sets(result), converter.convert_to_sets(ans))
