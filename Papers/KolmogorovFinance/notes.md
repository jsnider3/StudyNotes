## Notes from reading the paper

* In the end, they support the Fama's EMH. This is bad for people who are
  deep into technical analysis, but irrelevant for scalping.
* The idea that financial engineering has any hope to eventually make a
  deterministic model of the stock market, even theoretically is hilarious,
  But that's what the assert asserts on page 6. 
* It's kinda cool that the choice of language has only a constant effect on
  the complexity of an arbitrary string. I'm not sure if this is surprising
  or obvious.
* A definitely obvious result is that `K(s) <= n + O(log n)` for a string 
  `s` of length `n`. This is another way of saying that you can just copy
  a string for complexity `n` and waste `O(log n)` space on overhead.
* Kolmogorv complexity defines a random infinite string as one whose
  description is within a constant size of itself. Most strings are random.
* They also introduced an argument that `K(s)` could be used as a predictor
  of whether or not a string was random.  
* Their idea of "lossless discretization" isn't actually lossless, but just
  gets rid of spurious precision.
* They suggest using 13 bits to preserve the 4th digit. 16 bits is probably
  better for the machine. 

* I'm 95% sure that the `i.i.d.N(0, 1)` on page 13 is the same function as
  numpy.random.normal
