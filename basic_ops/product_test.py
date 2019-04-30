import unittest
import helpers.convert_to_sets as converter
import helpers.string_helpers as helper
import json
from product import product

class TestProduct(unittest.TestCase):
    def setUp(self):
        filenames1 = [
            "test_files/product_tests/product_test_1a.in",
            "test_files/product_tests/product_test_2a.in"
        ]
        filenames2 = [
            "test_files/product_tests/product_test_1b.in",
            "test_files/product_tests/product_test_2b.in"
        ]

        # First automaton for each test case
        self.automata1 = [{}] * len(filenames1)
        for i in range(len(filenames1)):
            with open(filenames1[i]) as f:
                self.automata1[i] = json.load(f)

        # Second automaton for each test case
        self.automata2 = [{}] * len(filenames2)
        for i in range(len(filenames1)):
            with open(filenames2[i]) as f:
                self.automata2[i] = json.load(f)

    def test_product(self):
        '''
        This ensures that all pre-built test cases work.
        '''
        for i in range(len(self.automata1)):

            # Get the answer
            ans = None
            with open("test_files/product_tests/product_test_" + str(i + 1) + ".out") as f:
                ans = json.load(f)

            # Get the product of the appropriate automata
            result = product([self.automata1[i], self.automata2[i]])

            # Print
            # helper.pretty_print(result)
            # helper.pretty_print(ans)

            # Check answer, making sure it's OK if elements not in order
            self.assertEqual(converter.convert_to_sets(result), converter.convert_to_sets(ans))

if __name__ == "__main__":
    unittest.main()
