#!/usr/bin/env python3
"""
first unit test for utils.access_nested_map.
"""
from multiprocessing import context
from typing import Dict, Tuple
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized 
from utils import access_nested_map, get_json

class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for access_nested_map utility
    function in the utilities module.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        actual_result = access_nested_map(nested_map, path)
        self.assertEqual(actual_result, expected_result)
    
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
    ) -> None:
        """Tests exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
            
    class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
    ) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)

if __name__ == "__main__":
    unittest.main()
        