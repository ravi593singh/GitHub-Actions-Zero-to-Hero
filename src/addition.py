# app.py
# This is a test commit
# First ci workflows
# addition functionality
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
