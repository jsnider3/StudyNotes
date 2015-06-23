#!/usr/bin/env python
import pandas as pd
import pandas.io.data as web

def discretize(ls):
  '''quanta is e from equation 5.
     The rest implements equation 6.'''
  (mn, mx) = (min(ls), max(ls))
  quanta = (mx - mn) / 256
  ls = [int((i - mn) / quanta) for i in ls]
  return ls

def borne_discretize(ls):
  ''' Quick-and-dirty implementation
      of borne.'''
  q = sorted(ls)
  step = len(ls) // 245
  cutoffs = (q[-1::-step])[::-1]
  def borne_helper(n):
    if n < cutoffs[0]:
      return 0
    elif n > cutoffs[-1]:
      return 258
    for i in range(1, len(cutoffs)):
      if cutoffs[i] > n >= cutoffs[i-1]:
        return i
    return 257
  print(step, len(ls))
  print(len(cutoffs))
  return [borne_helper(n) for n in ls]
  
def get_openings():
  sp500 = web.DataReader('^GSPC', data_source='yahoo',
                     start='1/1/2000', end='4/14/2014')
  return sp500['Open'].tolist()

def main():
  opens = get_openings()
  discrete = discretize(opens)
  print(borne_discretize(opens))

if __name__ == "__main__":
  main()
