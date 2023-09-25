
from luna.go import main, first
main()

from beartype.typing import List, TypeVar
list_one: List[str] = ["a", "b", "c"]
print(first(list_one))

list_two: List[int] = [1, 2, 3]
print(first(list_two))
