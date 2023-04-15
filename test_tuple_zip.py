from typing import Any

from hypothesis import given
from hypothesis import strategies as st

from tuple_zip import zip_

random_types = st.one_of(st.integers(), st.text(), st.floats())
random_types_recursive = st.one_of(
    random_types,
    st.lists(random_types),
    st.tuples(random_types),
    st.sets(random_types),
    st.dictionaries(random_types, random_types),
)


@given(st.tuples(random_types_recursive))
def test_tuple_one_elem(tuple_: tuple[Any]) -> None:
    zipped = zip_(tuple_, tuple_)
    assert zipped == ((tuple_[0], tuple_[0]),)
    assert zipped == tuple(zip(tuple_, tuple_))


@given(st.tuples(random_types_recursive, random_types_recursive))
def test_tuple_two_elem(tuple_: tuple[Any, Any]) -> None:
    zipped = zip_(tuple_, tuple_)
    assert zipped == ((tuple_[0], tuple_[0]), (tuple_[1], tuple_[1]))
    assert zipped == tuple(zip(tuple_, tuple_))


@given(
    st.tuples(random_types_recursive, random_types_recursive, random_types_recursive)
)
def test_tuple_three_elem(tuple_: tuple[Any, Any, Any]) -> None:
    zipped = zip_(tuple_, tuple_)
    assert zipped == (
        (tuple_[0], tuple_[0]),
        (tuple_[1], tuple_[1]),
        (tuple_[2], tuple_[2]),
    )
    assert zipped == tuple(zip(tuple_, tuple_))


@given(
    st.tuples(
        random_types_recursive,
        random_types_recursive,
        random_types_recursive,
        random_types_recursive,
        random_types_recursive,
        random_types_recursive,
    )
)
def test_tuple_six_elem(tuple_: tuple[Any, Any, Any, Any, Any, Any]) -> None:
    zipped = zip_(tuple_, tuple_)
    assert zipped == (
        (tuple_[0], tuple_[0]),
        (tuple_[1], tuple_[1]),
        (tuple_[2], tuple_[2]),
        (tuple_[3], tuple_[3]),
        (tuple_[4], tuple_[4]),
        (tuple_[5], tuple_[5]),
    )
    assert zipped == tuple(zip(tuple_, tuple_))
