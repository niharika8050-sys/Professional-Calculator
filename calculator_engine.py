"""
------------------------------------------------------------
Professional Calculator - Calculation Engine
------------------------------------------------------------
This module contains all mathematical operations.
No user interaction should happen here.
------------------------------------------------------------
"""

import math


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def modulus(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus with zero.")
    return a % b


def power(a: float, b: float) -> float:
    return a ** b


def square_root(number: float) -> float:
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


def floor_division(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a // b


def percentage(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Percentage calculation cannot divide by zero.")
    return (a / b) * 100