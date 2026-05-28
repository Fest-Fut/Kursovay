#!/usr/bin/python

import numpy as np
import sys
from pathlib import Path


def main(args):
  """
  Merge files...
  """

  c2_f = [ "0kolNull_eRpsi2.dat", "1kolNull_eRpsi2.dat",
           "0kolNull_eIpsi2.dat", "1kolNull_eIpsi2.dat" ]
  c3_f = [ "1kolNull_eRpsi3.dat", "0kolNull_eRpsi3.dat",
           "1kolNull_eIpsi3.dat", "0kolNull_eIpsi3.dat" ]

  dt = np.dtype('i1, f8, f8, u8')

  for fl in c2_f:
    if not Path(fl).exists:
      sys.exit(f"[ERROR] file '{fl}' does not exist!")

  c2_Er = np.loadtxt(c2_f[0], dtype = dt)
  c2_Or = np.loadtxt(c2_f[1], dtype = dt)

  c2_Ei = np.loadtxt(c2_f[2], dtype = dt)
  c2_Oi = np.loadtxt(c2_f[3], dtype = dt)

  len_e = len(c2_Er)
  len_o = len(c2_Or)

  c2_r = []
  _len = len_e
  if len_o < len_e:
    _len = len_o
  for i in range(_len):
    c2_r.append(c2_Er[i])
    c2_r.append(c2_Or[i])
  if len_e != len_o:
    if len_e > len_o:
      c2_r.append(c2_Er[-1])
    else:
      c2_r.append(c2_Or[-1])

  len_e = len(c2_Ei)
  len_o = len(c2_Oi)

  c2_i = []
  _len = len_e
  if len_o < len_e:
    _len = len_o
  for i in range(_len):
    c2_i.append(c2_Ei[i])
    c2_i.append(c2_Oi[i])
  if len_e != len_o:
    if len_e > len_o:
      c2_i.append(c2_Ei[-1])
    else:
      c2_i.append(c2_Oi[-1])

  _fmt = "%d %.18e %.18e %d"
  _c2_r = np.array(c2_r, dtype = dt)
  _c2_i = np.array(c2_i, dtype = dt)
  c2_out = [ "kolNull_eRpsi2",  "kolNull_eIpsi2" ]
  # ###
  np.savetxt(f"{c2_out[0]}.dat", _c2_r, fmt = _fmt)
  np.savetxt(f"{c2_out[1]}.dat", _c2_i, fmt = _fmt)
  # ###
  np.save(f"{c2_out[0]}.npy", _c2_r)
  # ###
  np.save(f"{c2_out[1]}.npy", _c2_i)


  # ############################################################################
  for fl in c3_f:
    if not Path(fl).exists:
      sys.exit(f"[ERROR] file '{fl}' does not exist!")

  c3_Er = np.loadtxt(c3_f[0], dtype = dt)
  c3_Or = np.loadtxt(c3_f[1], dtype = dt)

  c3_Ei = np.loadtxt(c3_f[2], dtype = dt)
  c3_Oi = np.loadtxt(c3_f[3], dtype = dt)

  len_e = len(c3_Er)
  len_o = len(c3_Or)

  c3_r = []
  _len = len_e
  if len_o < len_e:
    _len = len_o
  for i in range(_len):
    c3_r.append(c3_Er[i])
    c3_r.append(c3_Or[i])
  if len_e != len_o:
    if len_e > len_o:
      c3_r.append(c3_Er[-1])
    else:
      c3_r.append(c3_Or[-1])

  len_e = len(c3_Ei)
  len_o = len(c3_Oi)

  c3_i = []
  _len = len_e
  if len_o < len_e:
    _len = len_o
  for i in range(_len):
    c3_i.append(c3_Ei[i])
    c3_i.append(c3_Oi[i])
  if len_e != len_o:
    if len_e > len_o:
      c3_i.append(c3_Ei[-1])
    else:
      c3_i.append(c3_Oi[-1])

  _fmt = "%d %.18e %.18e %d"
  _c3_r = np.array(c3_r, dtype = dt)
  _c3_i = np.array(c3_i, dtype = dt)
  c3_out = [ "kolNull_eRpsi3",  "kolNull_eIpsi3" ]
  # ###
  np.savetxt(f"{c3_out[0]}.dat", _c3_r, fmt = _fmt)
  np.savetxt(f"{c3_out[1]}.dat", _c3_i, fmt = _fmt)
  # ###
  np.save(f"{c3_out[0]}.npy", _c3_r)
  # ###
  np.save(f"{c3_out[1]}.npy", _c3_i)



if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")
