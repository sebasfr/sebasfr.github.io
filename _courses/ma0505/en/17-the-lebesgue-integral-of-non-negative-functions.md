---
layout: chapter
course: ma0505
chapter: 17
title: "The Lebesgue Integral of Non-negative Functions"
slug: 17-the-lebesgue-integral-of-non-negative-functions
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/17-the-lebesgue-integral-of-non-negative-functions/
---

{% raw %}
## The region under the graph

### Definition (Region under the graph and graph of a function)

Let $$f : E \to \overline{\mathbb{R}}$$ be measurable with $$E \subseteq \mathbb{R}^{d}$$ measurable and $$f \geq 0$$. We define the *region under the graph* of $$f$$ over $$E$$ as

$$
R(f,E) = \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq f(x) \},
$$

and the *graph* of $$f$$ over $$E$$ as

$$
\Gamma(f,E) = \{ (x, f(x)) :\ x \in E \}.
$$

The question arises: is $$R(f,E)$$ measurable?

### Example (The region under a multiple of an indicator)

Let us analyse the case

$$
f(x) = a \mathbf{1}_{A}(x)
$$

with $$A \subseteq E$$ measurable and $$a > 0$$. Then we have that

$$
\begin{aligned}
R(f,E) &= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq f(x) \} \\
&= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in A,\ 0 \leq y \leq a \} \cup \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E \setminus A,\ y = 0 \} \\
&= \big( A \times [0,a] \big) \cup \big( (E \setminus A) \times \{0\} \big).
\end{aligned}
$$

That is, the measurability of $$R(f,E)$$ in this case reduces to the measurability of products of the form $$A \times [0,a]$$.

### Lemma (Measure of the product of a measurable set with an interval)

Let $$A \subseteq \mathbb{R}^{d}$$ be measurable and $$a \geq 0$$. Then $$A \times [0,a] \subseteq \mathbb{R}^{d+1}$$ is measurable and its measure is

$$
m(A \times [0,a]) = a\, m(A),
$$

with the convention $$0 \cdot \infty = 0$$.

***Proof:*** *The case of a box.* If $$A = [a_{1},b_{1}] \times \dots \times [a_{d},b_{d}]$$, then $$A \times [0,a]$$ is a box in $$\mathbb{R}^{d+1}$$ and the result follows from the formula for the volume of boxes. Checking the details is left as an exercise for the reader.

*The case of an open set with $$m(A) < \infty$$.* If $$A$$ is open, then there exist boxes $$I_{k}$$ in $$d$$ dimensions such that

$$
A = \bigcup_{k=1}^{\infty} I_{k} \quad \text{with } I_{j}^{\circ} \cap I_{k}^{\circ} = \emptyset \text{ if } j \neq k.
$$

Then

$$
A \times [0,a] = \bigcup_{k=1}^{\infty} I_{k} \times [0,a]
$$

is a measurable set, being a countable union of boxes. Since

$$
(I_{k} \times [0,a])^{\circ} \cap (I_{j} \times [0,a])^{\circ} = \emptyset, \quad k \neq j,
$$

and the measure of a countable union of boxes with pairwise disjoint interiors is the sum of their measures, we have that

$$
m(A \times [0,a]) = \sum_{i=1}^{\infty} m(I_{i} \times [0,a]) = a \sum_{i=1}^{\infty} m(I_{i}) = a\, m(A).
$$

*The case of a $$G_{\delta}$$ with $$m(A) < \infty$$.* Now let

$$
A = \bigcap_{j=1}^{\infty} G_{j}
$$

be a $$G_{\delta}$$ with each $$G_{i}$$ open and $$G_{i+1} \subseteq G_{i}$$. We may assume monotonicity because, replacing $$G_{j}$$ by $$G_{1} \cap \dots \cap G_{j}$$, which is still open, the total intersection does not change. Moreover, since $$m(A) < \infty$$, by outer regularity there exists an open set $$G \supseteq A$$ with $$m(G) < \infty$$; intersecting each $$G_{j}$$ with $$G$$ we may also suppose that $$m(G_{1}) < \infty$$. Hence

$$
A \times [0,a] = \bigcap_{j=1}^{\infty} G_{j} \times [0,a],
$$

with $$G_{i+1} \times [0,a] \subseteq G_{i} \times [0,a]$$ measurable and of finite measure, since $$m(G_{i} \times [0,a]) = a\, m(G_{i}) \leq a\, m(G_{1}) < \infty$$ by the previous case. Then, by continuity from above of the measure,

$$
m(A \times [0,a]) = \lim_{i \to \infty} m(G_{i} \times [0,a]) = \lim_{i \to \infty} a\, m(G_{i}) = a\, m(A).
$$

*The general measurable case with $$m(A) < \infty$$.* In the case where $$A$$ is measurable with finite measure, we may write

$$
A = H \setminus Z
$$

with $$H$$ a $$G_{\delta}$$ set such that $$A \subseteq H$$, $$m(H) = m(A)$$, and $$Z = H \setminus A$$ of measure zero. Then, by the previous step, $$H \times [0,a]$$ is measurable and

$$
m(H \times [0,a]) = a\, m(H).
$$

It is left as an exercise to prove that

$$
m_{e}(Z \times [0,a]) = 0.
$$

Then $$Z \times [0,a]$$ is measurable with measure zero,

$$
A \times [0,a] = (H \times [0,a]) \setminus (Z \times [0,a])
$$

is measurable, and

$$
m(A \times [0,a]) = m(H \times [0,a]) = a\, m(H) = a\, m(A).
$$

*The case $$m(A) = \infty$$.* Finally, if $$m(A) = \infty$$, set

$$
A_{k} = A \cap B(0,k).
$$

In this way

$$
A = \bigcup_{k=1}^{\infty} A_{k},
$$

with $$A_{k} \subseteq A_{k+1}$$ measurable and bounded, in particular of finite measure. By the previous arguments,

$$
A_{k} \times [0,a] \subseteq A_{k+1} \times [0,a]
$$

are measurable sets such that

$$
m(A_{k} \times [0,a]) = a\, m(A_{k}).
$$

Then $$A \times [0,a] = \bigcup_{k=1}^{\infty} A_{k} \times [0,a]$$ is measurable and, by continuity from below,

$$
m(A \times [0,a]) = \lim_{k \to \infty} m(A_{k} \times [0,a]) = \lim_{k \to \infty} a\, m(A_{k}) = a\, m(A).
$$

### Exercise (The product of a null set with an interval is null)

Let $$Z \subseteq \mathbb{R}^{d}$$ with $$m(Z) = 0$$ and $$a \geq 0$$. Show that $$m_{e}(Z \times [0,a]) = 0$$.

## The graph of a measurable function

### Lemma (The graph of a measurable function has measure zero)

Let $$f : E \to \mathbb{R}$$ be measurable, with $$E$$ measurable. Then $$m_{e}(\Gamma(f,E)) = 0$$.

***Proof:*** Let us first assume that $$E$$ has finite measure. Let $$\varepsilon > 0$$ and, for each $$k \in \mathbb{Z}$$,

$$
E_{k} = \{ x \in E :\ k \varepsilon \leq f(x) < (k+1) \varepsilon \}.
$$

The $$E_{k}$$ are measurable, pairwise disjoint, and

$$
E = \bigcup_{k \in \mathbb{Z}} E_{k}.
$$

Note that

$$
\Gamma(f, E_{k}) = \{ (x, f(x)) :\ x \in E_{k} \} \subseteq E_{k} \times [k\varepsilon, (k+1)\varepsilon).
$$

By the previous lemma and the invariance of outer measure under translations, we have that

$$
m_{e}(\Gamma(f,E_{k})) \leq m_{e}\big( E_{k} \times [k\varepsilon,(k+1)\varepsilon) \big) \leq \varepsilon\, m(E_{k}).
$$

Therefore, by countable subadditivity of outer measure, it holds that

$$
m_{e}(\Gamma(f,E)) = m_{e}\left( \bigcup_{k \in \mathbb{Z}} \Gamma(f,E_{k}) \right) \leq \sum_{k \in \mathbb{Z}} m_{e}(\Gamma(f,E_{k})) \leq \sum_{k \in \mathbb{Z}} \varepsilon\, m(E_{k}) = \varepsilon\, m(E),
$$

where the last equality uses that the $$E_{k}$$ are pairwise disjoint. Since $$\varepsilon > 0$$ is arbitrary and $$m(E) < \infty$$, we conclude that $$m_{e}(\Gamma(f,E)) = 0$$.

Finishing the proof in the case $$m(E) = \infty$$ is left as an exercise (see the following exercise).

### Exercise (The infinite measure case of the graph lemma)

Finish the proof of the previous lemma: show that if $$m(E) = \infty$$, then also $$m_{e}(\Gamma(f,E)) = 0$$.

### Lemma (The region under a non-negative simple function is measurable)

Let $$\phi : E \to \mathbb{R}$$ be simple, measurable and non-negative, say

$$
\phi(x) = \sum_{i=1}^{m} a_{i} \mathbf{1}_{A_{i}},
$$

with $$a_{i} \neq a_{j}$$ and $$A_{i} \cap A_{j} = \emptyset$$ for $$i \neq j$$, and $$E = \bigcup_{i=1}^{m} A_{i}$$. Then $$R(\phi,E)$$ is measurable.

***Proof:*** We have that

$$
R(\phi,E) = \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq \phi(x) \} = \bigcup_{j=1}^{m} \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in A_{j},\ 0 \leq y \leq a_{j} \},
$$

that is, $$R(\phi,E) = \bigcup_{j=1}^{m} A_{j} \times [0,a_{j}]$$, which is a finite union of measurable sets by the product lemma, and is therefore a measurable set.

### Theorem (The region under the graph of a non-negative measurable function is measurable)

Let $$f : E \to \mathbb{R}$$ be measurable with $$f \geq 0$$ and $$E$$ measurable. Then $$R(f,E) \subseteq \mathbb{R}^{d+1}$$ is a measurable set.

***Proof:*** Since $$f \geq 0$$ is measurable, there exists an increasing sequence of simple, measurable and non-negative functions $$\{\phi_{k}\}_{k=1}^{\infty}$$ satisfying

$$
\lim_{k \to \infty} \phi_{k}(x) = f(x)
$$

on $$E$$. Hence, if $$0 \leq y < f(x)$$, since $$\phi_{k}(x) \to f(x) > y$$, there exists $$\phi_{k}$$ such that

$$
0 \leq y \leq \phi_{k}(x).
$$

Then, separating the points with $$y < f(x)$$ from those with $$y = f(x)$$,

$$
R(f,E) = \{ (x,y) :\ x \in E,\ 0 \leq y < f(x) \} \cup \{ (x,y) :\ x \in E,\ f(x) = y \},
$$

and by the above we obtain

$$
R(f,E) = \bigcup_{k=1}^{\infty} R(\phi_{k},E) \cup \{ (x,y) :\ x \in E,\ f(x) = y,\ y \geq 0 \},
$$

since each $$R(\phi_{k},E) \subseteq R(f,E)$$ because $$\phi_{k} \leq f$$. Now, each $$R(\phi_{k},E)$$ is measurable by the previous lemma, and the second set is contained in $$\Gamma(f,E)$$, which has outer measure zero and is therefore measurable. We conclude that $$R(f,E)$$ is measurable, being a countable union of measurable sets.

## The definition of the integral

### Definition (Lebesgue integral of a non-negative measurable function)

Given $$f : E \to \mathbb{R}$$ measurable such that $$f \geq 0$$, we define its *Lebesgue integral* as

$$
\int_{E} f \, dx = m(R(f,E)).
$$

### Proposition (The integral of a non-negative simple function)

Let $$\phi = \sum_{i=1}^{m} a_{i} \mathbf{1}_{A_{i}}$$ be simple, measurable and non-negative, with the $$A_{i} \subseteq E$$ measurable and pairwise disjoint. Then

$$
\int_{E} \phi(x) \, dx = \sum_{i=1}^{m} a_{i}\, m(A_{i}).
$$

***Proof:*** We may assume that $$a_{i} \neq 0$$ for $$1 \leq i \leq m$$, since the terms with $$a_{i} = 0$$ contribute to neither side. Then

$$
\begin{aligned}
\int_{E} \phi(x)\, dx &= m\big( R(\phi,E) \big) \\
&= m\big( \{ \phi = 0 \} \times \{0\} \big) + m\left( \bigcup_{i=1}^{m} \{ (x,y) :\ x \in A_{i},\ 0 \leq y \leq a_{i} \} \right) \\
&= 0 + \sum_{i=1}^{m} a_{i}\, m(A_{i}),
\end{aligned}
$$

where we used that $$\{\phi = 0\} \times \{0\}$$ has measure zero, that the sets $$A_{i} \times [0,a_{i}]$$ are pairwise disjoint because the $$A_{i}$$ are, and the formula $$m(A_{i} \times [0,a_{i}]) = a_{i}\, m(A_{i})$$.

### Theorem (Monotonicity of the integral with respect to the integrand and the domain)

Let $$f, g : E \to [0,\infty)$$ be measurable.

1. If $$0 \leq g \leq f$$, then

    $$
    \int_{E} g(x) \, dx \leq \int_{E} f(x) \, dx.
    $$
2. If $$E_{1} \subseteq E_{2} \subseteq E$$ are measurable, then

    $$
    \int_{E_{1}} f(x) \, dx \leq \int_{E_{2}} f(x) \, dx.
    $$

***Proof:*** Since $$0 \leq g \leq f$$, we have that

$$
\{ (x,y) :\ x \in E,\ 0 \leq y \leq g(x) \} \subseteq \{ (x,y) :\ x \in E,\ 0 \leq y \leq f(x) \},
$$

hence $$R(g,E) \subseteq R(f,E)$$, and part (i) follows from the monotonicity of the measure.

For the second part we shall first prove that

$$
\int_{E_{1}} f(x) \, dx = \int_{E} \mathbf{1}_{E_{1}} f(x) \, dx
$$

for $$E_{1} \subseteq E$$ measurable. Note that

$$
\{ (x,y) :\ x \in E,\ 0 \leq y \leq \mathbf{1}_{E_{1}}(x) f(x) \} = \big( (E \setminus E_{1}) \times \{0\} \big) \cup \{ (x,y) :\ x \in E_{1},\ 0 \leq y \leq f(x) \},
$$

and since $$(E \setminus E_{1}) \times \{0\}$$ has measure zero, then

$$
m\big( R(\mathbf{1}_{E_{1}} f, E) \big) = m\big( R(f,E_{1}) \big).
$$

Now, if $$E_{1} \subseteq E_{2}$$ are measurable, then

$$
\mathbf{1}_{E_{1}} f \leq \mathbf{1}_{E_{2}} f,
$$

and by part (i) we obtain

$$
\int_{E} \mathbf{1}_{E_{1}} f(x) \, dx \leq \int_{E} \mathbf{1}_{E_{2}} f(x) \, dx.
$$

We conclude that

$$
\int_{E_{1}} f(x) \, dx \leq \int_{E_{2}} f(x) \, dx.
$$
{% endraw %}
