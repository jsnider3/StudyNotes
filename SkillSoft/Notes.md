#### C++11 Programming Fundamentals

* They mentioned that `auto` was used when the type was obvious.
In practice it's usually used when the type just has a really long name.
Of course it's only possible to use it when the type is obvious to the
compiler, but C++'s typing discipline means that is all the time.

* They also mentioned `const auto&` vs `auto` in for-each loops, which
is good programming practice.

* `nullptr` was also mentioned and it's superiority over using `NULL` and
`0` was argued well.

* `initializer_list` was introduced as a way to initialize vectors
and also as something you could pass to constructors and functions.
And how these kinds of functions overload each other.

* `constexpr`, like `const` but compile-time! Nothing I didn't already know.

* They talked about using try catch for `bad_alloc` exceptions, which is 
something I've never actually seen done. They also compared that with
using `new(nothrow)`, which is also something I've never seen done. Neither
of these seem like reasonable choices, since running out of memory is
an extremely severe error and it's reasonable to just die when that happens.

* Suffix notation is another feature that seems absolutely useless.
