from tuple_zip import zip_


def test_tuple_one_elem() -> None:
    tuple1 = (1,)
    tuple2 = (2,)
    zipped = zip_(tuple1, tuple2)
    assert zipped == ((1, 2),)
    assert zipped == tuple(zip(tuple1, tuple2))


def test_tuple_two_elem() -> None:
    tuple1 = (1, "a")
    tuple2 = (2, "b")
    zipped = zip_(tuple1, tuple2)
    assert zipped == ((1, 2), ("a", "b"))
    assert zipped == tuple(zip(tuple1, tuple2))


def test_tuple_three_elem() -> None:
    tuple1 = (1, "a", 1.1)
    tuple2 = (2, "b", 2.1)
    zipped = zip_(tuple1, tuple2)
    assert zipped == ((1, 2), ("a", "b"), (1.1, 2.1))
    assert zipped == tuple(zip(tuple1, tuple2))


def test_tuple_four_elem() -> None:
    tuple1 = (1, "a", 1.1, None)
    tuple2 = (2, "b", 2.1, None)
    zipped = zip_(tuple1, tuple2)
    assert zipped == ((1, 2), ("a", "b"), (1.1, 2.1), (None, None))
    assert zipped == tuple(zip(tuple1, tuple2))


def test_tuple_five_elem() -> None:
    tuple1 = (1, "a", 1.1, None, [11, 12])
    tuple2 = (2, "b", 2.1, None, [21, 22])
    zipped = zip_(tuple1, tuple2)
    assert zipped == (
        (1, 2),
        ("a", "b"),
        (1.1, 2.1),
        (None, None),
        ([11, 12], [21, 22]),
    )
    assert zipped == tuple(zip(tuple1, tuple2))
