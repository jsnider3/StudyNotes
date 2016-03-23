# CPython

I'm interested in contributing to CPython. These are my notes on
the codebase and project.

## How to make and test

* ./configure --with-pydebug
* make -j2 && ./python -m test -j3

## Easy issues without patch

On the left of bugs.python.org, there are two links
called "Easy Issues" and "Issues with patch". Those links are:
* http://bugs.python.org/issue?status=1&@sort=-activity&@columns=id,activity,title,creator,status&@dispname=Issues%20with%20patch&@startwith=0&@group=priority&keywords=2&@action=search&@filter=&@pagesize=50
* http://bugs.python.org/issue?status=1&@sort=-activity&@columns=id,activity,title,creator,status&@dispname=Easy%20issues&@startwith=0&@group=priority&keywords=6&@action=search&@filter=&@pagesize=50

Is there a way to get the easy issues without a patch?

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

## PyObject_RichCompareBool

Takes two objects and a boolean operator. Returns -1 for error, 0 for
!(first op second), and 1 for first op second.

## Py_RETURN_NONE

You'll see this a lot. It's just a macro which takes the "None" object,
increments its reference count, and returns it. Basically, it's the
C-Code that makes Python functions return None by default.

You may feel that this should be similar to `return NULL;`, but that
signifies an error.

## Modules

The Modules directory contains the standard library modules.
All of these are named with module in their name.
I'm not sure what the other files in this directory do.

## heapq.heappushpop

This is supposed to be more efficient than doing heappush then heappop.
What does it do to make that happen? One thing it does is check if the new
thing would replace the top of the heap. In that case it does nothing.
It also only has to redo the heapiness once, instead of twice for the
succession.

## Patching

Patches are made by piping the result of 'hg diff' into a file.
When you have review comments on a patch xxx.patch, your next
patch should contain all the changes, including those from xxx.patch,
and be named xxx-2.patch.
