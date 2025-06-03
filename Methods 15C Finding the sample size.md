---
tags:
  - methods
  - notes
  - topic
---
### Foundational Concepts
$E(x)=np$
Var$(x)=np(p-1)$
### Big ideas and concepts
#### Finding trials 
Determining how many trials are required to reach a given level of probability entrails solving an equation with known indices. 
### Vocab and definitions
#### Solving for indecies
We can solve for unknown incecies using logarithms 

### Procedures
#### Solving
- Sbstitute
- simplify 
- solve
#### Remember
Your graphics calculator can solve equations for you
### Examples
#### Example 15.7
![[{535943C2-C8C0-4A66-B363-392B2AAA00D4}.png]]
##### a)
We require $Pr(x\geq1)>0.95$
$\therefore 1-Pr(x=0)>0.95$
The probability that we get at least one win is the same as $1-Pr(\textrm{Zero Wins})$

We are gonna subtract 1 from both sides then multiply both sides by $-1$. (when we do this we flip our $\leq$, >, <, etc)

$Pr(x=0)<0.05$
$\therefore (0.52)^n<0.05$ 
$Pr(x=x)=(^n _x ) p^x (1-p)^{nx}$
Consider $Pr(x=0)=(^n_0)p^0(1-p)^0=1(1-p)^n$
Take $\ln$ of both sides
$\ln(0.52^n)<\ln(0.05)$
$=n\cdot\ln(0.52)<\ln(0.05)$
$n\cdot\ln(0.52)<\ln(0.52)$
$\therefore n>\frac{\ln(0.05)}{\ln(0.52)}\approx 4.58114546\ldots$
$\therefore n>4.58114546\ldots$
$\therefore$ at least 5 games 

##### b)
We require $Pr(x\geq2) > 0.95$
$\therefore Pr(x=0)+Pr(x=1)<0.05$
$\therefore (^n_0)\cdot(0.48)^{0}\cdot(0.52)^{n-0}+(^n_1)\cdot(0.48)^1(0.52)^{n-1}$
$0.52^n+0.48n\cdot0.52^{n-1}<0.05$
Now we are gonna solve using our graphing calculator 🥳🎉

$=7.798...$
$\therefore$ 8 games required!!!!





