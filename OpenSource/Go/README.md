# README

Golang is a statically-typed programming language intended to compete
with C++. It also is a decent competitor against Python for some types
of quick scripting work.

Like a lot of open source projects it has a GitHub repo that is just
a mirror/bug-tracker. The authoritative repo is located at
https://go.googlesource.com/go.

Golang uses Lord Google's code review procedure basically.

## Implementing languages

Golang has 92 files written in C, plus 15 headers.
It has 1 file written in C++, but it's only like 10 lines.
It has 4289 files written in Go.

What can I conclude from that? Probably a lot, but I need more time
to assimilate that fact. 

It means that code generation (and probably parsing) is done in Go.
Bootstrapping for the win. Specifically, that kind of stuff can be
found in src/cmd/compile. 

## Name Mixup

In a hilarious sequence of events, I received an email 2016/4/10 asking
me to code review a change. It looked good to me, but it was probably
intended for a different Josh Snider and I let them know.
