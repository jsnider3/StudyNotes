#!/usr/bin/env python
'''
  Notes from reading the book Python for Finance
  by Yves Hilpisch.
  @see: http://shop.oreilly.com/product/0636920032441.do

  @author: Joshua Snider
  @date: 2015/05/17
  @license: GNU Public License v3.0
'''

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas.io.data as web
import scipy as sp
import scipy.stats 

def monte_carlo_euro(s, k, t, r, sigma):
  '''
     Calculate the value of a European Call option
     using Monte Carlo methods. No dividends.
     @param s: initial stock price
     @param k: strike price
     @param t: time to maturity
     @param r: Constant, riskless short rate
     @param sigma: Constant volatility
     @return: A value for an option with the given parameters.
  ''' 
  z = np.random.standard_normal(100000)
  st = s * np.exp((r - 0.5 * sigma ** 2) * t + sigma * np.sqrt(t) * z)
  ht = np.maximum(st - k, 0)
  return np.exp(-r * t) * sum(ht) / 100000

def black_scholes_euro_call(s, k, t, r, sigma):
  '''
     Calculate the value of a European Call option
     using Black-Scholes. No dividends.
     @param s: initial stock price
     @param k: strike price
     @param t: time to maturity
     @param r: Constant, riskless short rate
     @param sigma: Constant volatility
     @return: The value for an option with the given parameters.
  '''
  d = black_scholes_factors(s, k, t, r, sigma)
  return N(d[0]) * s - N(d[1]) * k * np.exp(-r * t)

def black_scholes_euro_put(s, k, t, r, sigma):
  '''
     Calculate the value of a European put option
     using Black-Scholes. No dividends.
     @param s: initial stock price
     @param k: strike price
     @param t: time to maturity
     @param r: Constant, riskless short rate
     @param sigma: Constant volatility
     @return: The value for an option with the given parameters.
  '''
  d = black_scholes_factors(s, k, t, r, sigma)
  return N(-d[1]) * k * np.exp(-r * t) - N(-d[0]) * s

def black_scholes_factors(s, k, t, r, sigma):
  '''
    Calcultes the d1 and d2 factors used in a large
    number of Black Scholes equations.
     @param s: initial stock price
     @param k: strike price
     @param t: time to maturity
     @param r: Constant, riskless short rate
     @param sigma: Constant volatility
     @return: [d1, d2]
  '''
  d = []
  d.append(1.0 / (sigma * np.sqrt(t)) * (math.log(s / k)
                  + (r + sigma ** 2 / 2) * t))
  d.append(1.0 / (sigma * np.sqrt(t)) * (math.log(s / k)
                  + (r - sigma ** 2 / 2) * t))
  return d

def black_scholes_call_partials(s, k, t, r, sigma):
  '''
    Calculates the partial derivatives from the Black-Scholes
    for a call option.
    @param s: initial stock price
    @param k: strike price
    @param t: time to maturity
    @param r: Constant, riskless short rate
    @param sigma: Constant volatility
    @return: (Delta, Gamma, Vega, Theta, Rho)
  '''
  d = [0.0, 0.0]
  d[0] = 1.0 / (sigma * np.sqrt(t)) * (math.log(s / k)
                  + (r + sigma ** 2 / 2) * t)
  d[1] = 1.0 / (sigma * np.sqrt(t)) * (math.log(s / k)
                  + (r - sigma ** 2 / 2) * t)
  Delta = N(d[0])
  Gamma = Np(d[0]) / (s*sigma*np.sqrt(t))
  Vega = s * Np(d[0]) * np.sqrt(t)
  Theta = (-s * Np(d[0]) * sigma / (2 * np.sqrt(t)) -
    r * k * math.exp(-r * t) * N(d[1]))
  Rho = k * t * np.exp(-r * t) * N(d[1])
  return (Delta, Gamma, Vega, Theta, Rho)

def float_eq(f,s, unc):
  ''' Determine if two floats are equal at a given uncertainty.
      @param f: First float.
      @param s: Second float.
      @param unc: The uncertainty.
      @return: Whether f and s are within that range of each other.
  '''
  return f + unc > s and s + unc > f

def N(x):
  '''cdf of the standard normal 
     distribution.'''
  return sp.stats.norm.cdf(x)

def Np(x):
  '''pdf of the standard normal 
     distribution.'''
  return sp.stats.norm.pdf(x)

def price_plot(stk):
  '''Plot the closing price and volatility of a stock,
     then hang until user input.
     @param stk: The stock's ticker symbol e.g. GOOG.'''
  info = web.DataReader(stk, data_source='google',
                  start='3/14/2009', end='4/14/2014')
  info['Log_Ret'] = np.log(info['Close'] / info['Close'].shift(1))
  info['Volatility'] = pd.rolling_std(info['Log_Ret'],
                          window=252) * np.sqrt(252)
  print(info.tail())
  print(type(info[['Close', 'Volatility']]))
  info[['Close', 'Volatility']].plot(subplots=True, color='blue',
                                  figsize=(8, 6))
  plt.show()
  input('')

def tests():
  ''' Run test cases.'''
  assert(8.1 > monte_carlo_euro(100.0, 105.0, 1.0, 0.05, 0.2) > 7.9)
  assert(float_eq(black_scholes_euro_call(100.0, 105.0, 1.0, 0.05, 0.2),
    8.021, .01))
  assert(float_eq(black_scholes_euro_put(100.0, 105.0, 1.0, 0.05, 0.2),
    7.9, .001))
  (d, g, v, t, r) = black_scholes_call_partials(100.0, 105.0, 1.0, 0.05, 0.2)
  assert(float_eq(d, 0.542, 0.001))
  assert(float_eq(g, 0.019, 0.001))
  assert(float_eq(v, 39.670, 0.001))
  assert(float_eq(t, -6.277, 0.001))
  assert(float_eq(r, 46.201, 0.001))
  price_plot('GOOG')

if __name__ == '__main__':
  tests()
