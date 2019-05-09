"""
This runs all tests for the program.
"""
import unittest

# Import the test cases to use
import tests.product.product_test as product
import tests.union.union_test as union
import tests.determinize.determinize_test as determinize
import tests.structure_validation.validator_test as validator

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add the tests
suite.addTests(loader.loadTestsFromModule(product))
suite.addTests(loader.loadTestsFromModule(union))
suite.addTests(loader.loadTestsFromModule(determinize))
suite.addTests(loader.loadTestsFromModule(validator))

# Initialize runner
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
