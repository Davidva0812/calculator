import unittest
import coverage
from calculator import (press, equation, clear, equal, backspace,square_root,
                        toggle_theme, window)


class TestCalculatorLogic(unittest.TestCase):
    def test_press(self):
        equation.set("")
        press("1")
        press("+")
        press("2")
        self.assertEqual(equation.get(), "1+2")

    def test_clear(self):
        equation.set("456+123")
        clear()
        self.assertEqual(equation.get(), "")

    def test_backspace(self):
        equation.set("1")
        backspace()
        self.assertEqual(equation.get(), "")

    def test_toggle_theme(self):
        original_theme = window.cget("bg")

        # test for if block
        toggle_theme()
        new_theme = window.cget("bg")
        self.assertNotEqual(original_theme, new_theme)

        # test for else block
        toggle_theme()
        back_to_original = window.cget("bg")
        self.assertEqual(original_theme, back_to_original)


class TestEqualFunction(unittest.TestCase):
    def test_addition(self):
        equation.set("2+3")
        equal()
        self.assertEqual(equation.get(), "5")

    def test_subtraction(self):
        equation.set("5-3")
        equal()
        self.assertEqual(equation.get(), "2")

    def test_multiplication(self):
        equation.set("4*5")
        equal()
        self.assertEqual(equation.get(), "20")

    def test_power_operator(self):
        equation.set("2^3")
        equal()
        self.assertEqual(equation.get(), "8")

    def test_zero_division(self):
        equation.set("1/0")
        equal()
        self.assertTrue(equation.get().startswith("Error:"))

    def test_unknown_error(self):
        equation.set("undefined")
        equal()
        self.assertTrue("Error" in equation.get())

    def test_float_result(self):
        equation.set("5/2")
        equal()
        self.assertEqual(equation.get(), "2.50")


class TestSquareRootFunction(unittest.TestCase):
    def test_square_root_positive(self):
        equation.set("9")
        square_root()
        self.assertEqual(equation.get(), "3.00")

    def test_square_root_negative(self):
        equation.set("-4")
        square_root()
        self.assertEqual(equation.get(), "Error: Negative number")

    def test_invalid_input(self):
        equation.set("abc")
        square_root()
        self.assertEqual(equation.get(), "Error: Invalid input")


# Launch Code Coverage
cov = coverage.Coverage()
cov.start()

# Run tests
loader = unittest.TestLoader()
suite = loader.discover(start_dir=".")  # Folder of test file
runner = unittest.TextTestRunner()
runner.run(suite)

# Stop and Generate report
cov.stop()
cov.save()

# Print result
cov.report()
cov.html_report(directory="coverage_report")  # Generate HTML report
