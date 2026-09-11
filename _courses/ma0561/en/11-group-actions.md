---
layout: chapter
course: ma0561
chapter: 11
title: "Group Actions"
slug: 11-group-actions
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/11-group-actions/
---

{% raw %}
## Elementary definitions and properties

### Definition (Group Action)

Let $$(G, \cdot)$$ be a group and let $$X$$ be a set. We say that $$G$$ acts on $$X$$ (or that $$X$$ is a $$G$$-set) if there exists a function $$\alpha: G \times X \to X$$ such that

1. $$\forall g,h \in G  \quad\forall x \in X  \quad \Big( \alpha\big(g, \alpha(h,x)\big) = \alpha(g \cdot h, x)\Big)$$,
2. $$\forall x \in X  \quad\Big( \alpha(1_{G}, x) = x \Big)$$.

### Notation (Action of an element)

If $$G$$ acts on $$X$$, given $$g \in G$$, we denote by $$\alpha_{g}:X \to X$$ the map such that $$x \mapsto \alpha(g,x)$$. If we know the specific action, it is common to write $$g \cdot x$$.

### Note (Immediate properties)

1. For all $$g,h \in G$$ and for every $$x \in X$$, we have that $$\alpha_{g}(\alpha_{h}(x)) = \alpha_{g \cdot h}(x)$$.
2. $$\alpha_{1_{G}} = \mathrm{id}_{X}$$

### Examples (Standard actions)

1. Let $$n \in \mathbb{N}$$. Consider $$G = S_{n}$$ and $$X = \{ 1,\dots,n \}$$. Define $$\alpha: S_{n} \times X \to X$$ such that $$(\sigma, i) \mapsto \sigma(i)$$. Note that if $$\gamma,\sigma \in S_{n}$$, given $$i \in X$$,

    $$
    \alpha_{\sigma}(\alpha_{\gamma}(i)) = \alpha_{\sigma}(\gamma(i)) = (\sigma \circ \gamma)(i) = \alpha_{\sigma \circ \gamma} (i).
    $$

Moreover, $$\alpha_{\mathrm{id}}(i) = \mathrm{id}(i) = i$$. Therefore, $$\alpha$$ is a group action and $$S_{n}$$ acts on $$X$$.

1. Let $$G = (\mathbb{Z}, +)$$ and $$X = \mathbb{R}$$. Define $$\tau: G \times X \to X$$ such that $$(n,x) \mapsto x+ n$$. Note that, given $$m,n \in \mathbb{Z}$$ and $$x \in \mathbb{R}$$,

    $$
    \tau_{n}(\tau_{m(x)}) = \tau_{n}(x+m) = (x+m)+n = x + (m+n) = \tau_{m+n}(x).
    $$

Moreover, $$\tau_{0}(x) = x+0 = x$$. Therefore, $$\mathbb{Z}$$ acts on $$\mathbb{R}$$.

1. Let $$G = \mathrm{GL}_{n}(\mathbb{R})$$ and $$X = \mathbb{R}^{n}$$. Define $$\alpha: G \times X \to X$$ such that $$(A,v) \mapsto A v$$. Showing that $$\alpha$$ is a group action is left as an exercise.

1. Given a group $$G$$, define $$\mu:G \times G \to G$$ such that $$(g,h) \mapsto g \cdot h$$. It is easy to see that $$\mu$$ is a group action. Thus, $$G$$ acts on itself.

### Lemma (The action is bijective on $$X$$)

Let $$G$$ be a group and $$X$$ a set. Suppose that $$\alpha:G \times X \to X$$ is a group action. Then, if $$g \in G$$, the map $$\alpha_{g}: X \to X$$ such that $$x \mapsto \alpha(g,x)$$ is a bijection, i.e., $$\alpha_{g} \in S_{x}$$.

***Proof:*** Consider $$\alpha_{g^{-1}}:X \to X$$ such that $$x \mapsto \alpha(g^{-1}, x)$$. Note that

$$
(\alpha_{g} \circ \alpha_{g^{-1}})(x) = \alpha_{g \circ g ^{-1}}(x) = \alpha_{1_{G}}(x) = x.
$$

In the same way, $$(\alpha_{g^{-1}} \circ \alpha_{g}) = \mathrm{id}_{X}$$, from which we conclude that the map is bijective.

### Theorem (Actions and homomorphisms are in bijection)

Let $$G$$ be a group and $$X$$ a set. Define

$$
\begin{aligned}
\Omega:&= \{ \alpha: G \times X  \to X: \alpha \text{ is an action of } G \text{ on }X\},\\
\Sigma:&= \{ \phi: G \to S_{X} : \phi \text{ is a group homomorphism} \}.
\end{aligned}
$$

Then $$\Omega$$ and $$\Sigma$$ are in bijection

***Proof:*** Define $$\Phi: \Omega \to \Sigma$$ as follows. Given an action $$\alpha: G \times X \to X$$, define $$\phi:G \to S_{X}$$ such that $$\phi(g) = \alpha_{g}$$ where $$\alpha_{g}:X \to X$$ is such that $$x \mapsto\alpha(g,x)$$. It is easy to see that $$\phi$$ is a homomorphism and that $$\alpha_{g} \in S_{X}$$. Take $$\Phi(\alpha) = \phi$$.
Now, define $$\Psi: \Sigma \to \Omega$$ as follows. Given a homomorphism $$\phi:G\to S_{X}$$, let $$\alpha:G \times X \to X$$ be such that $$(g,x) \mapsto \phi(g)(x) \in X$$. Note that $$\alpha$$ is an action, since if $$g,h \in G$$ and $$x \in X$$, we have that

$$
\begin{aligned}
\alpha(g \cdot h,x) = \phi(gh) (x) &= (\phi(g) \circ \phi(h))(x) \\
&= \phi(g) \big(\phi(h)(x)\big) \\
&=\phi(g) (\alpha(h, x)) \\
&=\alpha(g, \alpha(h,x)),
\end{aligned}
$$

and moreover, given $$x \in X$$, $$\alpha(1_{G}, x) = \phi(1_{G})(x) = \mathrm{id}_{X}(x) = x$$. Take $$\Psi(\phi) = \alpha$$. Verifying that $$\Phi \circ \Psi = \mathrm{id}_{\Sigma}$$ and that $$\Psi \circ \Phi = \mathrm{id}_{\Omega}$$ is left as an exercise.

### Theorem (Cayley)

Given a group $$G$$, $$G$$ is isomorphic to a subgroup of $$S_{G}$$.

***Proof:*** Consider $$\mu_{g}:G \to G$$ such that $$h \mapsto g\cdot h$$. Let $$\phi: G \to S_{G}$$ be such that $$g \mapsto \mu_{g}$$. We have already seen that $$\phi$$ is a homomorphism. Let us see that $$\phi$$ is injective:

$$
g \in \operatorname{Ker}(\phi) \iff \phi(g) = \mu_{g}= \mathrm{id}_{G} \iff g \cdot x = x  \quad \forall x \in G \iff g =1_{G},
$$

so that $$\operatorname{Ker}(\phi) = \{ 1_{G} \}$$. Now, using the first isomorphism theorem, we obtain that

$$
G / \operatorname{Ker}(\phi) = G/\{ 1_{G} \} = G\cong \operatorname{Im}(\phi) \leq  S_{G},
$$

from which we conclude the result.
{% endraw %}
