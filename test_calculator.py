import unittest

from calculator import add, subtract, multiply, divide, power, square_root


class AddTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_mixed_signs(self):
        self.assertEqual(add(-2, 5), 3)

    def test_zero(self):
        self.assertEqual(add(7, 0), 7)

    def test_float(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


class SubtractTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_result_negative(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_zero(self):
        self.assertEqual(subtract(7, 0), 7)

    def test_same_numbers(self):
        self.assertEqual(subtract(4, 4), 0)

    def test_float(self):
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)


class MultiplyTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_zero_mul(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_negative(self):
        self.assertEqual(multiply(-4, 5), -20)

    def test_two_negatives(self):
        self.assertEqual(multiply(-4, -5), 20)

    def test_float(self):
        self.assertAlmostEqual(multiply(0.5, 0.5), 0.25)


class DivideTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_fractional_result(self):
        self.assertEqual(divide(1, 4), 0.25)

    def test_negative(self):
        self.assertEqual(divide(-10, 2), -5.0)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0.0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_division_by_zero_message(self):
        with self.assertRaisesRegex(ValueError, "Деление на ноль"):
            divide(1, 0)


class PowerTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_first_power(self):
        self.assertEqual(power(7, 1), 7)

    def test_negative_exponent(self):
        self.assertEqual(power(2, -1), 0.5)

    def test_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_fractional_exponent(self):
        self.assertAlmostEqual(power(9, 0.5), 3.0)


class SquareRootTestCase(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(square_root(9), 3.0)

    def test_zero(self):
        self.assertEqual(square_root(0), 0.0)

    def test_one(self):
        self.assertEqual(square_root(1), 1.0)

    def test_non_perfect_square(self):
        self.assertAlmostEqual(square_root(2), 1.41421356, places=7)

    def test_float(self):
        self.assertAlmostEqual(square_root(0.25), 0.5)

    def test_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main()
