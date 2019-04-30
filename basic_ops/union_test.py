import unittest
import test_files.verify as verifier
import test_files.convert_to_sets as converter
import helpers.string_helpers as helper
import json
from union import union

class TestUnion(unittest.TestCase):
    def setUp(self):
        filenames = ["test_files/union_test_1a.in", "test_files/union_test_1b.in"]
        self.automata = [{}] * len(filenames)
        for i in range(len(filenames)):
            with open(filenames[i]) as f:
                self.automata[i] = json.load(f)

    def test_states(self):
        ans = None
        with open("test_files/union_test_1.out") as f:
            ans = json.load(f)
        print(ans)
        result = union(self.automata)
        self.assertEqual(converter.convert_to_sets(result), converter.convert_to_sets(ans))
        # self.assertTrue(verifier.verify(result, ans))
        helper.pretty_print(result)


if __name__ == "__main__":
    unittest.main()
