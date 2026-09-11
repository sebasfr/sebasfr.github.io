---
layout: chapter
course: ma0561
chapter: 8
title: "Normal Subgroups"
slug: 08-normal-subgroups
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/08-normal-subgroups/
---

{% raw %}
## Normal subgroups

### Definition (Product of sets)

Let $$G$$ be a group and $$S,T \subseteq G$$. Define $$ST = \{ s \ast t: s \in S, t \in T \}$$.
Note that if $$S = \{ s \}$$ and $$T\leq G$$, then $$sT =ST$$, a coset of $$G$$. Note that if $$S,T,U \subseteq G$$, . If $$\mathcal{F} = \{ A:A\subseteq G \}$$, then $$\cdot$$ is defined on $$\mathcal{F}$$ and is associative.

### Definition (Normal subgroup)

Let $$H \leq G$$. We say that $$H$$ is a normal subgroup of $$G$$ and we write $$H \triangleleft G$$ if $$Hx = xH$$ for every $$x \in G$$.

### Note (Properties of normal subgroups)

1. If $$G$$ is abelian, every subgroup is normal.
2. $$xH = Hx \iff xH x^{-1} = \{ x \ast h \ast x ^{-1}: h \in H \} = H$$.
3. If $$H \triangleleft G$$, this does not imply that for all $$x \in G$$ and $$h \in H$$ $$x \ast h = h \ast x$$. What is true is that if $$h \in H$$, there exists $$h' \in H$$ such that $$x \ast h = h' \ast x$$.
4. If for every $$x \in  G$$, $$x H x ^{-1} \subseteq H$$, this necessarily implies equality of the two sets, and hence that $$H \triangleleft G$$. Suppose that $$xHx ^{-1} \subseteq H$$ for every $$x \in G$$. Note that, for $$x \in G$$.

    $$
    H = x ^{-1}(\underbrace{  x H x ^{-1} }_{ \in H }) x \subseteq x ^{-1} H x \subseteq H \implies x ^{-1} H x = H.
    $$
5. For every group $$G$$, $$\{ 1_{G} \} \triangleleft G$$, $$G \triangleleft G$$.

### Proposition (Chained subgroups)

Let $$K,H,G$$ be groups with $$K\leq H\leq G$$. If $$K \triangleleft G$$, then $$K \triangleleft H$$.

***Proof:*** The result is trivial, since $$G \subseteq H$$.

### Theorem (The kernel is a normal subgroup)

Let $$f:G\to G'$$ be a group homomorphism. Then $$\operatorname{Ker}(f) \triangleleft G$$.

***Proof:*** Let $$H:= \operatorname{Ker}(f)$$. Let $$x \in G$$. We must show that $$xHx ^{-1} \subseteq H$$. Let $$h \in H$$. Then $$f(x \ast h \ast x ^{-1}) = f(x) \ast f(h) \ast f(x ^{-1}) = 1_{G'}$$.

### Example (Normal subgroup in $$S_3$$)

Let $$G = S_{3} = \{ (1), \begin{pmatrix}1 & 2\end{pmatrix}, \begin{pmatrix}1 & 3\end{pmatrix}, \begin{pmatrix}2 & 3\end{pmatrix} \begin{pmatrix}1 & 2 & 3\end{pmatrix} \begin{pmatrix}3 & 2 & 1\end{pmatrix} \}$$. Consider $$H = \langle \begin{pmatrix}1 & 2 & 3\end{pmatrix} \rangle$$. We have that

and similarly for the remaining cycles.
{% endraw %}
