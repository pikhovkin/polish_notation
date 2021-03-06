﻿#This file was originally generated by PyScripter's unitest wizard

import unittest
from polish_notation import compute_polish_notation, CorrectExpressionError

class TestGlobalFunctions(unittest.TestCase):

    def test_compute_polish_notation_float(self):
        s = '5.0 8 3 + /'
        self.assertIsInstance(compute_polish_notation(s), float)

    def test_compute_polish_notation_as_integer(self):
        s = '5 8 3 + *'
        self.assertIsInstance(compute_polish_notation(s), int)

    def test_operator_is_first(self):
        s = '+ 2 2 *'
        self.assertRaises(CorrectExpressionError, compute_polish_notation, s)

    def test_positive_element(self):
        s = '+2 2 *'
        self.assertEqual(compute_polish_notation(s), 4)

    def test_first_negative_element(self):
        s = '-2 2 *'
        self.assertEqual(compute_polish_notation(s), -4)

    def test_two_negative_element_in_expression(self):
        s = '-2 2 + -1 +'
        self.assertEqual(compute_polish_notation(s), -1)

    def test_string_in_expression(self):
        s = '2 2 + s +'
        self.assertRaises(CorrectExpressionError, compute_polish_notation, s)

    def test_too_many_terms(self):
        s = '2 2 2 -'
        self.assertRaises(CorrectExpressionError, compute_polish_notation, s)

    def test_too_few_terms(self):
        s = '2 2 - -'
        self.assertRaises(CorrectExpressionError, compute_polish_notation, s)

    def test_zero_division_error(self):
        s = '0 2 /'
        self.assertRaises(ZeroDivisionError, compute_polish_notation, s)

if __name__ == '__main__':
    unittest.main()
