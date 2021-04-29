#!/usr/bin/env python
import calc
import unittest




class TestCalc(unittest.TestCase):

    def test_add1(self):
        self.assertEqual(calc.add(1, 2), 1 + 2)
        
    def test_add2(self):
        self.assertEqual(calc.add(0, 0), 0 + 0)
        
    def test_add3(self):
        self.assertEqual(calc.add(1000, -1414), 1000 + -1414)

    def test_mult1(self):
        self.assertEqual(calc.mult(5, 8), 5 * 8)

    def test_mult2(self):
        self.assertEqual(calc.mult(0, 8), 0)

    def test_mult3(self):
        self.assertEqual(calc.mult(10, 10), 100)

    def test_div1(self):
        self.assertEqual(calc.div(5, 8), 5 / 8)

    def test_div2(self):
        self.assertEqual(calc.div(100, 10), 10)
    # Fail test.    
    def test_div3(self):
        self.assertEqual(calc.div(1, 0), 0)

    def test_minus1(self):
        self.assertEqual(calc.minus(1, 1), 0)

    def test_minus2(self):
        self.assertEqual(calc.minus(0, 1), -1)

    def test_minus3(self):
        self.assertEqual(calc.minus(1, 0), 1)

    def test_modulo1(self):
        self.assertEqual(calc.modulo(1, 1), 1 % 1)
    # Fail test.    
    def test_modulo2(self):
        self.assertEqual(calc.div(12, 2), 12 % 2)
    # Fail test.    
    def test_modulo3(self):
        self.assertEqual(calc.div(4, 2), 0)
        
if __name__ == '__main__':
    unittest.main()
