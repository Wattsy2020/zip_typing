from tuple_zip import zip_

def test_two_tuples() -> None:
    tuple1 = (1, "a")
    tuple2 = (2, "b")
    zipped = zip_(tuple1, tuple2)
    assert zipped == ((1, 2), ("a", "b"))
    assert zipped == tuple(zip(tuple1, tuple2))
