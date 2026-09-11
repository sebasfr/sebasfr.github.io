---
layout: chapter
course: ma0505
chapter: 4
title: "Continuity"
slug: 04-continuity
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/04-continuity/
---

{% raw %}
## Definitions and examples

### Definition (Limit of a function between metric spaces)

Let $$(X, d), (Y, \rho)$$ be metric spaces, $$f : X \to Y$$, $$a \in X$$ and $$\ell \in Y$$. We say that $$\lim_{z \to a} f(z) = \ell$$ if for every $$\varepsilon > 0$$ there exists $$\delta > 0$$ such that

$$
0 < d(z, a) < \delta \implies \rho(f(z), \ell) < \varepsilon.
$$

Note that to define the limit it is not necessary that $$f$$ be defined at $$a$$.

### Definition (Continuous function)

The function $$f : X \to Y$$ is *continuous* at $$a \in X$$ if $$\lim_{z \to a} f(z) = f(a)$$. That is, for every $$\varepsilon > 0$$ there exists $$\delta > 0$$ such that

$$
d(z, a) < \delta \implies \rho(f(z), f(a)) < \varepsilon,
$$

or equivalently, $$f(B_{X}(a, \delta)) \subseteq B_{Y}(f(a), \varepsilon)$$. We simply say that $$f$$ is *continuous* if it is so at every point of $$X$$.

### Definition (Lipschitz function)

$$f : X \to Y$$ is *$$\lambda$$-Lipschitz* if for all $$x, y \in X$$,

$$
\rho(f(x), f(y)) \leq \lambda\, d(x, y).
$$

We simply say that $$f$$ is *Lipschitz* if there exists $$\lambda \geq 0$$ with this property.

### Example (The distance to a point is $$1$$-Lipschitz)

Let $$(X, d)$$ be a metric space and $$a \in X$$. The function $$f(x) = d(x, a)$$ is $$1$$-Lipschitz, since from the triangle inequality

$$
|d(x, a) - d(y, a)| \leq d(x, y),
$$

that is $$|f(x) - f(y)| \leq d(x, y)$$. In particular $$f$$ is continuous.

## Topological characterisations of continuity

### Lemma (Continuity and preimages of open sets)

If $$f : X \to Y$$ is continuous and $$G \subseteq Y$$ is open, then $$f^{-1}(G)$$ is open in $$X$$.

***Proof:*** Let $$x_{0} \in f^{-1}(G)$$ and $$y_{0} = f(x_{0}) \in G$$. Since $$G$$ is open, there exists $$\varepsilon > 0$$ with $$B_{Y}(y_{0}, \varepsilon) \subseteq G$$. By continuity of $$f$$ at $$x_{0}$$, there exists $$\delta > 0$$ such that $$f(B_{X}(x_{0}, \delta)) \subseteq B_{Y}(y_{0}, \varepsilon) \subseteq G$$, that is $$B_{X}(x_{0}, \delta) \subseteq f^{-1}(G)$$.

### Theorem (Characterisations of continuity)

Let $$f : X \to Y$$. The following are equivalent:

1. $$f$$ is continuous;
2. $$f^{-1}(G)$$ is open in $$X$$ for every open $$G \subseteq Y$$;
3. $$f^{-1}(F)$$ is closed in $$X$$ for every closed $$F \subseteq Y$$;
4. $$f(\overline{B}) \subseteq \overline{f(B)}$$ for every $$B \subseteq X$$ (closure in $$X$$ on the left, in $$Y$$ on the right).

***Proof:*** $$(1) \implies (2)$$: Proved in the previous lemma.

$$(2) \implies (1)$$: Given $$\varepsilon > 0$$ and $$a \in X$$, $$B_{Y}(f(a), \varepsilon)$$ is open, so $$f^{-1}(B_{Y}(f(a), \varepsilon))$$ is open. Since $$a \in f^{-1}(B_{Y}(f(a), \varepsilon))$$, there exists $$\delta > 0$$ with $$B_{X}(a, \delta) \subseteq f^{-1}(B_{Y}(f(a), \varepsilon))$$, i.e. $$f(B_{X}(a, \delta)) \subseteq B_{Y}(f(a), \varepsilon)$$.

$$(2) \iff (3)$$: If $$F \subseteq Y$$ is closed, then $$Y \setminus F$$ is open and $$f^{-1}(Y \setminus F) = X \setminus f^{-1}(F)$$. Hence $$f^{-1}(F)$$ is closed if and only if $$f^{-1}(Y\setminus F)$$ is open.

$$(3) \iff (4)$$: $$f(\overline{B}) \subseteq \overline{f(B)}$$ for every $$B$$ is equivalent to $$\overline{B} \subseteq f^{-1}(\overline{f(B)})$$ for every $$B$$. Taking $$B = f^{-1}(F)$$ with $$F$$ closed, one obtains $$\overline{f^{-1}(F)} \subseteq f^{-1}(F)$$, that is $$f^{-1}(F)$$ closed, and conversely.

### Theorem (Characterisation by sequences)

Let $$f : X \to Y$$ and $$a \in X$$. Then $$f$$ is continuous at $$a$$ if and only if for every sequence $$\{ x_{n}\}_{n \in \mathbb{N}} \subseteq X$$ with $$x_{n} \to a$$ we have $$f(x_{n}) \to f(a)$$.

***Proof:*** $$(\implies)$$: If $$x_{n} \to a$$ and $$\varepsilon > 0$$, by continuity there exists $$\delta > 0$$ with $$d(x, a) < \delta \implies \rho(f(x), f(a)) < \varepsilon$$. Take $$n_{0}$$ such that $$n \geq n_{0}$$ implies $$d(x_{n}, a) < \delta$$; then $$\rho(f(x_{n}), f(a)) < \varepsilon$$, that is $$f(x_{n}) \to f(a)$$.

$$(\impliedby)$$: If $$f$$ were not continuous at $$a$$, there would exist $$\varepsilon > 0$$ such that for every $$\delta > 0$$ there exists $$x_{\delta} \in X$$ with $$d(x_{\delta}, a) < \delta$$ and $$\rho(f(x_{\delta}), f(a)) \geq \varepsilon$$. Taking $$\delta = 1/n$$ one obtains $$x_{n}$$ with $$d(x_{n}, a) < 1/n$$ and $$\rho(f(x_{n}), f(a)) \geq \varepsilon$$. Thus $$x_{n} \to a$$ but $$f(x_{n}) \not\to f(a)$$, a contradiction.

## Homeomorphisms and isometries

### Definition (Homeomorphism)

Let $$f : X \to Y$$. We say that $$f$$ is a *homeomorphism* if $$f$$ is continuous, bijective and $$f^{-1}$$ is continuous. In that case, $$X$$ and $$Y$$ are said to be *homeomorphic*.

### Note (Homeomorphisms map open sets to open sets)

If $$f : X \to Y$$ is a homeomorphism and $$A \subseteq X$$ is open, then $$f(A) = (f^{-1})^{-1}(A)$$ is open in $$Y$$.

### Exercise (Homeomorphisms preserve the interior)

If $$f : X \to Y$$ is a homeomorphism and $$A \subseteq X$$, then $$f(A^{\circ}) = (f(A))^{\circ}$$.

### Definition (Isometry)

Let $$\phi : (X, d_X) \to (Y, d_Y)$$. We say that $$\phi$$ is an *isometry* if $$\phi$$ is surjective and preserves the metric, that is, if for all $$x,y \in X$$,

$$
d_Y(\phi(x), \phi(y)) = d_X(x,y).
$$

### Note (Every isometry is bijective)

If $$\phi : (X, d_X) \to (Y, d_Y)$$ is an isometry, then $$\phi$$ is injective, since if $$\phi(x) = \phi(y)$$ then $$d_Y(\phi(x),\phi(y))=d_X(x,y) = 0$$, whence we have that $$x=y$$.
{% endraw %}
