---
tags:
  - Specialist
---
### Foundational Concepts 
![[Methods 10A Estimating the area under a graph]]

### Big ideas and concepts
#### Area under the curve
We can approximate area under a curve using parabolas 
### Vocab and definition
#### Simpsons rule with three intervals 
For a continuous function, $f(x)$, on an interval, $[a, b]$, we consider three points on on the graph for $f(x)$ where the three values are:
$$x+0 = a \;\;\;\;\;\;\; x_1 = \frac{a+b}{2} \;\;\;\;\;\; x_2=b$$
Simpsons rule is:
$$\int ^b _a f(x) dx \approx \frac{b-a}{6}(f(x_0) _ 4f(x_1) + f(x_2))$$
The approximation of the integral from $a$ to $b$ is that function of $f(x)$ 
#### The General form of Simpsons rule
Let $n$ be a positive even number. Divide the interval $[a, b]$ into $n$ equal sub-intervals: $[x_0, x_1], [x_1, x_2], [x_2, x_3],...[x_{n-1}, x_n]$. 

The width of each sub interval is:$$w=\frac{b-a}{n}$$
Therefore Simpsons rule becomes:
$$\int ^b _a f(x) dx \approx $$
$$\frac{w}{3} \left(f(x_0) + 4\left[f(x_1) + f(x_3) + ... + f(x_{n-1})\right] + 2\left[ f(x_2) + f(x_4) + .. + f(x_{n-2})\right] + f(x_n)\right)$$
