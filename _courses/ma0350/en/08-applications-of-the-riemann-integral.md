---
layout: chapter
course: ma0350
chapter: 8
title: "Applications of the Riemann Integral"
slug: 08-applications-of-the-riemann-integral
toc:
  sidebar: right
lang: en
fecha: 2025-05-27
permalink: /notes/ma0350/08-applications-of-the-riemann-integral/
---

{% raw %}
These notes present applications of the Riemann integral
## Area under a curve

#### Example 
Find the area enclosed between the curves $$f(x) = 2x$$ + $$g(x) = x^{3}$$. 

***Solution:*** First we must graph the functions. In particular, we must find the limits of integration. To do so, we set the two functions equal:
![Pasted image 20250527143919](/assets/img/courses/ma0350/Pasted%20image%2020250527143919.png)
Note that $$x^{3} = 2x \iff x= \pm \sqrt{ 2 } \quad \lor \quad x=0$$. Hence the area between the curves is given by 


$$
\int_{-\sqrt{ 2 }}^{0}( x^{3}-2x) \, dx + \int_{0}^{\sqrt{ 2 }} (2x-x^{3})  \, dx  = 2.
$$



#### Example 
Find the area between the curves $$f(x) = x^{3}, g(x) = 2x$$, $$h(x) = x$$ for $$0 \leq x \leq \sqrt{ 2 }$$.![Pasted image 20250527144810](/assets/img/courses/ma0350/Pasted%20image%2020250527144810.png)Consider the solution of $$x^{3} = x \iff x=\pm 1   \lor   x=0$$. Hence the area is given by 


$$
\int_{0}^{1} (2x-x) \, dx + \int_{1}^{\sqrt{ 2 }}  (2x-x^{3})\, dx.
$$



## Arc length of a curve
Let $$f(x) = \sin(x)$$. We want to know the length of the curve, i.e., how long it would measure if we straightened it out. We can approximate the length using rectangles and measuring the segments between the vertices of the rectangles. The length of the segments is given by 


$$
\sqrt{ (f(a_{i+1})-f(a_{i}))^{2} + (a_{i+1}-a_{i})^{2}}.
$$


Moreover, if $$f$$ is differentiable, then by the mean value theorem there exists $$\xi_{i}$$ such that $$f(a_{i+1})-f(a_{i}) = f'(\xi_{i})(a_{i+1}-a_{i})$$. Substituting this into the approximation of the segment, its value is given by 


$$
(a_{i+1}-a_{i}) \sqrt{ (f'(\xi_{i}))^{2} + 1 }.
$$


Summing over all the intervals, the segments measure 


$$
\sum_{i=0}^{n-1} (a_{i+1}-a_{i}) \sqrt{ (f'(\xi_{i}))^{2} + 1 } = S(\sqrt{ (f')^{2}+1 }, P, \xi_{1},\dots,\xi_{n}). 
$$


If the sum converges, the length of the curve is 


$$
\int_{a}^{b} \sqrt{ (f'(x))^{2} + 1 } \, dx .
$$


The sum converges whenever $$f'$$ is continuous.
{% endraw %}
