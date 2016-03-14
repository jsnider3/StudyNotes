# CPython

I'm interested in contributing to CPython. These are my notes on
the codebase.

## How to make and test

* make -j2 && ./python -m test -j3

## Mercurial Usage

* How to find out the author of a line of code?
** `hg annotate -u <filename>`

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

There's a TODO in Objects/byteobject.c to optimize a special case for
a single character. That seems like something I could do.

There is also an identical TODO in Objects/bytearrayobject.c.
Both of these are in functions called replace_interleave which are
basically the same except for using bytes vs bytearrays.

The TODO in bytesobject.c was added by "benjamin" while the TODO in
bytearrayobject.c was added by "nnorwitz".

I made a change to do nothing if the count was 1 and test_bytes
test_dbm failed. This is good since it means test cases cover this
scenario and we thus have an easy way to know when we've fixed the problem.
