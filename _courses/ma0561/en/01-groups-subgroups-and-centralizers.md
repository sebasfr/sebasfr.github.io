---
layout: chapter
course: ma0561
chapter: 1
title: "Groups, Subgroups and Centralizers"
slug: 01-groups-subgroups-and-centralizers
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/01-groups-subgroups-and-centralizers/
---

{% raw %}
## Elementary definitions

### Definition (Binary operation)

Let $$G$$ be a non-empty set. A binary operation is a map $$G \times G \to G$$ with $$(g_{1},g_{2}) \mapsto g_{3}$$.

### Definition (Group)

A group $$G$$ is a non-empty set together with a binary operation $$\ast: G \times G \to G$$ such that:

1. $$\ast$$ is associative:

    $$
    \forall g_{1},g_{2},g_{3} \in G \quad  (g_{1} \ast g_{2}) \ast g_{3} = g_{1} \ast (g_{2} \ast g_{3});
    $$
2. there exists an identity element $$e \in G$$ such that $$e \ast g = g\ast e = g$$ for every $$g \in G$$. We often write $$1_{G}$$ to denote the identity element of the group $$G$$;
3. every element has an inverse, that is,

    $$
    \forall g \in G  \quad \exists h \in G  \quad (g \ast h = h \ast g = e).
    $$

### Definition (Abelian Group)

If $$(G, \ast)$$ is a group which moreover satisfies that for all $$g_{1},g_{2} \in G$$, $$g_{1} \ast g_{2} = g_{2} \ast g_{1}$$, we say that $$G$$ is *commutative* or *abelian*.

### Definition (Monoid)

A monoid is a more general structure, given by a set and an associative binary operation with an identity element, but where not every element necessarily has an inverse.

## Properties of groups

### Proposition (Uniqueness of the identity)

If $$e, e'$$ are two identity elements, $$e' = e' \ast e = e$$.

### Proposition (Uniqueness of the inverse)

Let $$g \in G$$ and let $$h, h'$$ be inverses of $$g$$. Then

$$
h' = e \ast h' = (h \ast g) \ast h' = h \ast (g \ast h') = h \ast e = h.
$$

### Notation (Inverse)

If $$(G, \ast)$$ is a group and $$g \in G$$, we denote by $$g^{-1}$$ the inverse of $$g$$.

### Note (Properties of the inverse)

1. $$(g^{-1})^{-1} = g$$ for every $$g \in G$$
2. $$(g \ast h)^{-1} = h ^{-1} \ast g ^{-1}$$ for all $$g,h \in G$$.

### Proposition (Cancellation laws)

If $$g, h_{1}, h_{2} \in G$$, then

1. $$g \ast h_{1} = g \ast h_{2} \implies h_{1}=h_{2}$$,
2. $$h_{1} \ast g = h_{2} \ast g \implies h_{1} = h_{2}$$.

## Examples of groups

Some examples are very important within the theory

### Example (Trivial group)

Let $$G = \{  e \}$$ be such that $$e \ast e = e$$. $$(G, \ast)$$ is a group and is called the trivial group.

### Example (Additive groups)

$$(\mathbb{Z}, + )$$ is a group with identity element $$0$$ and in which the inverse of $$z \in Z$$ is $$-z$$. $$(\mathbb{N}, +)$$ is not a group but it is a monoid, whereas $$(\mathbb{N}^{\ast},+)$$ is not a monoid. $$(\mathbb{R},+), (\mathbb{Q},+), (\mathbb{C}, +), (\mathbb{Z},+)$$ are all abelian groups.

### Example (Multiplicative groups)

$$(\mathbb{R}^{\ast}, \cdot), (\mathbb{Q}^{\ast}, \cdot), (\mathbb{C}^{\ast}, \cdot)$$ are abelian groups with identity $$1$$ and where the inverse of $$x$$ is $$\frac{1}{x}$$. In general, if $$\mathbb{F}$$ is a field, $$(\mathbb{F}^{\ast}, \cdot)$$ is a group. $$(\mathbb{Z}^{\ast}, \cdot)$$ is not a group because not every element has an inverse.

### Example (Linear groups)

Let $$n \in \mathbb{N}^{\ast}$$ and let $$\mathbb{F}$$ be a field. We define

$$
GL_{n}(\mathbb{F}) = \{\text{invertible }n \times n \text{ matrices with entries in }\mathbb{F} \}.
$$

$$(GL_{n}(\mathbb{F}), \cdot)$$, where $$\cdot$$ is the standard multiplication of matrices. This group is called the linear group over $$\mathbb{F}$$.

### Example (Groups over congruences)

Let $$m>0$$ and consider $$\mathbb{Z}_{m} = \mathbb{Z}/{\equiv_{m}}$$ ($$\mathbb{Z}$$ quotiented by the relation of congruence modulo $$m$$), i.e., $$\mathbb{Z}_{m} = \{ [0], [1],\dots, [m-1] \}$$. Define the operation $$\hat{+}$$ on $$\mathbb{Z}_{m}$$ such that $$[a]\hat{+}[b] = [a+b]$$ (we must show that it is well defined). $$(\mathbb{Z}_{m}, \hat{+})$$ is a group with identity element $$[0]$$. If $$[n] \in \mathbb{Z}_{m}$$, the inverse is $$[-n]$$. Let us consider the example with $$m=2$$.

For $$\mathbb{Z}_{2}$$, we have $$\mathbb{Z}_{2} = \{ [0]. [1] \}$$. Note the operation table

| $$\hat{+}$$ | $$[0]$$ | $$[1]$$ |
| --- | --- | --- |
| $$[0]$$ | $$[0]$$ | $$[1]$$ |
| $$[1]$$ | $$[1]$$ | $$[0]$$ |

Let us now define on $$\mathbb{Z}_{m}^{\ast} = \mathbb{Z}_{m} \setminus \{ [0] \}$$. Let us define the operation $$\hat{\cdot}$$ as

$$
[a] \hat{\cdot} [b] = [a \cdot b]
$$

We want to construct a multiplicative group with this new operation. For which cases of $$m$$ is this well defined and do inverses exist? For composite $$m$$, multiplication is not well defined on $$\mathbb{Z}_{m}^{\ast}$$ because we may take elements of certain equivalence classes whose product has result $$[0]$$.

For primes, the operation is well defined. Let $$n$$ be prime and suppose that there exist $$[a], [b] \in \mathbb{Z}_{n}^{\ast}$$ such that $$[a] \hat{\cdot} [b] = [a \cdot b] = [0]$$. This implies that $$n \mid a \cdot b$$, but since $$n$$ is prime, $$n \mid a$$ or $$n \mid b$$, so that $$[a] = [0]$$ or $$[b]=[0]$$, a contradiction since $$[0] \not\in \mathbb{Z}_{n}^{\ast}$$.

We shall prove that $$(\mathbb{Z}_{n}^{\ast}, \hat{\cdot})$$ is a group for $$n$$ prime. Note that $$\mathbb{Z}_{n}^{\ast} = \{ [1],\dots,[n-1] \}$$. Let $$r \in \{ 1,\dots,n-1 \}$$. Since $$n$$ is prime, we have that $$\operatorname{GCD}(r,n) = 1$$. Hence there exist integers $$q,s$$ such that $$qr+sn = 1$$. This implies that

$$
[q \cdot r] = [1] \implies [q] \hat{\cdot} [r] = [1].
$$

We may suppose that $$q \in \{ 1,\dots,n-1 \}$$, since otherwise we take the representative of its equivalence class. Thus $$[q]$$ is the inverse of $$[r]$$. So $$(\mathbb{Z}_{n}^{\ast}. \hat{\cdot})$$ has inverses for every element, and therefore it is a group (the other properties are trivial).

### Note (Field $$\mathbb{Z}_p$$)

It is easy to verify that if $$p$$ is prime $$(\mathbb{Z}_{p}, \hat{+}, \hat{\cdot}, [0], [1])$$ is a field.

### Example (Groups of symmetries of a square)

Consider a square with its vertices numbered. In how many ways can we move its vertices so that the square still occupies the same space? We can perform four rotations ($$0^{\circ}, 90^{\circ}, 180^{\circ}, 270^{\circ}$$) anticlockwise, ($$r_{0},r_{90},r_{180},r_{270}$$). Moreover, we can perform four reflections: vertical ($$s_{1}$$), horizontal ($$s_{2}$$), diagonal starting bottom-left ($$s_{3}$$) and diagonal starting top-left ($$s_{4}$$).

We call $$D_{4}= \{ r_{0},r_{90},r_{180},r_{270}, s_{1},s_{2},s_{3},s_{4} \}$$. We define an operation $$\circ$$ on $$D_{4}$$, as the "composition of movements", e.g., $$r_{90} \circ s_{2}$$.

### Exercise (Dihedral group $$D_4$$)

$$(D_{4},\circ)$$ is a group but is **not** commutative.

In general $$D_{n}$$ is the group of symmetries of a regular polygon with $$n$$ sides. It is made up of $$r_{0},\dots,r_{n-1}$$ rotations, where $$r_{k}$$ rotates the figure by an angle of $$\frac{2\pi k}{n}$$ and $$s_{0}, \dots, s_{n-1}$$ are $$n$$ reflections about the lines $$\theta = \frac{\pi k}{n}$$. $$D_{n}$$ has $$2n$$ elements, and is called the dihedral group.

### Example (Group of permutations of $$n$$ elements)

A permutation of $$n$$ elements is a bijective function

$$
\begin{aligned}
\sigma:\{ 1,\dots,n \} &\to \{ 1,\dots,n \}, \text{ such that} \\
1 &\mapsto \sigma(1)\\
& \quad\vdots \\
n &\mapsto \sigma(n).
\end{aligned}
$$

We define $$S_{n} = \{ \sigma: \sigma \text{ is a permutation of }n \text{ elements}\}$$. $$S_{n}$$ is a group under composition of functions (exercise).

### Notation (Permutations)

$$\sigma: \begin{pmatrix}1 & 2 & 3 \\ 2 & 3 & 1\end{pmatrix}$$ represents $$\sigma:\{ 1,2,3 \} \to \{ 1,2,3 \}$$, with $$\sigma(1)=2, \sigma(2)=3,\sigma(3)=1$$. Its inverse is $$\sigma ^{-1}:\begin{pmatrix}1 & 2 & 3 \\ 3 & 1 & 2\end{pmatrix}$$.

### Example (Product of groups)

Let $$(G_{1}, \ast_{1})$$ and $$(G_{2}, \ast_{2})$$ be two groups. Consider the Cartesian product $$G_{1} \times G_{2}$$. Define the operation $$\ast$$ on $$G_{1} \times G_{2}$$ such that

$$
(g_{1}, g_{2}) \ast (h_{1},h_{2}) := (g_{1} \ast_{1} h_{1}, g_{2} \ast_{2} h_{2}) \in G_{1} \times G_{2}.
$$

Then, $$(G_{1} \times G_{2}, \ast)$$ is a group with identity element $$(1_{G_{1}}, 1_{G_{2}})$$. If $$(g_{1},g_{2}) \in G_{1} \times G_{2}$$, then $$(g_{1}, g_{2})^{-1} = (g_{1}^{-1}, g_{2}^{-1})$$. This can be generalised to the product of $$n$$ groups.

## Iterated operations in groups

If $$(G, \ast)$$ is a group we denote by $$g^{n} = \underbrace{ g \ast g \ast \dots \ast g }_{ n \text{ times} }$$,, $$g^{0} = 1_{G}$$, $$g^{-n}:= (g^{-1})^{n}$$.

### Proposition (Properties of exponentiation)

Let $$(G, \ast)$$ be a group, $$g,h \in G$$. Then

1. $$g^{-n} = (g^{n}) ^{-1}$$
2. $$g^{n+m} = g^{n} \ast g^{m}$$
3. If $$g \ast h = h \ast g$$, then $$(g \ast h)^{m} = g^{m} \ast h^{m}$$.

## Subgroups

Let $$(G, \ast)$$ be a group and $$H \subseteq G$$. We say that $$H$$ is a subgroup of $$G$$ if $$(H, \ast \mid_{H})$$ is a group. In that case we write $$H \leq G$$

### Note (Subgroup verification)

To verify that $$H \leq G$$, it suffices to check (1) that $$h_{1}\ast h_{2} \in H  \quad \forall h_{1}, h_{2} \in H$$, (2) that $$1_{G} \in H$$ and (3) that, if $$h \in H$$ then $$h^{-1} \in H$$.

### Theorem (Characterisation of a subgroup)

Let $$\emptyset \neq H \subseteq G$$. Then $$H \leq G$$ if and only if

$$
\forall x,y \in H  \quad (x \ast y^{-1} \in H).
$$

***Proof:*** $$(\implies)$$ is trivial. Let us prove $$(\impliedby)$$. If $$x \in H$$, then $$x \ast x ^{-1} = 1_{G}  \in H$$. On the other hand, since $$1_{G} \in H$$, $$1_{G} \ast x^{-1} = x^{-1} \in H$$. Finally, if $$x,y \in H$$, since $$y^{-1} \in H$$, then $$x \ast (y ^{-1}) ^{-1} = x \ast y \in H$$. Therefore, $$H$$ is a subgroup.

### Lemma (The intersection of subgroups is a subgroup)

Let $$(G, \ast)$$ and let $$\{ H_{i}:i \in I \}$$ be a family of subgroups of $$G$$. Then $$H:=\bigcap_{i \in I} H_{i} \leq G_{i}$$.

***Proof:*** Note that $$H\neq \emptyset$$, since $$1_{G} \in H_{i}$$ for every $$i$$. Let $$x,y \in H$$. Since $$x,y \in H_{i}$$ for every $$i \in I$$. Then $$x \ast y^{-1} \in H_{i}$$ for every $$i$$. Hence $$x \ast y ^{-1} \in H$$.

### Definition (Group generated by a subset)

Let $$(G, \ast)$$ be a group and $$S \subseteq G$$. Define

$$
\langle S \rangle := \bigcap \{ H:H\leq G  \quad \land  \quad S \subseteq H\}
$$

as the group generated by $$S$$.

### Theorem (The generated group is the smallest group containing the set)

$$\langle S \rangle$$ is the smallest group containing $$S$$, i.e., if $$K\leq G$$ is such that $$S \subseteq K$$, then $$\langle S \rangle \subseteq K$$.

***Proof:*** If $$K \leq G$$ and $$S \subseteq K$$, then $$K \in \{ H \leq G : S \subseteq H \}$$, so that $$\bigcap \{ H:H\leq G  \quad \land  \quad S \subseteq H\} = \langle S \rangle \subseteq K$$.

### Theorem (Characterisation of the generated group)

If $$(G, \ast)$$ is a group and $$S \neq \emptyset$$, then

$$
\langle S \rangle = \{ x_{1}^{\alpha_{1}} \ast \dots \ast x_{n}^{\alpha_{n}}: n \in \mathbb{N}^{\ast}, x_{i} \in S, \alpha_{i} \in \{ -1,1\} \}.
$$

***Proof:*** Let $$H = \{ x_{1}^{\alpha_{1}} \ast \dots \ast x_{n}^{\alpha_{n}}: n \in \mathbb{N}^{\ast}, x_{i} \in S, \alpha_{i} \in \{ -1,1\} \}$$. Note that $$H \neq \emptyset$$. Let $$x,y \in H$$. Then there exist $$k, \ell \in \mathbb{N}^{\ast}; \{ \alpha_{i} \}_{i=1}^{k}, \{ \beta_{i} \}_{i=1}^{\ell}$$ with $$\alpha_{i}, \beta_{i} \in \{ -1,1 \}$$ for every $$i$$, and $$x_{1},\dots,x_{k},y_{1},\dots y_{\ell} \in S$$ such that

$$
x = x_{1}^{\alpha_{1}} \ast \dots \ast x_{k}^{\alpha_{k}}, y = y_{1}^{\beta_{1}}\dots y_{\ell}^{\beta_{\ell}}.
$$

Note that $$x \ast y^{-1} = x_{1}^{\alpha_{1}} \ast \dots \ast x_{k}^{\alpha_{k}} \ast y_{1}^{-\beta_{1}}\dots y_{\ell}^{\beta_{-\ell}} \in H$$. Thus $$H \leq G$$ and therefore $$\langle S \rangle \subseteq H$$.
On the other hand, since $$\langle S \rangle$$ is a group, $$H \subseteq \langle S \rangle$$.

### Definition (Generated group)

If $$(G, \ast)$$ is a group and $$S \subseteq G$$ is such that $$\langle S \rangle = G$$, we say that $$G$$ is generated by $$S$$. If $$S$$ is finite, we say that $$G$$ is finitely generated.

### Examples (of generated groups)

1. Let $$(G, \ast)$$ be a group. Then

    $$
    \begin{aligned}
    \langle \emptyset \rangle &= \bigcap \{ H: H\leq  G \} \\
    &= \{ 1_{G} \}.
    \end{aligned}
    $$
2. If $$(G, \ast)$$ is a group and $$S \leq G$$, $$\langle S \rangle = \langle S \rangle$$.
3. If $$S = \{ i \} \subseteq (\mathbb{C}^{\ast}, \cdot)$$, then $$\langle S \rangle = \{ i,-1,1,-i \}$$.
4. If $$S = \{ 2 \} \subseteq (\mathbb{Z},+)$$, $$\langle S \rangle = \{ 2k:k \in \mathbb{Z} \}$$.
5. If $$S=\{ 12,-8 \} \subseteq (\mathbb{Z}, +)$$, then $$\langle S \rangle = \{ 12 a + (-8)b: a,b \in \mathbb{Z} \} = \{ 4k: k \in \mathbb{Z} \}$$ .
6. In general, if $$a \in (G, \ast)$$,

    $$
    \begin{aligned}
    \langle a \rangle &= \bigcap \{ H: H<a  \quad\land  \quad a \in H \}\\
    &= \{ a^{n}: n \in \mathbb{Z} \}.
    \end{aligned}
    $$

## Centre and centralizer

### Definition (centre of $$G$$)

Let $$(G, \ast)$$ be a group. Define

$$
Z(G) = \{ g \in G: \forall h \in G (gh = hg)\}
$$

### Note (Properties of the centre)

1. $$e \in Z(G)$$,
2. $$G$$ is abelian if and only if $$Z(G) = G$$.
3. If $$g \in Z(G)$$, then for every $$h \in G$$, $$h = g \ast h \ast g^{-1}$$.

### Theorem (The centre is a subgroup)

If $$G$$ is a group, then $$Z(G) \leq G$$ and $$Z(G)$$ is commutative.

### Definition (Centralizer)

Let $$G$$ be a group and $$a \in G$$. Define the centralizer as

$$
C(a):= \{ g \in G: a \ast g = g \ast a \}
$$

### Exercise (The centralizer is a subgroup)

$$C(a) \leq G$$.

It can be proved that $$Z(G) = \bigcap_{a \in G} C(a)$$.
{% endraw %}
