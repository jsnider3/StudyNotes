# Golang

Considering contributing to Golang's development. I've heard good
things about it for a while and it seems like something I'd like to be
more familiar with.

## How to Contribute
The instruction are at https://golang.org/doc/contribute.html
Fortunately I still have a CLA on file.

go-contrib-init says I need to configure my .gitcookies. This is
as simple as visiting the linked website and copying a shell command.

Then it says I'm using a release of Go for my GOROOT and should mess with
Golang in a fresh checkout. That can be accomplished with "set GOROOT=".

Then I'm told I need to run go-contrib-init in a git checkout of
https://go.googlesource.com/go. I was expecting go-contrib-init to do that
for me.

After downloading a go repo to Documents\Git\go, it then installed git-codereview
and told me it was set up correctly.

## Search for TODOs

I felt that the easiest place to get started would be to grep for TODO and see
which I could do without help. There were a lot more in go than in CPython, which
you can see in the file in this directory.