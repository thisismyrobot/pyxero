""" Tests of the utils module.
"""
try:
    # Try importing from unittest2 first. This is primarily for Py2.6 support.
    import unittest2 as unittest
except ImportError:
    import unittest

import datetime
import xero.utils


class UtilsTest(unittest.TestCase):
    """ Test of the utils module.
    """
    def test_json_hook(self):
        """ Tests the json hook used in Manager._parse_api_response, and the
            call it makes to parse_date.
        """
        example_input = {
            'data': {
                'Status': 'OK',
            },
        }

        self.assertEqual(
            xero.utils.json_load_object_hook(example_input),
            example_input
        )

        # The hook parses dates
        example_input = {
            'data': {
                'Status': 'OK',
            },
            'date': '/Date(1426849200000+1300)/',
        }

        excepted_output = {
            'data': {
                'Status': 'OK',
            },
            'date': datetime.datetime(2015, 3, 21, 0, 0),
        }

        self.assertEqual(
            xero.utils.json_load_object_hook(example_input),
            excepted_output
        )
