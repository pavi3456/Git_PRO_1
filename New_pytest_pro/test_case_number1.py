import pytest
import allure


@pytest.fixture()
@allure.step
def add_method(request):
    print("Start the add method")

    def last_execution():
        print("Execution successfully")
    request.addfinalizer(last_execution)


@pytest.fixture()
@allure.step
def giving_two_number():
    for i in range(1, 10):
        for j in range(1, i+1):
            return i, j


@allure.step
@allure.title("To verify the Behaviour Add method")
def test_auto_case_001(giving_two_number):
    print(giving_two_number)
    print("Application Start to compare the two  number")
    print("Actual value as %s and Expected value as %s" % (str(giving_two_number[0]), str(giving_two_number[1])))
    assert int(giving_two_number[0]) == int(giving_two_number[1])


@allure.step
@allure.title("To verify the Behaviour Add method while adding two values")
@pytest.mark.parametrize('param1,param2,expected', [(1, 2, 3)])
def test_auto_case_002(add_method, param1, param2, expected):
    assert param1+param2 == expected
    print("validate the condition"+str(param1+param2)+'=='+str(expected))
