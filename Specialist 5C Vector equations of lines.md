
### Foundational Concepts
#### Vector
- Has direction and magnitude
- Can be moved

#### Position vector
$\vec{OA}=\mathbf{a}$
$\vec{AB}=\mathbf{b}-\mathbf{a}$

#### Equating Coefficients

#### Parralel lines
- Same direction (or gradient)

However, in the concetxt of a vector equation, $d$ is the direction of the line. 
	
#### Perpandicular lines
When lines $\mathbf{a}$ and $\mathbf{b}$ are perpandicular
- $\mathbf{a} \times \mathbf{b} = 0

### Big ideas and concepts
#### Vector equation of a lines

![[Image1.png]]

### Vocab and definitions
#### Position vectors
For position vector 

$\mathbf{a}=a_1 i + a_2 \mathbf{j} + a_3 \mathbf{k}$
and vector parralel to the line:
$\mathbf{d} = d_1 \mathbf{i} + d_2 \mathbf{j} + d_3 \mathbf{k}$ 
#### Vector equation
$\mathbf{r}(t)=\mathbf{a}+t\mathbf{d}, t \epsilon \mathbb{R}$

#### Parametric equations
$x=a_1 + d_1 t = x(t)$
$y=a_2 + d_2 t = y(t)$
$z=a_3 + d_3 t = z(t)$

#### Cartesian equations
$\frac{x-a_1}{d_1} = \frac{y-a_2}{d_2} = \frac{z-a_3}{d_3}$


### Examples
#### Example 5.7
![[Example 1.png]]
#### Example 5,8
We are going to let $a=i+j-2k$, $b=2i-j-k$

$d=b-a=i-2j+k$

$\therefore r(t) = a +td, t \epsilon \mathbb{R}$
$=i+j-2k+t(i-2j+k)$

#### Example 5.9
##### a)
The line passing through $A(1, 2)$, and $B(0, -3)$

let $a=i+2j$, $b=-3j$
These are the cartesian co-ordiantes of $A$ and $B$

$d=a-b=i+5j$ 

We are going from $b$ to $a$ by going from $b$, to the origin, to $a$
now we find $r(t)$
consider $r(t)=a+td=i+2j+t(i+5j)$
##### b)
Let $a=i_2j, d-2i+3j$
$\therefore r(t)=i_2j + t(2i+3j)$
##### c)
let $a=3i-5j+4k$, $b=-4k+3j+10k$, $d=a-b$ (we do this because now we can deal with less negative numbers. doing both ways is valid however this will reverse the $t$ axis
$d=a-b=7i-8j-6k$
$\therefore r(t)=a+td=ei-5j+4k+t(7i-8j-6k$)
we could do $r(t)=a-td$ however this would negate the value of $t$, like mentioned ealier

#### Example 5.10
##### a)
We just take the given vector equation for $r$ and suibstitute in a different point.
$r(s)=i+3j+2k+s(-i-3j)$

##### b)
Let $d=ai+bj+0k $(\because$ || to x-y plane$)$
We have $(-i-3j) \times (ai+bj)=0$
$\therefore -a+-3b=0$
$\therefore a=-3b$

Let $b=-1$ because we can literally choose any value as long as the relationship $a=-3b$ holds. We are just defining how big we want the vector.
$\therefore a=3$
$\therefore 3i-j$ is a possible parralel vector

$\therefore i+3j+2k+s(3i-j)$
#### Example 5.11
##### a)
This can also simplify to $r(t)=i+2j+2k+t(-i-3j)$
We want to find the shortest distance between the origin and the point. We want the shortest path possible. 
How do we know which path will be the shorest?
We want to find the path that is perpandicular to the vector

![[Example 2.png]]

We require $P(x, y, z)$ such that $P$ is on the line and $OP$ is *parralel* to the line
i.e) $\vec{OP}\times d = 0$, Remember $d=-i-3j$ as simplified earlier.

We have $((1-t)i+(2-3t)j + 2k)(-i-3j)=0$
$(t-1)+(9t-6)+0=0$
$\therefore 10t-7=0 \therefore t=\frac{7}{10}$
Now we substitute into $r(t)=i+2j+2k+t(-i-3j)$
$\therefore \vec{OP}=(-1\frac{7}{10})i + (2-3\times \frac{7}{10}+2k$
$=\frac{3}{10}i-\frac{1}{10}j+2k$
$\therefore |\vec{OP}|=\sqrt{(\frac{3}{10})^2+(\frac{-1}{10})^2+2^2}=\frac{\sqrt{410}}{10}$

#### Example 5.12
##### a) **THIS IS ON THE EXAM!!!!**
**embed example 3**
$r(t)=a+t(b-a), t\epsilon \mathbb{R}$
$=i-4j+t((2-3)i+(0--4)j+(-3-0)k)$
$=i-4j+t(i_4j-4k), t\epsilon \mathbb{R}$
##### b)

We are looking for a 'domain' for $t$ that describes the segment $AB$
For $A$: we require 
$i+4j+t(i-4j-3k) = i-4j$ 
Clearly $t=0$, because clearly.
For $B$: We require 
Consider $i+4j+t(i-4j-3k) =...$
$=(1+t)i + (-4+4t)j + (-3t)k=2i-3k$

Equating coefficients
$\therefore i+t$
$4t+4=0$
$-3t=-3$

Clearly $t=1$ solves all
$\vec{AB}< r(t), t\epsilon [0, 1]

##### c) 
For C: (1+t)i+(4t-4)j+(-3t)k=4i+8j-9k$ 
We will check them all to make sure that for all equated coefficients, $t$ is the same. 
$\therefore 1+t=4 \Rightarrow t=3$ 
$4t-4=8 \Rightarrow t=3$
$-3t=-9 \implies t=3$

$\therefore $t=3$
