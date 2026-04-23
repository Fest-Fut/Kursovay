#!/usr/bin/python

import sys
sys.path.append("./magexp/playground/python")
import os

# If there is no magexp directory (actually, the above path), this will fail!
import magexp4 as m4

import numpy as np
from pathlib import Path
import datetime


SMDIR = "magexp"


def _step1(fh, mode):
  """
  Run first step: calculate quasi-period intervals for the first component.
  """

  match mode:
    case 're':
      qprR1 = funcQPeriodStat(eRpsi1, 10, 100)

      fname = fh("qperiod_eRpsi1.dat")
      np.savetxt(fname, qprR1)

      fname = fh("qperiod_eRpsi1.npy")
      np.save(fname, qprR1)

    case 'im':
      qprI1 = funcQPeriodStat(eIpsi1, 10, 100)

      fname = fh("qperiod_eIpsi1.dat")
      np.savetxt(fname, qprI1)

      fname = fh("qperiod_eIpsi1.npy")
      np.save(fname, qprI1)

    case _:
      print(f"[ERROR:_step1] unsupported mode: '{mode}'")


def _step2(fh, mode, idx):
  """
  Run routine to calculate then number of zeroes for the second component in an
  interval.

  The data file with array of intervals must be located under 'OUTPUT' dir and
  has name 'qperiod_eR|Ipsi1.npy' (only binary format is supported).
  """

  match mode:
    case "re":
      datO = fh("qperiod_eRpsi1.npy")
      NAME = "RE-PSI2"
      _fh = eRpsi2
      odat = fh(f"{idx}kolNull_eRpsi2.dat")

    case "im":
      datO = fh("qperiod_eIpsi1.npy")
      NAME = "IM-PSI2"
      _fh = eIpsi2
      odat = fh(f"{idx}kolNull_eIpsi2.dat")

    case _:
      print(f"[ERROR:_step2] unsupported mode: '{mode}'")
      return

  with open(datO, 'rb') as f:
    _dat = np.load(f)
    _ldt = len(_dat)

    if Path(odat).exists():
      _dt = np.loadtxt(odat)
      _idx = int(_dt[-1][0])
      if _idx + 2 > _ldt:
        print(f"[WARNING] everything seems already be calculated: last item {_idx}, total number of elements {_ldt}")
        return
      data = _dat[_idx+2::2]
    else:
      data = _dat

    funMasivNullInRangesQPeriod(_fh, data, 10, NAME, odat)


def _step3(fh, mode, idx):
  """
  Run routine to calculate the number of zeroes for the third component in an
  interval.

  The data file with array of intervals must be located under 'OUTPUT' dir and
  has name 'qperiod_eR|Ipsi1.npy' (only binary format is supported).
  """

  match mode:
    case "re":
      datO = fh("qperiod_eRpsi1.npy")
      NAME = "RE-PSI3"
      _fh = eRpsi3
      odat = fh(f"{idx}kolNull_eRpsi3.dat")

    case "im":
      datO = fh("qperiod_eIpsi1.npy")
      NAME = "IM-PSI3"
      _fh = eIpsi3
      odat = fh(f"{idx}kolNull_eIpsi3.dat")

    case _:
      print(f"[ERROR:_step3] unsupported mode: '{mode}'")
      return

  with open(datO, 'rb') as f:
    _dat = np.load(f)
    _ldt = len(_dat)

    if Path(odat).exists():
      _dt = np.loadtxt(odat)
      _idx = int(_dt[-1][0])
      if _idx + 2 > _ldt:
        print(f"[WARNING] everything seems already be calculated: last item {_idx}, total number of elements {_ldt}")
        return
      data = _dat[_idx+2::2]
    else:
      data = _dat

    funMasivNullInRangesQPeriod(_fh, data, 10, NAME, odat)



def main(args):
  """
  'Main' function.
  """

  if len(args) != 3:
    print("[ERROR] script expects two parameters: mode and 'index' (odd/even).")
    sys.exit(1)

  os.chdir(SMDIR)
  if not m4.prepareBinDir():
    sys.exit(f"Failed to prepare bin directory of '{SMDIR}', see message above.")

  os.chdir("./bin")

  outdir = "../../data/magexp"

  def filn(name):
    return f"{outdir}/{name}"

  mode = args[1]
  idx = int(args[2]) % 2

  match mode:
    case 'psi1':
      _step1(filn, "re")
      _step1(filn, "im")
    case 're-psi1':
      _step1(filn, 're')
    case 'im-psi1':
      _step1(filn, 'im')
    case 'psi2':
      _step2(filn, "re", idx)
      _step2(filn, "im", idx)
    case 're-psi2':
      _step2(filn, 're', idx)
    case 'im-psi2':
      _step2(filn, 'im', idx)
    case 'psi3':
      _step3(filn, "re", idx)
      _step3(filn, "im", idx)
    case 're-psi3':
      _step3(filn, 're', idx)
    case 'im-psi3':
      _step3(filn, 'im', idx)
    case _:
      print(f"[ERROR] unrecognized mode: '{mode}'")


def eRpsi1(x):
  """
  Wrapper for real part of first component
  """

  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(rpsi1)


def eIpsi1(x):
  """
  Wrapper for imaginary part of first component
  """

  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(ipsi1)


def eRpsi2(x):
  """
  Wrapper for real part of second component
  """

  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(rpsi2)


def eIpsi2(x):
  """
  Wrapper for imaginary part of second component
  """

  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(ipsi2)


def eRpsi3(x):
  """
  Wrapper for real part of third component
  """

  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(rpsi3)


def eIpsi3(x):
  """
  Wrapper for imaginary part of third component
  """

  prob, _, _, rpsi1, ipsi1, rpsi2, ipsi2, rpsi3, ipsi3, err = m4.sol(x)
  return float(ipsi3)



def funcNullRanges(fn, x1, x2, n):
  """
  Определяем с заданной «точностью» подынтервалы, где зануляется функция.

  Возвращаем массив подынтервалов.

  Функция проводит «грубую» оценку числа «нулевых» интервалов (где зануляется
  функция).
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
  Определяем до заданной предельной точности подынтервалы, где есть только один
  нуль.

  Возвращаем границы интервала.
  """

  tt = []
  imx = 6
  n1 = n2 = -1
  _name="INFO:funcNullRangesStab"

  for i in range(imx):
    nx = n*(4 + i)**i + 1
    print(f"[${_name}] {nx=}")
    tt = funcNullRanges(fn, x1, x2, nx)
    n1 = n2
    n2 = len(tt)
    if n1 == n2:
      break

  return tt


def funcTochnNull(fn, x1, x2, eps):
  """
  Определяем с указанной точностью точное положение нуля.

  Возвращаем границы интервала.
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
  _name="ERROR:funcQPRangeEnvelop"
  _nm="DEBUG:funcQPRangeEnvelop"

  tt = np.array(funcNullRangesStab(fn, x1, x2, 10))
  ttmin = np.min(np.abs(tt[:,0] - x0))
  i0 = np.where( np.abs(tt[:,0] - x0) == ttmin)[0][0]
  if i0 > len(tt) -1:
    print(f"[{_name}] the smallest is the last one!")
    return True
  """
  print(f"[{_nm}] {i0=}, {tt=}, tt[:,0] - x0 = {tt[:,0] - x0}")
  """
  xl = tt[i0 - 1]
  #  xc = tt[i0]
  xr = tt[i0 + 1]
  xl = funcTochnNull(fn, xl[0], xl[1], eps)
  xr = funcTochnNull(fn, xr[0], xr[1], eps)

  return [xl[0], xr[1]]


def funcLastQPeriod(fn, n):
  """
  Найти положение крайнего правого нуля и вернуть интервал его содержащий.

  Пояснение:

  Из предварительного анализа известно, что на правом конце есть последний
  интервал с нулём, который не доходит до правой границы. Задача фукнции —
  определить положение этого нуля и его «изолирующий» интервал.
  """

  x0 = 0.50
  x2 = 0.8
  tt = []
  y1 = y2 = y3 = 0
  eps = 1e-8
  _name="INFO:funcLastQPeriod"

  tt = funcNullRangesStab(fn, x0, x2, n)
  k = len(tt)-1
  print(f"[{_name}] seredina funcLastQPeriod")
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
  _name="INFO:funcQPeriodStat"
  _nm="WARNING:funcQPeriodStat"
  _nnm="DEBUG:funcQPeriodStat"

  endt = funcLastQPeriod(fn, nSeed)
  print(f"[{_name}] Konec funcLastQPeriod")
  dx = endt[2][0] - endt[0][0]
  tabQPeriod.append([endt[0][0], endt[2][0]])
  for i in range(nSteps+1):
    t = tabQPeriod[i][0]
    if t - 3.*dx/2 < x0:
      print(f"[{_nm}] reached the lower bound '{x0}' on step '{i}'")
      return tabQPeriod
    x00 = t - 3*dx/4

    """
    print(f"[{_nnm}] {i=}, t - 1.5dx = {t-3/2*dx}, {x00=}, {t=}, {dx=}")
    """
    print(f"[_name] {i=}")
    gran1 = funcQPRangeEnvelop(fn, x00, x00-dx, x00+dx)
    dx = np.abs(gran1[1] - gran1[0])
    tabQPeriod.append(gran1)

  return tabQPeriod


def funMasivNullInRangesQPeriod(fn, qpr, n, name, odat):
  """
  Подсчитывает количество переходов через нуль данной функции на заданных
  интервалах.

  Результаты сразу записываем в файл.
  """

  _nm=f"funMasivNullInRagesQPeriod:'{name}'"

  for i in range(len(qpr)):
    t = datetime.datetime.now()
    print(f"[{_nm}]: {t} -- {i}/{len(qpr)} -- ({qpr[i][0]}, {qpr[i][1]})")
    _nm = len(funcNullRangesStab(fn, qpr[i][0], qpr[i][1], n))
    with open(odat, "a") as f:
      print(f"{i:d}\t{qpr[i][0]:.18e}\t{qpr[i][1]:.18e}\t{_nm:d}", file=f, flush = True)

  return


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")
