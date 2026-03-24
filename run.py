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


if __name__ == "__main__":
  try:
    main(sys.argv)
  except KeyboardInterrupt:
    sys.exit("Interrupted by user")
