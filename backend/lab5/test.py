import unittest
from calculator import Calculator

class TDDinCalculator(unittest.TestCase):

	def test_calculator_add(self):
		self.calc = Calculator()

		result = self.calc.add(2,3)

		self.assertEqual(5, result)

	def test_calculator_add_strings(self):
		self.calc = Calculator()
		self.assertRaises(ValueError, self.calc.add, 'two', 'three')

	def test_calculator_add_strings_one(self):
		self.calc = Calculator()
		self.assertRaises(ValueError, self.calc.add, 2, 't')


