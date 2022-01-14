import unittest

from jsondiff import diff

from src.utils import logger


class AssertUtil(unittest.TestCase):

    @staticmethod
    def true(expected_value, message: str = ''):
        logger.debug('Assertion %s is true' % expected_value)
        AssertUtil.assertTrue(expected_value, message)

    @staticmethod
    def false(expected_value, message: str = ''):
        logger.info('Assertion %s is false' % expected_value)
        AssertUtil.assertFalse(expected_value, message)

    @staticmethod
    def equal(expected_value, actual_value, message: str):
        logger.info('Assertion Equal: %s' % expected_value)
        mess = """
                \t%s
                \tExpect: '%s'
                \tActual: '%s'""" % (message, expected_value, actual_value)
        AssertUtil.assertEqual(expected_value, actual_value, mess)

    @staticmethod
    def not_equal(expected_value, actual_value, message: str):
        log = "%s is not '%s'" % (message, expected_value)
        mess = """ 
                \t%s
                \tExpect: '%s'
                \tActual: '%s' """ % (log, expected_value, actual_value)
        AssertUtil.assertNotEqual(expected_value, actual_value, mess)

    @staticmethod
    def contain(expected_value, actual_value: str, message: str = ''):
        result = expected_value in actual_value
        mess = """
                \tExpect: %s would contain
                \tActual: %s""" % (expected_value, actual_value)
        AssertUtil.true(result, mess)

    @staticmethod
    def equal_json(expected_value: str, actual_value: str):
        result = diff(expected_value, actual_value)
        mess = """
                \tExpected: %s
                \tActual: %s
                \tDiff: %s
        """ % (expected_value, actual_value, result)
        AssertUtil.true(0 == len(result), mess)
