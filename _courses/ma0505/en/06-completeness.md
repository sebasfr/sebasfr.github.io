---
layout: chapter
course: ma0505
chapter: 6
title: "Completeness"
slug: 06-completeness
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/06-completeness/
---

{% raw %}
## Cauchy sequences and complete spaces

### Definition (Cauchy sequence)

A sequence $$\{x_{n}\}_{n=1}^{\infty}$$ in $$(X, d)$$ is *Cauchy* if for every $$\varepsilon > 0$$ there exists $$n_{0} \in \mathbb{N}$$ such that

$$
n, m \geq n_{0} \implies d(x_{n}, x_{m}) < \varepsilon.
$$

Unlike compactness, this notion is *intrinsic* to the metric space.

### Exercise (Reminder on Cauchy sequences)

1. Every convergent sequence is Cauchy.
2. Every Cauchy sequence is bounded.

### Definition (Complete metric space)

$$(X, d)$$ is *complete* if every Cauchy sequence in $$X$$ converges in $$X$$.

### Example ($$(\mathcal{C}([0,1], \mathbb{R}), d_{\infty})$$ is complete)

Let $$\mathcal{C} = \{ f : [0,1] \to \mathbb{R} \;:\; f \text{ continuous}\}$$ with $$d_{\infty}(f, g) = \sup_{x \in [0,1]} |f(x) - g(x)|$$. Let $$\{f_{n}\}_{n=1}^{\infty}$$ be Cauchy. For each $$x \in [0,1]$$, $$|f_{n}(x) - f_{m}(x)| \leq d_{\infty}(f_{n}, f_{m})$$, so $$\{f_{n}(x)\}_{n=1}^{\infty}$$ is Cauchy in $$\mathbb{R}$$. Since $$\mathbb{R}$$ is complete, define $$f(x) = \lim_{n \to \infty} f_{n}(x)$$.

Let us show that $$f \in \mathcal{C}$$. Given $$\varepsilon > 0$$, fix $$n_{0}$$ with $$d_{\infty}(f_{n}, f_{m}) < \varepsilon/2$$ for $$n, m \geq n_{0}$$. For $$x \in [0,1]$$, there exists $$m_{1} \geq n_{0}$$ with $$|f(x) - f_{m_{1}}(x)| < \varepsilon/2$$, hence for $$n \geq n_{0}$$,

$$
|f(x) - f_{n}(x)| \leq |f(x) - f_{m_{1}}(x)| + d_{\infty}(f_{m_{1}}, f_{n}) < \tfrac{\varepsilon}{2} + \tfrac{\varepsilon}{2} = \varepsilon.
$$

Therefore $$f_{n} \to f$$ uniformly and, being a uniform limit of continuous functions, $$f$$ is continuous.

### Note (Strategy for proving that a Cauchy sequence converges)

As usual, to prove that a Cauchy sequence converges one begins by finding a *candidate* for the limit and then verifies convergence towards it.

## Completeness and closed sets

### Lemma (Characterisation of complete subspaces as closed sets)

Let $$(X, d)$$ be a metric space and $$C \subseteq X$$. Then:

1. If $$(C, d)$$ is complete, then $$C$$ is closed in $$(X, d)$$;
2. If $$X$$ is complete and $$C$$ is closed in $$X$$, then $$(C, d)$$ is complete.

***Proof:*** *(2)*: Let $$\{x_{n}\}_{n=1}^{\infty} \subseteq C$$ be Cauchy. Since $$X$$ is complete, there exists $$x \in X$$ with $$x_{n} \to x$$. As $$C$$ is closed, $$x \in C$$, so $$\{x_{n}\}$$ converges in $$C$$.

*(1)*: Let $$x \in \overline{C}$$ and take $$\{x_{n}\}_{n=1}^{\infty} \subseteq C$$ with $$x_{n} \to x$$ in $$X$$. Since $$\{x_{n}\}$$ is convergent, it is Cauchy in $$C$$. By completeness of $$C$$, there exists $$x' \in C$$ with $$x_{n} \to x'$$. By uniqueness of the limit, $$x = x' \in C$$, which proves $$\overline{C} \subseteq C$$.

### Lemma (Compact implies complete)

If $$(X, d)$$ is compact, then $$(X, d)$$ is complete.

***Proof:*** Let $$\{x_{n}\}_{n=1}^{\infty}$$ be Cauchy. By compactness there exists $$\{x_{n_{k}}\}$$ converging to $$x \in X$$. Given $$\varepsilon > 0$$, there exist $$n_{0}, k_{0}$$ with $$n, m \geq n_{0} \implies d(x_{n}, x_{m}) < \varepsilon/2$$ and $$k \geq k_{0} \implies d(x, x_{n_{k}}) < \varepsilon/2$$. For $$n, k \geq \max\{n_{0}, k_{0}\}$$,

$$
d(x_{n}, x) \leq d(x_{n}, x_{n_{k}}) + d(x_{n_{k}}, x) < \tfrac{\varepsilon}{2} + \tfrac{\varepsilon}{2} = \varepsilon.
$$

### Note (Completeness does not imply compactness)

The converse implication is false: $$\mathbb{R}$$ is complete but not compact.

## Totally bounded sets

### Definition (Totally bounded space)

$$(X, d)$$ is *totally bounded* (or *paracompact*) if for every $$\varepsilon > 0$$ there exist $$x_{1}, \dots, x_{m} \in X$$ such that

$$
X = \bigcup_{i=1}^{m} B(x_{i}, \varepsilon).
$$

In particular, every compact space is totally bounded.

### Example (Bounded but not totally bounded)

Consider $$\rho : \mathbb{N} \times \mathbb{N} \to \{0, 1\}$$ with $$\rho(n, m) = 1$$ if $$n \neq m$$ and $$\rho(n, n) = 0$$. For any $$n$$, $$\mathbb{N} = B(n, 2)$$, so $$(\mathbb{N}, \rho)$$ is bounded. However, $$B(n, 1/2) = \{n\}$$, so it is not possible to cover $$\mathbb{N}$$ with a finite collection of balls of radius $$1/2$$. We conclude that $$(\mathbb{N}, \rho)$$ is bounded but not totally bounded.

### Exercise (Sequences taking finitely many values admit a convergent subsequence)

If the set $$\{ x_{n} : n \in \mathbb{N}\}$$ is finite, then there exists a subsequence $$\{x_{n_{k}}\}_{k=1}^{\infty}$$ converging to a point of the sequence.

### Lemma (Characterisation of total boundedness by Cauchy subsequences)

$$(X, d)$$ is totally bounded if and only if every sequence $$\{x_{n}\}_{n=1}^{\infty} \subseteq X$$ has a Cauchy subsequence.

***Proof:*** $$(\implies)$$: By the previous exercise, we may assume that the sequence takes infinitely many distinct values. Since $$X$$ is totally bounded there exist $$y_{1}, \dots, y_{m}$$ with $$X \subseteq \bigcup_{i=1}^{m} B(y_{i}, 1)$$. One of these $$B(y_{i_{1}}, 1)$$ contains infinitely many points of $$\{x_{n}\}$$; let $$\{x_{n_{k,1}}\}_{k=1}^{\infty}$$ be the corresponding subsequence.

Iterating, at step $$\ell$$ there exist $$\tilde{y}_{\ell}$$ and a subsequence $$\{x_{n_{k,\ell}}\}_{k=1}^{\infty} \subseteq B(\tilde{y}_{\ell}, 1/\ell)$$ extracted from $$\{x_{n_{k,\ell-1}}\}$$. Note that $$d(x_{n_{k,\ell}}, x_{n_{s,\ell}}) < 2/\ell$$ for all $$k, s$$. Consider the diagonal subsequence $$\{x_{n_{\ell,\ell}}\}_{\ell=1}^{\infty}$$: if $$\ell \leq s$$, $$d(x_{n_{\ell,\ell}}, x_{n_{s,s}}) \leq 2/\ell$$, which shows that it is Cauchy.

$$(\impliedby)$$: If $$X$$ were not totally bounded, there would exist $$\varepsilon > 0$$ such that no finite collection of balls of radius $$\varepsilon$$ covers $$X$$. Construct iteratively $$x_{0} \in X$$ and, given $$x_{1}, \dots, x_{n-1}$$, $$x_{n} \in X \setminus \bigcup_{i=1}^{n-1} B(x_{i}, \varepsilon)$$. Then $$d(x_{i}, x_{j}) \geq \varepsilon$$ for $$i \neq j$$, a sequence with no Cauchy subsequences.

### Theorem (Compact $$=$$ complete $$+$$ totally bounded)

A metric space is compact if and only if it is complete and totally bounded.

***Proof:*** $$(\implies)$$: Every compact space is complete (proved above). To see that every compact space is totally bounded, given $$\varepsilon > 0$$ the family $$\{ B(x, \varepsilon) : x \in X\}$$ is an open cover of $$X$$, so by compactness there exist $$x_{1}, \dots, x_{m} \in X$$ with $$X = \bigcup_{i=1}^{m} B(x_{i}, \varepsilon)$$.

$$(\impliedby)$$: Let $$\{x_{n}\}_{n=1}^{\infty} \subseteq X$$. Since it is totally bounded, it has a Cauchy subsequence $$\{x_{n_{k}}\}$$. By completeness, $$\{x_{n_{k}}\}$$ converges in $$X$$. Thus $$X$$ is sequentially compact, equivalently compact.

## Completion of a metric space

### Theorem (Existence of the completion)

Let $$(X, d)$$ be a metric space. Then:

1. There exist a complete metric space $$(X^{\sharp}, d^{\sharp})$$ and an injective, distance-preserving map $$i : X \to X^{\sharp}$$, with $$i(X)$$ dense in $$X^{\sharp}$$.
2. If $$(X, d)$$ is complete, then $$(X^{\sharp}, d^{\sharp})$$ is isometric to $$(X, d)$$.

***Proof:*** *Construction.* Let $$\{x_{n}\}, \{y_{n}\} \subseteq X$$ be Cauchy. The triangle inequality gives

$$
|d(x_{m}, y_{m}) - d(x_{n}, y_{n})| \leq d(x_{m}, x_{n}) + d(y_{m}, y_{n}),
$$

hence $$\{d(x_{m}, y_{m})\}_{m=1}^{\infty}$$ is Cauchy in $$\mathbb{R}$$. We define

$$
\tilde{d}(\{x_{n}\}, \{y_{n}\}) = \lim_{m \to \infty} d(x_{m}, y_{m}).
$$

This $$\tilde{d}$$ is symmetric and satisfies the triangle inequality but may equal $$0$$ for two distinct sequences; it is a *semimetric*. We define $$\{x_{n}\} \sim \{y_{n}\}$$ when $$\tilde{d}(\{x_{n}\}, \{y_{n}\}) = 0$$ and consider

$$
X^{\sharp} = \big\{[\{x_{n}\}] \;:\; \{x_{n}\} \subseteq X \text{ Cauchy}\big\}, \quad d^{\sharp}([\{x_{n}\}], [\{y_{n}\}]) = \tilde{d}(\{x_{n}\}, \{y_{n}\}).
$$

*$$d^{\sharp}$$ is well defined.* If $$\{x_{n}\} \sim \{x_{n}'\}$$, then $$d(x_{m}, x_{m}') \to 0$$, and given $$\{y_{n}\}$$ Cauchy,

$$
d(x_{m}, y_{m}) \leq d(x_{m}, x_{m}') + d(x_{m}', y_{m}),
$$

hence $$\lim_{m} d(x_{m}, y_{m}) \leq \lim_{m} d(x_{m}', y_{m})$$. Conversely, $$d(x_{m}', y_{m}) \leq d(x_{m}', x_{m}) + d(x_{m}, y_{m})$$ implies $$\lim_{m} d(x_{m}', y_{m}) \leq \lim_{m} d(x_{m}, y_{m})$$, from which equality follows and therefore $$d^{\sharp}$$ does not depend on the representatives.

*$$i$$ preserves distances and $$i(X)$$ is dense.* For $$x \in X$$ define $$i(x) = [\{x, x, \dots\}]$$. Then $$d^{\sharp}(i(x), i(y)) = \lim_{m} d(x, y) = d(x, y)$$. Given $$[\{x_{n}\}] \in X^{\sharp}$$ and $$\varepsilon > 0$$, there exists $$n_{0}$$ with $$d(x_{n}, x_{n_{0}}) < \frac{\varepsilon}{2}$$ for $$n \geq n_{0}$$, so $$d^{\sharp}([\{x_{n}\}], i(x_{n_{0}})) = \lim_{m} d(x_{m}, x_{n_{0}}) \leq \frac{\varepsilon}{2} < \varepsilon$$.

*$$X^{\sharp}$$ is complete.* Let $$\{\underline{x}^{m}\}_{m=1}^{\infty} \subseteq X^{\sharp}$$ be Cauchy. By the density of $$i(X)$$ in $$X^{\sharp}$$ just proved, for each $$m \in \mathbb{N}$$ there exists $$y_{m} \in X$$ with $$d^{\sharp}(\underline{x}^{m}, i(y_{m})) < 1/m$$. Then

$$
d(y_{m}, y_{n}) = d^{\sharp}(i(y_{m}), i(y_{n})) \leq \tfrac{1}{m} + d^{\sharp}(\underline{x}^{m}, \underline{x}^{n}) + \tfrac{1}{n},
$$

so $$\{y_{n}\}$$ is Cauchy in $$X$$. Let $$\underline{y} = [\{y_{n}\}] \in X^{\sharp}$$. Given $$\varepsilon > 0$$, choose $$k_{0}$$ with $$d(y_{n}, y_{j}) < \varepsilon/2$$ for all $$n, j \geq k_{0}$$. For $$m \geq k_{0}$$,

$$
d^{\sharp}(i(y_{m}), \underline{y}) = \lim_{j \to \infty} d(y_{m}, y_{j}) \leq \tfrac{\varepsilon}{2},
$$

whence

$$
d^{\sharp}(\underline{x}^{m}, \underline{y}) \leq d^{\sharp}(\underline{x}^{m}, i(y_{m})) + d^{\sharp}(i(y_{m}), \underline{y}) \leq \tfrac{1}{m} + \tfrac{\varepsilon}{2} < \varepsilon
$$

for $$m$$ sufficiently large. We conclude that $$\underline{x}^{m} \to \underline{y}$$ in $$X^{\sharp}$$.

*(2)*: If $$(X, d)$$ is complete, given $$\{x_{n}\}$$ Cauchy there exists $$x \in X$$ with $$x_{n} \to x$$. Then $$d^{\sharp}([\{x_{n}\}], i(x)) = \lim_{m} d(x_{m}, x) = 0$$, so $$i(x) = [\{x_{n}\}]$$ and $$i$$ is surjective, hence an isometry.

### Definition (Completion of a space)

We say that $$X^\ast$$ is a completion of $$X$$ if $$X^\ast$$ is complete and contains a copy of $$X$$, which is dense. That is, there exists an isometry $$\phi: X \to \phi(X) \subseteq X^\ast$$, with $$\overline{\phi(X)} = X^\ast$$.

### Lemma (Universal property of the completion)

Let $$(Y, \rho)$$ be a complete metric space and $$j : X \to Y$$ a distance-preserving map with $$j(X)$$ dense in $$Y$$. Then there exists $$\theta : X^{\sharp} \to Y$$, an isometry such that $$\theta \circ i = j$$.

***Proof:*** Exercise (extend $$\theta$$ from $$\theta(i(x)) = j(x)$$ using density and completeness).
{% endraw %}
