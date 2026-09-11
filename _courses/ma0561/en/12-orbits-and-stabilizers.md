---
layout: chapter
course: ma0561
chapter: 12
title: "Orbits and Stabilizers"
slug: 12-orbits-and-stabilizers
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/12-orbits-and-stabilizers/
---

{% raw %}
## Orbits and stabilizers

Let $$G$$ be a group and $$X$$ a set. Let $$\alpha$$ be an action of $$G$$ on $$X$$. Define the relation $$\sim$$ on $$X$$ such that $$x \sim y \iff \exists g \in G \Big(\alpha_{g}(x) = y\Big)$$. It is easy to see that $$\sim$$ is an equivalence relation.

### Definition (Orbit)

Let $$G$$ be a group and $$X$$ a set such that $$G$$ acts on $$X$$ by the action $$\alpha$$. Given the equivalence relation $$\sim$$ defined above, we define the orbit of $$x \in X$$ as

$$
\mathcal{O}_{x} := \{ y \in X:y \sim x \} = \{ y \in X: \exists g \in G \big( \alpha_{g}(x) = y \big) \}.
$$

Since $$\sim$$ is an equivalence relation, the orbits form a partition of $$X$$, i.e., $$X = \dot\bigcup_{x \in X} \mathcal{O}_{x}$$.

### Definition (Transitive action)

Let $$G$$ be a group and $$X$$ a set such that $$G$$ acts on $$X$$. If there exists $$x \in X$$ such that $$\mathcal{O}_{x} =X$$ we say that the action is transitive. Equivalently, the action is transitive if for all $$x,y \in X$$ there exists $$g \in G$$ such that $$x = \alpha_{g}(y)$$.

### Definition (Stabilizer)

Let $$G$$ be a group and $$X$$ a set such that $$G$$ acts on $$X$$ by the action $$\alpha$$. Given $$x \in X$$, we define the stabilizer of $$x$$ by $$G_{x}:= \{ g \in G:\alpha_{g}(x)=x \}$$.

### Lemma (Stabilizer is a subgroup)

***Proof:*** $$G_{x} \neq \emptyset$$ since $$1_{G} \in G_{x}$$ by definition. Now, let $$g,h \in G_{x}$$. Note that $$\alpha_{h^{-1}}(x) = (\alpha_{h})^{-1}(x) = x$$. Finally, we have that

$$
\alpha_{gh^{-1}}(x) = \alpha_{g}(\alpha_{h^{-1}}(x)) = x,
$$

so that $$g \cdot h^{-1} \in G_{x}$$, from which we conclude that $$G_{x} \leq G$$.

### Examples (Orbits and stabilizers)

1. Let $$n\geq2$$. Consider the action of $$S_{n}$$ on $$X = \{ 1,\dots,n \}$$ such that $$\alpha_{\sigma}(i) = \sigma(i)$$. In this case there is a single orbit. Let $$i,j \in X$$ and consider $$\tau = \begin{pmatrix}i & j\end{pmatrix}$$. Note that $$\alpha_{\tau}(i) = j$$, so that $$i \sim j$$, i.e., any two elements of $$X$$ are related. Hence the action is transitive. Now, note that if $$1 \leq i\leq n$$, $$G_{i} = \{ \sigma \in S_{n}: \sigma(i) = i \} \cong S_{n-1}$$.

1. Consider $$G = (\mathbb{Z}, + )$$ and $$X=\mathbb{R}$$ under the action $$\tau(n,x) = x+n$$. Note that if $$x,y \in \mathbb{R}$$,

    $$
    x \sim y \iff \exists n \in \mathbb{Z} \Big(\tau_{n}(x) = y\Big) \iff \exists n \in \mathbb{Z} \Big(y=x+n\Big) \iff x-y \in \mathbb{Z},
    $$

from which we have that $$x$$ and $$y$$ have the same decimal part. There is an uncountable number of orders. It is evident that for every $$x \in \mathbb{R}$$, $$G_{x} = \{ 0 \}$$.

1. Consider $$G = \mathbb{S}^{1} =\{ e^{i\theta}:\theta \in [0, 2\pi) \}$$ and $$X = \mathbb{C}$$. Define the action $$\rho_{\theta}(z) = z e^{i \theta}$$ (checking that this is an action is an exercise). Let $$z \in \mathbb{C}$$. Then,

    $$
    \mathcal{O}_{z} = \{ \rho_{\theta}(z): \theta \in [0, 2\pi) \} = \{ ze^{i \theta}: \theta \in [0,2\pi) \} = \{ w \in \mathbb{C}: \lvert w \rvert  = \lvert z \rvert  \}.
    $$

Now, let us see what happens with the stabilizer. If $$z = 0$$, we have that

$$
G_{0} = \{ \theta \in \mathbb{S}^{1}: \rho_{\theta}(0) = 0 \} = \{ g \in \mathbb{S}^{1}: 0 e^{i \theta} = 0 \} = \mathbb{S}^{1}.
$$

On the other hand, if $$z \neq 0$$,

$$
\rho_{\theta}(z) = z \iff z e^{i \theta} = z \iff \theta = 0 \iff e^{i \theta } = 1,
$$

which implies that $$G_{Z} = \{ 1 \}$$.

1. Let $$G$$ be a group and $$H \leq G$$. Consider $$G / H = \{ gH : g \in G\}$$. Define an action of $$G$$ on $$G / H$$ such that $$\mu:G \times G / H\to G /H$$ such that $$\mu_{g}(hH) = (g \cdot h) H$$. It is left as an exercise to see that $$\mu$$ is a transitive action. Now, note that

    $$
    g \in G_{xH} \iff (g \cdot x) H = xH \iff x ^{-1} \cdot g \cdot x \in H \iff g \in x H x ^{-1},
    $$

so that $$G_{xH} = xH x ^{-1}$$.

1. Let $$G = \mathrm{GL}(n,\mathbb{R})$$ and $$X = \mathbb{R}^n$$. Define the action $$\alpha_{A}(v)=Av$$. Note that

    $$
    \mathcal{O}_{0} = \{ v \in \mathbb{R}: \exists A \in G (Av = w) \} = \{ 0 \}.
    $$

Hence this action is not transitive.

1. Let $$G$$ be a group. Define $$\mu:G\to G$$ such that $$\mu_{g}(h) = gh$$. Let $$h,g \in G$$. Note that $$\mu_{gh^{-1}}(h) = (gh^{-1})h=g$$, so that $$h \sim g$$. Hence the action is transitive.

1. Let $$G$$ be a group and consider the action of $$G$$ on $$G$$ given by conjugation $$\mu_{g}(h) = ghg^{-1}$$. Let $$x \in G$$. We have that

    $$
    x^G := O_{x} = \{ y \in G: \exists g \in G (g xg^{-1} = y) \} = \{ gxg^{-1}:g \in G \}.
    $$

On the other hand, $$G_{x}:= \{ g \in G: gxg^{-1} = x \} = C_{G}(x)$$ (the centralizer).

### Theorem (Orbit and quotient of the stabilizer)

Let $$G$$ be a group and $$X$$ a set such that $$G$$ acts on $$X$$. Let $$x \in X$$. Then $$\lvert \mathcal{O}_{x} \rvert = [G:G_{x}]$$.

***Proof:*** We shall construct a bijection $$\Phi:\mathcal{O}_{x} \to G / G_{x}$$. Let $$y \in \mathcal{O}_{x}$$. Then there exists $$g \in G$$ such that $$\alpha_{g}(x) = y$$. Define $$\Phi(y) = g \cdot G_{x}$$. $$\Phi$$ is well defined, since if $$g,h$$ are such that $$\alpha_{g}(x) = \alpha_{h}(x)$$, then

$$
\alpha_{h^{-1}g}(x) = \alpha_{h^{-1}}(\alpha_{g}(x)) = \alpha_{h^{-1}}(\alpha_{h}(x)) = \alpha_{1_{G}}(x) = x,
$$

so that $$h^{-1}g \in G_{x}$$ and hence $$g \cdot G_{x} = h \cdot G_{x}$$. $$\Phi$$ is injective since if $$y,z \in \mathcal{O}_{x}$$ are such that $$\Phi(y) = \Phi(z)$$, there exist $$g,h \in G$$ such that $$\alpha_{g}(x) = y$$ and $$\alpha_{h}(x) = z$$. Thus, we have that

$$
g G_{x} = h G_{x} \implies h^{-1} g \in G_{x} \implies \alpha_{h^{-1}g}(x)=x.
$$

Thus, $$\alpha_{h^{-1}}(\alpha_{g}(x)) = \alpha_{h}^{-1}(\alpha_{g}(x)) = x \implies \alpha_{g}(x)=\alpha_{h}(x)$$. Finally $$\Phi$$ is surjective, since if $$g \cdot G_{x} \in G / G_{x}$$, take $$y = \alpha_{g}(x)$$. Note that $$\Phi(y) = g \cdot G_{x}$$. Thus, $$\Phi$$ is a bijection and hence the given sets have the same cardinality.

### Corollary (The orbit divides the order of the group)

Let $$G$$ be a finite group and $$X$$ a set such that $$G$$ acts on $$X$$. Then for every $$x \in X$$, $$\lvert \mathcal{O}_{x} \rvert \Big\lvert \lvert G \rvert$$.

***Proof:*** We have that $$\lvert \mathcal{O}_{x} \rvert = [G:G_{x}] =\frac{ \lvert G \rvert}{\lvert G_{x} \rvert}$$, from which we conclude the result

### Corollary (Size of the conjugacy class)

Let $$G$$ be a finite group and $$x \in G$$, Then $$\lvert x^{G} \rvert = [G:C_{G}(x)]$$.

### Theorem (Cauchy)

Let $$G$$ be a finite group and $$p$$ a prime such that $$p \Big\lvert \lvert G \rvert$$. Then there exists $$g \in G$$ such that $$\lvert g \rvert = p$$.

***Proof:*** [**Proof 1, for abelian groups.**]
Suppose that $$G$$ is abelian. We proceed by strong induction on $$\lvert G \rvert=n$$. The base case ($$n=1$$) is trivially true, vacuously. Suppose as inductive hypothesis that the result is true for every group $$H$$ such that $$\lvert H \rvert < n$$. Let $$a \in G$$ with $$a \neq 1_{G}$$ and $$k = \lvert  a \rvert$$. Consider the following cases:
**Case 1:** Suppose that $$p \mid k$$. Then, there exists $$\ell \in \mathbb{N}$$ such that $$p \ell = k$$. Hence $$\lvert a^{\ell} \rvert = p$$.
**Case 2:** Suppose that $$p \not\mid k$$. Let $$H = \langle a \rangle$$. Since $$G$$ is abelian, $$H \triangleleft G$$, so that $$G/H$$ is a group and $$\lvert H \rvert = k$$. Note that

$$
\lvert G / H \rvert = \frac{\lvert G \rvert }{\lvert H \rvert } = \frac{n}{k} < n.
$$

Since $$p \mid n$$ and $$p \not\mid k$$, $$p \mid \frac{n}{k}$$. By the inductive hypothesis, there exists $$sH \in G /H$$ such that $$\lvert sH \rvert = p$$. Let $$m = \lvert s \rvert$$. Note that $$(sH)^{m} = s^{m}H = H$$, so that $$p \mid m$$. Finally, apply case 1 to $$s$$. We conclude the result

***Proof:*** [**Proof 2, general.**]
Let $$x \in G$$. Recall that $$x^{G} = \{ g x g^{-1}: g \in G \}$$ and that $$\lvert x^{G} \rvert = [G:C_{G}(x)]$$. We proceed by strong induction on $$\lvert G \rvert=n$$. Consider the following cases:
**Case 1:** If $$x \in Z(G)$$, then $$x^{G}=\{ x \} \implies G = C_{G}(x)$$.
**Case 2:** If $$x \not\in Z(G)$$, then $$\lvert x^{G} \rvert > 1$$. Then $$C_{G}(x) < G \implies \lvert C_{G}(x) \rvert < \lvert G \rvert$$. If $$p \Big\lvert \lvert C_{G}(x) \rvert$$, by the inductive hypothesis, there exists $$g \in C_{G}(x) \subseteq G$$ such that $$\lvert g \rvert=p$$, from which we conclude the result. If $$p \not\Big\lvert \lvert C_{G}(x) \rvert$$, we have that

$$
[G:C_{G}(x)] = \frac{\lvert G \rvert }{\lvert C_{G}(x) \rvert } \implies [G:C_{G}(x)] \cdot \lvert C_{G}(x) \rvert = \lvert G \rvert \implies p \mid [G:C_{G}(x)].
$$

Let $$x_{1},\dots,x_{k}$$ be the distinct conjugacy classes obtained through the relation of being conjugate and which are not in $$Z(G)$$. Then,

$$
G = Z(G) \dot{\cup} \bigcup_{i=1}^{k} x_{i}^{G} \implies \lvert G \rvert = \lvert Z(G) \rvert + \sum_{i=1}^{k} \lvert x_{i}^{G} \rvert \implies \lvert G \rvert - \sum_{i=1}^{k} \lvert x_{i}^{G} \rvert = \lvert Z(G) \rvert,
$$

from which we conclude that $$p \Big\lvert \lvert Z(G) \rvert$$. Thus, $$Z(G)$$ is a proper subgroup of $$G$$, and we conclude the result by applying the inductive hypothesis to $$Z(G)$$.

### Note (The primality hypothesis is necessary)

The theorem is false if $$p$$ is not prime. Note that $$8 \mid 120 \implies 8 \Big\lvert \lvert S_{5} \rvert$$. But we have seen that there are no subgroups of order 8 in $$S_{5}$$.

### Definition ($$p$$-group)

Let $$p$$ be prime. A group $$G$$ is a $$p$$-group if there exists $$k \in \mathbb{N}$$ such that $$\lvert G \rvert=p^{k}$$.

### Exercise (Centre of a $$p$$-group)

If $$G$$ is a $$p$$-group, $$Z(G) \neq \{ 1_{G} \}$$.

### Corollary (Groups of order $$p^{2}$$)

If $$p$$ is prime and $$\lvert G \rvert = p^{2}$$, then $$G$$ is abelian.

***Proof:*** Suppose that $$G$$ is not abelian. Then $$Z(G)$$ is a proper subgroup of $$G$$. By Lagrange, $$\lvert Z(G) \rvert \in \{ 1,p \}$$. By the previous exercise, $$\lvert Z(G) \rvert = p$$. We know that $$Z(G) \triangleleft G$$. Thus, $$\lvert G / Z(G) \rvert = \frac{\lvert G \rvert}{\lvert Z(G) \rvert} = p$$, from which we conclude that $$G / Z(G)$$ is cyclic and hence $$G$$ is abelian.

### Theorem (Subgroups of a finite abelian group)

Let $$G$$ be a finite abelian group. Then $$G$$ has a subgroup of order $$d$$ for every $$d$$ such that $$d \Big\lvert \lvert G \rvert$$.

***Proof:*** Let $$n = \lvert G \rvert$$. Proceed by strong induction on $$d$$, with $$d \mid n$$. The base case is trivial, since if $$H = \{ 1_{G} \}\implies \lvert H \rvert=1$$. Let $$d>1$$. Suppose as inductive hypothesis that for every $$e < d$$ and every group $$\tilde{G}$$ with $$e \Big\lvert \lvert \tilde{G} \rvert$$ there exists $$\tilde{H} < \tilde{G}$$ such that $$\lvert \tilde{H} \rvert = e$$. Since $$d \mid n$$, there exists $$k \in \mathbb{N}$$ such that $$kd=n$$. Since $$d>1$$, there exists a prime $$p$$ such that $$p \mid d$$, i.e., there exists $$\ell \in \mathbb{N}$$ such that $$\ell p = d$$. By Cauchy's theorem, there exists $$g \in G$$ such that $$\lvert g \rvert=p$$. Let $$H = \langle g \rangle$$. Note that $$H$$ is cyclic, and hence abelian and normal. Hence, $$G / H$$ is a group. Thus,

$$
\lvert G / H \rvert = \frac{\lvert G \rvert }{\lvert H \rvert } = \frac{n}{p} = \frac{kd}{p} = \frac{k \ell p}{p} = k \ell.
$$

Thus, $$\ell \Big\lvert \lvert G / H \rvert$$ and $$\lvert G/H \rvert < n$$. Since $$\ell < d$$, by the inductive hypothesis, there exists $$S^{\ast} < G / H$$ such that $$\lvert S^{\ast} \rvert = \ell$$. By the correspondence theorem, there exists $$S < G$$ such that $$H \leq S \leq G$$ and $$S^{\ast} = S/H$$. We conclude by noting that

$$
\ell = \lvert S^{\ast} \rvert = \frac{\lvert S \rvert}{\lvert H \rvert } = \frac{\lvert S \rvert}{p} \implies \lvert S \rvert = \ell p =d,
$$

from which the result follows.

### Theorem (Subgroups of a $$p$$-group)

Let $$G$$ be a $$p-grupo$$ such that $$\lvert G \rvert = p^{e}$$. Then for every $$k \leq e$$, there exists $$H \leq G$$ such that $$\lvert H \rvert = p^{k}$$.

***Proof:*** We proceed by induction on $$e$$. For $$e=0$$, we have that $$G=\{ 1_{G} \}.$$ Take $$H = G$$. Let $$e > 0$$ and let $$k \leq e$$. Suppose as inductive hypothesis that the result is true for $$f<e$$. Since $$\lvert G \rvert = p^{e}$$ and $$e>0$$, then $$Z(G)$$ is non-trivial. Consider the following cases.

- If $$G = Z(G)$$, then $$G$$ is abelian. By the previous theorem, we conclude the result.
- Now, if $$G \neq Z(G)$$, there exists $$c < e$$ such that $$\lvert Z(G) \rvert = p^{c}$$ with $$c<e$$. If $$k \leq c$$, then by the inductive hypothesis applied to $$Z(G)$$, there exists $$H \triangleleft Z(G)$$ such that $$\lvert H \rvert=p^{k}$$. On the other hand, if $$k>c$$, we know that $$G / Z(G)$$ is a group (since $$Z(G) \triangleleft G$$). Now, note that

    $$
    \lvert G / Z(G) \rvert = \frac{\lvert G \rvert }{\lvert Z(G) \rvert } = p^{e-c}.
    $$

Applying the inductive hypothesis to $$G / Z(G)$$, there exists $$S^{\ast} \leq G/Z(G)$$ such that $$\lvert S^{\ast} \rvert = p^{k-c}$$. By the correspondence theorem, there exists $$S \leq G$$ such that $$Z(G) \leq S \leq G$$ and $$S^{\ast} = S / Z(G)$$. Thus,

$$
\lvert S^{\ast} \rvert \cdot \lvert Z(G) \rvert = \lvert S \rvert \implies p^{k-c} \cdot p^{c} = \lvert S \rvert,
$$

from which we conclude the result.
{% endraw %}
