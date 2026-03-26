"""
test_app.py — Pytest tests for app.py
Used by the GitHub Actions matrix test job.
"""

import pytest
from app import add, subtract, multiply, greet


class TestAdd:
    def test_positive_numbers(self):
        assert add(3, 4) == 7

    def test_negative_numbers(self):
        assert add(-2, -5) == -7

    def test_mixed_numbers(self):
        assert add(-3, 10) == 7

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 10) == -7

    def test_zero(self):
        assert subtract(5, 5) == 0


class TestMultiply:
    def test_positive(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(100, 0) == 0

    def test_negative(self):
        assert multiply(-2, 5) == -10

    def test_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestGreet:
    def test_normal_name(self):
        result = greet("Himanshu")
        assert "Himanshu" in result
        assert "Welcome" in result

    def test_empty_name(self):
        assert greet("") == "Hello, World!"

    def test_whitespace_name(self):
        assert greet("   ") == "Hello, World!"

    def test_name_with_spaces(self):
        result = greet("  Himanshu  ")
        assert "Himanshu" in result

    def test_emoji_in_result(self):
        result = greet("CoHack")
        assert "🚀" in result
