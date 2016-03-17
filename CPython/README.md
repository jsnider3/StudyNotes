# CPython

I'm interested in contributing to CPython. These are my notes on
the codebase.

## How to make and test

* ./configure --with-pydebug
* make -j2 && ./python -m test -j3

## How to debug

* Edit your .gdbinit to add it to the auto-load path.
  gdb will tell you if you don't do this.
* Run `gdb python` with your modified python binary.

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

## Py_MEMCPY

Py_MEMCPY is defined in Include/pyport.h. It's #defined as memcpy,
except for when compiling with Visual Studio in which case it does
some optimizations for blocks smaller than 16.

## Patching

Patches are made by piping the result of 'hg diff' into a file.
When you have review comments on a patch xxx.patch, your next
patch should contain all the changes, including those from xxx.patch,
and be named xxx-2.patch.
