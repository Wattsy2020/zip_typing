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
