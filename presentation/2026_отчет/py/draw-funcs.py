#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = (
    r"\usepackage[conf=matplotlib]{isu-th3}"
)

labsy={
  'pr': r'\(\Prob\)',
  'r1': r'\(\Re\Psi_{1}\)',
  'i1': r'\(\Im\Psi_{1}\)',
  'r2': r'\(\Re\Psi_{2}\)',
  'i2': r'\(\Im\Psi_{2}\)',
  'r3': r'\(\Re\Psi_{3}\)',
  'i3': r'\(\Im\Psi_{3}\)',
  'ph1': r'\(\arg{\Psi_{1}}\)',
  'ph2': r'\(\arg{\Psi_{2}}\)',
  'ph3': r'\(\arg{\Psi_{3}}\)',
  'a1': r'\(|\Psi_{1}|^{2}\)',
  'a2': r'\(|\Psi_{2}|^{2}\)',
  'a3': r'\(|\Psi_{3}|^{2}\)',
  'c' : r'\(\sum_{k}|\Psi_{k}|^2-1\)',
  'R_e1' : r'\(\epsilon R_{1}\)',
  'I_e1' : r'\(\epsilon I_{1}\)',
  'R_e2' : r'\(\epsilon R_{2}\)',
  'I_e2' : r'\(\epsilon I_{2}\)',
  'R_e3' : r'\(\epsilon R_{3}\)',
  'I_e3' : r'\(\epsilon I_{3}\)',
  'A_e1' : r'\(\epsilon |\Psi_{1}|^{2}\)',
  'A_e2' : r'\(\epsilon |\Psi_{2}|^{2}\)',
  'A_e3' : r'\(\epsilon |\Psi_{3}|^{2}\)',
  'P_e1' : r'\(\epsilon \arg{\Psi_{1}}\)',
  'P_e2' : r'\(\epsilon \arg{\Psi_{2}}\)',
  'P_e3' : r'\(\epsilon \arg{\Psi_{3}}\)',
  'P_E1' : r'\(\Delta \arg{\Psi_{1}}\)',
  'P_E2' : r'\(\Delta \arg{\Psi_{2}}\)',
  'P_E3' : r'\(\Delta \arg{\Psi_{3}}\)',
  'Pr_E' : r'\(\Delta \Prob\)',
  'Pr_e' : r'\(\epsilon \Prob\)'
}

tit1='RK'
tit2='DOPRI'


def loadData(file1,file2):
  global x1,pr1,r11,i11,r21,i21,r31,i31,ph11,ph21,ph31,a11,a21,a31,c1,tit1
  global x2,pr2,r12,i12,r22,i22,r32,i32,ph12,ph22,ph32,a12,a22,a32,c2,tit2

  x1,pr1,r11,i11,r21,i21,r31,i31,ph11,ph21,ph31,a11,a21,a31,c1 = np.loadtxt(file1, unpack=True)
  x2,pr2,r12,i12,r22,i22,r32,i32,ph12,ph22,ph32,a12,a22,a32,c2 = np.loadtxt(file2, unpack=True)

  tit1 = file1.partition('_')[0]
  tit2 = file2.partition('_')[0]


def fplot_xy(x, y, labx=r"$\xi$", laby='r1', name="ampty"):
  fig, ax = plt.subplots()

  ax.plot(x,y)
  ax.set_xlabel(labx, usetex = True)
  ax.set_ylabel(labsy[laby], usetex = True)

  fig.savefig(f"{name}.pdf")


def fplot_xy2(x, y, labx=r"\(\xi\)", laby=r'\(y\)', tit = 'None', name="ampty"):
  fig, ax = plt.subplots(layout='constrained')

  ax.plot(x,y)
  ax.set_xlabel(labx, usetex = True)
  ax.set_ylabel(laby, usetex = True)

  #  fig.suptitle(tit, usetex = True)
  fig.suptitle(tit)

  fig.savefig(f"{name}.pdf")


def fplot_xyy(x, y1, y2, labx=r"$\xi$", laby='r1', leg=['T1','T2'], name="ampty"):
  fig, ax = plt.subplots()

  ax.plot(x,y1, label=leg[0])
  ax.plot(x,y2, label=leg[1])
  ax.legend()
  ax.set_xlabel(labx)
  ax.set_ylabel(labsy[laby])

  fig.savefig(f"{name}.pdf")


def fplot_2xy(x, c1, c2, y, labx=r"$\xi$", laby='r1', leg=[tit1,tit2], name="ampty"):
  fig, (ax1,ax2) = plt.subplots(2, 1)
  ax1.plot(x,c1, label=leg[0])
  ax1.plot(x,c2, label=leg[1])
  ax2.plot(x,y)
  ax2.set_xlabel(labx)
  ax1.set_ylabel("Control")
  ax1.legend()
  ax2.set_ylabel(labsy[laby])

  fig.savefig(f"{name}.pdf")


def fplot_22xy(x, c1, y, labx=r"$\xi$", laby='r1', leg=tit1, name="ampty"):
  fig, (ax1,ax2) = plt.subplots(2, 1)
  ax1.plot(x,c1, label=leg)
  ax2.plot(x,y)
  ax2.set_xlabel(labx)
  ax1.set_ylabel("Control")
  ax1.legend()
  ax2.set_ylabel(labsy[laby])

  fig.savefig(f"{name}.pdf")


def loadDatFile(file):
  global x1,pr1,r11,i11,r21,i21,r31,i31,ph11,ph21,ph31,a11,a21,a31,c1,tit1

  x1,pr1,r11,i11,r21,i21,r31,i31,ph11,ph21,ph31,a11,a21,a31,c1 = np.loadtxt(file, unpack=True)


def plotControlScaled(file):
  loadDatFile(file)

  x = x1
  y = c1
  ysc = c1*1e4

  fplot_xy2(x,y, laby=r'\(\displaystyle\sum_{k}|\Psi_{k}|^2-1\)', tit="Теоретическая точность", name="control-bare")
  fplot_xy2(x,ysc, laby=r'\(10^{4}\cdot\big(\displaystyle\sum_{k}|\Psi_{k}|^2-1\big)\)', tit="Теоретическая точность", name="control-scaled")


# For not-interactive use!!!
plotControlScaled("DOPRI_0.00001.dat")
