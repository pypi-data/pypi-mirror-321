from typing import *

__all__ = ["datarepr"]


def datarepr(name: Any, /, *args: Any, **kwargs: Any) -> str:
    "This function allows for common sense representation."
    parts = list()
    for a in args:
        parts.append(repr(a))
    for i in kwargs.items():
        parts.append("%s=%r" % i)
    content = ", ".join(parts)
    ans = "%s(%s)" % (name, content)
    return ans
