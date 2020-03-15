import unittest
import basic_ops.helpers.convert_to_sets as converter
from structure_validation.automaton_validator import validate
import basic_ops.helpers.string_helpers as helper
import json
from asynchronous_communication.t1_add_comm import add_communication


class TestAddCommAnnotations(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            "tests/asynchronous_communication/test_cases/t1_test.in"
        ]

        self.agent = [
            1
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

            result = add_communication(self.automata[i], self.agent[i])
            validate(result)

            # Print
            # helper.pretty_print(result)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(converter.convert_to_sets(result),
                             converter.convert_to_sets(ans))