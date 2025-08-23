---
tags:
  - maths
---
### Finding [[Conditional Probability]] in a [[Probability Density Function]]

For equation $Pr(A<X<B | C<X<D)$
1. Consider $Pr(A<X<B)$, and $Pr(C<X<D)$ 

	Ensure that the bounds of $A$ are within $B$, if they are not, shorten. 
	e.g. Considering $Pr(2<X<10|Pr(X<5)$, clearly bounds for first condition must shrink to be within bounds of second contrition. Separating these functions, we will have
	$Pr(2<x<5)$ and $Pr(X<5)$ with matching bounds. 
2. The result of transforming these bounds is literally $Pr(A\cap B)$
3. Solve using formula sheet ($Pr(A|B)=\frac{Pr(A\cap B)}{Pr(B)}$
