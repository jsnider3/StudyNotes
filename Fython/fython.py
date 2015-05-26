#!/usr/bin/env python
'''
  Notes from reading the book "Python for Finance"
  by Yves Hilpisch.
  @see: http://shop.oreilly.com/product/0636920032441.do

  @author: Joshua Snider
  @date: 2015/05/17
  @license: GNU Public License v3.0
'''

import datetime
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas.io.data as web
import scipy as sp
import scipy.stats 
import time

def annualized_return(stk, begin, stop):
  '''Look up the closing price and calculate 
     volatility of a stock.
     @param stk: The stock's ticker symbol e.g. "GOOG".
     @type stk: str
     @type start: start date
     @type end: end date
     @return: The annualized return of the stock in that time.'''
  info = web.DataReader(stk, data_source='google',
                  start=begin, end=stop)
  starttime = datetime.datetime(*time.strptime(begin,"%m/%d/%Y")[:6])
  endtime = datetime.datetime(*time.strptime(stop, "%m/%d/%Y")[:6])
  delta = endtime - starttime
  Y = delta.days / 365.25
  S0 = info.head()['Open'][0]
  ST = info.tail()['Open'][-1]
  return (ST/S0) ** (1/Y) - 1

def float_eq(f,s, unc):
  ''' Determine if two floats are equal at a given uncertainty.
      @param f: First float.
      @param s: Second float.
      @param unc: The uncertainty.
      @type f: float
      @type s: float
      @type unc: float
      @return: Whether f and s are within that range of each other.
      @rtype: bool
  '''
  return f + unc > s and s + unc > f

def monte_carlo_euro(s, k, t, r, sigma):
  '''
     Calculate the value of a European call option
     using Monte Carlo methods. No dividends.
     @param s: initial stock price
     @param k: strike price
     @param t: time to maturity
     @param r: Constant, riskless short rate
     @param sigma: Constant volatility
     @return: A value for an option with the given parameters.
     @rtype: float
  ''' 
  z = np.random.standard_normal(100000)
  st = s * np.exp((r - 0.5 * sigma ** 2) * t + sigma * np.sqrt(t) * z)
  ht = np.maximum(st - k, 0)
  return np.exp(-r * t) * sum(ht) / 100000

def rolling_vol(stk):
  '''Look up the closing price and calculate 
     volatility of a stock.
     @param stk: The stock's ticker symbol e.g. "GOOG".
     @type stk: str
     @return: The dataframe with closing volatility.'''
  info = web.DataReader(stk, data_source='google',
                  start='3/14/2009', end='4/14/2014')
  info['Log_Ret'] = np.log(info['Close'] / info['Close'].shift(1))
  info['Volatility'] = pd.rolling_std(info['Log_Ret'],
                          window=252) * np.sqrt(252)
  return info

def main():
  ''' Main '''
  price_plot('GOOG')

if __name__ == '__main__':
  main()
