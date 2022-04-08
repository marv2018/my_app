import pytest
from src.my_app.resources.my_data import MyDataClass
from src.my_app.meta_info import __app_name__

@pytest.mark.parametrize("val", ["Ben", "Alice"])
def test_sample(val):
    my = MyDataClass()
    assert my.employee == val


def test_sample2():
    my = MyDataClass()
    assert __app_name__ == "My App2"
