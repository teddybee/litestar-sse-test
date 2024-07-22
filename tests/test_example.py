import sys
import unittest
import logging

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG


class TestExample(unittest.TestCase):  

    # def setUp(self):
    # runs before every testcase
    # logger.info("setup")
    
    def test_example(self):
        self.assertEqual('foo'.upper(), 'FOO')
        