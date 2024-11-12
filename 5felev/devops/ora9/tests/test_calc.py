import unittest
from calculator.calc import Calculator

NUMBER_1 = 3.0
NUMBER_2 = 2.0
FAILURE_MSG = "INCORRECT RESULT"

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0.0, FAILURE_MSG)

    def test_add(self):
        value = self.calc.add(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 5.0, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)
    
    def test_subtract(self):
        value = self.calc.subtract(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.0, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)
    
    def test_subtract_negative(self):
        value = self.calc.subtract(NUMBER_2, NUMBER_1)
        self.assertEqual(value, -1.0, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)
    
    def test_multiply(self):
        value = self.calc.multiply(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 6.0, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)
    
    def test_divide(self):
        value = self.calc.divide(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.5, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, NUMBER_1, 0)

    def test_minimum_lesser(self):
        value = self.calc.minimum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)
    
    def test_minimum_greater(self):
        value = self.calc.minimum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)

    def test_minimum_equal(self):
        value = self.calc.minimum(NUMBER_1, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)

    def test_maximum_greater(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_1, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)

    def test_maximum_lesser(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_1, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)

    def test_max_equals(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE_MSG)
        self.assertEqual(value, self.calc.last_answer, FAILURE_MSG)

if __name__ == '__main__':
    import xmlrunner

    testRunner = unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'), 
    failfast=False, 
    buffer=False, 
    catchbreak=False)