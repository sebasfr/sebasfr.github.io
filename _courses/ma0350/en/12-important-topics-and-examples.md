---
layout: chapter
course: ma0350
chapter: 12
title: "Important Topics and Examples"
slug: 12-important-topics-and-examples
toc:
  sidebar: right
lang: en
fecha: 2025-04-10
permalink: /notes/ma0350/12-important-topics-and-examples/
---

{% raw %}
Here are some useful tools for assessing the convergence of series. See also: Series of functions (Taylor series).
### Example 

Let $$\alpha \in \mathbb{R}$$; then


$$
\begin{aligned}
\lim_{ n \to \infty } \frac{\ln(n^{\alpha})}{n}  &= \alpha \lim_{ n \to \infty } \frac{\ln (n)}{n}   \\
&\overset{\text{L'H}}{=} \alpha \lim_{ n \to \infty } \frac{1}{n} \\
&= 0.
\end{aligned}
$$



## Asymptotic expansions

![Pasted image 20250428210634](/assets/img/courses/ma0350/Pasted%20image%2020250428210634.png)

Some examples are:
![WhatsApp Image 2025-04-29 at 16.01.57_39813150](/assets/img/courses/ma0350/WhatsApp%20Image%202025-04-29%20at%2016.01.57_39813150.jpg)

We can approximate functions using Taylor polynomials with asymptotic expansions. For example, $$(1+x)^{\alpha} = 1+\alpha x+o(x)$$, where we treat the remainder as Landau's little $$o$$ *notation*, so that $$\lim_{ x \to 0} \frac{o(x)}{x} = 0$$. In the same way, 


$$
(1+x)^{\alpha} = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2} x^{2} + o(x^{2}).
$$


Now, $$o(x) + o(x^{2}) = o(x)$$, since 


$$
\lim_{ x \to 0 } \frac{o(x^{2})}{x^{2}} x = 0.
$$



#### Example:


$$
\sqrt{ n^{2}+1 } -\sqrt[3]{n^{3}+1} = \underbrace{ n\left( \left( 1+\frac{1}{n^{2}} \right)^{1/2} - \left( 1+\frac{1}{n^{3}} \right)^{1/3} \right) }_{ \ast }.
$$


Applying asymptotic expansions, note that 


$$
\left( 1+\frac{1}{n^{2}} \right)^{1/2} = 1+\frac{1}{2} \cdot \frac{1}{n^{2}} + o\left( \frac{1}{n^{2}} \right),
$$




$$
\left( 1+\frac{1}{n^{3}} \right)^{1/3} = 1 + \frac{1}{3} \cdot\frac{1}{n^{3}} + o\left( \frac{1}{n^{3}} \right).
$$


Then, substituting into the initial expression, 


$$
\ast = n\left(\frac{1}{2n^{2}} - \frac{1}{3n^{3}} + o\left( \frac{1}{n^{2}} \right)\right) = \frac{1}{2n} + \frac{1}{3n^{2}} + no\left( \frac{1}{n^{2}} \right) = \frac{1}{2n} + \frac{1}{3n^{2}} + o\left( \frac{1}{n} \right).
$$


***CAREFUL:*** $$o(x^{2}) = x o(x)$$ and $$o(x^{n}) = x o(x^{n-1})$$. 

Then $$\lim_{ n \to \infty } \frac{\frac{1}{2n} - \frac{1}{3n^{2}} + o\left( \frac{1}{n} \right)}{\frac{1}{n}} = \frac{1}{2}$$, so by limit comparison $$\sum_{n=1}^\infty \sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}$$ diverges. 
 
#### Example 
Consider $$\sum_{n=1}^\infty \frac{\sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}}{n^{p}}$$. For which values of $$p$$ does it converge? Note that, by the asymptotic expansion above, 


$$
\frac{\sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}}{n^{p}} \approx \frac{1}{n^{p}},
$$


since 


$$
\lim_{ n \to \infty } \frac{\frac{\sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}}{n^{p}}}{\frac{1}{n^{p+1}}} = \lim_{ n \to \infty } \frac{\frac{1}{2n} - \frac{1}{3n^{2}} + o\left( \frac{1}{n} \right)}{\frac{1}{n}} = \frac{1}{2}.
$$



Therefore the series converges if and only if $$\sum_{n=q}^\infty \frac{1}{n^{p+1}}$$ converges, i.e., if $$p>0$$. 
 
#### Example 
Consider the series $$\sum_{n=1}^\infty \frac{\left( 1-\frac{1}{n} \right)^{n}}{n}$$. First, note that 


$$
\left( 1-\frac{1}{n^{2}} \right)^{n} = e^{\ln(1-1/n^{2})^{n}} = e^{n\ln(1-1/n^{2})}.
$$


Recall that 


$$
\ln(1+x) = x + o(x) = x - \frac{x^{2}}{2} + o(x). 
$$


Then, to first order, we have that 


$$
\ln\left( 1-\frac{1}{n^{2}} \right) = -\frac{1}{n^{2}} + o\left( \frac{1}{n^{2}} \right).
$$


Hence we have that 


$$
n \ln\left( -\frac{1}{n^{2}}+o\left( \frac{1}{n^{2}} \right) \right) = n\left( -\frac{1}{n^{2}}+o\left( \frac{1}{n^{2}} \right) \right) = -\frac{1}{n} + o\left( \frac{1}{n} \right).
$$


So $$\left( 1-\frac{1}{n^{2}} \right)^{n} \underset{n \rightarrow \infty}{\longrightarrow} 1$$, and therefore, by limit comparison, $$\frac{\left( 1-\frac{1}{n} \right)^{n}}{n} \approx \frac{1}{n}$$. Hence the series diverges. 
 
#### Example 
Consider $$\sum_{n=1}^\infty (-1)^{n} e^{-pn}$$. For which values of $$p$$ does it converge? 
Note that the series converges absolutely if $$p>0$$. If $$p\leq 0$$, then $$(-1)^{n} e^{-pn} \underset{n \rightarrow \infty}{\cancel{ \longrightarrow }}$$ 0, i.e., it diverges. 
 
#### Example 
Consider $$\sum_{n=1}^\infty \frac{n^{n}}{n! 2^{n}}$$. Applying the ratio test, note that 


$$
\lim_{ n \to \infty } \frac{\frac{(n+1)^{n+1}}{(n+1)!2^{n+1}}}{\frac{n^{n}}{n! 2^{n}}} = \lim_{ n \to \infty } (\frac{(n+1)^{n+1}}{2(n+1)n^{n}} = \frac{1}{2}\lim_{ n \to \infty } \left( \frac{n+1}{n} \right)^{n} = \frac{e}{2} > 1.
$$


Hence the series diverges.

## Stirling's formula


$$
\lim_{ n \to \infty } \frac{n!}{\left( \frac{n}{e} \right)^{n} \sqrt{ 2 \pi n }} = 1 \implies n! \approx \left( \frac{n}{e} \right)^{n} \sqrt{ 2 \pi n }.
$$


 
#### Example
In the previous example, 


$$
\frac{n^{n}}{2^{n}n!} \approx \left( \frac{e}{2} \right)^{n} \frac{1}{\sqrt{ 2\pi n }}
$$



#### Example 
Let $$a_{n}\geq_{0}$$ be such that $$\sum_{n=1}^\infty a_{n}$$ converges. Does the series $$\sum_{n=1}^\infty a_{n}^{3}$$ converge? Note that 


$$
\lim_{ n \to \infty } \frac{a_{n}^{3}}{a_{n}} = \lim_{ n \to \infty } a_{n}^{2} = 0. 
$$


Another way to see it is that $$a_{n}^{3} \leq a_{n}$$ whenever $$a_{n} < 1$$. 
 
#### Example 
Consider $$\sum_{n=1}^\infty (-1)^{n} (1+\frac{1}{n})$$. Note that the terms do not converge to zero, since $$\lim_{ n \to \infty } (-1)^{n}\left( 1+\frac{1}{n} \right) = 1$$. Therefore the series diverges. 
 
#### Example 
Consider $$\sum_{n=1}^\infty \sinh(n) = \sum_{n=1}^\infty \frac{e^{n} - e^{-n}}{2}$$.  The series diverges, since $$\sum_{n=1}^\infty \frac{e^{n}}{2}$$ diverges and $$\sum_{n=1}^\infty e^{-n}$$ converges.
![Pasted image 20250428212044](/assets/img/courses/ma0350/Pasted%20image%2020250428212044.png)

#### Example 
Compute the value that the series $$\sum_{n=0}^\infty n(n-1)x^{n}$$ converges to, with $$\lvert x \rvert < 1$$. 

## The arctangent formula

This formula is useful for computing series involving the arctangent. 


$$
\arctan\left( \frac{x-y}{1+xy} \right) = \arctan(x) - \arctan(y).
$$



## Trigonometric inequalities.

For every $$x \in \mathbb{R}$$, we have that 


$$
\lvert \sin(x) \rvert \leq \lvert x \rvert \leq  \lvert \tan(x) \rvert .
$$



If $$x < \frac{\pi}{2}$$ 


$$
\sin(x) > \frac{x}{2}
$$


## Definition of supremum and infimum
![Pasted image 20250430225646](/assets/img/courses/ma0350/Pasted%20image%2020250430225646.png)

![Pasted image 20250430225732](/assets/img/courses/ma0350/Pasted%20image%2020250430225732.png)
![Pasted image 20250430225747](/assets/img/courses/ma0350/Pasted%20image%2020250430225747.png)
{% endraw %}
