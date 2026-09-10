---
layout: chapter
course: ma0350
chapter: 11
title: "Convergence of Functions"
slug: 11-convergence-of-functions
toc:
  sidebar: right
lang: en
fecha: 2025-06-17
permalink: /notes/ma0350/11-convergence-of-functions/
---

{% raw %}
### Definition (Pointwise convergence)
A sequence of functions $$f_{n}:A \to \mathbb{R}$$ converges pointwise to $$f:A \to \mathbb{R}$$ if for every $$x \in A$$ we have that $$\lim_{ n \to \infty } f_{n}(x)=f(x)$$.

#### Example 
Consider $$f_{n}(x) = x^{n}$$ for $$x \in (-1,+\infty)$$.
Note that 


$$
\lim_{ n \to \infty } f_{n}(x) \begin{cases}
0  \quad \text{if } \lvert x \rvert <1 \\
1  \quad \text{if } x=1 \\
\infty  \quad \text{if } x>1
\end{cases}.
$$


Let 


$$
f(x) = \begin{cases}
0  \quad \text{if } x \in (-1,1) \\
1  \quad \text{if } x=1
\end{cases}.
$$


Then $$f_{n}$$ converges point by point to $$f$$ on $$(-1,1]$$. How would we prove this from the definition?

***Proof:***  Let $$\varepsilon>0$$. Let $$N  = \max \left\{  1, \left\lfloor  \frac{\ln(\varepsilon)}{\ln(\lvert x \rvert)}  \right\rfloor -1  \right\}$$. Then, for $$n\geq N$$,


$$
n > \frac{\ln(\varepsilon)}{\ln\lvert x \rvert } \iff n\ln \lvert x \rvert < \ln \varepsilon \iff \lvert x^{n} \rvert = \lvert x \rvert ^{n} < \varepsilon.
$$


***CAREFUL:*** Note that $$N = N(x, \varepsilon)$$. If $$x$$ changes, $$N$$ changes. Moreover, $$\lim_{ x \to 1^{-} } N = +\infty$$. That is, there is no $$N$$ such that $$\lvert x^{n} \rvert < \varepsilon$$ for every $$n>N$$ and every $$x \in (-1, 1])$$

### Definition (Uniform convergence) 
A sequence of functions $$f_{n}:A\to \mathbb{R}$$ converges uniformly to $$f:A\to \mathbb{R}$$ if for every $$\varepsilon>0$$ there exists $$N \in \mathbb{N}$$ such that for $$n\geq N$$ we have that, for every $$x \in A$$, 


$$
\lvert f_{n}(x)-f(x) \rvert < \varepsilon.
$$



#### Example 
Consider now the same sequence of functions as in the previous example but with $$x \in (0,a)$$, where $$a<1$$. We will prove that it converges uniformly.

***Proof:***  Let $$\varepsilon>0$$. Let $$N  = \max \left\{  1, \left\lfloor  \frac{\ln(\varepsilon)}{\ln(a)}  \right\rfloor -1  \right\}$$. Then, for $$n\geq N$$ and for every $$x \in (0,a)$$


$$
n > \frac{ln(\varepsilon)}{\ln (a)}\geq  \frac{\ln(\varepsilon)}{\ln\lvert x \rvert } \iff n\ln \lvert x \rvert < \ln \varepsilon \iff \lvert x^{n} \rvert = \lvert x \rvert ^{n} < \varepsilon.
$$



### Definition (Supremum norm)
Let $$f:A\to \mathbb{R}$$ be bounded. Define $$\lVert f \rVert_{\infty} := \sup \{ \lvert f(x) \rvert: x \in A \}$$. Note that if $$\lVert f \rVert_{\infty} = 0$$, then $$\lvert f(x) \rvert \leq 0$$ for every $$x \in A$$, and therefore $$f=0$$.

On the other hand, if $$f:A\to \mathbb{R}$$, $$g:A\to \mathbb{R}$$ are bounded, then 


$$
\sup \{ \lvert f(x) + g(x) \rvert: x \in A \} \leq  \sup \{ \lvert f(x) \rvert + \lvert g(x) \rvert : x \in A  \} \leq  \sup \{ \lvert f(x) \rvert: x \in A  \} + \sup \{ \lvert g(x) \rvert: x \in A  \}.
$$


Hence  $$\lVert f+g \rVert_{\infty} \leq \lVert f \rVert_{\infty} + \lVert g \rVert_{\infty}$$.
Therefore $$\lVert  \rVert_{\infty}$$ is a norm on the space of bounded functions $$A\to \mathbb{R}$$.

### Uniform convergence and the supremum norm
Let $$f_{n}:A\to \mathbb{R}$$ converge uniformly to $$f:A\to \mathbb{R}$$. Then, given $$\varepsilon>0$$, there exists $$N \in \mathbb{N}$$ such that if $$n\geq N$$, $$\lvert f_{n}(x) - f(x) \rvert < \varepsilon$$ for every $$x \in A$$. Hence 


$$
\sup \{ \lvert f_{n}(x) - f(x) \rvert : x \in A  \} \leq  \varepsilon,
$$


so $$\lVert f_{n}-f \rVert_{\infty} \leq \varepsilon$$ for $$n\geq N$$.

#### Exercise 
Let $$f_{n}:A\to \mathbb{R}$$ and $$f:A\to \mathbb{R}$$ be such that $$\lVert f_{n}-f \rVert_{\infty} \underset{n  \rightarrow \infty}{\longrightarrow} 0$$. Then $$f_{n}$$ converges uniformly to $$f$$.

#### Example 
Consider $$f_{n}(x) = x^{n}(1-x)$$ for $$x \in [0,1]$$. Then $$f_{n} \underset{n  \rightarrow \infty}{\longrightarrow} 0$$ pointwise. We will prove that it converges uniformly. 
Let $$0 < \delta < \min \left\{  \varepsilon,1  \right\}$$. Then, on $$[0,1-\delta]$$, we have that 


$$
\lvert x \rvert ^{n} \lvert 1-x \rvert < \varepsilon.
$$


Now, 


$$
\begin{aligned}
\lvert x^{n} \rvert \lvert 1-x \rvert &\leq \lvert x \rvert ^{n} < \varepsilon \\
\iff n > \left\lfloor  \frac{\ln(\varepsilon)}{\ln(1-\delta)}  \right\rfloor &= N.
\end{aligned}
$$


Hence, for $$n\geq N$$, we have that $$\lvert x^{n}(1-x) \rvert < \varepsilon$$ if $$x \in [0,1-\delta]$$.
On the other hand, if $$x \in [1-\delta,1]$$, then $$\lvert x^{n}(1-x) \rvert \leq 1-x \leq \delta < \varepsilon$$.

### Theorem (Boundedness of the limit function) 
 Let $$f_{n}:A\to \mathbb{R}$$ be bounded functions converging uniformly to $$f:A\to \mathbb{R}$$. Then $$f$$ is bounded.
 
***Proof:*** Let $$\varepsilon = 1$$. There exists $$N \in \mathbb{N}$$ such that $$\lvert f_{n}(x) - f(x) \rvert < 1$$ for every $$n\geq N$$. Then 


$$
f_{n}(x) -1 < f(x) < f_{n}(x)+1
$$


Since $$f_{n}$$ is bounded (for any $$n\geq N$$), we know that there exists $$M \in \mathbb{R}$$ such that $$-M \leq f_{n}(x) \leq M$$. Hence $$-M-1 \leq f(x) \leq M+1$$.

#### Example 
Consider $$f_{n}(x) = \frac{1}{x+1/n}$$; then $$\lvert f_{n}(x) \rvert \leq n$$ for $$x \in [0,+\infty]$$, but $$\lim_{ n \to \infty } f_{n}(x) = \frac{1}{x}$$ is not bounded. Therefore the convergence is not uniform.

#### Example 
### Theorem (Uniform convergence of continuous functions)
Let $$f_{n}:A\to \mathbb{R}$$ be continuous functions converging uniformly to $$f:A\to \mathbb{R}$$. Then $$f$$ is continuous.

***Proof:*** Let $$\varepsilon>0$$. There exists $$N \in \mathbb{N}$$ such that if $$n\geq N$$, 


$$
\lvert f_{n}(x) - f(x) \rvert < \frac{\varepsilon}{3}
$$


for every $$x \in A$$. Moreover, there exists $$\delta>0$$ such that if $$\lvert x-x_{0} \rvert < \delta$$, then $$\lvert f_{N}(x) - f_{N}(x_{0}) \rvert < \frac{\varepsilon}{3}$$. Hence, if $$\lvert x-x_{0} \rvert < \delta$$


$$
\begin{aligned}
\lvert f(x)-f(x_{0}) \rvert  &\leq \lvert f(x) - f_{N}(x) \rvert  + \lvert f_{N}(x) - f(x_{0}) \rvert  \\
&\leq \lvert f(x) - f_{N}(x) \rvert + \lvert f_{N}(x) - f_{N}(x_{0}) \rvert + \lvert f_{N}(x_{0}) - f_{N}(x) \rvert < \varepsilon.  
\end{aligned}
$$


Conclude that $$f$$ is continuous.

#### Example
Consider $$f_{n}(x) = x^{n}$$, $$x \in [0,1]$$. Note that 


$$
\lim_{ n \to \infty } f_{n}(x) = \begin{cases}
0  \quad \text{if } x \in [0,1) \\
1  \quad \text{if } x = 1
\end{cases}.
$$


Conclude that the convergence is not uniform.

### Definition (Uniformly Cauchy)
Let $$f_{n}:A\to \mathbb{R}$$ be a sequence of functions. We say that $$f_{n}$$ is uniformly Cauchy if, given $$\varepsilon>0$$, there exists $$N$$ such that if $$n,m\geq N$$ we have that $$\lvert f_{n}(x) - f_{m}(x) \rvert < \varepsilon$$ for every $$x \in A$$.

### Lemma  (Uniform convergence if and only if uniformly Cauchy)
Let $$f_{n}:A\to \mathbb{R}$$ be a sequence of functions and $$f:A\to \mathbb{R}$$. Then $$f_{n} \underset{n \rightarrow \infty}{\longrightarrow} f$$ uniformly if and only if $$f_{n}$$ is uniformly Cauchy.

***Proof:*** ($$\implies$$): Let $$\varepsilon>0$$. Then there exists $$N \in \mathbb{N}$$ such that for $$n\geq N$$ we have that $$\lvert f_{n}(x) - f(x) \rvert < \frac{\varepsilon}{2}$$ for every $$x \in A$$. Now for all $$n,m\geq N$$, 


$$
\lvert f_{n}(x)-f_{m}(x) \rvert \leq \lvert f_{n}(x) - f(x)\rvert + \lvert f(x) - f_{m}(x) \rvert  < \varepsilon.
$$


Therefore it is uniformly Cauchy.
($$\impliedby$$): Let $$\varepsilon>0$$. Then there exists $$N$$ such that for all $$m,n\geq N$$ we have that 
$$\lvert f_{n}(x)-f_{m}(x) \rvert < \frac{\varepsilon}{2}$$for every $$x \in A$$. 
Let $$x_{0} \in A$$. Then $$\{f_{n}(x_{0})\}_{n=1}^\infty$$ is Cauchy and therefore convergent, i.e., there exists $$\ell \in \mathbb{R}$$ such that $$f_{n}(x_{0}) \underset{n \rightarrow \infty}{\longrightarrow} \ell$$. Define $$f(x) = \lim_{ n \to \infty } f_{n}(x)$$. Then, given $$x \in A$$, there exists $$N_{0}\geq N$$ such that if $$n \geq N_{0}(x)$$ then 


$$
\lvert f(x) - f_{n}(x) \rvert < \frac{\varepsilon}{2}.
$$


Now, if $$m\geq N$$, 


$$
\begin{aligned}
\lvert f(x) - f_{m}(x) \rvert &\leq  \lvert f(x) - f_{N_{0}}(x) \rvert + \lvert f_{N_{0}}(x) - f_{m}(x) \rvert \\
& \leq \frac{\varepsilon}{2} + \lvert f_{N_{0}}(x) - f_{m}(x) \rvert < \varepsilon  \quad \text{since it is uniformly Cauchy.}
\end{aligned}
$$



### Theorem (Uniform convergence and Riemann integrability)
Let $$f_{n}:[a,b] \to \mathbb{R}$$ be Riemann integrable functions converging uniformly to $$f:[a,b] \to \mathbb{R}$$. Then $$f$$ is Riemann integrable and moreover 


$$
\lim_{ n \to \infty } \int_{a}^{b} f_{n}(x)   \, dx =  \int_{a}^{b} f(x) \, dx. 
$$



***Proof:***  Given $$\varepsilon>0$$, there exists $$N \in \mathbb{N}$$ such that for every $$n\geq N$$, $$\lvert f_{n}(x) - f(x) \rvert < \frac{\varepsilon}{4(b-a)}$$ for every $$x \in [a,b]$$. Since $$f_{N}$$ is Riemann integrable, there exists $$P_{\varepsilon}$$ such that $$U(f_{N}, P_{\varepsilon}) - L(f_{N},P_{\varepsilon}) < \frac{\varepsilon}{2}$$.
Let $$P_{\varepsilon} = \{ a_{0}=a < \dots < a_{n} = b \}$$. Then 


$$
(a_{i+1}-a_{i}) \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \} \leq \left( \sup \{ f_{N}(x) : a_{i} \leq x \leq  a_{i+1}\} + \frac{\varepsilon}{4(b-a)} \right)(a_{i+1}-a_{i}).
$$


since $$f_{N}(x) - \varepsilon \leq f(x) \leq f_{N}(x) + \varepsilon$$ for every $$x \in A$$. In the same way, 


$$
\sup \{ f_{N}(x):a_{i}\leq x\leq a_{i+1} \} - \frac{\varepsilon}{4(b-a)} \leq \sup \{ f(x):a_{i}\leq x\leq a_{i+1} \}.
$$


Then 


$$
U(f, P_{\varepsilon}) \leq U(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4}
$$


since 


$$
U(f, P_{\varepsilon}) = \sum_{i=0}^{n-1} \sup\{ f(x):a_{i}\leq x\leq a_{i+1} \} (a_{i+1}-a_{i}).
$$


In the same way, we have that 


$$
U(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4}\leq  U(f, P_{\varepsilon}),
$$


so that 


$$
U(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4} \leq U(f, P_{\varepsilon}) \leq U(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4}.
$$


In an analogous way (but working with infima instead of suprema) we can prove that 


$$
L(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4}\leq L(f, P_{\varepsilon}) \leq L(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4}.
$$


Finally, we have that 


$$
\begin{aligned}
U(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) &\leq  U(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4} - \left( L(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4} \right) \\
&= U(f_{N}, P_{\varepsilon}) - L(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{2} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon,
\end{aligned}
$$


from which we conclude that $$f$$ is Riemann integrable. For the proof of the limit of the integrals: given $$\varepsilon>0$$, there exists $$M \in \mathbb{N}$$ such that for every $$n\geq M$$ and $$x \in [a,b]$$, $$\lvert f(x) - f_{n}(x) \rvert < \frac{\varepsilon}{b-a}$$ Take 


$$
\begin{aligned}
\left\lvert  \int_{a}^{b} f_{n}(x) \, dx - \int_{a}^{b} f(x) \, dx    \right\rvert &= \left\lvert  \int_{a}^{b} (f_{n}(x) - f(x)) \, dx   \right\rvert \\
&\leq \int_{a}^{b} \lvert f_{n}(x)-f(x) \rvert  \, dx \\
&< \int_{a}^{b} \frac{\varepsilon}{b-a} \, dx = \varepsilon, 
\end{aligned}
$$


whenever $$n\geq M$$, from which the limit follows. 

#### Example 
For $$n \in \mathbb{N}$$, consider $$f_{n}:[0,1] \to \mathbb{R}$$ such that 


$$
f_{n}(x) = \begin{cases}
0  \quad\text{if } \frac{1}{n}\leq x\leq 1 \\
n^{2}x  \quad \text{if } 0\leq x < \frac{1}{n}
\end{cases}.
$$


Let $$x_{0} \in (0,1)$$. Then there exists $$n_{0}$$ such that $$\frac{1}{n_{0}} \leq x_{0}$$. Then $$f_{n}(x_{0}) = 0$$ if $$n \geq n_{0}$$. Now, 


$$
\int_{0}^{1} f_{n}(x) \, d = \int_{0}^{1/n}  n ^{2}x\, dx + \int_{1/n}^{1} 0  \, dx = \frac{n^{2}x^{2}}{2} \biggr\rvert_{0}^{1/n} = \frac{1}{2}.
$$


Then 


$$
\int_{0}^{1} f_{n}(x)  \, dx = \frac{1}{2} \underset{n \rightarrow \infty}{ \not\longrightarrow} \int_{0}^{1} 0 \, dx = 0.
$$



#### Exercise 
Find a sequence of Riemann integrable functions $$f_{n}$$ such that 


$$
f_{n} \underset{n \rightarrow \infty}{\longrightarrow} f = \begin{cases}
1  \quad \text{if }x \in \mathbb{Q} \\ \\
0  \quad \text{if }x \in \mathbb{I}
\end{cases},
$$


with $$f_{n}:[0,1]\to \mathbb{R}$$ and $$f : [0,1] \to \mathbb{R}$$.

### Theorem (Derivatives and uniform convergence)
Let $$f_{n}:[a,b]\to \mathbb{R}$$ be differentiable functions such that $$f_{n}' \underset{n \rightarrow \infty}{\longrightarrow} g$$ uniformly on $$[a,b]$$. Assume that there exists $$x_{0} \in [a,b]$$ such that $$f_{n}(x_{0})$$ converges.  Then $$f_{n}$$ converges uniformly to a function $$f:[a,b] \to \mathbb{R}$$ such that  $$f'(x) = g(x)$$ for every $$x \in [a,b]$$.

***Proof:*** Let $$n,m \in \mathbb{N}$$. Take $$h(x) = f_{n}(x)-f_{m}(x)$$. Then, by the mean value theorem, there exists $$y$$ between $$x$$ and $$x_{0}$$ such that 




$$
\begin{aligned}
\frac{h(x) - h(x_{0})}{x-x_{0}} &= h'(y) \implies h(x) = h(x_{0}) + h'(y)(x-x_{0}) \\
\implies f_{n}(x) - f_{m}(x) &= (f_{n}(x_{0})-f_{m}(x_{0})) + (x-x_{0})(f_{n}'(y)-f_{m}'(y))
\end{aligned}
$$


Since $$f_{n}' \underset{n \rightarrow \infty}{\longrightarrow} g$$, it is Cauchy, i.e., given $$\varepsilon>0$$, there exists $$N \in \mathbb{N}$$ such that for all $$n,m\geq N$$ and every $$x \in [a,b]$$, $$\lvert f_{n}'(x) - f_{m}'(x)\rvert < \frac{\varepsilon}{2(b-a)}$$. 
Moreover, since $$f_{n}(x_{0})$$ converges, it is Cauchy, so there exists $$M \in \mathbb{N}$$ such that if $$n,m\geq M$$, $$\lvert f_{n}(x_{0}) - f_{m}(x_{0}) \rvert < \frac{\varepsilon}{2}$$. Hence, if $$n,m\geq N$$ then, for every $$x \in [a,b]$$ 


$$
\begin{aligned}
\lvert f_{n}(x) - f_{m}(x) \rvert &\leq \lvert f_{n}(x_{0}) - f_{m}(x_{0})   \rvert + \lvert x-x_{0} \rvert \lvert f_{n}'(y) - f_{m}'(y) \rvert\\
&< \frac{\varepsilon}{2} + (b-a)\frac{\varepsilon}{2(b-a)} = \varepsilon.
\end{aligned}
$$


Therefore $$f_{n}$$ is uniformly Cauchy and converges. 
**CAREFUL:** If $$\{f_{n}(x)\}_{n=1}^\infty$$ is Cauchy, define $$\ell_{x} = \lim_{ n \to \infty } f_{n}(x)$$. Then $$f(x) = \ell_{x}$$.

We will now prove that $$f'(x) = g(x)$$.
We must show that 


$$
\lim_{ x \to y } \frac{f(x)-f(y)}{x-y} = g(y).
$$


Consider 


$$
\begin{aligned}
&\left\lvert  \frac{f(x)-f(y)}{x-y} - g(y)  \right\rvert \leq \left\lvert \frac{f(x)-f(y)}{x-y} -\frac{f_{N}(x)-f_{N}(y)}{x-y}  \right\rvert  + \left\lvert \frac{f_{N}(x)-f_{N}(y)}{x-y} - g(y) \right\rvert \\
&\leq  \left\lvert \frac{f(x)-f(y)}{x-y} -\frac{f_{N}(x)-f_{N}(y)}{x-y}  \right\rvert  + \left\lvert \frac{f_{N}(x)-f_{N}(y)}{x-y} - f_{N}'(y) \right\rvert + \lvert f_{N}'(y) - g(y) \rvert .
\end{aligned}
$$


Given $$\varepsilon>0$$, there exist $$N \in \mathbb{N}$$ and $$\delta>0$$ such that 
1. $$\lvert f_{n}'(x) - g(x) \rvert < \frac{\varepsilon}{3}$$ if $$n\geq N$$ and $$x \in [a,b]$$.
2. If $$\lvert x-y \rvert < \delta$$ then 


$$
\left\lvert \frac{f_{N}(x)-f_{N}(y)}{x-y} - f_{N}'(y) \right\rvert < \frac{\varepsilon}{3}.
$$


Now consider 


$$
\begin{aligned}
\frac{f_{m}(x)-f_{m}(y)}{x-y} - \frac{f_{N}(x)-f_{N}(y)}{x-y} &= \frac{(f_{m}(x) - f_{N}(x))- (f_{m}(y)-f_{N}(y))}{x-y} \\
&= f_{m}'(c)-f_{N}'(c)
\end{aligned}
$$


for some $$c$$ between $$x$$ and $$y$$ (which exists by the intermediate value theorem). Then 


$$
\lim_{ m \to \infty } \left\lvert  \frac{f_{m}(x)-f_{m}(y)}{x-y} - \frac{f_{N}(x)-f_{N}(y)}{x-y}\right\rvert = \left\lvert \frac{f(x)-f(y)}{x-y} - \frac{f_{N}(x)-f_{N}(y)}{x-y} \right\rvert < \frac{\varepsilon}{3}.
$$


Finally, we have that 


$$
\left\lvert  \frac{f(x)-f(y)}{x-y} - g(y)  \right\rvert < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.
$$


#### Example 
Let $$f_{n}:[-1,1] \to \mathbb{R}$$ be such that $$f_{n}(x) = \sqrt{ x^{2}+\frac{1}{n} }$$. Then $$f_{n}$$ is differentiable on $$(0,1)$$ and  $$f_{n}'(x) = \frac{x}{\sqrt{ x^{2}+\frac{1}{n} }}$$. Moreover $$\lim_{ n \to \infty } f_{n}(x) = \sqrt{ x^{2} } = \lvert x \rvert$$. We are going to prove that, given $$\varepsilon>0$$, there exists $$N \in \mathbb{N}$$ such that $$\left\lvert  \sqrt{ x^{2}+\frac{1}{n} } - \sqrt{ x^{2} } \right\rvert < \varepsilon$$ for every $$x \in [-1,1]$$. Given $$\varepsilon>0$$, we know that there exists $$N_{0} \in \mathbb{N}$$ such that $$\frac{1}{\sqrt{ N_{0}}} < \varepsilon$$. Note that, for $$n\geq N_{0}$$


$$
\sqrt{ x^{2}+\frac{1}{n} } - \sqrt{ x^{2} } = \frac{\frac{1}{n}}{\sqrt{ x^{2}+\frac{1}{n} } + \sqrt{ x^{2} }} \leq \frac{\frac{1}{n}}{\sqrt{ \frac{1}{n} }}  = \frac{1}{\sqrt{ n }} < \varepsilon
$$



#### Example 
 


$$
f_{n}(x) = \sum_{k=0}^{n} \frac{\cos(3^{k}x)}{2^{k}}
$$


 converges uniformly to a function that is nowhere differentiable.

### Lemma (Pointwise convergence of increasing functions)   
Let $$\{f_{n}(x)\}_{n=1}^\infty$$ be continuous with $$f_{n}(x) \leq f_{n+1}(x)$$ for every $$x \in [a,b]$$. Assume that there exists a continuous $$f:[a,b] \to \mathbb{R}$$ such that  $$\lim_{ n \to \infty }f_{n}(x) = f(x)$$ pointwise. Then $$f_{n} \underset{n \rightarrow \infty}{\longrightarrow} f$$ uniformly on $$[a,b]$$.

***Proof:*** We must show that $$M_{n} = \lVert f-f_{n} \rVert_{\infty} \underset{n \rightarrow \infty}{\longrightarrow} 0$$, where $$\lVert f - f_{n} \rVert_{\infty} = \sup \{ \lvert f(x) -f_{n}(x) \rvert: x \in A \}$$. Note that for every $$x \in A$$, 


$$
0 \leq f(x) - f_{n+1}(x) \leq  f(x)-f_{n}(x) \implies M_{n+1} \leq  M_{n}.
$$


Since $$f - f_{n}$$ is continuous, we know that there exists $$x_{n}$$ such that $$f(x_{n}) - f_{n}(x_{n}) = M_{n}$$. In particular, $$\{x_{n}\}_{n=1}^\infty \subseteq [a,b]$$. By Bolzano-Weierstrass, there exists a subsequence $$x_{n_{k}} \underset{n_{k} \rightarrow \infty}{\longrightarrow} x \in[a,b]$$. Moreover, note that $$f_{1}(x_{n_{k}}) \leq f_{{n_{k}}}(x_{n_{k}}) \leq f(x_{n_{k}})$$. Then, by BW, there exists a subsequence $$x_{n_{k_{\ell}}}$$ such that $$f_{n_{k_{\ell}}}(x_{n_{k_{\ell}}})$$ is convergent, ($$f_{n}(x_{n})$$). Without loss of generality I may assume that ...
{% endraw %}
