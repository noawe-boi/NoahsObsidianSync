---
tags:
  - maths
---
### Equation for normal distribution [[Probability Density Function]]
#### Regular
$f(x)=\frac{1}{\sqrt{2\pi}}\cdot e^{-\frac{1}{2}\cdot x^2}$
- $\mu = 0$
- $\sigma = 1$
```desmos-graph
y=\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}\cdot x^2}
```

#### Modified
$f(x)=\frac{1}{\sigma\sqrt{2\pi}}\cdot e^{-\frac{1}{2}\cdot \frac{x-\mu}{\sigma}^2}$
$\textrm{Pr}(X\leq a)=\textrm{Pr}({Z}\leq\frac{a-\mu}{\sigma})$
Where $Z$ is the regular (standard) normal distribution.
