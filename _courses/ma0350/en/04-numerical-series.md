---
layout: chapter
course: ma0350
chapter: 4
title: "Numerical Series"
slug: 04-numerical-series
toc:
  sidebar: right
lang: en
fecha: 2025-03-25
permalink: /notes/ma0350/04-numerical-series/
---

{% raw %}
In this note we define series in terms of the partial sums of sequences. See also: Convergence tests for series, Series of functions.

Consider the sequence $$\{x_{n}\}_{n=0}^\infty$$, where $$x_{n} = a^{n}$$. Consider the following sequence:


$$
\begin{aligned}
S_{0} &= 1 \\
S_{1} &= 1+a \\
S_{2} &= 1+a+a^{2} \\
 &  \quad  \quad \vdots \\
S_{n} &= 1+a+\dots+a^{n}.\\
&= \frac{1-a^{n+1}}{1-a} \quad\text{for $a \neq 1$.}
\end{aligned}
$$



Then, if $$\lvert a \rvert < 1$$, we have that $$\lim_{ n \to \infty } S_{n} = \frac{1}{1-a}$$. Therefore $$\sum_{n=0}^\infty a^{n} = \frac{1}{1-a}$$ for $$a \in (-1,1)$$. 

## Numerical series and convergence
### Definition (Partial sums)

Given a sequence $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$, we define the sequence of partial sums $$\{S_{n}\}_{n=0}^\infty$$ as follows 


$$
\begin{aligned}
S_{0} &= a_{0} \\
S_{1} &= a_{0}+a_{1} \\
S_{2} &= a_{0}+a_{1}+a_{2} \\
 &  \quad  \quad \vdots \\
S_{n} &= a_{0}+a_{1}+\dots+a_{n}.\\
&= \sum_{k=1}^{n} a_{k}
\end{aligned}
$$




### Definition (Convergence of series)

Given a sequence $$\{x_{n}\}_{n=0}^\infty$$, we say that the series $$\sum_{n=0}^\infty x_{n}$$ converges if the limit $$\lim_{ n \to \infty } S_{n} = \lim_{ n \to \infty } \sum_{k=0}^{n} x_{n} = L \in \mathbb{R}$$ exists, in which case we say that $$\sum_{n=0}^\infty x_{n} = L$$. 
 
### Example 1: Geometric series

As we saw at the start, if $$x_{n} = a^{n}$$, then $$S_{n} = \frac{1-a^{n+1}}{1-a}$$. The series converges to $$\frac{1}{1-a}$$ if and only if $$\lvert a \rvert < 1$$.

### Example 2: Telescoping series

Given $$\{a_{n}\}_{n=0}^\infty$$, define $$x_{0} := a_{0}$$ and $$x_{n+1} := a_{n+1}-a_{n}$$, for $$n \geq 1$$. Then


$$
\begin{aligned}
S_{n} &= x_{0}+x_{1}+\dots x_{n} \\
&= a_{0}+(a_{1}-a_{0}) + (a_{2}-a_{1}) + \dots + (a_{n}-a_{n-1}) \\
&= a_{n}.
\end{aligned}
$$


Note that $$\sum_{n=0}^\infty x_{n} = \lim_{ n \to \infty } S_{n} = \lim_{ n \to \infty } a_{n}$$. The series converges if and only if $$\{a_{n}\}_{n=0}^\infty$$ converges, in which case they converge to the same value.

In general, it is hard to compute the value a series converges to when it is neither geometric nor telescoping. There are, however, several tests that make it possible to determine whether the series converges without necessarily knowing the value it converges to. In general, if $$\{a_{n}\}_{n=1}^\infty$$ is a sequence, then 


$$
\sum_{n=k}^\infty (a_{n}-a_{n+1}) = a_{k} - \lim_{ n \to \infty } a_{n+1}.
$$


The series converges if the sequence converges.
{% endraw %}
