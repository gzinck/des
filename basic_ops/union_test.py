import unittest
import helpers.convert_to_sets as converter
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

    def test_union_normal(self):
        '''
        This ensures that the first pre-built test case (two simple automata,
        multiple initial states) works.
        '''
        ans = None
        with open("test_files/union_test_1.out") as f:
            ans = json.load(f)
        result = union(self.automata)
        helper.pretty_print(result)
        helper.pretty_print(ans)
        self.assertEqual(converter.convert_to_sets(result), converter.convert_to_sets(ans))


if __name__ == "__main__":
    unittest.main()
