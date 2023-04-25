import pytest

from functions import check_diagonals,game_still_on


@pytest.fixture
def testboard():
    return ["X", "-", "O",
            "-", "X", "-",
            "-", "-", "X"]


def test_diagonals(testboard):
    assert check_diagonals(testboard) == "X"