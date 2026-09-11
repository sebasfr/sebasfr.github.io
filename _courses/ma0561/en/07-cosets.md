---
layout: chapter
course: ma0561
chapter: 7
title: "Cosets"
slug: 07-cosets
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/07-cosets/
---

{% raw %}
## Cosets

### Definition (Cosets)

Let $$G$$ be a group and $$H \leq G$$:

1. A left (right) coset of $$H$$ is $$aH = \{ a \ast h:h \in H \}$$ ($$Ha = \{ h \ast a:h \in H \}$$), with $$a \in G$$.

One usually writes "$$a+H$$" or "$$H+a$$" in additive groups.

### Examples (Cosets in $$\mathbb{Z}$$ and $$S_3$$)

1. Consider $$G = (\mathbb{Z}, +)$$ and let $$n \in \mathbb{Z}$$. Take $$H = \langle n \rangle = n \mathbb{Z}$$. Let $$a \in \mathbb{Z}$$. Note that

    $$
    \begin{aligned}
    a + H &= \{ a+h:h \in H \} \\
    &=\{ a + nk: k \in \mathbb{Z} \} \\
    &=\{ t: t \equiv a  \quad \mathrm{mod } \hspace{2mm}n \}.
    \end{aligned}
    $$
2. Consider $$G = S_{3}$$ and $$\tau = \begin{pmatrix}1 & 2\end{pmatrix}$$. Take $$H = \langle \tau \rangle = \{ \mathrm{id}, \tau \}$$. We have that

    $$
    \begin{aligned}
    H \cdot \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix} &= \{ \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix}, \begin{pmatrix}
    1 & 2
    \end{pmatrix} \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix} \} \\
    &=\{ \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix}, \begin{pmatrix}
    2 & 3
    \end{pmatrix} \},\\
    \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix} \cdot H &= \{ \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix}, \begin{pmatrix}
    3 & 1
    \end{pmatrix} \},\\
    H \cdot \begin{pmatrix}
    3 & 2 & 1
    \end{pmatrix} &= \{ \begin{pmatrix}
    3 & 2 & 1
    \end{pmatrix}, \begin{pmatrix}
    1 & 3
    \end{pmatrix} \}
    \end{aligned}
    $$

Note that $$H \cdot \begin{pmatrix}3 & 2 & 1\end{pmatrix} \quad \cap \quad H \ast \begin{pmatrix}1 & 2 & 3\end{pmatrix} = \emptyset$$.

### Lemma (Coset equality criterion)

Let $$H \leq G$$ and $$a,b \in G$$. Then

$$
aH = bH \iff (b^{-1} \ast a) \in H.
$$

***Proof:*** ($$\implies$$): We have that $$a \in bH$$. Hence there exists $$h \in H$$ such that $$a = b \ast h \implies b^{-1} \ast a = h \in H$$.
($$\impliedby$$): Suppose that $$b ^{-1} \ast a \in H$$. Hence there exists $$h_{0} \in H$$ such that $$b ^{-1} \ast a = h_{0}$$. Then $$a = b \ast h_{0}$$, so $$a \in bH$$. Hence $$aH \subseteq bH$$, since if $$x \in aH$$, we have that

$$
x = a \ast h = b \ast\underbrace{ h_{0} \ast h }_{ \in H }\in bH
$$

The other inclusion is proved analogously.

### Theorem (Any two cosets are equal or disjoint)

Let $$H\leq G$$ and let $$a,b \in G$$. Then $$aH = bH$$ or $$aH \cap bH = \emptyset$$.

***Proof:*** Suppose that $$aH \cap bH \neq \emptyset$$. Let $$x \in aH \cap bH$$. Hence there exist $$h_{1}, h_{2} \in H$$ such that $$x= a \ast h_{1} = b \ast h_{2}$$. Then $$b^{-1} \ast x = b^{-1} \ast a \ast h_{1} \in H$$ , so that $$b ^{-1} \ast a \in H$$. By the previous lemma $$aH = bH$$., from which we conclude the result.

### Note (Cosets as a partition)

This shows us that the cosets form a partition of the group. Moreover, if we define the relation $$\sim$$ on $$G$$ by $$a \sim b \iff aH = bH$$, this is an equivalence relation.

### Definition (Quotient set)

We define the quotient set of $$G$$ over $$H$$ as $$G/H := \{ aH:a \in G \}$$, that is, the set of representatives of $$G$$ quotiented by the equivalence class of cosets of $$H$$.

### Theorem (Equality of the number of left/right cosets)

Let $$H\leq G$$. Then the number of right cosets is equal to the number of left cosets.

***Proof:*** Let $$A = \{ aH: a \in G \}$$ and $$B = \{ Hb:b \in G \}$$. Let $$f:A\to B$$ be such that $$f(aH) = Ha^{-1}$$. $$f$$ is well defined: If $$aH = a'H$$, then $$H a^{-1} = H(a')^{-1}$$. Finish the proof (exercise).

### Proposition (Cardinality of a subgroup and its cosets)

If $$H\leq G$$ and $$a \in G$$, then $$\lvert a H \rvert = \lvert H \rvert$$ (as cardinality, since $$aH$$ is not necessarily a group)

***Proof:*** Define $$f:H\to aH$$ by $$h \mapsto a \ast h$$. Note that

$$
\begin{aligned}
f(h_{1}) = f(h_{2}) \implies a \ast h_{1} = a \ast h_{2} \implies a^{-1} \ast a \ast h_{1} = a^{-1} \ast a \ast h_{2} \implies h_{1}=h_{2}.
\end{aligned}
$$

### Definition (Indices)

Let $$H \leq G$$. We define the index of $$H$$ in $$G$$ as $$[G:H] = \lvert G/H \rvert$$ is the number of distinct cosets of $$H$$ in $$G$$.

### Theorem (Lagrange for finite groups)

Let $$G$$ be a finite group and $$H\leq G$$. Then $$\lvert G \rvert = [G:H] \cdot \lvert H \rvert$$. In particular, $$\lvert H \rvert \Big\lvert \lvert G \rvert$$.

***Proof:*** Let $$k = [G :H]$$. Let $$a_{1}H, a_{2}H, \dots, a_{k}H$$ be the distinct cosets of $$H$$ in $$G$$. Then $$G = \bigcup_{i=1}^{k} a_{i} H$$. Since $$a_{1}H, a_{2}H, \dots, a_{k}H$$ are disjoint, we have that $$\lvert G \rvert = \sum_{i=1}^{k} \lvert a_{i} H \rvert = k \lvert H \rvert$$.

### Corollary (The order of an element divides the order of the group)

Let $$a \in G$$. Then $$\lvert a \rvert \Big\lvert \lvert G \rvert$$.

***Proof:*** Take $$H = \langle a \rangle$$. Then $$\lvert H \rvert = \lvert a \rvert$$ and the result follows from Lagrange's theorem.

### Corollary (Multiplicativity of the index)

Let $$K,H,G$$ be groups such that $$K \leq H\leq G$$. Then $$[G:K] = [G:H] [H:K]$$.

***Proof:*** Applying Lagrange's theorem to the three indices:

$$
[G:H] \cdot \lvert H \rvert = \lvert G \rvert, \quad [H:K] \cdot \lvert K \rvert = \lvert H \rvert, \quad [G:H] \cdot [H : K] = \lvert G \rvert.
$$

Thus,

$$
[G:H] \cdot [H:K] = \frac{\lvert G \rvert}{\lvert H \rvert } \cdot \frac{\lvert H \rvert}{\lvert K \rvert }  = \frac{\lvert G \rvert}{\lvert K \rvert } = [G:K].
$$

### Proposition (Cosets over the kernel of a homomorphism)

Let $$G, G'$$ be groups and $$f:G \to G'$$ a homomorphism. Let $$H = \operatorname{Ker}(f) \leq G$$. Let $$a \in G$$ and $$a' = f(a)$$. Then $$aH = \{ x \in G:f(x) = a' \}$$.

***Proof:*** Let $$x \in aH$$, then there exists $$h \in H$$ such that $$x = a \ast h$$. Hence $$f(x) = f(a) \ast_{G'} f(h) = f(a) = a'$$. Hence $$aH \subseteq \{ x \in G:f(x) = a' \}$$. On the other hand, if $$x \in G$$ is such that $$f(x) = a'$$, we have that

$$
f(x) = f(a) \iff \big(f(a)\big)^{-1} \ast_{G'} f(x) = 1_{G'} \iff f(a^{-1} \ast x) = 1_{G'},
$$

from which we have that $$a^{-1} \ast x \in H$$ and, by the coset equality criterion, $$xH = aH$$, whence $$x \in aH$$. Thus $$\{ x \in G: f(x) = a' \} \subseteq aH$$, and therefore $$aH \subseteq \{ x \in G:f(x) = a' \}$$.
{% endraw %}
