---
tags:
  - 12Textbook
  - notes
  - topic
  - Specialist
---
## Mathematical Induction for Sums
### Foundational Concepts
#### Proof
- Applying steps we know to be true
- Proving generic statement - NOT JUST GIVING AN EXAMPLE

i.e. 
$\forall a, b \exists Z$
$a+b \exists Z$
$ab \exists Z$ 
$a-b \exists Z$ 

#### Sets
$Z\rightarrow$ integers
$N\rightarrow$ Natural numbers - Positive whole integers ($Z^+$)

### Vocab and definitions

#### Mathematical Induction
1. Proposition, $P(n)$
2. Prive $P(n)$ holds, $\forall n \exists N$ 
3. Prove 2 things
	1. P$(1)$ holds
	2. $P(k) \implies P(k+1)$ 

### Foundational Concepts
#### P principle
$P(1) \implies P(2)$
$P(2) \implies P(3)$
$P(2) \implies P(3)$
$P(4) \implies ...$
### Procedures
1. Prove $P(1)$ holds
2. Assume $P(k)$ holds
3. Prove $P(k) \implies P(k+1)$ 
4. Clearly state result. 

### Examples
![[Methods 3B Mathematical Induction 2025-02-18 09.14.32.excalidraw]]


## Mathematical Induction with summation notation
### Vocab and definitions
#### Summation Notation
$\Sigma^b_{r=a}f(r) = f(u){ + f(a+1)+\dots+f(b-1)+f(b)}$

### Examples
![[Methods 3B Mathematical Induction 2025-02-18 10.05.09.excalidraw]]

## Mathematical Induction for divisibility results
### Foundational Concepts
#### Remainder
$\frac{3}{25}=3r_{1}$
$25=3\times 8 + r$

### Vocab and definitions
#### Evenly dividing
Say $p$, evenly divides $q$, ($p|q$), if the remainder is 0 when $q$ is divided by $p$
i.e $\epsilon n\;  s.t \; q=np+0$
	There exists some number so that $q$ is equal to some integer scalar applied to $p$ 

### Big ideas and concepts
#### Induction
$(P(1) \cap P(k) \rightarrow P(K+1)) \implies p(n) \; \textrm{holds}\; A n \epsilon N$
i.e $P(1) \implies P(2) \implies P(3)...$ 

### Procedures
#### Proving $P(k)$ holds
1. Prove $P(1)$ holds
2. Assume that $P(k)$ holds 
3. Prove $P(k) \implies P(k+1)$ 
4. Clearly state results
### Examples
![[Methods 3B Mathematical Induction 2025-02-25 09.07.11.excalidraw]]
