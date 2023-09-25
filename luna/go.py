
from beartype import beartype

class TP: pass

@beartype
def add(x: int, y: int) -> TP:
    return TP()

@beartype
def main():
    total: TP = add(1, 2)

from beartype.typing import List, TypeVar

T = TypeVar("T")

def first(container: List[T]) -> T:
    return "a"
    #return container[1]
