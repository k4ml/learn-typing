
from luna.go import add, first
add(1, 2)

"""
beartype will throw:-

add(1, "a")
  File "<@beartype(luna.go.add) at 0x7f6e3661d580>", line 40, in add
beartype.roar.BeartypeCallHintParamViolation: Function luna.go.add() parameter y='a' violates type hint <class 'int'> under non-default configuration BeartypeConf(claw_is_pep526=True, is_color=None, is_debug=False, is_pep484_tower=False, strategy=<BeartypeStrategy.O1: 2>, warning_cls_on_decorator_exception=<class 'beartype.roar._roarwarn.BeartypeClawDecorWarning'>), as str 'a' not instance of int.

mypy will throw:-

error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
"""
#add(1, "a")


"""
mypy will throw:-

error: Incompatible types in assignment (expression has type "TP", variable has type "str")  [assignment]
run.py:29: error: Name "ret" already defined on line 18  [no-redef]
"""
ret: str = add(1, 2)

from beartype.typing import List, TypeVar
list_one: List[str] = ["a", "b", "c"]
print(first(list_one))

list_two: List[int] = [1, 2, 3]
print(first(list_two))

from luna.go import DMessage
dmesg = DMessage()
ret: str = dmesg.send("hello", 1)
