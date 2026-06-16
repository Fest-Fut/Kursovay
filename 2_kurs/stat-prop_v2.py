#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
from pathlib import Path

import dnk_stat as ds
from dnk_load import loadData


plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = (
  r"\usepackage[conf=matplotlib]{isu-th3}"
)


def main(args):
  """
  'Main' function.
  """

  if len(args) < 2:
    sys.exit("Pass at least one argument --- file name of form 'qperiod_I|Rpsi1_1e2|3.dat'.")

  rxi, ixi, rwd, iwd, rpsi2c, ipsi2c, rpsi3c, ipsi3c, mrk = loadData(args[1])

  outdir = Path(mrk)
  outdir.mkdir(parents = True, exist_ok = True)

  ds.plot_single(rxi, rwd, laby = r'\(T_{\Re}\)',
              tit = r'Quasi-period of \(\Re{\psi_{1}}\)',
              name = f"{mrk}/Rpsi1_width")
  ds.plot_single(ixi, iwd, laby = r'\(T_{\Im}\)',
              tit = r'Quasi-period of \(\Im{\psi_{1}}\)',
              name = f"{mrk}/Ipsi1_width")

  ds.plot_single(rxi, rwd, laby = r'\(T_{\Re}\)',
              tit = r'Квазипериод реальной части \(\psi_{1}\)',
              name = f"{mrk}/Rpsi1_width-ru")
  ds.plot_single(ixi, iwd, laby = r'\(T_{\Im}\)',
              tit = r'Квазипериод мнимой части \(\psi_{1}\)',
              name = f"{mrk}/Ipsi1_width-ru")

  # ############################################################################

  ds.plot_single(rxi, rpsi2c, laby = r'\(N_{\text{zero},\Re}\)',
              tit = r'Number of zero transitions for \(\Re{\psi_{2}}\)',
              name = f"{mrk}/Rpsi2_trans")
  ds.plot_single(ixi, ipsi2c, laby = r'\(N_{\text{zero},\Im}\)',
              tit = r'Number of zero transitions for \(\Im{\psi_{2}}\)',
              name = f"{mrk}/Ipsi2_trans")

  ds.plot_single(rxi, rpsi2c, laby = r'\(N_{\text{zero},\Re}\)',
              tit = r'Число переходов нуля для \(\Re{\psi_{2}}\)',
              name = f"{mrk}/Rpsi2_trans-ru")
  ds.plot_single(ixi, ipsi2c, laby = r'\(N_{\text{zero},\Im}\)',
              tit = r'Число переходов нуля для \(\Im{\psi_{2}}\)',
              name = f"{mrk}/Ipsi2_trans-ru")

  # ############################################################################

  ds.plot_single(rxi, rpsi3c, laby = r'\(N_{\text{zero},\Re}\)',
              tit = r'Number of zero transitions for \(\Re{\psi_{3}}\)',
              name = f"{mrk}/Rpsi3_trans")
  ds.plot_single(ixi, ipsi3c, laby = r'\(N_{\text{zero},\Im}\)',
              tit = r'Number of zero transitions for \(\Im{\psi_{3}}\)',
              name = f"{mrk}/Ipsi3_trans")

  ds.plot_single(rxi, rpsi3c, laby = r'\(N_{\text{zero},\Re}\)',
              tit = r'Число переходов нуля для \(\Re{\psi_{3}}\)',
              name = f"{mrk}/Rpsi3_trans-ru")
  ds.plot_single(ixi, ipsi3c, laby = r'\(N_{\text{zero},\Im}\)',
              tit = r'Число переходов нуля для \(\Im{\psi_{3}}\)',
              name = f"{mrk}/Ipsi3_trans-ru")

  # ############################################################################

  ds.plot_single(rxi, rpsi2c/rwd, laby = r'\(N_{\text{zero},\Re}/T\)',
              tit = r'Number of transitions per quasi-period for \(\Re{\psi_{2}}\)',
              name = f"{mrk}/Rpsi2_rel-trans")
  ds.plot_single(ixi, ipsi2c/iwd, laby = r'\(N_{\text{zero},\Im}/T\)',
              tit = r'Number of transitions per quasi-period for \(\Im{\psi_{2}}\)',
              name = f"{mrk}/Ipsi2_rel-trans")

  ds.plot_single(rxi, rpsi2c/rwd, laby = r'\(N_{\text{zero},\Re}/T\)',
              tit = r'Число переходов нуля на квазипериод для \(\Re{\psi_{2}}\)',
              name = f"{mrk}/Rpsi2_rel-trans-ru")
  ds.plot_single(ixi, ipsi2c/iwd, laby = r'\(N_{\text{zero},\Im}/T\)',
              tit = r'Число переходов нуля на квазипериод для \(\Im{\psi_{2}}\)',
              name = f"{mrk}/Ipsi2_rel-trans-ru")

  # ############################################################################

  ds.plot_single(rxi, rpsi3c/rwd, laby = r'\(N_{\text{zero},\Re}/T\)',
              tit = r'Number of transitions per quasi-period for \(\Re{\psi_{3}}\)',
              name = f"{mrk}/Rpsi3_rel-trans")
  ds.plot_single(ixi, ipsi3c/iwd, laby = r'\(N_{\text{zero},\Im}/T\)',
              tit = r'Number of transitions per quasi-period for \(\Im{\psi_{3}}\)',
              name = f"{mrk}/Ipsi3_rel-trans")

  ds.plot_single(rxi, rpsi3c/rwd, laby = r'\(N_{\text{zero},\Re}/T\)',
              tit = r'Число переходов нуля на квазипериод для \(\Re{\psi_{3}}\)',
              name = f"{mrk}/Rpsi3_rel-trans-ru")
  ds.plot_single(ixi, ipsi3c/iwd, laby = r'\(N_{\text{zero},\Im}/T\)',
              tit = r'Число переходов нуля на квазипериод для \(\Im{\psi_{3}}\)',
              name = f"{mrk}/Ipsi3_rel-trans-ru")


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user.")

# vim: fdm=indent:
