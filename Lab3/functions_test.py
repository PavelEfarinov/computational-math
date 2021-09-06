import random
import unittest

from Lab3.lab_functions import sign, bisection_method, secant_method


class LabFunctionsTests(unittest.TestCase):
    def test_sign(self):
        random_positive = random.randint(1, 1e10) / 1000
        random_negative = random.randint(-1e10, -1) / 1000

        self.assertEqual(sign(random_positive), sign(random_positive))
        self.assertEqual(sign(0), sign(0))
        self.assertEqual(sign(random_negative), sign(random_negative))
        self.assertNotEqual(sign(random_negative), sign(random_positive))
        self.assertNotEqual(sign(random_positive), sign(random_negative))
        self.assertNotEqual(sign(0), sign(random_negative))
        self.assertNotEqual(sign(0), sign(random_positive))

    def test_bisection(self):
        def x(x: float):
            return x

        def x_2(x: float):
            return (x ** 2) - 1

        def d_x(x: float):
            return 1 / x

        epsilon = 1e-6
        self.assertAlmostEqual(bisection_method(-1, 1, x, epsilon)[1], 0, delta=epsilon)
        self.assertAlmostEqual(bisection_method(0, 1.5, x_2, epsilon)[1], 0, delta=epsilon)

        self.assertNotAlmostEqual(bisection_method(1, 2, d_x, epsilon)[1], 0, delta=epsilon)

    def test_scant(self):
        def x(x: float):
            return x

        def x_2(x: float):
            return x ** 2 - 1

        def d_x(x: float):
            return 1 / x

        epsilon = 1e-6
        self.assertAlmostEqual(secant_method(-1, 1, x, epsilon)[1], 0, delta=epsilon)
        self.assertAlmostEqual(secant_method(5, 7, x_2, epsilon)[1], 0, delta=epsilon)
        self.assertAlmostEqual(secant_method(0.01, 1, d_x, epsilon)[1], 0, delta=epsilon)


if __name__ == '__main__':
    unittest.main()
