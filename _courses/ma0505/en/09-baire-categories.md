---
layout: chapter
course: ma0505
chapter: 9
title: "Baire Categories"
slug: 09-baire-categories
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/09-baire-categories/
---

{% raw %}
## Sets of first and second category

### Definition (Nowhere dense set)

Given a metric space $$(X, d)$$, $$A \subseteq X$$ is *nowhere dense* if $$(\overline{A})^{c}$$ is dense in $$X$$. Equivalently, $$(\overline{A})^{\circ} = \emptyset$$.

### Note (Characterisation via the interior of the closure)

$$A$$ is nowhere dense if and only if for every $$x \in X$$ and $$r > 0$$,

$$
(\overline{A})^{c} \cap B(x, r) \neq \emptyset.
$$

### Definition (First and second category (meagre))

1. A set $$A \subseteq X$$ is of *first category* (or *meagre*) if it is a countable union of nowhere dense sets.
2. A set is of *second category* if it is not of first category.

## The Baire theorems

### Theorem (Baire (countable intersection of dense open sets))

Let $$(X, d)$$ be complete. If $$\{G_{n}\}_{n=1}^{\infty}$$ is a sequence of open dense sets in $$X$$, then $$\bigcap_{n=1}^{\infty} G_{n}$$ is dense in $$X$$.

***Proof:*** Let $$A \subseteq X$$ be a non-empty open set. Since $$G_{1}$$ is dense, there exists $$x_{1} \in A \cap G_{1}$$, and since $$A \cap G_{1}$$ is open, there exists $$r_{1} > 0$$ with $$B(x_{1}, r_{1}) \subseteq A \cap G_{1}$$. Take $$B_{1} = B(x_{1}, r_{1}/2)$$, so $$\overline{B}_{1} \subseteq B(x_{1}, r_{1}) \subseteq A \cap G_{1}$$.

Applying the same argument to $$B_{1}$$ and $$G_{2}$$, there exist $$x_{2} \in G_{2}$$ and $$0 < r_{2} < r_{1}/2$$ such that $$B(x_{2}, r_{2}) \subseteq B_{1} \cap G_{2} \subseteq A \cap G_{1} \cap G_{2}$$ and, defining $$B_{2} = B(x_{2}, r_{2}/2)$$, $$\overline{B}_{2} \subseteq B_{1} \cap G_{2}$$.

Iterating, we obtain a sequence $$\{x_{n}\}$$ with $$x_{n} \in G_{n}$$ and $$r_{n} < r_{n-1}/2 \leq r_{1}/2^{n-1}$$ such that

$$
B(x_{n}, r_{n}) \subseteq B_{n-1} \cap G_{n} \subseteq A \cap \bigcap_{i=1}^{n} G_{i}, \quad \overline{B}_{n} \subseteq B_{n-1} \cap G_{n}.
$$

If $$n \geq m$$ then $$B_{n} \subseteq B_{m}$$ and $$x_{n}, x_{m} \in B_{m}$$, so $$d(x_{n}, x_{m}) < 2 r_{m} < r_{1}/2^{m-2}$$. Thus $$\{x_{n}\}$$ is Cauchy. By completeness there exists $$x = \lim_{n} x_{n}$$, and since $$\{x_{n}\}_{n=m}^{\infty} \subseteq B_{m}$$, $$x \in \overline{B}_{m} \subseteq A \cap \bigcap_{i=1}^{m} G_{i}$$ for every $$m \geq 1$$, so $$x \in A \cap \bigcap_{i=1}^{\infty} G_{i}$$. We conclude that $$\bigcap_{i=1}^{\infty} G_{i}$$ is dense.

### Theorem (Baire categories)

Let $$(X, d)$$ be a complete metric space. If $$G \subseteq X$$ is a non-empty open set, then $$G$$ is of second category.

***Proof:*** Suppose, for a contradiction, that $$G$$ is of first category. There exist nowhere dense sets $$A_{n}$$ with $$G = \bigcup_{n=1}^{\infty} A_{n}$$. Let $$G_{n} = (\overline{A}_{n})^{c}$$; each $$G_{n}$$ is open and dense (by the definition of nowhere dense). By Baire's theorem,

$$
\bigcap_{n=1}^{\infty} G_{n} \;=\; \bigcap_{n=1}^{\infty} (\overline{A}_{n})^{c} \;=\; \Big(\bigcup_{n=1}^{\infty} \overline{A}_{n}\Big)^{c}
$$

is dense in $$X$$. On the other hand, since $$A_{n} \subseteq \overline{A}_{n}$$ for every $$n$$,

$$
G \;=\; \bigcup_{n=1}^{\infty} A_{n} \;\subseteq\; \bigcup_{n=1}^{\infty} \overline{A}_{n},
$$

whence

$$
G \cap \Big(\bigcup_{n=1}^{\infty} \overline{A}_{n}\Big)^{c} \;=\; G \cap \bigcap_{n=1}^{\infty} G_{n} \;=\; \emptyset.
$$

But $$G$$ is a non-empty open set, so $$G$$ must meet every dense set. This contradicts the density of $$\bigcap_{n=1}^{\infty} G_{n}$$, concluding the result.
{% endraw %}
