import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctle(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctle(self):
        assert self.calc.division(self, 12, 2) == 6

    def test_subtraction_calculate_correctle(self):
        assert self.calc.subtraction(self, 14, 6) == 8

    def test_adding_calculate_correctle(self):
        assert self.calc.adding(self, 3, 4) == 7








