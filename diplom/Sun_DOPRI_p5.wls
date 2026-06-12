#!/usr/bin/env wolframscript
(* ::Package:: *)

(* ::Section:: *)
(*Global Parameters*)


(* ::Text:: *)
(*We are researching the peculiarities of numeric solution of the neutrino oscillation in matter equation obtained by Runge--Kutta family of methods.*)
(**)
(*The equation relays on the Hermitian matrix \(H=H_{0} + v(\xi)W\), where \(H_{0}\) is Hermitian matrix of oscillation in vacuum, the \(v(\xi)\) is density function (effective density profile) and \(W\) is composed from mixing angles.*)
(**)
(*Due to its nature, the oscillation depends on neutrino energy, which is incorporated into \(H\) matrix, while the neutrino masses are part of \(H_{0}\) matrix. Below we set these parameters and though we explicitly set energy to only one value, it is possible, after testing, to adapt the code to any energy (making it function-like).*)


(* ::Input:: *)
(*a=4.35196 10^6;*)
(*b=0.030554;*)


(* ::Subsection:: *)
(*Sun model*)


(* ::Text:: *)
(*As for the density function, we use known result for the Sun (aka, the Sun model). The density is exponential function with given factor and known magnitude factor.*)


(* ::Input:: *)
(*\[Gamma]=6.5956 10^4;*)
(*n=10.54;*)
(*u[\[Xi]_]:=\[Gamma] E^(-n \[Xi])*)


(* ::Subsection:: *)
(*The mixing angles*)


(* ::Text:: *)
(*The \(W\) matrix, as was mentioned above, is constructed from mixing angles. The formula is given below. We use values for the angles from the work [Casas et al, 2016].*)


(* ::Input:: *)
(*s12=Sqrt[0.308];*)
(*s23=Sqrt[0.437];*)
(*s13=Sqrt[0.0234];*)
(*c12=Sqrt[1-s12^2];*)
(*c23=Sqrt[1-s23^2];*)
(*c13=Sqrt[1-s13^2];*)
(*W={{c13^2 c12^2,c12 s12 c13^2,c12 c13 s13},{c12 s12 c13^2,s12^2 c13^2,s12 c13 s13},{c12 s13 c13,s12 c13 s13,s13^2}};*)
(*W//MatrixForm;*)
(**)


(* ::Subsection:: *)
(* Dorman-Prince method*)


(* ::Text:: *)
(*According to work [Casas et al], the more "correct" result would be obtained if one uses the Dorman-Prince method of Runge--Kutta family. Mathematica allows to explicitly set coefficients for Runge--Kutta method used internally.*)


(* ::Input:: *)
(*DOPRICoeffs[5,p_]:=N[{{{1/5},{3/40,9/40},{44/45,-56/15,32/9},{19372/6561,-25360/2187,64448/6561,-212/729},{9017/3168,-355/33,46732/5247,49/176,-5103/18656},{35/384,0,500/1113,125/192,-2187/6784,11/84}},{35/384,0,500/1113,125/192,-2187/6784,11/84,0},{1/5,3/10,4/5,8/9,1,1},{71/57600,0,-71/16695,71/1920,-17253/339200,22/525,-1/40}},p];*)


(* ::Input:: *)
(*\[Psi][\[Xi]_]:={\[Psi]1[\[Xi]],\[Psi]2[\[Xi]],\[Psi]3[\[Xi]]}*)


(* ::Input:: *)
(*(* The idea is following: the getPsi function should calculate solution for given energy and returns the function "handler", which could be used to get actual numbers. All used variables must be local, but it may be incorrect way to use `Module`, because all it's variables are local, so it for uf... dunno. May be we should use `Block`, but before that we must compare `Block` vs `Module`. *)*)


(* ::Input:: *)
(*(* This "function" must all the work that the previous version of NB did (current one is p5, see p4). *)*)


(* ::Input:: *)
(*getPsi[energy_]:=Module[{a=4.35196 10^6, b=0.030554,*)
(*H0,W,u,\[Psi],\[Psi]1,\[Psi]2,\[Psi]3,sol,uf,\[Xi]0=0.1,\[Xi]1=1.0,DOPRICoeffs,*)
(*s12=Sqrt[0.308], s23=Sqrt[0.437], s13=Sqrt[0.0234],*)
(*c12=0,c13=0,c23=0, \[Gamma]=6.5956 10^4, n=10.54,*)
(*},*)
(*c12=Sqrt[1-s12^2];*)
(*c23=Sqrt[1-s23^2];*)
(*c13=Sqrt[1-s13^2];*)
(*H0=a/energy {{0,0,0},{0,b,0},{0,0,1}};*)
(*W={{c13^2 c12^2,c12 s12 c13^2,c12 c13 s13},{c12 s12 c13^2,s12^2 c13^2,s12 c13 s13},{c12 s13 c13,s12 c13 s13,s13^2}};*)
(*H0;*)
(*u[\[Xi]_]:=\[Gamma] E^(-n \[Xi]);*)
(*\[Psi][\[Xi]_]:={\[Psi]1[\[Xi]],\[Psi]2[\[Xi]],\[Psi]3[\[Xi]]};*)
(*DOPRICoeffs[5,p_]:=N[{{{1/5},{3/40,9/40},{44/45,-56/15,32/9},{19372/6561,-25360/2187,64448/6561,-212/729},{9017/3168,-355/33,46732/5247,49/176,-5103/18656},{35/384,0,500/1113,125/192,-2187/6784,11/84}},{35/384,0,500/1113,125/192,-2187/6784,11/84,0},{1/5,3/10,4/5,8/9,1,1},{71/57600,0,-71/16695,71/1920,-17253/339200,22/525,-1/40}},p];*)
(*sol=NDSolve[{I*D[\[Psi][\[Xi]],\[Xi]]==(H0+u[\[Xi]]*W) . \[Psi][\[Xi]],\[Psi][\[Xi]0]=={c12 c13,s12 c13, s13}},{\[Psi]1,\[Psi]2,\[Psi]3},{\[Xi],\[Xi]0,\[Xi]1}, Method->{"ExplicitRungeKutta","Coefficients"->DOPRICoeffs,"DifferenceOrder"->5,"StiffnessTest"->False},StartingStepSize->0.25,MaxSteps->Infinity,MaxStepFraction->1/12,WorkingPrecision->MachinePrecision,AccuracyGoal->Infinity];*)
(*uf[x_]:= Evaluate[{\[Psi]1[\[Xi]],\[Psi]2[\[Xi]],\[Psi]3[\[Xi]]}/.sol]/.{\[Xi]->x}/.{\[Xi]_}->\[Xi];*)
(*uf*)
(*];*)
(*(* TODO: check that function getPsi is working. Assumed interface:*)
(*uf=getPsi[1];*)
(*Then, the below (with uf) must work as in `_p4` part.*)
(**)*)


(* ::Subsection:: *)
(*Numeric solution*)


(* ::Text:: *)
(*One of flaws of the [Casas et al] work is that they don't describe how they get the numeric solution from Mathematica. For example, if one sees below, it would see that the call to `NDSolve` is quite complex. First, we use own coefficients, then we set other parameters to fine tune the Mathematica `NDSolve` to obtain numeric result.*)


(* ::Input:: *)
(*\[Xi]0=0.1;\[Xi]1=1.0;*)


(* ::Input:: *)
(*sol=NDSolve[{I*D[\[Psi][\[Xi]],\[Xi]]==(H0+u[\[Xi]]*W) . \[Psi][\[Xi]],\[Psi][\[Xi]0]=={c12 c13,s12 c13, s13}},{\[Psi]1,\[Psi]2,\[Psi]3},{\[Xi],\[Xi]0,\[Xi]1}, Method->{"ExplicitRungeKutta","Coefficients"->DOPRICoeffs,"DifferenceOrder"->5,"StiffnessTest"->False},StartingStepSize->0.25,MaxSteps->Infinity,MaxStepFraction->1/12,WorkingPrecision->MachinePrecision,AccuracyGoal->Infinity];*)


(* ::Subsection:: *)
(*The solution form*)


(* ::Text:: *)
(*Besides opaque way how Mathematica calculates the solution, the `NDSolve` returns not a solution itself, but rather interpolation function using Pade approximation (?). The details very cloudy, so we have only hunch of what is going on.*)
(**)
(*Still, to get numbers from solution we have to construct the `uf` handler.*)


(* ::Input:: *)
(*uf[x_]:= Evaluate[{\[Psi]1[\[Xi]],\[Psi]2[\[Xi]],\[Psi]3[\[Xi]]}/.sol]/.{\[Xi]->x}/.{\[Xi]_}->\[Xi];*)


(* ::Subsection:: *)
(* The "correctness" check route*)


(* ::Text:: *)
(*The below code is used to check the solution "correctness". Ideally, the equation is the Schr\[ODoubleDot]dinger type with Hermitian matrix. As such, the probability (or the norm of the function) must be conserved. If initially the norm is very close to 1, then the solution at any point (\(\xi=1\) including), must have the same norm.*)
(**)
(*Though, if there is an absorption then the matrix \(H\) is NOT Hermitian anymore and this feature is not hold.*)


(* ::Input:: *)
(*quf[v_]:=Abs[v[[1]]]^2+Abs[v[[2]]]^2+Abs[v[[3]]]^2;*)


(* ::Input:: *)
(*absuf[v_] := {Abs[v[[1]]]^2,Abs[v[[2]]]^2,Abs[v[[3]]]^2};*)


(* ::Input:: *)
(*reimuf[v_]:={Re[v[[1]]],Im[v[[1]]],Re[v[[2]]],Im[v[[2]]],Re[v[[3]]],Im[v[[3]]]};*)


(* ::Input:: *)
(*surProb[v_]:=c12^2*c13^2*Abs[v[[1]]]^2+s12^2*c13^2*Abs[v[[2]]]^2+s13^2*Abs[v[[3]]]^2;*)


(* ::Input:: *)
(*arguf[v_] := {Arg[v[[1]]],Arg[v[[2]]],Arg[v[[3]]]};*)


(* ::Input:: *)
(*st=10^(-5);*)


(* ::Input:: *)
(*xi0=\[Xi]0+0.01;xi1=\[Xi]1-0.1;*)


(* ::Input:: *)
(*dat1=Table[Flatten[{x,surProb[uf[x]],reimuf[uf[x]],arguf[uf[x]],absuf[uf[x]],quf[uf[x]]-1}],{x,xi0,xi1,st}];*)


(* ::Subsection:: *)
(*The data directory*)


(* ::Text:: *)
(*It is inconvenient to use full path when exporting (saving) the data. Instead, one may use the path relative to the notebook itself, as we do below. It is big help that `NotebookDir[]` returns path with path separator at the end.*)
(**)
(*NB: the `<>` is the Mathematica way to join (merge) the string.*)


(* ::Input:: *)
(*(* SetDirectory[$UserDocumentsDirectory] ... *)
(*NotebookDirectory[] ...*)
(*$HomeDirectory ...*)
(*$UserBaseDirectory ...*)
(*$Username*)
(*In[.] $UserBaseDirectory*)
(*Out[.] -> dir *)*)


(* ::Input:: *)
(*nbDir=NotebookDirectory[];*)


(* ::Input:: *)
(*mkEngFmt[n_]:=ToString[EngineeringForm[1. n,NumberFormat->(Row[{#1,"e",#3}]&)]];*)


(* ::Input:: *)
(*mkScnFmt[n_]:=ToString[ScientificForm[1. n,NumberFormat->(Row[{#1,"e",#3}]&)]];*)


(* ::Input:: *)
(*datfn=FileNameJoin[nbDir,"SUN_DOPRI_"<>ToString[\[Xi]0] <> "_"<>ToString[\[Xi]1]<>"_"<>mkScnFmt[st]<>".dat"];*)


(* ::Input:: *)
(*Export[datfn,dat1,"Table"];*)


(* ::Subsection:: *)
(*The convenience*)


(* ::Text:: *)
(*For convenience we explicitly "extract" parts of solution: real and imaginary parts, and all three components.*)


(* ::Input:: *)
(*eRpsi1[x_]:=Re[uf[x][[1]]];*)
(*eIpsi1[x_]:=Im[uf[x][[1]]];*)
(*eRpsi2[x_]:=Re[uf[x][[2]]];*)
(*eIpsi2[x_]:=Im[uf[x][[2]]];*)
(*eRpsi3[x_]:=Re[uf[x][[3]]];*)
(*eIpsi3[x_]:=Im[uf[x][[3]]];*)


(* ::Section:: *)
(*The utility functions*)


(* ::Text:: *)
(*These functions are used to get some data from obtained solution.*)


(* ::Subsection:: *)
(*The `funcNullRanges` function*)


(* ::Text:: *)
(*Takes function handler, two points and integer.*)
(**)
(*The purpose is roughly search for the ranges where the function has a zero. The two points set the wide range within we looking for the zeroes. The integer parameter is used to split the wide range into pieces. The function actually doesn't calculate exact position of the zeroes. Instead, it checks the function signs on the subinterval edges. If the sign is different, then we call such interval a zero range.*)
(**)
(*The routine returns array of zero ranges.*)
(**)
(*We presume that the function has zero of first order (only!) and many of them.*)


(* ::Input:: *)
(*funcNullRanges[fn_,x1_,x2_,n_]:=Module[{t={},xx={},mm={},dx=(x2-x1)/n,i=1,nL=0},*)
(*xx=Table[k,{k,x1,x2,dx}];*)
(*mm=Table[fn[k],{k,xx}];*)
(*nL=Length[mm];*)
(*While[i<nL,*)
(*If[mm[[i]]*mm[[i+1]]<0,AppendTo[t,{xx[[i]],xx[[i+1]]}]];*)
(*i++;];*)
(*t*)
(*];*)


(* ::Subsection:: *)
(*The `funcNullRangesStab` function*)


(* ::Text:: *)
(*Takes the same argument as `funcNullRanges`.*)
(**)
(*The previous function is a bit too rough, so this one tries to "stabilize" the number of zero ranges.*)
(**)
(*The idea is simple: if the wide range splitting on different number of subparts gives the save number of zero ranges, then we found the "exact" number of "zeroes" on the wide interval. For that we iteratively call the `funcNullRanges` function increasing number of splits and checking the returned array size.*)
(**)
(*The routine returns array of zero ranges (as function `funcNullRanges` do).*)


(* ::Input:: *)
(*funcNullRangesStab[fn_,x1_,x2_,n_]:=Module[{n1=-1,n2=-1,nx=n,i=0,imx=6,tt={}},*)
(*While[i<imx,*)
(*nx=n (4+i)^i;*)
(*tt=funcNullRanges[fn,x1,x2,nx];*)
(*n1=n2;*)
(*n2=Length[tt];*)
(*If[n1==n2,Break[]];*)
(*i++];*)
(*tt*)
(*];*)


(* ::Subsection:: *)
(*The `funcTochnNull` function*)


(* ::Text:: *)
(*Takes four arguments: function handler, two points and precision.*)
(**)
(*It returns zero range which length is less than given precision.*)


(* ::Input:: *)
(*funcTochnNull[fn_,x1_,x2_,eps_]:=Module[{t1=x1,t2=x2,tt={}},*)
(*While[t2-t1>eps,*)
(*If[fn[t1] fn[(t1+t2)/2]<0,t2=(t1+t2)/2,t1=(t1+t2)/2];*)
(*];*)
(*List[t1,t2]*)
(*];*)


(* ::Subsection:: *)
(*The `funcQPRangeEnvelop` function*)


(* ::Text:: *)
(*Takes four arguments: function handler and three points.*)
(**)
(*The first point is a point in vicinity of which we try to find zero range. The rest two give the wide range bounds, within which the assumed zero range should be located.*)
(**)
(*Idea for the function is the following. We want to find the nearest to given point the function zero. We only know, that is must be somewhere in the given range. It is possible that there is more than one such zero. We need only the nearest. So we get all possible zeroes (zero ranges), subtract the given point and search for the smallest possible distance. There is a possibility that the given point resides "exactly" between two zeroes. In such case we take the left one.*)


(* ::Input:: *)
(*funcQPRangeEnvelop[fn_,x0_,x1_,x2_]:=Module[{i0=0,tt={},xl={},xc={},xr={},eps=10^-8},*)
(*tt=funcNullRangesStab[fn,x1,x2,10];*)
(*i0=tt[[;;,1]]-x0//Abs//PositionSmallest//First;*)
(*If[(i0>Length[tt]-1) || (i0 ==1),*)
(*(*Print["[WARNING] `funcQPRangeEnvelop`: the smallest is on an edge!"];*)
(*Print["[DEBUG] i0 = ", i0, "; x0 = ", x0, "; (", x1,";",x2,")", "; tt = ", tt];*)*)
(*Return[List[-1,-1]]];*)
(*(*Print["[DEBUG:funcQPRangeEnvelop] i0 = ", i0, "; tt = ", tt, "; tt[:,1] - x0 = ", tt[[;;,1]]-x0];*)*)
(*xl=tt[[i0-1]]//Flatten;*)
(*xc=tt[[i0]]//Flatten;*)
(*xr=tt[[i0+1]]//Flatten;*)
(*xl=funcTochnNull[fn,xl[[1]],xl[[2]],eps];*)
(*xr=funcTochnNull[fn,xr[[1]],xr[[2]],eps];*)
(*List[xl[[1]],xr[[2]]]*)
(*]*)


(* ::Subsection:: *)
(*The `funcLastQPeriod` function*)


(* ::Text:: *)
(*Takes two arguments: function handler and integer.*)
(**)
(*This is very specific function. The real and imaginary parts of the solution "oscillates" very often, but the first component (which is true for the Sun model) at the right edge of the interval (\(\xi=1\)) stops oscillating and "asymptotically" tends to a value (zero).*)
(**)
(*This function finds the last three zeroes, such that after the last one there no more zeroes.*)
(**)
(*Returns array of zero ranges.*)
(**)
(*Designed only for real and imaginary parts of first component.*)


(* ::Input:: *)
(*xi0=0.5;xi1=0.99;*)


(* ::Input:: *)
(*funcLastQPeriod[fn_,n_]:=Module[{x0=xi0,x2=xi1,i=1,tt={},y1=0,y2=0,y3=0,eps=10^-8},*)
(*tt=funcNullRangesStab[fn,x0,x2,n];*)
(*k=Length[tt];*)
(*y1=funcTochnNull[fn,tt[[k-2,1]],tt[[k-2,2]],eps];*)
(*y2=funcTochnNull[fn,tt[[k-1,1]],tt[[k-1,2]],eps];*)
(*y3=funcTochnNull[fn,tt[[k,1]],tt[[k,2]],eps];*)
(*List[y1,y2,y3]*)
(*]*)


(* ::Subsection:: *)
(*The `funcQPeriodStat` function*)


(* ::Text:: *)
(*Takes three arguments: function handler and two integers. The first integer is a number of "rough tries", the second one is the number of random sample points.*)
(**)
(*Despite the name it works only with real and imaginary parts of first component (though technically, could work with second component too) and returns array of two element array. The first element is the random point within predefined interval, the second element is the width of zero range containing the random point.*)
(**)
(*The function handler and number of "rough tries" are passed to `funcLastQPeriod` function.*)
(**)
(*The random points are generated by `getSRandoms` function. The interval is predefined and doesn't changed: \((0,11;0,99)\).*)
(**)
(*As we are interested in how the "quasiperiod" (the width of zero range) changes while goes from left to right by \(\xi\), we collect the data in an array.*)
(**)
(*Later, it could be used by other routines to obtain data for second and third components.*)


(* ::Input:: *)
(*xi0=0.11*)


(* ::Input:: *)
(*funcQPeriodStat[fn_,nSeed_, nSteps_]:=Module[{i=1,tabQPeriod={},endt={},x00=0,x01=0,x02=0,x0=xi0,gran1={},dx=0,t=0,pf={1,3/2,7/4,2},k=1,fl=1},*)
(*endt=funcLastQPeriod[fn,nSeed];*)
(*dx=endt[[3,1]]-endt[[1,1]];*)
(*AppendTo[tabQPeriod,{endt[[1,1]],endt[[3,1]]}];*)
(*fl=Length[pf];*)
(*While[i<=nSteps,*)
(*t=tabQPeriod[[i,1]];*)
(*x02=t+dx/4;*)
(*Label[rechoose];*)
(*x01=t-pf[[k]] dx;*)
(*x00=(x01+x02)/2;*)
(*If[x01<x0,Print["[WARNING] reached the lower bound (", x0,") on step '", i,"'"]; tabQPeriod;Break[]];*)
(*(*Print["[DEBUG.funcQPeriodStat] i = ", i, "; (", x01, "; ",x02,"); x00 = ", x00, "; t = ", t, "; dx = ", dx];*)*)
(*gran1=funcQPRangeEnvelop[fn,x00,x01,x02];*)
(*(*Print["[DEBUG] gran1 = ", gran1, "; x00 = ", x00, "; (", x01, ";",x02,"); k = ", k];*)*)
(*If[k>=fl,Print["[WARNING] rough way to get Null Enveloped Ranges failed: get ", i," ranges."];Goto[end]];*)
(*If[gran1[[1]] == -1,k=k+1;Goto[rechoose]];*)
(*dx=Abs[gran1[[2]]-gran1[[1]]];*)
(*AppendTo[tabQPeriod,gran1];*)
(*i++;k=1;];*)
(*Label[end];*)
(*tabQPeriod*)
(*]*)


(* ::Input:: *)
(*nSamp=100;*)


(* ::Input:: *)
(*qpRR1=funcQPeriodStat[eRpsi1,10,nSamp];*)


(* ::Input:: *)
(*qpRI1=funcQPeriodStat[eIpsi1,10,nSamp];*)


(* ::Input:: *)
(*datfR=nbDir<>"qperiod_Rpsi1_"<>mkScnFmt[nSamp]<>".dat";*)
(*datfI=nbDir<>"qperiod_Ipsi1_"<>mkScnFmt[nSamp]<>".dat";*)


(* ::Input:: *)
(*Export[datfR,qpRR1,"Table"];*)
(*Export[datfI,qpRI1,"Table"];*)


(* ::Input:: *)
(*tP2R=funcCountZrsInRanges[eRpsi2,qpRR1,10];*)


(* ::Input:: *)
(*tP2I=funcCountZrsInRanges[eIpsi2,qpRI1,10];*)


(* ::Input:: *)
(*tP3R=funcCountZrsInRanges[eRpsi3,qpRR1,10];*)


(* ::Input:: *)
(*tP3I=funcCountZrsInRanges[eIpsi3,qpRI1,10];*)


(* ::Input:: *)
(*dat2R=nbDir<>"zrsCountsRpsi2_"<>mkScnFmt[nSamp]<>".dat";*)
(*dat2I=nbDir<>"zrsCountsIpsi2_"<>mkScnFmt[nSamp]<>".dat";*)
(*dat3R=nbDir<>"zrsCountsRpsi3_"<>mkScnFmt[nSamp]<>".dat";*)
(*dat3I=nbDir<>"zrsCountsIpsi3_"<>mkScnFmt[nSamp]<>".dat";*)


(* ::Input:: *)
(*Export[dat2R,tP2R,"Table"];*)
(*Export[dat2I,tP2I,"Table"];*)
(*Export[dat3R,tP3R,"Table"];*)
(*Export[dat3I,tP3I,"Table"];*)


(* ::Input:: *)
(*nSamp=1000;*)


(* ::Input:: *)
(*datfR=nbDir<>"qperiod_Rpsi1_"<>mkScnFmt[nSamp]<>".dat";*)
(*datfI=nbDir<>"qperiod_Ipsi1_"<>mkScnFmt[nSamp]<>".dat";*)


(* ::Input:: *)
(*qpTR1=funcQPeriodStat[eRpsi1,10,nSamp];*)


(* ::Input:: *)
(*qpTI1=funcQPeriodStat[eIpsi1,10,nSamp];*)


(* ::Input:: *)
(*Export[datfR,qpTR1, "Table"];*)
(*Export[datfI,qpTI1, "Table"];*)


(* ::Input:: *)
(*funcCountZrsInRanges[fn_,tab_, n_]:=Module[{i=1,tabZrs={},l=0,tt={},nm=0},*)
(*l=Length[tab];*)
(*While[i<=l,*)
(*tt=funcNullRangesStab[fn,tab[[i,1]],tab[[i,2]],n];*)
(*nm=Length[tt];*)
(*AppendTo[tabZrs,{tab[[i,1]],tab[[i,2]],nm}];*)
(*i++*)
(*];*)
(*tabZrs*)
(*]*)


(* ::Input:: *)
(*qP2R=funcCountZrsInRanges[eRpsi2,qpTR1,10];*)


(* ::Input:: *)
(*qP2I=funcCountZrsInRanges[eIpsi2,qpTI1,10];*)


(* ::Input:: *)
(*qP3R=funcCountZrsInRanges[eRpsi3,qpTR1,10];*)


(* ::Input:: *)
(*qP3I=funcCountZrsInRanges[eIpsi3,qpTI1,10];*)


(* ::Input:: *)
(*dat2R=nbDir<>"zrsCountsRpsi2_"<>mkScnFmt[nSamp]<>".dat";*)
(*dat2I=nbDir<>"zrsCountsIpsi2_"<>mkScnFmt[nSamp]<>".dat";*)
(*dat3R=nbDir<>"zrsCountsRpsi3_"<>mkScnFmt[nSamp]<>".dat";*)
(*dat3I=nbDir<>"zrsCountsIpsi3_"<>mkScnFmt[nSamp]<>".dat";*)


(* ::Input:: *)
(*Export[dat2R,qP2R,"Table"];*)
(*Export[dat2I,qP2I,"Table"];*)
(*Export[dat3R,qP3R,"Table"];*)
(*Export[dat3I,qP3I,"Table"];*)
