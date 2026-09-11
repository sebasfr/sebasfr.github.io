---
layout: chapter
course: ma0505
chapter: 10
title: "Functions of Bounded Variation"
slug: 10-functions-of-bounded-variation
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/10-functions-of-bounded-variation/
---

{% raw %}
## Motivation: length of curves and mass of a wire

Two geometric problems show the need to enlarge the class of functions that can be treated with the Riemann integral. Consider a continuous curve $$\gamma : [a,b] \to \mathbb{R}^{2}$$, $$\gamma(t) = (\gamma_{1}(t), \gamma_{2}(t))$$. Given a partition $$a = t_{0} < t_{1} < \dots < t_{n} = b$$, the polygonal path with vertices $$\gamma(t_{i})$$ approximates the curve, and its length is

$$
\sum_{i=0}^{n-1} \|\gamma(t_{i+1}) - \gamma(t_{i})\|.
$$

![Polygonal approximation of a curve](/assets/img/courses/ma0505/variacion-acotada-poligonal.svg)

If $$\gamma_{1}, \gamma_{2}$$ are differentiable with Riemann-integrable derivative, the mean value theorem suggests that the length is $$\int_{a}^{b} \|\gamma'(t)\|\,dt$$; but in general it is not even clear that the set of polygonal lengths is bounded. An analogous phenomenon appears when computing the mass of a wire of density $$\rho$$, which is approximated by sums $$\sum_{i} \rho(t_{i})\, A\, \|\gamma(t_{i+1}) - \gamma(t_{i})\|$$. In both cases the relevant quantity is the supremum of the sums of increments $$\sum |f(t_{i+1}) - f(t_{i})|$$ over all partitions; the functions for which that supremum is finite are the subject of this section.

## Definition and first examples

### Definition (Function of bounded variation and sum of increments)

Let $$f : [a,b] \to \mathbb{R}$$. For a partition $$\Gamma = \{ a = t_{0} < t_{1} < \dots < t_{n} = b\}$$ we define the *sum of increments*

$$
S(f, \Gamma) = \sum_{i=0}^{n-1} |f(t_{i+1}) - f(t_{i})|.
$$

We say that $$f$$ is of *bounded variation* if there exists $$M > 0$$ such that $$S(f, \Gamma) \leq M$$ for every partition $$\Gamma$$; equivalently, if

$$
\sup_{\Gamma} S(f, \Gamma) < \infty.
$$

### Example (Every monotone function is of bounded variation)

If $$f$$ is increasing, the increments $$f(t_{i+1}) - f(t_{i})$$ are non-negative and the sum telescopes:

$$
S(f, \Gamma) = \sum_{i=0}^{n-1} \big(f(t_{i+1}) - f(t_{i})\big) = f(b) - f(a).
$$

Analogously, if $$f$$ is decreasing, $$S(f, \Gamma) = f(a) - f(b)$$ for every $$\Gamma$$. In both cases $$S(f, \Gamma)$$ does not depend on $$\Gamma$$, so that $$f$$ is of bounded variation.

### Example (The indicator of the irrationals is not of bounded variation)

Let $$\varphi : [0,1] \to \mathbb{R}$$ with $$\varphi(x) = 0$$ if $$x \in \mathbb{Q}$$ and $$\varphi(x) = 1$$ if $$x \notin \mathbb{Q}$$. Given $$n$$, choose a partition $$\{x_{k}\}_{k=0}^{2n}$$ with $$x_{0} = 0$$, $$x_{2n} = 1$$, $$x_{2k} \in \mathbb{Q}$$ and $$x_{2k+1} \notin \mathbb{Q}$$. Each increment $$|\varphi(x_{k+1}) - \varphi(x_{k})|$$ equals $$1$$, so that

$$
S(\varphi, \Gamma) = \sum_{k=0}^{2n-1} |\varphi(x_{k+1}) - \varphi(x_{k})| = 2n.
$$

Since $$n$$ is arbitrary, $$\sup_{\Gamma} S(\varphi, \Gamma) = \infty$$ and $$\varphi$$ is not of bounded variation.

## The total variation

### Definition (Total variation)

If $$f : [a,b] \to \mathbb{R}$$ is of bounded variation, its *total variation* over $$[a,b]$$ is

$$
\operatorname{Var}(f, [a,b]) = \sup_{\Gamma} S(f, \Gamma).
$$

### Proposition (Monotonicity of the variation over subintervals)

Let $$f : [a,b] \to \mathbb{R}$$ be of bounded variation and $$[a_{1}, b_{1}] \subseteq [a,b]$$. Then the restriction of $$f$$ to $$[a_{1}, b_{1}]$$ is of bounded variation and

$$
\operatorname{Var}(f, [a_{1}, b_{1}]) \leq \operatorname{Var}(f, [a,b]).
$$

***Proof:*** Let $$\Gamma_{1}$$ be a partition of $$[a_{1}, b_{1}]$$ and consider the partition $$\Gamma = \Gamma_{1} \cup \{a, b\}$$ of $$[a,b]$$. Adding the endpoints only adds non-negative summands, so that

$$
S(f, \Gamma_{1}) \leq S(f, \Gamma_{1}) + |f(a_{1}) - f(a)| + |f(b) - f(b_{1})| = S(f, \Gamma) \leq \operatorname{Var}(f, [a,b]).
$$

Taking the supremum over $$\Gamma_{1}$$ we obtain $$\operatorname{Var}(f, [a_{1}, b_{1}]) \leq \operatorname{Var}(f, [a,b]) < \infty$$.

### Proposition (Functions of bounded variation are bounded)

If $$f : [a,b] \to \mathbb{R}$$ is of bounded variation, then for every $$x \in [a,b]$$

$$
2|f(x)| \leq \operatorname{Var}(f, [a,b]) + |f(a)| + |f(b)|.
$$

In particular $$f$$ is bounded.

***Proof:*** For $$x \in (a,b)$$, the partition $$\{a, x, b\}$$ gives

$$
|f(x) - f(a)| + |f(b) - f(x)| \leq \operatorname{Var}(f, [a,b]).
$$

By the reverse triangle inequality, $$|f(x)| - |f(a)| \leq |f(x) - f(a)|$$ and $$|f(x)| - |f(b)| \leq |f(b) - f(x)|$$. Adding,

$$
2|f(x)| - |f(a)| - |f(b)| \leq \operatorname{Var}(f, [a,b]),
$$

which is the desired inequality (trivial at $$x = a, b$$). Hence $$|f(x)| \leq \tfrac{1}{2}\big(\operatorname{Var}(f,[a,b]) + |f(a)| + |f(b)|\big)$$ for every $$x$$.

### Lemma (Algebraic properties of functions of bounded variation)

Let $$f, g : [a,b] \to \mathbb{R}$$ be of bounded variation. Then:

1. $$cf + g$$ is of bounded variation for every $$c \in \mathbb{R}$$;
2. $$fg$$ is of bounded variation;
3. if there exists $$\varepsilon > 0$$ with $$|g(x)| \geq \varepsilon$$ for every $$x \in [a,b]$$, then $$1/g$$ is of bounded variation;
4. $$f$$ and $$g$$ are bounded.

***Proof:*** Exercise.

### Lemma (Additivity of the variation over subintervals)

Let $$f : [a,b] \to \mathbb{R}$$ be of bounded variation and $$a < c < b$$. Then

$$
\operatorname{Var}(f, [a,b]) = \operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b]).
$$

***Proof:*** *($$\leq$$).* Let $$\Gamma = \{a = x_{0} < \dots < x_{n} = b\}$$ and let $$\Gamma' = \Gamma \cup \{c\}$$, with $$x_{m_{0}} \leq c < x_{m_{0}+1}$$. Refining by adding $$c$$ does not decrease the sum of increments:

$$
S(f, \Gamma) \leq S(f, \Gamma') = S(f, \Gamma_{1}) + S(f, \Gamma_{2}),
$$

where $$\Gamma_{1} = (\Gamma' \cap [a,c]) \cup \{c\}$$ and $$\Gamma_{2} = \{c\} \cup (\Gamma' \cap [c,b])$$ are partitions of $$[a,c]$$ and $$[c,b]$$ respectively. Hence $$S(f, \Gamma) \leq \operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b])$$, and taking the supremum over $$\Gamma$$,

$$
\operatorname{Var}(f, [a,b]) \leq \operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b]).
$$

*($$\geq$$).* If $$\Gamma_{1}$$ and $$\Gamma_{2}$$ are partitions of $$[a,c]$$ and $$[c,b]$$, then $$\Gamma = \Gamma_{1} \cup \Gamma_{2}$$ is a partition of $$[a,b]$$ and $$S(f, \Gamma_{1}) + S(f, \Gamma_{2}) = S(f, \Gamma) \leq \operatorname{Var}(f, [a,b])$$. Taking the supremum first in $$\Gamma_{1}$$ and then in $$\Gamma_{2}$$,

$$
\operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b]) \leq \operatorname{Var}(f, [a,b]).
$$

## The Jordan decomposition

### Notation (Positive and negative part; positive and negative variations)

For $$x \in \mathbb{R}$$ we define $$x^{+} = \max\{x, 0\}$$ and $$x^{-} = \max\{-x, 0\}$$; both are non-negative and

$$
x^{+} + x^{-} = |x|, \qquad x^{+} - x^{-} = x.
$$

Given $$f : [a,b] \to \mathbb{R}$$ and a partition $$\Gamma = \{a = t_{0} < \dots < t_{n} = b\}$$, we define

$$
P(f, \Gamma) = \sum_{i=0}^{n-1} \big(f(t_{i+1}) - f(t_{i})\big)^{+}, \qquad
N(f, \Gamma) = \sum_{i=0}^{n-1} \big(f(t_{i+1}) - f(t_{i})\big)^{-},
$$

and the *positive and negative variations* $$P(f, [a,b]) = \sup_{\Gamma} P(f, \Gamma)$$, $$N(f, [a,b]) = \sup_{\Gamma} N(f, \Gamma)$$.

### Lemma (Relation between the total variation and the positive and negative variations)

Let $$f : [a,b] \to \mathbb{R}$$ be of bounded variation. Then

$$
P(f, [a,b]) - N(f, [a,b]) = f(b) - f(a), \qquad P(f, [a,b]) + N(f, [a,b]) = \operatorname{Var}(f, [a,b]).
$$

Equivalently,

$$
P(f, [a,b]) = \tfrac{1}{2}\big(\operatorname{Var}(f, [a,b]) + f(b) - f(a)\big), \quad
N(f, [a,b]) = \tfrac{1}{2}\big(\operatorname{Var}(f, [a,b]) - f(b) + f(a)\big).
$$

***Proof:*** For each partition $$\Gamma$$, using $$x^{+} + x^{-} = |x|$$ and $$x^{+} - x^{-} = x$$ on each increment,

$$
P(f, \Gamma) + N(f, \Gamma) = S(f, \Gamma), \qquad
P(f, \Gamma) - N(f, \Gamma) = \sum_{i=0}^{n-1}\big(f(t_{i+1}) - f(t_{i})\big) = f(b) - f(a).
$$

From the second identity, $$f(a) + P(f, \Gamma) = f(b) + N(f, \Gamma)$$; since the left-hand side and the right-hand side differ by the constant $$f(b) - f(a)$$, taking the supremum in $$\Gamma$$ gives $$f(a) + P(f, [a,b]) = f(b) + N(f, [a,b])$$, that is, $$P(f, [a,b]) - N(f, [a,b]) = f(b) - f(a)$$. Moreover, from $$P(f,\Gamma) - N(f,\Gamma) = f(b) - f(a)$$ we obtain $$S(f, \Gamma) = 2P(f, \Gamma) - (f(b) - f(a))$$; taking the supremum,

$$
\operatorname{Var}(f, [a,b]) = 2P(f, [a,b]) - (f(b) - f(a)),
$$

and combining with $$P - N = f(b) - f(a)$$ we obtain $$P + N = \operatorname{Var}(f, [a,b])$$ and the closed formulas for $$P$$ and $$N$$.

### Theorem (Jordan's characterisation of bounded variation)

A function $$f : [a,b] \to \mathbb{R}$$ is of bounded variation if and only if $$f$$ is the difference of two increasing functions. Moreover, the functions may be taken non-negative.

***Proof:*** *($$\Rightarrow$$).* Define $$P(x) = P(f, [a,x])$$ and $$N(x) = N(f, [a,x])$$ (with $$P(a) = N(a) = 0$$). By the previous lemma applied to $$[a,x]$$,

$$
f(x) - f(a) = P(x) - N(x), \qquad \text{that is} \qquad f(x) = \big(f(a) + P(x)\big) - N(x).
$$

By the monotonicity of the variation over subintervals, $$P$$ and $$N$$ are increasing and non-negative. Choosing a constant $$c \geq \max\{0, -f(a)\}$$, the functions $$g = c + f(a) + P$$ and $$h = c + N$$ are increasing, non-negative and $$f = g - h$$.

*($$\Leftarrow$$).* If $$f = g - h$$ with $$g, h$$ increasing, then $$g$$ and $$h$$ are of bounded variation (every monotone function is) and, by the lemma on algebraic properties, so is $$f = g - h$$.

## Discontinuities and refinement of partitions

### Theorem (Functions of bounded variation have at most countably many discontinuities)

Let $$f : [a,b] \to \mathbb{R}$$ be of bounded variation. Then $$f$$ has at most countably many discontinuities, and each one is a jump or a removable discontinuity (that is, the one-sided limits $$f(x^{+})$$ and $$f(x^{-})$$ exist at every point).

***Proof:*** By Jordan's characterisation, $$f = f_{1} - f_{2}$$ with $$f_{1}, f_{2}$$ increasing; it suffices to prove the statement for an increasing function $$g$$, since the union of two countable sets is countable and the one-sided limits of $$g$$ exist by monotonicity. For $$k \geq 1$$ let

$$
D_{k} = \big\{ x \in [a,b] : g(x^{+}) - g(x^{-}) \geq \tfrac{1}{k}\big\}.
$$

If $$x_{0} < x_{1} < \dots < x_{m}$$ are points of $$D_{k}$$, one may interleave $$y_{i}, z_{i}$$ with $$y_{i} < x_{i} < z_{i} = y_{i+1}$$, so that the jumps at the $$x_{i}$$ are dominated by disjoint increments of $$g$$:

$$
\frac{m+1}{k} \leq \sum_{i=0}^{m} \big(g(z_{i}) - g(y_{i})\big) \leq g(b) - g(a).
$$

Therefore $$D_{k}$$ is finite, with at most $$k\,(g(b) - g(a))$$ elements. The set of discontinuities of $$g$$ is $$\bigcup_{k \geq 1} D_{k}$$, a countable union of finite sets, hence countable.

### Theorem (Approximation of the total variation by fine partitions)

Let $$f : [a,b] \to \mathbb{R}$$ be continuous and of bounded variation, and let $$V = \operatorname{Var}(f, [a,b])$$. For every $$M < V$$ there exists $$\delta > 0$$ such that

$$
M < S(f, \Gamma) \leq V \qquad \text{for every partition } \Gamma \text{ with } |\Gamma| < \delta,
$$

where $$|\Gamma|$$ denotes the norm (largest subinterval length) of $$\Gamma$$.

***Proof:*** The bound $$S(f, \Gamma) \leq V$$ is the definition of $$V$$. Fix $$\mu > 0$$ with $$M + \mu < V$$ and a partition $$\Gamma_{1} = \{a = \tilde{x}_{0} < \dots < \tilde{x}_{k} = b\}$$ such that $$M + \mu < S(f, \Gamma_{1})$$. Since $$f$$ is uniformly continuous, there exists $$\delta_{1} > 0$$ with

$$
|x - y| < \delta_{1} \implies |f(x) - f(y)| < \frac{\mu}{2(k+1)}.
$$

Let $$\gamma = \min_{0 \leq j \leq k-1} |\tilde{x}_{j+1} - \tilde{x}_{j}|$$ and take any $$\Gamma$$ with $$|\Gamma| < \min\{\delta_{1}, \gamma\}$$. Then each subinterval of $$\Gamma$$ contains at most one point of $$\Gamma_{1}$$. Let $$\Gamma_{2} = \Gamma \cup \Gamma_{1}$$; in passing from $$\Gamma$$ to $$\Gamma_{2}$$ at most $$k+1$$ points are inserted, and each insertion of a point $$\tilde{x}$$ into a subinterval $$[x_{j-1}, x_{j}]$$ replaces $$|f(x_{j}) - f(x_{j-1})|$$ by $$|f(x_{j}) - f(\tilde{x})| + |f(\tilde{x}) - f(x_{j-1})|$$, increasing the sum by at most $$2\cdot \frac{\mu}{2(k+1)}$$. Therefore

$$
S(f, \Gamma_{2}) \leq S(f, \Gamma) + (k+1)\cdot \frac{2\mu}{2(k+1)} = S(f, \Gamma) + \mu.
$$

Since $$\Gamma_{2}$$ refines $$\Gamma_{1}$$, $$S(f, \Gamma_{1}) \leq S(f, \Gamma_{2})$$, whence

$$
M < S(f, \Gamma_{1}) - \mu \leq S(f, \Gamma_{2}) - \mu \leq S(f, \Gamma).
$$

### Corollary (Total variation and derivative)

Let $$f : [a,b] \to \mathbb{R}$$ with $$f'$$ continuous on $$[a,b]$$. Then

$$
\operatorname{Var}(f, [a,b]) = \int_{a}^{b} |f'(x)|\,dx, \qquad
P(f, [a,b]) = \int_{a}^{b} \big(f'(x)\big)^{+} dx, \qquad
N(f, [a,b]) = \int_{a}^{b} \big(f'(x)\big)^{-} dx.
$$

***Proof:*** Exercise.
{% endraw %}
