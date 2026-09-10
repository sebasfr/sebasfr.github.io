---
layout: chapter
course: ma0350
chapter: 1
title: "Sequences"
slug: 01-sequences
toc:
  sidebar: right
lang: en
fecha: 2025-03-11
permalink: /notes/ma0350/01-sequences/
---

{% raw %}
Let $$0<x<1$$, then


$$
x = 0,\bar{a_{1}}\bar{a_{2}}\bar{a_{3}}\dots
$$


Let $$x_{1} = 10x$$, then $$0<x_{1} <10$$. If $$0 \leq x_{1} <1$$, then the first decimal digit is given by $$a_{1} = 0$$. If not, iterate to find the natural number $$0 \leq n_{1} \leq 9$$ such that $$n_{1} \leq x_{1} < n_{1} + 1.$$ Then $$0 \leq a_{1}=n_{1} \leq 9 \quad \text{(1)}$$. 

Now take $$x_{2} = 10(x_{1}-n_{1})$$. Note that $$0\leq x_{2} < 10$$.  Take $$a_{2} = n_{2}$$, where $$n_{2}$$ is such that $$n_{2}\leq x_{2} \leq n_{2}+1.$$  From (1), we have that 


$$
\begin{aligned}
n_{1} &\leq 10x < n_{1} + 1\\
\implies \frac{n_{1}}{10} &\leq  x < \frac{n_{1}}{10}+\frac{1}{10} \\
\implies 0 &\leq x-\frac{n_{1}}{10} < \frac{1}{10}.
\end{aligned}
$$


Moreover, 


$$
\begin{aligned}
&n_{2} \leq 10(x_{1}-n_{1}) < n_{2} + 1\\
\implies & \frac{n_{2}}{10} \leq  x_{1}-n_{1} < \frac{n_{2}}{10}+\frac{1}{10} \\
\implies & n_{1}+\frac{n_{2}}{10} \leq x_{1} < n_{1} + \frac{n_{2}}{10} + \frac{1}{10}  \\
\implies & n_{1}+\frac{n_{2}}{10} \leq 10x < n_{1} + \frac{n_{2}}{10} + \frac{1}{10}  \\
\implies & \frac{n_{1}}{10}+\frac{n_{2}}{100} \leq x < \frac{n_{1}}{10} + \frac{n_{2}}{100} + \frac{1}{100}  \\
\implies&  0\leq x -\frac{n_{1}}{10} -\frac{n_{2}}{100} < \frac{1}{10^{2}}.
\end{aligned}
$$


Iterating the process, we obtain 


$$
0\leq n_{1},n_{2},n_{3},...,n_{k} \leq 9,
$$


with 


$$
\frac{n_{1}}{10} +\frac{n_{2}}{10^{2}}+\frac{n_{3}}{10^{3}} + \dots + \frac{n_{k}}{10^{k}} \leq x \leq \frac{n_{1}}{10} +\frac{n_{2}}{10^{2}}+\frac{n_{3}}{10^{3}} + \dots + \frac{n_{k}}{10^{k}} + \frac{1}{10^{k}}.
$$



Let $$x_{k+1} = 10(x_{k}-n_{k})$$. Then there exists $$n_{k+1} \in \mathbb{N}$$ such that $$n_{k+1} \leq x_{k+1} < n_{k+1} +1,$$ with $$0\leq n_{k+1} \leq 9.$$ Since 


$$
0 \leq \underbrace{ x-\frac{n_{1}}{10}-\frac{n_{2}}{10^{2}} - \frac{n_{3}}{10^{3}} - \dots - \frac{n_{k}}{10^{k}} }_{ y_{1} } < \frac{1}{10^{k}},
$$


we have that $$0 \leq 10^{k+1} y_{1} < 10$$. Then $$x_{k+1} = 10^{k+1}y_{1}$$. We know that $$n_{k+1} \leq x_{k+1} < n_{k+1} +1,$$, so 


$$
\begin{aligned}
& n_{k+1} \leq 10^{k+1}\left( x-\frac{n_{1}}{10}-\frac{n_{2}}{10^{2}}-\frac{n_{3}}{10^{3}}-\dots-\frac{n_{k}}{10^{k}} \right) < n_{k+1}+1\\
\implies & 0 \leq x-\frac{n_{1}}{10}-\frac{n_{2}}{10^{2}}-\frac{n_{3}}{10^{3}}-\dots-\frac{n_{k}}{10^{k}} - \frac{n_{k+1}}{10^{k+1}} < \frac{1}{10^{k+1}}.
\end{aligned}
$$


Conclude by induction that $$x - \left( \frac{n_{1}}{10} + \frac{n_{2}}{10^{2}} +\frac{n_{3}}{10^{3}} +\dots+ \frac{n_{k}}{10^{k}} \right) < \frac{1}{10^{k}}$$. Sequences are born in order to approximate numbers.

## Sequences 

### Definition (Real-valued sequence)

A sequence in $$\mathbb{R}$$ (denoted $$\{x_{n}\}_{n=1}^\infty$$) is a function $$\underset{n \to x_{n}}{f:\mathbb{N} \to \mathbb{R}}$$.

### Definition (Convergence)

We say that a sequence $$\{x_{n}\}_{n=1}^\infty$$ converges to $$L$$ $$(\lim_{ n \to \infty } x_{n} = L)$$, denoted by $$x_{n} \underset{n \rightarrow  \infty}{\longrightarrow} L$$, if for every $$\varepsilon > 0$$ there exists $$N \in \mathbb{N}$$ such that for every $$n \geq N$$, $$\lvert x_{n}-L \rvert < \varepsilon$$. 
 
#### Example 

Given $$x \in (0,1)$$, there exists $$x_{m} = \sum_{i=1}^{m} \frac{n_{i}}{10^{i}}$$ satisfying $$\lvert x-x_{m} \rvert < \frac{1}{10^{m}}$$. Let $$\varepsilon > 0$$ be fixed and arbitrary. Take $$N = \left\lceil  \log_{10}\left( \frac{1}{\varepsilon} \right)  \right\rceil$$. Let $$n \geq N$$ be fixed and arbitrary. Note that 


$$
\log_{10} \left( \frac{1}{\varepsilon} \right) \leq M \leq n
$$




$$
\implies\quad\frac{1}{\varepsilon} \leq 10^{n}
$$




$$
\implies \frac{1}{10^{n}} \leq \varepsilon
$$




$$
\implies \lvert x_{n} - x \rvert < \frac{1}{10^{n}} \leq \varepsilon. 
$$


 Conclude that $$\lim_{ n \to \infty } x_{n} = x$$.

### Theorem (Uniqueness of the limit) 

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{1}$$ and $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{2}$$. Then $$\ell_{1} = \ell_{2}$$.

***Proof:*** Suppose for the sake of contradiction that $$\ell_{1} \neq \ell_{2}$$. Consider 


$$
0 < \lvert \ell_{2} - \ell_{2} \rvert \leq \lvert \ell_{1}-x_{n} \rvert + \lvert x_{n}-\ell_{2} \rvert.
$$


Take $$\varepsilon = \frac{\lvert \ell_{1}-\ell_{2} \rvert}{2}$$. Then there exists $$N \in \mathbb{N}$$ such that $$\lvert \ell_{1}-x_{n} \rvert < \varepsilon$$ and $$\lvert x_{n} - \ell_{2} \rvert < \varepsilon$$ for $$n \geq N$$. Hence, 


$$
0 < \lvert \ell_{1} - \ell_{2} \rvert \leq  \lvert x_{n}-\ell_{1} \rvert + \lvert x_{n} - \ell_{2} \rvert < 2\varepsilon = \lvert \ell_{1} - \ell_{2} \rvert. \quad (\Rightarrow\!\Leftarrow)
$$



### Theorem (Boundedness)

Let $$\{x_{n}\}_{n=1}^\infty$$ be such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Then $$\{x_{n}\}_{n=1}^\infty$$ is bounded.

***Proof:*** Take $$\varepsilon = 1$$. Then there exists $$N \in \mathbb{N}$$ such that $$\lvert x_{n}-1 \rvert < 1$$ for $$n \geq N$$, that is, 


$$
L -1 < x_{n} <L+1 \implies \lvert x_{n} \rvert < \max\{\lvert L+1 \rvert , \lvert L-1 \rvert \}.
$$


Take $$M = \max \{\lvert x_{1} \rvert\ , \lvert x_{2} \rvert,\dots,\lvert x_{N} \rvert, \lvert L-1 \rvert, \lvert L+1 \rvert\}$$. Then $$\lvert x_{n} \rvert \leq M$$ for every $$n \in \mathbb{N}$$. 

#### Corollary 

Let $$\{x_{n}\}_{n=1}^\infty$$ be an unbounded sequence. Then $$\{x_{n}\}_{n=1}^\infty$$ is divergent. 

***Proof:*** This follows directly from the contrapositive of the theorem.

#### Example 

Let $$b>1$$ and let $$y_{n} = b^{n}$$ for $$n \geq 0$$. Assume that there exists $$M \in \mathbb{R}$$ such that $$b^{n} \leq M$$ for every $$n \in \mathbb{N}$$. By Bernoulli's inequality, we have that $$1 + n(b-1) \leq b^{n} \leq M$$. But this implies that $$n \leq \frac{M-1}{b-1}$$ for every $$n \in \mathbb{N}$$, that is, that the sequence $$\{n_{}\}_{n=1}^\infty$$ is bounded $$(\Rightarrow\!\Leftarrow)$$. 

### Definition (Cauchy sequence)

Let $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$. We say that the sequence is Cauchy if for every $$\varepsilon>0$$ there exists $$N_{0} \in \mathbb{N}$$ such that $$\lvert x_{n}-x_{m} \rvert < \varepsilon$$ for all $$n,m \geq N_{0}$$. 

### Theorem (Convergence implies Cauchy)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L \in \mathbb{R}$$. Then $$\{x_{n}\}_{n=1}^\infty$$ is Cauchy. 

***Proof:*** Assume that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Then, given $$\varepsilon > 0$$, there exists $$N_{0} \in \mathbb{N}$$ such that $$\lvert x_{n} - L \rvert > \frac{\varepsilon}{2}$$ for every $$n \geq N_{0}$$. Let $$n,m \geq N_{0}$$ be fixed and arbitrary. Then 


$$
\lvert x_{n} - x_{m} \rvert \leq \lvert x_{n} - L \rvert + \lvert x_{m} - L \rvert < \varepsilon.
$$


Conclude that $$\{x_{n}\}_{n=1}^\infty$$ is Cauchy. 
#### Corollary 
If $$\{x_{n}\}_{n=1}^\infty$$ is not Cauchy, then it does not converge. 
 
#### Example 

Let $$z_{n} = (-1)^{n}$$.  Note that 


$$
z_{n} =
\begin{cases}
1  \quad\text{if $n$ is even} \\
-1  \quad\text{if $n$ is odd}
\end{cases}
$$


Let $$0 < \varepsilon <2$$ and $$N_{0} \in \mathbb{N}$$. Take $$n = 2N_{0} > N_{0}$$ and $$m = 2N_{0}+1>N_{0}$$. Then $$\lvert x_{n} - x_{m}\rvert = 2 > \varepsilon$$. Therefore $$\{z_{n}\}_{n=1}^\infty$$ is not Cauchy and diverges. 

### Definition (Divergence to infinity)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence. We say that it diverges to infinity, denoted by $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$$ ($$\lim_{ n \to \infty } x_{n} = \infty$$), if for every $$\alpha > 0$$ there exists $$N \in \mathbb{N}$$ such that $$x_{n} > \alpha$$ for every $$n \geq N$$. In the same way, $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} -\infty$$ if for every $$\beta >0$$ there exists $$N \in \mathbb{N}$$ such that $$x_{n} < -\beta$$ for every $$n \geq N$$. 
 
#### Example 

If $$b>1$$ and $$y_{n} = b^{n}$$, then $$y_{n} \underset{n \rightarrow \infty}{\longrightarrow}\infty$$.  $$\underset{}{\sup}$$

### Theorem (Monotone convergence)

Let $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$.
1. If $$\{x_{n}\}_{n=1}^\infty$$ is decreasing and bounded below, then $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \underset{n \in \mathbb{N}}{\inf} x_{n}$$.
2. If $$\{x_{n}\}_{n=1}^\infty$$ is increasing and bounded above, then $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \underset{n \in \mathbb{N}}{\sup} x_{n}$$. 

***Proof of 2:*** Assume that $$\{x_{n}\}_{n=1}^\infty$$ is increasing and bounded above. Take $$L = \underset{n \in \mathbb{N}}{\sup} x_{n}$$ and $$\varepsilon >0$$ fixed and arbitrary. By the definition of the supremum, there exists $$N \in \mathbb{N}$$ such that $$L - \varepsilon < x_{N} \leq L$$. Take $$n \geq N$$, then $$x_{n} \geq x_{N}$$. Hence $$L - \varepsilon < x_{N} \leq x_{n} \leq L$$. Therefore, conclude that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}L$$. The proof of 1. is analogous. 
 
#### Example 

Consider $$z_{n} = a^{n}$$ with $$0<a<1$$. Note that $$a < 1$$, so $$a^{n+1} < a^{n}$$. Let $$L = \underset{n \in \mathbb{N}}{\inf} z_{n}$$. Take $$\varepsilon>0$$. By the definition of the infimum, we know that there exists $$N_{1} \in \mathbb{N}$$ such that $$L \leq a^{N_{1}} < L + \varepsilon$$. Let $$n \geq N_{1}$$. Then $$L \leq a^{n} < a^{N_{1}} < L + \varepsilon$$, i.e. $$\lvert a^{n}-L \rvert < \varepsilon$$. Therefore $$z_{n} \underset{n \rightarrow \infty}{\longrightarrow}L$$. We will now prove that $$L = 0$$. To that end, suppose for the sake of contradiction that $$L>0$$, that is, that for every $$n \in \mathbb{N}$$, $$0 < L < a^{n}$$. Then $$\left( \frac{1}{a} \right)^{n} < \frac{1}{L}$$, a contradiction since $$\frac{1}{a} > 1$$ and in that case the sequence diverges to $$\infty$$. 

### Theorem (Algebraic properties of the limit)

Let $$\{x_{n}\}_{n=1}^\infty$$ and $$\{y_{n}\}_{n=1}^\infty$$ be sequences in $$\mathbb{R}$$ such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}\ell_{1}$$ and $$y_{n} \underset{n \rightarrow \infty}{\longrightarrow}\ell_{2}$$. Then:
1. $$x_{n} + y_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{1} + \ell_{2}$$.
2. $$x_{n}y_{n} \underset{ \rightarrow \infty}{\longrightarrow} \ell_{1} \ell_{2}$$.
3. If $$y_{n} \neq 0$$ for every $$n \in \mathbb{N}$$ and $$\ell_{2} \neq 0$$, then $$\frac{1}{y_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{\ell_{2}}$$.

***Proof of 3:***  We know that $$\ell_{2} \neq 0$$. Let $$\varepsilon > 0$$ be fixed and arbitrary. Then there exists $$N_{1} \in \mathbb{N}$$ such that 


$$
\begin{aligned}
&\lvert y_{n} \rvert - \lvert \ell_{2} \rvert \leq \lvert y_{n}-\ell_2 \rvert < \varepsilon \leq \\
\implies & \lvert l_{2}\rvert - \varepsilon < \lvert y_{n} \rvert.
\end{aligned}
$$


I take $$\varepsilon = \frac{\lvert l_{2} \rvert}{2}$$, so $$\lvert y_{n} \rvert \geq\lvert l_{2} \rvert - \varepsilon \geq \lvert \ell_{2} \rvert - \frac{\lvert l_{2} \rvert}{2} = \frac{\lvert \ell_{2} \rvert}{2}$$ for $$n \geq N_{1}$$, that is, $$\frac{1}{\lvert y_{n} \rvert} \leq \frac{2}{\lvert \ell_{2} \rvert}$$. Then, for $$n\geq N_{1}$$, we have that 


$$
\left\lvert  \frac{1}{y_{n}} - \frac{1}{\ell_{2}}  \right\rvert = \frac{\lvert \ell_{2} - y_{n} \rvert }{\lvert y_{n} \rvert \lvert \ell_{2} \rvert } \leq \frac{\lvert \ell_{2}-y_{n} \rvert }{\lvert \ell_{2} \rvert} \frac{2}{\lvert \ell_{2} \rvert }.
$$


Let $$N_{2} \in \mathbb{N}$$ be such that $$\lvert y_{n} - \ell_{2} \rvert < \frac{\varepsilon \lvert \ell_{2} \rvert}{2}$$. Then, for $$n \geq \max\{N_{1}, N_{2}\}$$, we have that 


$$
\left\lvert  \frac{1}{y_{n}} - \frac{1}{\ell_{2}}  \right\rvert = \frac{\lvert y_{n}-\ell_{2} \rvert }{\lvert  y_{n} \rvert \lvert \ell_{2} \rvert } \leq \frac{2\lvert y_{n}-\ell_{2} \rvert }{\lvert \ell_{2} \rvert ^{2}} < \frac{\varepsilon \lvert \ell_{2} \rvert ^{2}}{2} \frac{2}{\lvert \ell_{2} \rvert ^{2}} = \varepsilon.
$$


Conclude that $$\frac{1}{y_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{\ell_{2}}$$. 

### Theorem (Limits and continuous functions)

Let $$\{x_{n}\}_{n=1}^\infty$$ be such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$ and let $$f:(a,b) \to \mathbb{R}$$ be continuous with $$L \in (a,b)$$. Then $$f(x_{n}) \underset{n \rightarrow \infty}{\longrightarrow} f(L)$$.

***Proof:*** Given $$\varepsilon>0$$, there exists $$\delta > 0$$ such that if $$\lvert x-L \rvert < \delta$$ then $$\lvert f(x) - f(L)  \rvert < \varepsilon$$. Since $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$, there exists $$N_{0}$$ such that $$\lvert x_{n} - L\rvert < \delta$$ if $$n \geq N_{0}$$. Hence, for every $$n \geq N_{0}$$, $$\lvert x_{n} - L \rvert < \delta$$ and consequently $$\lvert f(x_{n}) - f(L) \rvert < \varepsilon$$. 
 
#### Example 

 $$\sqrt{ 1+\frac{2}{1+\frac{1}{n}}} \underset{n \rightarrow \infty}{\longrightarrow} \sqrt{ 3 }$$. 
 Note that: 


$$
\frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} 0
$$





$$
\implies 1+\frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} 1
$$


since $$1+x$$ is continuous on $$\mathbb{R}$$, 


$$
\implies \frac{2}{1+\frac{1}{n}} \underset{n \rightarrow \infty}{\longrightarrow} 2
$$


since $$\frac{2}{x}$$ is continuous on $$(0,+\infty)$$, 


$$
\implies \sqrt{ 1 + \frac{2}{1+\frac{1}{n}} } \underset{n \rightarrow \infty}{\longrightarrow} \sqrt{ 3 },
$$


since $$\sqrt{ 1+x }$$ is continuous on $$(0,+\infty)$$. 
 
#### Example 

Compute $$\lim_{ n \to \infty } k - \sqrt{ k^{2}-k }$$.

Note that 


$$
\begin{aligned}
x_{k} &= \frac{(k-\sqrt{ k^{2}-k })(k+\sqrt{ k^{2}-k })}{k + \sqrt{ k^{2}-k }} \\
&= \frac{k^{2} - (\sqrt{ k^{2}-k })^{2}}{k + \sqrt{ k^{2}-k }} \\
&= \frac{k}{k+\sqrt{ k^{2}-k }} \\
&= \frac{1}{1 + \sqrt{ 1-\frac{1}{k}}}.
\end{aligned}
$$


Then 


$$
x_{k} = \frac{1}{1+\sqrt{ 1-\frac{1}{k} }} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{2}.
$$



#### Example

Compute $$\lim_{ n \to \infty } \ln(n^{2}-1) - \ln(n(n-1))$$.

Note that 


$$
\begin{aligned}
\ln(n^{2}-1) - \ln(n(n-1)) &= \ln\left(\frac{n^{2}-1}{n(n-1)}\right) \\
&= \ln\left( \frac{(n+1)(n-1)}{n(n-1)} \right) \\
&= \ln\left( \frac{n+1}{n} \right) \\
&= \ln\left( 1 + \frac{1}{n} \right) \underset{n \rightarrow \infty}{\longrightarrow} \ln(1) = 0.
\end{aligned}
$$



## Recursive sequences

#### Example 

Let $$\{a_{n}\}_{n=1}^\infty$$ be such that $$a_{0} = 1$$ and $$a_{n+1} = \sqrt{ 1+a_{n} }$$. Prove that it converges and compute its limit.

***Proof:*** First, we will prove by induction that $$\{a_{n}\}_{n=1}^\infty$$ is increasing, i.e., $$a_{n+1} \geq a_{n}$$ for every $$n \in \mathbb{N}$$.
**Base case:** For $$n = 0$$, $$a_{1} = \sqrt{ 2 } \geq 1 = a_{0}$$. This proves the base case.
**Inductive step:** Suppose as the inductive hypothesis that $$a_{m+1} \geq a_{m}$$ for some fixed and arbitrary $$m \in \mathbb{N}$$. We must show that $$a_{m+2} \geq a_{m+1}$$. From the inductive hypothesis: 


$$
\begin{aligned}
a_{m+1} &\geq a_{m} \\
1 + a_{m+1} &\geq 1+a_{m} \\
a_{m+2} = \sqrt{ 1 + a_{m+1} } &\geq \sqrt{ 1 + a_{m} } = a_{m+1}.
\end{aligned}
$$


This proves the inductive step. Conclude that $$\{a_{n}\}_{n=1}^\infty$$ is increasing.
We will now prove that it is bounded above. In particular, we will prove by induction that for every $$n \in \mathbb{N}$$, $$a_{n} \leq 2$$.
**Base case:** For $$n=0$$, $$a_{0} = 1 \leq 2$$. This proves the base case.
**Inductive step:** Suppose as the inductive hypothesis that $$a_{m} \leq 2$$ for some fixed and arbitrary $$m \in \mathbb{N}$$. We must show that $$a_{m+1} \leq 2$$. From the inductive hypothesis: 


$$
\begin{aligned}
a_{m} &\leq 2 \\
1 + a_{m} &\leq 3\\
a_{m+1} = \sqrt{ 1 + a_{m} } &\leq \sqrt{3} < 2.
\end{aligned}
$$


This proves the inductive step. Conclude that $$\{a_{n}\}_{n=1}^\infty$$ is bounded.
Then, by the monotone convergence theorem, conclude that $$\{a_{n}\}_{n=1}^\infty$$ converges. Let $$L = \lim_{ n \to \infty } a_{n}$$. Then 


$$
\begin{aligned}
a_{n+1} &= \sqrt{ 1 + a_{n} } \\
\implies \lim_{ n \to \infty } a_{n+1} &=\lim_{ n \to \infty } \sqrt{1 + a_{n}} \\
\implies L &= \sqrt{ 1 + L } \\
\implies L^{2}-L-1 &= 0 \\
\implies L &= \frac{1+\sqrt{ 5 }}{2}.
\end{aligned}
$$


 
#### Example 

Let $$x_{n} = \frac{x_{n-1}+1}{3} = \frac{x_{n-1}}{3} + \frac{1}{3}$$ for $$n \geq 1$$ and $$x_{0} = x$$. Note that 


$$
\begin{aligned}
x_{1} &= \frac{x}{3}+\frac{1}{3} \\
x_{2} &= \frac{ \frac{x+1}{3}}{3} + \frac{1}{3} = \frac{x}{3^{2}} + \frac{1}{3^{2}} +\frac{1}{3} \\
x_{3} &= \frac{x}{3^{3}} + \frac{1}{3^{3}} + \frac{1}{3^{2}} + \frac{1}{3}.
\end{aligned}
$$


In general, one can show by induction that 


$$
x_{n} = \frac{x}{3^{n}} + \frac{1}{3^{n}} + \frac{1}{3^{n-1}} + \dots + \frac{1}{3}.
$$


Now, if $$a \neq 1$$, $$1+a+a^{2}+\dots+a^{n} = \frac{1-a^{n+1}}{1-a}$$. Then 


$$
x_{n} = \frac{x}{3^{n}} + \frac{ 1-\left( \frac{1}{3} \right)^{n+1} }{\frac{2}{3}} - 1 = \frac{x}{3^{n}} + \frac{3}{2}\left( 1-\left( \frac{1}{3} \right)^{n+1} \right) -1.
$$


Therefore $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{2}$$. 
### Theorem (Convergence under permutation)
Let $$\phi: \mathbb{N} \to\mathbb{N}$$ be a bijection and let $$\{a_{n}\}_{n=0}^\infty$$ be such that $$\sum_{n=0}^\infty \lvert a_{n} \rvert$$ converges. Then $$\sum_{n=0}^\infty a_{\phi(n)}$$ converges and moreover $$\sum_{n=0}^\infty a_{\phi_{n}} = \sum_{n=0}^\infty a_{n}$$. 

***Proof:*** Define 


$$
S_{k} = \sum_{n=0}^{k} a_{n}, \quad \tilde{S}_{k} = \sum_{n=0}^{k} \lvert a_{n} \rvert, \quad U_{k} = \sum_{n=0}^{k} a_{\phi(n)}.
$$


We know that $$\sum_{n=0}^\infty \lvert a_{n} \rvert$$ converges. Then, given $$\varepsilon>0$$, there exists $$N$$ such that $$\lvert \tilde{S}_{n} - \tilde{S}_{m} \rvert < \varepsilon$$ for all $$m\geq n\geq N$$. Then 


$$
\lvert a_{n+1} \rvert + \lvert a_{n+2} \rvert +\dots+ \lvert a_{m} \rvert < \varepsilon.
$$


We must show that $$\lim_{ k \to \infty } S_{k} = \ell = \lim_{ k \to \infty } U_{k}$$. Take $$N_{1}$$ such that $$\lvert S_{k} - \ell \rvert < \varepsilon$$ if $$k \geq N_{1}$$. Since $$\phi$$ is a bijection, we know that for every $$m \in \mathbb{N}$$ there exists $$n_{m}$$ such that $$\phi(n_{m})$$. Take $$M = \max \phi^{-1}[\{ 1,\dots,N \}]$$. Then $$\{ 1,\dots,N \} \subseteq \{ \phi(1),\dots,\phi(M) \}$$. Then, for $$m\geq M$$, $$k \geq N$$, we have that 


$$
\lvert U_{m} - S_{k} \rvert \leq  \lvert a_{N+1} \rvert +\dots+\lvert a_{\ell} \rvert < \varepsilon.
$$
{% endraw %}
