
from beartype import beartype

class TP: pass

@beartype
def add(x: int, y: int) -> TP:
    """
    Change to `return 1` and beartype will throw:-

    total: TP = add(1, 2)
                ^^^^^^^^^
  File "<@beartype(luna.go.add) at 0x7fc1feb91c60>", line 56, in add
beartype.roar.BeartypeCallHintReturnViolation: Function luna.go.add() return 1 violates type hint <class 'luna.go.TP'> under non-default configuration BeartypeConf(claw_is_pep526=True, is_color=None, is_debug=False, is_pep484_tower=False, strategy=<BeartypeStrategy.O1: 2>, warning_cls_on_decorator_exception=<class 'beartype.roar._roarwarn.BeartypeClawDecorWarning'>), as int 1 not instance of <class "luna.go.TP">.
    """
    return TP()

def main():
    total: TP = add(1, 2)

from beartype.typing import List, TypeVar

T = TypeVar("T")

def first(container: List[T]) -> T:
    """
    Change to something like `return "a"` and mypy will throw:-

    error: Incompatible return value type (got "str", expected "T")  [return-value]

    """
    return container[1]

class Message():
    def send(self, text: str) -> str:
        return text

class DMessage(Message):
    """
    mypy should throw:-

    error: Signature of "send" incompatible with supertype "Message"  [override]
    """

    def send(self, text: str, num: int) -> str:
        return text
