import pytest

from main import *


@pytest.fixture
def testboard():
    return ["X", "-", "O",
            "-", "X", "-",
            "-", "-", "X"]
def test_construction(testboard):
    game_board == testboard
    check_diagonals()
    assert game_still_on == False