---
layout: chapter
course: ma0350
chapter: 6
title: "The Riemann Integral"
slug: 06-the-riemann-integral
toc:
  sidebar: right
lang: en
fecha: 5/6/25
permalink: /notes/ma0350/06-the-riemann-integral/
---

{% raw %}
### Theorem (Uniqueness of the Riemann integral)
***Proof:***  Assume that $$I_{1}$$ and $$I_{2}$$ both satisfy the definition. Given $$\varepsilon>0$$ there exist $$P_{\varepsilon_{1}}$$ and $$P_{\varepsilon_{2}}$$ such that 


$$
\lvert S(f, P_{1}, \xi_{1},\dots, \xi_{n}) - I_{1} \rvert < \varepsilon  \quad \text{(1)}
$$


for every $$P_{1} \supseteq P_{\varepsilon_{1}}$$, $$a_{i} \leq \xi_{i} \leq a_{i+1}$$ and


$$
\lvert S(f, P_{2}, \eta_{1},\dots,\eta_{m}) - I_{2} \rvert < \varepsilon  \quad \text{(2)}
$$


for every $$P_{2} \supseteq P_{\varepsilon_{2}}$$, $$b_{i} \leq \eta_{i} \leq b_{i+1}$$. Take $$P = P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$$. Then $$P \supseteq P_{\varepsilon_{1}}$$ and $$P \supseteq P_{\varepsilon_{2}}$$. Hence, combining (1) and (2), we have that $$\lvert I_{1} - I_{2}\rvert < 2\varepsilon$$. Since this holds for every $$\varepsilon>0$$, conclude that $$I_{1} = I_{2}$$.

### Theorem (Additivity of the integral)
Let $$f:[a,b] \to \mathbb{R}$$ be bounded and let $$a<c<b$$. Assume that $$f$$ is Riemann integrable on $$[a,c]$$ and on $$[c,b]$$. Then it is Riemann integrable on $$[a,b]$$. Moreover $$\int_{a}^{b} f(x)\, dx = \int_{a}^{c} f(x)  \, dx + \int_{c}^{b} f(x) \, dx.$$

***Proof:*** Given $$\varepsilon>0$$, we know that there exist $$I_{1}$$ and $$I_{2}$$, $$P_{\varepsilon_{1}}$$ and $$P_{\varepsilon_{2}}$$ satisfying:
1. $$P_{\varepsilon_{1}} = \{ a_{0}=a < a_{1}<...<a_{n} = c \}$$ is a partition of $$[a,c]$$.
2. $$P_{\varepsilon_{2}} = \{ d_{0}=c < d_{1}<...<d_{n} = b \}$$ is a partition of $$[c,b]$$.
Moreover, if $$P_{1}$$ is a partition of $$[a,c]$$ such that $$P_{1} \supseteq P_{\varepsilon_{1}}$$, then


$$
\lvert S(f, P_{1}, \xi_{1},\dots, \xi_{n}) - I_{1} \rvert < \frac{\varepsilon}{2}  \quad \text{(1)}.
$$


Similarly, if $$P_{2}$$ is a partition of $$[c,b]$$ such that $$P_{2} \supseteq P_{\varepsilon_{2}}$$.


$$
\lvert S(f, P_{2}, \eta_{1},\dots,\eta_{m}) - I_{2} \rvert < \frac{\varepsilon}{2}  \quad \text{(2)}.
$$


We are going to prove that $$I_{1} + I_{2}$$ is the integral on $$[a,b]$$. Take $$P_{\varepsilon}=P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$$. Let $$P = \{ h_{0} = a<h_{1},\dots,h_{\ell}=b\}$$ be such that $$P \supseteq P_{\varepsilon}$$. Since $$c \in P_{\varepsilon}$$, there is an $$h_{k} = c$$ such that $$\{ h_{0}=a < h_{1} <...<h_{k} = c \}$$ is a partition of $$[a,c]$$ finer than $$P_{\varepsilon_{1}}$$ and $$\{ h_{k}=c < h_{k+1} <...<h_{\ell} = b\}$$ is a partition of $$[c,b]$$ finer than $$P_{\varepsilon_{2}}$$. Consider the Riemann sum 


$$
\sum_{i=1}^{\ell-1} f(\xi_{i})(h_{i+1}-h_{i}) = \sum_{i=1}^{k-1}  f(\xi_{i}) (h_{i+1}-h_{i})U + \sum_{i=k}^{\ell-1}  f(\xi_{i})(h_{i+1}-h_{i})
$$


Finally, applying (1) and (2) together with the triangle inequality:


$$
\lvert S(f,P, \xi_{1},\dots,\xi_{\ell}) - I_{1}-I_{2}\rvert < \varepsilon.
$$



Let $$\varepsilon>0$$ and let $$f:[a,b] \to \mathbb{R}$$ be such that there exist $$I_{1}$$ and $$P_{\varepsilon_{1}}$$ with the property that if $$P \supseteq P_{\varepsilon_{1}}$$ then 


$$
\lvert S(f,P, \xi_{1},\dots,\xi_{n}) - I_{1} \rvert < \frac{\varepsilon}{2}
$$


where $$S(f, P, \xi_{1},\dots \xi_{n}) = \sum_{i=0}^{n-1} f(\xi_{i})(a_{i+1}-a_{i})$$. Take $$g:[a,b] \to \mathbb{R}$$ Riemann integrable. There exist $$I_{1}$$ and $$P_{\varepsilon_{2}}$$ such that if $$P' \supseteq P_{\varepsilon_{2}}$$,



$$
\lvert S(g,P', \eta_{1},\dots,\eta_{m}) - I_{1} \rvert < \frac{\varepsilon}{2\lvert c \rvert}
$$


If $$\tilde{P} \supseteq P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$$. We conclude that $$\tilde{P} \supseteq P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$$ implies 


$$
\lvert f+cg, \tilde{P}, \alpha_{1},\dots,\alpha_{\ell} \rvert < \frac{\varepsilon}{2} + \lvert c \rvert \frac{\varepsilon}{2\lvert c \rvert } = \varepsilon.
$$



### Lemma (Upper and lower sums across partitions) 
Let $$P_{1}$$ and $$P_{2}$$ be two partitions of $$[a,b]$$ such that $$P_{1} \subseteq P_{2}$$. Then 


$$
\begin{aligned}
U(f,P_{2}) \leq& U(f, P_{1}) \\
L(f,P_{1}) \leq& L(f, P_{2})
\end{aligned}
$$


***Proof:***  Let $$P = \{ a_{0}=a<a_{1}<...<a_{n}=b \}$$ and let 


$$
\begin{aligned}
\mathrm{U}(f, P) &= \sum_{i=0}^{n-1} M_{i}(a_{i+1}-a_{i}),\\
\mathrm{L}(f,P) &= \sum_{i=0}^{n-1} m_{i}(a_{i+1}-a_{i}),
\end{aligned}
$$


with $$M_{i} = \sup \{ f(x):a_{i}\leq x\leq a_{i+1} \}$$ and $$m_{i} = \inf \{ a_{i} \leq x \leq a_{i+1} \}$$. Let $$\alpha \in [a,b]$$ be such that $$\alpha \not\in P$$. Note that there exists $$i \in {0,\dots,n-1}$$ such that  $$a_{i} < \alpha <a_{i+1}$$. Let $$P_{1} = P \cup \{ \alpha \}$$. Take 


$$
\begin{aligned}
M_{i} &= \sup \{ f(x):a_{i}\leq x,=a_{i+1} \} \\
M_{i}' &= \sup \{ f(x): a_{i} \leq  x \leq  \alpha \} \\
M_{i}'' &= \sup \{ f(x): \alpha \leq x \leq a_{i+1}  \}.
\end{aligned}
$$


Note that $$M_{i}' \leq M_{i}$$ and $$M_{i}''\leq M_{i}$$. Hence: 


$$
M_{i}(a_{i+1}-a_{i}) = M_{i}(a_{i+1}-\alpha) + M_{i}(\alpha-a_{i} \geq M_{i}''(a_{i+1}-\alpha) + M_{i}'(\alpha-a_{i}).
$$


Then $$\mathrm{U}(f,P) \geq U(f,P_{1})$$, since they agree in every term except the ones described above. The proof for the lower sum is left as an exercise.

### Theorem (UL characterisation of the Riemann integral) 
Let $$f:[a,b]$$ be bounded. Then $$f$$ is Riemann integrable if and only if for every $$\varepsilon>0$$ there exists a partition $$P_{\varepsilon}$$ such that for every partition $$P \supseteq P_{\varepsilon}$$ 


$$
\lvert U(f,P) - L(f,P) \rvert < \varepsilon.
$$


***Proof:*** ($$\implies$$): Given $$\varepsilon>0$$, there exist $$I$$ and $$P_{\varepsilon}$$ such that for every $$P \supseteq P_{\varepsilon}$$


$$
\lvert S(f,P,\xi_{1},\dots, \xi_{n}) - I \rvert < \varepsilon.
$$


Take $$P \supseteq P_{\varepsilon}$$. Then $$P = \{ a_{0} = a < a_{1}< \dots < a_{n} = b \}$$. Consider $$M_{i} = \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \}$$. Since it is the supremum, there exists $$\xi_{i} \in [a_{i},a_{i+1}]$$ such that 


$$
M_{i} - \frac{\varepsilon}{b-a} <  f(\xi_{i}) \leq  M_{i}.
$$


Note that 


$$
\sum_{i=0}^{n-1} f(\xi_{i})(a_{i+1}-a_{i}) \leq  \sum_{i=0}^{n-1} M_{i}(a_{i+1}-a_{i}).
$$


Moreover, 


$$
\begin{aligned}
S(f, P, \xi_{1},\dots,\xi_{n}) &= \sum_{i=0}^{n-1} f(\xi_{i})(a_{i+1}-a_{i}) \\&> \sum_{i=0}^{n-1} \left( M_{i} - \frac{\varepsilon}{b-a} \right) (a_{i+1}-a_{i}) \\
&= \sum_{i=0}^{n-1}  M_{i}(a_{i+1}-a_{i}) - \frac{\varepsilon}{b-a}\underbrace{ \sum_{i=0}^{n-1} a_{i+1}-a_{i} }_{ = b-a } \\
&= \mathrm{U}(f, P) - \varepsilon.
\end{aligned}
$$


Therefore $$\mathrm{U}(f,P) - S(f, P, \xi_{1},\dots,\xi_{n}) < \varepsilon$$.
Now consider $$m_{i} = \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \}$$. Since it is the infimum, there exists $$\eta_{i} \in [a_{i},a_{i+1}]$$ such that 


$$
m_{i} + \frac{\varepsilon}{b-a} >  f(\eta_{i}) \geq   m_{i}.
$$


Note that 


$$
\sum_{i=0}^{n-1} f(\eta_{i})(a_{i+1}-a_{i}) \geq   \sum_{i=0}^{n-1} m_{i}(a_{i+1}-a_{i}).
$$


Moreover, 


$$
\begin{aligned}
S(f, P, \eta_{1},\dots,\eta_{n}) &= \sum_{i=0}^{n-1} f(\eta_{i})(a_{i+1}-a_{i}) \\&< \sum_{i=0}^{n-1} \left( m_{i} + \frac{\varepsilon}{b-a} \right) (a_{i+1}-a_{i}) \\
&= \sum_{i=0}^{n-1}  m_{i}(a_{i+1}-a_{i}) + \frac{\varepsilon}{b-a}\underbrace{ \sum_{i=0}^{n-1} a_{i+1}-a_{i} }_{ = b-a } \\
&= \mathrm{L}(f, P) + \varepsilon.
\end{aligned}
$$


Therefore $$S(f, P, \eta_{1},\dots,\eta_{n}) - \mathrm{L}(f,P)  < \varepsilon$$. Then 


$$
\begin{aligned}
&\lvert \mathrm{U}(f, P) - \mathrm{L}(f,P) \rvert \leq  \lvert \mathrm{U}(f,P) - S(f,P, \xi_{1},\dots,\xi_{n}) \rvert + \lvert S(f,P, \xi_{1},\dots,\xi_{n}) - \mathrm{L}(f,P) \rvert \\
&\leq \varepsilon + \lvert S(f,P, \xi_{1},\dots,\xi_{n}) - S(f,P, \eta_{1},\dots,\eta_{n}) \rvert + \underbrace{ \lvert S(f,P, \eta_{1},\dots,\eta_{n}) - \mathrm{L}(f,P)\rvert.   }_{ < \varepsilon } 
\end{aligned}
$$


Finally, 


$$
\begin{aligned}
&\lvert S(f,P, \xi_{1},\dots,\xi_{n}) - S(f,P, \eta_{1},\dots,\eta_{n}) \rvert\\
\leq &\lvert S(f,P, \xi_{1},\dots,\xi_{n}) - I) \rvert + \lvert I - S(f,P, \eta_{1},\dots,\eta_{n}) \rvert < 2\varepsilon
\end{aligned}
$$



#### Example
Consider $$f:[0,1] \to \mathbb{R}$$ such that 


$$
f(x) = \begin{cases}
a, x \in \mathbb{Q}\\ \\
0, x \not\in \mathbb{Q}
\end{cases}
$$


for $$a >0$$. Let $$P$$ be a partition $$\{ a_{0} = 0 < a_{1}<a_{2}<...<a_{n}=1 \}$$. Then 


$$
\begin{aligned}
M_{i} &= \sup \{ f(x):a_{i}\leq x\leq a_{i+1} \}  = a \\
m_{i} &= \inf \{ f(x): a_{i} \leq  x a_{i+1} \} = 0.
\end{aligned}
$$


Hence $$U(f, P) = \sum_{i=0}^{n-1} a (a_{i+1}-a_{i}) = a$$ and $$L(f,p) = \sum_{i=1}^{n-1} 0(a_{i+1}-a_{i})=0$$. 

Therefore $$U(f,P) - L(f,P) = a$$, i.e., it cannot be made arbitrarily small. 

### A trick for building increasing partitions
We prove the UL characterisation using a trick that lets us build successively finer partitions.

***Proof:*** ($$\impliedby$$): Let $$\varepsilon>0$$ and $$n \in \mathbb{N}$$. Then there exists a partition $$P_{n}$$ such that 


$$
\lvert U(f,P_{n}) - L(f, P_{n}) \rvert < \frac{\varepsilon}{n}.
$$


Let $$P_{1}' = P_{1}$$ and define $$P_{m}' = \bigcup_{i=1}^{m} P_{i}$$. Then $$P_{n}' \subseteq P_{n+1}'$$ and $$P_{n} \subseteq P_{n}'$$. We know that 


$$
\begin{aligned}
U(f, P_{n}') &\geq U(f, P_{n+1}') \\
L(f, P_{n+1}') &\geq L(f,P_{n}')
\end{aligned}
$$


and that the sequences are bounded. Then 


$$
\begin{aligned}
\lim_{ n \to \infty } U(f, P_{n}')  &= L_{1} \\
\lim_{ n \to \infty } L(f, P_{n}') &= L_{2}.
\end{aligned}
$$


Moreover, note that 


$$
\begin{aligned}
L_{1} &\leq  U(f, P_{n}') \\
L_{2} &\geq L(f, P_{n}') \\
\implies 0 \leq  L_{1} - L_{2} &\leq U(f,P_{n}') - L(f,P_{n}') < \frac{\varepsilon}{n}.
\end{aligned}
$$


Since this holds for every $$\varepsilon>0$$, we conclude that $$L_{1} = L_{2} = I$$.

($$\implies$$): Let $$P$$ be a partition such that $$P_{N}' \subseteq P$$. Then 


$$
S(f, P, \xi_{1},\dots,\xi_{n}) - I \leq  U(f, P) - L_{1} \leq  U(f, P_{N}') - L_{1} < \varepsilon,
$$


where $$N$$ is such that, for $$n\geq N$$


$$
\begin{aligned}
0 &< U(f, P_{n}) - L_{1} < \varepsilon \\
0 &< L_{2} - L(f, P_{n}) < \varepsilon,
\end{aligned}
$$


Hence $$S(f, P, \xi_{1}, \dots, \xi_{n}) - I< \varepsilon$$. On the other hand,  


$$
S(f, P, \xi_{1}, \dots, \xi_{n}) - I \geq L(f,P) - L_{2} > -\varepsilon.
$$


We conclude that if $$P_{N}' \subseteq P$$, then 


$$
\lvert S(f,P,\xi_{1},\dots,\xi_{n}) - I \rvert <\varepsilon
$$


> Tips for working with U and L:
> 1. Build the sequence of partitions.
> 2. Consider finer partitions.
> 3. Bound above with $$U$$ and below with $$L$$.

### Lemma (Increasing implies R-integrable)
Let $$f:[a,b] \to \mathbb{R}$$ be increasing. Then $$f$$ is Riemann integrable

 ***Proof:*** Let $$f:[a,b] \to \mathbb{R}$$ be increasing. Take 


$$
P = \{ a_{0}=a<a_{1}<a_{2}< \dots < a_{n} = b \}.
$$


Then 


$$
U(f,P) = \sum_{i=0}^{n} M_{i}(a_{i+1}-a_{i}),
$$


with $$M_{i} = \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \} = f(a_{i+1})$$. 
In the same way, $$m_{i} = \inf \{ f(x): a_{i} \leq x \leq a_{i+1} \} = f(a_{i})$$. Now, 


$$
\begin{aligned}
U(f,P) - L(f,P) &= \sum_{i=0}^{n-1} (M_{i} - m_{i})(a_{i+1}-a_{i}) \\
&= \sum_{i=0}^{n-1}(f(a_{i+1})-f(a_{i}))(a_{i+1}-a_{i}). 
\end{aligned}
$$


Let $$P_{\varepsilon}$$ be a partition such that $$0<(a_{i+1}-a_{i})< \frac{\varepsilon}{f(b)-f(a)}$$. Then 


$$
\begin{aligned}
U(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) &= \sum_{i=0}^{n-1} (f(a_{i+1})-f(a_{i}))(a_{i+1}-a_{i}) \\
&< \sum_{i=0}^{n-1} \frac{\varepsilon}{f(b)-f(a)} (f(a_{i+1})-f(a_{i})) \\
&= \varepsilon,
\end{aligned}
$$


So $$0 < U(f,P) - L(f,P) < \varepsilon$$. Finally, if $$P \supseteq P_{\varepsilon}$$, then 


$$
\begin{aligned}
U(f,P_{\varepsilon}) &\geq U(f,P) \\
L(f, P) &\geq L(f, P_{\varepsilon})
\end{aligned} \\
\implies 0 <U(f,P) - L(f,P) \leq u(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) < \varepsilon
$$



### Theorem (Continuity implies R-integrability)
Let $$f:[a,b] \to \mathbb{R}$$ be continuous. Then it is Riemann integrable.

***Proof:***  Let $$f:[a,b]\to \mathbb{R}$$ be bounded. Then, if $$M_{i} = \sup \{ f(x) : a_{i}\leq x\leq a_{i+1} \}$$, and $$m_{i} = \inf \{ f(x):a_{i}\leq x<a_{i+1} \}$$.


$$
\begin{aligned}
U(f,P) &= \sum_{i=0}^{n-1} M_{i}(a_{i+1}-a_{i}) \\
L(f,P) &= \sum_{i=0}^{n-1} m_{i}(a_{i+1}-a_{i}) \\
U(f,P)-L(f,P) &= \sum_{i=0}^{n-1} (M_{i}-m_{i})(a_{i+1}-a_{i}).
\end{aligned}S
$$


If $$f$$ is continuous, then there exist $$\xi_{i} ,\eta_{i} \in [a_{i},a_{i+1}]$$ such that $$f(\xi_{i}) = M_{i}$$ and $$f(\eta_{i}) = m_{i}$$. Moreover, since $$f$$ is continuous on a closed interval, it is uniformly continuous, i.e., for every $$\varepsilon>0$$ there exists $$\delta >0$$ such that for all $$x,y \in [a,b]$$, if $$\lvert x-y \rvert < \delta$$ then $$\lvert f(x) - f(y) \rvert < \varepsilon$$. Take $$P_{\varepsilon}$$ such that $$\lvert a_{i+1}-a_{i} \rvert < \delta$$; then $$\lvert \xi_{i} - \eta_{i} \rvert < \delta$$ and consequently $$\lvert f(\xi_{i}) - f(\eta_{i}) \rvert < \varepsilon$$. Hence 


$$
U(f,P) - L(f,P) < \sum_{i=0}^{n-1} \varepsilon(a_{i+1}-a_{i}) = \varepsilon(b-a). 
$$



#### Example 
Show that $$f:[0,1] \to \mathbb{R}$$ given by 


$$
f(x) \begin{cases}
=a \text{ if } x \in \mathbb{Q} \\
=0 \text{ if } x \not\in \mathbb{Q}
\end{cases}.
$$


is not R-integrable. 

***Proof:*** Consider a partition $$P = \{ a_{0} = a < a_{1} < \dots < a_{n} = b \}$$. Note that $$M_{i} = a$$ and  $$m_{i} = 0$$ for every $$i \in \{ 0,1,\dots,n-1 \}$$. Hence $$U(f,P) - L(f,P) = a$$.

### Definition (Mesh of a partition). 
Let $$P = \{ a_{0} = a < a_{1} < \dots <a_{n} = b \}$$ be a partition of $$[a,b]$$. Define the mesh of the partition as 


$$
\lVert P \rVert = \max \{ \lvert a_{i+1}-a_{i} \rvert: 0\leq i\leq N-1  \}.
$$


### Theorem (Mesh and continuity)
Let $$f:[a,b] \to \mathbb{R}$$ be bounded. Assume that for every $$\varepsilon>0$$ there exists $$\delta$$ such that if $$\lVert P \rVert < \delta$$ then $$\lvert U(f,P) - L(f,P) \rvert < \varepsilon$$. Then $$f$$ is Riemann integrable.

***Proof:*** Given $$\varepsilon>0$$, there exists $$\delta > 0$$ such that if $$\lVert P \rVert < \delta$$ then $$\lvert U(f,P) -  L(f,P) \rvert < \varepsilon$$. Let $$P_{\varepsilon}$$ be such that $$\lVert P_{\varepsilon} \rVert < \delta$$. Take $$P \supseteq P_{\varepsilon}$$. Then 


$$
\begin{aligned}
U(f,P) <& U(f, P_{\varepsilon}),\\
L(f,P_{\varepsilon}) <& L(f,P).
\end{aligned}
$$


Then 


$$
0 < U(f,P) - L(f,P) < u(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) < \varepsilon.
$$



### Theorem (Riemann integrability and composition) 
Let $$f:[a,b] \to \mathbb{R}$$ be Riemann integrable with $$f([a,b]) \subseteq [c,d]$$. If $$g:[c,d] \to \mathbb{R}$$ is continuous, then $$g \circ f: [a,b] \to \mathbb{R}$$ is Riemann integrable. 

***Proof:*** Let $$\varepsilon, \varepsilon_{1} > 0$$. We know that there exists $$\delta>0$$ such that if $$\lvert x-y \rvert$$ then $$\lvert g(x) - g(y) \rvert < \varepsilon$$. Moreover there exists $$P_{\varepsilon_{1}}$$ such that if $$P = \{ a_{0} = a <a_{1}<...<a_{n} = b \} \supseteq P_{\varepsilon_{1}}$$ then


$$
\begin{aligned}
\lvert U(f,P) - L(f,P) \rvert < \varepsilon_{1} \iff 0 \leq  \sum_{i=1}^{n-1} (M_{i}-m_{i}) (a_{i+1}-a_{i}) < \varepsilon_{1}
\end{aligned}
$$


where $$M_{i} = \sup \{f(x):a_{i}\leq x \leq a_{i+1}\}$$ and $$m_{i} = \inf \{ f(x):a_{i}\leq x\leq a_{i+1} \}$$.
Now, 


$$
U(g\circ f, P) - L(g \circ f, P) = \sum_{i=0}^{n-1} (\tilde{M_{i}}- \tilde{m_{i}}) (a_{i+1}-a_{i})
$$


with $$\tilde{M_{i}} = \sup \{(g \circ f)(x):a_{i}\leq x \leq a_{i+1}\}$$ and  $$\tilde{m_{i}} = \inf \{(g \circ f)(x):a_{i}\leq x \leq a_{i+1}\}$$.

Now consider the following cases:
**Case 1**: $$M_{i} - m_{i} < \delta$$, so $$\lvert f(x)- f(y) \rvert < \delta$$ for all $$x,y \in [a_{i},a_{i+1}]$$. Then 


$$
\lvert (g \circ f)(x) - (g \circ f)(y) \rvert < \varepsilon.
$$


So $$\tilde{M_{i}} - \tilde{m_{i}} \leq \varepsilon$$. Hence 


$$
\sum_{\text{Case 1}} (\tilde{M_{i}} - \tilde{m_{i}})(a_{i+1}-a_{i}) \leq \sum_{\text{Case 1}} \varepsilon(a_{i+1}-a_{i}) \leq  \sum_{i=0}^{n-1} \varepsilon (a_{i+1}-a_{i}) = \varepsilon(b-a).
$$


**Case 2:** $$M_{i} - m_{i} \geq \delta$$. Let $$-c < g(f(c)) < c$$ for $$x \in [a,b]$$ (we know it is bounded because it is continuous on a closed interval). Then $$\tilde{M_{i}} \leq c$$, $$\tilde{m_{i}}\geq - c$$, and therefore $$\tilde{M_{i}} - \tilde{m_{i}} \leq 2c$$. Then 


$$
\begin{aligned}
\sum_{\text{Case 2}}  (\tilde{M_{i}} - \tilde{m_{i}})(a_{i+1}-a_{i}) &\leq \sum_{\text{Case 2}} \frac{2c}{\delta} \delta (a_{i+1}-a_{i})  \\
&\leq  \frac{2c}{\delta} \sum_{\text{Case 2}} (M_{i} - m_{i})(a_{i+1}-a_{i})A \\
&\leq \frac{2c}{\delta}(U(f,P) - L(f,P)) < \frac{2c}{\delta} \varepsilon_{1}.
\end{aligned}
$$



#### Example 
Let $$f:[a,b] \to \mathbb{R}$$ and $$g:[a,b] \to \mathbb{R}$$ be Riemann integrable. Then the following are Riemann integrable:
1. $$\lvert f \rvert$$
2. $$(f)^{n}, n \in \mathbb{N}$$
3. $$\lvert f \rvert^{1/n}$$
4. $$fg = \frac{(f+g)^{2}-f^{2}-g^{2}}{2}$$.
 
### Lemma (Integrability on subintervals):
Let $$f:[a,b] \to \mathbb{R}$$ be Riemann integrable. Take $$a<x<b$$. Then $$f$$ is Riemann integrable on $$[a,x]$$.

***Proof:*** Exercise.

Define the function $$F(x) = \int_{a}^{x} f(t) \, dt$$. 

### Lemma (Bounds on the Riemann integral) 
Let $$f:[a,b] \to \mathbb{R}$$ be Riemann integrable. Then 


$$
m(b-a) \leq \int_{a}^{b} f(x) \, dx \leq  M(b-a) 
$$


***Proof:*** Let $$f:[a,b] \to \mathbb{R}$$ be bounded. Take $$M = \sup\{ f(x): a \leq x \leq b \}$$ and $$m = \inf\{ f(x): a \leq x \leq b \}$$. Consider a partition $$P = \{ a_{0}=a<a_{1}<...< a_{n} = b \}$$ and consider the Riemann sum 
$$S(f,P,\xi_{1},\dots,\xi_{n}) = \sum_{i=0}^{n} f(\xi_{i})(a_{i+1}-a_{i}) \leq \sum_{i=0}^{n} M(a_{i+1}-a_{i}) = M(b-a).$$ In the same way, $$m(b-a) \leq S(f,P,\xi_{1},\dots \xi_{n}) \leq M(b-a)$$. Moreover, for every $$\varepsilon>0$$, 


$$
I-\varepsilon \leq S(f,P,\xi_{1},\dots,\xi_{n}) \leq I+\varepsilon
$$


In particular, for $$\varepsilon$$ such that $$m(b-a) \leq I-\varepsilon$$ and $$I+\varepsilon \leq M(b-a)$$,

#### Exercise 
Let $$f;[a,b] \to \mathbb{R}$$ be Riemann integrable. Prove that $$f:[x,y] \to \mathbb{R}$$ is Riemann integrable if $$a\leq x\leq y \leq b$$. Then $$F(x) = \int_{a}^{x} f(t)\, dt$$ satisfies that if $$x<y$$, 


$$
\begin{aligned}
F(y) &= \int_{a}^{y} f(t) \, dt = \int_{a}^{x} f(t) \, dt + \int_{x}^{y} f(t) \, dt \\
&= F(x) + \int_{x}^{y} f(t)  \, dt.
\end{aligned}
$$



### Fundamental Theorem of Calculus

Let $$f:[a,b] \to \mathbb{R}$$ be continuous. If $$F(x) = \int_{a}^{x} f(x)  \, dx$$ then $$F'(x) = f(x)$$.

***Proof:*** As a result of the previous exercise, $$-F(x)+F(y) = \int_{x}^{y} f(t) \, dt$$. Moreover, by the lemma bounding the integral, if $$m = \inf \{ f(x):a\leq x\leq b \}$$ and $$M = \sup \{ f(x):a\leq x\leq y \}$$, 


$$
m(y-x)\leq -F(x)+F(y) \leq M(y-x).
$$


We conclude that $$\lvert F(x)-F(y) \rvert \leq \max \{ \lvert M \rvert, \lvert m \rvert \}(y-x)$$.  Let $$x_{0} \in (a,b).$$ We will prove that $$\lim_{y \to x_{0}} \frac{F(y)-F(x_{0})}{y-x_{0}} = f(x_{0})$$. Note that 


$$
 \frac{\int_{x_{0}}^{y} f(x_{0}) \, dx}{y-x_{0}} = \frac{(y-x_{0})f(x_{0})}{y-x_{0}} = f(x_{0}). \tag{1}
$$


Let $$\varepsilon>0$$ be fixed and arbitrary. Then there exists $$\delta>0$$ such that if $$\lvert x-y \rvert < \delta$$ then $$\lvert f(x)-f(y) \rvert < \varepsilon$$. Then


$$
\begin{aligned}
\lim_{ y \to x_{0} } \frac{F(y)-F(x_{0})}{y-x_{0}} - f(x_{0}) &= \lim_{ y \to x_{0} } \frac{\int_{x_{0}}^{y} f(x) \, dx}{y-x_{0}} - \frac{\int_{x_{0}}^{y} f(x_{0}) \, dx}{y-x_{0}}. \\
&=\lim_{ y \to x_{0} } \frac{ \int_{x_{0}}^{y} (f(x)-f(x_{0})) \, dx }{y-x_{0}} = 0.
\end{aligned}
$$


since if $$\lvert y-x_{0} \rvert < \delta$$ and $$y>x_{0}$$ then 


$$
\frac{\left\lvert  \int_{x_{0}}^{y} (f(x)-f(x_{0})) \, dx  \right\rvert }{\lvert y-x_{0} \rvert } \leq  \frac{ \int_{x_{0}}^{y} \lvert f(x)-f(x_{0}) \rvert \, dx  }{\lvert y-x_{0} \rvert } \leq \frac{\varepsilon (y-x_{0})}{y-x_{0}} = \varepsilon.
$$


The case $$x_{0}<y$$ is analogous.

### Definition (Antiderivative):
 Let $$f:[a,b] \to \mathbb{R}$$. We say that $$F:[a,b]\to \mathbb{R}$$ is the antiderivative of $$f$$ if $$F'(x) = f(x)$$ for $$a<x<b$$. 
 
 We have just proved that if $$f$$ is continuous, the antiderivative exists. Assume now that $$f:[a,b] \to \mathbb{R}$$ is differentiable.

### Theorem (Integral of the derivative)
Let $$f:[a,b] \to \mathbb{R}$$. Assume that $$f'[a,b] \to \mathbb{R}$$ is Riemann integrable. Then $$\int_{a}^{b} f'(x) \, dx = f(b)-f(a)$$

***Proof:*** Since $$f'$$ is Riemann integrable, there exists $$I$$ such that, given $$\varepsilon>0$$, there exists $$P_{\varepsilon}$$ such that for every partition $$P = \{ a_{0}=a<a_{1}<...<a_{n}=b \} \supseteq P_{\varepsilon}$$ and for all $$a_{i}\leq\eta_{i}\leq a_{i+1}$$, we have $$\lvert S(f',P, \eta_{1},\dots,\eta_{n}) \rvert < \varepsilon$$.  By the mean value theorem, there exist $$\xi_{i}$$ such that $$f'(\xi_{i})(a_{i+1}-a_{i}) = f(a_{i+1})-f(a_{i})$$. Hence 


$$
S(f',P, \xi_{1},\dots,\xi_{n}) = \sum_{i=0}^{n-1} f'(\xi_{i})(a_{i+1}-a_{i}) = \sum_{i=0}^{n-1} f(a_{i+1}) - f(a_{i}) = f(b)-f(a). 
$$


Now consider $$\lvert (f(b)-f(a)) - I \rvert$$. Expanding, 


$$
\lvert (f(b)-f(a)) - I \rvert = \lvert S(f',P, \xi_{1},\dots, \xi_{n}) - I \rvert < \varepsilon.
$$


Hence $$\lvert (f(a) - f(b)) - I \rvert < \varepsilon$$ for every $$\varepsilon<0$$. Therefore $$f(a)-f(b) = I$$.

### Lemma (Integration by parts)
Let $$f:[a,b] \to \mathbb{R}$$ and $$g:[a,b] \to \mathbb{R}$$ be differentiable with $$f'$$ and $$g'$$ both Riemann integrable. Then $$(fg)' = f'g+fg'$$ is Riemann integrable. Moreover 


$$
\begin{aligned}
\int_{a}^{b} (fg)' \, dx &= \int_{a}^{b} (f'(x)g(x)+f(x)g'(x))  \, dx =f(b)g(b) - f(a) g(a) \\
\implies \int_{a}^{b} f'(x) g(x)  \, dx &= f(b)g(b)-f(a)g(a) - \int_{a}^{b} f(x) g'(x)  \, dx .
\end{aligned}
$$



#### Exercise 
Let $$f:[a,b]\to \mathbb{R}$$ be bounded and Riemann integrable. Suppose that there exist $$m, M \in \mathbb{R}$$ and a partition $$P_{\varepsilon}$$ such that for every partition $$P \supseteq P_{\varepsilon}$$ there exist $$\xi_{1},\dots,\xi_{n}$$ such that 


$$
m\leq S(f,P, \xi_{1},\dots, \xi_{n}) \leq  M.
$$


Then $$m \leq \int_{a}^{b} f(x)  \, dx \leq M$$.

### Theorem (Change of variables) 
Assume that $$f:[a,b] \to \mathbb{R}$$ is continuous and let $$\phi:[c,d] \to [a,b]$$ have a continuous derivative, so that $$\phi([c,d]) \subseteq [a,b]$$. Then 


$$
\int_{c}^{d} f(\phi(u)) \phi'(u) \, du = \int_{\phi(c)}^{\phi(d)} f(x)  \, dx. 
$$



***Proof:*** Consider $$F(x) = \int_{\phi(c)}^{x} f(t)  \, dt$$. Consider $$F(\phi(t))$$. Note that 


$$
[F(\phi(t))]' = F'(\phi(t)) \phi'(t)
$$


Hence 


$$
\begin{aligned}
\int_{c}^{d} F'(\phi(t)) \phi'(t) \, dt &= \int_{c}^{d} [F(\phi(t))]' \, dt  \\
&=F(\phi(d)) - F(\phi(c)) \\
&=\int_{\phi(c)}^{\phi(d)} f(t) \, dt - \int_{\phi(c)}^{\phi(c)} f(t)  \, dt \\
&= \int_{\phi(c)}^{\phi(d)} f(t) \, dt.
\end{aligned}
$$


Finally, 


$$
\begin{aligned}
\int_{\phi(c)}^{\phi(d)}f(t)  \, dt &= \int_{c}^{d} F'(\phi(t)) \phi'(t) \, dt \\
&= \int_{c}^{d} f(\phi(t)) \phi'(t) \, dt. 
\end{aligned}
$$



### Theorem (Mean value theorem for integrals) 

Let $$f:[a,b] \to \mathbb{R}$$ be continuous and Riemann integrable. Then there exists $$c \in [a,b]$$ such that $$f(c) = \frac{1}{b-a}\int_{a}^{b} f(x) \, dx$$

***Proof:*** Take $$M = \sup \{ f(x):a\leq x \leq b \}$$ and $$m =\inf \{ f(x):a\leq x \leq b \}$$.


$$
m \leq \frac{1}{b-a} \int_{a}^{b} f(x) \, dx \leq  M
$$


Since $$f$$ is continuous, there exist $$x_{1}, x_{2} \in [a,b]$$ such that $$M = f(x_{2})$$ and $$m = f(x_{1})$$. Hence 


$$
f(x_{1}) \leq \frac{1}{b-a} \int_{a}^{b} f(x) \, dx \leq  f(x_{2}).
$$


By the mean value theorem, there exists $$c \in [a,b]$$ such that $$f(x) = \frac{1}{b-a}\int_{a}^{b} f(x) \, dx$$.

### Theorem (Mean value theorem for integrals, v2)
Let $$f:[a,b] \to \mathbb{R}$$ be continuous and non-negative, and let $$g:[a,b] \to \mathbb{R}$$ be decreasing, positive and bounded. Then there exists $$c \in [a,b]$$ such that 


$$
F(c) g(a) = \int_{a}^{b} f(x) g(x) \, dx = g(a) \int_{a}^{c} f(x) \, dx.
$$



***Proof:*** Let $$f:[a,b] \to \mathbb{R}$$ be continuous and $$g:[a,b] \to \mathbb{R}$$ Riemann integrable. Recall that 


$$
F(x) = \int_{a}^{x} f(t) \, dt \implies F'(x) = f(x). 
$$


Let $$P = \{ a_{0}=a<a_{1}< \dots<a_{n} = b \}$$ and take (by the intermediate value theorem)


$$
\begin{aligned}
\frac{F(a_{i+1})-F(a_{i})}{a_{i+1}-a_{i}} &= F'(\xi_{i}) = f(\xi_{i}) \\ 
\iff f(\xi_{i})(a_{i+1}-a_{i}) &= F(a_{i+1}) - F(a_{i}).
\end{aligned}
$$


Consider 

$$
\begin{aligned}
\sum_{i=0}^{n-1} f(\xi_{i}) g(\xi_{i}) (a_{i+1}-a_{i}) &= \sum_{i=0}^{n-1} g(\xi_{i})(F(a_{i+1}-F(a_{i})) \\
&= \sum_{i=0}^{n-1} g(\xi_{i}) F(a_{i+1}) - \sum_{i=0}^{n-1} g(\xi_{i}) F(a_{i}) \\
&=\sum_{i=1}^{n} g(\xi_{i-1}) F(a_{i}) - \sum_{i=0}^{n-1} g(\xi_{i}) F(a_{i}) \\
&= \left( \sum_{i=1}^{n-1} F(a_{i})(g(\xi_{i-1}) - g(\xi_{i}))  \right) + g(\xi_{n-1})F(a_{n})- g(\xi_{0})\underbrace{ F(a_{0}) }_{ =0 } \\
&= \underbrace{ \left( \sum_{i=1}^{n-1} F(a_{i})(g(\xi_{i-1}) - g(\xi_{i}))  \right) + g(\xi_{n-1}) F(b).  }_{ (\ast) }
\end{aligned}
$$


Take $$F(z_{1}) = \sup \{ F(x):a\leq x\leq b \}$$. If $$g$$ is decreasing, then 


$$
\begin{aligned}
(\ast) &\leq \left( \sum_{i=1}^{n-1} F(z_{1})(g(\xi_{i-1}) - g(\xi_{i}))  \right) + g(\xi_{n-1}) F(b) \\
&= (g(\xi_{0}) - g(\xi_{n-1}))F(z_{1}) + F(b) g(\xi_{n-1}).
\end{aligned}
$$


 Moreover, since $$g(x)\geq 0$$, we have that 


$$
\begin{aligned}
(\ast) &\leq (g(\xi_{0}) - g(\xi_{n-1}))F(z_{1}) + F(b) g(\xi_{n-1}) \\
&\leq  (g(\xi_{0}) - g(\xi_{n-1}))F(z_{1}) + F(z_{1}) g(\xi_{n-1}) \\
&= F(z_{1}) g(\xi_{0}),
\end{aligned}
$$


since $$F(b) \leq F(z_{1})$$. As $$0\leq F(x)$$ for every $$x$$, we get $$(\ast) \leq F(z_{1})g(a)$$. We conclude that $$\sum_{i=0}^{n-1} f(\xi_{i}) g(\xi_{i})(a_{i+1}-a_{i}) \leq F(z_{1}) g(a)$$, where $$F(z_{1}) = \sup \{ F(x): a\leq x\leq b  \}$$.

By an analogous argument, we can prove that $$\sum_{i=0}^{n-1} (a_{i+1}-a_{i}) \geq F(z_{2})g(a)$$, where  $$F(z_{2}) = \inf \{ F(x): a\leq x\leq b  \}$$. Hence 


$$
\begin{aligned}
g(a) F(z_{1}) \geq  \int_{a}^{b} f(x) g(x) \, d \geq  g(a) F(z_{2}) \\
\iff F(z_{1}) \geq \frac{1}{g(a)}\int_{a}^{b} f(x)g(x) \, dx  \geq  F(z_{2})
\end{aligned}
$$


The result then follows from the mean value theorem for integrals.

### Partitioning disjoint intervals
Consider two intervals $$[a,c]$$ and $$[c,b]$$ and $$f:[a.b] \to \mathbb{R}$$. Let $$P_{1}, P_{2}$$ be partitions of $$[a,c]$$ and $$[c,b]$$ respectively. If $$P_{1} = \{ a_{0}=a<a_{1}< \dots < a_{m}=c\}$$ and $$P_{2} = \{ b_{0} = c < \dots <b_{k} = b \}$$, then $$P_{1} \cup P_{2} = \{ a_{0}=a< \dots < a_{m} = b_{0} = c < \dots < b_{k} = b \}$$.
Hence 


$$
\begin{aligned}
U(f, P_{1} \cup P_{2}) &= U(f,P_{1}) + U(f,P_{2}) \\
L(f, P_{1} \cup P_{2}) &= L(f,P_{1}) + L(f,P_{2}),
\end{aligned}
$$


since, for instance, for the lower sum, 


$$
L(f,P_{1} \cup P_{2}) = \sum_{i=0}^{n-1} m_{i} (a_{i+1}-a_{i}) + \sum_{i=0}^{k-1} m_{i}'(b_{i+1}-b_{i}),
$$


where $$m_{i} = \inf \{ f(x):a_{i}\leq x\leq a_{i+1} \}$$, $$m_{i}' = \inf \{ f(x): b_{i}\leq x \leq b_{i+1}\}$$.

## A removable discontinuity at an endpoint of the interval
Let $$f:[a,b] \to \mathbb{R}$$ be continuous on $$(a,b]$$ with $$\lim_{ x \to a^{+}} \ell_{1} \in \mathbb{R}$$. Then $$f$$ is Riemann integrable on $$[a,b]$$.

***Proof:*** Note that:
1. If $$0<\alpha<b-a$$, $$f:[a + \alpha, b] \to \mathbb{R}$$ is continuous, i.e., Riemann integrable. x
2. Given $$\varepsilon>0$$, there exists $$\delta>0$$ such that if $$0<x-a<\delta$$ then $$\lvert f(x)-\ell_{1} \rvert< \frac{\varepsilon}{2}$$.
Then, if $$a<x,y<a+\delta$$, we have that 


$$
\lvert f(x)-f(y) \rvert \leq  \lvert f(x)- \ell_{1} \rvert + \lvert \ell_{1}-f(y) \rvert < \varepsilon.\ \tag{*}
$$


Let $$P_{1} =  \left\{  a_{0}=a < \dots < a_{m} = a+ \frac{\delta}{2}  \right\}$$ be a partition of $$\left[ a, a + \frac{\delta}{2} \right]$$. Then 


$$
\begin{aligned}
U(f,P_{1})  - L(f, P_{1}) = \sum_{i=0}^{m-1} (M_{i} - m_{i})(a_{i+1}-a_{i}).
\end{aligned}
$$


By $$(*)$$, note that $$f(x) - f(y) \leq M_{i} - m_{i} < \varepsilon$$. Hence 


$$
\begin{aligned}
U(f, P_{1}) - L(f, P_{1}) \leq \sum_{i=0}^{m-1} \varepsilon(a_{i+1}-a_{i}) = \varepsilon \left( a+\frac{\delta}{2} - a \right) = \frac{\varepsilon \delta}{2}.
\end{aligned}
$$


Recall that $$f:\left[ a+\frac{\delta}{2},b \right] \to \mathbb{R}$$ is continuous, i.e. Riemann integrable, so there exists $$P_{\varepsilon} = \left\{  b_{0}=a+\frac{\delta}{2} < \dots < b_{k} = b  \right\}$$ such that for every partition $$P \supseteq P_{\varepsilon}$$ 


$$
U(f,P)-L(f,P) < \frac{\varepsilon}{2}.
$$


We need a $$P_{\varepsilon}'$$ for $$[a,b]$$. Take $$P_{\varepsilon}' = \left\{  a = c_{0} < c_{1} = a+ \frac{\delta}{2} = b_{0} < \dots < b_{k} = c_{k+1} = b  \right\} = P_{\varepsilon} \cup \left\{  a, a+ \frac{\delta}{2}  \right\}$$. Then 


$$
\begin{aligned}
&U(f, P_{\varepsilon}') - L(f, P_{\varepsilon}') \\&= U\left( f,\left\{  a,a+\frac{\delta}{2}  \right\} \right) - L\left( f,\left\{  a,a+\frac{\delta}{2}  \right\} \right) + U(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) \\
& < \frac{\varepsilon \delta}{2} + \frac{\varepsilon}{2}.
\end{aligned}
$$



 > Note: We take the union only with $$\left\{  \alpha, \alpha + \frac{\delta}{2}  \right\}$$ because we bounded $$U-L$$ for every partition of $$[a,a+\delta/2]$$N. In particular, we take the simplest possible partition in order to build a refinement and preserve the properties developed on both subintervals.

## Other useful results

![Pasted image 20250605105619](/assets/img/courses/ma0350/Pasted%20image%2020250605105619.png)

## Some useful tricks.
- Taking the union of partitions produces a refinement of all of them, which is useful when extending results to finer partitions.
- When working around a problematic point $$x_{0}$$, it helps to build a partition around that point, i.e., one that includes the points $$x_{0}-\delta$$ and $$x_{0} + \delta$$, with $$\delta>0$$.
- If a function is known to be Riemann integrable, it is sometimes useful to consider a sequence of partitions $$P_{n}$$ coming from the definition of Riemann integrability for $$\frac{1}{n}$$ (or for $$\frac{\varepsilon}{n}$$ if the goal is to prove the Riemann integrability of another function). One can usually work with some refinement of these partitions. This is generally useful when proving convergence to the integral.
- To prove the mean value theorems, it is usually enough to bound the expression of interest by a function evaluated at two endpoints of an interval.
{% endraw %}
