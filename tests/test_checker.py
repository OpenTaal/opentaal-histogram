"""Test class Checker."""

from pytest import fixture

from opentaal import Checker

# pylint:disable=missing-function-docstring


@fixture
def checker():
    return Checker()


@fixture
def words():
    return ['D', 'tafel', 'geod', ',', 'wow', '?', 'Ja', '!']

# pylint:disable=redefined-outer-name


def test_members(checker):
    res = str(checker)
    assert '.dic' in res and ' ' in res and res.endswith('aff')
    res = repr(checker)
    assert 'entries=' in res and 'version=' in res
    assert ' ' in checker.version()
    assert len(checker) > 0


def test_spelling(checker):
    assert checker.check('tafel') is True
    assert checker.check('tafle') is False
    assert checker.check('tafel poot') is False
    assert checker.check('tafle poot') is False
    assert checker.check('tafel poot', space=True) is True
    assert checker.check('tafle poot', space=True) is False


def test_suggest(checker):
    assert checker.suggest('tafle') == ['tafel', 'tale']
    assert checker.suggest('tafel') == ['Tafel']


def test_stem(checker):
    assert checker.stem('tafels') == [b'tafel']


def test_analyze(checker):
    assert checker.analyze('tafels') == [b' st:tafel ts:NN2']


def test_spelling_list(checker, words):
    assert checker.check_list(words) == [True, True, False, True, True, True,
                                         True, True]


def test_spelling_list_index(checker, words):
    assert checker.check_list_index(words) == {2}

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring
