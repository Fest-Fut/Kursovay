#!/usr/bin/python

import sys
sys.path.append("./magexp/playground/python")
import os

# If there is no magexp directory (actually, the above path), this will fail!
import magexp4 as m4

import numpy as np

SMDIR = "magexp"


def _step1(fh):
  """
  Run first step: calculate quasi-period intervals for the first component.
  """

  qprR1 = funcQPeriodStat(eRpsi1, 10, 100)
  qprI1 = funcQPeriodStat(eIpsi1, 10, 100)

  fname = fh("qperiod_eRpsi1.dat")
  np.savetxt(fname, qprR1)

  fname = fh("qperiod_eRpsi1.npy")
  np.save(fname, qprR1)

  fname = fh("qperiod_eIpsi1.dat")
  np.savetxt(fname, qprI1)

  fname = fh("qperiod_eIpsi1.npy")
  np.save(fname, qprI1)


def _step2(fh):
  """
  Calculate number of zeroes for the second component in given interval.

  The array of intervals must be under 'OUTPUT' dir and has name
  'qperiod_eR|Ipsi1.npy' (only binary format is supported).
  """

  datR = fh("qperiod_eRpsi1.npy")
  datI = fh("qperiod_eIpsi1.npy")

  with open(datR, 'rb') as f:
    data = np.load(f)
    knR2 = funMasivNullInRangesQPeriod(eRpsi2, data, 10)

    odat = fh("kolNull_eRpsi2.dat")
    np.savetxt(odat, knR2)

    odat = fh("kolNull_eRpsi2.npy")
    np.save(odat, knR2)

  with open(datI, 'rb') as f:
    data = np.load(f)
    knI2 = funMasivNullInRangesQPeriod(eIpsi2, data, 10)

    odat = fh("kolNull_eIpsi2.dat")
    np.savetxt(odat, knI2)

    odat = fh("kolNull_eIpsi2.npy")
    np.save(odat, knI2)


def _step3(fh):
  """
  Calculate number of zeroes for the third component in given interval.

  The array of intervals must be under 'OUTPUT' dir and has name
  'qperiod_eR|Ipsi1.npy' (only binary format is supported).
  """

  datR = fh("qperiod_eRpsi1.npy")
  datI = fh("qperiod_eIpsi1.npy")

  with open(datR, 'rb') as f:
    data = np.load(f)
    knR3 = funMasivNullInRangesQPeriod(eRpsi3, data, 10)

    odat = fh("kolNull_eRpsi3.dat")
    np.savetxt(odat, knR3)

    odat = fh("kolNull_eRpsi3.npy")
    np.save(odat, knR3)

  with open(datI, 'rb') as f:
    data = np.load(f)
    knI3 = funMasivNullInRangesQPeriod(eIpsi3, data, 10)

    odat = fh("kolNull_eIpsi3.dat")
    np.savetxt(odat, knI3)

    odat = fh("kolNull_eIpsi3.npy")
    np.save(odat, knI3)



def main(args):
  """
  'Main' function.
  """

  os.chdir(SMDIR)
  if not m4.prepareBinDir():
    sys.exit(f"Failed to prepare bin directory of '{SMDIR}', see message above.")

  os.chdir("./bin")

  outdir = "../../data/magexp"

  def filn(name):
    return f"{outdir}/{name}"

  match args:
    case 're-psi1' | 'im-psi1':
      _step1(filn)
    case 're-psi2' | 'im-psi2':
      _step2(filn)
    case 're-psi3' | 'im-psi3':
      _step3(filn)
    case _:
      print(f"[ERROR] unrecognized parameter: '{args}'")


def eRpsi1(x):
  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(rpsi1)


def eIpsi1(x):
  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(ipsi1)


def eRpsi2(x):
  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(rpsi2)


def eIpsi2(x):
  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(ipsi2)


def eRpsi3(x):
  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(rpsi3)


def eIpsi3(x):
  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(ipsi3)



def funcNullRanges(fn, x1, x2, n):
  """
  Определяем области где есть нули.
  """

  t = []
  xx = np.linspace(x1,x2,n)
  mm = [fn(x) for x in xx]
  for i in range(len(xx)-1):
    """
    print(f"{i=}")
    """
    if mm[i]*mm[i+1] < 0:
      t.append([xx[i],xx[i+1]])

  return t

def funcNullRangesStab(fn, x1, x2, n):
  """
  Определяем области где есть один нуль.
  """

  tt = []
  imx = 6
  n1 = n2 = -1

  for i in range(imx):
    nx = n*(4 + i)**i
    print(f"[INFO:funcNullRangesStab] {nx=}")
    tt = funcNullRanges(fn, x1, x2, nx)
    n1 = n2
    n2 = len(tt)
    if n1 == n2:
      break

  return tt


def funcTochnNull(fn, x1, x2, eps):
  """
  Определяем точные координаты нулей
  """

  t1 = x1
  t2 = x2
  while (t2-t1) > eps:
    if fn(t1)*fn((t1+t2)/2) < 0:
      t2 = (t1+t2)/2
    else:
      t1 = (t1+t2)/2

  return [t1,t2]


def funcQPRangeEnvelop(fn, x0, x1, x2):
  """
  Ищет ближайший ноль к x0 в диапозоне [x1,x2] и выдает предыдущий и последующие нули
  """

  i0 = 0
  tt = []
  xl = []
  #  xc = []
  xr = []
  eps = 1e-8

  tt = np.array(funcNullRangesStab(fn, x1, x2, 10))
  ttmin = np.min(np.abs(tt[:,0] - x0))
  i0 = np.where( np.abs(tt[:,0] - x0) == ttmin)[0][0]
  if i0 > len(tt) -1:
    print("[ERROR] 'funcQPRangeEnvelop': the smallest is the last one!")
    return True
  """
  print(f"[DEBUG:funcQPRangeEnvelop] {i0=}, {tt=}, tt[:,0] - x0 = {tt[:,0] - x0}")
  """
  xl = tt[i0 - 1]
  #  xc = tt[i0]
  xr = tt[i0 + 1]
  xl = funcTochnNull(fn, xl[0], xl[1], eps)
  xr = funcTochnNull(fn, xr[0], xr[1], eps)

  return [xl[0], xr[1]]


def funcLastQPeriod(fn, n):
  """
  Вернуть крайний правый интервал с нулём.

  Из предварительного анализа известно, что на правом конце есть последний интервал с нулём, который не доходит до правой границы. Задача фукнции — определить положение этого нуля и его           «изолирующий» интервал.
  """

  x0 = 0.50
  x2 = 0.8
  tt = []
  y1 = y2 = y3 = 0
  eps = 1e-8

  tt = funcNullRangesStab(fn, x0, x2, n)
  k = len(tt)-1
  print("[INFO:funcLastQPeriod] seredina funcLastQPeriod")
  y1 = funcTochnNull(fn, tt[k-2][0], tt[k-2][1], eps)
  y2 = funcTochnNull(fn, tt[k-1][0], tt[k-1][1], eps)
  y3 = funcTochnNull(fn, tt[k][0], tt[k][1], eps)

  return [y1, y2, y3]


def funcQPeriodStat(fn, nSeed, nSteps):
  """
  Обязательная документация к функции.
  """

  tabQPeriod = []
  endt = []
  x00 = 0
  x0 = 0.11
  gran1 = []
  dx = 0
  t = 0

  endt = funcLastQPeriod(fn, nSeed)
  print("[INFO:funcQPeriodStat] Konec funcLastQPeriod")
  dx = endt[2][0] - endt[0][0]
  tabQPeriod.append([endt[0][0], endt[2][0]])
  for i in range(nSteps+1):
    t = tabQPeriod[i][0]
    if t - 3.*dx/2 < x0:
      print(f"[WARNING] reached the lower bound '{x0}' on step '{i}'")
      return tabQPeriod
    x00 = t - 3*dx/4

    """"
    print(f"[DEBUG:funcQPeriodStat] {i=}, t - 1.5dx = {t-3/2*dx}, {x00=}, {t=}, {dx=}")
    """
    print(f"[INFO:funcQPeriodStat] {i=}")
    gran1 = funcQPRangeEnvelop(fn, x00, x00-dx, x00+dx)
    dx = np.abs(gran1[1] - gran1[0])
    tabQPeriod.append(gran1)

  return tabQPeriod


def funMasivNullInRangesQPeriod(fn, qpr, n):
  kolnull = []
  for i in range(len(qpr)):
     kolnull.append(len(funcNullRangesStab(fn, qpr[i][0], qpr[i][1], n)))
  return(kolnull)


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")
