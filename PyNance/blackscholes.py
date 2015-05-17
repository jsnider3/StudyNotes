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

  def __init__(self, s, k, t, r, sigma):
    '''Initialize a model with the given parameters.
       @param s: initial stock price
       @param k: strike price
       @param t: time to maturity
       @param r: Constant, riskless short rate
       @param sigma: Constant volatility
    '''
    self.s = s
    self.k = k
    self.t = t
    self.r = r
    self.sigma = sigma

  def euro_call(self):
    '''
       Calculate the value of a European Call option
        using Black-Scholes. No dividends.
       @return: The value for an option with the given parameters.
    '''
    d = self.factors()
    return self.N(d[0]) * self.s - (self.N(d[1]) * self.k *
                                      np.exp(-self.r * self.t))

  def euro_put(self):
    '''
      Calculate the value of a European put option
      using Black-Scholes. No dividends.
      @return: The value for an option with the given parameters.
    '''
    d = self.factors()
    return (self.N(-d[1]) * self.k * np.exp(-self.r * self.t)
            - self.N(-d[0]) * self.s)

  def factors(self):
    '''
      Calcultes the d1 and d2 factors used in a large
      number of Black Scholes equations.
      @return: [d1, d2]
    '''
    d = []
    d.append(1.0 / (self.sigma * np.sqrt(self.t)) * (math.log(self.s / self.k)
                    + (self.r + self.sigma ** 2 / 2) * self.t))
    d.append(1.0 / (self.sigma * np.sqrt(self.t)) * (math.log(self.s / self.k)
                    + (self.r - self.sigma ** 2 / 2) * self.t))
    return d

  def call_partials(self):
    '''
      Calculates the partial derivatives from the Black-Scholes
      for a call option.
      @return: (Delta, Gamma, Vega, Theta, Rho)
    '''
    d = self.factors()
    Delta = self.N(d[0])
    Gamma = self.Np(d[0]) / (self.s * self.sigma * np.sqrt(self.t))
    Vega = self.s * self.Np(d[0]) * np.sqrt(self.t)
    Theta = (-self.s * self.Np(d[0]) * self.sigma / (2 * np.sqrt(self.t)) -
      self.r * self.k * math.exp(-self.r * self.t) * self.N(d[1]))
    Rho = self.k * self.t * np.exp(-self.r * self.t) * self.N(d[1])
    return (Delta, Gamma, Vega, Theta, Rho)

  def N(self, x):
    '''cdf of the standard normal 
      distribution.'''
    return sp.stats.norm.cdf(x)

  def Np(self, x):
    '''pdf of the standard normal 
      distribution.'''
    return sp.stats.norm.pdf(x)
