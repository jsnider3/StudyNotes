#!/usr/bin/env python
'''
  Provides methods for valuing options
  in a Black-Scholes world.
  @author: Joshua Snider
  @date: 2015/05/17
  @license: GNU Public License v3.0
'''

import math
import numpy as np
import pandas as pd
import pandas.io.data as web
import pdb
import scipy as sp
from scipy.stats import norm

class BlackScholes(object):
  '''Class wrapper for methods.'''

  def __init__(self, s, k, t, r, sigma):
    '''Initialize a model with the given parameters.
       @type s: float
       @param s: initial stock price
       @type k: float
       @param k: strike price
       @type t: float
       @param t: time to maturity
       @type r: float
       @param r: Constant, riskless short rate
       @type sigma: float
       @param sigma: Constant volatility, or best estimate.
    '''
    self.s = s
    self.k = k
    self.t = t
    self.r = r
    self.sigma = sigma
    self.d = self.factors()

  def euro_call(self):
    ''' Calculate the value of a European call option
        using Black-Scholes. No dividends.
        @rtype: float
        @return: The value for an option with the given parameters.'''
    return norm.cdf(self.d[0]) * self.s - (norm.cdf(self.d[1]) * self.k *
                                          np.exp(-self.r * self.t))

  def euro_put(self):
    ''' Calculate the value of a European put option
        using Black-Scholes. No dividends.
        @rtype: float
        @return: The value for an option with the given parameters.'''
    return (norm.cdf(-self.d[1]) * self.k * np.exp(-self.r * self.t)
            - norm.cdf(-self.d[0]) * self.s)

  def factors(self):
    '''
      Calculates the d1 and d2 factors used in a large
      number of Black Scholes equations.
      @rtype: (float, float)
      @return: (d1, d2)
    '''
    d1 = (1.0 / (self.sigma * np.sqrt(self.t)) * (math.log(self.s / self.k)
                    + (self.r + self.sigma ** 2 / 2) * self.t))
    d2 = (1.0 / (self.sigma * np.sqrt(self.t)) * (math.log(self.s / self.k)
                    + (self.r - self.sigma ** 2 / 2) * self.t))
    return (d1, d2)

  def gamma(self):
    ''' Gamma is the second derivative of the option's
        value relative to the value of the asset.
        It is the same for both calls and puts.
        @rtype: float
        @return: gamma'''
    return norm.pdf(self.d[0]) / (self.s * self.sigma * np.sqrt(self.t))

  def imp_vol(self, C0):
    ''' Calculate the implied volatility of a call option,
        where sigma is interpretered as a best guess.
        Updates sigma as a side effect.
        @type it: int
        @param it: Number of iterations to loop for.
        @rtype: float
        @return: Implied volatility.'''
    for i in range(128):
      self.sigma -= (self.euro_call() - C0) / self.vega()
      self.d = self.factors()
    return self.sigma

  def partials_call(self):
    ''' Calculates the partial derivatives from the Black-Scholes
        for a call option.
        @rtype: (float, float, float, float, float)
        @return: (Delta, Gamma, Vega, Theta, Rho)'''
    Delta = norm.cdf(self.d[0])
    Theta = (-self.s * norm.pdf(self.d[0]) * self.sigma / (2 * np.sqrt(self.t))
           - self.r * self.k * math.exp(-self.r * self.t) * norm.cdf(self.d[1]))
    Rho = self.k * self.t * np.exp(-self.r * self.t) * norm.cdf(self.d[1])
    return (Delta, self.gamma(), self.vega(), Theta, Rho)

  def partials_put(self):
    ''' Calculates the partial derivatives from the Black-Scholes
        for a put option.
        @rtype: (float, float, float, float, float)
        @return: (Delta, Gamma, Vega, Theta, Rho)'''
    Delta = norm.cdf(self.d[0]) - 1
    Theta = (-self.s * norm.pdf(self.d[0]) * self.sigma / (2 * np.sqrt(self.t))+
      self.r * self.k * math.exp(-self.r * self.t) * norm.cdf(-self.d[1]))
    Rho = -self.k * self.t * np.exp(-self.r * self.t) * norm.cdf(-self.d[1])
    return (Delta, self.gamma(), self.vega(), Theta, Rho)

  def vega(self):
    ''' Returns vega, which is the derivative of the
        option value with respect to the asset's volatility.
        It is the same for both calls and puts.
        @rtype: float
        @return: vega'''
    return self.s * norm.pdf(self.d[0]) * np.sqrt(self.t)

