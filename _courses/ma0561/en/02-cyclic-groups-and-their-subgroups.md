---
layout: chapter
course: ma0561
chapter: 2
title: "Cyclic Groups and Their Subgroups"
slug: 02-cyclic-groups-and-their-subgroups
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/02-cyclic-groups-and-their-subgroups/
---

{% raw %}
## Cyclic groups

### Definition (Order of a group and of an element)

Let $$(G, \ast)$$ be a group. The order of $$G$$ is the number of elements of $$G$$ and is denoted by $$\lvert  G \rvert$$.

1. If there exists a prime $$p$$ such that $$\lvert  G \rvert = p^{k}$$ with $$k \in \mathbb{N}$$, we say that $$G$$ is a $$p$$-group.
2. If $$G$$ is a group and $$g \in G$$, the order of $$g$$ ($$\lvert  g \rvert$$) is the least $$n \in \mathbb{N}$$ such that $$g^{n} = 1_{G}$$. If no such $$n$$ exists, we say that $$\lvert g \rvert = \infty$$.

### Examples (Orders in $$\mathbb{Z}_n$$)

1. $$(\mathbb{Z}_{n}, +) = \{ [0],[1],\dots,[n-1] \}$$, $$\lvert \mathbb{Z}_{n} \rvert = n$$.
2. Consider $$(\mathbb{Z}_{4}, +) = \{ [0], [1], [2], [3] \}$$, $$\lvert \mathbb{Z}_{4} \rvert = 4$$. Note that

    $$
    [2] \neq [0] \quad \land  \quad [2]+[2] = [0],
    $$

so $$\lvert [2] \rvert = 2$$. In the same way, we check that $$\lvert [1] \rvert = 4$$ and $$\langle [1] \rangle = \mathbb{Z}_{4}$$.

### Theorem (Order and divisibility)

Let $$G$$ be a group and $$g \in G$$, $$n \in \mathbb{Z}$$. Then

$$
g^{n} = 1_{G} \iff \lvert g \rvert \mid n.
$$

***Proof:*** Let us prove the case $$n \in \mathbb{N}$$.
($$\impliedby$$): If $$\lvert g \rvert \mid n$$, there exists $$k \in \mathbb{N}$$ such that $$k \lvert g \rvert = n$$. Then

$$
g^{n} = g^{k \lvert  g \rvert } = (g^{\lvert g \rvert })^{k} = (1_{G})^{k} = 1_{G}.
$$

$$(\implies)$$: Suppose that $$g^{n} = 1_{G}$$. By minimality, $$\lvert g \rvert \leq n$$. By the division algorithm, there exist $$q,r \in \mathbb{N}$$ such that $$n = q \lvert g \rvert + r$$ and $$0 \leq r < \lvert g \rvert$$. Then,

$$
1_{G} = g^{n} =g^{q \lvert g \rvert} \ast g^{r} = 1_{G} \ast g^{r} = g^{r},
$$

from which we conclude that $$r = 0$$ by minimality of $$\lvert g \rvert$$, and therefore $$\lvert g \rvert \mid n$$.

For the general case $$n \in \mathbb{Z}$$, it suffices to see that $$g^{n} = 1_{G} \iff g^{-n} = 1_{G}$$ and moreover $$\lvert  g \rvert \mid n \iff \lvert g \rvert \mid -n$$.

### Definition (Cyclic group)

Let $$G$$ be a group. $$G$$ is cyclic if there exists $$g \in G$$ such that $$G = \langle g \rangle$$.

### Example (Cyclic groups)

1. $$(\mathbb{Z}, +) = \langle 1 \rangle = \langle -1 \rangle$$. We have that $$\lvert \mathbb{Z} \rvert = \infty, \lvert 1 \rvert = \infty, \lvert 2 \rvert = \infty$$.
2. Consider $$\mathbb{Z}_{5}$$ with the multiplication of equivalence classes (congruence modulo 5) defined earlier. We define

    $$
    U(5) = \{ [x] \in \mathbb{Z}_{5}: \exists [y] \in \mathbb{Z}_{5}([x] \cdot [y]=[1]) \} = \mathbb{Z}^{\ast}_{5}
    $$

Is $$U(5)$$ a cyclic group? Yes, for example, $$\lvert [2] \rvert = 4$$. In the same way, its inverse $$[3]$$ also works to generate $$U(5)$$. But $$[4]$$ does not. Thus, $$\langle [2] \rangle, \langle [3] \rangle$$.

### Definition (Units of $$\mathbb{Z}_{m}$$)

Consider $$\mathbb{Z}_{m}$$. Define

$$
U(m) = \{ [x] \in \mathbb{Z}_{m}: \exists [y] \in \mathbb{Z}_{m}([x] \cdot [y] = [1]) \}.
$$

We say that $$[a]$$ is a unit of $$\mathbb{Z}_{m}$$ if $$a \in U(m)$$.

### Exercise (Characterisation of units)

Show that $$[a] \in U(m) \iff \operatorname{GCD}(a,m) = 1$$.

### Theorem (Generator of $$\mathbb{Z}_m$$)

Let $$m \in \mathbb{N}^{\ast}$$. Consider $$(\mathbb{Z}_{m}, +)$$. Let $$[a] \in \mathbb{Z}_{m}$$. Let $$[a] \in \mathbb{Z}_{m}$$. Then

$$
\langle [a] \rangle = \mathbb{Z}_{m} \iff \operatorname{GCD}(a,m) = 1.
$$

***Proof:*** ($$\impliedby$$): Suppose that $$\operatorname{GCD}(a,m)=1$$. By the previous exercise, there exists $$[a]^{-1} \in \mathbb{Z}_{m}$$ such that $$[a] \cdot [a] ^{-1} = [1]$$. Let $$[b] \in \mathbb{Z}_{m}$$. We shall prove that $$[b] \in \langle [a] \rangle$$. Let $$k \in \mathbb{Z}$$ be such that $$[k]:=[b] \cdot [a^{-1}]$$. Thus,

$$
\begin{aligned}
[k]= [b] \cdot [a]^{-1} \implies [k] \cdot [a] = [b] \implies [a] + \dots + [a] = [b],
\end{aligned}
$$

from which we conclude that $$b \in \langle[a]\rangle$$, and therefore $$\langle [a] \rangle = \mathbb{Z}_{m}$$.
The other direction is left as an exercise.

### Note (Cardinality of cyclic groups)

If $$G$$ is cyclic, then $$G$$ is countable ($$\lvert G \rvert \leq \lvert \mathbb{N} \rvert$$). Since it is cyclic, there exists $$g \in G$$ such that $$G = \langle g \rangle = \{ g^{n}:n \in \mathbb{Z} \}$$. Consider the function $$\Phi: \mathbb{Z} \to G$$ such that $$n \mapsto g^{n}$$. Since $$g$$ is cyclic, this function is surjective. Thus, $$\lvert G \rvert \leq \lvert \mathbb{Z} \rvert$$. This implies that any group built from uncountable sets, such as $$(\mathbb{R}, +)$$, cannot be cyclic.

### Proposition (Cyclic groups and order)

Let $$G$$ be a cyclic group with $$g \in G$$ such that $$G = \langle g \rangle$$. Then:

1. If $$\lvert g \rvert = \infty$$, then $$g^{i}=g^{j} \iff i=j$$.
2. If $$\lvert g \rvert=n \in \mathbb{N}$$, then $$\langle g \rangle = \{ e,g,\dots, g^{n-1}\}$$. In this case $$g^{i} = g^{j} \iff n \mid i-j$$. This implies that $$\lvert G \rvert = \lvert g \rvert$$.

***Proof:*** For (1), suppose that $$\lvert g \rvert=\infty$$. Hence for every $$n \in \mathbb{N}$$, $$g^{n} \neq e$$. Suppose that there exist distinct $$i,j$$ (with $$i<j$$ without loss of generality) such that $$g^{i} = g^{j}$$. Since $$j-i>0$$, we have that $$e = g^{i} \ast g^{-i} =g^{j-i}$$, a contradiction since $$g$$ has infinite order.
For (2), we know that $$\langle g \rangle = \{ g^{n}: n \in \mathbb{Z} \}$$, so $$\{ e,g,\dots, g^{n-1}\} \subseteq \langle g \rangle$$. Now, let $$h \in \langle g \rangle$$. Then, there exists $$k \in \mathbb{Z}$$ such that $$h = g^{k}$$. By the division algorithm, there exist $$q,r \in \mathbb{Z}$$ with $$0\leq r\leq n-1$$ such that $$k=nq+r$$. Thus, $$h=g^{nq+r} = (g^{n})^{q} \ast g^{r}  = g^{r} \in \{ e,g,\dots, g^{n-1}\}$$. We conclude that $$\langle  g \rangle = \{ e,g,\dots, g^{n-1}\}$$.
Now, given $$i,j \in \mathbb{Z}$$, suppose that $$g^{i} = g^{j} \implies g^{i-j} = e$$, hence $$\lvert g \rvert \Big\lvert i-j$$. Finally, it suffices to show that if $$0 \leq i<j<n$$ then $$g^{i} \neq g^{j}$$. Note that $$0<j-i<n$$, so if $$g^{i} = g^{j}$$, then $$g^{j-i} = e$$, which contradicts the minimality of the order $$n$$.

## Subgroups of Cyclic Groups

### Lemma (Divisibility and generated subgroup)

Let $$G$$ be a cyclic group and $$g \in G$$ such that $$G = \langle g \rangle$$. If $$k \mid \ell$$, then $$\langle g^{\ell} \rangle \subseteq \langle g^{k} \rangle$$.

***Proof:*** Let $$x \in \langle g^{\ell} \rangle$$. There exists $$r \in \mathbb{Z}$$ such that $$x=(g^{\ell})^{r}$$. Moreover, since $$k \mid \ell$$, there exists $$t \in \mathbb{Z}$$ such that $$tk = \ell$$. Thus, $$x = (g^{tk})^{r} = (g^{k})^{tr} \in \langle g^{k} \rangle$$.

### Exercise (Order of a power)

If $$g \in G$$ with $$\lvert g \rvert = rs$$, with $$r,s \in \mathbb{N}$$, then $$\lvert g^{r} \rvert = s$$.

### Proposition (Orders of subgroups of cyclic groups)

Let $$G$$ be a group and $$g \in G$$ such that $$\lvert g \rvert = n$$. Given $$k \in \mathbb{N}$$, then

1. $$\langle g^{k} \rangle = \langle g^{\operatorname{gcd}(n,k)} \rangle$$
2. If $$c \mid n$$, then $$\lvert g^{c} \rvert  = \frac{n}{c}$$.

In particular, $$\lvert g^{k} \rvert = \frac{n}{\operatorname{gcd}(n,k)}$$.

***Proof:*** For (1), let $$d=\operatorname{gcd}(n,k)$$. It is clear that $$d \mid k \implies \langle g^{k} \rangle \subseteq \langle g^{d} \rangle$$. On the other hand, by Bezout's lemma, there exist $$r,t \in \mathbb{Z}$$ such that $$d = rn + tk$$. Hence, $$g^{d} = g^{rn} \ast g^{tk} = (g^{k})^{t},$$ so $$g^{d} \in \langle g^{k} \rangle$$ and therefore $$\langle g^{d} \rangle \subseteq \langle g^{k} \rangle$$. We conclude that $$\langle g^{d} \rangle = \langle g^{k} \rangle$$.

Now, for (2), since $$c \mid n$$, there exists $$m \in \mathbb{Z}$$ such that $$mc = n \implies m = \frac{n}{c} \in \mathbb{Z}$$. Using the previous exercise, we have that $$\lvert g \rvert = \frac{n}{c} \cdot c$$ and therefore $$\lvert g^{c} \rvert = \frac{n}{c}$$. For the particular result, take $$c=d$$ in (2) and use property (1).

### Corollary (order of elements in cyclic groups)

Let $$G$$ be cyclic such that $$\lvert G \rvert = n$$ and $$h \in G$$. Then, $$\lvert h \rvert \Big\lvert n$$.

***Proof:*** Let $$g \in G$$ be such that $$\langle g \rangle = G$$. Since $$h \in G$$, there exists $$k \in \{ 0,\dots,n-1 \}$$ such that $$h = g^{k}$$. Thus, $$\lvert h \rvert = \lvert g^{k} \rvert = \frac{n}{\operatorname{gcd}(n,k)} \implies \lvert h \rvert \operatorname{gcd}(n,k) = n$$, from which the divisibility follows.

### Theorem (Equality of subgroups)

Let $$G$$ be a group and $$g \in G$$ such that $$\lvert g \rvert = n$$. The following are equivalent:

1. $$\operatorname{gcd}(k,n) = \operatorname{gcd}(\ell, n)$$
2. $$\langle g^{k} \rangle = \langle g^{\ell} \rangle$$.
3. $$\lvert g^{k} \rvert = \lvert g^{\ell} \rvert$$.

***Proof:*** $$(2) \implies (3)$$ is trivial. For $$(1) \implies (2)$$, assume that $$\operatorname{gcd}(k,n) = \operatorname{gcd}(\ell, n)$$. Note that

$$
\langle g^{k} \rangle = \langle g^{\operatorname{gcd}(n,k)} \rangle = \langle g^{\operatorname{gcd}(n,\ell)} \rangle = \langle g^{\ell} \rangle.
$$

Finally, for $$(3) \implies (1)$$, using the previous proposition, note that

$$
\lvert g^{k} \rvert = \lvert g^{\ell} \rvert \implies \frac{n}{\operatorname{gcd}(n,k)} = \frac{n}{\operatorname{gcd}(n, \ell)} \implies \operatorname{gcd}(n,k) = \operatorname{gcd}(n, \ell).
$$

### Corollary (Generating element of a cyclic group)

Let $$G = \langle g \rangle$$ with $$\lvert g \rvert=n$$. Let $$k \in \mathbb{Z}$$. Then $$G = \langle g^{k} \rangle \iff \operatorname{gcd}(n,k) = 1$$.

***Proof:*** By the previous theorem $$\langle g^{k} \rangle = \langle g^{1} \rangle \iff \operatorname{gcd}(n,k)=\operatorname{gcd}(n,1)  = 1$$.

### Theorem (A subgroup of a cyclic group is cyclic)

Let $$G$$ be a cyclic group and $$H \leq G$$. Then $$H$$ is cyclic.

***Proof:*** Let $$g \in G$$ be such that $$G = \langle g \rangle$$. If $$H$$ is the trivial subgroup, it is clearly cyclic. Suppose that $$H$$ is non-trivial. Let $$e \neq h \in H$$. Since $$h \in H \subseteq G = \langle g \rangle$$, there exists $$0 \neq k \in \mathbb{Z}$$ such that $$h = g^{k}$$. Define $$A = \{ n \in \mathbb{N}^{\ast} : g^{n} \in H\}$$. Note that $$A \neq \emptyset$$, since if $$k \geq 0$$, $$k \in A$$, and otherwise $$-k \in A$$ (as $$H$$ is a group, $$h^{-1} \in H$$). Hence, applying the well-ordering principle, $$A$$ has a minimal element $$\ell$$. We shall prove that $$H = \langle g^{\ell} \rangle$$. On the one hand, since $$\ell \in A$$, $$g^{\ell}\in H$$ and therefore $$\langle g^{\ell} \rangle \subseteq H$$. Now, take $$t \in H$$. There exists $$i \in \mathbb{Z}$$ such that $$t = g^{i}$$. Assuming that $$i \neq 0$$, by the division algorithm, there exist $$q,r \in \mathbb{Z}$$ with $$0\leq r<\ell$$ such that $$i = q\ell+r \implies r = i-q\ell$$. Thus, $$g^{r} = g^{i} \ast g^{-q \ell} \in H$$. If $$r\neq0$$, we have that $$r \in A$$, which contradicts the minimality of $$\ell$$. Conclude that $$r=0$$. Thus, $$t = g^{i} = (g^{\ell})^{q}$$, from which we have that $$t \in \langle g^{\ell} \rangle$$, we conclude that $$H = \langle g^{\ell} \rangle$$.

### Note (Finding the generator)

From the proof, we know how to find a generator of $$H$$ from a generator of $$G$$,

### Theorem (Lagrange for cyclic groups)

Let $$G$$ be a cyclic group such that $$\lvert G \rvert = n$$ and $$H \leq G$$. Then, $$\lvert H \rvert \Big\lvert n$$.

***Proof:*** Let $$g \in G$$ be such that $$\langle g \rangle=G$$ and $$H\leq G$$. Hence, $$H$$ is cyclic and there exists $$k \in \mathbb{N}$$ such that $$H = \langle g^{k} \rangle$$. Let $$d = \operatorname{gcd}(n,k)$$. Then,

$$
\lvert H \rvert  = \lvert \langle g^{k} \rangle  \rvert = \lvert g^{k} \rvert = \frac{n}{d}  \implies d \lvert H \rvert = n,
$$

from which the divisibility follows.

### Theorem (Uniqueness of orders in subgroups)

Let $$G$$ be a cyclic group with $$\lvert G \rvert = n$$ and let $$k \in \mathbb{N}$$ be such that $$k \mid n$$. Then there exists a unique subgroup $$H$$ of $$G$$ with $$\lvert H \rvert = k$$. Moreover, if $$G = \langle g \rangle$$ then $$H = \langle g^{n/k} \rangle$$

***Proof:*** Let $$\ell = \frac{n}{k} \in \mathbb{N}$$ (since $$k \mid n$$). Let $$H = \langle g^{\ell} \rangle$$. Then, $$\lvert H \rvert = \lvert \langle g^{\ell} \rangle  \rvert = \frac{n}{\operatorname{gcd}(n, \ell)}$$. Now, since $$n = k\ell$$ then $$\operatorname{gcd}(n, \ell) = \operatorname{gcd}(k\ell, \ell) = \ell \operatorname{gcd}(k,1) = \ell$$. Thus, $$\lvert H \rvert = \frac{n}{\ell} = k$$. Uniqueness is left as an exercise.
{% endraw %}
