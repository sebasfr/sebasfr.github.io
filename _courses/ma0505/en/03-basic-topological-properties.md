---
layout: chapter
course: ma0505
chapter: 3
title: "Basic Topological Properties"
slug: 03-basic-topological-properties
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/03-basic-topological-properties/
---

{% raw %}
## Interior of a set

### Definition (Interior point and interior of a set)

Let $$(E, d)$$ be a metric space and $$A \subseteq E$$. We say that $$x_{0} \in A$$ is an *interior point* of $$A$$ if there exists $$r > 0$$ with $$B(x_{0}, r) \subseteq A$$. The *interior* of $$A$$, denoted $$A^{\circ}$$, is the set of interior points of $$A$$.

### Lemma ($$A^{\circ}$$ is the largest open set contained in $$A$$)

Let $$G \subseteq A$$ with $$G$$ open. Then $$G \subseteq A^{\circ}$$. In particular, $$A^{\circ}$$ is the largest open set contained in $$A$$.

***Proof:*** If $$x_{0} \in G$$, since $$G$$ is open there exists $$r > 0$$ with $$B(x_{0}, r) \subseteq G \subseteq A$$, so that $$x_{0} \in A^{\circ}$$. We conclude that $$G \subseteq A^{\circ}$$.

### Exercise ($$A^{\circ}$$ is open)

Prove that for every $$A \subseteq E$$, $$A^{\circ}$$ is an open set.

### Lemma (Interior of an intersection)

Let $$A_{1}, A_{2} \subseteq E$$. Then $$(A_{1} \cap A_{2})^{\circ} = A_{1}^{\circ} \cap A_{2}^{\circ}$$.

***Proof:*** Since $$A_{1}^{\circ} \cap A_{2}^{\circ}$$ is open and is contained in $$A_{1} \cap A_{2}$$, by the previous lemma $$A_{1}^{\circ} \cap A_{2}^{\circ} \subseteq (A_{1} \cap A_{2})^{\circ}$$.

Conversely, if $$x \in (A_{1} \cap A_{2})^{\circ}$$, there exists $$r > 0$$ with $$B(x, r) \subseteq A_{1} \cap A_{2}$$. Then $$B(x, r) \subseteq A_{1}$$ and $$B(x, r) \subseteq A_{2}$$, which implies $$x \in A_{1}^{\circ} \cap A_{2}^{\circ}$$.

### Exercise (Monotonicity of the interior)

If $$A \subseteq B$$ then $$A^{\circ} \subseteq B^{\circ}$$. *Hint:* use the lemma $$G \subseteq A^{\circ}$$ whenever $$G$$ is open and $$G \subseteq A$$.

### Exercise (Characterisation of open sets by the interior)

Given $$B \subseteq E$$, $$B$$ is open if and only if $$B = B^{\circ}$$.

## Convergence of sequences and distance between sets

### Definition (Convergence of sequences)

A sequence $$\{ x_{n} \}_{n=1}^{\infty} \subseteq E$$ *converges* to $$x \in E$$ if for every $$\varepsilon > 0$$ there exists $$n_{0} \in \mathbb{N}$$ such that $$n \geq n_{0}$$ implies $$d(x_{n}, x) < \varepsilon$$. We write $$x_{n} \to x$$ as $$n \to \infty$$.

### Definition (Distance between sets)

Given $$A, B \subseteq E$$, we define

$$
d(A, B) = \inf \{ d(x, y) : (x, y) \in A \times B \}.
$$

In particular, for $$x \in E$$ and $$A \subseteq E$$, $$d(x, A) = \inf\{ d(x,a) : a \in A\}$$.

### Exercise (The distance to a set is $$1$$-Lipschitz)

For every $$A \subseteq E$$ and $$x, y \in E$$, $$|d(x, A) - d(y, A)| \leq d(x, y)$$.

## Closure of a set

### Lemma (Characterisation of the closure by sequences and by distance)

Given $$x \in E$$ and $$A \subseteq E$$, the following are equivalent:

1. $$d(x, A) = 0$$;
2. there exists $$\{ x_{n} \}_{n=1}^{\infty} \subseteq A$$ such that $$x_{n} \to x$$ as $$n \to \infty$$.

***Proof:*** $$(1) \implies (2)$$: If $$d(x, A) = 0$$, for each $$n \in \mathbb{N}$$ there exists $$x_{n} \in A$$ with $$d(x, x_{n}) < 1/n$$, so that $$\{x_{n}\}_{n=1}^{\infty} \subseteq A$$ and $$x_{n} \to x$$.

$$(2) \implies (1)$$: If $$\{x_{n}\}_{n=1}^{\infty} \subseteq A$$ and $$x_{n} \to x$$, then $$d(x, A) \leq d(x, x_{n}) \to 0$$, whence $$d(x, A) = 0$$.

### Definition (Closure and adherent points)

Given $$A \subseteq E$$, the *closure* of $$A$$ is

$$
\overline{A} = \{ x \in E : d(x, A) = 0\}.
$$

Its elements are called *adherent points* of $$A$$. It is immediate that $$A \subseteq \overline{A}$$.

### Proposition (Monotonicity of the closure)

If $$A \subseteq B \subseteq E$$, then $$\overline{A} \subseteq \overline{B}$$.

***Proof:*** For $$x \in E$$,

$$
\inf_{b \in B} d(x, b) \leq \inf_{a \in A} d(x, a),
$$

i.e. $$d(x, B) \leq d(x, A)$$. Thus, $$d(x, A) = 0$$ implies $$d(x, B) = 0$$.

### Example (Zero distance between two disjoint closed sets)

Let $$A = \{ n + \tfrac{1}{n} \}_{n=1}^{\infty}$$ and $$B = \mathbb{Z}$$. Both are closed (for example $$\mathbb{R} \setminus B = \bigcup_{n \in \mathbb{Z}} (n, n+1)$$ is open). Nevertheless,

$$
d\!\left(n + \tfrac{1}{n}, n\right) = \tfrac{1}{n} \to 0,
$$

so that $$d(A, B) = 0$$.

### Lemma (Closed is equivalent to being equal to its closure)

Let $$A \subseteq E$$. Then $$A$$ is closed if and only if $$A = \overline{A}$$.

***Proof:*** $$(\impliedby)$$: If $$A = \overline{A}$$ and $$x \notin A$$, then $$d(x, A) > 0$$. There exists $$r > 0$$ with $$r \leq d(x, A)$$ and then $$B(x, r) \cap A = \emptyset$$, i.e. $$B(x, r) \subseteq E \setminus A$$. Thus $$E\setminus A$$ is open and $$A$$ is closed.

$$(\implies)$$: Suppose $$A$$ is closed and take $$x \in E \setminus A$$. Since $$E\setminus A$$ is open, there exists $$r_{1} > 0$$ with $$B(x, r_{1}) \subseteq E \setminus A$$, so that $$B(x, r_{1}) \cap A = \emptyset$$ and $$d(x, A) \geq r_{1} > 0$$. Hence $$x \notin \overline{A}$$, which proves $$\overline{A} \subseteq A$$. The inclusion $$A \subseteq \overline{A}$$ is immediate.

### Proposition (The closure is a closed set)

For every $$A \subseteq E$$, $$\overline{A}$$ is closed.

***Proof:*** Let $$z \notin \overline{A}$$, that is $$d(z, A) = r > 0$$. We shall see that $$B(z, r/2) \subseteq E \setminus \overline{A}$$. If $$w \in B(z, r/2)$$ and $$a \in A$$, then

$$
r \leq d(z, a) \leq d(z, w) + d(w, a) < \tfrac{r}{2} + d(w, a),
$$

so that $$d(w, a) > r/2$$ and, taking the infimum, $$d(w, A) \geq r/2 > 0$$, i.e. $$w \notin \overline{A}$$.

### Exercise (Properties of the closure under unions and intersections)

For $$A, B \subseteq E$$:

1. $$\overline{A \cup B} = \overline{A} \cup \overline{B}$$;
2. $$\overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$$.

## Accumulation and boundary

### Definition (Accumulation point)

A point $$x_{0} \in E$$ is an *accumulation point* of $$A \subseteq E$$ if for every $$r > 0$$,

$$
\big(B(x_{0}, r) \setminus \{ x_{0}\}\big) \cap A \neq \emptyset.
$$

That is, every ball centred at $$x_{0}$$ contains points of $$A$$ other than $$x_{0}$$.

### Exercise (Characterisation of accumulation points by sequences)

$$x_{0}$$ is an accumulation point of $$A$$ if and only if there exists a sequence $$\{ x_{n}\}_{n=1}^{\infty} \subseteq A \setminus \{x_{0}\}$$ such that $$x_{n} \to x_{0}$$.

### Example (Unique accumulation point of $$\{1/n\}$$)

Let $$A = \{ 1/n : n \geq 1\}$$. Then $$\overline{A} = A \cup \{ 0\}$$ and $$0$$ is the only accumulation point of $$A$$, since

$$
B\!\left(\tfrac{1}{n}, \tfrac{1}{(n+1)^{2}}\right) \cap A = \left\{ \tfrac{1}{n}\right\} \quad \text{if } n \geq 1.
$$

### Definition (Boundary point and boundary of a set)

Given $$A \subseteq E$$ and $$x \in E$$, we say that $$x$$ is a *boundary point* of $$A$$ if for every $$r > 0$$,

$$
B(x, r) \cap A \neq \emptyset \quad\text{and}\quad B(x, r) \cap (E \setminus A) \neq \emptyset.
$$

Equivalently, $$d(x, A) = d(x, E \setminus A) = 0$$.

### Notation (Boundary)

The *boundary* of $$A$$ is denoted

$$
\partial A = \{\text{boundary points of } A\} = \{ x \in E : d(x, A) = d(x, E \setminus A) = 0\} = \overline{A} \cap \overline{E \setminus A}.
$$

Note that $$\partial A \subseteq \overline{A}$$.

## Neighbourhoods and density

### Definition (Neighbourhood of a point)

Given $$x \in E$$, $$V \subseteq E$$ is a *neighbourhood* of $$x$$ if there exists $$r > 0$$ such that $$B(x, r) \subseteq V$$.

### Note (Open sets as neighbourhoods)

If $$V$$ is open, $$V$$ is a neighbourhood of each of its points.

### Definition ($$r$$ neighbourhood of a set)

Given $$A \subseteq E$$ and $$r > 0$$, we define

$$
V_{r}(A) = \{ x \in E : d(x, A) < r\}.
$$

In particular $$A \subseteq \overline{A} \subseteq V_{r}(A)$$.

### Exercise (Balls centred in $$A$$ are contained in $$V_{r}(A)$$)

Let $$x \notin \overline{A}$$ with $$x \in V_{r}(A)$$. If $$0 < r_{1} < r - d(x, A)$$, show that

$$
B(x, r_{1}) \subseteq V_{r}(A).
$$

### Lemma ($$V_{r}(A)$$ is open)

If $$A \subseteq E$$ and $$r > 0$$, then $$V_{r}(A)$$ is open.

***Proof:*** Let $$x \in V_{r}(A)$$ and take $$a \in A$$ with $$d(x, a) < r$$. Define $$r_{1} = r - d(x, a) > 0$$. For $$y \in B(x, r_{1})$$ we have that

$$
d(y, A) \leq d(y, a) \leq d(y, x) + d(x, a) < r_{1} + d(x, a) = r,
$$

that is, $$y \in V_{r}(A)$$. Thus $$B(x, r_{1}) \subseteq V_{r}(A)$$.

### Proposition (The closure is an intersection of neighbourhoods)

For every $$A \subseteq E$$,

$$
\overline{A} = \bigcap_{r > 0} V_{r}(A).
$$

In particular, $$\overline{A}$$ is a countable intersection of open sets.

***Proof:*** If $$x \in \overline{A}$$ then $$d(x, A) = 0 < r$$ for every $$r > 0$$, so $$x \in V_{r}(A)$$. Conversely, if $$x \in \bigcap_{r > 0} V_{r}(A)$$ then $$d(x, A) < r$$ for every $$r > 0$$, so that $$d(x, A) = 0$$ and $$x \in \overline{A}$$.

### Definition (Dense set and separable space)

$$A \subseteq E$$ is *dense* in $$E$$ if $$\overline{A} = E$$. A metric space $$(E, d)$$ is *separable* if it possesses a countable dense set.

### Example ($$\mathbb{R}$$ and $$\mathbb{R}^{d}$$ are separable)

$$(\mathbb{R}, |\cdot|)$$ is separable since $$\mathbb{Q}$$ is dense in $$\mathbb{R}$$. In general $$(\mathbb{R}^{d}, \|\cdot\|)$$ is separable because $$\mathbb{Q}^{d}$$ is dense in $$\mathbb{R}^{d}$$.
{% endraw %}
