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


@given(st.lists(random_types_recursive))
def test_normal_zip_one_elem(list_: list[Any]) -> None:
    assert zip_(list_) == tuple(zip(list_))


random_list = st.lists(random_types_recursive)


@given(
    st.tuples(
        random_list, random_list, random_list, random_list, random_list, random_list
    )
)
def test_normal_zip_six_elem(lists: tuple[list[Any], ...]) -> None:
    assert zip_(lists) == tuple(zip(lists))


def test_type_tuple_zip() -> None:
    """Test that mypy infers the type correctly, it should raise a type error if return type of zip_ doesn't match the declared type"""
    tuple1 = (1, "a")
    tuple2 = (2, "b")
    result: tuple[tuple[int, ...], tuple[str, ...]]
    result = zip_(tuple1, tuple2)

    assert isinstance(result, tuple)
    output1, output2 = result
    assert isinstance(output1, tuple) and all(isinstance(o, int) for o in output1)
    assert isinstance(output2, tuple) and all(isinstance(o, str) for o in output2)


def test_type_normal_zip() -> None:
    """Test that mypy infers the type correctly, it should raise a type error if return type of zip_ doesn't match the declared type"""
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    result: tuple[tuple[int, str], ...]
    result = zip_(list1, list2)

    assert isinstance(result, tuple)
    assert all(
        isinstance(elem1, int) and isinstance(elem2, str) for elem1, elem2 in result
    )
