---
layout: chapter
course: ma0350
chapter: 10
title: "Series of Functions"
slug: 10-series-of-functions
toc:
  sidebar: right
lang: en
fecha: 2025-06-24
permalink: /notes/ma0350/10-series-of-functions/
---

{% raw %}
Let $$f_{n}:A\to \mathbb{R}$$ be a sequence of functions. Consider $$S_{n}(x) = \sum_{i=1}^{n} f_{i}(x)$$. Note that $$S_{n}(x)$$ is a sequence of functions 

### Definition (convergence of a series of functions)
We say that $$\sum_{n=1}^\infty f_{n}(x)$$ converges:
1. pointwise if the $$S_{n}(x)$$ converge pointwise.
2. uniformly if the $$S_{n}(x)$$ converge uniformly
3. absolutely if $$\sum_{i=1}^{\infty} \lvert f_{i}(x) \rvert$$ converges (pointwise or uniformly). 
### Lemma (Cauchy if and only if uniform convergence) 
Let $$f_{n}:A\to \mathbb{R}$$ be functions. Then $$\sum_{n=1}^\infty f_{n}$$ converges uniformly if and only if for every $$\varepsilon>0$$ there exists $$N$$ such that for every $$x  \in A$$ 


$$
\lvert S_{n}(x) - S_{m}(x) \rvert < \varepsilon
$$


if $$n,m \geq N$$. Equivalently, if $$n>m\geq N$$, then for every $$x \in A$$ 


$$
\lvert f_{m+1}(x) + f_{m+2}(x) + \dots + f_{n}(x) \rvert < \varepsilon.
$$



### Lemma (Weierstrass M-test) 
Let $$f_{n}:A\to \mathbb{R}$$ be a sequence of functions and $$\{a_{n}\}_{n=1}^\infty$$ a convergent sequence such that 
1. $$\sum_{n=1}^\infty a_{n}$$ converges, 
2. $$\lvert f_{n}(x) \rvert \leq a_{n}$$ for every $$x \in A$$. 

Then $$\sum_{n=1}^\infty \lvert f_{n}(x) \rvert$$ converges uniformly.

***Proof:*** Given $$\varepsilon>0$$ there exists $$N$$ such that for all $$n,m\geq N$$ 


$$
\begin{aligned}
\lvert a_{m}+a_{m+1}+\dots+a_{n} \rvert < \varepsilon \iff &a_{m} + a_{m+1} + \dots + a_{n} < \varepsilon \\
\implies \lvert f_{m}(x) \rvert + \lvert f_{m+1}(x) \rvert + \dots+ \lvert f_{n}(x) \rvert <  \quad  &a_{m} + a_{m+1} + \dots + a_{n} < \varepsilon
\end{aligned}
$$


for every $$x \in A$$, $$n,m\geq N$$. 
#### Example 
Consider $$\sum_{k=1}^\infty \frac{\sin(kx)}{k^{2}}$$. Note that $$\left\lvert  \frac{\sin(kx)}{k^{2}}  \right\rvert \leq \frac{1}{k^{2}}$$. Since $$\sum_{k=1}^\infty \frac{1}{k^{2}}$$ converges, by the M-test $$\sum_{k=1}^\infty \frac{\sin(kx)}{k^{2}}$$ converges uniformly. 

#### Example 
Consider $$\sum_{k=1}^\infty x^{k}$$ for $$\lvert x \rvert<1$$. In those cases it converges pointwise. Let $$0<a<1$$. If $$\lvert x \rvert \leq a$$, then $$f_{n}(x) = \lvert x \rvert^{n} \leq a^{n} = a_{n}$$. Since $$a<1$$, the series $$\sum_{n=1}^\infty a^{n}$$ converges. Then by the M-test, $$\sum_{n=1}^\infty x^{n}$$ converges uniformly on $$\lvert x \rvert \leq a$$.

### Lemma (Continuity, integrability and differentiability)
Let $$f_{n}:A\to \mathbb{R}$$ be a sequence of functions such that $$\sum_{n=1}^\infty f_{n}(x)$$ converges uniformly to a function $$f(x)$$.
1. If $$f_{n}(x)$$ is continuous then $$f(x)$$ is continuous.
2. If the $$f_{n}$$ are R-integrable, then $$f$$ is R-integrable. Moreover 


$$
\int_{a}^{b} \left( \sum_{n=1}^\infty f_{n}(x) \right) \, dx = \int_{a}^{b} f(x) \, dx = \sum_{n=1}^\infty \int_{a}^{b} f_{n}(x) \, dx 
$$


3. If $$f_{n}:A \to \mathbb{R}$$ is differentiable and 
1.  $$\sum_{n=1}^\infty f_{n}'(x)$$ converges uniformly
2. $$\sum_{n=1}^\infty f_{n}(x_{0})$$ converges for some $$x_{0} \in A$$,   
then $$\sum_{n=1}^\infty f_{n}(x)$$ converges uniformly to a function $$f(x)$$ and $$f'(x) = \sum_{n=1}^\infty f_{n}'(x)$$.

#### Example 
Let $$f_{n}(x) = \frac{x^{n}}{n^{3}}$$. Does $$\sum_{n=1}^\infty \frac{x^{n}}{n^{3}}$$ converge uniformly on $$[-1,1]$$? Since $$\left\lvert  \frac{x^{n}}{n^{3}}  \right\rvert \leq  \frac{1}{n^{3}}$$ and $$\sum_{n=1}^\infty \frac{1}{n^{3}}$$ converges, the series converges uniformly by the M-test.

Let $$f(x) = \sum_{n=1}^\infty \frac{x^{n}}{n^{3}}$$; then $$f$$ is continuous and R-integrable. On the other hand, $$f_{n}'(x) = \frac{nx^{n-1}}{n^{3}} = \frac{x^{n-1}}{n^{2}}$$, which converges uniformly by the M-test, since 


$$
\frac{x^{n-1}}{n^{2}} \leq  \frac{1}{n^{2}} \quad \text{and} \quad \sum_{n=0}^\infty \frac{1}{n^{2}} \text{ converges.}
$$


Moreover, $$f'(x) = \sum_{n=1}^\infty \frac{x^{n-1}}{n^{2}}$$.

### Theorem (Dirichlet's test)
Let $$f_{n}:A\to \mathbb{R}$$ be a sequence of functions such that 
1. there exists $$M \in \mathbb{R}$$ such that 


$$
\underset{x \in A}{\sup} \left\{  \sum_{k=1}^{n} f_{k}(x)  \right\} = \underset{x \in A}{\sup} \left\{  S_{n}(x)  \right\} \leq  M.
$$


Assume moreover that $$g_{n}:A\to \mathbb{R}$$ satisfies 
2. $$g_{n} \geq 0$$ ,
3. $$g_{n}(x)\geq g_{n+1}(x)$$ for every $$x \in A$$ (decreasing in $$n$$) ,
4. $$\lim_{ n \to \infty } g_{n}(x) = 0$$ uniformly. 

Then $$\sum_{n=1}^\infty f_{n}(x)g_{n}(x)$$ converges uniformly.

***Proof:*** 
Consider 


$$
\sum_{k=n}^{m} f_{k}(x) g_{k}(x) = g_{m}(x)S_{m}(x) - g_{n}(x) S_{n-1}(x) + \sum_{j=n}^{m-1} (g_{j}-g_{j+1}) S_{j} (x),
$$


where $$S_{m}(x) = \sum_{i=1}^{m} f_{i}(x)$$. Given $$\varepsilon>0$$, there exists $$N$$ such that for every $$x \in A$$, $$\lvert g_{n}(x) \rvert < \frac{\varepsilon}{2M}$$ if $$n\geq N$$. Now, 


$$
\begin{aligned}
\left\lvert  \sum_{j=n}^{m-1} (g_{j}(x) - g_{j+1}(x))S_{j}(x)  \right\rvert &\leq \sum_{j=n}^{m-1} \lvert g_{j}(x) - g_{j+1}(x) \rvert   \lvert S_{j}(x) \rvert \\
& \leq M \sum_{=}^\infty (g_{j}(x)-g_{j+1}(x)) \\
& = M(g_{n}(x)-g_{m}(x)).
\end{aligned}
$$


Therefore 


$$
\begin{aligned}
\left\lvert  \sum_{k=n}^{m} f_{k}(x) g_{k}(x)  \right\rvert &\leq  \lvert g_{n}(x) \rvert \lvert S_{m}(x) \rvert + \lvert g_{n}(x) \rvert \lvert S_{n-1}(x)\rvert + M (g_{n}(x)-g_{m}(x)) \\
&\leq g_{m}(x) M + g_{n}(x) M + M(g_{n}(x) - g_{m}(x)) = 2M g_{n}(x) < \varepsilon.
\end{aligned}
$$



#### Example 
Consider $$\sum_{k=1}^{\infty} \frac{\sin(kx)}{k}$$. Note that 


$$
\left\lvert  \sum_{k=1}^{n} \sin(kx)  \right\rvert =\frac{\left\lvert  \cos\left( \frac{x}{2} \right) - \cos\left( \left( n-\frac{1}{2} \right) x\right)  \right\rvert}{2 \sin\left( \frac{x}{2} \right)} \leq \frac{2}{2\sin(x^{2})} < M 
$$


for every $$x \in [\delta, 2\pi-\delta$$, with $$0 < \delta <n - \delta$$.

### Theorem (Abel's test)
Let $$f_{n}:A\to \mathbb{R}$$ be a sequence of functions such that 
1. $$\sum_{n=1}^{\infty} f_{n}(x)$$ converges uniformly.
2. $$g_{n}:A\to \mathbb{R}$$ is monotone,
3. there exists $$K \in \mathbb{R}$$ such that $$\underset{x \in A}{\sup}\{ \lvert g_{n}(x) \rvert \} \leq k$$ for every $$n \in \mathbb{N}$$.
Then $$\sum_{n=1}^{\infty} f_{n}(x) g_{n}(x)$$ converges uniformly.

***Proof:*** 
Let $$S = \sum_{n=1}^\infty f_{n}(x)$$ and  $$S_{n}(x) = \sum_{k=1}^{n} f_{k}(x)$$. Note that 


$$
\begin{aligned}
\sum_{j=n}^{m} f_{j}(x)g_{j}(x) &= g_{m} S_{m} - g_{n} S_{n-1} + \sum_{j=n}^{m-1} (g_{j}-g_{j-1}) S_{j} \\
&= g_{m}(S-S_{m}) - g_{n}(S-S_{n-1}) + \sum_{j=n}^{m-1} (g_{j}-g_{j+1})(S-S_{j})
\end{aligned}
$$


Given $$\varepsilon>0$$, there exists $$N \in \mathbb{N}$$ such that for every $$\ell\geq N$$ and every $$x \in A$$, 


$$
\lvert S(x)-S_{\ell}(x) \rvert < \frac{\varepsilon}{3K} 
$$


for $$\ell\geq N$$ and $$x \in A$$. Then 


$$
\begin{aligned}
\lvert g_{n}(x) \rvert \lvert S(x) - S_{n-1}(x) \rvert &< \frac{\varepsilon}{4} \\
\lvert g_{n}(x) \rvert \lvert S(x) - S_{m}(x) \rvert &< \frac{\varepsilon}{4}, 
\end{aligned}
$$


if $$n-1,m\geq N$$.
On the other hand, 


$$
\begin{aligned}
\left\lvert  \sum_{j=n}^{m-1} (g_{j}(x) - g_{j+1}(x))(S(x)-S_{j}(x)) \right\rvert &\leq \sum_{j=n}^{m-1} \lvert g_{i}(x) - g_{i+1}(x) \rvert \lvert S(x) - S_{j}(x) \rvert  \\
&< \frac{\varepsilon}{4k} \sum_{j=n}^{m-1} \lvert g_{j}(x) - g_{j-1}(x) \rvert  
\end{aligned}
$$


#### Example 
Consider $$S(x) = \sum_{n=1}^\infty \frac{(-1)^{n}}{n}e^{-xn}$$ for $$x \in [1,+\infty)$$. Note that $$\lvert g_{n}(x) \rvert = \left\lvert  \frac{1}{n}  \right\rvert \leq 1$$. Now, $$\lvert (-1)^{n} \exp(-xn) \rvert \leq \exp(-n)$$ and $$\sum_{n=1}^\infty \exp(-n)$$ converges, so the series under study converges uniformly.

# Power series

Consider $$f_{n}(x) = a_{n} x^{n}$$ and $$S_{n}(x) = \sum_{k=0}^{n} a_{n} x^{n}$$, where $$\{a_{n}\}_{n=0}^\infty$$ is a sequence.

Consider $$\sqrt[n]{\lvert a_{n} \rvert \lvert x^{n} \rvert} = \lvert x \rvert \sqrt[n]{\lvert a_{n} \rvert}$$. To apply the root test I need to study $$\sqrt[n]{\lvert a_{n} \rvert}$$. We are going to prove that there is uniform convergence on $$[-p,p]$$, with $$p < R$$, and pointwise convergence on $$(-R,R)$$.


$$
p + \varepsilon < R =\frac{1}{\limsup \sqrt[n]{\lvert a_{n} \rvert}} \iff \limsup \sqrt[n]{\lvert a_{n} \rvert } < \frac{1}{p+\varepsilon}.
$$

 
If $$\limsup \sqrt[n]{\lvert a_{n} \rvert} = \underset{n\geq 1}{\inf} \underset{k\geq n}{\sup} \{ \sqrt[k]{\lvert a_{k} \rvert } \} < \frac{1}{p+\varepsilon}$$, then there exists $$n_{0}$$ such that 


$$
\underset{k\geq n_{0}}{\sup} \{ \sqrt[k]{\lvert a_{k} \rvert } \} < \frac{1}{p+\varepsilon}.
$$


Then $$\sqrt[k]{\lvert a_{k} \rvert} \leq \frac{1}{p + \varepsilon}$$ for every $$k\geq n_{0}$$. Now, 


$$
\begin{aligned}
\sqrt[n]{\lvert a_{k} \rvert } < \frac{1}{p+\varepsilon} &\iff \lvert a_{k} \rvert < \frac{1}{(p+\varepsilon)^{k}} \\ 
&\implies \lvert x^{k}  \rvert \lvert a_{k} \rvert < \left( \frac{\lvert x \rvert }{p+\varepsilon}  \right)^k \leq \left( \frac{p }{p+\varepsilon}  \right)^k  
\end{aligned}
$$


for $$\lvert x \rvert \leq p$$. Since $$\sum_{k=1}^\infty \left( \frac{p}{p+\varepsilon} \right)^{k}$$ converges, we conclude that $$\sum_{k=1}^\infty a_{k} x^{k}$$ converges uniformly by the M-test.

So the series converges pointwise on $$(-R, R)$$ with $$R = \frac{1}{\limsup \sqrt[n]{ \lvert a_{n} \rvert}}$$ and converges uniformly on $$[-p,p]$$ with $$p < R$$. The same applies to $$\hat{S}(x) = \sum_{k=1}^\infty a_{k}(x-x_{0})^{k}$$, which converges **pointwise** if $$-R < x-x_{0} < R$$.

#### Exercise 
Let $$\{a_{n}\}_{n=1}^\infty$$ and $$\{b_{n}\}_{n=1}^\infty$$ be two sequences with $$b_{n} \underset{n \rightarrow \infty}{\longrightarrow}b$$. Then
1. $$\limsup(a_{n}+b_{n}) = (\limsup a_{n}) + b$$.
2. $$\limsup(a_{n} b_{n}) = b \limsup a_{n}$$.

### Lemma (Differentiation and radius of convergence)
Let $$f_{n}(x) = a_{n} x^{n}$$ and $$f_{n}'(x) = n a_{n} x^{n}$$. Then the power series $$S(x) = \sum_{n=0}^\infty f_{n}(x)$$ and $$S'(x) = \sum_{n=0}^\infty n a_{n} x^{n-1}$$ have the same radius of convergence.

***Proof:***  Consider $$\sum_{n=0}^\infty a_{n} n x^{n-1}$$, which has radius of convergence $$\frac{1}{\limsup \sqrt[n]{n \lvert a_{n} \rvert}}$$. Expanding: 


$$
\limsup \sqrt[n]{n \lvert  a_{n} \rvert } = \limsup \sqrt[n]{n} \sqrt[n]{\lvert a_{n} \rvert } = \limsup \sqrt[n]{a_{n}},
$$


where we used the fact that 


$$
\lim_{ n \to \infty } \sqrt[n]{n} = \lim_{ n \to \infty } \exp\left( \frac{\ln(n)}{n} \right) = \exp(0) = 1.
$$


Hence the series 


$$
\sum_{n=0}^\infty n a_{n} x^{n-1} = \frac{1}{x}\sum_{n=0}^\infty n a_{n} x^{n} \quad \text{and} \quad \sum_{n=0}^\infty a_{n}x^{n}
$$


have the same radius of convergence.

### Lemma (R-integration and radius of convergence)

***Proof:***  If $$S(x) = \sum_{n=0}^\infty a_{n} x^{n}$$ converges uniformly on $$[-p,p]$$ with $$p <R$$, then


$$
\int_{0}^{x} S(y) \, dy = \sum_{n=0}^\infty \int_{0}^{x} a_{n} y^{n} \, dy = \sum_{n=0}^\infty a_{n} \frac{x^{n+1}}{n+1}.
$$


Analysing the radius of convergence, note that 


$$
\limsup \sqrt[n]{\frac{\lvert a_{n} \rvert }{n+1}} = \limsup \frac{\sqrt[n]{\lvert a_{n} \rvert }}{\sqrt[n]{n+1}} = \limsup \sqrt[n]{\lvert  a_{n} \rvert, }
$$


since $$\limsup \sqrt[n]{n+1} = \lim_{ n \to \infty } \sqrt[n]{n+1}$$. We conclude then that 


$$
\sum_{n=0}^\infty a_{n} \frac{x^{n+1}}{n+1} \quad \text{and} \quad \sum_{n=0}^\infty a_{n}x^{n}
$$


have the same radius of convergence.

## Taylor series

#### Example 
Let $$\lvert x \rvert < 1$$ and consider $$\sum_{n=0}^\infty x^{n} = \frac{1}{1-x}$$. Since $$\limsup \sqrt[n]{1} = 1$$, we have uniform convergence on $$[-p,p]$$, with $$0<p<1$$. Then 


$$
\begin{aligned}
\int_{0}^{x} \frac{1}{1-y} \, dy  &= \int_{0}^{x} \sum_{n=0}^\infty y^{n} \, dy \\
\iff -\ln(1-x) &= \sum_{n=0}^\infty \frac{x^{n+1}}{n+1}.
\end{aligned}
$$


Manipulating the resulting expression, for $$\lvert x \rvert < 1$$ we have that


$$
\begin{aligned}
-\ln(1+x) &= \sum_{n=0}^{\infty} \frac{(-x)^{n+1}}{n+1} \\
\iff \ln(1+x) &= \sum_{n=0}^\infty (-1)^{n} \frac{x^{n+1}}{n+1}.
\end{aligned}
$$


Could it happen that, for two different sequences, the associated power series converge to the same function? Note that 


$$
S^{(n)}(x) = \left( \sum_{k=0}^\infty a_{k} x^{k}  \right)^{(n)} = \sum_{k=n}^\infty a_{k} k(k-1) \dots (k-n+1) x^{k-n}.
$$


Evaluating, 


$$
S^{(n)}(0) =  n(n-1)(n-2)\dots \cdot 2 \cdot 1 \cdot a_{n} = n! a_{n} \iff \frac{S^{(n)}(0)}{n!} = a_{n},
$$


so the sequence $$a_{n}$$ is unique for each function.

### Theorem (Taylor)
Let $$f:[a,b] \to \mathbb{R}$$ be a function such that $$f',f'',\dots,f^{(n)}$$ are continuous on $$[a,b]$$. If $$f^{(n+1)}$$ exists on $$[a,b]$$ and $$x_{0} \in (a,b)$$, then there exists $$c$$ between $$x_{0}$$ and $$x$$ such that 


$$
f(x) = f(x_{0}) + f'(x_{0})(x-x_{0}) + \dots+f^{(n)}(x_{0}) \frac{(x-x_{0})^{n}}{n!} + R_{n}(x),
$$


with $$R_{n}(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-x_{0})^{n+1}$$.

Consider the power series


$$
S(x) = \sum_{n=0}^\infty a_{n}(x-x_{0})^{n}, \quad \text{with }a_{n} = \frac{f^{(n)}(x_{0})}{n!}
$$


Is it true that $$S(x) = f(x)$$? Consider the partial sum $$S_{k}(x) = \sum_{n=0}^{k} a_{n}(x-x_{0})^{n}$$. Then 


$$
\lvert f(x) - S_{k}(x) \rvert = \lvert R_{k}(x) \rvert = \left\lvert  \frac{f^{(n+1)}(c)}{n+1} (x-x_{0})^{n+1}  \right\rvert \overset{?}{\underset{n \rightarrow \infty}{ \longrightarrow}}  0.
$$


If the remainder converges to zero, the Taylor series converges to the function.

#### Example 
Consider $$f(x) = \sin(x)$$. Then 


$$
\begin{aligned}
f'(x) &= \cos(x) \\
f''(x) &= -\sin(x) \\
f'''(x) &= -\cos(x) \\
f^{(4)}(x) &= \sin(x).
\end{aligned}
$$


In general, for $$x_{0}=0$$ we have that 


$$
f^{(2n)}(x) = 0,  \quad f^{(2n+1)}(0) = (-1)^{n}.
$$


Considering the Taylor series $$\sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{(2n+1)!}$$, note that $$\limsup \sqrt[2n+1]{\frac{1}{(2n+1)!}} = 0$$. Hence the series converges on $$\mathbb{R}$$ and uniformly on $$[-p,p]$$ for any $$p>0$$. On the other hand, 


$$
\begin{aligned}
\lvert \sin(x) - S_{n}(x) \rvert &= \left\lvert  \frac{f^{(n+1)}(c)}{(n+1)!} x^{n+1}  \right\rvert.
\end{aligned}
$$


Since 


$$
f^{(n+1)}(c) \begin{cases}
= \lvert \sin(c) \rvert \\ \\
= \lvert \cos(cazx  \quad) \rvert 
\end{cases} \leq  1,
$$


we get $$\lvert \sin(x) - S_{n}(x) \rvert \leq \frac{\lvert x^{n+1} \rvert}{(n+1)!}$$. Now, for $$\lvert x \rvert < p$$, 


$$
\lvert \sin(x) - S_{n}(x) \rvert \leq \frac{\lvert \rho^{n+1} \rvert }{(n+1)!} < \varepsilon
$$


for  $$n\geq N_{0}$$, by the ratio test for limits.

#### Example 
Consider $$f(x) = \exp(x)$$. Then $$f^{(n)}(x) = \exp(x)$$. Hence, for $$x_{0}=0$$, the Taylor series is given by 


$$
\sum_{n=0}^\infty \frac{x^{n}}{n!}, \quad \text{with } R = +\infty.
$$


Note that 


$$
S'(x) = \sum_{n=1}^\infty n \frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{n=0}^\infty \frac{x^{n}}{n!}. 
$$


We will prove that $$S(x)S(y) = S(x+y)$$. Let $$c \in \mathbb{R}$$ and $$h(x) = S(x)S(c-x)$$. Then 


$$
h'(x) = S'(x)S(c-x) - S(x)S'(c-x) =S(x)S(c-x) - S(x)S(c-x) = 0,
$$


so $$h(x)$$ is constant. Hence 


$$
h(x) = S(x) S(c-x) = S(c) S(0) = S(c).
$$


Evaluating at $$c = x+y$$, we get $$S(x)S(y) = S(x+y)$$.

Now, 


$$
\begin{aligned}
\lvert \exp(x) - S_{k}(x) \rvert = \left\lvert  \frac{f^{(n+1)}(c)}{(n+1)!} x^{n+1}  \right\rvert = \left\lvert  \frac{e^{c}}{(n+1)!} x^{n+1}  \right\rvert \leq  \frac{e^{p}}{(n+1)!} p^{n+1} \underset{n \rightarrow \infty}{\longrightarrow} 0
\end{aligned}
$$


for $$x \in [-p,p]$$ with $$c$$ between 0 and $$x$$.

##### Exercise 
Prove that $$\exp(x) \geq 0$$ for every $$x$$.
#### Example 
Consider $$f(x) = \cos(x)$$. Then


$$
\cos(x) = \sum_{n=0}^\infty (-1)^{n} \frac{x^{2n}}{(2n)!}, \quad \sin(x) = \sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{(2n+1)!}.
$$


Then 


$$
\begin{aligned}
\cos'(x) &= \sum_{n=1}^\infty (-1)^{n} (2n) \frac{x^{2n-1}}{(2n)!} \\
&= \sum_{n=1}^\infty (-1)^{n} \frac{x^{2n-1}}{(2n-1)!} \\
&= \sum_{n=0}^\infty (-1)^{n+1} \frac{x^{2n+1}}{(2n+1)!} \\
&= - \sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{(2n+1)!} = -\sin(x).
\end{aligned}
$$


In an analogous way, we can prove that $$\sin'(x) = \cos(x)$$. 

Note that $$\sin(0)=0$$, $$\cos(0)=1$$. Moreover, 


$$
(\sin^{2}(x)+\cos ^{2}(x))' = 2\sin x\cos x + 2 \sin x \cos x + 2 \cos x(-\sin x) = 0.
$$


Hence $$\sin ^{2}(x)+\cos^{2}(x) = \sin ^{2}(0)+\cos^{2}(0) = 1$$.

##### Exercise 
Prove that $$\sin(x+y)=\sin(x)\cos(y) + \cos(x)\sin(y)$$ and that $$\cos(x+y) = \cos(x)\cos(y) - \sin(x)\sin(y)$$.

Now note that 


$$
\cos(x) = \sum_{n=}^\infty (-1)^{n} \frac{x^{2n}}{(2n)!} = \left( 1-\frac{x^{2}}{2}  \right) + \left( \frac{x^{4}}{4!} - \frac{x^{6}}{6!}\right) + \cdots,
$$


so $$\cos(x)\geq 0$$ if 


$$
\begin{aligned}
\frac{x^{2n}}{(2n)!} - \frac{x^{2n+2}}{(2n+2)!} &\geq 0 \\
\iff {x^{2n}}{(2n)!} &\geq \frac{x^{2n+2}}{(2n+2)!} \\
\iff (2n+1)(2n+2) \geq  x^{2},
\end{aligned}
$$


which holds for $$0\leq x\leq 1$$. Note that if $$\cos(x)\geq 0$$ then $$\sin'(x) \geq 0$$ and so $$\sin$$ is increasing. Therefore, if $$\cos(x)\geq 0$$ for every $$x \in [0,p]$$, $$\sin$$ is increasing on $$[0,p]$$. Moreover, since $$\sin(0) = 0$$, we have that $$\sin(x) \geq 0$$ for $$x \in [0,p]$$. Hence $$\cos(x)$$ is decreasing.

We will now prove that there exists $$c \in \mathbb{R}$$ such that $$\cos(c) < 0$$. We know that $$\cos(0) = 1$$ and $$\sin(0) = 0$$. Using the Taylor series of the cosine, we have that 


$$
\cos(y) \leq  1 \iff \int_{0}^{x} \cos(y) \, dy \leq  \int_{0}^{x} 1 \, dy \iff \sin(x) \leq  x.
$$


Hence 


$$
\int_{0}^{x} \sin(y) \, dy \leq  \int_{0}^{x} y \, dy = \frac{x^{2}}{2} \iff 1-\cos(x) \leq \frac{x^{2}}{2} \iff 1-\frac{x^{2}}{2} \leq  \cos(x).
$$


Integrating both sides of this last inequality, we have that $$\sin(x)\geq x - \frac{x^{3}}{6}$$, and integrating once more, we have that 


$$
\cos(x) \leq 1-\frac{x^{2}}{2}+\frac{x^{4}}{4!},
$$


from which, evaluating at $$x = \sqrt{ 3 }$$, we get a negative value on the right-hand side and therefore prove that $$\cos(\sqrt{ 3 }) \leq 0$$, i.e., there are values where the cosine is negative.

By continuity, there exists some zero of the function. Let $$p$$ be the first zero. 

We now analyse the period of $$\sin$$ and $$\cos$$. Since $$\cos(p) = 0$$, we have that 


$$
\begin{aligned}
\sin(2p) = \sin(p)\cos(p) + \sin(p) \cos(p) &= 0, \\
\sin ^{2}(p) +\cos ^{2}(p) = \sin ^{2}(p) &= 1 \implies \sin(p) = \pm 1.
\end{aligned}
$$


Note that 


$$
\begin{aligned}
\sin(x+4p) &= \sin(x) \cos(4p) + \cos(x) \sin(4p),\\
\sin(4p) &= \sin(2p)\cos(2p) + \sin(2p)\cos(2p) = 0 \\
\cos(4p) &= \cos(2p)^{2} - \sin(2p)^{2} = 1  \quad \text{since } \cos(2p) =\pm 1,
\end{aligned}
$$


from which we conclude that $$\sin(x+4p) = \sin(x)$$. 

#### Example 
We had seen that 


$$
\ln(1+x) = \sum_{n=0}^\infty (1)^{n+1} \frac{x^{n+1}}{n+1}.
$$


Observing that 


$$
\frac{(\ln(1+x))^{(n)}}{n!} \biggr\rvert_{x=0} = \frac{(-1)^{n+1}}{n+1},
$$


we have that the Taylor series converges to the function.

![Pasted image 20250708163347](/assets/img/courses/ma0350/Pasted%20image%2020250708163347.png)

## Tricks
1. If $$\lim_{ n \to \infty } \sqrt[n]{a_{n}}$$ is very hard, use the fact that $$\lim_{ n \to \infty } \frac{a_{n+1}}{a_{n}}$$ must have the same value.
2. Compute the supp whenever we are stuck
{% endraw %}
