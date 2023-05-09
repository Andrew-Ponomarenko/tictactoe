import pytest
import mock


from functions import check_diagonals, check_columns, check_rows, play_game


@pytest.fixture
def testboard1():
    return ["X", "O", "O",
            "X", "X", "O",
            "X", "O", "X"]
@pytest.fixture
def testboard2():
    return ["O", "O", "O",
            "X", "O", "X",
            "O", "X", "X"]
@pytest.fixture
def emptyboard():
    return ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
def test_diagonals(testboard1):
    assert check_diagonals(testboard1) == (True,"X")
def test_columns(testboard1):
    assert check_columns(testboard1) == (True,"X")

def test_rows(testboard2):
    assert check_rows(testboard2) == (True,"O")
def test_diagonals2(testboard2):
    assert check_diagonals(testboard2) == (True,"O")

inputs = iter(['1','2','3','4','5','6','7','8'])
def test_full_game(monkeypatch,emptyboard):
    monkeypatch.setattr('builtins.input',lambda name: next(inputs))

    assert play_game(emptyboard,"X") == True

