#!/usr/bin/env python
'''
  Test cases for Fython.

  @author: Joshua Snider
  @date: 2015/05/17
  @license: GNU Public License v3.0
'''

from  blackscholes import *
import unittest
from fython import *

class Tests(unittest.TestCase):

  def test_blackscholes(self):
    '''Test cases for Black-Scholes option pricing.'''
    bs = BlackScholes(100.0, 105.0, 1.0, 0.05, 0.2)
    assert(float_eq(bs.euro_call(), 8.021, .01))
    assert(float_eq(bs.euro_put(), 7.9, .001))
    (d, g, v, t, r) = bs.partials_call()
    assert(float_eq(d, 0.542, 0.001))
    assert(float_eq(g, 0.019, 0.001))
    assert(float_eq(v, 39.670, 0.001))
    assert(float_eq(t, -6.277, 0.001))
    assert(float_eq(r, 46.201, 0.001))
    (d, g, v, t, r) = bs.partials_put()
    assert(float_eq(d, -0.458, 0.001))
    assert(float_eq(g, 0.019, 0.001))
    assert(float_eq(v, 39.670, 0.001))
    assert(float_eq(t, -1.283, 0.001))
    assert(float_eq(r, -53.678, 0.001))

  def test_montecarlo(self):
    '''Example usage of monte_carlo, but will probabilistically fail.'''
    #assert(8.1 > monte_carlo_euro(100.0, 105.0, 1.0, 0.05, 0.2) > 7.9)
    pass

  def test_vol(self):
    info = rolling_vol('GOOG')
#    print(info.tail())
    '''info[['Close', 'Volatility']].plot(subplots=True, color='blue',
                                  figsize=(8, 6))
    plt.show()'''

  def test_imp_vol(self):
    '''Test implied volatility.'''
    hs = pd.HDFStore('./source/vstoxx_data_31032014.h5', 'r')
    futures_data = hs['futures_data'] 
    #print(futures_data)
    options_data = hs['options_data'] 
    options_data['IMP_VOL'] = 0.0
    moneyness = 0.5
    V0 = 17.6639
    r = 0.01
    assert(float_eq(1.9409,
      BlackScholes(17.6639, 1.0, 1, .01, 2.0).imp_vol(16.85), .01))
    for option in options_data.index:
      forward = (futures_data[futures_data['MATURITY'] ==
                  options_data.loc[option]['MATURITY']]['PRICE'].values[0])
      if (forward  and (1 - moneyness) < options_data.loc[option]['STRIKE'] <
                                      (1 + moneyness)):
        imp_vol = BlackScholes(V0, options_data.loc[option]['STRIKE'],
                              options_data.loc[option]['TTM'], r, 2.0).imp_vol(
                              options_data.loc[option]['PRICE'])
        options_data['IMP_VOL'].loc[option] = imp_vol

if __name__ == '__main__':
  unittest.main()

