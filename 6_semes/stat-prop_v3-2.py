#!/usr/bin/python

#  import numpy as np
import sys
import matplotlib.pyplot as plt
from pathlib import Path

import dnk_stat as ds
from dnk_load import loadData2 as loadData


plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = (
  r"\usepackage[conf=matplotlib]{isu-th3}"
)


def main(args):
  """
  'Main' function.
  """

  if len(args) < 2:
    sys.exit("Pass at least one argument --- file name of form 'qperiod_I|Rpsi1.dat'.")

  rxi, ixi, rwd, iwd, rpsi2c, ipsi2c, rpsi3c, ipsi3c = loadData(args[1])

  mrk = "figs"
  outdir = Path(mrk)
  outdir.mkdir(parents = True, exist_ok = True)

  # ############################################################################

  ds.plot_pair(rxi, rwd, ixi, iwd, laby1 = r'\(T\)',
               leg1 = r'\(\Re{\psi_{1}}\)', leg2 = r'\(\Im{\psi_{1}}\)',
               tit = r'Quasi-period of \(\psi_{1}\)',
               name = f"{mrk}/RIpsi1_width")

  ds.plot_pair(rxi, rwd, ixi, iwd, laby1 = r'\(T\)',
               leg1 = r'\(\Re{\psi_{1}}\)', leg2 = r'\(\Im{\psi_{1}}\)',
               tit = r'Квазипериод \(\psi_{1}\)',
               name = f"{mrk}/RIpsi1_width-ru")

  ds.plot_l2pair(rxi, rwd, ixi, iwd, laby1 = r'\(T\)',
                 leg1 = r'\(\Re{\psi_{1}}\)', leg2 = r'\(\Im{\psi_{1}}\)',
                 tit = r'Quasi-period of \(\psi_{1}\)',
                 name = f"{mrk}/RIpsi1_logwidth")

  ds.plot_l2pair(rxi, rwd, ixi, iwd, laby1 = r'\(T\)',
                 leg1 = r'\(\Re{\psi_{1}}\)', leg2 = r'\(\Im{\psi_{1}}\)',
                 tit = r'Квазипериод \(\psi_{1}\)',
                 name = f"{mrk}/RIpsi1_logwidth-ru")

  # ############################################################################

  ds.plot_pair(rxi, rpsi2c, ixi, ipsi2c, laby1 = r'\(N_{\text{zero}}\)',
               leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
               tit = r'Number of zero transitions for \(\psi_{2}\)',
               name = f"{mrk}/RIpsi2_trans")

  ds.plot_pair(rxi, rpsi2c, ixi, ipsi2c, laby1 = r'\(N_{\text{zero}}\)',
               leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
               tit = r'Число переходов нуля для \(\psi_{2}\)',
               name = f"{mrk}/RIpsi2_trans-ru")

  # ############################################################################

  # ### Due to computational costs for psi3 we compute data for not whole psi1.
  sz = len(rpsi3c)
  rxi_r = rxi[-sz:]
  ixi_r = ixi[-sz:]

  ds.plot_pair(rxi_r, rpsi3c, ixi_r, ipsi3c, laby1 = r'\(N_{\text{zero}}\)',
               leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
               tit = r'Number of zero transitions for \(\psi_{3}\)',
               name = f"{mrk}/RIpsi3_trans")

  ds.plot_pair(rxi_r, rpsi3c, ixi_r, ipsi3c, laby1 = r'\(N_{\text{zero}}\)',
               leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
               tit = r'Число переходов нуля для \(\psi_{3}\)',
               name = f"{mrk}/RIpsi3_trans-ru")

  # ############################################################################

  ds.plot_pair(rxi, rpsi2c/rwd, ixi, ipsi2c/iwd, laby1 = r'\(N_{\text{zero}}/T\)',
               leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
               tit = r'Number of transitions per quasi-period for \(\psi_{2}\)',
               name = f"{mrk}/RIpsi2_rel-trans")

  ds.plot_pair(rxi, rpsi2c/rwd, ixi, ipsi2c/iwd, laby1 = r'\(N_{\text{zero}}/T\)',
               leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
               tit = r'Число переходов нуля на квазипериод для \(\psi_{2}\)',
               name = f"{mrk}/RIpsi2_rel-trans-ru")

  ds.plot_l2pair(rxi, rpsi2c/rwd, ixi, ipsi2c/iwd, laby1 = r'\(N_{\text{zero}}/T\)',
                 leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
                 tit = r'Number of transitions per quasi-period for \(\psi_{2}\)',
                 name = f"{mrk}/RIpsi2_logrel-trans")

  ds.plot_l2pair(rxi, rpsi2c/rwd, ixi, ipsi2c/iwd, laby1 = r'\(N_{\text{zero}}/T\)',
                 leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
                 tit = r'Число переходов нуля на квазипериод для \(\psi_{2}\)',
                 name = f"{mrk}/RIpsi2_logrel-trans-ru")

  ds.plot_l2pair(rxi, rpsi2c/rwd, ixi, ipsi2c/iwd, cutoff = 1e4,
                 laby1 = r'\(N_{\text{zero}}/T\)',
                 leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
                 tit = r'Number of transitions per quasi-period for \(\psi_{2}\)',
                 name = f"{mrk}/RIpsi2_logrel-transCUT")

  ds.plot_l2pair(rxi, rpsi2c/rwd, ixi, ipsi2c/iwd, cutoff = 1e4,
                 laby1 = r'\(N_{\text{zero}}/T\)',
                 leg1 = r'\(\Re{\psi_{2}}\)', leg2 = r'\(\Im{\psi_{2}}\)',
                 tit = r'Число переходов нуля на квазипериод для \(\psi_{2}\)',
                 name = f"{mrk}/RIpsi2_logrel-transCUT-ru")

  # ############################################################################
  rwd_r = rwd[-sz:]
  iwd_r = iwd[-sz:]

  ds.plot_pair(rxi_r, rpsi3c/rwd_r, ixi_r, ipsi3c/iwd_r,
               laby1 = r'\(N_{\text{zero}}\)',
               leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
               tit = r'Number of transitions per quasi-period for \(\psi_{3}\)',
               name = f"{mrk}/RIpsi3_rel-trans")

  ds.plot_pair(rxi_r, rpsi3c/rwd_r, ixi_r, ipsi3c/iwd_r,
               laby1 = r'\(N_{\text{zero}}\)',
               leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
               tit = r'Число переходов нуля на квазипериод для \(\psi_{3}\)',
               name = f"{mrk}/RIpsi3_rel-trans-ru")

  ds.plot_l2pair(rxi_r, rpsi3c/rwd_r, ixi_r, ipsi3c/iwd_r, laby1 = r'\(N_{\text{zero}}\)',
                 leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
                 tit = r'Number of transitions per quasi-period for \(\psi_{3}\)',
                 name = f"{mrk}/RIpsi3_logrel-trans")

  ds.plot_l2pair(rxi_r, rpsi3c/rwd_r, ixi_r, ipsi3c/iwd_r, laby1 = r'\(N_{\text{zero}}\)',
                 leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
                 tit = r'Число переходов нуля на квазипериод для \(\psi_{3}\)',
                 name = f"{mrk}/RIpsi3_logrel-trans-ru")

  ds.plot_l2pair(rxi_r, rpsi3c/rwd_r, ixi_r, ipsi3c/iwd_r, cutoff = 1e6,
                 laby1 = r'\(N_{\text{zero}}\)',
                 leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
                 tit = r'Number of transitions per quasi-period for \(\psi_{3}\)',
                 name = f"{mrk}/RIpsi3_logrel-transCUT")

  ds.plot_l2pair(rxi_r, rpsi3c/rwd_r, ixi_r, ipsi3c/iwd_r, cutoff = 1e6,
                 laby1 = r'\(N_{\text{zero}}\)',
                 leg1 = r'\(\Re{\psi_{3}}\)', leg2 = r'\(\Im{\psi_{3}}\)',
                 tit = r'Число переходов нуля на квазипериод для \(\psi_{3}\)',
                 name = f"{mrk}/RIpsi3_logrel-transCUT-ru")


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user.")

# vim: fdm=indent:
