"""
This runs all tests for the program.
"""
import unittest

# Import the test cases to use
import tests.product.product_test as product
import tests.union.union_test as union
import tests.accessible.accessible_test as accessible
import tests.coaccessible.coaccessible_test as coaccessible
import tests.controllable.controllable_test as controllable
import tests.determinize.determinize_test as determinize
import tests.opacity.opacity_test as opacity
import tests.opacity.modular_opacity_test as modular_opacity
import tests.structure_validation.validator_test as validator
import tests.leaking_secrets_arenas.contruct_arena_test as const_arena
import tests.leaking_secrets_arenas.construct_attractor_test as const_attr
import tests.synchronous_communication.construct_comm_arena_test as const_comm
import tests.asynchronous_communication.t0_test as t0
import tests.asynchronous_communication.t1_test as t1

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add the tests
suite.addTests(loader.loadTestsFromModule(product))
suite.addTests(loader.loadTestsFromModule(union))
suite.addTests(loader.loadTestsFromModule(accessible))
suite.addTests(loader.loadTestsFromModule(coaccessible))
suite.addTests(loader.loadTestsFromModule(controllable))
suite.addTests(loader.loadTestsFromModule(determinize))
suite.addTests(loader.loadTestsFromModule(opacity))
suite.addTests(loader.loadTestsFromModule(modular_opacity))
suite.addTests(loader.loadTestsFromModule(validator))
suite.addTests(loader.loadTestsFromModule(const_arena))
suite.addTests(loader.loadTestsFromModule(const_attr))
suite.addTests(loader.loadTestsFromModule(const_comm))
suite.addTests(loader.loadTestsFromModule(t0))
suite.addTests(loader.loadTestsFromModule(t1))

# Initialize runner
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
