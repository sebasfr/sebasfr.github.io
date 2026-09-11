---
layout: chapter
course: ma0561
chapter: 4
title: "Group Homomorphisms"
slug: 04-group-homomorphisms
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/04-group-homomorphisms/
---

{% raw %}
## Elementary definitions

### Definition (Group homomorphism)

Let $$(G,\ast_{G}), (H,\ast_{H})$$ be groups. A group homomorphism between $$G$$ and $$H$$ is a function $$f:G\to H$$ such that

$$
\forall a,b, \in G  \quad \Big( f(a \ast_{G} b) = f(a) \ast_{h} f(b)\Big).
$$

### Examples (Basic homomorphisms)

1. Let $$G$$ be a group and $$f:G\to G$$ such that $$f(x) = 1_{G}$$ for all $$x \in G$$. Note that

    $$
    f(x \ast y) = 1_{G} = 1_{G} \ast 1_{G} = f(x) \ast f(g)
    $$
2. Consider $$f:(\mathbb{R},+) \to (\mathbb{R}^{\ast}, \cdot)$$ such that $$f(x) = e^{x}$$. Note that

    $$
    f(x+y) = e^{x+y} = e^{x}
     \cdot e^{y} = f(x) \cdot f(y).
    $$

### Proposition (Properties of homomorphisms)

Let $$(G,\ast_{G}), (H,\ast_{H})$$ be groups and $$f:G\to H$$ a homomorphism. Then:

1. $$f(1_{G}) = 1_{H}$$,
2. $$\forall g \in G  \quad \Big( f(g^{-1}) = \big(f(g)\big)^{-1}\Big)$$,
3. $$\forall n \in \mathbb{Z} \quad \Big(f(g^{n}) = \big(f(g)\big)^{n}\Big)$$
4. If $$g \in G$$ and $$\lvert g \rvert = n$$, then $$\lvert f(g) \rvert \Big\lvert n$$.

***Proof:*** For (1), note that

$$
f(1_{G}) = f(1_{G} \ast_{G} 1_{G}) = f(1_{G}) \ast_{H} f(1_{G}),
$$

from which we conclude that $$f(1_{G}) = 1_{H}$$.
For (2), note that

$$
g \ast_{G} g^{-1} = 1_{G} \implies f(g) \ast_{H} f(g^{-1}) = 1_{H} \implies f(g^{-1}) = \big(f(g)\big)^{-1}.
$$

For (3), in the case $$n\geq 0$$, we proceed by induction. The base case $$n=0$$ was proved in (1). Suppose as inductive hypothesis that $$f(g^{n})=\big(f(g)\big)^{n}$$ for some $$n \in \mathbb{N}$$. Note that

$$
\begin{aligned}
f(g^{n+1}) = f(g^{n} \ast_{G} g) &=f(g^{n}) \ast_{H} f(g)\\
&=\big(f(g)\big)^{n} \ast_{H} f(g) \\
&= \big(f(g)\big)^{n+1}.
\end{aligned}
$$

Now, for $$n<0$$, note that $$-n > 0$$. Thus, $$g^{n} = (g^{-n})^{-1}$$. Thus,

$$
f(g^{n}) = f\big((g^{-n})^{-1}\big) = \big(f(g^{-n})\big)^{-1} = \Big(\big(f(g)\big)^{-n}\Big)^{-1} = \big(f(g)\big)^{n}.
$$

Finally, for (4), since $$\lvert g \rvert = n$$,

$$
g^{n} = 1_{G} \implies f(g^{n}) = \big(f(g)\big)^{n} = 1_{H},
$$

from which we deduce that $$\lvert f(g) \rvert \Big\lvert n$$.

### Example (Projection and homomorphisms into $$\mathbb{Z}$$)

1. Consider $$f:(\mathbb{Z}, +)\to(\mathbb{Z}_{n}, +)$$ such that $$x \mapsto [x]$$. Note that

    $$
    f(x+y) = [x+y] = [x] + [y] = f(x) + f(y),
    $$

from which we conclude that $$f$$ is a homomorphism.

1. Is there a non-trivial homomorphism $$f:\mathbb{Z}_{n} \to \mathbb{Z}$$? If there were, note that $$\lvert [1] \rvert = n$$ and hence $$\lvert f[1] \rvert \Big\lvert n$$, a contradiction, since the order of the elements of $$\mathbb{Z}$$ is infinite (except for zero).

### Proposition (Composition of homomorphisms)

Let $$G,H,K$$ be groups and $$f:G\to H$$, $$g:H\to K$$ homomorphisms. Then $$g \circ f:G \to K$$ is a homomorphism.

***Proof:*** Exercise

### Definition (Kernel and image of a homomorphism)

Let $$G,H$$ be groups and $$f:G\to H$$ a homomorphism. Define

$$
\begin{aligned}
\operatorname{Ker}(f) &= \{ x \in G: f(x) = 1_{H} \} \subseteq G \\
\operatorname{Im}(f) &= \{ f(x):x \in G \} \subseteq H.
\end{aligned}
$$

### Theorem (Kernel and image are subgroups)

Let $$G,H$$ be groups and $$f:G\to H$$ a homomorphism. Then,

1. $$\operatorname{Ker}(f) \leq G$$
2. $$\operatorname{Im}(f) \leq H$$

***Proof:*** For (1), note that $$1_{G} \in \operatorname{Ker}(f)$$, so $$\operatorname{Ker}(f) \neq \emptyset$$. Let $$x,y \in \operatorname{Ker}(f)$$.

$$
f(x \ast_{G} y^{-1}) = f(x) \ast_{H} f(y^{-1}) =1_{H} \implies x \ast_{G} y \in \operatorname{Ker}(f).
$$

For (2), note that $$f(1_{G}) = 1_{H} \in \operatorname{Im}(f)$$, so $$\operatorname{Im}(f) \neq \emptyset$$. Let $$a,b \in \operatorname{Im}(f)$$. Hence, there exist $$x,y \in G$$ such that $$f(x) = a$$ and $$f(y) = b$$. By the properties of homomorphisms, $$b^{-1} = f(y^{-1})$$. Thus,

$$
f(x \ast_{G} y^{-1}) = f(x) \ast_{H} \big(f(y)\big)^{-1} = a \ast_{H} b^{-1} \in \operatorname{Im}(f).
$$

### Example (Projection $$\mathbb{Z} \to \mathbb{Z}_n$$)

Let $$\pi:\mathbb{Z} \to \mathbb{Z}_{n}$$ be such that $$x \mapsto [x]$$. We have that

$$
\begin{aligned}
\operatorname{Im}(\pi) &= \{ \pi(x):x \in \mathbb{Z} \} \\
&=\{ [x]: x \in \mathbb{Z} \} \\
&=\mathbb{Z}_{n},\\
\operatorname{Ker}(\pi) &=\{ x:\pi(x) = [0] \} \\
&=\{ x: [x] = 0 \} \\
&=n \cdot \mathbb{Z}.
\end{aligned}
$$

### Definition (Monomorphisms, epimorphisms and isomorphisms)

Let $$f:G\to H$$ be a group homomorphism:

1. if $$f$$ is injective, we say that $$f$$ is a monomorphism,
2. if $$f$$ is surjective, we say that $$f$$ is an epimorphism,
3. if $$f$$ is bijective, we say that $$f$$ is an isomorphism.

### Theorem (Existence of the inverse isomorphism)

If $$f:G\to H$$ is an isomorphism, then $$f^{-1}:H\to G$$ (as a function) is an isomorphism.

***Proof:*** Exercise.

### Theorem (Monomorphisms and kernel)

Let $$f:G\to H$$ be a homomorphism. Then,

$$
f \text{ is a monomorphism} \iff \operatorname{Ker}(f) = \{ 1_{G} \}
$$

***Proof:*** exercise. Note that $$f(x)=f(y) \implies f(x \ast y^{-1}) = 1_{H}$$.

### Theorem (Inverse image and homomorphisms)

Let $$f:G\to H$$ be a homomorphism and let $$H'\leq H$$. Then $$f^{-1}(H') \leq G$$

***Proof:*** Note that $$1_{G} \in f^{-1}(H')$$ since $$f(1_{G}) = 1_{H} \in H \implies f^{-1}(H') \neq \emptyset$$. Let $$x,y \in f^{-1}(H')$$. We must show that $$x \ast_{G} y^{-1} \in f^{-1}(H')$$. Since $$f(x) \in H', f(y) \in H'$$, we have that $$\big(f(y)\big)^{-1} = f(y^{-1}) \in H'$$. Then $$f(x \ast_{G} y^{-1}) = f(x)\ast_{H} f(y^{-1}) \in H'$$.

### Definition (Automorphism and automorphism group)

Let $$G$$ be a group. An automorphism of $$G$$ is an isomorphism from $$G$$ to $$G$$. Define $$\mathrm{Aut} \hspace{2pt}(G) = \{ f:G\to G \text{ isomorphism}\}$$ as the set of automorphisms of $$G$$.
Note that $$\mathrm{Aut} \hspace{2pt}(G) \subseteq S_{G} = \{ \phi: G\to G \text{ bijective}\}$$.

### Theorem (Subgroup of automorphisms)

$$\mathrm{Aut} \hspace{2pt}(G) \leq S_{g}$$.

***Proof:*** Exercise

### Definition (Isomorphic groups)

We say that two groups $$G$$ and $$H$$ are isomorphic if there exists an isomorphism $$f:G\to H$$. We write $$G \cong H$$.

### Example (Isomorphism $$\mathbb{Z}_4 \cong G$$)

Consider $$G = (\{ 1,i,-1,-i \}, \ast)$$.

$$Z_{4} \cong G$$ under the isomorphism

$$
\begin{aligned}
0  &\mapsto 1 \\
1 &\mapsto i \\
2 &\mapsto -1 \\
3 &\mapsto -i
\end{aligned}
$$

### Note (Being isomorphic is an equivalence relation)

Note that the relation $$G \cong H$$ is reflexive, transitive and symmetric (this is easy to prove). Hence it is an equivalence relation.

### Theorem (Isomorphisms of cyclic groups)

If $$G = \langle g \rangle$$, then:

1. If $$\lvert g \rvert = \infty \implies G \cong \mathbb{Z}$$.
2. If $$\lvert g \rvert = n \implies G \cong \mathbb{Z}_{n}$$.
{% endraw %}
