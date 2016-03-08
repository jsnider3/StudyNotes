# CPython

I'm interested in contributing to CPython. These are my notes on
the codebase.

## Objects/rangeobject.c

Why does range(4,4) < range(3,6), but not range(4,5) < range(3,6)?
(Because that was python2 and we were comparing lists not rangeobjects)

range is implemented in Objects/rangeobject.c.

It’s cool that they have specialized range iterators for objects that
can and cannot fit in a long.

In python3, ranges are incomparable except for equality.

## Include/object.h

Py_DECREF and Py_INCREF are used for reference counting
(and garbage collecting), they require non-null objects.

Is python3 deployed to anything with a c int less than 16 bits?
object.h:682 leaves room for the possibility.

## TODOs

There's a TOOD in Objects/byteobject.c to optimize a special case.
That seems like something I could do.
