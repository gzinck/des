import unittest
import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
from structure_validation.automaton_validator import validate
import json
from communication.construct_communication_arena import construct_communication_arena


class TestConstructCommArena(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            "tests/communication/construct_comm_arena_test_cases/comm_test_1.in"
        ]

        # First automaton for each test case
        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_construct_arena(self):
        """
        This ensures that all pre-built test cases work.
        """
        for i in range(len(self.automata)):
            # Get the answer
            ans = None
            with open(self.filenames[i][:-3] + ".out") as f:
                ans = json.load(f)

            # Get the arena for the appropriate automaton
            result = construct_communication_arena(self.automata[i])
            validate(result)
            # Print
            # helper.pretty_print(result)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(converter.convert_to_sets(result), converter.convert_to_sets(ans))
