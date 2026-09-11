---
layout: chapter
course: ma0505
chapter: 12
title: "Outer Measure"
slug: 12-outer-measure
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/12-outer-measure/
---

{% raw %}
## Motivation: measuring lengths and areas

The length of a segment $$[a,b)$$ is $$b - a$$; that of a finite union of disjoint intervals $$[a_{i}, b_{i})$$ is $$\sum_{i} (b_{i} - a_{i})$$.

![The elementary measure of an interval](/assets/img/courses/ma0505/medida-elemental-intervalo.svg)

A point has length zero, since $$\{a\} \subseteq [a, a + \varepsilon)$$ gives $$\ell(\{a\}) \leq \varepsilon$$ for every $$\varepsilon > 0$$. Consequently, every finite union of points has length zero. But what is the “length” of $$\mathbb{Q} \cap [0,1]$$? If one enumerates $$\mathbb{Q} \cap [0,1] = \{q_{n}\}_{n=1}^{\infty}$$, each $$\bigcup_{i=1}^{n}\{q_{i}\}$$ has length $$0$$; formally, $$\mathbf{1}_{\mathbb{Q} \cap [0,1]} = \lim_{n} \mathbf{1}_{\bigcup_{i=1}^{n}\{q_{i}\}}$$, and if limit and integral could be interchanged one would obtain “$$\int_{0}^{1} \mathbf{1}_{\mathbb{Q} \cap [0,1]} = 0$$”. The problem is that $$\mathbf{1}_{\mathbb{Q} \cap [0,1]}$$ is not Riemann integrable. The *outer measure* captures this idea of size without depending on the Riemann integral.

## The elementary measure and the outer measure on R

### Definition (Family of intervals and elementary measure)

Let

$$
S = \{[a,b] : a < b\} \cup \{(-\infty, b] : b \in \mathbb{R}\} \cup \{[a, \infty) : a \in \mathbb{R}\} \cup \{\emptyset\}.
$$

We define $$m : S \to [0, \infty]$$ by $$m([a,b]) = b - a$$ (if $$a < b$$), $$m((-\infty, b]) = m([a, \infty)) = \infty$$ and $$m(\emptyset) = 0$$. It is extended additively to finite unions of intervals with disjoint interiors: if the $$\mathring{I_{i}}$$ are pairwise disjoint and $$I_{i} = [a_{i}, b_{i}]$$, then $$m\big(\bigcup_{i=1}^{k} I_{i}\big) = \sum_{i=1}^{k}(b_{i} - a_{i})$$.

### Exercise (Monotonicity of the elementary measure over covers)

Prove that if $$\bigcup_{k=1}^{n} I_{k} \subseteq \bigcup_{\ell=1}^{m} J_{\ell}$$ with the interiors $$\mathring{I_{k}}$$ pairwise disjoint, then

$$
\sum_{k=1}^{n} m(I_{k}) \leq \sum_{\ell=1}^{m} m(J_{\ell}).
$$

### Definition (Outer measure)

Given $$E \subseteq \mathbb{R}$$, its *outer measure* is

$$
m_{e}(E) = \inf\left\{ \sum_{k=1}^{\infty} m(I_{k}) : E \subseteq \bigcup_{k=1}^{\infty} I_{k},\ I_{k} \in S \right\}.
$$

*Monotonicity* follows immediately from the definition: if $$E_{1} \subseteq E_{2}$$, then $$m_{e}(E_{1}) \leq m_{e}(E_{2})$$.

### Lemma (Outer measure of an interval)

For $$a < b$$, $$m_{e}([a,b]) = b - a$$.

***Proof:*** Since $$[a,b] \in S$$ covers itself, $$m_{e}([a,b]) \leq b - a$$. For the lower bound, let $$\{I_{k}\} \subseteq S$$ with $$[a,b] \subseteq \bigcup_{k} I_{k}$$ and fix $$\varepsilon > 0$$. If some $$I_{k}$$ is unbounded (of the form $$(-\infty, b]$$ or $$[a, \infty)$$), then $$\sum_{k} m(I_{k}) = \infty \geq b - a$$ and that cover does not constrain the infimum; we may therefore suppose each $$I_{k} = [a_{k}, b_{k}]$$ is finite. For each $$k$$ choose an open interval $$I_{k}^{\ast} \supseteq I_{k}$$ with $$m(\overline{I_{k}^{\ast}}) \leq (1 + \varepsilon)\, m(I_{k})$$. Then $$[a,b] \subseteq \bigcup_{k} I_{k}^{\ast}$$ and, by compactness of $$[a,b]$$, there exists $$k_{0}$$ with $$[a,b] \subseteq \bigcup_{k=1}^{k_{0}} I_{k}^{\ast} \subseteq \bigcup_{k=1}^{k_{0}} \overline{I_{k}^{\ast}}$$. Since an interval covered by finitely many intervals has length at most the sum of the lengths,

$$
b - a \leq \sum_{k=1}^{k_{0}} m(\overline{I_{k}^{\ast}}) \leq (1 + \varepsilon)\sum_{k=1}^{k_{0}} m(I_{k}) \leq (1 + \varepsilon)\sum_{k=1}^{\infty} m(I_{k}).
$$

Therefore $$\frac{b - a}{1 + \varepsilon} \leq \sum_{k} m(I_{k})$$; taking the infimum over the covers, $$\frac{b - a}{1 + \varepsilon} \leq m_{e}([a,b])$$, and letting $$\varepsilon \to 0$$, $$b - a \leq m_{e}([a,b])$$.

### Lemma (Countable subadditivity of the outer measure)

Let $$E_{k} \subseteq \mathbb{R}$$ for $$k \geq 1$$. Then

$$
m_{e}\left(\bigcup_{k=1}^{\infty} E_{k}\right) \leq \sum_{k=1}^{\infty} m_{e}(E_{k}).
$$

***Proof:*** If some $$m_{e}(E_{k}) = \infty$$ the inequality is trivial, so we suppose $$m_{e}(E_{k}) < \infty$$ for every $$k$$. Let $$\varepsilon > 0$$. By definition of the outer measure, for each $$k$$ there exist $$\{I_{i}^{k}\}_{i=1}^{\infty} \subseteq S$$ with $$E_{k} \subseteq \bigcup_{i} I_{i}^{k}$$ and

$$
\sum_{i=1}^{\infty} m(I_{i}^{k}) \leq m_{e}(E_{k}) + \frac{\varepsilon}{2^{k}}.
$$

The countable family $$\{I_{i}^{k}\}_{i,k}$$ covers $$\bigcup_{k} E_{k}$$, hence

$$
m_{e}\left(\bigcup_{k} E_{k}\right) \leq \sum_{k=1}^{\infty}\sum_{i=1}^{\infty} m(I_{i}^{k}) \leq \sum_{k=1}^{\infty}\left( m_{e}(E_{k}) + \frac{\varepsilon}{2^{k}}\right) = \sum_{k=1}^{\infty} m_{e}(E_{k}) + \varepsilon.
$$

Since $$\varepsilon > 0$$ is arbitrary, the result follows.

## The outer measure on Rd

### Definition (Outer measure on $$\mathbb{R}^{d}$$)

Let $$S_{d} = \{[a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}] : a_{k} \leq b_{k}\} \cup \{\emptyset\}$$ and $$m\big([a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}]\big) = \prod_{k=1}^{d}(b_{k} - a_{k})$$. For $$E \subseteq \mathbb{R}^{d}$$,

$$
m_{e}(E) = \inf\left\{ \sum_{k=1}^{\infty} m(I_{k}) : E \subseteq \bigcup_{k=1}^{\infty} I_{k},\ I_{k} \in S_{d} \right\}.
$$

### Lemma (Outer measure of a box)

Let $$I = [a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}]$$. Then $$m_{e}(I) = \prod_{k=1}^{d}(b_{k} - a_{k})$$.

***Proof:*** The bound $$m_{e}(I) \leq \prod_{k}(b_{k} - a_{k})$$ is immediate since $$I \in S_{d}$$. The lower bound repeats the argument of the one-dimensional case: given a cover $$\{I_{k}\} \subseteq S_{d}$$ of $$I$$ and $$\varepsilon > 0$$, the $$I_{k}$$ are dilated to open boxes $$I_{k}^{\ast} \supseteq I_{k}$$ with $$m(\overline{I_{k}^{\ast}}) \leq (1 + \varepsilon) m(I_{k})$$; by compactness of $$I$$ a finite subcover suffices, and the finite additivity of volume over boxes (with disjoint interiors, after subdividing) gives $$\prod_{k}(b_{k} - a_{k}) \leq (1 + \varepsilon)\sum_{k} m(I_{k})$$. The result follows by letting $$\varepsilon \to 0$$.

### Lemma (Countable subadditivity on $$\mathbb{R}^{d}$$)

Let $$E_{i} \subseteq \mathbb{R}^{d}$$ for $$i \geq 1$$. Then $$m_{e}\big(\bigcup_{i} E_{i}\big) \leq \sum_{i} m_{e}(E_{i})$$.

***Proof:*** The proof of the one-dimensional case does not use the dimension: covering each $$E_{i}$$ by boxes of $$S_{d}$$ with sum of volumes less than $$m_{e}(E_{i}) + \varepsilon/2^{i}$$ and gathering the covers together, one obtains $$m_{e}\big(\bigcup_{i} E_{i}\big) \leq \sum_{i} m_{e}(E_{i}) + \varepsilon$$ for every $$\varepsilon > 0$$.

### Example (Sets of outer measure zero)

1. If $$m_{e}(E_{i}) = 0$$ for every $$i \geq 1$$, by subadditivity $$m_{e}\big(\bigcup_{i} E_{i}\big) \leq \sum_{i} m_{e}(E_{i}) = 0$$.
2. For $$x = (x_{1}, \dots, x_{d})$$, $$\{x\} \subseteq [x_{1}, x_{1} + \varepsilon] \times \dots \times [x_{d}, x_{d} + \varepsilon]$$ gives $$m_{e}(\{x\}) \leq \varepsilon^{d}$$, hence $$m_{e}(\{x\}) = 0$$. By (a), every countable set has outer measure zero; in particular $$m_{e}(\mathbb{Q}^{d}) = 0$$.

## Approximation by open sets and G-delta sets

### Lemma (Approximation of the outer measure by open sets)

Let $$E \subseteq \mathbb{R}^{d}$$ and $$\varepsilon > 0$$. Then there exists an open set $$G \subseteq \mathbb{R}^{d}$$ with $$E \subseteq G$$ and

$$
m_{e}(E) \leq m_{e}(G) \leq m_{e}(E) + \varepsilon.
$$

***Proof:*** The bound $$m_{e}(E) \leq m_{e}(G)$$ is monotonicity. Suppose $$m_{e}(E) < \infty$$ (otherwise $$G = \mathbb{R}^{d}$$ will do). Take $$\{I_{i}\}_{i=1}^{\infty} \subseteq S_{d}$$ with $$E \subseteq \bigcup_{i} I_{i}$$ and $$\sum_{i} m(I_{i}) \leq m_{e}(E) + \varepsilon/2$$. For each $$i$$ choose a box $$I_{i}^{\ast}$$ with $$I_{i} \subseteq \mathring{I_{i}^{\ast}}$$ and $$m(I_{i}^{\ast}) \leq m(I_{i}) + \varepsilon/2^{i+1}$$. Then $$G = \bigcup_{i} \mathring{I_{i}^{\ast}}$$ is open, $$E \subseteq G$$ and, by subadditivity,

$$
m_{e}(G) \leq \sum_{i=1}^{\infty} m_{e}(\mathring{I_{i}^{\ast}}) \leq \sum_{i=1}^{\infty} m(I_{i}^{\ast}) \leq \sum_{i=1}^{\infty}\left(m(I_{i}) + \frac{\varepsilon}{2^{i+1}}\right) \leq m_{e}(E) + \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = m_{e}(E) + \varepsilon.
$$

### Definition ($$G_{\delta}$$ set)

A set $$H \subseteq \mathbb{R}^{d}$$ is of type *$$G_{\delta}$$* if it is a countable intersection of open sets: $$H = \bigcap_{k=1}^{\infty} G_{k}$$ with each $$G_{k}$$ open.

### Lemma ($$G_{\delta}$$ hull of equal outer measure)

For every $$E \subseteq \mathbb{R}^{d}$$ there exists a $$G_{\delta}$$ set, $$H \supseteq E$$, with $$m_{e}(E) = m_{e}(H)$$.

***Proof:*** By the previous lemma, for each $$k \geq 1$$ there exists an open set $$G_{k} \supseteq E$$ with $$m_{e}(E) \leq m_{e}(G_{k}) \leq m_{e}(E) + \tfrac{1}{k}$$. Let $$H = \bigcap_{k} G_{k}$$, a $$G_{\delta}$$ set with $$E \subseteq H$$. By monotonicity, $$m_{e}(H) \leq m_{e}(G_{k}) \leq m_{e}(E) + \tfrac{1}{k}$$ for every $$k$$, hence $$m_{e}(H) \leq m_{e}(E)$$; the opposite inequality is the monotonicity $$m_{e}(E) \leq m_{e}(H)$$.

## Lebesgue measurable sets

### Definition (Lebesgue measurable set)

$$E \subseteq \mathbb{R}^{d}$$ is *Lebesgue measurable* if for every $$\varepsilon > 0$$ there exists an open set $$G \supseteq E$$ with $$m_{e}(G \setminus E) < \varepsilon$$. If $$E$$ is measurable, its *Lebesgue measure* is defined as $$m(E) = m_{e}(E)$$.

### Example (Intervals and sets of outer measure zero are measurable)

If $$E = [a,b]$$, taking $$G = (a - \tfrac{\varepsilon}{2}, b + \tfrac{\varepsilon}{2})$$ we have $$m_{e}(G \setminus E) = m_{e}\big((a - \tfrac{\varepsilon}{2}, a) \cup (b, b + \tfrac{\varepsilon}{2})\big) \leq \varepsilon$$; analogously $$[a,b)$$, $$(a,b]$$ and $$(a,b)$$ are measurable, with $$m([a,b]) = b - a$$. If $$m_{e}(E) = 0$$, by approximation there exists an open set $$G \supseteq E$$ with $$m_{e}(G) < \varepsilon$$, and then $$m_{e}(G \setminus E) \leq m_{e}(G) < \varepsilon$$; therefore every set of outer measure zero is measurable.

### Theorem (A countable union of measurable sets is measurable)

Let $$\{E_{i}\}_{i=1}^{\infty}$$ be a family of measurable sets. Then $$E = \bigcup_{i=1}^{\infty} E_{i}$$ is measurable.

***Proof:*** Let $$\varepsilon > 0$$. For each $$i$$ there exists an open set $$G_{i} \supseteq E_{i}$$ with $$m_{e}(G_{i} \setminus E_{i}) < \varepsilon/2^{i}$$. Then $$G = \bigcup_{i} G_{i}$$ is open, $$E \subseteq G$$ and

$$
G \setminus E = \Big(\bigcup_{i} G_{i}\Big) \setminus E \subseteq \bigcup_{i} (G_{i} \setminus E_{i}),
$$

since if $$x \in G_{i}$$ but $$x \notin E$$ then $$x \notin E_{i}$$. By subadditivity and monotonicity,

$$
m_{e}(G \setminus E) \leq \sum_{i=1}^{\infty} m_{e}(G_{i} \setminus E_{i}) < \sum_{i=1}^{\infty}\frac{\varepsilon}{2^{i}} = \varepsilon.
$$

### Exercise (Additivity of the outer measure over boxes with disjoint interiors)

Let $$I_{j} = I_{1}^{j} \times \dots \times I_{d}^{j}$$ with each $$I_{i}^{j}$$ a finite interval and $$\mathring{I_{i}} \cap \mathring{I_{j}} = \emptyset$$ for $$i \neq j$$. Prove that

$$
m_{e}\left(\bigcup_{j=1}^{m} I_{j}\right) = \sum_{j=1}^{m} m_{e}(I_{j}).
$$

### Lemma (Additivity for sets at positive distance)

If $$E_{1}, E_{2} \subseteq \mathbb{R}^{d}$$ satisfy $$d(E_{1}, E_{2}) > 0$$, then

$$
m_{e}(E_{1} \cup E_{2}) = m_{e}(E_{1}) + m_{e}(E_{2}).
$$

***Proof:*** The inequality $$\leq$$ is subadditivity. For $$\geq$$, let $$\varepsilon > 0$$ and $$\{I_{k}\} \subseteq S_{d}$$ with $$E_{1} \cup E_{2} \subseteq \bigcup_{k} I_{k}$$ and $$\sum_{k} m(I_{k}) \leq m_{e}(E_{1} \cup E_{2}) + \varepsilon$$. Subdividing each box if necessary (which does not alter the sum of volumes, by the finite additivity of volume over boxes with disjoint interiors, cf. the previous exercise), we may suppose $$\operatorname{diam}(I_{k}) < \tfrac{1}{2} d(E_{1}, E_{2})$$. Then no box meets both $$E_{1}$$ and $$E_{2}$$: if $$I_{k} \cap E_{1} \neq \emptyset$$, then $$I_{k} \cap E_{2} = \emptyset$$. Separating the cover into the boxes $$\{J_{\ell}\}$$ that meet $$E_{1}$$ and those $$\{\widetilde{J}_{\ell}\}$$ that meet $$E_{2}$$,

$$
m_{e}(E_{1}) + m_{e}(E_{2}) \leq \sum_{\ell} m(J_{\ell}) + \sum_{\ell} m(\widetilde{J}_{\ell}) \leq \sum_{k} m(I_{k}) \leq m_{e}(E_{1} \cup E_{2}) + \varepsilon.
$$

Since $$\varepsilon$$ is arbitrary, $$m_{e}(E_{1}) + m_{e}(E_{2}) \leq m_{e}(E_{1} \cup E_{2})$$.
{% endraw %}
