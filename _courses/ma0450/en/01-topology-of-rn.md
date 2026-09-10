---
layout: chapter
course: ma0450
chapter: 1
title: "Topology of Rn"
slug: 01-topology-of-rn
toc:
  sidebar: right
lang: en
fecha: 2025-08-11
permalink: /notes/ma0450/01-topology-of-rn/
---

{% raw %}
## Preliminaries
### Definition ($$\mathbb{R}^{n}$$)


$$
\begin{aligned}
\mathbb{R}^{n} :&= \mathbb{R} \times \mathbb{R} \times \dots \times \mathbb{R} \\
&= \{ (x_{1},x_{2},\dots,x_{n}): x_{i} \in \mathbb{R} \quad  \forall 1 \leq i \leq  n \}
\end{aligned}
$$


We write $$\bar{x} = (x_{1},\dots,x_{n}) \in \mathbb{R}^{n}$$. We have two operations, which make it a vector space: 


$$
\begin{aligned}
\bar{x} + \bar{y} &= (x_{1}+y_{1},\dots,x_{n}+y_{n}) \\
\alpha \bar{x} &= (\alpha x_{1}, \dots, \alpha x_{n}).
\end{aligned}
$$



### Definition (Norm)
Given a vector space $$E$$ over $$\mathbb{R}$$, a norm is an operation $$\lVert \cdot \rVert: E \to \mathbb{R}$$ such that 
1. $$\forall x \in E \quad (\lVert x \rVert \geq 0  \quad \land  \quad \lVert x \rVert = 0 \iff x=0)$$.
2.  $$\forall x \in E \quad \forall \alpha \in \mathbb{R} \quad  (\lVert \alpha x \rVert = \lvert \alpha \rvert \lVert x \rVert)$$.
3. $$\forall x,y \in E \quad (\lVert x+y \rVert \leq \lVert x \rVert+ \lVert y \rVert)$$.

#### Example 
On $$\mathbb{R}$$ the absolute value is a norm.

### Definition (Normed vector space)
A v.s. with a norm $$\lVert \cdot \rVert$$ is called a normed v.s. and is denoted $$(E, \lVert \cdot \rVert)$$.

### Definition (Inner product)
Given a v.s. $$E$$ over $$\mathbb{R}$$, an inner product is a map $$\langle \cdot,\cdot \rangle : E \times E \to \mathbb{R}$$ such that 
1. $$\langle x, y \rangle = \langle y, x \rangle$$.
2. $$\langle x, y_{1}+y_{2} \rangle = \langle x, y_{1}\rangle +  \langle x, y_{2}\rangle$$.
3. $$\langle x, \lambda y \rangle = \lambda \langle x, y \rangle \quad \forall \lambda \in \mathbb{R}$$.
4. $$\langle x, x \rangle \geq 0$$ and if $$x \neq 0$$ then $$\langle x, x \rangle > 0$$.

#### Remark 1


$$
\begin{aligned}
\langle x_{1}+x_{2},y \rangle &= \langle y, x_{1}+x_{2} \rangle  \\
&= \langle y, x_{1} \rangle + \langle y,x_{2} \rangle \\
&= \langle x_{1},y \rangle + \langle x_{2},y \rangle.
\end{aligned}
$$



#### Remark 2


$$
\langle 0,0+0 \rangle = \langle 0,0 \rangle + \langle 0,0 \rangle \implies \langle 0,0 \rangle = 0.
$$



#### Example 
On $$\mathbb{R}^{n}$$, $$\langle x,y \rangle = x \cdot y = \sum_{i=1}^{n} x_{i} y_{i}$$ is an inner product (exercise).

### Lemma (Cauchy-Schwarz)
For all $$x, y \in E$$, we have that $$\langle x,y \rangle^{2} \leq \langle x,x \rangle \cdot \langle y,y \rangle$$.

***Proof:*** By property 3 of the inner product, for every $$\lambda \in \mathbb{R}$$ we have that


$$
\begin{aligned}
0 &\leq \langle x+\lambda y, x + \lambda y \rangle \\
&= \langle x,x \rangle + 2 \lambda \langle x,y \rangle + \lambda^{2} \langle y,y \rangle = f(\lambda).
\end{aligned}
$$


Note that $$f(\lambda)$$ is quadratic and its discriminant is necessarily less than or equal to zero (by property 4 of the inner product). The discriminant is given by 


$$
4 \langle x,y \rangle^{2} - 4 \langle x,x \rangle \langle y,y \rangle \leq  0
\iff \langle x,y \rangle^{2} \leq \langle x,x \rangle \langle y,y \rangle. 
$$


 
#### Example (The 2-norm)
Given an inner product $$\langle \cdot, \cdot \rangle$$,  $$\lVert x \rVert = \sqrt{ \langle x,x \rangle }$$ is a norm.

***Proof:*** We prove each property
1. $$\lVert x \rVert\geq 0$$ and $$\lVert x \rVert = 0 \iff \langle x,x \rangle = 0 \iff x=0$$. 
2. $$\lVert \lambda x \rVert = \sqrt{ \langle \lambda x, \lambda x \rangle } = \sqrt{ \lambda^{2} \langle x, x \rangle } = \lvert \lambda \rvert \lVert x \rVert$$.
3. 

$$
\begin{aligned}
\lVert x+y \rVert^{2} &= \langle x+y, x+y\rangle \\
&= \langle x,x \rangle + 2 \langle x,y \rangle + \langle y,y \rangle  \\
&= \lVert x \rVert^{2}+ 2 \langle x,y \rangle  + \lVert y \rVert^{2} \\
&\leq_{C.S.} \lVert x \rVert^{2}+2 \lVert x \rVert \lVert y \rVert + \lVert y \rVert^{2} \\
&= ( \lVert x \rVert + \lVert y \rVert)^{2}.
\end{aligned}
$$


Every inner product induces a norm.

#### Remark
On $$\mathbb{R}^{n}$$, with $$\langle x,y \rangle = \sum_{i=1}^{n} x_{i} y_{i}$$, 


$$
\lVert x \rVert = \sqrt{ \langle x,x \rangle  } = \sqrt{ \sum_{i=1}^{n} x_{i}^{2} } = \lVert x \rVert_{2}
$$


![norma](/assets/img/courses/ma0450/norma.svg)
#### Example 
On $$\mathbb{R}^{n}$$, given $$x = (x_{1},..., x_{n})$$, the following are norms:
1. $$\lVert x \rVert_{1} := \sum_{i=1}^{n} \lvert x_{i} \rvert$$,
2. $$\lVert x \rVert_{\infty} := \underset{1\leq j\leq n}{\max} \lvert x_{j} \rvert$$
3.  $$\lVert x \rVert_{p} := \left\lvert  \sum_{i=1}^{n} \lvert x_{i}^{p} \rvert  \right\rvert^{1/p}$$.
By convention, the 2-norm is used throughout the course unless stated otherwise.
### Definition (Equivalent norms)
Given norms $$\lVert \cdot \rVert_{a}$$ and $$\lVert \cdot \rVert_{b}$$, they are said to be equivalent if there exist $$\alpha, \beta >0$$ such that for every $$x \in E$$, 


$$
\alpha \lVert x \rVert_{a} \leq \lVert x \rVert_{b} \leq  \beta \lVert x \rVert_{a}.
$$



#### Example 


$$
\begin{aligned}
\lVert x \rVert_{2} &\leq \lVert x\rVert_{1} \leq  \sqrt{ n } \lVert x \rVert_{2} \\
\lVert x \rVert_{\infty} &\leq \lVert x \rVert_{2} \leq  \sqrt{ n } \lVert x \rVert_{\infty} \\
\lVert x \rVert_{\infty} &\leq \lVert x \rVert_{1} \leq  n \lVert x \rVert_{\infty} 
\end{aligned}
$$



#### Example 
Each norm defines a different geometry: 
1. $$B_{2} = \{ x \in \mathbb{R}^{2}: \lVert x \rVert_{2} = 1\}$$
![Norma2](/assets/img/courses/ma0450/Norma2.svg)
2.  $$B_{1} = \{ x \in \mathbb{R}^{2}: \lVert x \rVert_{1} = 1\}$$
![Norma1](/assets/img/courses/ma0450/Norma1.svg)
3.  $$B_{\infty} = \{ x \in \mathbb{R}^{2}: \lVert x \rVert_{\infty} = 1\}$$
![NormaInf](/assets/img/courses/ma0450/NormaInf.svg)

#### Example 
On $$E = C([a,b], \mathbb{R})$$, $$\langle f,g \rangle = \int_{a}^{b} f(x)g(x) \, dx$$ is an inner product and its induced norm is $$\lVert f \rVert = \sqrt{ \langle f,f \rangle } = \sqrt{ \int_{a}^{b} \lvert f \rvert^{2} \, dx }$$.

### Lemma (Parallelogram law)
In a v.s. with an inner product, the induced norm satisfies 


$$
\lVert x+y \rVert^{2} + \lVert x-y \rVert^{2} = 2 \lVert x \rVert^{2}+2 \lVert y \rVert^{2} \ \tag{*}
$$


***Proof:*** Exercise.

#### Note
In a normed v.s., there does not necessarily exist an inner product associated with each norm.

### Lemma (Inner product from a norm) 
In a normed v.s., $$\langle \cdot, \cdot \rangle$$ can be defined from $$\lVert \cdot \rVert$$ if and only if the parallelogram law holds. In that case, 


$$
\langle x,y \rangle = \frac{1}{4}[ \lVert x+y \rVert^{2} - \lVert x-y \rVert^{2} ].
$$



#### Example 
$$\lVert x \rVert_{\infty}$$ on $$\mathbb{R}^{n}$$ does not satisfy $$(*)$$.

### Definition (Distance)
A distance is a function $$d(\cdot,\cdot): E \times E \to \mathbb{R}$$ such that 
1. $$d(x,y) = 0 \iff x=y$$,
2. $$d(x,y) = d(y,x)$$
3. $$d(x,z) \leq d(x,y) + d(y,z)$$.

#### Note
Every norm induces the distance $$d(x,y) = \lVert x-y \rVert$$. On $$\mathbb{R}^{n}$$, the distance is given by 
$$d(x,y) = \lVert x-y \rVert_{2} = \left( \sum_{i=1}^{n} (x_{i} - y_{i})^{2} \right)^{1/2}.$$

## Open and closed sets (in $$\mathbb{R}^{n}$$)
 
### Definition (Open and closed balls)
Given $$a \in \mathbb{R}^{n}, r \in \mathbb{R}$$:
1. The open ball with centre $$a$$ and radius $$r$$ is 


$$
B_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a \rVert < r \}
$$


2. and the closed ball with centre $$a$$ and radius $$r$$ is


$$
\bar{B}_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a \rVert \leq  r \}.
$$


#### Example 
![intervalo](/assets/img/courses/ma0450/intervalo.svg)
On $$\mathbb{R}$$ every interval $$(c,d)$$ is an open ball, taking $$a = \frac{c+d}{2}, r= \frac{d-c}{2} >0$$, since 


$$
\lvert x-a \rvert < r \iff a-r = c < x < d = a+r.
$$


In an analogous way, every interval $$[c,d]$$ is a closed ball.

#### Example
1. In $$\mathbb{R}^{2}$$:
![bola R2](/assets/img/courses/ma0450/bola%20R2.svg)

2. In $$\mathbb{R}^{3}$$:
![bola R3](/assets/img/courses/ma0450/bola%20R3.svg)
### Definition (interior point and open set)
Given a set $$A \subseteq \mathbb{R}^{n}$$,
1. we say that $$a \in A$$ is an interior point of $$A$$ if there exists a ball $$B_{\delta}(x)$$ with $$a \in B_{\delta}(x)$$ such that $$B_{\delta}(x) \subseteq A$$,
2. we define $$A^{0} = \{ a \in A: a \text{ is an interior point} \}$$,
3. $$A$$ is open if $$A = A^{0}$$, i.e., if  


$$
\forall x \in A  \quad \exists \delta>0  \quad(B_{\delta}(x) \subseteq A)
$$


![conjunto abierto](/assets/img/courses/ma0450/conjunto%20abierto.svg)

#### Example 
$$A = (0,1)$$ is open in $$\mathbb{R}$$ but $$A = [0,1)$$ is not. (draw it)

### Lemma (Open ball $$\implies$$ open set)
Every open ball $$B_{r}(a)$$ is an open set.

***Proof:*** Let $$x \in B_{r}(a)$$. Take $$0 < \delta < r - \lVert x-a \rVert$$. We know that $$\lVert x-a \rVert < r$$. 
Let us see that $$B_{\delta}(x) \subseteq B_{r}(a)$$. Let $$y \in B_{\delta}(x)$$; then $$\lVert x-y \rVert < \delta$$. We must show that $$y \in B_{r}(a)$$, i.e., $$\lVert y-a \rVert < r$$. Note that 


$$
\begin{aligned}
\lVert y-a \rVert &\leq \lVert y-x \rVert + \lVert x-a \rVert \\
&< \delta + (r-\delta) = r.
\end{aligned}
$$


![bola es conjunto abierto](/assets/img/courses/ma0450/bola%20es%20conjunto%20abierto.svg)

### Definition (closed set)
A set $$F \subseteq \mathbb{R}^{n}$$ is called closed if $$F^{C}$$ is open.
 
#### Example
Note that $$\mathbb{R}^{n}$$ is open, since if $$x \in \mathbb{R}^{n}$$, take $$-$$ and then $$B_{\delta}(x) \subseteq \mathbb{R}^{n}$$. $$\mathbb{R}^{n}$$ is also closed, since $$(\mathbb{R}^{n})^{C} = \emptyset$$ is open vacuously. Hence $$\mathbb{R}^{n}$$ and  $$\emptyset$$ are both open and closed (*clopen*).

#### Example 
$$A = [0,1)$$ is not open since $$0$$ is not an interior point. It is also not closed, since its complement $$(-\infty, 0) \cup  [1,\infty)$$ is not open (consider $$x=1$$). 

#### Example 
A closed ball $$\bar{B}_{r}(a)$$ is a closed set.
Recall that $$\bar{B}_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a \rVert \leq r \}$$. Let $$x \in (\bar{B}_{r}(a))^{C}$$. Take $$0<\delta< \lVert x-a \rVert-r$$ (which makes sense since $$\lVert x-a \rVert>r$$).
Let $$y \in B_{\delta}(x)$$. We must show that $$y \in (\bar{B}_{r}(a))^{C}$$. Since 


$$
\begin{aligned}
\delta + r < \lVert x-a \rVert &\leq \lVert x-y \rVert + \lVert y-a \rVert \\
& < \delta + \lVert y-a \rVert 
\end{aligned}
$$


we get $$r < \lVert y-a \rVert$$, from which we conclude that $$y \not\in \bar{B}_{r}(a)$$.
![bola cerrada es cerrado](/assets/img/courses/ma0450/bola%20cerrada%20es%20cerrado.svg)
### Definition (Exterior point and boundary point)
1. We say that $$x$$ is an exterior point of $$A$$ if it is an interior point of $$A^{C}$$, that is, the set of exterior points is $$(A^{C})^{0}$$.
2. $$x$$ is a boundary point if 


$$
\forall \delta > 0  \quad(B_{\delta}(x) \cap A \neq  \emptyset  \quad\land  \quad B_{\delta}(x) \cap A^{C} \neq  \emptyset).
$$


We denote $$\partial A = \{ \text{boundary points of }A \}$$.
![ext front int](/assets/img/courses/ma0450/ext%20front%20int.svg)

#### Example 
$$A = [0,1)$$ is not open (since for $$x=0$$ there is no $$\delta>0$$ with $$B_{\delta}(0) \subseteq A$$. Note that 


$$
A^{0} = (0,1), \quad \partial A = \{ 0,1 \}, \quad (A^{C})^{0} = (-\infty,0) \cap(1,+\infty).
$$



#### Example 
Given $$a \in \mathbb{R}^{n}$$, $$r>0$$, $$\partial B_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a = r\rVert \}$$.

***Proof:*** "$$\supseteq$$" Let $$x \in \mathbb{R}^{n}$$ be such that $$\lVert x-a \rVert=r$$. Let us see that $$x \in \partial B_{r}(a)$$. Let $$\delta>0$$.
1. We find $$z \in B_{\delta}(x) \cap (B_{\delta}(a))^{C}$$. Take $$\bar{z} = \bar{a} + \left( 1 + \frac{\delta}{2r} \right) (\bar{x}-\bar{a})$$. Then 


$$
\lVert z-a \rVert = \left\lVert  \left( 1+\frac{\delta}{2r} \right)(x-a)  \right\rVert = r +\frac{\delta}{2} > r.
$$


Hence $$z \in (B_{r}(a))^{C}$$. Moreover $$\lVert z-x \rVert = \frac{\delta}{2} < \delta$$, so $$z \in B_{\delta}(x)$$. We conclude that  $$z \in B_{\delta}(a) \cap (B_{\delta}(a))^{C}$$.
![Frontera bola 1](/assets/img/courses/ma0450/Frontera%20bola%201.svg)
2. We want $$y \in B_{\delta}(x) \cap B_{r}(a)$$. If $$r > \frac{\delta}{2}$$, take $$\bar{y} = \bar{a} + \left( 1-\frac{\delta}{2r} \right)(\bar{x}-\bar{a})$$. Then 


$$
\lVert y-a \rVert = \left\lvert  1-\frac{\delta}{2r}  \right\rvert r = \left\lvert  r-\frac{\delta}{2}  \right\rvert = r-\frac{\delta}{2} < r.
$$


So $$y \in B_{r}(a)$$. Moreover,


$$
\lVert y-x \rVert = \frac{\delta}{2r} \lVert x-a \rVert = \frac{\delta}{2} < \delta.
$$


So $$y \in B_{\delta}(x)$$. Therefore, if $$r> \frac{\delta}{2}$$, $$y \in B_{\delta}(x) \cap B_{r}(a)$$.
![Frontera bola 2](/assets/img/courses/ma0450/Frontera%20bola%202.svg)
Now, if $$r< \frac{\delta}{2}$$, take $$y = a$$. Clearly $$y \in B_{r}(a)$$. Moreover 


$$
\lVert y-x \rVert = \lVert a-x \rVert  = r \leq \frac{\delta}{2} < \delta,
$$


so $$y \in B_{\delta}(x)$$. We conclude that $$y \in B_{\delta}(x) \cap B_{r}(a)$$.
![Frontera bola 3](/assets/img/courses/ma0450/Frontera%20bola%203.svg)
"$$\subseteq$$": Let $$x$$ be a boundary point of $$B_{r}(a)$$.  If $$\lVert x-a \rVert > r$$ there exists $$\delta>0$$ such that $$B_{\delta}(x) \cap B_{r}(a) = \emptyset$$, a contradiction. If $$\lVert x-a \rVert < r$$, there exists $$\delta > 0$$ such that $$B_{\delta}(x) \cap (B_{r}(a))^{C} = \emptyset$$, a contradiction. We conclude that $$\lVert x-a \rVert = r$$.

### Definition (Closure)
The closure of a set $$A$$ is $$\bar{A} = A \cup \partial A$$.

### Lemma (Complement of the closure and interior points of the complement)
$$(\bar{A})^{C} = (A^{C})^{0}$$  and $$\overline{(A^{c})} = (A^{0})^{C}$$

***Proof:*** "$$\subseteq$$" Let $$x \in (\bar{A})^{C}$$. Then $$x \in (A \cup \partial A)^{C}$$, that is, $$x \not\in A$$ and $$x \not\in \partial A$$.  Since $$x \not\in \partial A$$, by definition there exists $$\delta>0$$ such that $$B_{\delta}(x) \cap A = \emptyset$$ or $$B_{\delta}(x) \cap A^{c} = \emptyset$$. Note that the latter is impossible, since $$x \in A^{c}$$ and $$x \in B_{\delta}(x)$$. Hence 


$$
\begin{aligned}
&B_{\delta}(x) \cap A = \emptyset \\
&\implies B_{\delta}(x) \subseteq A^{c}\\
&\implies x \text{ is an interior point of } A^{c} \\
&\implies x \in (A^{c})^{0}.
\end{aligned}
$$


"$$\supseteq$$" Let $$x \in (A^{c})^{0}$$. Then $$x$$ is an interior point of $$A^{c}$$, so there exists $$\delta>0$$ such that $$B_{\delta}(x) \subseteq A^{c}$$. So $$x \not\in A$$ (since $$x \in B_{\delta}(x) \subseteq A^{c}$$) and $$x \not\in \partial A$$ (since $$B_{\delta}(x) \cap A = \emptyset$$). We conclude that $$x \in (\bar{A})^{C}$$.

![Cerradura y complemento](/assets/img/courses/ma0450/Cerradura%20y%20complemento.svg)

(prove part ii as a moral exercise) 
### Theorem (Interiors, closure and subsets)
Let $$A$$ be a set. Then:
1. $$A^{\circ}$$ is open and it is the largest open set contained in $$A$$, that is 


$$
\forall U  \quad(U \subseteq A  \quad\land  \quad U \text{ open} \implies U \subseteq A^{\circ}).
$$


2. $$\bar{A}$$ is closed and it is the smallest closed set containing $$A$$, i.e., 


$$
\forall F  \quad (F\supseteq A  \quad\land  \quad F \text{ closed} \implies \bar{A} \subseteq F).
$$



***Proof:*** 1. We first prove that $$A^{\circ}$$ is open. Let $$a \in A^{\circ}$$. We must show that there is an open ball containing $$a$$ that is contained in $$A^{\circ}$$. Since $$a \in A^{\circ}$$ is an interior point, there exists $$\delta>0$$ with $$B_{\delta}(a) \subseteq A$$. Since $$B_{\delta}(a)$$ is open, for every $$x \in B_{\delta}(a)$$ there exists $$\eta > 0$$ such that $$B_{\eta}(x) \subseteq B_{\delta}(a) \subseteq A$$. So every $$x \in B_{\delta}(a)$$ is an interior point of $$A$$ (since it lies inside $$B_{\eta}(x)$$ and therefore belongs to $$B_{\delta}(a)$$). Hence $$B_{\delta}(a) \subseteq A^{\circ}$$. We conclude that $$A^{\circ}$$ is open.
We now prove that $$A^{\circ}$$ is the largest open set contained in $$A$$. Let $$U \subseteq A$$ with $$U$$ open. Let $$u \in U$$. Since $$U$$ is open, there exists $$\delta>0$$ such that $$B_{\delta}(u) \subseteq U \subseteq A$$ and so $$u$$ is an interior point of $$A$$, i.e., $$U \in A^{\circ}$$.

For 2., we first prove that $$\bar{A}$$ is closed. We know that $$(\bar{A})^{c} = (A^{c})^{\circ}$$. By the previous point, $$(A^{c})^{\circ} = (\bar{A})^{c}$$ is open and therefore $$\bar{A}$$ is closed. 
We now prove that $$\bar{A}$$ is the largest closed set contained in $$A$$. Let $$F \supseteq A$$, with $$F$$ closed. Note that $$F^{c} \subseteq A^{c}$$ and, since $$F^{c}$$ is open, by the result proved in 1. we have $$F^{c} \subseteq (A^{c})^{\circ} = (\bar{A})^{c}$$. Hence $$F \supseteq \bar{A}$$.

### Theorem (On unions and intersections of open sets)
1. $$\emptyset$$ and $$\mathbb{R}^{n}$$ are open (and closed).
2. An arbitrary union of open sets is open.
3. A <u>finite</u> intersection of open sets is open

***Proof:*** The first point was already proved. 
For 2, let $$\{ U_{k} \}_{k \in I}$$ be an arbitrary collection of open sets. Define $$U = \bigcup_{k \in I} U_{k}$$. Let $$x \in U$$. Then there exists $$\alpha_{j} \in I$$ such that $$x \in U_{\alpha_{j}}$$ (since $$x$$ belongs to the union, it must belong to at least one of the sets). Since $$U_{\alpha_{j}}$$ is open, there exists $$\delta>0$$ such that $$B_{\delta}(x) \subseteq U_{\alpha_{j}} \subseteq U$$, from which we conclude that $$U$$ is open.

For 3, let $$\{ U_{j} \}_{i=1}^{n}$$ be open. Let $$U = \bigcap_{j=1}^{n} U_{j}$$. Let $$x \in U$$. So $$x \in U_{j}$$ for every $$j \in \{ 1,\dots,n \}$$. Since $$U_{j}$$ is open, there exists $$\delta_{j}>0$$ such that $$B_{\delta_{j}}(x) \subseteq U_{j}$$. Take $$\delta = \min \{ \delta_{1},\dots, \delta_{n} \}$$. Note that $$B_{\delta}(x) \subseteq B_{\delta_{j}}(x) \subseteq U_{j}$$ for every $$j$$. Hence $$B_{\delta}(x) \subseteq U$$ and we conclude that $$U$$ is open.

#### Example 
Let us look for open sets $$\{U_{j}\}_{j=1}^{\infty}$$ such that $$\bigcap_{j=1}^{\infty} U_{j}$$ is not open. In $$\mathbb{R}$$, note that the sets $$U_{j} = \left( -\frac{1}{j}, \frac{1}{j} \right)$$ are open and that $$\bigcap_{j=1}^{\infty} U_{j} = \{ 0 \}$$, and $$\{ 0 \}$$ is closed (we can see that its complement $$(-\infty,0)  \cup (0,+\infty)$$ is open since it is a union of two open sets).

#### Example 
Is $$\mathbb{N}$$ closed in $$\mathbb{R}$$? It is clearly not open (consider a ball of size $$\frac{1}{2}$$). Note that $$\mathbb{N}^{c} = (-\infty, 0) \cap [\bigcup_{k=0}^{\infty} (k,k+1)]$$, which is open since it is a union of open sets. We conclude that $$\mathbb{N}$$ is closed.

### Theorem (On unions and intersections of closed sets)
1. An arbitrary intersection of closed sets is closed.
2. A finite union of closed sets is closed.

***Proof:*** For 1, let $$\{ F_{\alpha} \}_{\alpha \in I}$$ be a family of closed sets and let $$F = \bigcap_{\alpha \in I} F_{\alpha}$$. Then $$F^{c} = \bigcup_{\alpha \in I} F_{\alpha}^{c}$$ is open since $$F_{\alpha}^{c}$$ is open for every $$\alpha \in I$$. We conclude that $$F$$ is closed. For 2, similarly, $$\left( \bigcup_{j=1}^{n} F_{j} \right)^{c} = \bigcap_{j=1}^{n} F_{j}^{c}$$.

#### Example 
Take $$F_{n} = [\frac{0,1}{n]}$$, which are closed. Then $$\bigcap_{n=1}^{\infty} F_{n} = \{ 0 \}$$ is closed.

#### Example 
 $$\mathbb{Z}$$ is closed in $$\mathbb{R}$$.

### Definition (accumulation point and isolated point) 
1. A point $$p$$ is said to be an accumulation point of $$A$$ if 


$$
\forall\delta>0  \quad(B_{\delta}(p) \setminus \{ p \} \cap A \neq  \emptyset)
$$


We denote $$A' = \{ \text{accumulation points of }A \}$$.
2.A point $$p \in A$$ is called isolated if 


$$
\exists \delta>0  \quad (B_{\delta}(p) \setminus \{ p \} \cap A = \emptyset ).
$$



#### Example 
In $$\mathbb{N}$$, every point is isolated, taking $$\delta=\frac{1}{2}$$. Then, for $$n \in \mathbb{N}$$, $$B_{\delta}(n) = \left( n-\frac{1}{2}, n +\frac{1}{2} \right)$$ and $$B_{\delta}(n) \setminus \{ n \} \cap \mathbb{N} = \emptyset$$.

#### Example 
For $$A=[0,1]$$, $$A' = [0,1]$$.
#### Example 
For $$A = \{ 0 \}$$, $$A' = \emptyset$$.
#### Example 
In $$\mathbb{R}^{2}$$, consider $$A = \left\{  \frac{1}{m}, \frac{1}{n} : m,n \in \mathbb{N}^{*}  \right\}$$. Every point of $$A$$ is isolated (exercise). Moreover, $$A'= \{ (0,0) \}$$, since if $$(x,y) \neq (0,0)$$ it cannot be an accumulation point, because such a $$\delta$$ always exists. For $$(0,0)$$ it can, since by the Archimedean property there always exist $$m,n$$ such that $$\left\lVert  \frac{1}{m}, \frac{1}{n}  \right\rVert < \delta$$.
### Theorem (Closed sets and accumulation points)
$$F$$ is closed if and only if every accumulation point of F belongs to F.

***Proof:*** ($$\implies$$): Suppose that $$F$$ is closed. Let $$a$$ be an accumulation point of $$F$$ and suppose for contradiction that $$a \not\in F$$, i.e., $$a \in F^{c}$$. Note that $$F^{c}$$ is open, i.e., there exists $$\delta>0$$ such that $$B_{\delta}(a) \subseteq F^{c}$$. Then $$B_{\delta}(a) \cap F = \emptyset$$, and hence $$B_{\delta}(a) \setminus \{ a \} \cap F = \emptyset$$, which contradicts the definition of an accumulation point. We conclude then that $$a \in F$$.
($$\impliedby$$): Suppose that $$F$$ is a set containing all of its accumulation points. Suppose for contradiction that $$F$$ is <u>not</u> closed. So $$F^{c}$$ is not open, that is, there exists $$a \in F^{c}$$ such that for every $$\delta>0$$, $$B_{\delta}(a) \not\subseteq F^{c}$$, that is, there are points $$x \in B_{\delta}(a) \cap F$$. Since $$a \not\in F$$ we get $$(B_{\delta}(a)\setminus \{ a \}) \cap F \neq \emptyset$$. Hence $$a$$ is an accumulation point, and so $$a \in F$$, a contradiction since we assumed $$a \not\in F$$.

## Compactness

### Definition (Open cover and compact set)
1. A collection of open sets $$\{ U_{\alpha} \}_{\alpha \in I}$$ is called an open cover of $$A$$ if $$A \subseteq \bigcup_{\alpha \in I} U_{\alpha}$$. 
2. A is called compact if for every open cover $$\{ U_{\alpha} \}$$ of $$A$$ there exist $$\{U_{\alpha_{1}}, U_{\alpha_{2}}, \dots U_{\alpha_{m}}\}$$ (a finite subcover) such that $$A \subseteq \bigcup_{j=1}^{n} U_{\alpha_{j}}$$.

#### Example 
In $$\mathbb{R}^{n}$$, one cover of $$\mathbb{R}^{n}$$ is $$U_{\alpha} = R_{1}(\alpha)$$, $$\alpha \in \mathbb{R}^{n}$$.

#### Example 
$$\mathbb{R}$$ is not compact. If $$\mathbb{R}$$ were compact, since $$\mathbb{R} \subseteq \bigcup_{n \in \mathbb{N}}(-n,n)$$ is an open cover of $$\mathbb{R}$$, there would exist $$n_{1},\dots,n_{m} \in \mathbb{N}$$ such that 


$$
\mathbb{R} \subseteq \bigcup_{j=1}^{m} (-n_{j}, n_{j}) \subseteq (
-M,M)
$$


with $$M = \max \{ n_{1}, \dots, n_{m} \}$$, a contradiction.

#### Example 
$$(0,1)$$ is not compact. Take $$(0,1) \subseteq \bigcup_{n=1}^{\infty} \left( \frac{1}{n}, 1 \right)$$. If it were compact, there would exist $$n_{1}, \dots, n_{m} \in N^{\ast}$$ such that 


$$
(0,1) \subseteq \bigcup_{j=1}^{n} \left( \frac{1}{n_{j}},1 \right) = \left( \frac{1}{M}, 1 \right)
$$


with $$M = \max \{ n_{1}, \dots, n_{m} \}$$, a contradiction.

#### Example 
$$[a,b]$$ is compact. 

***Proof:***  Let $$\{ U_{\alpha} \}_{\alpha \in J}$$ be an open cover of $$[a,b]$$, that is, $$[a,b] \subseteq \bigcup_{\alpha \in J} U_{\alpha}$$. For contradiction, suppose that there is no finite subcover. Define $$I_{1} = [a,b]$$. Consider the partition $$\{ [a, \frac{a+b}{2}], [\frac{a+b}{2}, b] \}$$ of $$[a,b]$$. At least one of these subintervals has no finite subcover (if both had one, there would be a finite subcover for $$[a,b]$$). Call this subinterval $$I_{2} \supseteq I_{1}$$. Recursively, define $$\{ I_{j} \}_{j=1}^{\infty}$$ such that $$I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots$$ are closed and $$I_{j}$$ has no finite subcover for every $$j$$. By the nested interval theorem, there exists $$x \in \bigcap_{j=1}^{\infty} \subseteq [a,b] \subseteq \bigcup_{\alpha \in J} U_{\alpha}$$.  Then there exists some $$\alpha \in J$$ such that $$x \in U_{\alpha}$$. Moreover, since $$U_{\alpha}$$ is open, there exists $$\delta>0$$ such that $$B_{\delta}(x) \subseteq U_{\alpha}$$. Moreover, note that $$\lvert I_{j} \rvert \underset{j \rightarrow \infty}{\longrightarrow} 0$$. So there exists $$I_{N} \subseteq B_{\delta}(x) \subseteq U_{\alpha}$$, i.e., $$I_{N}$$ has a finite subcover, a contradiction since we assumed the $$\{ I_{j} \}_{j=1}^{\infty}$$ had none. 
#### Example (A finite set is compact)
Every finite set $$A = \{ x_{1},\dots,x_{n} \}$$ is compact.

***Proof:*** Let $$\{ U_{\alpha} \}_{\alpha \in I}$$ be an open cover of $$A$$, i.e., $$A \subseteq \bigcup_{\alpha \in I} U_{\alpha}$$. For $$j \in \{ 1,\dots,n \}$$, since $$x_{j} \in A \subseteq \bigcup_{\alpha \in I} U_{\alpha}$$, there exists $$\alpha_{j} \in I$$ such that $$x_{j} \in U_{\alpha_{j}}$$. Take the finite subcover $$\{ U_{\alpha_{1}}, \dots, U_{\alpha_{n}} \}$$. So $$A \subseteq \bigcup_{j=1}^{n} U_{\alpha_{j}}$$.
![conjunto finito es compacto](/assets/img/courses/ma0450/conjunto%20finito%20es%20compacto.svg)

### Lemma (A closed subset of a compact set is compact) 
Let $$K$$ be compact and $$F \subseteq K$$ with $$F$$ closed. Then $$F$$ is compact. 

***Proof:*** Let $$\{ U_{\alpha} \}_{\alpha \in I}$$ be open sets such that $$F \subseteq \bigcup_{\alpha \in I} U_{\alpha}$$. Since $$K \subseteq F \cup F^{C}$$, then $$\left(\bigcup_{\alpha \in I} U_{\alpha}\right) \cup F^{C}$$ is an open cover of $$K$$. Since $$K$$ is compact, there exists a finite subcover $$\{U_{\alpha_{1}}, \dots, U_{\alpha_{n}}\}$$ such that 


$$
F \subseteq K \subseteq U_{\alpha_{1}} \cup \cdots \cup U_{\alpha_{n}} \cup F^{C},
$$


and since $$F \cap F^{C} = \emptyset$$, we get $$F \subseteq \bigcup_{i=1}^{n} U_{\alpha_{i}}$$. Conclude that $$F$$ is compact.

### Lemma  (The cube is compact)
The cube $$[-M,M]^{n} = \{ x \in \mathbb{R}^{n}: -M \leq x_{j} \leq M  \quad \forall j\}$$ is compact. 
The proof is similar to the case $$[a,b]$$.

### Theorem (Compact if and only if closed and bounded) 
In $$\mathbb{R}^{n}$$, $$K$$ is compact if and only if it is closed and bounded.

***Proof:*** ($$\implies$$): Suppose that $$K$$ is compact. Since $$K \subseteq \bigcup_{x \in  K} B_{1}(x)$$ is an open cover of $$K$$, there exist $$x_{1},\dots,x_{m}$$ such that 


$$
K \subseteq \bigcup_{j=1}^{m}B_{1}(x_{j}) \subseteq B_{R}(0),
$$


with $$R = \max \{ \lVert x_{1} \rVert, \dots, \lVert x_{m} \rVert \} +1$$, since if $$x \in B_1(x_{k})$$ then 


$$
\lVert x \rVert \leq \lVert x-x_{k}\rVert + \lVert x_{k} \rVert  \leq  1 + \max \{ \lVert x_{1} \rVert, \dots, \lVert x_{m} \rVert \} = R.
$$


We conclude that $$K$$ is bounded. It remains to see that $$K$$ is closed, i.e., that $$K^{C}$$ is open. Let $$x \in A^{C}$$. For $$a \in K$$, let $$\delta_{a} = \frac{\lVert x-a \rVert}{2}$$. Take as an open cover $$\bigcup_{a \in K} B_{\delta_{a}}(a) \supseteq K$$. Since $$K$$ is compact, there exist $$a_{1},\dots,a_{m} \in K$$ such that $$K \subseteq \bigcup_{j=1}^{m} B_{\delta_{a_{j}}}(a_{j})$$. Take $$0 < \delta < \min \{ \delta_{a_{1}}, \dots \delta_{a_{m}} \}$$ and consider $$B_{\delta}(x)$$. Let us see that $$B_{\delta}(x) \cap B_{\delta_{a_{j}}}(a_{j}) = \emptyset$$ for every $$j \in \{ 1,\dots,n \}$$. If $$y \in B_{\delta_{a_{j}}}(a_{j})$$, then $$\lVert y - a_{j} \rVert < \frac{\lVert x-a_{j} \rVert}{2}$$. Hence 


$$
\begin{aligned}
\lVert x-y \rVert &= \lVert x-a_{j} + a_{j} - y \rVert \\
& \geq \lVert x-a_{j} \rVert + \lVert y-a_{j} \rVert \\
& > \lVert x - a_{j} \rVert - \frac{\lVert x -a_{j} \rVert }{2} \\
&= \frac{\lVert x-a_{j} \rVert }{2} = \delta_{a_{j}} > \delta.
\end{aligned} 
$$


Since $$K \subseteq \bigcup_{j=1}^{m} B_{\delta_{a_{j}}}(a_{j})$$ and $$B_{\delta}(x) \cap B_{\delta_{a_{j}}}(a_{j}) = \emptyset$$ for every $$j$$, we get $$K \cap B_{\delta}(x) = \emptyset$$ and hence $$B_\delta(x) \subseteq K^{C}$$. Therefore $$K$$ is closed. 
($$\impliedby$$): Suppose that $$K$$ is closed and bounded. Since $$K$$ is bounded, there exists $$R>0$$ such that $$\lVert x \rVert < R$$ for every $$x \in K$$. So $$K \subseteq \bar{B}_{R}(0) \subseteq [-R, R]^{n}$$, since $$\lVert x \rVert_{\infty} < \lVert x \rVert_{2}$$. By the previous lemma, since $$K$$ is closed and contained in a compact set, conclude that $$K$$ is compact.

## Sequences in $$\mathbb{R}^{n}$$

### Definition (Sequence)
A generalisation of sequences to $$\mathbb{R}^n$$. A sequence in $$\mathbb{R}^{n}$$ is a function $$\phi: \mathbb{N} \to \mathbb{R}^{n}$$. We denote $$\bar{x_{k}} = \phi(k) \in \mathbb{R}^{n}$$, and $$\phi = (x_{k})_{k \in \mathbb{N}}$$.

### Definition (Convergence of sequences)
We say that $$(x_{k})_{k \in \mathbb{N}}$$ converges to $$x \in \mathbb{R}^{n}$$ if for every $$\varepsilon>0$$ there exists $$N \in \mathbb{N}$$ such that for every $$k \geq N$$ we have that 


$$
\lVert x_{k}-x \rVert < \varepsilon \iff x_{k} \in B_{\varepsilon}(x).
$$


We write $$\lim_{ n \to \infty } x_{n} = x$$ or $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} x$$.

#### Example 
$$\bar{x}_{k} = \begin{pmatrix}\frac{(-1)^{k}}{k} \\ \frac{k+1}{k+2} \\ e^{-k}\sin k\end{pmatrix} \underset{k \rightarrow \infty}{\longrightarrow} \begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix}$$.

## Notes
1. It is enough to consider $$\lVert \cdot \rVert_{2}$$, since all norms are equivalent.
2. If $$\bar{x}_{k} = (x_{1}^{(k)}, \dots, x_{n}^{(k)}) \in \mathbb{R}^{n}$$, that is, $$(x_{j}^{(k)})_{k\geq 1}$$ is the sequence in $$\mathbb{R}$$ of the $$j$$-th entry.

### Theorem (Convergence entry by entry)
Let $$(a_{n})_{n \in \mathbb{N}}$$ be a sequence in $$\mathbb{R}^n$$. Then $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} x$$ if and only if for every $$j \in \{ 1,\dots,n \}$$ we have that $$x^{(k)}_{j} \underset{n \rightarrow \infty}{\longrightarrow} x_{j}$$, where $$x_{k} = (x_{1}^{(k)}, \dots, x_{n}^{(k)})$$ and $$x = (x_{1}, \dots, x_{n})$$.

***Proof:*** ($$\implies$$): Suppose that $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} x$$. Given $$\varepsilon>0$$, by the definition of convergence there exists $$N \in \mathbb{N}$$ such that for every $$k \geq N$$, $$\lVert x_{k} - x \rVert < \varepsilon$$. Since $$\lvert x_{j}^{(k)} - x_{j} \rvert \leq \lVert x_{k}-x \rVert < \varepsilon$$, it follows that $$x_{j}^{(k)} \underset{k \rightarrow \infty}{\longrightarrow} x_{j}$$.
($$\impliedby$$): Suppose that $$x_{j}^{(k)} \underset{k \rightarrow \infty}{\longrightarrow} x_{j}$$ for every $$j \in \{ 1,\dots, n \}$$. Then, for each $$j$$, there exists $$N_{j} \in \mathbb{N}$$ such that $$\lvert x_{j}^{(k)} - x_{j} \rvert < \frac{\varepsilon}{n}$$. Take $$N = \max \{ N_{1},\dots N_{n} \}$$. Then, for $$k \geq N$$, note that 


$$
\lVert x_{k}-x \rVert \leq \sum_{j=1}^{n} \lvert x_{j}^{(k)} - x_{j} \rvert < \sum_{j=1}^{n} \frac{\varepsilon}{n} = \varepsilon.
$$


Conclude that $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} x$$.

### Definition (Bounded sequence)
$$(x_{k})_{k \in \mathbb{N}}$$ is bounded if there exists $$M>0$$ such that for every $$k \in \mathbb{N}$$, $$\lVert x_{k} \rVert \leq M$$.

### Theorem (Convergence implies boundedness)
Every convergent sequence is bounded

***Idea of the proof:*** Use the definition for some fixed value of $$\varepsilon$$ (e.g. $$\varepsilon = 1$$) and take $$M = \max \{ \lVert x_{1} \rVert, \dots, \lVert x_{N-1} \rVert \}$$, where $$N$$ comes from the definition of convergence.

#### Note
In contrapositive form, this says that if $$(x_{k})_{k \in \mathbb{N}}$$ is not bounded then it does not converge.

### Theorem (Operations on limits)
Let $$(x_{k})_{k \in \mathbb{N}}$$ and $$(y_{k})_{k \in \mathbb{N}}$$ be sequences such that $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow}x$$ and $$y_{k} \underset{k \rightarrow \infty}{\longrightarrow} y$$, and let $$c \in \mathbb{R}$$. Then:
1. $$x_{k} \pm y_{k} \underset{k \rightarrow \infty}{\longrightarrow} x \pm y$$,
2. $$c x_{k} \underset{k  \rightarrow \infty}{\longrightarrow} cx$$,
3. $$\bar{x}_{n} \cdot \bar{y}_{n} \underset{k \rightarrow \infty}{\longrightarrow} \bar{x} \cdot \bar{y}$$,
4. If $$(c_{k})_{k \in \mathbb{N}} \subseteq \mathbb{R}$$ and $$c_{k} \underset{k \rightarrow \infty}{\longrightarrow} c$$, then $$c_{k} x_{k} \underset{k \rightarrow \infty}{\longrightarrow} c x$$.

***Proof:*** Exercise.

### Definition (Cauchy sequence)
$$(x_{n})_{n \in \mathbb{N}}$$ is Cauchy if for every $$\varepsilon>0$$ there exists $$N \in \mathbb{N}$$ such that for all $$m,n \geq N$$, $$\lVert x_{n}-x_{m} \rVert < \varepsilon$$.

### Theorem (Convergent if and only if Cauchy)
A sequence $$(x_{k})_{k \in \mathbb{N}} \subseteq \mathbb{R}^n$$ is convergent if and only if it is Cauchy

***Proof:*** The same idea as in 250, applied entry by entry.

### Theorem (Closed sets and convergence)
A set $$F \subseteq \mathbb{R}^n$$ is closed if and only if every sequence $$(x_{k})_{k \in \mathbb{N}} \subseteq F$$ converging to $$x$$ satisfies $$x \in F$$.

***Proof:*** ($$\implies$$): Suppose that $$F$$ is closed. Let $$(x_{k})_{k \in \mathbb{N}} \subseteq F$$ with $$x_{k} \underset{k  \rightarrow \infty}{\longrightarrow} x$$. Suppose for contradiction that $$x \not\in F$$, i.e. $$x \in F^{C}$$, and since $$F^{C}$$ is open, there exists $$\varepsilon>0$$ such that $$B_{\varepsilon}(x) \subseteq F^{C}$$. By convergence of the sequence, there exists $$N \in \mathbb{N}$$ such that for every $$k \geq N$$ we have that $$\lVert x_{k}-x \rVert < \varepsilon \iff x_{k} \in B_{\varepsilon}(x)$$. Finally, since $$x_{k} \in B_{\varepsilon}(x) \subseteq F^{C}$$, we get $$x_{k} \in F_{C}$$, a contradiction, since we assumed that $$x_{k} \in F$$ for every $$k \in \mathbb{N}$$. We conclude that $$x \in F$$.
($$\impliedby$$): Suppose for contradiction that $$F$$ is not closed, i.e., $$F^{C}$$ is not open. Then there exists $$x \in F^{C}$$ such that for every $$\delta>0$$, $$B_{\delta}(x) \not \subseteq = F^{C}$$, i.e., $$B_{\delta}(x) \cap F\neq \emptyset$$. For $$n \in N^{\ast}$$, take $$\delta_{n} = \frac{1}{n} > 0$$. Then there exists $$x_{n} \in B_{\delta_{n}}(x) \cap F$$. Define the sequence $$(x_{n})_{n \in \mathbb{N}}$$. So $$x_{n} \in F$$ for every $$n \in \mathbb{N}^{\ast}$$ and $$\lVert x-x_{n} \rVert < \frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} 0$$. So $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} x \in F$$, a contradiction.

#### Example 
$$F = (0,1]$$ is not closed since $$\left( \frac{1}{k} \right)_{ k\in \mathbb{N}} \subseteq (0,1]$$ but $$\frac{1}{k} \underset{k \rightarrow \infty}{\longrightarrow} 0 \not\in F$$.

### Definition (Subsequence)
Cf. Subsequences (MA0350). Given a sequence $$(x_{k})_{k \in \mathbb{N}} \subseteq \mathbb{R}^n$$, a subsequence of $$(x_{k})_{k \in \mathbb{N}}$$ is a function $$\phi: \mathbb{N} \to \{ x_{k}:k\geq 1 \}$$ such that $$\phi (k) = x_{n_{k}}$$, with $$(n_{k})_{k \in \mathbb{N}} \subseteq \mathbb{N}$$ strictly increasing.

### Theorem (Bolzano-Weierstrass)
Every bounded sequence has a convergent subsequence

***Proof:*** If the range of the sequence is finite, at least one term of the sequence repeats infinitely often. Take that constant subsequence. 
If the range is infinite, since the sequence is bounded we know there exists a closed ball $$B$$ such that $$\{ x_{k}:k\geq 1 \} \subseteq B$$. We know that $$B$$ is compact. Suppose for contradiction that $$(x_{k})_{k \in \mathbb{N}}$$ has no convergent subsequence. So for every $$x \in \mathbb{R}^n$$ there exists $$\delta_{x}>0$$ such that $$B_{\delta_{x}}(x)$$ contains only finitely many terms of $$(x_{k})_{k \in \mathbb{N}}$$. Since $$\{ B_{\delta_{x}}:x \in B \}$$ is an open cover of $$B$$ and $$B$$ is compact, there exist $$x_{1},\dots,x_{n} \in B$$ such that $$B \subseteq \bigcup_{j=1}^{m} B_{\delta_{x_{j}}}(x_{j})$$. Note that the set on the right-hand side of the inclusion has finitely many points of the sequence, since it is a finite union of balls which in turn contain finitely many points of the sequence. But then $$B$$ has finitely many points of $$(x_{k})_{k \in \mathbb{N}}$$, a contradiction since we assumed the sequence had infinite range.

### Lemma (Nested compact sets)
Let $$K_{1} \supseteq K_{2} \supseteq \dots$$ be non-empty compact sets. Then $$\bigcap_{j=1}^{\infty} K_{j} \neq \emptyset$$.

***Proof:*** Since $$K_{1}$$ is bounded, there exists an open ball $$B$$ such that $$K_{1}  \subseteq B$$ and therefore $$K_{j} \subseteq B$$ for every $$j \in \mathbb{N}^{\ast} \}$$. Suppose for contradiction that $$\bigcap_{j=1}^{\infty} K_{j} = \emptyset$$ and define, for each $$j$$, $$O_{j} = B \setminus K_{j} = B \cap K_{j}^{C}$$. Then 


$$
\bigcup_{j=1}^{\infty} O_{j} = \bigcup_{j=1}^{\infty} (B \cap K_{j}^{C}) = B \cap \left( \bigcup_{j=1}^{\infty} K_{j}^{C} \right) = B \cap \left( \bigcap_{j=1}^{\infty} K_{j} \right)^{C} = B \supseteq K_{1}.
$$


Note moreover that  $$O_{j}= B \cap K_{j}^{C}$$ is open. So $$\{ O_{j} \}_{j=1}^{\infty}$$ is an open cover of $$K_{1}$$ and $$K_{1}$$ is compact. Then there exist $$O_{1}, \dots O_{m}$$ such that $$K_{1} \subseteq \bigcup_{j=1}^{m} O_{j} = O_{m} = B \cap K_{m}^{C}$$, which implies that $$K_{1} \subseteq K_{m}^{C}$$. But since $$K_{m} \subseteq K_{1}$$, this happens if and only if $$K_{m} = \emptyset$$, a contradiction.

## Connectedness

### Definition (Disconnected set)
A set $$D$$ is called disconnected if there exist non-empty disjoint open sets $$A, B$$ such that $$D \subseteq A \cup B$$, $$D \cap A \neq \emptyset$$ and $$D \cap B \neq \emptyset$$.
#### Example 
The set $$(0,1) \cup (2,3)$$ is disconnected.

### Definition (Connected set)
$$D$$ is connected if it is not disconnected, i.e., if for all open sets $$A, B$$, 


$$
(A \cap B = \emptyset \quad \land  \quad D \subseteq A \cup B) \implies (D \subseteq A  \quad\lor  \quad D\subseteq B)
$$



#### Example 
The interval $$I = [0,1]$$ is connected.

#### Additional examples
1. Any interval (open, half-open or closed) is connected
2. $$\{ x_{1} \}$$ is connected
3. $$\{ x_{1}, x_{2} \}$$ is disconnected
4. Any ball is connected.
5. $$\mathbb{R}^n \setminus\{ 0 \}$$ is connected if $$n \geq 2$$ and disconnected if $$n=1$$.
{% endraw %}
