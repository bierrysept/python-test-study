import pytest
from src.calculator import Calculator
from typing import Union

@pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 0.5),
            (5, -1, -5)
        ]
        )
def test_divide(x: Union[int, float], y: Union[int, float], res: Union[int, float]):
    assert Calculator().divide(x, y) == res

@pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 3),
            (5, -1, 4)
        ]
        )
def test_add(x: Union[int, float], y: Union[int, float], res: Union[int, float]):
    assert Calculator().add(x, y) == res