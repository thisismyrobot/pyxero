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
        # The hook parses dates
        example_input = {
            'date': '/Date(1426849200000+1300)/',
        }

        self.assertEqual(
            xero.utils.json_load_object_hook(example_input),
            {
                'date': datetime.datetime(2015, 3, 21, 0, 0),
            }
        )

        # In both format styles
        example_input = {
            'date': '2015-04-29T00:00:00',
        }

        self.assertEqual(
            xero.utils.json_load_object_hook(example_input),
            {
                'date': datetime.date(2015, 4, 29)
            }
        )

    def test_parse_date(self):
        """ Tests of the parse_date input formats.
        """
        # 07/05/2015 00:00:00 +12 (06/05/2015 12:00:00 GMT/UTC)
        self.assertEqual(
            xero.utils.parse_date('/Date(1430913600000+1200)/'),
            datetime.datetime(2015, 5, 7, 0, 0)
        )

        # 16/09/2008 10:28:51.5 +12 (15/09/2008 22:25:51.5 GMT/UTC)
        self.assertEqual(
            xero.utils.parse_date('/Date(1221517731500+1200)/'),
            datetime.datetime(2008, 9, 16, 10, 28, 51, 500000)
        )

        # 10/08/2015 10:55:33 GMT/UTC
        self.assertEqual(
            xero.utils.parse_date('/Date(1439204133355)/'),
            datetime.datetime(2015, 8, 10, 10, 55, 33, 355000)
        )

        # 29/04/2015 00:00:00
        self.assertEqual(
            xero.utils.parse_date('2015-04-29T00:00:00'),
            datetime.date(2015, 4, 29)
        )

        # 29/04/2015 10:21:03
        self.assertEqual(
            xero.utils.parse_date('2015-04-29T10:21:03'),
            datetime.datetime(2015, 4, 29, 10, 21, 3)
        )

        # Not a date
        self.assertEqual(
            xero.utils.parse_date('not a date'),
            None
        )