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
    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()
        