import unittest
import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
import json
from basic_ops.opacity import check_opacity


class TestOpacity(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            "tests/opacity/opacity_test_cases/opacity_test_1.in",
            "tests/opacity/opacity_test_cases/opacity_test_2.in",
            "tests/opacity/opacity_test_cases/opacity_test_3.in",
            "tests/opacity/opacity_test_cases/opacity_test_4.in"
        ]

        # First automaton for each test case
        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_opacity(self):
        """
        This ensures that all pre-built test cases work.
        """
        for i in range(len(self.automata)):
            # Get the answer
            ans = None
            with open(self.filenames[i][:-2] + "out") as f:
                ans = json.load(f)

            # Check if opaque
            result = check_opacity(self.automata[i])

            # Print
            # helper.pretty_print(result)
            # helper.pretty_print(ans)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(converter.convert_to_sets(result), converter.convert_to_sets(ans))
