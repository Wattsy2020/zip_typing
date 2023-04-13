# First problem: pylance cannot infer the type of this list without the type hint
tuple_list: list[tuple[int, str]] = [(1, "a"), (2, "b")]
reveal_type(tuple_list)

# Second problem: mypy cannot infer the type of the zipped list
zipped = zip(*tuple_list)  # problem is here, mypy cannot understand the type after zipping, maybe it has a problem with generics?
reveal_type(zipped)
zipped_list = list(zipped)
reveal_type(zipped_list)
ints, strs = zipped_list
reveal_type(ints) # for some reason it thinks this is tuple[Any, ...] (pylance is more correct and knows this is tuple[int | str])
reveal_type(strs)
int1, _ = ints
reveal_type(int1) # mypy thinks int1 is Any for some reason

# TODO:
# File github issue on mypy bug, it should be able to recognise the type of zip
# Work on it I guess, figure out how to write a unit test for this
