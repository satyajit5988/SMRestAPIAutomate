import pytest

a=5

#@pytest.mark.skipif(a>6, reason="Skipping condition met")
def test_tc01_login():
    print("This is my first test case")
    assert a != 5, "These two values of a must not be same"

#@pytest.mark.skip("Not a part of current testing scope")
def test_tc02_logout():
    print("This is my second test case")

#@pytest.mark.skipif(a>4, reason="Skipping condition met")
def test_tc03_create():
    print("This is my third test case")