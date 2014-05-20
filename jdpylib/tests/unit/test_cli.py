import unittest

import sys

from jdpylib import cli




class TestCLIErrors(unittest.TestCase):

    def setUp(self):
        pass

    def test_error_invalid_usage_exits_with_error_code(self):
        with self.assertRaises(SystemExit) as ctx:
            cli.error_invalid_usage()
        self.assertEqual(ctx.exception.code, 1, "Did not receive an exit status of 1")






