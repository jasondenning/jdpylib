import unittest
import json
from collections import OrderedDict


from jdpylib import parser, errors

class TestParser(unittest.TestCase):

    def setUp(self):
        self.valid_yaml = """
key1: value1
key2: value2
list1:
  - item1a
  - item1b
"""
        self.invalid_yaml = """
this isn't YAML-- is it?
If it were:: <- this would be invalid
"""

    def test_yaml_to_json_outputs_valid_json(self):
        output_json = parser.yaml_to_json(self.valid_yaml)
        output_arr = json.loads(output_json)
        self.assert_('key1' in output_arr.keys())
        self.assertEquals(['item1a', 'item1b'], output_arr['list1'])


    def test_yaml_to_json_raises_exception_on_invalid_yaml(self):
        with self.assertRaises(Exception):
            output = parser.yaml_to_json(self.invalid_yaml)

    def test_yaml_to_json_raises_InvalidYAML_exception_on_invalid_yaml(self):
        with self.assertRaises(errors.InvalidYAML):
            output = parser.yaml_to_json(self.invalid_yaml)


    def test_load_yaml_ordered_returns_OrderedDict(self):
        output = parser.load_yaml_ordered(self.valid_yaml)
        self.assert_(isinstance(output, OrderedDict))

    def test_load_yaml_ordered_maintains_order(self):
        output = parser.load_yaml_ordered(self.valid_yaml)
        keys = output.keys()
        expected = ['key1', 'key2', 'list1']
        self.assertEqual(keys, expected,
            "Expected output.keys to be list like:\n %s, but got:\n %s" %
            (expected, keys))

    def test_yaml_to_json_preserves_order(self):
        expected_json='{"key1": "value1", "key2": "value2", "list1": ["item1a", "item1b"]}'
        output = parser.yaml_to_json(self.valid_yaml)
        self.assertEqual(output,
                         expected_json,
                         "Expected %s - got %s"% (expected_json, output))

