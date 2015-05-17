#!/usr/bin/env python
'''
  Notes from reading the book "Python for Finance"
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

def float_eq(f,s, unc):
  ''' Determine if two floats are equal at a given uncertainty.
      @param f: First float.
      @param s: Second float.
      @param unc: The uncertainty.
      @return: Whether f and s are within that range of each other.
  '''
  return f + unc > s and s + unc > f

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

def price_plot(stk):
  '''Plot the closing price and volatility of a stock,
     then hang until user input.
     @param stk: The stock's ticker symbol e.g. GOOG.
     @return: The dataframe used to make the plot.'''
  info = web.DataReader(stk, data_source='google',
                  start='3/14/2009', end='4/14/2014')
  info['Log_Ret'] = np.log(info['Close'] / info['Close'].shift(1))
  info['Volatility'] = pd.rolling_std(info['Log_Ret'],
                          window=252) * np.sqrt(252)
  info[['Close', 'Volatility']].plot(subplots=True, color='blue',
                                  figsize=(8, 6))
  plt.show()
  return info

def main():
  ''' Main '''
  price_plot('GOOG')

if __name__ == '__main__':
  main()
