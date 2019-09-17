import unittest
import basic_ops.helpers.convert_to_sets as converter
import basic_ops.helpers.string_helpers as helper
import json
from modular_opacity.modular_opacity_verification import check_modular_opacity
from structure_validation.automaton_validator import validate
from modular_opacity.heuristics import most_shared_heuristic, least_new_heuristic

class TestModularOpacity(unittest.TestCase):
    def setUp(self):
        self.filenames = [
            # Test case that doesn't work, from paper
            "tests/opacity/modular_opacity_test_cases/modular_test_1-1.in",
            "tests/opacity/modular_opacity_test_cases/modular_test_1-2.in",
            # Test case that DOES work
            "tests/opacity/modular_opacity_test_cases/modular_test_2-1.in",
            "tests/opacity/modular_opacity_test_cases/modular_test_2-2.in"
        ]
        self.answers = [False, True]

        # First automaton for each test case
        self.automata = [{}] * len(self.filenames)
        for i in range(len(self.filenames)):
            with open(self.filenames[i]) as f:
                self.automata[i] = json.load(f)
                validate(self.automata[i])

    def test_modular_opacity(self):
        """
        This ensures that all pre-built test cases work.
        """
        for i in range(len(self.automata) // 2):
            # Check if opaque
            result = check_modular_opacity([self.automata[2*i], self.automata[2*i+1]])
            self.assertEqual(result, self.answers[i])
            result = check_modular_opacity([self.automata[2*i], self.automata[2*i+1]], heuristic = most_shared_heuristic)
            self.assertEqual(result, self.answers[i])
            result = check_modular_opacity([self.automata[2*i], self.automata[2*i+1]], heuristic = least_new_heuristic)
            self.assertEqual(result, self.answers[i])
