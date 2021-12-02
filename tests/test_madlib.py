import pytest
from madlib_cli.madlib import read_template, parse_template, merge, regex_strip, regex_list


def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_regex_strip():
    actual = regex_strip('{Test}')
    expected = '{}'
    assert actual == expected



def test_regex_list_a():
    actual = regex_list('this is a {test} of the emergency broadcast {system}')
    expected = ['test','system']
    assert actual == expected

def test_regex_list_b():
    actual = regex_list('{Adjective}')
    expected = ['Adjective']
    assert actual == expected