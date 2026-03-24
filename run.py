#!/usr/bin/python

import sys
sys.path.append("./magexp/playground/python")
import os

# If there is no magexp directory (actually, the above path), this will fail!
import magexp4 as m4

import numpy as np

SMDIR="magexp"

def main(args):
  """
  'Main' function.
  """

  os.chdir(SMDIR)
  if not m4.prepareBinDir():
    sys.exit(f"Failed to prepare bin directory of '{SMDIR}', see message above.")

  os.chdir("./bin")

  for x in np.linspace(0.5, 0.9, 5):
    prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
    print(f"{x}\t{prob}")
  print(f"{funcTochnNull(eRpsi1, 0.5318181818181819, 0.5363636363636364, 10^-6)}")


def eRpsi1(x):
  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(rpsi1)


def funcNullRanges(fn, x1, x2, n):
  """
  Определяем области где есть нули.
  """

  t = []
  xx = np.linspace(x1,x2,n)
  mm = [fn(x) for x in xx]
  for i in range(len(xx)-1):
    if mm[i]*mm[i+1] < 0:
      t.append([xx[i],xx[i+1]])

  return t

def funcNullRangesStab(fn, x1, x2, n):
  """
  Определяем области где есть один нуль.
  """

  tt = []
  imx=6
  n1 = n2 = -1

  for i in range(imx):
    nx = (n-i)*(4 + i)**i
    print(f"{nx}")
    tt = funcNullRanges(fn, x1, x2, nx)
    n1 = n2
    n2 = len(tt)
    if n1 == n2:
      break

  return tt


def funcTochnNull(fn, x1, x2, eps):
  """
  Документация к функции
  """

  t1 = x1
  t2 = x2
  while (t2-t1) > eps:
    if fn(t1)*fn((t1+t2)/2) < 0:
      t2 = (t1+t2)/2
    else:
      t1 = (t1+t2)/2

  return [t1,t2]


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")
