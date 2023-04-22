from unittest import TestCase, main

from test_edu.calculatore import calculate


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculate('3 + 2'), 5)

    def test_multi(self):
        self.assertEqual(calculate('3 * 2'), 6)

    def test_minus(self):
        self.assertEqual(calculate('3 - 2'), 1)

    def test_divide(self):
        self.assertEqual(calculate('6 / 2'), 3)


    def test_no_sign(self):
        with self.assertRaises(ValueError) as ex:
            calculate('some text')
        self.assertEqual('Выражение должно содержать один из арифмитических знаков: + - * /', ex.exception.args[0])

    def test_two_sign(self):
        with self.assertRaises(ValueError) as ex:
            calculate('2 + 2 + 2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', ex.exception.args[0])

    def test_many_sign(self):
        with self.assertRaises(ValueError) as ex:
            calculate('3 ** 2')

    def test_no_ints(self):
        with self.assertRaises(ValueError) as ex:
            calculate('2.5 * 5')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', ex.exception.args[0])

    def test_int_values(self):
        with self.assertRaises(TypeError) as ex:
            calculate(2 + 5)
        self.assertEqual("argument of type 'int' is not iterable", ex.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as ex:
            calculate('a * b')
        self.assertEqual(self.duplicate_assertion, ex.exception.args[0])

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError) as ex:
            calculate('2 / 0')
        self.assertEqual('division by zero', ex.exception.args[0])


if __name__ == '__main__':
    main()
