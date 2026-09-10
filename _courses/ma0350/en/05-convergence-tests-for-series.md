---
layout: chapter
course: ma0350
chapter: 5
title: "Convergence Tests for Series"
slug: 05-convergence-tests-for-series
toc:
  sidebar: right
lang: en
fecha: 2025-04-01
permalink: /notes/ma0350/05-convergence-tests-for-series/
---

{% raw %}
What follows presents several convergence tests for numerical series. See also: Important topics and examples, Series of functions.
Let $$\{x_{n}\}_{n=0}^\infty$$ be a sequence. Consider 


$$
S_{n} = \sum_{i=1}^{n}  x_{k} = x_{1} + x_{2} +\dots+x_{n}
$$


We say that $$\sum_{k=0}^{\infty} x_{k}$$ converges if $$\lim_{ n \to \infty } S_{n}$$ exists

### Cauchy condition

The series $$\sum_{n=1}^\infty x_{n}$$ converges if and only if for every $$\varepsilon > 0$$ there exists $$N \in \mathbb{N}$$ such that 


$$
\lvert S_{n} - S_{m} \rvert < \varepsilon \quad \text{for all \quad$n,m \geq N$}  
$$




$$
\iff \lvert x_{n+1} + x_{n+2} + \dots + x_{m} \rvert < \varepsilon  \quad \text{if  \quad$m > n$}
$$


The series converges if and only if it is Cauchy.

#### Example 

Consider $$x_{n} = \frac{1}{n}, n\geq 1$$. We will prove that $$S_{2n} - S_{n} \geq \frac{1}{2}$$.  Note that 


$$
\begin{aligned}
S_{2n} - S_{n} &= \left( 1+\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{2n} \right) -\left( 1+\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{n} \right) \\
&= \frac{1}{n+1} + \frac{1}{n+2} +\dots +\frac{1}{2n-1} + \frac{1}{2n} \\
&\geq \frac{1}{2n} + \frac{1}{2n} + \dots +\frac{1}{2n} + \frac{1}{2n} = \frac{n}{2n} = \frac{1}{2}.
\end{aligned}
$$


Hence the Cauchy condition fails for $$\varepsilon < \frac{1}{2}$$.

Consider the case $$x_{n} \geq 0$$. Then 


$$
S_{n+1} = S_{n} + x_{n+1}\geq S_{n}
$$




$$
\implies S_{n+1} - S_{n} = x_{n+1}.
$$



### Lemma (Boundedness of partial sums):

Let $$\{x_{n}\}_{n=1}^\infty$$ be such that $$x_{n} \geq 0$$ \. Then
1. $$\sum_{n=0}^{\infty}x_{n}$$  converges if there exists $$M$$ such that $$\lvert S_{n} \rvert \leq M$$ for every $$n$$.
2. Otherwise the $$S_{n}$$ are unbounded, i.e., $$\lim_{ n \to \infty }S_{n} = \infty$$.

### The p-series test

#### Example 

Consider


$$
\sum_{n=1}^{\infty} \frac{1}{n} = +\infty 
$$


***Proof:*** If $$x_{n} \geq 0$$, then the $$S_{n}$$ are increasing. Hence $$S_{n}$$ converges if and only if it is bounded. Take $$M > 0$$; there exists $$N$$ such that $$S_{N} > M$$. Then, for $$n\geq N$$, 


$$
S_{n} \geq S_{N} > M.
$$



#### Example 

Consider $$x_{n} = \frac{1}{n^2}$$, that is,


$$
\sum_{n=1}^{\infty}  \frac{1}{n^2}.
$$


We know that $$\lim_{ n \to \infty }S_{n} = \infty$$ or $$\lim_{ n \to \infty } S_{n} = l \in \mathbb{R}$$.
Note that:


$$
\begin{aligned}
S_{1} =& 1 \\
S_{2} =& 1 + \frac{1}{2^2} \\
S_{3} =& 1 + \frac{1}{2^2} + \frac{1}{3^2} \leq 1 + \frac{1}{2^2} + \frac{1}{2^2} = 1+\frac{1}{2} \\
S_{7} =& 1 + \frac{1}{2^2} + \frac{1}{3^2} + \dots + \frac{1}{7^2} \leq 1 + \frac{1}{2} + \frac{1}{4^{2}} + \frac{1}{4^{2}} + \frac{1}{4^{2}} + \frac{1}{4^{2}} \\
=&1 + \frac{1}{2} + \left( \frac{1}{2} \right)^2.
\end{aligned}
$$


Consider 


$$
S_{2^j -1} = S_{n_{j}}.
$$


We will prove that $$S_{n_{j}} \leq \sum_{n=0}^{j-1} \left( \frac{1}{2} \right)^n \quad \text{(*)}$$.
We have already done the base case. For the inductive step, suppose that $$\text{(*)}$$ holds. We must show that 


$$
S_{n_{j+1}} \leq \sum_{n=0}^{j+1} \left( \frac{1}{2} \right)^n.
$$


Note that 


$$
\begin{aligned}
S_{n_{j+1}} &= S_{n_{j}} + x_{2^j} + x_{2^{j}+1} + \dots + x_{2^{j+1}-1} \\
&\leq  \sum_{n=0}^{j} \left( \frac{1}{2} \right)^n + \frac{2^j}{(2^j)^{2}}  = \sum_{n=0}^{j-1} \left( \frac{1}{2} \right)^n + \left( \frac{1}{2} \right)^j = \sum_{n=1}^{j} \left( \frac{1}{2} \right)^n 
\end{aligned}
$$


Since 


$$
\sum_{n=0}^\infty \left( \frac{1}{2} \right)^n = \frac{1}{1-\frac{1}{2}}.
$$



it is bounded, so $$S_{2^{j+1} - 1} \leq M$$, and therefore it converges. 

We know that 


$$
\sum_{n=1}^\infty \frac{1}{n} = +\infty
$$




$$
\sum_{n=1}^\infty \frac{1}{n^{2}} \quad \text{converges}.
$$


Let $$0<p<1$$. Then 


$$
n > n^p \implies \frac{1}{n^p} > \frac{1}{n} \implies \sum_{k=0}^\infty \frac{1}{k^p} > \sum_{k=0}^\infty \frac{1}{k} \rightarrow \infty
$$


Therefore it diverges to infinity. If $$p>2$$, then 


$$
\frac{1}{n^2} > \frac{1}{n^p},
$$


so $$\sum_{n=1}^\infty \frac{1}{n ^p}$$ converges. 

In general, if $$p > 1$$, the series $$\sum_{n=1}^\infty \frac{1}{n^p}$$ converges.

### Exercise: 

Let $$x_{n} = \frac{1}{n^{p}}$$, with $$p > 1$$. Show that 


$$
S_{2^j - 1} \leq \sum_{i=0}^{j-1} \frac{1}{2^{j-1}} 
$$



### Theorem (Comparison)

Let $$\{x_{n}\}_{n=0}^\infty$$ and $$\{z_{n}\}_{n=0}^\infty$$ be such that $$0\leq x_{n}\leq z_{n}$$ for every $$n\geq 1$$. Then
- If $$\sum_{n=1}^\infty z_{n}$$ converges, then $$\sum_{n=1}^\infty x_{n}$$ converges.
- If $$\sum_{n=1}^\infty x_{n}$$ diverges, then $$\sum_{n=1}^\infty z_{n}$$ diverges.

### Example 

Consider 


$$
x_{n} = \frac{1}{\sqrt{ n^{3}+1 }} \leq \frac{1}{\sqrt{ n^{3} }} = \frac{1}{n^\frac{3}{2}}
$$


Therefore $$\sum_{n=0}^\infty x_{n}$$ converges.

### Lemma (Limit comparison) 

Let $$\{x_{n}\}_{n=1}^\infty$$ and $$\{z_{n}\}_{n=1}^\infty$$ be sequences such that $$x_{n} \geq 0$$ and $$z_{n} \geq 0$$ for $$n\geq1$$.
1. If $$\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = l \neq 0$$, then either both converge or both diverge to infinity.
2. If $$\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = 0$$, 
 - then $$\sum_{n=0}^\infty x_{n}= +\infty$$ implies  $$\sum_{n=0}^\infty z_{n}= +\infty$$.
 - then, if $$\sum_{n=0}^\infty z_{n}$$ converges then $$\sum_{n=0}^\infty x_{n}$$ converges
3. If $$\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = \infty$$, 
 - then $$\sum_{n=0}^\infty z_{n}= +\infty$$ implies  $$\sum_{n=0}^\infty x_{n}= +\infty$$.
 - then, if $$\sum_{n=0}^\infty x_{n}$$ converges then $$\sum_{n=0}^\infty z_{n}$$ converges

***Proof of (a):*** Assume that 


$$
\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = l > 0.
$$


Given $$\varepsilon > 0$$, there exists $$N \in \mathbb{N}$$ such that for every $$n \geq N$$ 


$$
l - \varepsilon < \frac{x_{n}}{z_{n}} < l + \varepsilon \implies (l-\varepsilon) z_{n} < x_{n} < (l+\varepsilon) z_{n}. 
$$


Taking $$\varepsilon$$ such that $$0<\varepsilon< \frac{l}{2}$$, we get $$0 \leq (l-\varepsilon) z_{n} < x_{n}$$.
Note that 


$$
0 \leq (l - \varepsilon) \sum_{k=1}^\infty z_{k} \leq \sum_{k=1}^\infty x_{k} \leq (l+\varepsilon) \sum_{n=0}^\infty z_{n}
$$


If $$\sum_{k=0}^\infty x_{k}$$ converges, then by comparison $$\sum_{k=0}^\infty z_{k}$$  

### Example 

$$\sum_{n=0}^\infty \frac{1}{n^{5}-n^{3}+1}$$ behaves like $$\sum_{n=1}^\infty \frac{1}{n^{5}}$$ since 


$$
\lim_{ n \to \infty } \frac{\left( \frac{1}{n^{5}-n^{3}+1} \right)}{\left( \frac{1}{n^{5}} \right)} = \lim_{ n \to \infty } \frac{n^{5}}{n^{5}-n^{3}+1} = 1
$$



### Example 

$$\sum_{n=0}^\infty \frac{2^{3n}+n^{5}}{10^{n}}$$ behaves like $$\sum_{n=1}^\infty \left( \frac{8}{10} \right)^{n}$$ since 


$$
\lim_{ n \to \infty } \frac{\frac{2^{3n}+n^{5}}{10^{n}}}{\left( \frac{8}{10} \right)^{n}} = 1
$$



### Lemma (Root test)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence. Consider 


$$
\lim_{ n \to \infty } \sqrt[n]{ \lvert x_{n} \rvert  }.
$$


- If $$\lim_{ n \to \infty }  \sqrt[n]{ \lvert x_{n} \rvert  } = l < 1$$, then $$\sum_{n=0}^\infty \lvert x_{n} \rvert$$ converges.

***Proof:*** Let $$\varepsilon > 0$$ be such that $$0 < l+\varepsilon < 1$$. Then there exists $$N \in \mathbb{N}$$ such that for every $$n \geq \mathbb{N}$$ 


$$
l-\varepsilon <  \sqrt[n]{ \lvert x_{n} \rvert  } < l + \varepsilon \implies \lvert x_{n} \rvert <(l+\varepsilon)^n
$$


for $$n \geq N$$. Hence the series converges by comparison. 

- If $$\lim_{ n \to \infty }  \sqrt[n]{ \lvert x_{n} \rvert  } = l > 1$$, then $$\sum_{n=0}^\infty \lvert x_{n} \rvert +\infty.$$

### Example

For $$a>0$$ let $$x_{n}=\frac{a^{n}}{n^{n}}$$, with $$n\geq{1}$$. Then 


$$
\lim_{ n \to \infty } \sqrt[n]{\frac{a^{n}}{n^{n}}} = \frac{a}{n} = 0.
$$


Therefore $$\sum_{n=1}^\infty \frac{a^{n}}{n^{n}}$$ converges.

### Lemma (Ratio test)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence. Consider 


$$
\lim_{ n \to \infty } \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert}
$$


If $$\lim_{ n \to \infty }   \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert} = l < 1$$, then $$\sum_{n=0}^\infty \lvert x_{n} \rvert$$ converges.

If $$\lim_{ n \to \infty } \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert} = l >1$$, then $$\sum_{n=0}^\infty \lvert x_{n} \rvert = +\infty$$ .

***Proof:*** Let $$\varepsilon > 0$$ be such that $$l-\varepsilon > 1$$. Then there exists $$N \in \mathbb{N}$$ such that for every $$n \geq \mathbb{N}$$ 


$$
l-\varepsilon <  \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert}  \implies (l-\varepsilon) \lvert x_{n} \rvert < \lvert x_{n+1} \rvert 
$$


Then, iterating, 


$$
\lvert x_{N+k} \rvert \geq (l-\varepsilon)^k \lvert x_{N} \rvert 
$$


Since $$(l-\varepsilon) > 1$$, $$\sum_{k=1}^\infty(l-\varepsilon)^k = +\infty$$. Hence by comparison, $$\sum_{n=0}^\infty \lvert x_{n} \rvert = +\infty$$.

### Example 

Consider $$x_{n} = \frac{a^n}{n!}$$ with $$a>0$$. Note that 


$$
\lim_{ n \to \infty } \left\lvert  \frac{a_{n+1}}{a_{n}}  \right\rvert = \lim_{ n \to \infty } \frac{a}{n+1} = 0.
$$


Hence $$\sum_{n=0}^\infty x_{n}$$ converges.


### Theorem (Absolute convergence):

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence. If $$\sum_{n=1}^\infty \lvert x_{n} \rvert$$ converges, then $$\sum_{n=1}^\infty x_{n}$$ converges.

***Proof:*** Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence. Then 


$$
\lvert x_{n} \rvert - x_{n} \leq 2 \lvert x_{n} \rvert
$$


for every $$n \geq 1$$. Assume that $$\sum_{n=0}^\infty \lvert x_{n} \rvert$$ converges to L. Then 


$$
\sum_{n=0}^\infty 2 \lvert x_{n} \rvert = 2L.
$$


We conclude then that $$\sum_{n=0}^\infty \lvert x_{n} \rvert - x_{n}$$ converges.
Let


$$
S_{n} = \sum_{k=0}^n \lvert x_{k} \rvert - x_{k},
$$





$$
\hat{S}_{n} = \sum_{k=0}^{n} \lvert x_{k} \rvert  
$$


Then $$\hat{S}_{n} - S_{n} = \sum_{k=0}^{n} x_{k}$$. Therefore $$\sum_{n=0}^\infty x_{n}$$ converges.

### Theorem (Convergence of a product of series) 

Consider two sequences $$\{x_{n}\}_{n=0}^\infty$$ and $$\{y_{n}\}_{n=0}^\infty$$. If
1. $$\lvert y_{k} \rvert \leq M$$ for $$k \geq 1$$.
2. $$\sum_{k=1}^\infty \lvert x_{k} \rvert$$ converges,
then $$\sum_{k=1}^\infty \lvert x_{k} y _{k} \rvert$$ converges.

***Proof:*** Consider two sequences $$\{x_{n}\}_{n=1}^\infty$$ and $$\{y_{n}\}_{n=1}^\infty$$. We want to study the convergence of $$\sum_{n=1}^\infty x_{n} y_{n}$$. Assume that $$\lvert y_{k} \rvert \leq M$$ for $$k \geq 1$$ and that $$\sum_{k=1}^\infty \lvert x_{k} \rvert$$ converges. Note that 


$$
\sum_{k=1}^\infty \lvert x_{k}y_{k} \rvert \leq \sum_{k=1}^\infty M \lvert x_{k} \rvert = M \sum_{k=1}^\infty \lvert x_{k} \rvert 
$$


Conclude that $$\sum_{k=1}^\infty \lvert x_{k}y_{k} \rvert$$ converges, and hence $$\sum_{k=1}^\infty x_{k} y_{k}$$ converges.

### Example

$$x_{k} = \frac{\sin k}{k^2}$$. Note that $$\lvert \sin k \rvert \leq 1$$ and $$\sum_{k=1}^\infty \frac{1}{k^{2}}$$ converges

**A more general trick**: Consider $$\sum_{k=1}^{n} x_{k} y_{k}$$. Take $$S_{k} = \sum_{k=1}^{n} y_{n}$$. Then $$y_{k} = S_{k} - S_{k-1}$$. Expanding:


$$
\sum_{k=1}^{n} x_{k} y_{k} =  \sum_{k=1}^{n} x_{k} (S_{k} - S_{k-1}) = \sum_{k=1}^{n} x_{k} S_{k} - \sum_{k=0}^{n} x_{k+1} S_{k} = \sum_{k=1}^{n-1} S_{k}(x_{k} - x_{k+1}) + x_{n} S_{n} - x_{1}S_{0}.
$$


In fact, for $$m \leq n$$, we have that


$$
\sum_{k=m}^{n} x_{k}y_{k} = \sum_{k=m}^{n} (x_{k}-x_{k+1}) S_{k} + x_{n}S_{n} - x_{m}S_{m-1}.
$$




### Theorem (Dirichlet's test)

Let $$\{x_{n}\}_{n=1}^\infty$$ and $$\{y_{n}\}_{n=1}^\infty$$ be such that 
1. $$x_{n} \geq x_{n+1}$$ for every $$n \in \mathbb{N}$$,
2. $$\lim_{ n \to \infty } x_{n} = 0$$,
3. there exists $$M \in \mathbb{R}$$ such that for every $$n \in \mathbb{N}$$, $$\lvert  \sum_{k=1}^n y_{k} \rvert \leq M$$ for every $$n  \in \mathbb{N}$$.
Then $$\sum_{n=1}^\infty x_{n}y_{n}$$ converges.

***Proof:*** Let $$k \leq l$$, then 


$$
\begin{aligned}
\left\lvert  \sum_{n=k}^{l} x_{n}y_{n}   \right\rvert &\leq  \sum_{n=k}^{l-1} \lvert x_{n}-x_{n+1} \rvert \lvert S_{n} \rvert +\lvert x_{l} \rvert \lvert S_{l} \rvert + \lvert x_{k} \rvert \lvert S_{k-1} \rvert \\
&\leq \sum_{n=k}^{l-1} (x_{n}-x_{n+1}) M + \lvert x_{l} \rvert M + \lvert x_{k} \rvert M \\
&=M(x_{k}-x_{l}) + Mx_{l} + Mx_{k} = 2Mx_{k}
\end{aligned}
$$


since $$x_{n}\geq_{0}$$. Moreover, since $$\lim_{ n \to \infty } x_{n} = 0$$, there exists $$N \in \mathbb{N}$$ such that $$\lvert x_{k} \rvert < \frac{\varepsilon}{2M}$$ if $$k \geq N$$, for a fixed and arbitrary $$\varepsilon > 0$$. Hence, if $$l \geq l \geq N$$, we have that 


$$
\left\lvert  \sum_{n=k}^{l}  x_{n} y_{n} \right\rvert  < \varepsilon.
$$


Therefore the series is Cauchy and converges.

#### Example 

Consider $$\sum_{n=1}^\infty \frac{(-1)^{n}}{n}$$. Take $$x_{n} = \frac{1}{n}$$, $$y_{n} = (-1)^{n}$$. Then 


$$
S_{n} = \sum_{k=1}^{n} y_{k},\quad \text{In particular, }S_{1} =-1, S_{2} = 0 , S_{3} = -1,\dots
$$


Hence $$S_{n}$$ is bounded. Therefore $$\sum_{n=1}^\infty \frac{(-1)^{n}}{n}$$ converges. 

### Lemma (Alternating series convergence)  

Let $$\{x_{n}\}_{n=1}^\infty$$ be such that $$\lim_{ n \to \infty } x_{n} = 0$$ and $$x_{n+1} \leq x_{n}$$ for every $$n\geq1$$. Then $$\sum_{n=1}^{\infty} (-1)^{n} x_{n}$$ converges.

### Example 
$$x_{n} = \frac{1}{\sqrt{ n }}$$, $$x_{n}=\frac{1}{\ln(n+1)}$$.

Consider $$y_{n} = \cos(nx)$$, with $$x \in [0,2\pi)$$. We want to bound $$\sum_{k=1}^\infty \cos(nx)$$ for $$x \neq 0$$ and $$x \neq \pi$$. Note that 


$$
\begin{aligned}
\sin\left( \left( k-\frac{1}{2} \right)x \right) - \sin\left( \left( k+\frac{1}{2} \right)x \right) &= 2 \cos(kx) \sin\left( \frac{x}{2} \right) \\
\iff \cos(kx) &= \frac{1}{2\sin\left( \frac{x}{2} \right)}\left[ \sin\left( \left( k+\frac{1}{2} x \right) \right) - \sin\left( \left( k-\frac{1}{2} \right) x \right) \right]
\end{aligned}
$$


Then,


$$
\begin{aligned}
\left\lvert  \sum_{k=1}^{n} \cos(kx)  \right\rvert &= \frac{1}{\left\lvert  2 \sin\left( \frac{x}{2} \right)  \right\rvert } \left\lvert  \sum_{k=1}^{n} \left[ \sin\left( \left( k+\frac{1}{2} \right) x \right) - \sin\left( \left( k-\frac{1}{2} \right) x \right)\right]  \right\rvert \\
&=\frac{1}{\left\lvert  2 \sin\left( \frac{x}{2} \right)  \right\rvert } \underbrace{ \left\lvert  \sin\left( \left( n+\frac{1}{2} \right)x \right) -\sin\left( \frac{1}{2} x \right) \right\rvert }_{ \leq 2 \text{ since }-1 \leq \sin(x) \leq 1 } \\
&\leq \frac{1}{\lvert \sin\left( \frac{x}{2} \right) \rvert }.
\end{aligned}
$$



### Theorem (Abel's test)

Let $$\{x_{n}\}_{n=1}^\infty$$ and $$\{y_{n}\}_{n=1}^\infty$$ be sequences such that
1. $$\{x_{n}\}_{n=1}^\infty$$ is monotone and convergent.
2. $$\sum_{n=1}^\infty y_{n}$$ converges.
Then $$\sum_{n=1}^\infty x_{n} y_{n}$$ converges.

***Proof:*** Consider the following cases:

**Case 1:** The $$x_{n}$$ are decreasing. Let $$L = \lim_{ n \to \infty } x_{n}$$. Define $$z_{n} = x_{n} - L$$. Then $$z_{n}$$ is decreasing and $$\lim_{ n \to \infty }z_{n} = 0$$. Therefore $$\sum_{n=1}^\infty y_{n} z_{n}$$ converges. Note that 


$$
\sum_{n=1}^{m} y_{n} z_{n} + \underbrace{ \sum_{n=1}^{m} y_{n} L }_{\text{convergent} } = \sum_{n=1}^{m} y_{n} x_{n}.
$$


Conclude that $$\sum_{n=1}^\infty x_{n} y_{n}$$ converges.

**Case 2:** The $$x_{n}$$ are increasing. Let $$L = \lim_{ n \to \infty } x_{n}$$. Define $$z_{n} = L -x_{n}$$. Then $$z_{n}$$ is decreasing and $$\lim_{ n \to \infty }z_{n} = 0$$. Therefore $$\sum_{n=1}^\infty y_{n} z_{n}$$ converges. Note that 


$$
- \sum_{n=1}^{m} y_{n} z_{n} + \underbrace{ \sum_{n=1}^{m} y_{n} L }_{\text{convergent} }  = \sum_{n=1}^{m} y_{n} x_{n}.
$$


Conclude that $$\sum_{n=1}^\infty x_{n} y_{n}$$ converges. 
 
#### Example 



$$
\sum_{n=2}^\infty \frac{1}{n^{2}} \ln\left( 1-\frac{1}{n} \right)
$$


Take $$y_{n} = \frac{1}{n^{2}}$$ and $$x_{n} = \ln\left( 1-\frac{1}{n} \right)$$. We know that $$\sum_{n=2}^\infty \frac{1}{n^{2}}$$ converges. Moreover 


$$
\lim_{ n \to \infty } x_{n} = \ln(1) = 0.
$$


Since $$1-\frac{1}{n}$$ is increasing, $$x_{n}$$ is increasing. Conclude by Abel's test that the series converges. 
 
#### Example 

Consider $$\sum_{n=1}^\infty (-1)^{n} \frac{\ln(n)}{n}$$. Note that $$\left( \frac{\ln(n)}{n} \right)' =\frac{1-\ln(x)}{x^{2}} \leq 0$$ if $$x \geq e$$. Then $$\frac{\ln(n)}{n}$$ is decreasing for $$n \geq 3$$ (we only need it to be eventually decreasing). Therefore $$\sum_{n=2}^\infty (-1)^{n} \frac{\ln(n)}{n}$$ converges. 

### Theorem (Raabe's test)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence such that $$x_{n}\neq_{0}$$ for every $$n \in \mathbb{N}$$. Consider 


$$
\lim_{ n \to \infty } n\left( 1 - \frac{\lvert x_{n+1}\rvert}{\lvert x_{n} \rvert } \right) = L.
$$


Then 
1. $$\sum_{n=1}^{\infty} \lvert x_{n} \rvert$$ converges if $$L >1$$.
2. $$\sum_{n=1}^\infty \lvert x_{n} \rvert$$ diverges if $$L < 1$$.

***Proof:*** Given $$\varepsilon > 0$$, there exists $$N \in \mathbb{N}$$ such that 


$$
L - \varepsilon \leq n\left( 1 - \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert \right) \leq L +\varepsilon 
$$


for $$n \geq N$$.
Assume $$L > 1$$. Take $$\varepsilon>0$$ such that $$L -\varepsilon > 1$$. Now 


$$
\begin{aligned}
\frac{L-\varepsilon}{n} &\leq 1 - \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert \\
\iff \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert &\leq 1 - \frac{l-\varepsilon}{n} \\
\iff n \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert  &\leq  n - (l -\varepsilon) \\
\iff n \lvert x_{n+1} \rvert &\leq n \lvert x_{n} \rvert -(l-\varepsilon) \lvert x_{n} \rvert \\
\iff n \lvert x_{n+1} \rvert &\leq (n-1) \lvert x_{n} \rvert -(L - \varepsilon - 1) \lvert  x_{n} \rvert 
\end{aligned}
$$


Then, for $$n\geq2$$,


$$
0 \leq (l-\varepsilon - 1) \lvert x_{n} \rvert \leq  (n-1) \lvert x_{n} \rvert  - n \lvert x_{n+1} \rvert. 
$$


Hence, if $$S =\sum_{n=1}^\infty (n-1) \lvert x_{n} \rvert - n \lvert x_{n+1} \rvert$$ converges then $$\sum_{n=1}^\infty\lvert x_{n} \rvert$$ converges. Now, $$\sum_{n=1}^{k} (n-1) \lvert x_{k} \rvert - n \lvert x_{n+1} \rvert = -k \lvert x_{k+1} \rvert$$. Then S converges if $$\lim_{ n \to \infty } k \lvert x_{k+1} \rvert$$ exists.
But $$(n-1) \lvert x_{n} \rvert  - n \lvert x_{n+1} \rvert$$, i.e., the sequence is decreasing and bounded below (since it is positive). Therefore, conclude that $$\sum_{n=1}^\infty \lvert x_{n} \rvert$$ converges.

#### Example 

Consider $$x_{n} = \frac{1\cdot 3 \cdot 5 \cdot \dots (2n+1)}{2 \cdot 4 \cdot 6 \cdot... \cdot (2n+2)}$$. Note that 


$$
\frac{x_{n+1}}{x_{n}} = \frac{\frac{1\cdot 3 \cdot 5 \cdot \dots (2n+3)}{2 \cdot 4 \cdot 6 \cdot... \cdot (2n+2)}}{ \frac{1\cdot 3 \cdot 5 \cdot \dots (2n+4)}{2 \cdot 4 \cdot 6 \cdot... \cdot (2n+2)}} = \frac{2n+3}{2n+4}  \underset{n\rightarrow \infty}{\longrightarrow} 1.
$$


Applying Raabe's test:



$$
n\left( 1-\frac{x_{n+1}}{x_{n}} \right) = n\left( 1 - \frac{2n+3}{2n+4} \right) = n\left( \frac{1}{2n+4} \right) \underset{n \rightarrow  \infty}{\longrightarrow} \frac{1}{2}.
$$


Therefore it diverges. 
 
### Theorem (Cauchy condensation)

Let $$\{a_{n}\}_{n=1}^\infty$$ be decreasing and positive. Then $$\sum_{n=1}^\infty a_{n}$$ converges if and only if $$\sum_{n=1}^\infty 2^{n} a_{2^{n}}$$ converges

***Proof:*** Let $$\{a_{n}\}_{n=1}^\infty$$ be a decreasing, positive sequence. Note that 


$$
\begin{aligned}
2a_{2} &\leq a_{1}+a_{2} &&\leq 2a_{1} \\
2a_{4} &\leq a_{3}+a_{4} &&\leq 2a_{3} \\
2^{2} a_{8} &\leq a_{5}+a_{6}+a_{7}+a_{8} &&\leq 2^{2} a_{5} \\
2^{3} a_{16} &\leq a_{9} + a_{10} + \dots + a_{16} &&\leq 2^{3}a_{9} \\
&   \vdots && \\\
2^{n-1} a_{2^{n}} &\leq a_{2^{n-1}+1}  + \dots + a_{2^{n}} &&\leq  2^{n-1} a_{2^{n-1}+1}.
\end{aligned}
$$


We want $$S_{n} = \sum_{k=1}^{n} a_{k}$$ to converge when $$\{a_{k}\}_{k=1}^\infty$$ is decreasing and positive. Since $$S_{n}$$ is increasing, because $$\{a_{k}\}_{k=1}^\infty$$ is positive, there are 2 possibilities:
1. $$S_{n}$$ converges if it is bounded.
2. $$\lim_{ n \to \infty } S_{n} = +\infty$$ if it is not.

Consider $$S_{2^{n}} = a_{1} + a_{2} + a_{4} + \dots + a_{2^{n}}$$. We know that, being increasing, $$S_{n}$$ converges if and only if $$S_{2^{n}}$$ converges. Now, note that 


$$
\begin{aligned}
S_{2^{n}} &= a_{1}+a_{2}+\dots+a_{2^{n}} \\
&= (a_{1}+a_{2}) + (a_{3} + a_{4}) + (a_{3} + \dots+a_{8}) + \dots+(a_{2^{n-1}+1} + \dots + a_{2^{n}}),
\end{aligned}
$$


so that, by the expansion above, we have that 


$$
\begin{aligned}
2a_{2} + 2a_{4}+2^{2} a_{8} + \dots +2^{n-1} a_{2^{n}} &= \frac{1}{2} \sum_{k=2}^{n} 2^{k} a_{2^{k}} + 2a_{2} \\
&\leq S_{2^{n}} \\
& \leq 2a_{1} + 2a_{3} + 2^{2} a_{5} + \dots +2^{n-1} a_{2^{n-1}+ 1} \\
&\leq 2a_{1} + 2a_{2} + 2^{2} a_{4} + \dots + 2^{n-1} a_{2^{n-1}} \\
&= 2a_{1} + \sum_{k=1}^{n-1} 2^{k} a_{2^{k}}.
\end{aligned}
$$



This test is useful for handling logarithms inside series.

#### Example 

Consider $$\sum_{n=2}^\infty \frac{1}{n(\ln n)^{2}}$$. Take $$\sum_{n=2}^\infty 2^{n} \left(\frac{1}{2^{n}} \frac{1}{(\ln2^{n})^{2}} \right) = \sum_{n=1}^\infty \frac{1}{(n\ln 2)^{2}} = \frac{1}{(\ln 2)^{2}} \sum_{n=2}^\infty \frac{1}{n^{2}}$$, which converges by the p-series test.

### Theorem (Absolute convergence and permutations)

Let $$\{a_{n}\}_{n=1}^\infty$$ be such that $$\sum_{n=0}^\infty \lvert a_{n} \rvert$$ converges and let $$\phi: \mathbb{N} \to \mathbb{N}$$. Then $$\sum_{n=0}^\infty a_{\phi(n)}$$ converges and moreover $$\sum_{n=0}^\infty a_{\phi(n)} = \sum_{n=0}^\infty a_{n}$$.

 ***Proof:***  Define $$S_{k} =\sum_{n=0}^{k} a_{n}$$ , $$\tilde{S_{k}} = \sum_{n=0}^{k} \lvert a_{n} \rvert$$ and $$u_{k} = \sum_{n=0}^{k}. a_{\phi(n)}$$. We know that $$\sum_{n=0}^\infty \lvert a_{n} \rvert$$ converges, i.e., being Cauchy we have that, given $$\varepsilon > 0$$, there exists $$N \in \mathbb{N}$$ such that for all $$n,m\geq N$$ 


$$
\lvert \tilde{S_{n}} - \tilde{S_{m}} \rvert  < \varepsilon.
$$


Then $$\lvert a_{n+1} \rvert + \lvert a_{n+2} \rvert + \dots + \lvert a_{m} \rvert < \varepsilon$$
Let $$\ell = \lim_{ n \to \infty } S_{n}$$. 
Now take $$N_{1}$$ such that $$\lvert S_{k} - \ell \rvert < \varepsilon$$ TO BE COMPLETED.
### Worked example 1

Consider the series $$\sum_{n=1}^\infty \frac{1}{\sqrt{ n(n+1) }}$$. Note that $$\frac{1}{\sqrt{ n(n+1) }} \approx \frac{1}{\sqrt{ n \cdot n }} = \frac{1}{n}$$. Since 


$$
\lim_{ n \to \infty } \frac{\frac{1}{\sqrt{ n(n+1) }}}{\frac{1}{n}} = 1
$$


and $$\sum_{n=1}^\infty \frac{1}{n}$$ diverges, the given series diverges. 
 

### Worked example 2

Consider the series $$\sum_{n=1}^\infty \sin\left( \frac{1}{n^{p}} \right)$$ for $$p>1$$. Note that $$0 \leq \sin(x) \leq x$$ for every $$x\geq 0$$. Since $$0 \leq \frac{1}{n^{p}}$$, we have that $$0\leq \sin\left( \frac{1}{n^{p}} \right) \leq \frac{1}{n^{p}}$$. Therefore the series converges by comparison. 
 

### Worked example 3
 
Consider the series $$\sum_{n=1}^{\infty} \frac{n^{n}}{(n+1)^{n+1}}$$. Note that 



$$
\frac{n^{n}}{(n+1)^{n+1}} = \frac{1}{n+1} \frac{1}{\left( 1+\frac{1}{n} \right)^{n}} \approx \frac{1}{n+1}
$$


Now, $$\lim_{ n \to \infty } (1+\frac{1}{n})^{n} = e$$. Hence  


$$
\lim_{ n \to \infty } \frac{\frac{n^{n}}{(n+1)^{n+1}}}{\frac{1}{n+1}} = e
$$



so the given series diverges. 
 

### Worked example 4

Consider the series $$\sum_{n=1}^\infty \frac{\sqrt{ n } - \sqrt{ n+1 }}{\sqrt{ n(n+1) }} = \sum_{n=1}^\infty \frac{1}{\sqrt{ n+1 }} - \frac{1}{\sqrt{ n }}$$. This series converges because it is telescoping and $$\lim_{ n \to \infty } \frac{1}{\sqrt{ n }} = 0$$. In particular, the series converges to $$-1$$. 
 

### Worked example 5

Compute the following limit: 


$$
\lim_{ n \to \infty } n\left( 1-\left( 1-\frac{1}{2n} \right)^{p} \right).
$$
{% endraw %}
