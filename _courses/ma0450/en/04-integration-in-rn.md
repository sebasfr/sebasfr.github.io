---
layout: chapter
course: ma0450
chapter: 4
title: "Integration in Rn"
slug: 04-integration-in-rn
toc:
  sidebar: right
lang: en
permalink: /notes/ma0450/04-integration-in-rn/
---

{% raw %}
The general idea of the Riemann integral in one variable is to approximate the area under the graph by computing rectangular areas between partitions. How can we carry this idea over to functions of several variables?

## Introduction
Let $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, with $$f$$ bounded and $$D$$ bounded. If $$f: D \subseteq \mathbb{R}^{2} \to \mathbb{R}$$, with $$f(x,y)>0$$, we want $$\int \int_{D} f(x,y) dx dy$$ to represent the volume under $$f$$.

### Definition (Box in $$\mathbb{R}^{n}$$)
We define a box as $$C:[a_{1},b_{1}] \times [a_{2},b_{2}] \times...\times[a_{n}, b_{n}] \subseteq \mathbb{R}^n$$.
1. The volume of $$C$$ is given by $$V(C) = \prod_{i=1}^{n} (b_{i}-a_{i})$$.
2. The faces of the box are the sets of the form 


$$
[a_{1},b_{1}] \times \dots \times [a_{i-1}, b_{i-1}] \times \{ a_{i} \} \times [a_{i+1}, b_{i+1}] \times \dots \times [a_{n}, b_{n}]
$$




$$
[a_{1},b_{1}] \times \dots \times [a_{i-1}, b_{i-1}] \times \{ b_{i} \} \times [a_{i+1}, b_{i+1}] \times \dots \times [a_{n}, b_{n}]
$$


for $$i \in \{ 1,\dots,n \}$$.
3. $$D \subseteq \mathbb{R}^n$$ has volume zero if for every $$\varepsilon>0$$ there is a finite collection of boxes $$\{ C_{i} \}_{i=1}^{k}$$ such that $$D \subseteq \bigcup_{i=1}^{k} C_{i}$$ and $$\sum_{i=1}^{k} V(C_{i}) < \varepsilon$$.
The idea is to define $$\int_{C} f(x)$$ over boxes first.

#### Example 
For $$n=2$$, let $$f:[a_{1}, b_{1}]\to \mathbb{R}$$ be continuous. Define $$G_{f} = \{ (x, f(x)): x \in [a_{1}, b_{1}] \}\subseteq R_{2}$$. We will prove that $$G_{f}$$ has volume zero. Let $$\varepsilon>0$$. Since $$f$$ is continuous on $$G_{f}$$ and $$G_{f}$$ is compact, $$f$$ is uniformly continuous. Then there exists $$\delta>0$$ such that for all $$x,y \in D$$, if $$\lVert x-y \rVert<\delta \implies \lvert f(x) - f(y) \rvert < \frac{\varepsilon}{b-a}$$. Partition the interval $$[a_{1},b_{1}]$$ into $$m \in \mathbb{N}$$ equal intervals ($$a=x_{0}<x_{1}< \dots < x_{m} = b$$), so that $$\frac{b-a}{m} < \delta$$. Explicitly, we define $$x_{i} = a + i \frac{b-a}{m}$$ for $$i \in \{ 0,\dots,m \}$$. It is possible to cover $$G_{f}$$ by boxes of the form $$C_{i} = [x_{i-1}, x_{i}] \times J_{i}$$, with $$J_{i} = \left( \underset{x \in [x_{i-1}, x_{i}] }{\min f(x)}, \underset{x \in [x_{i-1}, x_{i}] }{\min f(x)}+ \frac{\varepsilon}{b-a} \right)$$. So $$G_{f} \subseteq \bigcup_{i=1}^{m} C_{i}$$ and 


$$
V(C_{i}) = \frac{b-a}{m} \frac{\varepsilon}{b-a} = \frac{\varepsilon}{m} \implies  \sum_{i=1}^{m} V(C_{i}) = m \frac{\varepsilon}{m} = \varepsilon. 
$$


![Cajas](/assets/img/courses/ma0450/Cajas.svg)

#### Exercise 
For $$f:D =[a_{1}, b_{1}] \times [a_{2}, b_{2}] \to \mathbb{R}$$, define $$G_{f} = \{ (x,y,f(x,y)):(x,y) \in D \} \subseteq \mathbb{R}^{3}$$. Show that $$V(G_{f}) = 0$$.

### Definition (Partition of a box)
Given a box $$C$$, a partition of $$C$$ is a finite collection of subboxes $$\{ C_{i} \}_{i=1}^{m}$$ obtained from partitions $$P_{i}$$ of $$[a_{i},b_{i}]$$. That is, if $$C= \prod_{i=1}^{n} [a_{i}, b_{i}]$$, we take for each $$i$$ a partition $$P_{i} = \{ a_{i} = x_{0}^{i} < \dots < x_{\ell_{i}}^{i} = b_{i}\}$$, defining the subboxes $$\prod_{i=1}^{n} [x_{m_{i}}^{i}, x_{m_{i}+1}^{i}]$$.

### Definition (Refinement)
Given a box $$C$$ and partitions $$P, Q$$ of $$C$$, we say that $$P$$ is a refinement of $$Q$$ ($$P$$ is finer than $$Q$$) and write $$P \leq Q$$ if every subbox of $$Q$$ is a finite union of subboxes of $$P$$.

#### Note
Given $$P = \{ C_{1},\dots,C_{m} \}$$, $$Q=\{ D_{1},\dots, D_{n} \}$$, even if there is no refinement relation between them, one can build a refinement $$R = \{ C_{i} \cap D_{j}, 1\leq i\leq m, 1\leq j\leq n \}$$, with $$R\leq P$$ and $$R \leq Q$$.

### Definition (Jordan set)
Let $$K \subseteq \mathbb{R}^n$$. We say that $$K$$ is a Jordan set if $$K$$ is bounded and $$V(\partial K) = 0$$. 

#### Example 
Every box is Jordan. 

#### Example 
Given a box $$C \subseteq \mathbb{R}^n$$ and continuous $$f,g: C \to \mathbb{R}$$, 


$$
K = \{ (x, x_{n+1}) \in \mathbb{R}^{n+1}: f(x) \leq x_{n+1} \leq  g(x) \}
$$


is Jordan. This is of interest because it is the volume between two functions.

![Conjunto Jordan](/assets/img/courses/ma0450/Conjunto%20Jordan.svg)
### Definition (Volume with respect to a partition)
Let $$K \subseteq \mathbb{R}^n$$ be Jordan, $$K \subseteq C$$, $$C$$ a box. Given a partition $$P = \{ C_{1}, \dots, C_{m} \}$$ of $$C_{1}$$, the volume of $$K$$ with respect to $$P$$ is defined as


$$
v(K,P) = \sum_{C_{j}\cap \bar{K}\neq \emptyset} v(C_{j}).
$$


We set $$v(\emptyset, P) = 0$$.
![volumen respecto a caja](/assets/img/courses/ma0450/volumen%20respecto%20a%20caja.svg)
#### Exercise

For any partitions $$P$$ and $$Q$$ with $$Q$$ finer than $$P$$, and any Jordan set $$K$$, we have that 


$$
v(K,Q) \leq V(K,P).
$$



### Definition (Volume of a set)
Given a Jordan set $$K$$ and a box $$C$$, the volume of $$K$$ is 


$$
v(K) = \inf \{ v(K,P): \quad P \text{ partition of } C\}.
$$


If $$K$$ is a box, the volume agrees with the definition of the volume of a box.

### Lemma (Independence of the volume)
The volume of $$K$$ is the same no matter which box is chosen.

***Proof:***  Let $$C,D$$ be boxes containing $$K$$. It is enough to consider the case $$K \subseteq C \subseteq D$$ (since $$C \cap D$$ is a box). Define 


$$
\begin{aligned}
v_{C}(K) &= \inf \{ v(K,P): \quad P \text{ partition of } C\},\\
v_{D}(K) &=\inf \{ v(K,P): \quad P \text{ partition of } D\}.
\end{aligned}
$$


Since $$C \subseteq D$$, every partition of $$C$$ can be completed to a partition of $$D$$. So 


$$
v_{D}(K) \leq  v_{C}(K).
$$


Take a partition $$P = \{ C_{1}, \dots, C_{m} \}$$ of $$D$$. Intersecting the boxes in $$P$$ with $$C$$ gives a refinement $$Q = \{ D_{1}, \dots, D_{\ell} \}$$ of $$P$$. Let $$Q_{C}$$ be the subboxes that meet $$C$$. Then 


$$
\begin{aligned}
v(K,P) &= {\sum_{C_{j} \in P, \, C_{j} \cap \bar{K} \neq \emptyset}} v(C_{j}) \quad  \geq  \quad \sum_{D_{j} \in Q, \, D_{j} \cap \bar{K} \neq  \emptyset} v(D_{j})\\
&= v(K, Q) = v(K, Q_{c}) \geq  v_{c}(K).
\end{aligned}
$$


Taking the $$\inf$$ over $$P$$, we get $$v_{D}(K) \geq v_{C}(K)$$. We conclude that $$v_{D}(K) = v_{C}(K)$$.

#### Example 
Let $$f:[a,b]\to \mathbb{R}^{+}$$ be continuous. Let $$B=\{ (x,y)\in \mathbb{R}^{2}, a\leq x\leq b, 0\leq y\leq f(x)\}$$. Let us see that $$\int_{a}^{b} f(x) \, dx = v(B)$$.

***Proof:*** Let $$M>0$$ be such that $$B \subseteq [a,b] \times [0,M]$$. Let $$\varepsilon>0$$. Since $$f$$ is uniformly continuous, take $$\delta>0$$ such that 


$$
\forall x,y \in [a,b], \lvert x-y \rvert < \delta \implies \lvert f(x) - f(y) \rvert < \varepsilon.
$$


Take $$m > \frac{b-a}{\delta}$$ and consider the partition $$P_{x} = \{ a=x_{0} < x_{1} < \dots < x_{m} = b\}$$ with $$x_{i+1} - x_{i} < \delta$$. Then the graph of $$f$$ is covered by boxes $$C_{i} = [x_{i-1},x_{i}] \times J_{i}$$ with $$\lvert J_{i} \rvert < \varepsilon$$ for $$i \in \{ 1,\dots,m \}$$. Moreover, $$J_{i} \subseteq [0, M+\varepsilon]$$. Take 


$$
Q = \{ \underbrace{ D_{1},\dots,D_{r} }_{ \text{covering the graph} }, \underbrace{ E_{1},\dots, E_{p} }_{ \text{below the graph} }, \underbrace{ F_{1},\dots,F_{n} }_{ \text{above the graph} } \}.
$$


So 


$$
\begin{aligned}
\sum_{k=1}^{p} v(E_{k}) \leq  \int_{a}^{b} f(x) \, dx &\leq \sum_{k=1}^{p} v(E_{k})+ \sum_{k=1}^{r} v(D_{k}) = v(B,Q) = \sum_{C_{i} \cap \bar{K} \neq \emptyset} v(C_{i}) \\
\implies v(B,Q) - \int_{a}^{b} f(x) \, dx & \leq v(B,Q) - \sum_{k=1}^{p} v(D_{k}) = \sum_{k=1}^{r} v(D_{k}) \\
&= \sum_{i=1}^{m} v(C_{i}) = \sum_{i=1}^{m} (x_{i}-x_{i-1})\lvert J_{i} \rvert \\
&= \sum_{i=1}^{m} \frac{b-a}{m} \lvert J_{i} \rvert < \sum_{i=1}^{m} \frac{b-a}{m} \lvert \varepsilon \rvert   = \varepsilon(b-a).
\end{aligned} 
$$


So, for every $$\varepsilon>0$$ there is a partition $$Q$$ of $$[a,b] \times [0, M+\varepsilon]$$ such that


$$
\int_{a}^{b} f(x) \, dx \leq v(B, Q) \leq \int_{a}^{b} f(x)  \, dx  + \varepsilon(b-a).
$$


Taking the infimum over $$Q$$, we get $$\int_{a}^{b} f(x) \, dx = v(B)$$.


### Lemma (Union and intersection of Jordan sets)
Let $$K_{1}, K_{2}$$ be Jordan sets in $$\mathbb{R}^n$$. Then:
1. $$K_{1} \cup K_{2}$$ and $$K_{1} \cap K_{2}$$ are Jordan.
2. $$v(K_{1} \cup K_{2}) = v(K_{1}) + v(K_{2}) - v(K_{1} \cap K_{2})$$.

***Proof:*** For 1, note that $$K_{1} \cap K_{2}$$ and $$K_{1} \cup K_{2}$$ are bounded. Moreover, since $$\partial (K_{1} \cup K_{2}) \subseteq \partial K_{1} \cup \partial K_{2}$$ and $$\partial (K_{1} \cap K_{2}) \subseteq \partial K_{1} \cup \partial K_{2}$$, both $$K_{1} \cup K_{2}$$ and $$K_{1} \cap K_{2}$$ are Jordan.

### Definition (Riemann sum)
Given $$f: C \subseteq \mathbb{R}^n \to \mathbb{R}$$ with $$C$$ a box, let $$P = \{ C_{1},\dots, C_{k} \}$$ be a partition of $$C$$. A Riemann sum of $$f$$ with respect to $$P$$ is defined as a sum of the form 


$$
S(f,P, \xi_{1},\dots,\xi_{k}) = \sum_{i=1}^{k} f(\xi_{i}) V(C_{i}), \quad \text{with }\xi_{i} \in C_{i}.
$$


We usually write $$S(f,P, \xi_{1},\dots,\xi_{k}) = S(f,P)$$ for convenience.

#### Note
1. If $$f(\xi_{i}) = \underset{x \in C_{i}}{\sup} f(x)$$, we get an upper sum, and if $$f(\xi_{i}) = \underset{x \in C_{i}}{\inf} f(x)$$.
2. If $$f$$ is bounded ($$\forall x \in C   (m \leq f(x) \leq M)$$), then $$m v(C) \leq S(f, P) \leq Mv(C)$$ for any choice of $$\{ \xi_{i} \}_{i=1}^{n}$$.

### Definition (Riemann integrability)
We say that $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ is Riemann integrable if there exists $$I \in \mathbb{R}$$ such that for every $$\varepsilon > 0$$ there is a partition $$P_{\varepsilon}$$ of $$C$$ such that for every partition $$P = \{ C_{1},\dots,C_{k} \} \leq P_{\varepsilon}$$ and any choice of $$\{ \xi_{i} \}_{i=1}^{n}$$, we have that


$$
\lvert S(f, P, \xi_{1}, \dots, \xi_{k}) - I \rvert < \varepsilon.
$$


We write $$\int_{C} f = I$$. (For $$n=2,3$$ we may write double and triple integrals.)

#### Note
1. $$I$$ is unique, since if there are $$I_{1}, I_{2}$$ satisfying the definition, 


$$
\lvert I_{1} - I_{2} \rvert \leq \lvert I_{1} - S \rvert + \lvert I_{2} - S \rvert < 2\varepsilon
$$


2. $$C = \prod_{i=1}^{n} [a_{i}, b_{i}]$$. If there is an $$i$$ with $$(a_{i}=b_{i})$$, then $$V(C) = \prod_{i=1}^{n} (b_{i}-a_{i}) = 0$$, from which we conclude that $$\int_{C} f = 0$$. 

### Theorem (Cauchy)
Let $$f:C\subseteq \mathbb{R}^n\to \mathbb{R}$$ with $$C$$ a box. Then $$f$$ is Riemann integrable on $$C$$ if and only if for every $$\varepsilon>0$$ there is a partition $$P_{\varepsilon}$$ of $$C$$ such that for all partitions $$P,Q$$ finer than $$P_{\varepsilon}$$ we have $$\lvert S(f,P) - S(f,Q) \rvert < \varepsilon$$ for any choice of the $$\xi_{i}$$.

***Proof:*** ($$\implies$$): Suppose that $$f$$ is Riemann integrable. Then 


$$
\lvert S(f,P) - S(f,Q) \rvert \leq \lvert S(f,P)-I \rvert + \lvert S(f,Q) - I \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon. 
$$



($$\impliedby$$) : Assume the hypothesis. For $$\varepsilon = 1$$, define $$Q_{1}  = P_{1}$$. For $$n \in \mathbb{N}$$, take $$P_{\frac{1}{n}}$$ to be the partition coming from the hypothesis for $$\varepsilon = \frac{1}{n}$$ and define inductively $$Q_{n}$$ as a refinement of $$P_{\frac{1}{n}}$$ and $$Q_{n-1}$$. Then, for every $$n < m$$, 


$$
\lvert S(f,Q_{n}) -S(f,Q_{m}) \rvert < \frac{1}{n}.
$$


For each $$n$$, fix $$\{ \xi_{i} \}$$ ("left interior" nodes). Let $$S_{n} = S(f,Q_{n}, \{ \xi_{i} \})$$. Then the sequence $$(S_{n})_{n \in \mathbb{N}}$$ is Cauchy and therefore converges to a value $$I \in \mathbb{R}$$. Let $$\varepsilon>0$$. Take $$N \in \mathbb{N}$$ such that $$\frac{1}{N} < \frac{\varepsilon}{3}$$ and such that $$\lvert S_{n} - I \rvert < \frac{\varepsilon}{3}$$. Let $$Q_{\varepsilon}$$ be the partition obtained by joining $$P_{\varepsilon}$$ and $$Q_{n}$$. If $$P$$ is finer than $$Q_{\varepsilon}$$, then 


$$
\begin{aligned}
\lvert S(f,P) - I \rvert &\leq \lvert S(f,P) - S(f, Q_{\varepsilon}) \rvert + \lvert S(f, Q_{\varepsilon}) - S_{n} \rvert  + \lvert S_{n}-I \rvert \\
& \leq \frac{1}{n} + \frac{1}{n} + \frac{\varepsilon}{3} < \varepsilon,
\end{aligned}
$$


since $$P \geq Q_{\varepsilon} \geq P_{\varepsilon}$$ and $$Q_{n} \geq P_{\varepsilon}$$.

### Lemma (Bounding sums across partitions)
Let $$f:C \subseteq \mathbb{R}^n\to \mathbb{R}$$ and $$P = \{ C_{1},\dots C_{m} \}$$ a partition of $$C$$. Let $$Q = \{ D_{1},\dots,D_{p} \}$$ be a partition of $$C$$ finer than $$P$$. Then 


$$
\lvert S(f, Q, \{ \xi_{j} \}) - S(f, P, \{ \eta_{k} \}) \rvert \leq  \sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) 
$$


for any choice of $$\{ \xi_{j} \}, \{ \eta_{k} \}$$ of $$P$$ with 


$$
M_{i} = \sup \{ f(x):x \in C_{i} \}, \quad m_{i} = \inf \{ f(x): x \in C_{i} \}.
$$



***Proof:***  Since $$Q$$ is finer than $$P$$, for every $$i \in \{ 1,\dots, m \}$$ we have 
$$C_{i} = D_{i_{1}} \cup \dots \cup D_{i_{\ell}}$$. So $$\xi_{i_{1}}, \dots, \xi_{i_{\ell}} \in C_{i}$$. For $$\eta_{i} \in C_{i}$$ we have 


$$
\begin{aligned}
\left\lvert  f(\eta_{i}) v(C_{i}) - \sum_{r=1}^{\ell} f(\xi_{i_{r}}) v(D_{i_{r}}) \right\rvert &= \left\lvert  \sum_{r=1}^{\ell} (f(\eta_{i}) - f(\xi_{irr})) v(D_{i_{r}})   \right\rvert \\
& \leq  \sum_{r=1}^{\ell} \lvert f(\eta_{i}) - f(\xi_{i_{r}})\rvert v(D_{i_{r}}) \\
& \leq \lvert M_{i} - m_{i} \rvert \sum_{r=1}^{\ell} v(D_{i_{r}}) \\
&=(M_{i}-m_{i}) v(C_{i}).
\end{aligned}
$$


So $$\lvert S(f, Q, \{ \xi_{j} \}) - S(f, P, \{ \eta_{k} \}) \rvert \leq  \sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) < \varepsilon$$.

### Theorem (Riemann)
A bounded $$f:C \subseteq \mathbb{R}^n\to \mathbb{R}$$, with $$C$$ a box, is Riemann integrable if and only if for every $$\varepsilon>0$$ there is a partition $$P_{\varepsilon}$$ of $$C$$ such that if $$P = \{ C_{1},..,C_{m} \}$$ is a refinement of $$P_{\varepsilon}$$, then $$\sum_{i=1}^{m}(M_{i}-m_{i})v(C_{i}) < \varepsilon$$.

***Proof:*** ($$\implies$$) Let $$\varepsilon>0$$. Take a partition $$P_{\varepsilon}$$ with $$\lvert S(f,P, \xi_{1}, \dots, \xi_{k}) \rvert < \varepsilon$$ for every partition $$P = \{ C_{1}, \dots, C_{m} \}$$ finer than $$P_{\varepsilon}$$ and every choice of $$\xi_{i} \in C_{i}$$. Choose $$z_{i}$$, $$y_{i} \in C_{i}$$ such that $$M_{i} - \varepsilon < f(y_{i})$$ and $$f(z_{i}) < m_{i} + \varepsilon$$. So $$M_{i}-m_{i} < f(y_{i}) - f(z_{i}) + 2\varepsilon$$ for every $$1 \leq i \leq m$$.  Then 


$$
\begin{aligned}
\sum_{i=1}^{m} (M_{i}-m_{i}) v(C_{i}) &\leq  \left( \sum_{i=1}^{m} f(y_{i}) v(C_{i}) - I \right) - \left( \sum_{i=1}^{m} f(z_{i}) v(C_{i}) - I \right) + 2\varepsilon v(C_{i}) \\
& < 2\varepsilon + 2\varepsilon v(C) = \varepsilon(1 + 2 v(C)).
\end{aligned}
$$


$$(\impliedby):$$ Let $$\varepsilon>0$$ and $$P_{\varepsilon} = \{ C_{1},\dots,C_{m} \}$$ as in the hypothesis. Since $$P_{\varepsilon}$$ is a refinement of itself, 


$$
\sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) < \varepsilon.
$$


If $$P,Q$$ are finer than $$P_{\varepsilon}$$, then by the previous lemma 


$$
\begin{aligned}
\lvert S(f,P) - S(f,Q) \rvert &\leq  \lvert S(f,P) - S(f, P_{\varepsilon}) \rvert + \lvert S(f,P_{\varepsilon}) - S(f,Q) \rvert \\
&\leq  2 \sum_{i=1}^{m} (M_{i}-m_{i}) v(C_{i}) < 2\varepsilon.
\end{aligned}
$$



### Theorem (Continuity implies Riemann integrability)
If $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ is continuous on $$C$$, then it is Riemann integrable on $$C$$.

***Proof:*** Since $$C$$ is compact, $$f$$ is uniformly continuous. Let $$\varepsilon>0$$. There exists $$\delta>0$$ such that for $$x,y \in C$$ with $$\lVert x-y \rVert < \delta$$ we have $$\lvert f(x) - f(y) \rvert < \frac{\varepsilon}{v(C)}$$. Let $$P_{\varepsilon}$$ be a partition of $$C$$ such that for all $$x,y$$ in each subbox we have $$\lVert x-y \rVert<\delta$$. If $$P = \{ C_{1},\dots,C_{m} \}$$ is finer than $$P_{\varepsilon}$$, then $$M_{i}-m_{i} < \frac{\varepsilon}{v(C)}$$ for every $$1\leq i\leq m$$, and so $$\sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) < \varepsilon v(C)$$.

### Lemma (Discontinuity on a set of volume zero)
Let $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ be bounded on a box $$C$$ and continuous on $$C \setminus D$$, with $$D \subseteq C$$ a set of volume zero. Then $$f$$ is Riemann integrable on $$C$$.

***Proof:*** Let $$\varepsilon>0$$. Since $$v(D) = 0$$, there exist $$C_{1}, \dots, C_{m} \subseteq C$$ with $$D \subseteq \bigcup_{i=1}^{m} C_{i}$$ and $$\sum_{i=1}^{m} v(C_{i}) < \varepsilon$$. Complete $$\{ C_{1},\dots, C_{m} \}$$ to a partition $$\{ C_{1}, \dots, C_{m} \}$$ to a partition $$\{C_{1},\dots,C_{m},\dots,C_{p}\}$$ of $$C$$. By continuity, $$f$$ is integrable on $$C_{m+1},\dots,C_{p}$$. For $$j \in \{ m+1,\dots,p \}$$, by Riemann integrability there exist $$P_{\varepsilon}^{j}$$ satisfying the definition for $$\frac{\varepsilon}{p-m}>0$$.

Let $$P_{\varepsilon}$$ be a partition of $$C$$ such that the subboxes of $$P_{\varepsilon}$$ lying in $$C_{j} \  (j=m+1,\dots,p)$$ form a partition finer than $$P_{\varepsilon}^{j}$$. Without loss of generality, take $$P_{\varepsilon}$$ such that $$C_{j} \, (j=m+1,\dots,p)$$ is a finite union of boxes of $$P_{\varepsilon}$$. 

Given a partition $$Q = \{ D_{1},\dots,D_{q} \}$$ finer than $$P_{\varepsilon}$$, suppose there is $$r \in \mathbb{N}$$ such that $$Q_{D} = \{D_{1},\dots,D_{r}\} \subseteq \{ C_{1},\dots, C_{m} \}$$ and $$Q_{C} = \{ D_{r+1},\dots,D_{q} \} \subseteq \{ C_{m+1},\dots,C_{p} \}$$. So


$$
\begin{aligned}
\left\lvert S(f,Q, \xi_{1},\dots,\xi_{q})  - \sum_{j=m+1}^{p} \int_{C_{j}} f \,\right\rvert &\leq \lvert S(f,Q_{D}, \xi_{1},\dots,\xi_{r}) \rvert + \left\lvert S(f,Q_{C}, \xi_{r+1},\dots,\xi_{q})  - \sum_{j=m+1}^{p} \int_{C_{j}} f \right\rvert \\ 
&\leq \sum_{j=1}^{r} \lvert f(\xi_{j}) \rvert v(D_{j}) + \sum_{j=m+1}^{p} \left\lvert  S(f,C_{j}) - \int_{C_{j}}f \right\rvert \\
&\leq M \varepsilon + (p-m) \frac{\varepsilon}{p-m}.
\end{aligned}
$$


### Definition (Riemann integrability on Jordan sets)
Let $$f:K \subseteq \mathbb{R}^n\to \mathbb{R}$$ with $$K$$ Jordan. Let $$C$$ be a box with $$C \supseteq K$$. We define the extension by zero of $$f$$ to $$C$$ as 


$$
f^{C}(x) = \begin{cases}
f(x), \quad \text{if } x \in K \\ 
0, \quad \text{if } x \not\in K. \\
\end{cases}
$$


We say that $$f$$ is Riemann integrable on $$K$$ if $$f^{C}$$ is Riemann integrable on $$C$$. We write $$\int_{K} f = \int_{T} f^{c}$$.

#### Note
The definition does not depend on $$C$$, since $$\int_{C_{1}} f^{C_{1}} = \int_{C_{2}} f^{C_{2}}$$ for boxes $$C_{1} \supseteq K$$, $$C_{2} \supseteq K$$.

***Proof:*** Given $$\varepsilon>0$$, take partitions $$P_{\varepsilon}, Q_{\varepsilon}$$ of $$C_{1}$$ and $$C_{2}$$ satisfying the definition of Riemann integrability for $$f^{C_{1}}$$ and $$f^{C_{2}}$$ respectively. Without loss of generality, suppose that every subbox of $$Q_{\varepsilon}$$ is a subbox of $$P_{\varepsilon}$$. So 


$$
\begin{aligned}
\left\lvert  \int_{C_{1}} f^{C_{1}} - \int_{C_{2}} f^{C_{2}}   \right\rvert &\leq \left\lvert  S(f^{C_{1}}, P\varepsilon) - \int_{C_{1}} f^{C_{1}} \right\rvert + \left\lvert  S(f^{C_{1}}, P\varepsilon) - \int_{C_{2}} f^{C_{2}} \right\rvert \\
&< \varepsilon + \left\lvert  S(f^{C_{1}}, P\varepsilon) - \int_{C_{2}} f^{C_{2}} \right\rvert < 2\varepsilon.
\end{aligned}
$$



### Definition (Characteristic function)
Let $$A \subseteq \mathbb{R}^n$$. The characteristic function of $$A$$ is $$1_{A}: \mathbb{R}^n\to \{ 0,1 \}$$ with


$$
1_{A}(x) = \begin{cases}
1, \quad \text{if }x \in A,\\
0, \quad \text{if }x \not\in A.
\end{cases}
$$


#### Note
$$1_{A \cup B} = 1_{A} + 1_{B} - 1_{A \cap B}$$. This can be proved case by case.
### Lemma (Volume as an integral) 
Let $$K \subseteq \mathbb{R}^n$$ be Jordan. Then $$\int_{K} 1 = v(K)$$.

***Proof:*** Let $$C$$ be a box with $$K \subseteq C$$ and let $$1_{C}$$ be the extension by zero to $$C$$. Note that $$1_{C}$$ is Riemann integrable since $$v(\partial K) = 0$$. We want to prove that 


$$
\int_{C} 1_{C} = \inf \{ v(K, P): P \text{ partition of }C \}.
$$


Let $$\varepsilon>0$$. Since $$v(\partial K) = 0$$, there exist $$C_{1},\dots, C_{m}$$ with $$\partial K \subseteq \bigcup_{i=1}^{m} C_{i}$$ such that $$\sum_{i=1}^{m}v(C_{i}) < \varepsilon$$. From the definition of the infimum, take a partition $$Q_{\varepsilon}$$ of $$C$$ such that 


$$
v(K) \leq v(K, Q_{\varepsilon}) < v(K) + \varepsilon.
$$


Let $$P_{\varepsilon}$$ be a partition of $$C$$ satisfying the definition of Riemann integrability for $$1_{C}$$. Without loss of generality, $$Q_{\varepsilon}=P_{\varepsilon}$$ and the $$C_{i}$$ are subboxes of $$P_{\varepsilon} = \{ C_{1},\dots,C_{m}, C_{m+1},\dots, C_{p} \}$$, with $$\{ C_{m+1},\dots, C_{n} \} \subseteq K^{\circ}$$ for $$n < p$$. So 


$$
\begin{aligned}
\left\lvert  \int_{K} 1 - v(K)   \right\rvert  &\leq \left\lvert  \int_{K}1-v(K, P_{\varepsilon})  \right\rvert + \lvert  v(K, P_{\varepsilon}) - v(K) \rvert \\
&< \left\lvert  \int_{K} 1 - \sum_{i=1}^{n} v(C_{i})  \right\rvert + \varepsilon\\
&= \left\lvert  \int_{C} 1_{C} - \sum_{i=1}^{n} v(C_{i})  \right\rvert + \varepsilon < 2\varepsilon, 
\end{aligned}
$$


since $$\sum_{i=1}^{n} v(C_{i})$$ is a Riemann sum for $$1_{C}$$ over $$P_{\varepsilon}$$.

### Lemma (Functions equal except on a set of volume zero)

Let $$f,g: C \subseteq \mathbb{R}^n \to \mathbb{R}$$ be functions defined on the box $$C$$ with $$f$$ Riemann integrable and $$g$$ bounded on $$C$$. If $$g(x) = f(x)$$ for every $$x \in C \setminus D$$, where $$D \subseteq C$$ has volume zero, then $$g$$ is integrable on $$C$$ and $$\int_{C}f = \int_{C} g$$.

***Proof:*** Pending
#### Corollary 
If $$f:K\subseteq \mathbb{R}^n \to \mathbb{R}$$ is bounded and $$v(K)=0$$, then $$f$$ is Riemann integrable on $$K$$ and $$\int_{K} f = 0$$.

***Proof:*** If $$C$$ is a box with $$K \subseteq C$$, then $$f_{C}(x) = 1_{K}(x) = 0$$ for every $$x \in C \setminus K$$. Then, applying the lemma,


$$
\int_{K} f = \int_{C} f_{C} = \int_{C} 1_{K} = \int_{K} 1 = v(K) = 0.
$$



## Properties of the Riemann integral

### Theorem (Linearity)
Let $$f,g:K \subseteq \mathbb{R}^n \to \mathbb{R}$$, with $$K$$ Jordan and $$f,g$$ Riemann integrable. Then, given $$c \in \mathbb{R}$$, $$f+cg$$ is Riemann integrable and 


$$
\int_{K} f+cg = \int_{K} f + c \int_{K} g.
$$


***Proof:*** Without loss of generality, suppose that $$K$$ is a box. Given $$\varepsilon > 0$$, take $$P_{\varepsilon}, Q_{\varepsilon}$$ satisfying the definition of Riemann integrability for $$f$$ and $$g$$ respectively. Without loss of generality, suppose that $$P_{\varepsilon} = Q_{\varepsilon}$$. Then, for $$P \leq P\varepsilon$$


$$
\begin{aligned}
S(f+cg, P) &= \sum_{i=1}^{m} (f+cg)(\xi_{i}) v(C_{i}) \\
&=S(f,P) + cS()g,P \\
\end{aligned}
$$


So


$$
\begin{aligned}
\left\lvert  S(f+cg),P - \int_{K}f -c \int_{K} g\right\rvert & \leq \left\lvert  S(f,P) - \int_{K} f \right\rvert + \lvert c \rvert \left\lvert  S(g,P) - \int_{K} g  \right\rvert  \\
& <\varepsilon + \lvert c \rvert \varepsilon = \varepsilon(1 + \lvert c \rvert ).
\end{aligned}
$$


### Theorem (Additivity over sets)
Let $$A,B$$ be Jordan sets in $$\mathbb{R}^n$$ and $$f:A \cup B \to \mathbb{R}$$ such that $$f \mid_{A}$$ and $$f \mid_{B}$$ are R.I. on $$A$$ and $$B$$ respectively. Then
1. $$f$$ is R.I. on $$A \cup B$$.
2. $$\int_{A \cup B} f = \int_{A} f + \int_{B}f - \int_{A \cap B} f$$. 

***Proof:*** One can check that $$A \cap B$$ is Jordan and that $$f$$ is Riemann integrable on $$A \cap B$$ (since $$A \cap B \subseteq A$$). Then 


$$
\begin{aligned}
\int_{A} f + \int_{B} f - \int_{A \cap B} f &= \int_{A \cup B} 1_{A} f + \int_{A \cup B} 1_{B} f - \int_{A \cup B} 1_{A \cap B} f \\
&= \int_{A \cup B} 1_{A}f + 1_{B} f - 1_{A \cap B} f \\
&= \int_{A \cup B} 1_{A \cup B} f = \int_{A \cup B} f.
\end{aligned}
$$



### Theorem (Building Riemann-integrable functions)
Let $$f,g: K \subseteq \mathbb{R}^n \to \mathbb{R}$$, with $$K$$ Jordan. Suppose both are Riemann integrable on $$K$$. Then
1. $$\lvert f \rvert$$ is Riemann integrable on $$K$$
2. For every $$n \in \mathbb{N}$$, $$f^{n}$$ is Riemann integrable on $$K$$.
3. If there exists $$\varepsilon>0$$ such that for every $$x \in K$$, $$f(x)\geq \varepsilon$$, then $$\frac{1}{f}$$ is Riemann integrable on $$K$$.
4. $$fg$$ is Riemann integrable on $$K$$. (Trick: $$fg = \frac{(f+g)^{2}-f^{2}-g^{2}}{2}$$).

### Theorem (Composition and Riemann integrability)
Let $$f:K \subseteq \mathbb{R}^n\to \mathbb{R}$$ be Riemann integrable on $$K$$ and $$g:[c,d]\to \mathbb{R}$$ continuous with $$f(K) \subseteq [c,d]$$. Then $$g \circ f$$ is Riemann integrable on $$K$$.

## Iterated integrals

We now focus on computing $$\int_{K} f$$ for general regions $$K$$.
### Lemma (Continuity of the inner integral)
If $$f:[a,b] \times [c,d] \to \mathbb{R}$$ is continuous, then $$F:[c,d]\to \mathbb{R}$$ given by 


$$
F(y) = \int_{a}^{b} f(x,y) \, dx 
$$


is continuous.

***Proof:*** Let $$\varepsilon>0$$. By uniform continuity, there exists $$\delta>0$$ such that for every $$x \in [a,b]$$ and all $$y,y_{0} \in [c,d]$$, if $$\lvert y-y_{0} \rvert<\delta$$ then $$\lvert f(x,y)-f(x,y_{0}) \rvert < \varepsilon$$. Then 


$$
\begin{aligned}
\lvert F(y)-F(y_{0}) \rvert &= \left\lvert  \int_{a}^{b} f(x,y) \, dx    - \int_{a}^{b} f(x,y_{0}) \, dx \right\rvert\\
& \leq  \int_{a}^{b} \lvert f(x,y) - f(x,y_{0}) \rvert  \, dx = \varepsilon(b-a),
\end{aligned}
$$


from which we conclude that $$F$$ is continuous.

#### Note
$$G(x) = \int_{c}^{d} f(x,y) \, dy$$ is continuous by the same argument.

### Theorem (Fubini)
Let $$f:\underbrace{ [a,b] \times [c,d] }_{ C } \to \mathbb{R}$$, with $$f$$ continuous. Then 


$$
\int_{C} f = \int_{a}^{b} \left( \underbrace{ \int_{c}^{d} f(x,y)  \, dy }_{ G(x) }  \right) \, dx = \int_{c}^{d} \left( \underbrace{ \int_{a}^{b} f(x,y)  \, dx  }_{ F(y) } \right) \, dy.
$$


***Proof:*** We know that the 3 integrals exist because $$f$$ is continuous. Moreover, since $$f$$ is uniformly continuous on $$[a,b] \times [c , d]$$, given $$\varepsilon>0$$ there exists $$\delta>0$$ such that $$\lvert f(x_{1},y_{1}) - f(x_{2},y_{2})\rvert < \varepsilon$$ whenever $$\lVert (x_{1}-x_{2},y_{1}-y_{2}) \rVert < \delta$$. Partition $$[a,b]$$ into $$\{ a=x_{0}<x_{1}< \dots < x_{m} = b \}$$ and $$[c,d]$$ into $$\{ c = y_{0} < y_{1} < \dots < y_{n} = d \}$$ such that $$\lvert x_{i+1} - x_{i} \rvert < \frac{\delta}{\sqrt{ 2 }}$$ and $$\lvert y_{j+1}-y_{j} \rvert < \frac{\delta}{\sqrt{ 2 }}$$ for all $$i,j$$. 
Since $$f$$ is Riemann integrable on $$C$$, without loss of generality suppose that $$P_{\varepsilon}$$ agrees with the partitions generated for $$[a,b]$$ and $$[c,d]$$. We have that 


$$
\begin{aligned}
I_{2}:=\int_{a}^{b} \left( \int_{c}^{d} f(x,y) \, dy  \right)  \, dx &= \int_{a}^{b} \left( \sum_{j=1}^{n} \int_{y_{j-1}}^{y_{j}} f(x,y) \, dy  \right) \, dx  \\
&= \underbrace{ \int_{a}^{b} \left(  \sum_{j=1}^{n} f(x,t_{j}) \cdot (y_{j}-y_{j-1}) \right) \, dx }_{ \text{by the MVT for integrals with } t_{j} \in [y_{j-1}, y_{j}] } \\
&= \sum_{j=1}^{n} (y_{j}-y_{j-1}) \int_{a}^{b} f(x,t_{j}) \, dx \\
&\underset{\text{MVT}}{=} \sum_{j=1}^{n} (y_{j} - y_{j-1}) \sum_{i=1}^{m} \int_{x_{i-1}}^{x_{i}} f(x,t_{j})  \, dx \\
&= \sum_{j=1}^{n} \sum_{i=1}^{m} (y_{j}-y_{j-1}) (x_{i}- x_{i-1}) f(s_{i}, t_{j}) \\ &= S(f, P_{\varepsilon}, \{ (s_{i},t_{j}) \}).
\end{aligned}
$$


In an analogous way, there exist $$p_{i} \in [x_{i-1}, x_{i}]$$ and $$q_{j} \in [y_{j-1}, y_{j}]$$ such that 


$$
I_{3}:= \int_{c}^{d} \left( \int_{a}^{b} f(x,y) \, dx  \right)  \, dy = S(f, P_{\varepsilon}, \{ (p_{i}, q_{j}) \}).
$$


So 


$$
\begin{aligned}
\lvert I_{2}-I_{3} \rvert & \leq  \sum_{i=1}^{m} \sum_{j=1}^{n} (y_{j} - y_{j-1})(x_{i}-x_{i-1}) \lvert f(s_{i},t_{j}) - f(p_{i}, q_{j}) \rvert \\
& < \varepsilon(b-a)(d-c)
\end{aligned}
$$


since $$\lVert (s_{i},t_{j}) - (p_{i}, q_{i}) \rVert = \sqrt{ (s_{i}-p_{i})^{2} +(t_{j}-q_{j})^{2}} \leq \sqrt{ \frac{\delta^{2}}{2} + \frac{\delta^{2}}{2} } = \delta$$. In this way, $$I_{2} = I_{3}$$.
Finally, 


$$
\left\lvert  \int_{C} f  - I_{2}\right\rvert = \left\lvert  \int_{C} f - S(f,P_{\varepsilon}, \{ (s_{i},t_{j}) \})  \right\rvert  < \varepsilon
$$


by the definition of Riemann integrability.
#### Note (Triple integrals)
If $$f:[a,b]\times[c,d] \times[e,f]\to \mathbb{R}$$ is continuous, we can generalise Fubini to any order of integration, and the proof runs analogously. The same holds for any reordering for functions from $$\mathbb{R}^n$$ to $$\mathbb{R}$$.

### Theorem (Fubini with discontinuities)
Let $$f:[a,b] \times [c,d] \to \mathbb{R}$$ be a Riemann integrable function such that for every $$y \in [c,d]$$ the function $$f(\cdot,y):[a,b] \to \mathbb{R}$$ has finitely many discontinuities. Then 


$$
F:[c,d]\to \mathbb{R}, \quad F(y) = \int_{a}^{b} f(x,y) \, dy
$$


is integrable and 


$$
\int_{[a,b] \times [c,d]} f = \int_{c}^{d} \left( \int_{a}^{b} f(x,y) \, dx  \right) \, dy.
$$



***Proof:*** $$F(y)$$ is well defined, since by hypothesis $$f(\cdot,y)$$ has finitely many discontinuities.  Given $$\varepsilon>0$$, take $$P_{\varepsilon}$$ from the definition of Riemann integrability. Let $$\{ x_{0},\dots, x_{n} \}, \{ y_{0},\dots,y_{m} \}$$ be the partitions of $$[a,b]$$ and $$[c,d]$$ respectively generated by $$P_{\varepsilon}$$. We have 


$$
\begin{aligned}
S(F, \{ y_{j} \}, \{ \xi_{j} \}) &= \sum_{j=1}^{m} F(\xi_{j})(y_{j}-y_{j-1}) \\
&= \sum_{j=1}^{m} \int_{a}^{b} f(x, \xi_{j})(y_{j}-y_{j-1}) \, dx 
\end{aligned}
$$


for any choice of $$\{ \xi_{1},\dots,\xi_{m} \}$$ with $$x_{j-1} < \xi_{j} < x_{j}$$. Since $$f(\cdot, \xi_{j})$$ is Riemann integrable on $$[a,b]$$, there is a Riemann sum $$S(f(\cdot, \xi_{j}))$$ over a partition $$Q$$ of $$[a,b]$$ finer than $$\{ x_{j} \}_{j=0}^{n}$$ such that 


$$
\left\lvert  \int_{a}^{b} f(x, \xi_{j}) \,dx - S(f(\cdot, \xi_{j}))  \right\rvert < \varepsilon.
$$


Note that the partition generated by $$Q$$ and $$\{ y_{0},\dots, y_{m} \}$$ of $$[a,b] \times [c,d]$$ is finer than $$P_{\varepsilon}$$ and 


$$
\sum_{j=1}^{m} S(f(\cdot, \xi_{i}))(y_{j}-y_{j-1})
$$


is a Riemann sum for $$f$$ over that partition. So 


$$
\begin{aligned}
\left\lvert  \int_{C} f - S(F, \{ y_{j} \}, \{ \xi_{j} \} )  \right\rvert &\leq \left\lvert  \int_{C} f - \sum_{j=1}^{m}  S(f(\cdot, \xi_{i}))(y_{j}-y_{j-1})  \right\rvert \\  &\quad + \left\lvert  \sum_{j=1}^{m}  S(f(\cdot, \xi_{i}))(y_{j}-y_{j-1}) - \sum_{j=1}^{m} \int_{a}^{b} f(x, \xi_{j})(i_{j}-y_{j-1}) \, dx  \right\rvert \\
& <\varepsilon + \sum_{j=1}^{m} \left\lvert  S(f(\cdot, \xi_{i})) - \int_{a}^{b} f(x, \xi_{j})  \, dx   \right\rvert (y_{j}-y_{j-1}) \\
& < \varepsilon(1+d-c),
\end{aligned} 
$$


from which we conclude that $$F$$ is Riemann integrable on $$[c,d]$$ and $$\int_{C} = \int_{c}^{d} F(y) \, dy$$.
### Lemma (Area between graphs)

Let $$\phi, \psi:[a,b]\to \mathbb{R}$$ be continuous, with $$\phi(x) \leq \psi(x)$$ for every $$x \in [a,b]$$. Define 


$$
A = \{ (x,y): a\leq x\leq b, \phi(x) \leq  y \leq  \psi(x) \}.
$$


If $$f:A\to \mathbb{R}$$ is continuous, then $$\int_{A} f = \int_{a}^{b}\left( \int_{\phi(x)}^{\psi(x)}f(x,y)  \, dy \right)  \, dx$$.

***Proof:*** We know that $$A$$ is Jordan and $$f$$ is continuous. Therefore $$f$$ is Riemann integrable on $$A$$. By the definition of $$\int_{A} f$$, I need a box $$C \supseteq A$$. Define 


$$
f^{C}(x) = \begin{cases}
f(x),  \quad x \in A \\
0, \quad x \in C \setminus A
\end{cases} 
$$


So $$\int_{A} f = \int_{C} f^{C} = \int_{c}^{d} \int_{e}^{\text{f}} f^{C}(x,y)  \, dy  \, dx = \int_{a}^{b} \int_{e}^{f}  f^{C}(x,y)\, dy  \, dx$$. Expanding: 


$$
\begin{aligned}
\int_{a}^{b} \int_{e}^{\text{f}}  f^{C}(x,y)\, dy  \, dx &= \int_{a}^{b} \left( \underbrace{ \int_{e}^{\phi(x)} f^{C}  \, dy }_{ 0 } + \int_{\phi(x)}^{\psi(x)} f^{C} \, dy + \underbrace{ \int_{\phi(x)}^{\text{f}} f^{c}  \, dy }_{ 0 }  \right) \, dx  \\
&= \int_{a}^{b} \int_{\phi(x)}^{\psi(x)} f(x,y)  \, dy   \, dx.
\end{aligned}
$$



#### Example 
Compute the volume of the region bounded by $$x^{2}+y^{2}\leq 9$$, $$y^{2}-x^{2} \leq 1$$. 
Working algebraically,


$$
y^{2}-x^{2} = 1 \implies y = \pm \sqrt{ 1+x^{2} }.
$$


Note that in this relation $$\lvert y \rvert\geq1$$ and $$y=x$$ for every $$(x,y) \in A$$. Let us find the intersections between the two relations: 


$$
\begin{aligned}
x^{2}+y^{2}&=9\\
y^{2}-x^{2}&=1\\
\implies 2y^{2} &= 10,
\end{aligned}
$$


from which we get $$y = \pm \sqrt{ 5 }, x = \pm 2$$. I need 


$$
v(A) = \int_{A} 1  = \int_{?} \int_{?} \, dy \, dx = \int_{?} \int_{?}\, dx \, dy.
$$


To compute the limits of integration it helps to draw pictures. Let us first integrate over $$y$$ and then over $$x$$ ("type 1").



$$
\begin{aligned}
v(A) &= \underbrace{ \int_{-3}^{-2} \int_{-\sqrt{ 9-x^{2} }}^{\sqrt{ 9-x^{2} }} 1 \, dy  \, dx  }_{ I_{1} }+ \int_{-2}^{2} \int_{-\sqrt{ 1+x^{2} }}^{\sqrt{ 1+x^{2} }} 1 \, dy \, dx + \int_{2}^{3} \int_{-\sqrt{ 9-x^{2} }}^{\sqrt{ 9-x^{2} }}  \, dy   \, dx \\
&=
\end{aligned}
$$


If we integrate first over $$x$$ and then over $$y$$ ("type 2") 


$$
\begin{aligned}
v(A) &= \int_{-1}^{1} \int_{-\sqrt{ 9-y^{2} }}^{\sqrt{ 9-y^{2} }} 1 \, dx  \, dy +\int_{1}^{\sqrt{ 5 }} \int_{-\sqrt{ 9-y^{2} }}^{-\sqrt{ y^{2}-1 }}  1\, dx   \, dy + \int_{1}^{\sqrt{ 5 }} \int_{\sqrt{ 9-y^{2} }}^{\sqrt{ y^{2}-1 }}  \, 1 dx   \, dy \\
&  \quad + \int_{-1}^{\sqrt{ -5 }} \int_{-\sqrt{ 9-y^{2} }}^{-\sqrt{ y^{2}-1 }}  \, 1 dx   \, dy  + \int_{-1}^{\sqrt{ -5 }} \int_{\sqrt{ 9-y^{2} }}^{\sqrt{ y^{2}-1 }}  \, 1 dx   \, dy 
\end{aligned}
$$



### Theorem (Integration with finitely many discontinuities)
Let $$f:[a,b] \times [c,d] \to \mathbb{R}$$ be such that for every $$y \in [c,d]$$ the function $$f(\cdot, y):[a,b] \to \mathbb{R}$$ has finitely many discontinuities. Then:
1. $$F:[c,d] \to \mathbb{R}$$, $$F(y) = \int_{a}^{b} f(x,y) \, dx$$ is R.I.
2. $$\int_{[a,b]\times[c,d]}f = \int_{c}^{d} F(y) dy = \int_{c}^{d} \left( \int_{a}^{b} f(x,y) \, dx \right) \, dy$$. 

#### Idea
In 2 dimensions, $$\int_{K} f = \int_{a}^{b} \int_{\psi(X)}^{\phi(x)} f \, dy \, dx$$

#### Example 
Compute the volume of a sphere of radius $$r$$: 


$$
K = \{ (x,y,z):x^{2}+y^{2}+z^{2} \leq  r \}.
$$


The volume of the sphere is given by 


$$
\int_{-r}^{r} \int_{-\sqrt{ r^{2}-x^{2} }}^{\sqrt{ r^{2}-x^{2} }} \int_{-\sqrt{ r^{2}-x^{2}-y^{2}}}^{\sqrt{ r^{2}-x^{2}-y^{2}}} 1 \, dx   \, dy  \, dx 
$$



#### Example 
Compute the volume in the first octant bounded by the plane $$2x+3y+z=6$$.
We have that 


$$
V = \int_{0}^{2} \int_{0}^{(6-3y)/2} \int_{0}^{6-2x-3y}  \, dz  \, dx  \, dy = \int_{0}^{6} \int_{0}^{(6-z)/3} \int_{0}^{(6-z-3y)/2}  \, dx  \, dy  \, dz.
$$


 For the first order we analyse first on the $$xy$$ plane, and for the second on the $$yz$$ plane.
#### Example 
Compute $$\int \int \int_{K} f \,dz \,dy \,dx$$, with $$K$$ in the first octant bounded by 


$$
\begin{aligned}
P_{1}&: x=0 \\
P_{2}&: y=0 \\
P_{3}&: z=0 \\
\pi_{1}&: 2x+4y+3z = 36 \\
\pi_{2}&: x+y+z = 11 \\
\pi_{3}&: 2x+3z = 24.
\end{aligned}
$$



## Change of variables

In one dimension, if $$f$$ is continuous and $$g:[a,b]\to \mathbb{R}$$ is differentiable with continuous first derivative, then


$$
\int_{g(a)}^{g(b)}  f(x) \, dx  = \int_{a}^{b} f(g(t)) g'(t) \, dt.
$$


Moreover, this can be relaxed to $$f$$ integrable on $$g([a,b])$$ and $$g$$ monotone on $$[a,b]$$, in which case $$\lvert g'(t) \rvert$$ is used in the integral

### Theorem (Change of variables)
A generalisation of the Riemann integral (MA0350, substitution in one variable). Uses determinants (MA0360). Let $$A \subseteq \mathbb{R}^n$$ be an open set and $$g:A\to \mathbb{R}^n$$ injective and continuously differentiable on $$A$$ with $$\det J_{g}(x) \neq 0$$ for every $$x \in A$$. If $$K$$ is Jordan and $$\bar{K} \subseteq A$$, then 


$$
\int_{g(K)} f = \int_{K} (f \circ g) \lvert \det J_{g} \rvert. \ \tag{*} 
$$



### Lemma (The image of a box under $$g$$ is Jordan)
1. If $$K \subseteq A$$ is Jordan then $$g(K)$$ is Jordan
2. If $$v(K) = 0$$ then $$v(g(K)) = 0$$

### Lemma (Volume under transformations) 
Let $$C \subseteq \mathbb{R}^n$$ be a box and $$g:C\to \mathbb{R}^n$$ linear and injective. Then 


$$
v(g(C)) = \int_{g(C)} 1 = \int_{C} \lvert \det J_{g} \rvert 
$$



### Lemma  (Composition of changes of variables)
If $$(*)$$ holds for $$g:A\to \mathbb{R}^n$$ and $$h:B\to \mathbb{R}^n$$ with $$g(A) \subseteq B$$, then it holds for $$h \circ g: A \to \mathbb{R}^n$$.

### Lemma 
If $$(*)$$ holds for $$f \equiv 1$$, then it holds for any function.


#### Examples of changes of variables
1.  Elliptic coordinates: for ellipses of the form 


$$
\left( \frac{x}{a} \right)^{2} + \left( \frac{y}{b} \right)^{2} = 1,
$$


make the change of variables $$x = a r \cos \theta, y = br \sin \theta$$, with $$r \in [0,1]$$ and $$\theta \in [0,2\pi]$$; then $$\lvert \det J_{g} \rvert = abr \neq 0$$ for every $$r \neq 0$$.
{% endraw %}
