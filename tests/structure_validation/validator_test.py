import unittest
from structure_validation.automaton_validator import validate
import json


class TestAutomatonValidation(unittest.TestCase):
    def setUp(self):
        filenames_good = [
            "tests/product/product_test_cases/product_test_1a.in",
            "tests/product/product_test_cases/product_test_1b.in",
            "tests/product/product_test_cases/product_test_2a.in",
            "tests/product/product_test_cases/product_test_2b.in"
        ]

        filenames_bad = [
            "tests/structure_validation/structure_validation_test_cases/structure_validation_1.in",
            "tests/structure_validation/structure_validation_test_cases/structure_validation_2.in",
            "tests/structure_validation/structure_validation_test_cases/structure_validation_3.in",
            "tests/structure_validation/structure_validation_test_cases/structure_validation_4.in",
        ]

        # First automaton for each test case
        self.automata_good = [{}] * len(filenames_good)
        for i in range(len(filenames_good)):
            with open(filenames_good[i]) as f:
                self.automata_good[i] = json.load(f)

        # Second automaton for each test case
        self.automata_bad = [{}] * len(filenames_bad)
        for i in range(len(filenames_bad)):
            with open(filenames_bad[i]) as f:
                self.automata_bad[i] = json.load(f)

    def test_product(self):
        '''
        This ensures that all pre-built test cases work.
        '''
        # Good ones should return true
        for a in self.automata_good:
            self.assertTrue(validate(a))
        # Bad ones should give exceptions
        for a in self.automata_bad:
            with self.assertRaises(Exception):
                validate(a)
