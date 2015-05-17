#!/usr/bin/env python
'''
  Provides methods for using the Black-Scholes
  equation.
  @author: Joshua Snider
  @date: 2015/05/17
  @license: GNU Public License v3.0
'''

import math
import numpy as np
import pandas as pd
import pandas.io.data as web
import scipy as sp
import scipy.stats 

class BlackScholes(object):
  '''Wraps methods in an object'''

  def init(self):
    '''Nothing to do.'''
    pass

  def euro_call(self, s, k, t, r, sigma):
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
    d = self.factors(s, k, t, r, sigma)
    return self.N(d[0]) * s - self.N(d[1]) * k * np.exp(-r * t)

  def euro_put(self, s, k, t, r, sigma):
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
    d = self.factors(s, k, t, r, sigma)
    return self.N(-d[1]) * k * np.exp(-r * t) - self.N(-d[0]) * s

  def factors(self, s, k, t, r, sigma):
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

  def call_partials(self, s, k, t, r, sigma):
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
    d = self.factors(s, k, t, r, sigma)
    Delta = self.N(d[0])
    Gamma = self.Np(d[0]) / (s * sigma * np.sqrt(t))
    Vega = s * self.Np(d[0]) * np.sqrt(t)
    Theta = (-s * self.Np(d[0]) * sigma / (2 * np.sqrt(t)) -
      r * k * math.exp(-r * t) * self.N(d[1]))
    Rho = k * t * np.exp(-r * t) * self.N(d[1])
    return (Delta, Gamma, Vega, Theta, Rho)

  def N(self, x):
    '''cdf of the standard normal 
      distribution.'''
    return sp.stats.norm.cdf(x)

  def Np(self, x):
    '''pdf of the standard normal 
      distribution.'''
    return sp.stats.norm.pdf(x)
