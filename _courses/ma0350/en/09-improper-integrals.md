---
layout: chapter
course: ma0350
chapter: 9
title: "Improper Integrals"
slug: 09-improper-integrals
toc:
  sidebar: right
lang: en
fecha: 2025-06-03
permalink: /notes/ma0350/09-improper-integrals/
---

{% raw %}
We know how to integrate functions over intervals $$[a,b]$$. See also: convergence tests (in analogy with series). One can define $$\int_{a}^{\infty}  f(x)\, dx$$. 
### Definition (Convergence of an improper integral)
Let $$f:[a,+\infty] \to \mathbb{R}$$ be Riemann integrable on $$[a,b]$$ for every $$b>a$$. We say that $$\int_{a}^{\infty} f(x) \, dx$$ converges if $$\lim_{ b \to \infty } \int_{a}^{b} f(x)  \, dx$$ exists. 

#### Example 
Consider $$\int_{1}^{\infty}  \, \frac{1}{x^{p}}dx$$ . Since 


$$
\int_{1}^{b} x^{-p} \, dx = \frac{x^{1-p}}{1-p} \biggr\rvert_{1}^{b } = \frac{b^{1-p}}{1-p} - \frac{1}{1-p}.
$$


Note that 


$$
-\frac{1}{1-p} \quad \text{if }p>1  
\lim_{ b \to \infty } \frac{b^{1-p}}{1-p} - \frac{1}{1-p} = \begin{cases}
-\frac{1}{1-p} \quad \text{if }p>1 \\
+\infty  \quad \text{if }p <1
\end{cases}
$$


Moreover, if $$p=1$$


$$
\int_{1}^{b} \frac{1}{x} \, dx = \ln b \to \infty.
$$



### Lemma (The function must tend to zero) 
Let $$f:[a,+\infty) \to \mathbb{R}$$. If $$\lim_{ x \to \infty } f(x) = L \neq 0$$, then $$\int_{a}^{\infty} f(x) \, dx$$ diverges.

***Proof:***  Assume that $$\lim_{ x \to \infty } = \ell \neq 0$$. We know that, given $$\varepsilon>0$$, there exists $$M>0$$ such that if $$x>M$$ then $$\lvert f(x)-L \rvert < \varepsilon$$. Hence, if $$x>M$$, we have that $$L - \varepsilon <f(x)<L+\varepsilon$$. 
If $$L >0$$, take $$\varepsilon>0$$ such that $$L - \varepsilon > 0$$. Then $$L - \varepsilon < f(x)$$ if $$x>M$$. Integrating, 


$$
\int_{M}^{b} (l - \varepsilon) \, dx = (b-M)(L-\varepsilon) \leq \int_{M}^{b} f(x) \, dx.
$$


Hence 


$$
\lim_{ b \to \infty } \int_{a}^{b} f(x) \, dx = \lim_{ b \to \infty } \left( \int_{a}^{M} f(x)  \, dx  + \int_{M}^{b} f(x) \, dx + (l-\varepsilon)(b-M)  \right) = +\infty,
$$


If $$\ell<0$$, the argument is analogous but towards $$-\infty$$.

Assume that $$\lim_{ b \to \infty } \int_{a}^{b} f(x) \, dx = I \in \mathbb{R}$$. Given $$\varepsilon>0$$ there exists $$M>0$$ such that if $$b>M$$, then 


$$
\left\lvert  \int_{a}^{b} f(x) \, dx -I  \right\rvert < \frac{\varepsilon}{2}.
$$


Take $$b_{2} > b_{1} > M$$. Now, 


$$
\begin{aligned}
\left\lvert  \int_{b_{1}}^{b_{2}} f(x)  \, dx   \right\rvert &=  \left\lvert  \int_{a}^{b_{2}} f(x) \, dx - \int_{a}^{b_{1}} f(x)  \, dx    \right\rvert \\
&\leq \left\lvert  \int_{a}^{b_{1}} f(x) \, dx - I \right\rvert  + \left\lvert  \int_{a}^{b_{2}} f(x) \, dx - I   \right\rvert  < \varepsilon.
\end{aligned} 
$$


We conclude that $$\lvert  \int_{a}^{b_{1}} f(x) \, dx  \rvert < \varepsilon$$.
### Lemma  (Reduction to sequences)
$$\int_{0}^{\infty}  f(x)\, dx$$ converges to $$L$$ if, given $$\{ x_{n} \}_{n=1}^{\infty} \subseteq [a,+\infty]$$ with $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$$, we have that 


$$
\lim_{ n \to \infty } \int_{a}^{x_{n}}f(x)  \, dx = F(x_{n})\text{ exists and converges to } L.
$$


### Lemma (Cauchy condition for improper integrals) 
If, given $$\varepsilon>0$$, there exists $$M>0$$ such that $$\left\lvert  \int_{c}^{d}  f(x)\, dx  \right\rvert < \varepsilon$$ whenever $$c,d > M$$, then $$\int_{0}^{\infty} f(x)  \, dx$$ converges.

***Proof:*** Let $$\{ x_{n} \}_{n=1}^{\infty} \subseteq [a,+\infty]$$ be such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$$. Take $$z_{n} = \int_{a}^{x_{n}}  f(x)\, dx$$. Let $$\varepsilon>0$$; then there exists $$M \in \mathbb{N}$$ such that $$\left\lvert  \int_{c}^{d}  f(x)\, dx  \right\rvert < \varepsilon$$ for all $$c>d\geq M$$. Now, if we take $$x_{n} < x_{m}$$, then


$$
\lvert z_{n}-z_{m} \rvert = \left\lvert   \int_{x_{n}}^{x_{m}} f(x) \, dx   \right\rvert < \varepsilon.
$$


Let $$N \in \mathbb{N}$$ be such that $$x_{k}\geq M$$ for every $$k\geq N$$, which we know exists because $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$$.
Hence, if $$n,m \geq N$$, $$\left\lvert  \int_{x_{n}}^{x_{m}} f(x) \, dx  \right\rvert < \varepsilon$$. Then $$z_{n}$$ is Cauchy and converges.
We will now prove that they all converge to the same limit. Let $$\{ y_{n} \}_{n=1}^{\infty} \subseteq [a, +\infty]$$ be such that $$y_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$$. We must show that 


$$
\int_{a}^{x_{n}} f(x) \, dx  - \int_{a}^{y_{n}}  f(x)  \, dx = \int_{\min\{ x_{n}, y_{n}\}}^{\max \{ x_{n},y_{n} \}} f(x)  \, dx   \underset{n \rightarrow \infty}{\longrightarrow} 0.
$$


Take $$N_{1}$$ such that $$x_{n}, y_{n} \geq M$$; then for $$n\geq N_{1}$$,


$$
\left\lvert  \int_{\min\{ x_{n},y_{n} \}}^{\max\{ x_{n},y_{n} \}} f(x)\, dx   \right\rvert < \varepsilon.
$$


 Conclude that any two sequences converge to the same value.

### Theorem (Absolute convergence)
If $$\int_{a}^{\infty} \lvert f(x) \rvert \, dx$$ converges, then $$\int_{a}^{\infty} f(x) \, dx$$ converges.

***Proof:*** $$\int_{0}^{\infty} f(x) \, dx$$ exists if and only if, given $$\varepsilon>0$$, there exists $$M>0$$ such that $$\left\lvert\int_{c}^{d} f(x) \, dx \right\rvert < \varepsilon$$ whenever $$c,d \geq M$$. Note that 


$$
\left\lvert  \int_{c}^{d} f(x) \, dx   \right\rvert < \int_{c}^{d} \lvert f(x) \rvert  \, dx.
$$


Hence, if $$\int_{c}^{\infty} \lvert f(x) \rvert \, dx$$ converges, then given $$\varepsilon>0$$ there exists $$M > 0$$ such that $$\int_{c}^{d} \lvert f(x) \rvert \, d < \varepsilon$$ whenever $$c,d \geq M$$. Therefore 


$$
\left\lvert  \int_{c}^{d} f(x) \, dx   \right\rvert \leq  \int_{c}^{d} \lvert f(x) \rvert  \, dx < \varepsilon.
$$


So $$\int_{a}^{\infty} f(x) \, dx$$ converges. 

### Theorem (Comparison)
If there exists $$c \in [a, \infty)$$ such that $$0 \leq f(x) \leq g(x)$$ for every $$x \geq c$$, then:
1. $$\int_{a}^{\infty} g(x) \, dx$$ converges if  $$\int_{a}^{\infty} f(x) \, dx$$ converges.
2. $$\int_{a}^{\infty} f(x) \, dx$$ diverges if  $$\int_{a}^{\infty} g(x) \, dx$$ diverges.

***Proof of (1):***  Assume that $$0 \leq f(x) \leq g(x)$$ for every $$x \geq c$$, with $$a < c$$.
Then 


$$
0\leq \int_{c}^{d} f(x) \, dx \leq \int_{c}^{d} g(x) \, dx. 
$$


Suppose $$\int_{a}^{\infty} g(x) \, dx$$ converges. Then there exists $$M\geq 0$$ such that for all $$\ell,q \geq M$$,


$$
0 < \int_{\ell}^{q} g(x) \, dx < \varepsilon
$$


Hence $$0<\int_{\ell}^{q} f(x) \, dx < \varepsilon$$ and therefore it is Cauchy and converges.
The proof of 2 is left as an exercise. One hint is to note that $$F(x) = \int_{a}^{u} f(u) \, du$$ is increasing if $$f(x)\geq_{0}$$.

### Theorem (Limit comparison)
Let $$f:[a,\infty) \to \mathbb{R}$$ and $$g:[a,+\infty] \to \mathbb{R}$$ be such that $$0\leq f(x)\leq g(x)$$ for $$x\geq c$$, where $$c>a$$.
1. If $$\lim_{ n \to \infty } \frac{f(x)}{g(x)} = \ell \neq 0$$, then $$\int_{a}^{\infty} f(x) \, dx$$ converges if and only if $$\int_{a}^{\infty} g(x)\, dx$$ converges.
2. If $$\lim_{ n \to \infty } \frac{f(x)}{g(x)} = \infty$$, we have that 
1. $$\int_{a}^{\infty} g(x) \, dx$$ converges if  $$\int_{a}^{\infty} f(x) \, dx$$ converges.
2. $$\int_{a}^{\infty} f(x) \, dx$$ diverges if  $$\int_{a}^{\infty} g(x) \, dx$$ diverges.

***Proof:*** Assume that $$\lim_{ n \to \infty } \frac{f(x)}{g(x)} = \ell \neq 0$$. Given $$\varepsilon>0$$, there exists $$M>0$$ such that for every $$x \geq M$$, 


$$
\ell - \varepsilon < \frac{f(x)}{g(x)} < \ell + \varepsilon.
$$


Hence, if we take $$\varepsilon < \ell$$, then 


$$
0 \leq  (l-\varepsilon) g(x) \leq  f(x) \leq (l+\varepsilon) g(x).
$$


The result follows from the comparison theorem. 
On the other hand, if $$\lim_{ n \to \infty } \frac{f(x)}{g(x)} = +\infty$$: given $$M>0$$, there exists $$N>0$$ such that $$\frac{f(x)}{g(x)} \geq M$$ if $$x>N$$. Then $$f(x) \geq Mg(x)$$ if $$x\geq N$$.

For integrals of the other kinds, compute the limit towards the problematic point.
#### Example 
Let $$\Gamma(\alpha) = \int_{0}^{\infty} e^{-x} x^{\alpha-1} \, dx$$ for $$\alpha \geq 1$$. Note that 


$$
\lim_{ x \to \infty } \frac{e^{-x}x^{\alpha-1}}{e^{-x/2}} = \lim_{ x \to \infty } e^{-x/2} x^{\alpha-1} = 0.
$$


Since 


$$
\int_{0}^{a} e^{x/2} \, dx = -\frac{1}{2} e^{-x/2} \biggr\rvert_{a}^{0} = \frac{1}{2} - \frac{1}{2} e^{-a/2} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{2},
$$


that is, $$\int_{0}^{\infty} e^{-x/2} \, dx$$ converges, we conclude by limit comparison that $$\int_{0}^{\infty} e^{-x} x^{\alpha-1} \, dx$$ converges.

### Exercise 
Show that $$\Gamma(1) = 1$$ and that $$\Gamma(\alpha) = \alpha\Gamma(\alpha-1)$$ for $$\alpha \geq 2$$.

### Theorem (Dirichlet)
Let $$f:[a,+\infty) \to \mathbb{R}$$ and $$g:[a, +\infty) \to \mathbb{R}$$ be functions such that 
1. There exists $$M>0$$ such that $$\int_{a}^{b} f(x) \, dx \leq M$$ for all $$a<b \in \mathbb{R}$$.
2. $$g$$ is decreasing and $$\lim_{ x \to \infty } g(x) = 0$$.
Then $$\int_{a}^{\infty} f(x)g(x) \, dx$$ converges.

***Proof:*** Given $$\varepsilon>0$$, there exists $$K$$ such that $$0\leq g(x) < \frac{\varepsilon}{M}$$ for $$x\geq K$$. Moreover, given $$c,d\geq K$$, there exists $$c_{1} \in \mathbb{R}$$ such that 


$$
\int_{c}^{d} f(x)g(c) \, dx = g(c) \int_{c}^{c_{1}} f(x) \, dx,
$$


where $$c\leq c_{1} \leq d$$. Then, for all $$d\geq c\geq k$$


$$
\left\lvert  \int_{c}^{d} f(x)g(x) \, dx   \right\rvert =  g(c) \left\lvert  \int_{c}^{d} f(x) \, dx   \right\rvert < \frac{\varepsilon}{M} \cdot M = \varepsilon,
$$


and therefore the integral converges.

#### Example 
Consider $$\int_{0}^{\infty} \frac{\sin x}{x^{p}}\, dx$$ for $$p>0$$. Note that $$\lim_{ n \to \infty } \frac{1}{x^{p}} = 0$$ and $$\frac{1}{x^{p}}$$ is decreasing. Moreover, 


$$
\left\lvert  \int_{a}^{b} \sin x \, dx   \right\rvert = \left\lvert -\cos x \biggr\rvert_{a}^{b }  \right\rvert = \lvert \cos b-\cos a \rvert \leq 2.
$$


Therefore it converges.

#### Example 
Recall that $$\int_{1}^{\infty} \frac{\sin x}{x} \, dx$$ converges by Dirichlet's test. What happens with $$\int_{\pi}^{\infty} \left\lvert  \frac{\sin x}{x}  \right\rvert  \, dx$$?
Consider 


$$
\int_{\pi}^{k \pi} \left\lvert  \frac{\sin x}{x}  \right\rvert \, dx = \sum_{j=1}^{k-1} \int_{j \pi}^{(j+1)\pi}  \left\lvert  \frac{\sin x}{x}
\right\rvert  \, dx. 
$$


Now, 


$$
\begin{aligned}
\frac{2}{\pi(j+1)} =\frac{1}{(j+1)\pi} \int_{j \pi}^{(j+1) \pi} \left\lvert  \sin x \right\rvert  \, dx &\leq  \int_{j \pi}^{(j+1)\pi} \left\lvert  \frac{\sin x}{x}  \right\rvert  \, dx \\
&\leq \frac{1}{j\pi} \int_{j \pi}^{(j+1) \pi} \left\lvert \sin x \right\rvert  \, dx = \frac{2}{j \pi}.
\end{aligned}
$$


Then 


$$
\sum_{j=1}^{k-1} \frac{2}{\pi} \frac{1}{j+1} \leq  \int_{\pi}^{k \pi} \frac{1}{(j+1)\pi} \int_{j \pi}^{(j+1) \pi} \left\lvert  \frac{\sin x}{x}  \right\rvert  \, dx \leq  \sum_{j=1}^{k-1} \frac{2}{\pi} \frac{1}{j}.
$$


Since $$\sum_{k=1}^\infty \frac{1}{n} = +\infty$$, we get $$\lim_{ k \to \infty } \int_{0}^{k \pi} \left\lvert  \frac{\sin x}{x}  \right\rvert \, dx = \infty$$.

### Lemma (Abel's test)
Let $$f:[a,+\infty) \to \mathbb{R}$$ be such that 
1. $$\int_{a}^{\infty} f(x) \, dx$$ converges. 

Assume moreover that $$g:[a,+\infty) \to \mathbb{R}$$ 
2. is monotone,
3. $$\lim_{ x \to \infty } g(x) = \ell$$. 

Then $$\int_{0}^{\infty} f(x)g(x) \, dx$$ converges.


***Proof:*** Let $$\varepsilon>0$$. Let $$c,d \geq M$$. Then there exists $$c_{1} \in [c,d]$$ such that


$$
\int_{c}^{d} f(x)g(x) \, dx = g(c) \int_{c}^{c_{1}} f(x) \, dx + g(d) \int_{c_{1}}^{d} f(x)  \, dx,
$$


where $$M$$ is such that $$\ell-\varepsilon <  g(x) < \ell+\varepsilon$$ if $$x\geq M$$. Then there exists $$K$$ such that $$\lvert g(x) \rvert \leq K$$ for $$x \geq M$$. Let $$M_{1}$$ be such that 


$$
\left\lvert  \int_{p}^{q} f(x) \, dx   \right\rvert < \frac{\varepsilon}{2K}
$$


for $$p,q \geq M_{1}\geq M$$. Then 


$$
\left\lvert  \int_{c}^{d} f(x)g(x) \, dx   \right\rvert \leq  \lvert g(c) \rvert \left\lvert  \int_{c}^{c_{1}} f(x) \, dx   \right\rvert + \lvert g(d) \rvert \left\lvert  \int_{c_{1}}^{d} f(x) \, dx   \right\rvert \leq  K \frac{\varepsilon}{2K} + K \frac{\varepsilon}{2K} = \varepsilon.
$$


Conclude that it is Cauchy and therefore converges.

#### Example 
For $$\int_{1}^{\infty} \frac{\sin x \arctan x}{x} \, dx$$, take $$g(x) = \arctan x$$ and $$f(x)=\frac{\sin x}{x}$$. Since $$g(x)$$ is monotone, $$\lim_{ x \to \infty } \arctan x = \frac{\pi}{2}$$ and $$\int_{1}^{\infty} \frac{\sin x}{x} \, dx$$ converges, the given integral converges.

## Other types of improper integrals

### From -$$\infty$$ to $$b$$
Let $$f:(-\infty,b] \to \mathbb{R}$$ be such that $$f:[a,b] \to \mathbb{R}$$ is Riemann integrable for every $$a<b$$. If $$\lim_{ a \to -\infty } \int_{a}^{b} f(x) \, dx$$ exists, we say that $$\int_{-\infty}^{b} f(x) \, dx$$ converges $$\int_{0}^{1}  \, dx$$

Note that $$\int_{a}^{b} f(x)  \, dx = \int_{-b}^{-a}  f(u)  \, du$$, so $$\int_{-\infty}^{b}f(x)  \, dx$$ converges if and only if $$\int_{-b}^{\infty}  f(-x) \, dx$$ converges.

### From $$-\infty$$ to $$+\infty$$
Let $$f:(-\infty,+\infty) \to \mathbb{R}$$. Then $$\int_{-\infty}^{+\infty} f(x) \, dx$$ converges if and only if $$\int_{0}^{+\infty}  f(x)\, dx$$ and $$\int_{-\infty}^{0} f(x) \, dx$$ converge. 

#### Example 
Consider the following improper integral: $$\int_{-\infty}^{+\infty} x^{2}e^{-\lvert x \rvert} \, dx$$.
Note that 


$$
\int_{0}^{+\infty} x^{2}e^{-\lvert x \rvert }  \, dx = \int_{0}^{+\infty}  x^{2}e^{-x}\, dx.
$$


On the other hand, 


$$
\int_{-\infty}^{0} x^{2} e^{-\lvert x \rvert }  \, dx = \int_{-\infty}^{0} x^{2} e^{x}  \, dx = \int_{+\infty}^{0} (-u)^{2}e^{-u} - \, du = \int_{0}^{+\infty} (-u)^{2} e^{-u}  \, du.  
$$


Now,  


$$
\lim_{ x \to \infty } \frac{ x^{2}e^{-x}}{e^{-x/2}} = 0.
$$


Since $$\int_{0}^{+\infty} e^{-x/2} \, dx = -\frac{1}{2} e^{-x/2} \biggr\rvert_{0}^{+\infty } = \frac{1}{2}$$, we have that $$\int_{0}^{\infty} x^{2} e^{-x} \, dx$$ converges.

#### Example 
Consider $$\int_{\alpha}^{1} \frac{1}{x^{p}} \, dx$$ with $$\alpha>0$$. This function is not Riemann integrable on $$[0,1]$$ if $$p>0$$, but does $$\lim_{ \alpha \to 0^{+} } \int_{\alpha}^{1} \frac{1}{x^{p}} \, dx$$ exist?

Note that 


$$
\int_{\alpha}^{1} \frac{1}{x^{p}} \, dx = \begin{cases}
\frac{1}{1-p} x^{1-p} \biggr\rvert_{\alpha}^{1} \quad\text{if } p\neq 1, \\
\ln x \biggr\rvert_{\alpha}^{1} = \ln(1) - \ln(\alpha) \quad \text{if }p=1. 
\end{cases}
$$


Then


$$
 \lim_{ \alpha \to 0^{+} } \int_{\alpha}^{1} \frac{1}{x^{p}} \, dx = \begin{cases}
\frac{1}{1-p} \quad\text{if } 0<p<1, \\
+\infty \quad \text{otherwise}. 
\end{cases}
$$


Making the change of variable $$x = \frac{1}{u} \implies dx = -\frac{du}{u^{2}}$$, we have that 


$$
\int_{\alpha}^{1} \frac{1}{x^{p}} \, dx = \int_{1}^{1/\alpha}  \frac{1}{\left( \frac{1}{u} \right)^{p}}\, \frac{du}{u^{2}} = \int_{1}^{1/\alpha} \frac{1}{u^{2-p}}  \, du .  
$$


So $$\int_{\alpha}^{1} \frac{1}{x^{p}}  \, dx$$ converges if and only if $$\int_{1}^{+\infty} \frac{1}{u^{2-p}} \, dx$$ converges.
{% endraw %}
