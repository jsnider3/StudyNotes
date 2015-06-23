## Notes

* This book actually has a floppy disk! I guess Java's not
a youngun anymore.

* I did not know that Java started as Oak. Good to know.

* Author disparages Java's speed, which is somewhat inappropriate
to do in a book about Java, but I'm not sure he really had a way
to know of the improvements that would be made in JIT technology.

* Magic Beans does class verification, which includes type checking.
This type-checking is in addition to the checking done by the compiler.
Magic Beans is turned off and on depending on security settings.

* Microsoft's implementation of Java, the ill-fated J# is mentioned
briefly.

* They say that the bytecode doesn't record info about the lexical blocks
in the method, but that can be extracted automatically. I actually did
that by hand back in assembly programming class.

* Jasmin doesn't verify the java classes it generates, you have to run
`java -verify` on them to check. Jasmin also looks like it needs to have
one class per file. This is slightly annoying.

* In an ideal world, Java being a stack machine would greatly reduce
the amount of temporary variables you need to keep track of. A well built
compiler can take advantage of this fact, but I don't think Scales
will be smart enough to.

* One more obstacle is that we need to tell the jvm in advance how many
local variables and how much stack space we will be using. A trivial
workaround is to say we will be using an excessive amount of them. A
smarter approach may be to walk the ast first and have people estimate
how much stuff they need.

* Jasmin even has typed return statements! How strict!
