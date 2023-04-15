from typing import TYPE_CHECKING

# First problem: pylance cannot infer the type of this list without the type hint
tuple_list: list[tuple[int, str]] = [(1, "a"), (2, "b")]
if TYPE_CHECKING:
    reveal_type(tuple_list)

# Second problem: mypy cannot infer the type of the zipped list
zipped = zip(*tuple_list)  # problem is here, mypy cannot understand the type after zipping, maybe it has a problem with generics?
# actually the problem is that the length of the list is unknown, so it triggers zip's final overload which just assumes Any
zipped2 = list(zip(tuple_list[0], tuple_list[1]))
tuple1, tuple2 = tuple_list
# there is an additional problem: it can't understand tuples of mixed types
# zip is interpreting args (tuple[int, str], tuple[int, str]) as (Iterable[int | str], Iterable[int | str])
zipped3 = list(zip(tuple1, tuple2)) 
if TYPE_CHECKING:
    reveal_type(zipped)
    reveal_type(zipped2)
    reveal_type(tuple1)
    reveal_type(zipped3)
    a, b = zipped3
zipped_list = list(zipped)
if TYPE_CHECKING:
    reveal_type(zipped_list)
ints, strs = zipped_list
if TYPE_CHECKING:
    reveal_type(ints) # for some reason it thinks this is tuple[Any, ...] (pylance is more correct and knows this is tuple[int | str])
    reveal_type(strs)
int1, _ = ints
if TYPE_CHECKING:
    reveal_type(int1) # mypy thinks int1 is Any for some reason

# somehow mypy validates that it actually is an int at the end of the day
int2: int = int1 + 1
if TYPE_CHECKING:
    reveal_type(int2)

# and also is perfectly fine with saying it's an int???
# though python of course gives a type error here
str2: str = int1 + "hello"
if TYPE_CHECKING:
    reveal_type(str2)

# TODO:
# File github issue on mypy bug, it should be able to recognise the type of zip
# Work on it I guess, figure out how to write a unit test for this
