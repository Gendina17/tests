import pytest

def test_first_str(): # негативный тест на строку
    str = "aaa"
    try:
        assert str[5] == a
    except IndexError:
        pass

@pytest.mark.parametrize("test_input,expected", [("    fff ", "fff"), ("eee", "eee"), ("tt    ", "ttt")])
def test_second_str()
    assert test_input.strip == expected    # параметризованный тест

def test_third_str()
    assert '1<>2<>3'.split ('<>') == ['1', '2', '3']



def test_first_dict(): # негативный тест на строку
    d = {1: 2, 2: 4, 3: 9}
    try:
        assert d['1'] == 2
    except KeyError:
        pass

@pytest.mark.parametrize("test_input,expected", [({1: 2, 2: 4, 3: 9}, (1, 2)), ({'1': 'aaa', '2': 'bbb', '3': 'ccc'}, ('3', 'ccc'))])
def test_second_dict()
    assert test_input.popitem() == expected    # параметризованный тест

def test_third_dict(dict)
    assert dict.clear() == None
