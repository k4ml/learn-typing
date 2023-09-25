
## Quickstart

    python -mvenv venv
    venv/bin/pip install -r requirements.txt
    venv/bin/python run.py

## The Type check
Example type mismatch caught by beartype:-

```
Traceback (most recent call last):
  File "/home/kamal/python/learn-typing/run.py", line 3, in <module>
    main()
  File "/home/kamal/python/learn-typing/luna/go.py", line 12, in main
    total: TP = add(1, 2)
                ^^^^^^^^^
  File "<@beartype(luna.go.add) at 0x7ffb82a29440>", line 56, in add
beartype.roar.BeartypeCallHintReturnViolation: Function luna.go.add() return 1 violates type hint <class 'luna.go.TP'>, as int 1 not instance of <class "luna.go.TP">.
```

Example caught by mypy:-

```
 venv/bin/mypy run.py
luna/go.py:12: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
luna/go.py:19: error: Incompatible return value type (got "str", expected "T")  [return-value]
Found 1 error in 1 file (checked 1 source file)
```

Beartype however didn't catch above mismatch.
