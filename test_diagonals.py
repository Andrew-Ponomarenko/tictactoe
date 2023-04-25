import pytest

from main import check_diagonals,game_board


@pytest.fixture
def testboard():
    return ["X", "-", "O",
            "-", "X", "-",
            "-", "-", "X"]
@pytest.main()
def test_construction(testboard):
    game_board == testboard
    check_diagonals()
    assert game_still_on == False