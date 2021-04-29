#!/usr/bin/env python

import unittest

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def minus(a, b):
    return a - b

def modulo(a, b):
    # Intentional bug.
    if a == 4:
        return 0
    return a % b
