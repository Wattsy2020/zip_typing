# zip_typing
Did you know that mypy has difficulty understanding zip's output type? For instance in 
```python
tuple1: tuple[int, str] = (1, "a")
tuple2: tuple[int, str] = (2, "b")
result1, result2 = list(zip(tuple1, tuple2))  # [(1, 2), ('a', 'b')]
reveal_type(result1)  # Tuple[builtins.object, builtins.object]
reveal_type(result2)  # Tuple[builtins.object, builtins.object]
```

We understand that result1 is a `tuple[int, int]`, and result2 a `tuple[str, str]` but mypy can only tell us these tuples contain objects.
​
The reason is because python doesn't support Heterogenuous Iterables, i.e. Iterables that contain specified types in different elements.
So there is no way in the following example to represent `result` as having type: `list[tuple[int, int] in 0th element, then tuple[str, str] in 1st element]`
```python
tuple1: tuple[int, str] = (1, "a")
tuple2: tuple[int, str] = (2, "b")
result = list(zip(tuple1, tuple2))  # [(1, 2), ('a', 'b')]
reveal_type(result)  # builtins.list[Tuple[builtins.object, builtins.object]]
```
Instead the best it can do is type result as `list[tuple[object, object]]`.

This is because zip's mypy stubs are defined using Iterables:
```python
@overload
    def __new__(cls, __iter1: Iterable[_T1], *, strict: bool = ...) -> zip[tuple[_T1]]: ...
    @overload
    def __new__(cls, __iter1: Iterable[_T1], __iter2: Iterable[_T2], *, strict: bool = ...) -> zip[tuple[_T1, _T2]]: ...
...
```
For example the two argument form of zip takes two iterables of generic types `_T1` and `_T2`, and outputs a zip iterable of `tuple[_T1, T2]`. When passing this two argument form a `tuple[int, str]`, the only way to represent it as an `Iterable[_T1]` is to use the common type of `int` and `str`: `object`. So `tuple[int, str]` becomes `Iterable[object]`, and the output becomes `zip[tuple[object, object]]`.


There is a hack to "correctly" represent the output type of `zip` called on a tuple, which is implemented here in `tuple_zip.py`:
```python
@overload
def zip_(*tuples: tuple[_T1]) -> tuple[tuple[_T1, ...]]:  # type: ignore
@overload
def zip_(*tuples: tuple[_T1, _T2]) -> tuple[tuple[_T1, ...], tuple[_T2, ...]]:  # type: ignore
```
The only solution is to define `zip_` as outputting a `tuple`, not an iterable, as tuples are the only way to represent "element 0 has one type, element 1 has a different type". Unfortunately this means our `zip_` function loses the ability to output an iterator that can be lazily iterated over.

For further reading:
- mypy contributors attempted to fix this: https://github.com/python/mypy/issues/8454 
- a paper describing heterogenuous iterables: https://okmij.org/ftp/Haskell/HList-ext.pdf