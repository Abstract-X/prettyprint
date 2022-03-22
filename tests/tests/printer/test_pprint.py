import pytest

from prettyprint import pprint
from tests.stdout_context import StdoutContext


@pytest.mark.parametrize(
    ("value", "indent", "expected_output"),
    (
        ([], 4, "[]"),
        ([1], 4, """[
    1
]"""),
        ([1, 2], 4, """[
    1,
    2
]"""),
        ({}, 4, "{}"),
        ({"a": 1}, 4, """{
    'a': 1
}"""),
        ({"a": 1, "b": 2}, 4, """{
    'a': 1,
    'b': 2
}"""),
        ((), 4, "()"),
        ((1,), 4, """(
    1,
)"""),
        ((1, 2), 4, """(
    1,
    2
)"""),
        (set(), 4, "set()"),
        ({1}, 4, """{
    1
}"""),
        ({1, 2}, 4, """{
    1,
    2
}"""),
        (frozenset((1,)), 4, "frozenset({1})"),
        (frozenset((1, 2)), 4, "frozenset({1, 2})"),
        (None, 4, "None"),
        (True, 4, "True"),
        (False, 4, "False"),
        ({"a": [1, 2], "b": {"c": (3,), "d": {4}}}, 4, """{
    'a': [
        1,
        2
    ],
    'b': {
        'c': (
            3,
        ),
        'd': {
            4
        }
    }
}"""),
        ({"a": [1, 2], "b": {"c": (3,), "d": {4}}}, 2, """{
  'a': [
    1,
    2
  ],
  'b': {
    'c': (
      3,
    ),
    'd': {
      4
    }
  }
}""")
    )
)
def test_behavior(value, indent, expected_output):
    stdout_context = StdoutContext()

    with stdout_context:
        pprint(value, indent)

    assert stdout_context.get_value() == expected_output
