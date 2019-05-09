import unittest
import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
import json
from basic_ops.determinize import determinize


class TestProduct(unittest.TestCase):
    def setUp(self):
        filenames = [
            "tests/determinize/determinize_test_cases/determinize_test_1.in"
        ]

        # First automaton for each test case
        self.automata = [{}] * len(filenames)
        for i in range(len(filenames)):
            with open(filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_determinize(self):
        '''
        This ensures that all pre-built test cases work.
        '''
        for i in range(len(self.automata)):
            # Get the answer
            ans = None
            with open("tests/determinize/determinize_test_cases/determinize_test_" + str(i + 1) + ".out") as f:
                ans = json.load(f)

            # Get the product of the appropriate automata
            result = determinize(self.automata[i])

            # Print
            # helper.pretty_print(result)
            # helper.pretty_print(ans)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(converter.convert_to_sets(result), converter.convert_to_sets(ans))
