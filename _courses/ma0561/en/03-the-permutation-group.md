---
layout: chapter
course: ma0561
chapter: 3
title: "The Permutation Group"
slug: 03-the-permutation-group
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/03-the-permutation-group/
---

{% raw %}
## The permutation group

Let $$n \in \mathbb{N}^{\ast}$$. Define

$$
S_{n} = \{ \sigma: \sigma \text{ is a permutation of }\{ 1,\dots,n \} \}.
$$

If $$X$$ is any set, a bijective $$\sigma: X \to X$$ is a permutation.
$$S_{X} = \{ \sigma : \quad \sigma: X \to X \text{ permutation} \}$$. It is easy to see that if $$\lvert X \rvert = n$$, then $$S_{X} \cong S_{n}$$, since

$$
\begin{aligned}
X &= \{ x_{1},\dots,x_{n} \}\\
&\cong \{ 1,\dots,n \}
\end{aligned}.
$$

### Theorem (Order of the permutation group)

Let $$n \in \mathbb{N}^{\ast}$$. Then $$\lvert S_{n} \rvert = n!$$.

***Proof:*** Note that

$$
\begin{aligned}
\sigma(1) &\text{ has } n \text{ possibilities}\\
\sigma(2) &\text{ has } n-1 \text{ possibilities} \\
& \qquad \qquad \vdots \\
\sigma(n) &\text{ has } 1 \text{ possibility}.
\end{aligned}
$$

### Definition (Moving and fixing an element)

Let $$\alpha \in S_{n}$$ and let $$k \in \{ 1, \dots, n \}$$. We say that:

1. "$$\alpha$$ moves $$k$$" if $$\alpha(k) \neq k$$,
2. "$$\alpha$$ fixes $$k$$" if $$\alpha(k) = k$$.

### Notation (Composition of permutations)

Consider $$\alpha:\{ 1,2,3\} \to \{ 1,2,3 \}$$ and $$\beta:\{ 1,2,3\} \to \{ 1,2,3 \}$$ such that

$$
\alpha = \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 3
\end{pmatrix}, \quad
\beta = \begin{pmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{pmatrix}.
$$

We have that

$$
\alpha \circ \beta = \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 3
\end{pmatrix} \circ \begin{pmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{pmatrix} = \begin{pmatrix}
1 & 2 & 3 \\
3 & 1 & 2
\end{pmatrix},
$$

$$
\beta \circ \alpha = \begin{pmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{pmatrix} \circ \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 3
\end{pmatrix} = \begin{pmatrix}
1 & 2 & 3 \\
2 & 3 & 1
\end{pmatrix}.
$$

In general, two permutations need not commute.

### Definition (r-cycle)

Let $$n \in \mathbb{N}^\ast$$ and $$r \in \{ 1,\dots,n \}$$. We say that $$\alpha \in S_{n}$$ is an $$r$$-cycle. If there exist distinct $$i_{1},\dots,i_{r} \in \{ 1,\dots,n \}$$ such that

$$
\begin{aligned}
\alpha(i_{1}) &= i_{2}\\
\alpha(i_{2}) &= i_{3}\\
\vdots\\
\alpha(i_{r-1}) &= i_{r}\\
\alpha(i_{r}) &= i_{1}.
\end{aligned}
$$

We write, $$\begin{pmatrix}i_{1} & \cdots  & i_{r}\end{pmatrix}$$. Note that if $$\alpha = \begin{pmatrix} i_{1} & \cdots & i_{r}\end{pmatrix}$$ and $$j \not\in \{ i_{1},\dots,i_{r} \}$$, then $$\alpha(j) = j$$.

### Example ($$r$$-cycle in $$S_4$$)

$$\alpha=\begin{pmatrix}1 & 2 & 3 & 4 \\ 2 & 3 & 1 & 4\end{pmatrix} = \begin{pmatrix}1 & 2 & 3\end{pmatrix} \in S_{4}$$.

### Definition (Disjoint permutations)

Let $$\alpha,\beta \in S_{n}$$/ We say that $$\alpha$$ and $$\beta$$ are disjoint if every element moved by $$\alpha$$ is fixed by $$\beta$$ and every element moved by $$\beta$$ is fixed by $$\alpha$$. Note that this definition allows there to be elements fixed by both,

### Definition (Transposition)

We say that a $$2$$-cycle is a transposition.

### Note (Cycle notation)

$$
\begin{pmatrix}
1 & 3 & 5
\end{pmatrix} = \begin{pmatrix}
5 & 1 & 3
\end{pmatrix} = \begin{pmatrix}
3 & 5 & 1
\end{pmatrix}
$$

are the same cycle.

### Exercise ($$r$$-cycle and order)

Show that $$\alpha \in S_{n}$$ is an $$r$$-cycle if and only if $$\lvert a \rvert = r$$ (i.e., $$\alpha^{r} = \mathrm{id}_{n}$$).

### Note (Inverse of a cycle)

If $$\alpha = \begin{pmatrix}1 & 3 & 5\end{pmatrix} \in S_{5}$$, $$\alpha ^{-1} = \begin{pmatrix}5 & 3 & 1\end{pmatrix}$$.

### Example (Product of disjoint transpositions)

Consider $$\alpha \in S_{4}$$ with

$$
\alpha = \begin{pmatrix}
1 & 2 & 3 & 4 \\
2 & 1 & 4 & 3
\end{pmatrix} = \underbrace{ \begin{pmatrix}
1 & 2
\end{pmatrix} }_{ \beta_{1} } \underbrace{ \begin{pmatrix}
3 & 4
\end{pmatrix} }_{ \beta_{2} },
$$

where $$\beta_{1}, \beta_{2} \in S_{1}$$ are disjoint $$2$$-cycles.

### Theorem (Commutativity of disjoint permutations)

Let $$\alpha, \beta \in S_{n}$$ be disjoint. Then $$\alpha \circ \beta = \beta \circ \alpha$$.

***Proof:*** Let $$i \in \{ 1,\dots, n \}$$. We have three possible cases.
**Case 1:** $$\alpha$$ moves $$i$$. Let $$j = \alpha(i) \neq i$$. Then $$\beta(i) = i$$. Note moreover that $$\alpha(j) \neq j$$, since otherwise $$\alpha(i) = j = \alpha(j)$$ implies, by injectivity of $$\alpha$$, that $$i = j$$, a contradiction. Therefore $$\beta(j) = j$$. Thus, we have that

$$
\begin{aligned}
(\alpha \circ \beta)(i) &= \alpha(\beta(i)) = \alpha(i) = j \\
(\beta \circ \alpha)(i) &= \beta(\alpha(i)) = \beta(j) = j.
\end{aligned}
$$

**Case 2:** $$\beta$$ moves $$i$$. This case is analogous to the previous one.
**Case 3:** $$\alpha, \beta$$ fix $$i$$: Note that $$\alpha(i) = \beta(i) = i$$. Hence

$$
\begin{aligned}
(\alpha \circ \beta)(i) &= \alpha(\beta(i)) = \alpha(i) = i \\
(\beta \circ \alpha)(i) &= \beta(\alpha(i)) = \beta(j) = i.
\end{aligned}
$$

Conclude that disjoint permutations commute.

### Theorem (Finite orbit)

Let $$\alpha \in S_{n}$$, $$i \in \{ 1,\dots,n \}$$ such that $$\alpha(i) \neq i$$. Define the sequence $$\{ i_{k} \}_{k \in \mathbb{N}^{\ast}}$$ so that $$i_{1} = i$$, $$i_{2} = \alpha(i_{1}) = \alpha(i), \dots,i_{k+1} = \alpha (i_{k})$$ for every $$k \in \mathbb{N}^{\ast}$$. Then:

1. there exists $$k \in \{ 1,\dots,n \}$$ such that $$i_{k+1} \in \{ i_{1},\dots, i_{k} \}$$;
2. if $$r = \min \{ k \in \mathbb{N}^{\ast} : i_{k+1} \in \{ i_{1},\dots,i_{k} \} \} \implies i_{r+1} = i_{1}.$$

***Proof:*** For (1), note that for every $$k \in \mathbb{N}^{\ast}$$, $$\{ i_{1},\dots,i_{k} \} \subseteq \{ 1,\dots,n \}$$ and $$\{ 1,\dots,n \}$$ is finite, so the result follows directly.
For (2), define $$r$$ as in the statement. Take $$i_{j}:= i_{r+1} \in \{ i_{1},\dots,i_{r} \}$$. Suppose for contradiction that $$j>1 \implies j-1>0$$. Note that $$\alpha^{j-1}(i) = i_{j} = i_{r+1} = \alpha^{r}(i)$$. Applying $$\alpha ^{-1}$$ $$j-1$$ times, we have that

$$
i_{1} = i = \alpha^{r+1-j}(i),
$$

but $$r+1-j < r$$, so this contradicts the minimality of $$r$$. Therefore $$j = 1$$.

### Lemma (Equality of cycles)

Let $$\alpha, \beta \in S_{n}$$ and let $$i \in \{ 1,\dots,n \}$$. If $$\alpha, \beta$$ move $$i$$ and for every $$k \in \mathbb{N}$$, $$\alpha^{k}(i) = \beta^{k}(i)$$, then $$\alpha = \beta$$.

***Proof:*** exercise.

### Theorem (Factorisation into disjoint cycles)

Every permutation in $$S_{n}$$ is a product of disjoint cycles. Moreover, if we add the $$1$$-cycles the decomposition is unique up to order.

***Proof:*** Let $$\alpha \in S_{n}$$. Proceed by strong induction on the number $$k$$ of elements moved by $$\alpha$$. If $$k=0$$, then $$\alpha = \mathrm{id}_{n}$$. Then $$\alpha = (1)(2) \cdots (n)$$.
Consider now the case $$k>0$$. Suppose that the theorem is true for $$\{0,1,\dots,k-1\}$$. Let $$i \in \{ 1,\dots,n \}$$ such that $$\alpha(i) \neq i$$. Define $$i_{k} \in \{ 1,\dots,n \}$$ such that $$i_{1} = i$$ and $$i_{m+1} = \alpha(i_{m}) = \alpha^{m}(i)$$ for $$m \in \mathbb{N}^{\ast}$$. Let $$r = \min \{ \ell \in \mathbb{N}: i_{\ell+1} \in \{ i_{1},\dots,i_{\ell} \} \} \leq n$$. By the previous theorem, $$i_{r+1}=i_{1}$$. Let $$\delta = \begin{pmatrix}i_{1} & \cdots  & i_{r}\end{pmatrix} \in S_{n}$$ be an $$r$$=cycle.
If $$r = n$$ , $$\delta$$ is an $$n$$-cycle and $$\delta = \alpha$$. If $$r<n$$, define $$A := \{ 1,\dots,n \} \setminus \{ i_{1},\dots,i_{r} \}$$. Note that $$\alpha(A) = A$$, since all these points are fixed by $$\alpha$$. Moreover, $$\delta$$ fixes every element of $$A$$ by construction. Let $$\beta \in S_{n}$$ be such that for every $$x \in A$$, $$\beta(x) = \alpha(x)$$ and for every $$x \in \{ i_{1},\dots,i_{r} \}$$, $$\beta(x) = x$$. Note that $$\beta$$ and $$\delta$$ are disjoint. Moreover, $$\alpha = \beta \circ \delta$$. The number of elements moved by $$\beta$$ is less than $$k$$. Hence, by the inductive hypothesis applied to $$\beta$$, $$\beta$$ is a product of disjoint cycles, and therefore so is $$\alpha = \beta \circ \delta$$.

### Proposition (Decomposition into transpositions)

Let $$n\geq 2$$. Every $$\alpha \in S_{n}$$ is a product of transpositions.

***Proof:*** It is enough to show it when $$\alpha$$ is a cycle. Let $$\alpha = \begin{pmatrix}a_{1} & \cdots & a_{n}\end{pmatrix}$$ be a cycle. Proceed by strong induction on $$r$$. For $$r=1$$, note that $$\alpha = (a)$$. Hence $$\alpha$$ is the identity of $$S_n$$. Let $$b \in \{ 1,\dots,n \}$$ such that $$b\neq a$$ (we know it exists because $$n>2$$). Hence $$\alpha = \begin{pmatrix} a & b\end{pmatrix} \begin{pmatrix}a & b\end{pmatrix} = \mathrm{id}_{S_{n}}$$. Suppose as inductive hypothesis that the theorem is true for every $$k$$-cycle with $$k \leq r-1$$.
We shall prove that $$\alpha = \begin{pmatrix}a_{1} & a_{3} & \cdots  & a_{r-1}\end{pmatrix} \begin{pmatrix}a_{1} & a_{2}\end{pmatrix}$$. Let $$\beta = \begin{pmatrix}a_{1} & a_{3} & \cdots  & a_{r}\end{pmatrix} \begin{pmatrix}a_{1} & a_{2}\end{pmatrix}$$. Note that

$$
\begin{aligned}
\beta(a_{r}) = a_{1} &= \alpha(a_{r}) \\
\beta(a_{1}) = a_{2} &=\alpha(a_{1})\\
\beta(a_{2}) = a_{3} &= \alpha(a_{2})\\
\beta(a_{k}) = a_{k+1} &= \alpha(a_{k}), \qquad 3\leq k\leq r-1.\\b
\beta(b) = b &= \alpha(b), \qquad b \not\in \{ a_{1},\dots,a_{k} \}.
\end{aligned}
$$

Hence $$\alpha = \beta$$. We apply the I.H. to $$\begin{pmatrix}a_{1} & a_{3} & \cdots a_{r}\end{pmatrix}$$.

### Note (Standard form)

$$\alpha = \begin{pmatrix} x_{1} & \cdots & x_{m}\end{pmatrix} = \begin{pmatrix}x_{1} & x_{m}\end{pmatrix} \begin{pmatrix}x_{1} & x_{m-1}\end{pmatrix} \cdots \begin{pmatrix}x_{1} & x_{2}\end{pmatrix}$$.

### Example (Factorisation into transpositions)

Consider

$$
\begin{aligned}
\alpha &=\begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
6 & 2 & 7 & 9 & 8 & 3 & 1 & 5 & 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 6 & 3 & 7
\end{pmatrix} \begin{pmatrix}
2
\end{pmatrix} \begin{pmatrix}
4 & 9
\end{pmatrix} \begin{pmatrix}
8 & 5
\end{pmatrix} \qquad \text{factorisation into cycles} \\
&= \begin{pmatrix}
1 & 3 & 7
\end{pmatrix} \begin{pmatrix}
1 & 6
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
4 & 9
\end{pmatrix} \begin{pmatrix}
5 & 8
\end{pmatrix} \\
&=\begin{pmatrix}
1 & 7
\end{pmatrix} \begin{pmatrix}
1 & 3
\end{pmatrix} \begin{pmatrix}
1 & 6
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
4 & 9
\end{pmatrix} \begin{pmatrix}
5 & 8
\end{pmatrix} \qquad \text{decomposition into transpositions}.
\end{aligned}
$$

### Definition (Sign)

Let $$n \in \mathbb{N}$$, $$\alpha \in S_{n}$$. If $$\alpha = \beta_{1} \cdots \beta_{k}$$ is a complete factorisation into disjoint cycles. Define $$\operatorname{sgn}(\sigma) = (-1)^{n-k}$$.

### Theorem (Sign and transpositions)

Let $$\alpha \in S_{n}$$ and let $$\tau$$ be a transposition. Then $$\operatorname{sgn}(\tau\alpha) = -\operatorname{sgn}(\alpha)$$.

***Proof:*** Exercise

### Theorem (Sign splits products)

Let $$\alpha, \beta \in S_{n}$$. Then $$\operatorname{sgn}(\alpha\beta) = \operatorname{sgn}(\alpha) \operatorname{sgn}(\beta)$$.

***Proof:*** Exercise, induction on the number of transpositions.

### Definition (Parity of a permutation)

We say that $$\alpha \in S_{n}$$ is even if $$\alpha$$ can be decomposed as the product of an even number of transpositions. Otherwise $$\alpha$$ is odd.

### Theorem (Parity and sign)

Let $$\alpha \in S_{n}$$. $$\alpha$$ is odd if and only if $$\operatorname{sgn}( \alpha ) = - 1$$.

### Definition (Alternating group)

$$A_{n}:= \{ \sigma \in S_{n}: \sigma \text{ is even} \}$$ is a group. Moreover. $$\lvert A_{n} \rvert = \frac{n!}{2}$$.
{% endraw %}
