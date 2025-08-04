---
tags:
  - methods
---
### Foundational Concepts
#### Normal distribution
![[Equation for normal distribution Probability Density Function]]

#### Standard deviation
![[Standard Deviation]]

### Vocab and definitions
#### Point estimate
![[Point Estimate]]
#### Interval Estimate
![[Interval estimate]]

#### [[Z Score]]
![[Z Score]]
#### Common $z$ values
![[Common z values]]

#### Approximate confidence intervals for $p$
An approximate $C\%$ confidence interval for $p$ is given by
$(\hat{p} - z \sqrt{ \hat{p}(1-\hat{p} / n}, \hat{p} + z \sqrt{ \hat{p}(1-\hat{p} / n})$
Where:
- $p$ is the unknown population proportion
- $\hat p$ is the value of the sample proportion
- $n$ is the size of the sample
- $z$ is such that $Pr(-z<Z<z)=C\%$ 
#### Distance between sample estimate
Distance between sample estimate and the endpoints of the confidence interval is call margin of error:
- $E=z\sqrt{\hat p (\frac{1-\hat p}{n})}$
#### Required $C\%$ confidence for sample size
$n=\frac{z}{E}^2 \cdot p^*(1-p^*)$
Where:
- $p^*$ is an estimated value for the population proportion ($p$)

### Procedures
- What do I know? 
- What am I trying to figure out? 
- What is one thing that I can do to get closer to a solution
- Repeat

### Examples
1. You survey 1000 Australians and find that $55\%$ plan to vote for Labor at the next federal election. 
	Will Labor get more votes than the other parties in the election ?

Step 1: Find your confidence interval 
Using inverseNormCD

Tail: Central
Area:0.95 (we want to be $95\%$ sure)
$\mu=0$
$\sigma=1$ 

Confidence interval is 1.96

Step 2: Calculate confidence interval:
Consdier $\hat p \pm z\cdot\sqrt{\frac{\hat p{ (1-p)}}{n}}$
	$\therefore 55\pm1.96 \sqrt \frac{0.55\cdot 0.45}{1000}$
	$0.55+1.96 \sqrt \frac{0.55\cdot 0.45}{1000}\approx 0.5808349801\ldots$
	$0.55-1.96 \sqrt \frac{0.55\cdot 0.45}{1000}\approx 0.5191650198\ldots$

i.e we are $95\%$ confident that the population proportion is between $0.5191650198$, and $$0$.5808349801$


