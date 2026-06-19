```mathematica
a = 4.35196*10^6;
b = 0.030554;
e = 1;
H0 = a/e*{{0, 0, 0}, {0, b, 0}, {0, 0, 1}};
H0 // MatrixForm
```

|  |   |   |
| - | - | - |
| 0. | 0. | 0. |
| 0. | 132969.78584 | 0. |
| 0. | 0. | 4351960. |

```mathematica
\[Gamma] = 6.5956*10^4;
n = 10.54;
u[\[Xi]_] := \[Gamma]*\[ExponentialE]^(-1*n *\[Xi])
s12 = Sqrt[0.308];
s23 = Sqrt[0.437];
s13 = Sqrt[0.0234];
c12 = Sqrt[1 - s12^2];
c23 = Sqrt[1 - s23^2];
c13 = Sqrt[1 - s13^2];
W = {{c13^2*c12^2, c12*s12*c13^2, c12*c13*s13}, {c12*s12*c13^2, s12^2*c13^2, s12*c13*s13}, {c12*s13*c13, s12*c13*s13, s13^2}};
W // MatrixForm

```

|  |   |   |
| - | - | - |
| 0.6758071999999999 | 0.4508635491455923 | 0.1257532841718259 |
| 0.4508635491455923 | 0.30079279999999997 | 0.0838960757127531 |
| 0.1257532841718259 | 0.0838960757127531 | 0.0234 |

```mathematica
DOPRICoeffs[5, p_] := N[{{{1/5}, {3/40, 9/40}, {44/45, -56/15, 32/9}, {19372/6561, -25360/2187, 64448/6561, -212/729}, {9017/3168, -355/33, 46732/5247, 49/176, -5103/18656}, {35/384, 0, 500/1113, 125/192, -2187/6784,11/84}}, {35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0}, {1/5, 3/10, 4/5, 8/9, 1, 1}, {71/57600, 0, -71/16695, 71/1920, -17253/339200, 22/525, -1/40}}, p];
```

```mathematica
\[Psi][\[Xi]_] := {\[Psi]1[\[Xi]], \[Psi]2[\[Xi]], \[Psi]3[\[Xi]]}
```

```mathematica
sol = NDSolve[{\[ImaginaryI]*D[\[Psi][\[Xi]], \[Xi]] == (H0 + u[\[Xi]]*W) . \[Psi][\[Xi]], \[Psi][0.1] == {c12 c13, s12 c13, s13}}, {\[Psi]1, \[Psi]2, \[Psi]3}, {\[Xi], 0.1, 0.5}, Method -> {"ExplicitRungeKutta", "Coefficients" -> DOPRICoeffs, "DifferenceOrder" -> 5, "StiffnessTest" -> False}, StartingStepSize -> 0.25, MaxSteps -> Infinity, MaxStepFraction -> 1/12, WorkingPrecision -> MachinePrecision, AccuracyGoal -> Infinity];
```

```mathematica
uf[x_] := Evaluate[{\[Psi]1[\[Xi]], \[Psi]2[\[Xi]], \[Psi]3[\[Xi]]} /. sol] /. {\[Xi] -> x} /. {\[Xi]_} -> \[Xi];
```

```mathematica
quf[v_] := Abs[v[[1]]]^2 + Abs[v[[2]]]^2 + Abs[v[[3]]]^2;
```

```mathematica
absuf[v_] := {Abs[v[[1]]]^2, Abs[v[[2]]]^2, Abs[v[[3]]]^2};
```

```mathematica
reimuf[v_] := {Re[v[[1]]], Im[v[[1]]], Re[v[[2]]], Im[v[[2]]], Re[v[[3]]], Im[v[[3]]]};
```

```mathematica
surProb[v_] := c12^2*c13^2*Abs[v[[1]]]^2 + s12^2*c13^2*Abs[v[[2]]]^2 + s13^2*Abs[v[[3]]]^2;
```

```mathematica
arguf[v_] := {Arg[v[[1]]], Arg[v[[2]]], Arg[v[[3]]]};
st = 10^(-5);
```

```mathematica
dat1 = Table[Flatten[{x, surProb[uf[x]], reimuf[uf[x]], arguf[uf[x]], absuf[uf[x]], quf[uf[x]] - 1}], {x, 0.101, 0.5, st}];
```

```mathematica
Export["DOPRI_0.00001.dat", dat1, "Table"]

(*"DOPRI_0 00001.dat"*)
```
