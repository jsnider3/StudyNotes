#!/usr/bin/env python
'''
  Test cases for PyNance.

  @author: Joshua Snider
  @date: 2015/05/17
  @license: GNU Public License v3.0
'''

import blackscholes
import unittest
from pynance import *
from pynance import *

class Tests(unittest.TestCase):

  def test_blackscholes(self):
    '''Test cases for Black-Scholes option pricing.'''
    bs = blackscholes.BlackScholes()
    assert(float_eq(bs.euro_call(100.0, 105.0, 1.0, 0.05, 0.2),
      8.021, .01))
    assert(float_eq(bs.euro_put(100.0, 105.0, 1.0, 0.05, 0.2),
      7.9, .001))
    (d, g, v, t, r) = bs.call_partials(100.0, 105.0, 1.0, 0.05, 0.2)
    assert(float_eq(d, 0.542, 0.001))
    assert(float_eq(g, 0.019, 0.001))
    assert(float_eq(v, 39.670, 0.001))
    assert(float_eq(t, -6.277, 0.001))
    assert(float_eq(r, 46.201, 0.001))

  def test_montecarlo(self):
    '''Example usage of monte_carlo, but will probabilistically fail.'''
    #assert(8.1 > monte_carlo_euro(100.0, 105.0, 1.0, 0.05, 0.2) > 7.9)
    pass

  def test_plot(self):
    price_plot('GOOG')

if __name__ == '__main__':
  unittest.main()

