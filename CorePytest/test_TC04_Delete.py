import pytest

@pytest.mark.smoke
def test_tc10_login():
    print("This is my tenth test case")

@pytest.mark.sanity
def test_tc11_logout():
    print("This is my eleventh test case")

@pytest.mark.sanity
def test_tc12_create():
    print("This is my twelfth test case")