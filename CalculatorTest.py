import unittest

from Calculator import Calculator


class CalculatorTest(unittest.TestCase):

    calculator = Calculator()

    def test_my_power_should_return_8_when_base_two_and_power_three(self):
        print 'Running the test\n'
        self.assertEquals(self.calculator.power(2, 3), 8)

    def test_my_power_should_return_256_when_base_four_and_power_four(self):
        print 'Running the test\n'
        self.assertEquals(self.calculator.power(4, 4), 256)