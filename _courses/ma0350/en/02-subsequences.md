---
layout: chapter
course: ma0350
chapter: 2
title: "Subsequences"
slug: 02-subsequences
toc:
  sidebar: right
lang: en
permalink: /notes/ma0350/02-subsequences/
---

{% raw %}
In this note we define and develop everything related to subsequences of sequences. See also: Limit superior and limit inferior.
### Definition 

Given a sequence $$\{x_{n}\}_{n=1}^\infty$$ and a strictly increasing function $$\phi:\mathbb{N} \to \mathbb{N}$$, we define the sequence $$\{x_{\phi(n)}\}_{n=1}^\infty$$ to be a subsequence of $$\{x_{n}\}_{n=1}^\infty$$.

### Lemma  

Let $$\phi:\mathbb{N} \to \mathbb{N}$$ be a strictly increasing function. Then $$\phi(n) \geq n$$ for every $$n \in \mathbb{N}$$.

***Proof:*** We use induction on n.
**Base case:** For $$n = 0$$, note that $$\phi(0) \in \mathbb{N}$$, so $$\phi(0) \geq 0$$ trivially. This proves the base case.
**Inductive step:** Let $$m \in \mathbb{N}$$ be fixed and arbitrary. Suppose as the inductive hypothesis that $$\phi(m) \geq m$$. We must prove that $$\phi(m+1) \geq m+1$$. Note that $$m \leq \phi(m) < \phi(m+1)$$. Then, since $$\phi(m+1) \in \mathbb{N}$$ and $$\phi(m+1) > m$$, we have that $$\phi(m+1) \geq m+1$$. This proves the inductive step. Conclude that $$\phi(n) \geq n$$ for every $$n \in \mathbb{N}$$. 

### Lemma 

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$ and let $$\{x_{\phi(n)}\}_{n=1}^\infty$$ be a subsequence. Then $$x_{\phi(n)} \underset{n \rightarrow \infty}{\longrightarrow} L$$.

***Proof:*** Given $$\varepsilon >0$$, there exists $$N \in \mathbb{N}$$ such that $$\lvert x_{n}-L \rvert < \varepsilon$$ if $$n \geq N$$. Now, $$\phi(n) \geq n \geq N$$, so $$\lvert x_{\phi(n)} - L \rvert < \varepsilon$$ for $$n \geq N$$.  
 
#### Example 

Let $$w_{n} = \cos(n\pi) = (-1)^{n}$$. Then $$w_{2n} \underset{n \rightarrow \infty}{\longrightarrow} 1$$ and $$w_{2n+1} \underset{n \rightarrow \infty}{\longrightarrow} -1$$. Therefore $$w_{n}$$ diverges.

### Theorem (Bolzano-Weierstrass):

Let $$\{x_{n}\}_{n=1}^\infty$$ be a bounded sequence. Then there exists a subsequence $$\{x_{k_{n}}\}_{n=1}^{\infty}$$ that converges.

***Proof:*** Suppose that $$a \leq x_{n} \leq b$$ for every $$n \in \mathbb{N}$$. Let 


$$
\begin{aligned}
A_{1}^{1} &= \left\{  n: a\leq x_{n} \leq \frac{a+b}{2}  \right\} \\
A_{2}^{1} &= \left\{  n: \frac{a+b}{2} \leq x_{n} \leq b \right\}
\end{aligned}
$$


Then $$A_{1}^{1}$$ is infinite or $$A_{2}^{1}$$ is infinite. If $$A_{1}^{1}$$ is infinite, take $$a_{1}=a$$ and $$b_{1} = \frac{a+b}{2}$$. There are infinitely many $$x_{n}$$ such that $$a_{1} \leq x_{n} \leq b_{1}$$. Note that $$a = a_{1}$$, $$b_{1} < b$$. On the other hand, if $$A_{2}^{1}$$ is infinite, then take $$a_{1} = \frac{a+b}{2}$$ and $$b_{1} = b$$. In this case, $$a < a_{1}$$ and $$b = b_{1}$$. Note that, in both cases, $$b_{1}-a_{1} = \frac{b-a}{2}$$. We conclude that there are infinitely many $$n$$ such that $$a_{1} \leq x_{n} \leq b_{1}$$. Now let 


$$
\begin{aligned}
A_{1}^{2} &= \left\{  n: a_{1}\leq x_{n} \leq \frac{a_{1}+b_{1}}{2}  \right\} \\
A_{2}^{2} &= \left\{  n: \frac{a_{1}+b_{1}}{2} \leq x_{n} \leq b_{1} \right\}
\end{aligned}
$$


Then $$A_{1}^{2}$$ is infinite or $$A_{2}^{2}$$ is infinite. If $$A_{1}^{2}$$ is infinite, take $$a_{2}=a_{1}$$ and $$b_{2} = \frac{a_{1}+b_{1}}{2}$$. There are infinitely many $$x_{n}$$ such that $$a_{2} \leq x_{n} \leq b_{2}$$. Note that $$a_{1} = a_{2}$$, $$b_{2} < b_{1}$$. On the other hand, if $$A_{2}^{1}$$ is infinite, then take $$a_{2} = \frac{a_{1}+b_{1}}{2}$$ and $$b_{2} = b_{1}$$. In this case, $$a_{1} < a_{2}$$ and $$b_{1} = b_{2}$$. Note that, in both cases, $$b_{2}-a_{2} = \frac{b_{1}-a_{1}}{2} = \frac{b-a}{2^{2}}$$. We conclude that there are infinitely many $$n$$ such that $$a_{1} \leq x_{n} \leq b_{1}$$. 

Iterating the process, we can find $$a_{n}$$ and $$b_{n}$$ such that 
1. There are infinitely many $$m \in \mathbb{N}$$ such that $$a_{n} \geq x_{m} \leq b_{n}$$.
2. $$a \leq a_{n} \leq a_{n+1} \leq b$$.
3. $$a\leq b_{n+1} \leq b_{n} \leq b$$
4. $$b_{n}-a_{n} = \frac{b-a}{2^{n}}$$

By the monotone convergence theorem, since $$\{a_{n}\}_{n=1}^\infty$$ and $$\{b_{n}\}_{n=1}^\infty$$ are bounded and monotone, they converge. Suppose that $$a_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{1}$$ and $$b_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{2}$$. Note that 


$$
\ell_{2}-\ell_{1} =\lim_{ n \to \infty } b_{n}-a_{n} = \lim_{ n \to \infty } \frac{b-a}{2^{n}} = 0.
$$


Conclude that $$\ell_{2} = \ell_{1}$$. Let $$x_{k_{1}}$$ be such that $$a_{1} \leq x_{k_{1}} \leq b_{1}$$. Let $$B_{2} = \{ m:a_{2} \leq x_{m} \leq b_{2} \}$$. Note that, by construction, $$B_{2}$$ has infinitely many elements. Take $$k_{2} \in B -\{ 0,\dots,k_{1} \}$$. 

In general, let $$B_{n} = \{ m: a_{n} \leq x_{m} \leq b_{n} \}$$. Note that $$B_{n}$$ has infinitely many elements. Take $$k_{n} \in B_{n} - \{ 0,\dots,k_{n-1} \}$$. Then we have a subsequence $$\{x_{k_{n}}\}_{n=1}^\infty$$ such that $$a_{n} \leq x_{k_{n}} \leq b_{n}$$. Hence $$\ell_{1} = \lim_{ n \to \infty } a_{n} \leq \lim_{ n \to \infty } x_{k_{n}} \leq \lim_{ n \to \infty } b_{n} = \ell_{2}$$, from which we conclude that $$\{x_{k_{n}}\}_{n=1}^\infty$$ converges by the squeeze theorem. 

### Theorem (Cauchy implies bounded)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a Cauchy sequence. Then it is bounded.

***Proof:*** Take $$\varepsilon = 1$$. There exists $$N \in \mathbb{N}$$ such that $$\lvert x_{n} - x_{m} \rvert < 1$$ for all $$m,n \geq N$$. In particular (taking $$m = N$$), $$\lvert x_{n} \rvert -\lvert x_{N} \rvert \leq  \lvert x_{n} - x_{N} \rvert < 1$$. Then $$\lvert x_{n} \rvert < 1 + \lvert x_{N} \rvert$$. Let $$M = \max \{ \lvert x_{1} \rvert, \lvert x_{2} \rvert, \dots, \lvert x_{N-1} \rvert, 1 + \lvert x_{N}  \rvert \}$$. Then $$\lvert x_{n} \rvert \leq M$$ for every $$n \in \mathbb{N}$$.

### Theorem  (Cauchy implies convergence)

If $$\{x_{n}\}_{n=1}^\infty$$ is Cauchy, then it converges.

***Proof:*** Since $$\{x_{n}\}_{n=1}^\infty$$ is Cauchy, it is bounded. Then, by Bolzano-Weierstrass, there exists a subsequence $$\{ x_{k_{n}} \}_{n=1}^{\infty}$$ such that $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Let $$\varepsilon > 0$$. Then there exists $$N \in \mathbb{N}$$ such that $$\lvert x_{n}-x_{m} \rvert < \frac{\varepsilon}{2}$$ if $$n,m \geq N$$. Moreover, there exists $$N_{1} \in \mathbb{N}$$ such that $$N_{1} \geq N$$ and $$\lvert x_{k_{n}} - L \rvert < \frac{\varepsilon}{2}$$ if $$n \geq N_{1}$$. Then, for every $$n \geq N_{1}$$, $$k_{n} \geq n \geq N_{1} \geq N$$, so 


$$
\lvert x_{n} - L \rvert \leq \lvert x_{n} - x_{k_{n}} \rvert + \lvert x_{k_{n}} - L \rvert < \varepsilon. 
$$


Conclude then that $$\{x_{n}\}_{n=1}^\infty$$ converges. 

### Theorem (Sequential criterion for limits)

Let $$f:(a,b) \to \mathbb{R}$$ and $$c \in (a,b)$$. Then $$\lim_{x \to c } f(x) = L$$ if and only if for every sequence $$\{x_{n}\}_{n=1}^\infty \subseteq (a,b)$$ such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}c$$, we have that $$\lim_{ n \to \infty } f(x_{n}) = L$$.

***Proof:*** ($$\impliedby$$): We prove the contrapositive. Assume that there exists $$\varepsilon>0$$ such that for every $$\delta > 0$$ there exists $$x_{\delta}$$ such that $$\lvert x- c \rvert < \delta$$ and $$\lvert f(x_{\delta}) - L \rvert \geq \varepsilon$$. Take $$\delta = \frac{1}{n}$$. Then there exists $$x_{k_{n}}$$ such that $$\lvert x_{k_{n}} - c \rvert < \frac{1}{n}$$ and $$\lvert f(x_{k_{n}}) - L \rvert \geq \varepsilon$$. Note that $$\lim_{ n \to \infty } \lvert x_{k_{n}} - c \rvert = 0$$, and therefore $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} c$$, but $$f(x_{k_{n}}) \underset{n \rightarrow \infty}{\cancel{ \longrightarrow }} L$$. 

We had already proved the other direction.
{% endraw %}
