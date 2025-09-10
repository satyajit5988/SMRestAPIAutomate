import pytest

@pytest.fixture(scope="module")
def fixture_demo():
    print("This is our fixture code to be implemented before the testcases")
    print("---------------------------------------------------------------")
    yield
    print("This is our fixture code to be implemented after the testcases")
    print("---------------------------------------------------------------")


@pytest.mark.smoke
@pytest.mark.sanity
def test_tc07_login(fixture_demo):
    print("This is my sevent test case")

@pytest.mark.smoke
def test_tc08_logout(fixture_demo):
    print("This is my eight test case")

@pytest.mark.smoke
def test_tc09_create(fixture_demo):
    print("This is my ninth test case")