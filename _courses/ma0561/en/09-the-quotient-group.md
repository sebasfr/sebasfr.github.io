---
layout: chapter
course: ma0561
chapter: 9
title: "The Quotient Group"
slug: 09-the-quotient-group
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/09-the-quotient-group/
---

{% raw %}
## The quotient group

### Proposition (Normal groups and operations)

If $$H \triangleleft G$$ and $$a,b \in G$$, then $$aH \cdot bH = (a \ast b) H$$

***Proof:*** Note that

$$
\begin{aligned}
aH \cdot bH
\end{aligned} = aH \cdot Hb = a Hb = a b H = (a \ast b) H.
$$

### Theorem (Existence of the quotient group)

Let $$H \triangleleft G$$. Then $$G / H$$ is a group under the operation $$\cdot$$

$$
a H \cdot bH = (a \ast b) H.
$$

***Proof:*** The operation is well defined and associative (see the previous proposition).

1. Membership of the identity: $$1_{G} \cdot H = H$$
2. Existence of inverses: $$aH \cdot a^{-1}H = (a \ast a^{-1}) H = H = id_{G / H }$$.

### Note (Independence of the representative)

Why does it not depend on the representative? Suppose that $$aH = \hat{a}H$$ and $$bH = \hat{b}H$$. Then

$$
aH \cdot bH = \hat{a} H \cdot \hat{b}H \iff (a \ast b) H = (\hat{a} \ast \hat{b}) H \iff (a \ast b) \ast (\hat{ a} \ast \hat{b})^{-1} \in H,
$$

which is clearly true.

### Theorem (Every normal subgroup is the kernel of a homomorphism)

Let $$H \triangleleft G$$ and consider $$f:G\to G / H$$ such that $$f(a) = a H$$. Then $$f$$ is an epimorphism and $$\operatorname{Ker}(f) = H$$.

***Proof:*** We shall first show that $$f$$ is a homomorphism. Note that $$f(a \ast b) = (a \ast b) H = aH \cdot bH = f(a) \cdot f(b)$$. Surjectivity follows from the definition. Now, if $$x \in H$$, then $$f(x) = xH = H =id_{G / H}$$, hence, $$x \in \operatorname{Ker} f$$. If $$x \in \operatorname{Ker} f$$, then $$f(x) = xH = H$$, hence $$x \in H$$.

### Example (Trivial quotients)

1. Note that $$\{ 1_{G} \} \triangleleft G \implies G / \{ 1_{G} \} = \{ a \cdot \{ 1_{G}: a \in G \} \} = \{ \{ a \}: a \in G \} \cong G$$.
2. $$G \triangleleft G \implies G / G = \{ a \cdot G: a \in G \} = \{ G \} = \{ 1_{G / G} \}$$.

### Example (Quotients in $$\mathbb{Z}$$ and in a cyclic group)

1. Let $$G = (\mathbb{Z}, + )$$, $$H = 4\mathbb{Z}$$. Note that $$H \triangleleft G$$ since $$G$$ is abelian. Note that $$G / H \cong \mathbb{Z}_{4}$$, since $$aH = bH \iff a + (-b) \in 4\mathbb{Z} \iff 4 \mid a-b \iff a \cong b  \quad \text{mod }4$$.
2. Let $$G$$ be a group and let $$a \in G$$ be such that $$\lvert a \rvert = 8$$. and $$G=\langle a \rangle$$. Let $$H = \langle a^{4}. \rangle$$ Since $$G$$ is commutative. $$H \triangleleft G$$. We have that $$H = \{ 1_{G, }a^{4} \}$$ and $$G = \{ 1_{G}, a, a^{2},\dots,a^{7} \}$$. What is $$G/H$$? Let us find the cosets:

    1. $$H = a^{4}H$$
    2. $$aH = \{ a, a^{5} \} = a^{5} H$$
    3. $$a^{2}H = \{ a^{2}, a^{6} \} = a^{6}H$$
    4. $$a^{3}H = \{ a^{3},a^{7} \}= a^{7}H$$
        Thus, $$G/H = \{ H, aH, a^{2}H, a^{3}H \}$$ and $$G = H  \hspace{2mm}  \dot{\cup} \hspace{2mm} aH \hspace{2mm} \dot{\cup} \hspace{2mm} a^{2}H \hspace{2mm}\dot{\cup} \hspace{2mm} a^{3}H$$.

### Definition (Commutator and commutator subgroup)

Let $$(G,\ast)$$ be a group. Let $$a,b \in G$$. Define the commutator of $$a,b$$ as

$$
[a,b] = a \ast b \ast a^{-1} \ast b ^{-1} \in G
$$

Define the commutator subgroup of $$G$$ as $$G':=  \langle [a,b]:a,b \in G \rangle$$.

### Exercise (Characterisation via conjugation)

Let $$S < G$$. Then $$S \triangleleft G$$ if and only if $$C_{a}(S) \leq S$$ for every $$a \in G$$.

### Theorem (Commutator subgroup and abelian quotients)

Let $$G$$ be a group and $$G'$$ its commutator subgroup. Then $$G' \triangleleft G$$. Moreover, if $$H \triangleleft G$$, then $$G/H$$ is abelian if and only if $$G' \triangleleft H$$.

***Proof:*** We must show that, for every $$g \in G$$, $$gG'g^{-1} \subseteq G'$$. It suffices to show that if $$a, b \in G$$, $$g \in G$$ , then $$g[a,b]g^{-1} \in G'$$, why? If $$z = [a_{1} , b_{1}] [a_{2}, b_{2}]$$, then

$$
gzg^{-1} = g [a_{1},b_{1}] [a_{2}, b_{2}] g^{-1} = (g[a_{1},b_{1}]g^{-1})(g [a_{2},b_{2}] g^{-1}),
$$

hence, it suffices to prove the result for an arbitrary commutator and it follows immediately for every $$z \in G'$$, Let $$[a,b] \in G'$$. Then,

$$
\begin{aligned}
g \ast a \ast b \ast a^{-1} \ast b^{-1} \ast g^{-1}
\end{aligned}
$$

$$
= (g \ast a \ast g^{-1}) \ast (g \ast b \ast g^{-1}) \ast(g \ast a^{-1} \ast g ^{-1}) \ast (g \ast b ^{-1} \ast g ^{-1}) = [g \ast a \ast g ^{-1},g \ast b \ast g ^{-1} ]\in G'.
$$

Suppose now that $$G/H$$ is abelian. Then for all $$a,b \in G$$, $$aH \cdot b H = b H \cdot a H$$, so that $$(a \ast b) H = (b \ast a)H$$. Hence , $$(a \ast b) \ast (b \ast a) ^{-1} = a \ast b \ast a^{-1} \ast b ^{-1} = [a,b] \in H$$. Thus, $$\{ [a,b]: a,b \in G \} \subseteq H \implies G' \subseteq H \implies G' \leq H$$. (Write out the other direction).

### Example ($$A_3 \triangleleft S_3$$)

Consider $$S_{3} = \{ (1),\begin{pmatrix}1 & 2\end{pmatrix}, \begin{pmatrix}2 & 3\end{pmatrix}, \begin{pmatrix}1 & 3\end{pmatrix}, \begin{pmatrix}1 & 2 & 3\end{pmatrix} \begin{pmatrix}3 & 2 & 1\end{pmatrix} \}$$ and $$A_{3} = \{ \sigma \in S_{3}: \sigma \text{ is even} \} = \{ \begin{pmatrix}1\end{pmatrix}, \begin{pmatrix}1 & 2 & 3\end{pmatrix}, \begin{pmatrix}3 & 2 & 1\end{pmatrix}\}$$. We shall show that $$A_{3} \triangleleft S_{3}$$. Consider $$S = \{ -1,1 \}$$. Note that $$(S, \cdot) = (\mathbb{Z}_{2}, +)$$. Let $$f:S_{3} \to S$$ be such that $$\sigma \mapsto \operatorname{sgn}( \sigma )$$. Note that $$f$$ is a homomorphism, since

$$
\begin{aligned}
f(\sigma_{1} \circ \sigma_{2}) &= \operatorname{sgn}(\sigma_{1} \circ \sigma_{2}  )\\
&= \operatorname{sgn}( \sigma_{1} ) \cdot \operatorname{sgn}( \sigma_{2} )\\
&= f(\sigma_{1}) \cdot f(\sigma_{2}).
\end{aligned}
$$

Note that $$\operatorname{Ker} f = A_{3}$$, from which we conclude that $$A_{3} \triangleleft S_{3}$$. What is $$S_{3}/A_{3}$$? Let us construct the cosets

1. $$A_{3}$$
2. $$\begin{pmatrix}1 & 2\end{pmatrix} A_{3} = \{ \begin{pmatrix}1 & 2\end{pmatrix}, \begin{pmatrix}3 & 2\end{pmatrix}, \begin{pmatrix}1 & 3\end{pmatrix} \}$$.

Thus, $$S_{3}/A_{3} = \{ A_{3}, \begin{pmatrix}1&2\end{pmatrix}A_{3} \} \cong \mathbb{Z}_{2}$$.

### Example ($$\langle r_1\rangle \triangleleft D_4$$)

Consider $$D_{4} = \{ r_{0},r_{1},r_{2},r_{3},s_{1},s_{2},s_{3},s_{4} \}$$ the group of symmetries of the square and $$H = \langle r_{1} \rangle = \{ r_{0},r_{1},r_{2},r_{3} \}$$. We must show that for every $$i \in \{ 1,\dots,4 \}$$, $$s_{i} H s_{i} ^{-1} \subseteq H$$. Note first that for every $$i$$, $$s_{i}^{2} = r_{0}$$, hence, $$s_{i} = s_{i}^{-1}$$. Hence, we must show that for all $$j \in \{ 0,1,2,3 \}, i \in\{ 1,2,3,4 \}$$, $$s_{i} r_{j} s_{i} ^{-1} \in H$$
{% endraw %}
