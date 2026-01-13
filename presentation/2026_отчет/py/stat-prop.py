#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = (
    r"\usepackage[conf=matplotlib]{isu-th3}"
)


def loadData(file):
  """
  Load data from given file.

  The file must contains exactly 7 columns, separated by space(s).
  """

  global xi, rw, rp2, rp3, iw, ip2, ip3

  xi, rw, rp2, rp3, iw, ip2, ip3 = np.loadtxt(file, unpack = True)


def plot_single(x, y, labx = r'\(\xi\)', laby = r'WIDTH', tit = 'NONE', name = "DEFAULT"):
  """
  Plot simple graph, x vs y.

  Pass title, axes labels, title and name to save graph as PDF.
  """

  fig, ax = plt.subplots(layout='constrained')

  ax.plot(x, y, r'.-')
  ax.grid(True)

  ax.set_xlabel(labx)
  ax.set_ylabel(laby)
  
  fig.suptitle(tit)

  fig.savefig(f"{name}.pdf")


def plot_both(x, y1, y2, labx = r'\(\xi\)', laby = r'WIDTH', leg1 = "LEG1", leg2 = "LEG2", tit = 'NONE', name = "DEFAULT"):
  """
  Plot two graphs with the same x: x vs y1 and x vs y2.

  Pass title, axes labels, title, legend and name to save graph as PDF.
  """

  fig, ax = plt.subplots(layout='constrained')

  ax.plot(x, y1, r'.-', x, y2, r'-.')
  ax.grid(True)

  ax.legend([leg1, leg2])

  ax.set_xlabel(labx)
  ax.set_ylabel(laby)
  
  fig.suptitle(tit)

  fig.savefig(f"{name}.pdf")


loadData("DOPRI_p3_tabl.dat")

plot_single(xi, rw, laby = r'\(T_{\Re}\)', tit = r'Quasi-period of real part of \(\Psi_{1}\)', name = "rwidth")
plot_single(xi, iw, laby = r'\(T_{\Im}\)', tit = r'Quasi-period of imaginary part of \(\Psi_{1}\)', name = "iwidth")

plot_single(xi, rw, laby = r'\(T_{\Re}\)', tit = r'Квазипериод реальной части \(\Psi_{1}\)', name = "rwidth-ru")
plot_single(xi, iw, laby = r'\(T_{\Im}\)', tit = r'Квазипериод мнимой части \(\Psi_{1}\)', name = "iwidth-ru")

plot_both(xi, rw, iw, laby = r'\(\Delta\xi\)', leg1 = r"Re", leg2 = r"Im", tit = r'Quasi-period for both parts of \(\Psi_{1}\)', name = "ri-widths")

plot_both(xi, rw, iw, laby = r'\(\Delta\xi\)', leg1 = r"Re", leg2 = r"Im", tit = r'Квазипериоды реальной и мнимой частей \(\Psi_{1}\)', name = "ri-widths-ru")

plot_both(xi, rp2, ip2, laby = r'\(N\)', leg1 = r"Re", leg2 = r"Im", tit = r'Number of zero transitions for \(\Psi_{2}\)', name = "psi2-trans")
plot_both(xi, rp3, ip3, laby = r'\(N\)', leg1 = r"Re", leg2 = r"Im", tit = r'Number of zero transitions for \(\Psi_{3}\)', name = "psi3-trans")

plot_both(xi, rp2, ip2, laby = r'\(N\)', leg1 = r"Re", leg2 = r"Im", tit = r'Число переходов нуля для \(\Psi_{2}\)', name = "psi2-trans-ru")
plot_both(xi, rp3, ip3, laby = r'\(N\)', leg1 = r"Re", leg2 = r"Im", tit = r'Число переходов нуля для \(\Psi_{3}\)', name = "psi3-trans-ru")

plot_both(xi, rp2/rw, ip2/iw, laby = r'\(N/T\)', leg1 = r"Re", leg2 = r"Im", tit = r'Number of transitions per length for \(\Psi_{2}\)', name = "psi2-rel-trans")
plot_both(xi, rp3/rw, ip3/iw, laby = r'\(N/T\)', leg1 = r"Re", leg2 = r"Im", tit = r'Number of transitions per length for \(\Psi_{3}\)', name = "psi3-rel-trans")

plot_both(xi, rp2/rw, ip2/iw, laby = r'\(N/T\)', leg1 = r"Re", leg2 = r"Im", tit = r'Число переходов нуля на квазипериод для \(\Psi_{2}\)', name = "psi2-rel-trans-ru")
plot_both(xi, rp3/rw, ip3/iw, laby = r'\(N/T\)', leg1 = r"Re", leg2 = r"Im", tit = r'Число переходов нуля на квазипериод для \(\Psi_{3}\)', name = "psi3-rel-trans-ru")
