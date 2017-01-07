from Text.pig_latin import PigLatin
from pytest import fail


def test_latinize():
    expected = 'Isthay isway away esttay'
    observed = PigLatin.latinize('This is a test')
    assert expected == observed


def test_latinize_word():
    expected = 'esttay'
    observed = PigLatin.latinize_word('test')
    assert observed == expected


def test_latinize_single_vowel():
    expected = 'away'
    observed = PigLatin.latinize_word('a')
    assert observed == expected


def test_latinize_word_with_simple_consonant():
    expected = 'obbay'
    observed = PigLatin.latinize_word('bob')
    assert observed == expected


def test_latinize_word_with_consonant_cluster():
    expected = 'eepshay'
    observed = PigLatin.latinize_word('sheep')
    assert observed == expected


def test_starts_with_vowel():
    expected = True
    word = 'a'
    observed = PigLatin.starts_with_vowel(word)
    assert expected == observed


def test_doesnt_start_with_vowel():
    expected = False
    word = 'b'
    observed = PigLatin.starts_with_vowel(word)
    assert expected == observed


def test_empty_word_doesnt_start_with_vowel():
    expected = False
    word = ''
    observed = PigLatin.starts_with_vowel(word)
    assert expected == observed


def test_starts_with_consonant_cluster():
    expected = True
    word = 'sheep'
    observed = PigLatin.starts_with_consonant_cluster(word)
    assert observed == expected


def test_get_consonant_cluster_length():
    expected = 2
    word = 'sheep'
    observed = PigLatin.get_consonant_cluster_length(word)
    assert observed == expected
