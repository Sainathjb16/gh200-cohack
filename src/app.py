"""
app.py — GH-200 CoHack Sample Application
A simple Python module used to demonstrate CI/CD with GitHub Actions.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def greet(name: str) -> str:
    """Return a personalised greeting string."""
    if not name or not name.strip():
        return "Hello, World!"
    return f"Hello, {name.strip()}! Welcome to GH-200 CoHack 🚀"


if __name__ == "__main__":
    print("🚀 GH-200 CoHack Sample App")
    print(f"   add(3, 4)       = {add(3, 4)}")
    print(f"   subtract(10, 6) = {subtract(10, 6)}")
    print(f"   multiply(5, 7)  = {multiply(5, 7)}")
    print(f"   greet('Himanshu') = {greet('Himanshu')}")
