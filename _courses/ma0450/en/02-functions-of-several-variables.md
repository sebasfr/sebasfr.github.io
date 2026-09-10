---
layout: chapter
course: ma0450
chapter: 2
title: "Functions of Several Variables"
slug: 02-functions-of-several-variables
toc:
  sidebar: right
lang: en
fecha: 2025-08-25
permalink: /notes/ma0450/02-functions-of-several-variables/
---

{% raw %}
## Reminder (Definition of a function)
Given two sets $$A, B$$, a relation $$f: A \to B$$ is called a function if 


$$
\forall x \in A  \quad \exists! y \in B  \quad(y \in f(x)).
$$


We will consider functions $$f: D\subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, so that 


$$
x = \begin{pmatrix}
x_{1} \\
\vdots \\
x_{n}
\end{pmatrix} \to y = f(x) = \begin{pmatrix}
y_{1} \\
\vdots \\
y_{m}
\end{pmatrix}.
$$



#### Examples 
1. $$f:\mathbb{R}^{2} \to \mathbb{R}$$ with $$f(x,y) = 1+xy$$.
2. $$f:\mathbb{R}^{2} \to \mathbb{R}^{3}$$ with $$f(x,y) = (e^{x}, \sin(y), y^{2}+1)$$.
3. $$f:\mathbb{R^{2}} \to \mathbb{R}$$ with $$f(x,y) = x^{2}+y^{2}$$
## Continuity

### Definition (Neighbourhood)
Given $$x \in \mathbb{R}^n$$, a set $$V$$ is called a neighbourhood of $$x$$ if there exists an open set $$U$$ such that $$x \in U \subseteq V$$. We call $$V\setminus \{ x \}$$ a punctured neighbourhood.

### Definition (Continuous function)
Let $$f : D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ with $$D$$ a neighbourhood of $$a \in D$$. We say that $$f$$ is continuous at $$a$$ if 


$$
\begin{aligned}
&\forall \varepsilon>0  \quad \exists \delta>0  \quad \Big(\lVert x-a \rVert < \delta \implies \lVert f(x) - f(a) \rVert < \varepsilon \Big) \\
\iff &\forall \varepsilon>0  \quad \exists \delta>0  \quad \Big(x \in B_{\delta}(a) \implies f(x) \in B_{\varepsilon} (f(a)) \Big) \\
\iff &\forall \varepsilon>0  \quad \exists \delta>0  \quad \Big( f(B_{\delta}(a)) \subseteq B_{\varepsilon} (f(a))\Big).
\end{aligned}
$$


#### Note
Given a set $$A$$, $$f(A) = \{ y: \exists x  \quad (y = f(x)) \} = \{ f(x): x \in D \}$$.

### Definition (Continuity on a set)
$$f:D \subseteq \mathbb{R}^{n} \to \mathbb{R}^{m}$$ is continuous on $$D$$ if it is continuous at every point of $$D$$.

#### Example 
Consider $$f:\mathbb{R}^{2}\to \mathbb{R}$$ with $$f(x,y) = x^{2}+y^{2}$$. $$f$$ is continuous on $$\mathbb{R}^{2}$$.

***Proof:*** Let $$(a,b) \in \mathbb{R}^{2}$$ and $$\varepsilon>0$$. Take $$\delta = \min \left\{  1, \frac{\varepsilon}{1+2 \lvert  a \rvert}, \frac{\varepsilon}{1+2 \lvert  b \rvert} \right\}$$. Suppose that $$\lVert (x,y) - (a,b) \rVert < \delta$$. This implies that $$\lvert x-a \rvert < \delta$$ and that $$\lvert y-b \rvert < \delta$$, since in general $$\lvert x_{j} \rvert \leq \lVert x \rVert_{\infty} \leq \lVert x \rVert_{2}$$. So 


$$
\begin{aligned}
\lVert f(x,y) - f(a,b) \rVert &\leq \lvert x-a \rvert \lvert x+a \rvert + \lvert y-b \rvert \lvert y+b \rvert \\
&< \delta (1+2 \lvert a \rvert ) + \delta(1+2 \lvert b \rvert ) \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\end{aligned}
$$



### Theorem (Continuity componentwise)
Let $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, with $$D$$ a neighbourhood of $$a$$. Then $$f = (f_{1},\dots,f_{m})$$ is continuous at $$a$$ if and only if $$f_{j}:D \to \mathbb{R}$$ is continuous at $$a$$ for every $$j \in \{ 1,\dots,m \}$$.

***Proof:*** The idea is similar to the one used in the previous example, noting that 


$$
\lvert f_{j}(x) - f_{j}(a) \rvert \leq \lVert f_{j}(x) - f_{j}(a) \rVert \leq  \sum_{j=1}^{m} \lvert f(x) - f(a) \rvert.
$$



### Theorem (Sequential criterion for continuity)
Cf. convergence of sequences (MA0350). Let $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ be a function, with $$D$$ a neighbourhood of $$a$$. Then $$f$$ is continuous at $$a$$ if and only if for every sequence $$(x_{k})_{k \in \mathbb{N}} \subseteq D$$ with $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$, we have that $$f(x_{k}) \underset{k \rightarrow \infty}{\longrightarrow} f(a)$$.

***Proof:*** ($$\implies$$): Suppose that $$f$$ is continuous at $$a$$ and let $$(x_{k})_{k \in \mathbb{N}}$$ be a sequence in $$D$$ such that $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow}a$$. We must show that $$f(x_{k}) \underset{k \rightarrow \infty}{\longrightarrow} f(a)$$. Given $$\varepsilon>0$$, note that: 
1. since $$f$$ is continuous at $$a$$, there exists $$\delta >0$$ such that if $$\lVert x-a \rVert < \delta$$ then $$\lVert f(x)-f(a) \rVert < \varepsilon$$;
2. since $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$, there exists $$N \in \mathbb{N}$$ such that for every $$k \geq N$$, $$\lVert x_{k}-a \rVert < \delta$$.
Hence, for $$k \geq N$$, by (2) we get $$\lVert f(x_{k}) - f(a) \rVert < \varepsilon$$, from which we conclude that $$f(x_{k}) \underset{k  \rightarrow \infty}{\longrightarrow} f(a)$$.
($$\impliedby$$): Suppose for contradiction that $$f$$ is not continuous at $$x=a$$, i.e., there exists $$\varepsilon>0$$ such that for every $$\delta>0$$ we have $$\lVert x-a \rVert <\delta$$ and $$\lVert f(x)-f(a) \rVert \geq \varepsilon$$. We will prove that there exists a sequence $$(x_{k})_{k \in \mathbb{N}}$$ with $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ such that, for $$k \geq 1$$, take $$\delta_{k} = \frac{1}{k}$$. Then there exists $$x_{k}$$ such that $$\lVert x_{k}-a \rVert < \frac{1}{k}$$ and $$\lVert f(x_{k}) - f(a) \rVert \geq \varepsilon$$, so $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ and $$f(x_{k}) \underset{k \rightarrow \infty}{\cancel{ \longrightarrow }} f(a)$$, a contradiction, since we assumed that every sequence satisfies the convergence of its images.

#### Corollary
If there exist sequences $$(x_{k})_{k \in \mathbb{N}}$$ and $$(y_{k})_{k \in \mathbb{N}}$$ with $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ and $$y_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ such that $$f(x_{k}) \underset{k \rightarrow \infty}{\longrightarrow} L_{1}$$, $$f(y_{k}) \underset{k \rightarrow \infty}{\longrightarrow} L_{2}$$ and $$L_{1} \neq L_{2}$$, then $$f$$ is not continuous. 

#### Example 
Consider $$f:\mathbb{R}^{2} \to \mathbb{R}$$ with 


$$
f(x,y) = \begin{cases}
\frac{x^{2}y}{x^{4}+y^{2}}, \quad  \text{if }(x,y) \neq  (0,0) \\ \\
0, \quad \text{if }(x,y) = (0,0)
\end{cases}.
$$


Is it continuous at $$(0,0)$$? Consider the sequence $$\left( \frac{1}{k}, \frac{1}{k^{2}} \right) \underset{k \rightarrow \infty}{\longrightarrow} (0,0)$$. Note that $$f\left( \frac{1}{n}, \frac{1}{n^{2}} \right) = \frac{\frac{1}{n^{2}} \cdot \frac{1}{n^{2}}}{\frac{1}{n^{4}} + \frac{1}{n^{4}}} = \frac{1}{2}$$. Therefore $$f$$ is not continuous at $$(0,0)$$. In general, evaluating $$f$$ at $$\left( \frac{k}{n}, \frac{k}{n^{2}} \right)$$ gives different limit values as $$n \longrightarrow \infty$$.

### Theorem (Characterisation of continuity by open sets)
Let $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ with $$D$$ open. Then $$f$$ is continuous on $$D$$ if and only if for every open $$B \subseteq \mathbb{R}^{m}$$ we have that $$f^{-1}(B)$$ is open.

#### Note
Recall that $$f(A) : \{ f(x) : x \in A \}$$ and that $$f^{-1}(A) = \{ x \in D: f(x) \in A \}$$.

***Proof:*** $$(\implies):$$ Suppose that $$f$$ is continuous on $$D$$. Let $$B \subseteq \mathbb{R}^{m}$$ be open. We must show that $$f^{-1}(B)$$ is open. Let $$x \in f^{-1}(B)$$. Then $$f(x) \in B$$ and $$B$$ is open, so there exists $$\varepsilon > 0$$ such that $$B_{\varepsilon}(f(x)) \subseteq B$$. Since $$f$$ is continuous, there exists $$\delta > 0$$ such that 


$$
f(B_{\delta}(x)) \subseteq B_{\varepsilon}(f(x)) \subseteq B \implies B_{\delta}(x) \subseteq f^{-1}(B),
$$


where in the last implication we used the fact that if $$A \subseteq B$$ then $$f ^{-1}(A) \subseteq f^{-1}(B)$$. We conclude that $$f^{-1}(B)$$ is open.
($$\impliedby$$): Let $$\varepsilon>0$$. We know that $$B = B_{\varepsilon}(f(x))$$ is open. By hypothesis, $$f^{-1}(B)$$ is open. Note that $$x \in f^{-1}(B)$$. Then there exists $$\delta>0$$ such that $$B_{\delta}(x) \subseteq f^{-1}(B)$$, so $$f(B_{\delta}(x)) \subseteq f(f^{-1}(B)) \subseteq B$$, since for every set $$A$$, $$f(f^{-1}(A)) \subseteq A$$. Therefore $$f$$ is continuous at $$x$$ for every $$x \in D$$.

#### Example 
Let $$f:\mathbb{R}^n\to \mathbb{R}$$ be continuous. Since $$(c,+\infty)$$ is open, $$f^{-1}((c,+\infty))$$ is open. Then $$\{ x \in \mathbb{R}^n: f(x)>c \}$$ is open. Similarly, $$\{ x:a<f(x)<b \}, \{ x:f(x)<d \}$$ are open. Moreover, $$\{ x: f(x) \leq c \}$$, $$\{ x:f(x)\geq d \}$$, $$\{ x:a\leq f(x)\leq b \}$$, $$\{ x:f(x)=c \}$$ are closed.

### Definition (Relatively open set)
Let $$D \subseteq E$$. We say that $$O \subseteq D$$ is relatively open in $$D$$ (or open in $$D$$) if there exists an open set $$U \subseteq E$$ such that $$O = U \cap D$$.

#### Example 
In $$E = \mathbb{R}$$, take $$D = [0,+\infty)$$. Then, since $$U = (-1,1)$$ is open in $$\mathbb{R}$$, $$O_{1} = [0,1)$$ and $$O_{2} = (0,1)$$ are both relatively open in $$D$$.

### Theorem (Continuity and relatively open sets)
Let $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, where $$A$$ is a neighbourhood of $$D$$ ($$D \subseteq U \subseteq A$$ with $$U$$ open). Then $$f$$ is continuous on $$D$$ if and only if for every open $$B \subseteq \mathbb{R}^{m}$$ we have that $$f^{-1}(B)$$ is relatively open in $$D$$.

***Proof:*** Exercise

### Theorem (Operations and continuity)
Let $$D \subseteq \mathbb{R}^n$$ be a neighbourhood of $$a$$ and let $$f,g: D \to \mathbb{R}^{m}$$ be continuous. Then:
1. For every $$c \in \mathbb{R}$$, $$cf$$ is continuous at $$a$$,
2. $$f \pm g$$ is continuous at $$a$$,
3. $$f \cdot g = \sum_{i=1}^{n} f_{i} g_{i}$$ is continuous at $$a$$
4. If $$f(a) \neq \bar{0}$$, there exists an open $$U$$ around $$a$$ such that $$f(x) \neq \bar{0}$$ for every $$x \in U$$.
5. If $$g:\mathbb{R}^n \to \mathbb{R}$$, $$g(a) \neq 0$$, then $$(\frac{f_{1}}{g}, \dots, \frac{f_{m}}{g})$$ is continuous at $$a$$.
6. 

***Proof:*** Exercise; it can be worked out with sequences.

### Theorem (Composition and continuity)
Let $$D \subseteq \mathbb{R}^n$$ be a neighbourhood of $$a$$, $$f:D \to E \subseteq \mathbb{R}^{m}$$ continuous at $$a$$, and $$g:E \to \mathbb{R}^{p}$$ continuous at $$f(a)$$ with $$E$$ a neighbourhood of $$f(a)$$. Then $$g \circ f: D \to \mathbb{R}^{p}$$ is continuous at $$a$$.

***Proof:*** Exercise; it can be worked out with sequences.

### Theorem (Continuity and compactness)
Let $$f:K \subseteq \mathbb{R}^{n} \to \mathbb{R}^{m}$$ be continuous and $$K$$ compact. Then $$f(k)$$ is compact

***Proof:*** Let $$\{ U_{\alpha} \}_{\alpha \in I}$$ be an open cover of $$f(K)$$. So $$f(K) \subseteq \bigcup_{\alpha \in I} U_{\alpha}$$. Since for every $$\alpha \in I$$, $$U_{\alpha}$$ is open, $$V_{\alpha} = f^{-1}(U_{\alpha})$$ is open. So $$K \subseteq \bigcup_{\alpha \in I} V_{\alpha}$$.
Since $$K$$ is compact and $$\{ V_{\alpha} \}_{\alpha \in I}$$ is an open cover, there exist $$V_{\alpha_{1}}, \dots, V_{\alpha_{m}}$$ such that $$K \subseteq \bigcup_{j=1}^{m} V_{\alpha_{j}}$$. Then $$f(K) \subseteq f\left( \bigcup_{i=1}^{m} V_{\alpha_{i}} \right) = \bigcup_{i=1}^{m} f(V_{\alpha_{i}}) = \bigcup_{i=1}^{m} U_{\alpha}$$, so $$f(K)$$ is compact.

#### Corollary
Under the same hypotheses, $$f$$ is bounded on $$K$$.

### Theorem (Compactness and extreme values)
Let $$f:K \subseteq \mathbb{R}^n\to \mathbb{R}$$ and let $$\emptyset \neq K$$ be compact. Then $$f$$ attains a maximum and a minimum on $$K$$, i.e., there exist $$x_{m}, x_{M}$$ such that for every $$x \in K$$, $$f(x_{m}) \leq f(x) \leq f(x_{M})$$.

***Proof:*** We know that $$A = \{ f(x): x \in K \}$$ is bounded and that $$A \subseteq \mathbb{R}$$. Let $$\beta = \sup A$$. Suppose there is no $$x_{M} \in K$$ with $$f(x_{M}) = \beta$$, that is, for every $$x \in K$$, $$f(x) < \beta$$. Define the continuous function $$g:K \to \mathbb{R}$$ by $$g(x) := \frac{1}{\beta-f(x)}$$. There exists $$M>0$$ such that $$g(x) \leq M$$, so that $$f(x) \leq \beta - \frac{1}{M}$$. So $$\beta-\frac{1}{M}$$ is an upper bound of $$A$$, which contradicts the fact that $$\beta$$ is the supremum. We conclude that such an $$x_{M}$$ exists. The existence of $$x_{m}$$ is proved in an analogous way.

### Theorem (Generalised intermediate value theorem)
Let $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ be continuous, with $$C$$ connected. Let $$a,b \in C$$ with $$f(a)$$ and $$f(b)$$. Then, if $$u \in \mathbb{R}$$ with $$f(a) < u <f(b)$$, there exists $$c \in C$$ such that $$f(c) = u$$.

***Proof:***  Let $$u \in (f(a),f(b))$$. Suppose that for every $$x \in C$$ we have $$f(x) \neq u$$. Let $$A = \{ x \in C: f(x) < u \}$$ and $$B \in \{ x \in C: f(x)>u \}$$. Note that:
1. $$A \cap B  = \emptyset$$,
2. $$A \cup B = \emptyset$$,
3. $$A$$ and $$B$$ are open, since they are preimages of open sets
4. $$C \cap A \neq \emptyset$$ since $$a \in C$$ and $$a \in A$$. In the same way, $$C \cap B \neq \emptyset$$.
These observations contradict the connectedness of $$C$$, from which we conclude that there exists $$c \in C$$ satisfying $$f(c) = u$$.

### Theorem (Continuity and connectedness)
Let $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ be continuous with $$C$$ connected. Then $$f(c)$$ is connected.

***Proof:***  Suppose for contradiction that $$f(C)$$ is not connected. Then there exist disjoint open sets $$A$$ and $$B$$, with $$f(C) \subseteq A \cup B$$, $$f(C) \cap A \neq \emptyset$$, and $$f(C) \cap B \neq \emptyset$$. We know that:
1. $$f^{-1}(A)$$ and $$f^{-1}(B)$$ are open by continuity.
2. $$f^{-1}(A) \cap f^{-1}(B) = \emptyset$$ (this can be proved by contradiction).
3. Since $$f(C) \subseteq A \cup B$$, we have 


$$
C \subseteq f^{-1}(f(C)) \subseteq f^{-1}(A \cup B) = f^{-1}(A) \cup f^{-1}(B).
$$


4. Since $$f(C) \cap A \neq \emptyset$$, there exists $$y$$ such that $$y \in A$$ and $$y \in f(C)$$, i.e., $$y = f(x)$$ with $$x \in C$$. Hence $$x \in C \cap f^{-1}(A)$$, so $$C \cap f^{-1}(A) \neq 0$$. Similarly, we can prove that $$C \cap f ^{-1}(B) \neq \emptyset$$.
These observations contradict the connectedness of $$f(C)$$, from which we conclude that $$C$$ is connected. 

### Definition (Uniform continuity)
Let $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$.  $$f$$ is uniformly continuous if for every $$\varepsilon>0$$ there exists $$\delta > 0$$ such that for all $$x,y \in D$$ with $$\lVert x-y \rVert < \delta$$ we have $$\lVert f(x) - f(y) \rVert < \varepsilon$$.

### Theorem (Uniform continuity on compact sets)
If $$f$$ is continuous on a compact $$K$$, then $$f$$ is uniformly continuous on $$K$$.

***Proof:*** Let $$\varepsilon>0$$. For $$a \in K$$, there exists $$\delta_{a} > 0$$ such that if $$x \in B_{\delta_{a}}(a)$$ then $$\lVert f(x) - f(a) \rVert < \frac{\varepsilon}{2}$$ (by continuity at $$a$$). Moreover, $$K \subseteq \bigcup_{a \in K} B_{\frac{\delta_{a}}{2}}(a) = B$$ is an open cover. Since $$K$$ is compact, there exist $$a_{1}, \dots, a_{N} \in K$$ such that $$K \subseteq \bigcup_{j=1}^{N} B_{\frac{\delta_{a_{j}}}{2}}(a_{j})$$. Take $$\delta = \min\left\{ \frac{\delta_{a_{1}}}{2}, \dots, \frac{\delta_{a_{N}}}{2} \right\}$$. Let $$x,y \in K$$, with $$\lVert x-y \rVert<\delta$$.
There exists $$i \in \{ 1,\dots,N \}$$ such that $$x \in B_{\frac{\delta_{a_{i}}}{2}}(a_{i}) \subseteq B_{\delta_{a_{i}}}(a_{i})$$, so $$\lVert f(x)-f(a_{i}) \rVert < \frac{\varepsilon}{2}$$
Moreover, note that 


$$
\begin{aligned}
\lVert y-a_{i} \rVert & \leq \lVert y-x \rVert + \lVert x-a_{i} \rVert \\
& < \delta + \frac{\delta_{a_{i}}}{2} \leq \frac{\delta_{a_{i}}}{2} + \frac{\delta_{a_{i}}}{2} = \delta_{a_{i}},
\end{aligned}
$$


so $$y \in B_{\delta_{a_{i}}}(a_{i})$$, from which we get $$\lVert f(y) - f(a_{i}) \rVert < \frac{\varepsilon}{2}$$.
So 


$$
\begin{aligned}
\lVert f(x) - f(y) \rVert & \leq  \lVert f(x) - f(a_{i}) \rVert +  \lVert f(a_{i}) - f(y) \rVert \\
& < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\end{aligned}
$$



## Limits

### Definition (Limit of a function)
Let $$f:V \setminus \{ a \} \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, with $$V$$ a neighbourhood of $$a$$. We say that $$\lim_{ x \to a } f(x) = L$$ if 


$$
\forall \varepsilon > 0  \quad \exists \delta>0  \quad \forall x \in V \setminus \{ a \} (0 < \lVert x-a \rVert < \delta \implies \lVert f(x) - L \rVert < \varepsilon).
$$



### Theorem (Continuity and limits)
$$f:A \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ is continuous at a point $$a$$ if and only if $$\lim_{ x \to a } f(x) = f(a)$$.

***Proof:*** This follows directly from the definitions.

### Theorem (Sequential criterion for limits)
Let $$f:V \setminus \{ a \} \to \mathbb{R}^{m}$$. The following are equivalent: 
1. $$\lim_{ x \to a } f(x) = L$$
2. For every sequence $$(x_{n})_{n \in \mathbb{N}} \subseteq V \setminus \{ a \}$$ with $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} a$$, we have that $$f(x_{n}) \underset{n \rightarrow \infty}{\longrightarrow} L$$.

***Proof:*** The same as for continuity.

### Note (Algebraic operations on limits)
The results about $$+,-,\cdot$$ carry over to limits.

#### Example 
Consider $$f(x,y) = (x^{2} + y^{2}) \sin\left( \frac{1}{x^{2}+y^{2}} \right)$$. Compute $$\lim_{ (x,y) \to (0,0) } f(x,y)$$.
We conjecture that the limit is zero. Given $$\varepsilon>0$$, take $$\delta = \sqrt{ \varepsilon }$$. Suppose that $$\lVert (x,y) \rVert < \delta$$. Then 


$$
\left\lvert  (x^{2}+y^{2})\underbrace{ \sin\left( \frac{1}{x^{2}+y^{2}} \right) }_{ \leq 1 }  \right\rvert \leq \lVert (x,y) \rVert^{2} < \delta^{2} = \varepsilon. 
$$



#### Example 
Consider $$f:\mathbb{R}^{2} \to \mathbb{R}$$ such that 


$$
f(x,y) = \begin{cases}
\frac{x^{3}+y^{3}}{x+y}, \quad  \text{if }x\neq  y \\
x  \quad  \quad  \quad \text{if }x = -y
\end{cases}.
$$


Determine the points where the limit does not exist.
We conjecture that the limit does not exist at the points $$(-a,a)$$.
1. Let $$(x_{n},y_{n}) = \left( a+\frac{1}{n}, -\left( a+\frac{1}{n} \right) \right) \underset{n \rightarrow \infty}{\longrightarrow} (a,-a)$$. Then $$f(x_{n},y_{n}) = a+\frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} a$$.
2. Let $$(\hat{x}_{n}, \hat{y}_{n}) = \left( a+\frac{1}{n}, -a+\frac{1}{n} \right) \underset{n \rightarrow \infty}{\longrightarrow} (a,-a)$$. Then $$f(\hat{x}_{n}, \hat{y}_{n}) = \left( a+\frac{1}{n} \right)^{2} - \left( a + \frac{1}{n} \right)\left( -a+\frac{1}{n} \right) + \left( -a+\frac{1}{n} \right)^{2} \underset{n \rightarrow \infty}{\longrightarrow} 3a^{2}$$.
Note that $$3a^{2} = a$$ if and only if $$a = 0$$ or $$a = \frac{1}{3}$$, so it remains to prove that the limit exists at these points. It is also necessary to prove that the limit exists at the points $$(a,b)$$ with $$a \neq -b$$ (exercise).
{% endraw %}
