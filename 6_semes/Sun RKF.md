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
RKFCoeffs[4, p_] := N[{{{1/4}, {3/32, 9/32}, {1932/2197, -7200/2197, 7296/2197}, {439/216, -8, 3680/513, -845/4104}, {-8/27, 2, -3544/2565, 1859/4104, -11/40}}, {25/216, 0, 1408/2565, 2197/4104, -1/5, 0}, {1/4, 3/8, 12/13, 1, 1/2}, {-1/360, 0, 128/4275, 2197/75240, -1/50, -2/55}}, p];
```

```mathematica
\[Psi][\[Xi]_] := {\[Psi]1[\[Xi]], \[Psi]2[\[Xi]], \[Psi]3[\[Xi]]};
```

```mathematica
sol = NDSolve[{\[ImaginaryI]*D[\[Psi][\[Xi]], \[Xi]] == (H0 + u[\[Xi]]*W) . \[Psi][\[Xi]], \[Psi][0.1] == {c12 c13, s12 c13, s13}}, {\[Psi]1, \[Psi]2, \[Psi]3}, {\[Xi], 0.1, 1}, Method -> {"ExplicitRungeKutta", "Coefficients" -> RKFCoeffs, "DifferenceOrder" -> 4, "EmbeddedDifferenceOrder" -> 5, "StiffnessTest" -> False}, StartingStepSize -> 1, MaxSteps -> Infinity, MaxStepFraction -> 1/10, WorkingPrecision -> MachinePrecision, AccuracyGoal -> Infinity];
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
arguf[v_] := {Arg[v[[1]]], Arg[v[[2]]], Arg[v[[3]]]};
```

```mathematica
dat1 = Table[Flatten[{x, surProb[uf[x]], reimuf[uf[x]], arguf[uf[x]], absuf[uf[x]], quf[uf[x]] - 1}], {x, 0.101, 1, 0.00001}];
```

```mathematica
Export["RKF_1_0.00001.dat", dat1, "Table"]

(*"RKF_1_0.00001.dat"*)
```
