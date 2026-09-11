---
layout: chapter
course: ma0505
chapter: 18
title: "Properties of the Integral of Non-negative Functions"
slug: 18-properties-of-the-integral-of-non-negative-functions
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/18-properties-of-the-integral-of-non-negative-functions/
---

{% raw %}
## Functions with infinite values

### Definition (Integral of a measurable function with values in $$[0,\infty]$$)

Let $$f : E \to [0,\infty]$$ be measurable with $$E$$ measurable and $$f \geq 0$$. Take

$$
E_{1} = \{ x \in E :\ f(x) = \infty \}.
$$

We define

$$
\begin{aligned}
R(f,E) &= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq f(x) \} \\
&= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E \setminus E_{1},\ 0 \leq y \leq f(x) \} \cup \big( E_{1} \times [0,\infty) \big),
\end{aligned}
$$

and

$$
\Gamma(f,E) = \{ (x,f(x)) \in \mathbb{R}^{d+1} :\ x \in E \setminus E_{1} \}.
$$

Just as was done for real-valued functions, we define

$$
\int_{E} f \, dx = m\big( R(f,E) \big).
$$

### Note (The region is still measurable for infinite values)

The theory developed so far guarantees that $$R(f,E)$$ is measurable whenever $$f$$ and $$E$$ are measurable: the first part of the decomposition is the region under the restriction of $$f$$ to the measurable set $$E \setminus E_{1}$$, and

$$
E_{1} \times [0,\infty) = \bigcup_{n=1}^{\infty} E_{1} \times [0,n]
$$

is a countable union of measurable sets.

### Proposition (A function with finite integral is finite a.e.)

Let $$f : E \to [0,\infty]$$ be measurable such that

$$
\int_{E} f(x) \, dx < \infty.
$$

Then $$m(\{ x \in E : f(x) = \infty \}) = 0$$, that is, $$f$$ is finite almost everywhere.

***Proof:*** Let $$E_{1} = \{ f = \infty \}$$ and, for each $$n \in \mathbb{N}$$, take

$$
g(x) = n \mathbf{1}_{E_{1}}(x).
$$

Then $$g(x) \leq f(x)$$ for $$x \in E$$, since on $$E_{1}$$ we have $$f = \infty \geq n$$ and outside $$E_{1}$$ we have $$g = 0 \leq f$$. Hence, by the formula for simple functions and the monotonicity of the integral,

$$
n\, m(E_{1}) = \int_{E} g(x)\, dx \leq \int_{E} f(x) \, dx < \infty
$$

for every $$n \in \mathbb{N}$$, and therefore $$m(E_{1}) = 0$$.

## Decomposition of the domain and the monotone convergence theorem

### Proposition (Additivity of the integral with respect to the domain)

Let $$f : E \to [0,\infty]$$ be measurable. In the case where $$E = \bigcup_{i=1}^{\infty} E_{i}$$ with the $$E_{i}$$ measurable and $$E_{i} \cap E_{j} = \emptyset$$ if $$i \neq j$$, we have that

$$
\int_{E} f(x) \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f(x) \, dx.
$$

This formula is also valid for finite unions.

***Proof:*** Since the $$E_{i}$$ are pairwise disjoint, we have that

$$
R(f,E) = \bigcup_{k=1}^{\infty} R(f,E_{k}),
$$

and the $$R(f,E_{k})$$ are pairwise disjoint, since their first coordinates live in disjoint sets. In this way, by countable additivity of the measure,

$$
\int_{E} f(x) \, dx = m(R(f,E)) = m\left( \bigcup_{k=1}^{\infty} R(f,E_{k}) \right) = \sum_{k=1}^{\infty} m(R(f,E_{k})) = \sum_{k=1}^{\infty} \int_{E_{k}} f(x) \, dx.
$$

The formula for finite unions is obtained by taking $$E_{k} = \emptyset$$ for the remaining indices, since $$R(f,\emptyset) = \emptyset$$.

### Theorem (Monotone convergence for non-negative functions)

Let $$\{f_{k}\}_{k=1}^{\infty}$$ be a sequence of measurable functions such that

$$
0 \leq f_{k}(x) \leq f_{k+1}(x)
$$

for every $$x \in E$$. If

$$
\lim_{k \to \infty} f_{k}(x) = f(x)
$$

almost everywhere on $$E$$, then

$$
\lim_{k \to \infty} \int_{E} f_{k}(x) \, dx = \int_{E} f(x) \, dx.
$$

***Proof:*** Let $$Z \subseteq E$$ be the null set where convergence fails, and $$\tilde{E} = E \setminus Z$$. For any non-negative measurable function $$g$$ we have $$R(g,Z) \subseteq Z \times [0,\infty) = \bigcup_{n} Z \times [0,n]$$, which has measure zero; then $$\int_{Z} g \, dx = 0$$ and, by additivity of the domain, the integrals over $$E$$ and over $$\tilde{E}$$ coincide both for $$f$$ and for each $$f_{k}$$. We may therefore suppose that $$f_{k}(x) \to f(x)$$ for every $$x \in E$$.

By the same approximation argument used for the region under the graph, we have that

$$
R(f,E) = \Gamma(f,E) \cup \bigcup_{k=1}^{\infty} R(f_{k},E):
$$

if $$0 \leq y < f(x)$$, since $$f_{k}(x) \uparrow f(x)$$, there exists $$k$$ with $$y \leq f_{k}(x)$$, that is $$(x,y) \in R(f_{k},E)$$; if $$y = f(x) < \infty$$, then $$(x,y) \in \Gamma(f,E)$$; and each $$R(f_{k},E) \subseteq R(f,E)$$ because $$f_{k} \leq f$$. Since

$$
R(f_{k},E) \subseteq R(f_{k+1},E)
$$

by the monotonicity of the sequence, and $$m(\Gamma(f,E)) = 0$$, continuity from below of the measure gives us

$$
\int_{E} f(x) \, dx = m(R(f,E)) = m\left( \bigcup_{k=1}^{\infty} R(f_{k},E) \right) = \lim_{k \to \infty} m(R(f_{k},E)) = \lim_{k \to \infty} \int_{E} f_{k}(x) \, dx.
$$

## A useful formula

### Notation (Lower sum associated with a finite partition of the domain)

Given $$f : E \to [0,\infty]$$ measurable and a finite partition $$E = \bigcup_{i=1}^{N} E_{i}$$ into pairwise disjoint measurable sets, we define

$$
\sum\big(f, \{E_{i}\}_{i=1}^{N}\big) = \sum_{i=1}^{N} \Big( \inf_{E_{i}} f \Big) \mathbf{1}_{E_{i}} \leq f.
$$

### Theorem (The integral as a supremum of lower sums)

Let $$f : E \to [0,\infty]$$ be measurable, non-negative. Then

$$
\int_{E} f(x) \, dx = \sup \left\{ \int_{E} \sum\big(f, \{E_{i}\}_{i=1}^{N}\big) \, dx :\ E = \bigcup_{i=1}^{N} E_{i} \ \text{finite partition into disjoint measurable sets} \right\}.
$$

***Proof:*** Given $$E_{1}, \dots, E_{N}$$ pairwise disjoint measurable sets such that $$E = \bigcup_{i=1}^{N} E_{i}$$, we have that

$$
\sum\big(f, \{E_{i}\}_{i=1}^{N}\big) \leq f,
$$

then, by monotonicity and the formula for simple functions,

$$
\sum_{i=1}^{N} \Big( \inf_{E_{i}} f \Big) m(E_{i}) = \int_{E} \sum\big(f, \{E_{i}\}_{i=1}^{N}\big) \, dx \leq \int_{E} f(x) \, dx.
$$

That is, the supremum in the statement is less than or equal to the integral.

For the reverse inequality, given $$k \geq 1$$ and $$1 \leq i \leq k 2^{k}$$, define

$$
E_{k}^{0} = \{ f \geq k \}, \qquad E_{k}^{i} = \left\{ \frac{i-1}{2^{k}} \leq f(x) < \frac{i}{2^{k}} \right\}.
$$

Then

$$
E = \bigcup_{i=0}^{k 2^{k}} E_{k}^{i}
$$

is a finite partition into pairwise disjoint measurable sets. Take

$$
f_{k}(x) = k \mathbf{1}_{E_{k}^{0}} + \sum_{i=1}^{k 2^{k}} \left( \frac{i-1}{2^{k}} \right) \mathbf{1}_{E_{k}^{i}};
$$

this is the standard dyadic approximation, so we know that

$$
f_{k} \leq f_{k+1} \qquad \text{and} \qquad \lim_{k \to \infty} f_{k} = f
$$

pointwise on $$E$$. By the monotone convergence theorem,

$$
\int_{E} f_{k} \, dx \to \int_{E} f \, dx.
$$

Since on each piece of the partition the value of $$f_{k}$$ is less than or equal to the infimum of $$f$$ on it, we have that

$$
f_{k} \leq \sum\big(f, \{E_{k}^{i}\}_{i=0}^{k 2^{k}}\big) \leq f,
$$

and integrating,

$$
\int_{E} f_{k} \, dx \leq \sum_{i=0}^{k 2^{k}} \Big( \inf_{E_{k}^{i}} f \Big) m(E_{k}^{i}) \leq \int_{E} f(x) \, dx.
$$

The middle term is one of the lower sums in the statement, and the left-hand side converges to $$\int_{E} f \, dx$$; we then have that

$$
\lim_{k \to \infty} \sum_{i=0}^{k 2^{k}} \Big( \inf_{E_{k}^{i}} f \Big) m(E_{k}^{i}) = \int_{E} f(x) \, dx,
$$

and the supremum in the statement reaches the integral.

### Corollary (The integral as a supremum over simple functions)

Let $$f : E \to [0,\infty]$$ be measurable. Then

$$
\int_{E} f(x) \, dx = \sup \left\{ \int_{E} \phi(x) \, dx :\ \phi\ \text{simple and measurable},\ 0 \leq \phi \leq f\ \text{on } E \right\}.
$$

***Proof:*** Exercise.

## Null sets, Markov's inequality and null functions

### Lemma (The integral over a set of measure zero is zero)

Let $$f : E \to [0,\infty]$$ be measurable. If $$m(E) = 0$$, then

$$
\int_{E} f(x) \, dx = 0.
$$

***Proof:*** Let $$f_{k} = \sum_{i=1}^{m} a_{i} \mathbf{1}_{A_{i}}$$, with $$A_{i} \cap A_{j} = \emptyset$$ if $$i \neq j$$, be non-negative simple functions increasing to $$f$$, so that, by the monotone convergence theorem,

$$
\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f(x) \, dx.
$$

Note that

$$
\int_{E} f_{k}(x) \, dx = \sum_{i=1}^{m} a_{i}\, m(A_{i}).
$$

Since $$A_{i} \subseteq E$$, we have $$m(A_{i}) = 0$$ for $$1 \leq i \leq m$$, and each $$\int_{E} f_{k} \, dx = 0$$. We conclude that $$\int_{E} f \, dx = 0$$.

### Theorem (The integral respects a.e. inequalities)

Let $$f, g : E \to [0,\infty]$$ be measurable such that $$g(x) \leq f(x)$$ almost everywhere on $$E$$. Then it holds that

$$
\int_{E} g(x) \, dx \leq \int_{E} f(x) \, dx.
$$

In particular, if $$f = g$$ a.e. on $$E$$, then

$$
\int_{E} g(x) \, dx = \int_{E} f(x) \, dx.
$$

***Proof:*** Let

$$
A = \{ x \in E :\ g(x) \leq f(x) \}.
$$

Then $$E = A \cup Z$$ with $$Z = E \setminus A$$ of measure zero and $$A \cap Z = \emptyset$$. Thus, by additivity of the domain and the previous lemma, we have

$$
\int_{E} f(x) \, dx = \int_{A} f(x) \, dx + \int_{Z} f(x) \, dx = \int_{A} f(x) \, dx,
$$

$$
\int_{E} g(x) \, dx = \int_{A} g(x) \, dx + \int_{Z} g(x) \, dx = \int_{A} g(x) \, dx.
$$

Since $$g \leq f$$ pointwise on $$A$$, monotonicity of the integral gives $$\int_{A} g \, dx \leq \int_{A} f \, dx$$, and the result follows. If moreover $$f = g$$ a.e., both inequalities hold and equality is obtained.

### Proposition (Markov's inequality)

Let $$f : E \to [0,\infty]$$ be measurable and $$\alpha > 0$$. Then

$$
m(\{ f \geq \alpha \}) \leq \frac{1}{\alpha} \int_{E} f(x) \, dx.
$$

***Proof:*** Since $$f \geq 0$$, we have the pointwise inequalities

$$
\alpha \mathbf{1}_{\{f \geq \alpha\}} \leq f \mathbf{1}_{\{f \geq \alpha\}} \leq f.
$$

Integrating and using the formula for simple functions, the identity $$\int_{E} \mathbf{1}_{E_{1}} f \, dx = \int_{E_{1}} f \, dx$$ and monotonicity,

$$
\alpha\, m(\{ f \geq \alpha \}) \leq \int_{\{f \geq \alpha\}} f(x) \, dx \leq \int_{E} f(x) \, dx,
$$

and it suffices to divide by $$\alpha > 0$$.

### Corollary (A non-negative function with zero integral is zero a.e.)

Let $$f : E \to [0,\infty]$$ be measurable such that $$\int_{E} f(x) \, dx = 0$$. Then $$f = 0$$ almost everywhere.

***Proof:*** By Markov's inequality, for every $$\alpha > 0$$ we have that

$$
m(\{ f \geq \alpha \}) \leq \frac{1}{\alpha} \int_{E} f(x) \, dx = 0.
$$

Hence

$$
\{ f > 0 \} = \bigcup_{k=1}^{\infty} \left\{ f \geq \frac{1}{k} \right\}
$$

is a countable union of sets of measure zero, and therefore it is a set of measure zero. That is, $$f = 0$$ a.e.

## Linearity

### Theorem (Linearity of the integral for non-negative functions)

Let $$f, g : E \to [0,\infty]$$ be measurable and $$c \geq 0$$. Then

$$
\int_{E} \big( c f(x) + g(x) \big) \, dx = c \int_{E} f(x) \, dx + \int_{E} g(x) \, dx.
$$

***Proof:*** *Homogeneity.* If $$c = 0$$, with the convention $$0 \cdot \infty = 0$$ we have $$cf \equiv 0$$ and both sides of homogeneity are zero. So let $$c > 0$$; we shall prove that

$$
\int_{E} c f(x) \, dx = c \int_{E} f(x) \, dx.
$$

Let $$\{f_{k}\}$$ be a sequence of non-negative simple functions such that

$$
0 \leq f_{k} \leq f_{k+1} \qquad \text{and} \qquad \lim_{k \to \infty} f_{k} = f.
$$

If

$$
f_{k} = \sum_{i=1}^{m_{k}} a_{i} \mathbf{1}_{A_{i}},
$$

with the $$A_{i}$$ measurable and pairwise disjoint, we have that

$$
\lim_{k \to \infty} c f_{k} = \lim_{k \to \infty} \sum_{i=1}^{m_{k}} c a_{i} \mathbf{1}_{A_{i}} = c f(x), \qquad c f_{k} \leq c f_{k+1}.
$$

Then, applying the monotone convergence theorem twice and the formula for simple functions,

$$
\int_{E} c f(x) \, dx = \lim_{k \to \infty} \int_{E} c f_{k}(x) \, dx = \lim_{k \to \infty} \sum_{i=1}^{m_{k}} c a_{i}\, m(A_{i}) = c \lim_{k \to \infty} \sum_{i=1}^{m_{k}} a_{i}\, m(A_{i}) = c \int_{E} f(x) \, dx.
$$

*Additivity.* It remains to show additivity. To that end, let $$g_{k}$$ be a sequence of non-negative simple functions such that

$$
g_{k} \leq g_{k+1}, \qquad \lim_{k \to \infty} g_{k} = g.
$$

Then it follows that

$$
g_{k} + f_{k} \leq g_{k+1} + f_{k+1}, \qquad \lim_{k \to \infty} (g_{k} + f_{k}) = g + f.
$$

We shall first show additivity for simple functions, that is, that

$$
\int_{E} \big( g_{k}(x) + f_{k}(x) \big) \, dx = \int_{E} g_{k}(x) \, dx + \int_{E} f_{k}(x) \, dx.
$$

Let

$$
g_{k} = \sum_{j=1}^{\ell_{k}} b_{j} \mathbf{1}_{B_{j}}, \quad \text{with } E = \bigcup_{j=1}^{\ell_{k}} B_{j} \text{ pairwise disjoint},
$$

and let us recall that

$$
f_{k} = \sum_{i=1}^{m_{k}} a_{i} \mathbf{1}_{A_{i}}, \quad \text{with } E = \bigcup_{i=1}^{m_{k}} A_{i} \text{ pairwise disjoint}.
$$

Note that, since both families are partitions of $$E$$,

$$
\mathbf{1}_{A_{i}} = \sum_{j=1}^{\ell_{k}} \mathbf{1}_{B_{j} \cap A_{i}}, \qquad \mathbf{1}_{B_{j}} = \sum_{i=1}^{m_{k}} \mathbf{1}_{B_{j} \cap A_{i}},
$$

then

$$
g_{k}(x) + f_{k}(x) = \sum_{j=1}^{\ell_{k}} \sum_{i=1}^{m_{k}} b_{j} \mathbf{1}_{A_{i} \cap B_{j}} + \sum_{i=1}^{m_{k}} \sum_{j=1}^{\ell_{k}} a_{i} \mathbf{1}_{A_{i} \cap B_{j}} = \sum_{j=1}^{\ell_{k}} \sum_{i=1}^{m_{k}} (b_{j} + a_{i}) \mathbf{1}_{A_{i} \cap B_{j}},
$$

which is a simple function on the common partition $$\{A_{i} \cap B_{j}\}$$. Now, by finite additivity of the measure,

$$
\sum_{i=1}^{m_{k}} m(A_{i} \cap B_{j}) = m\left( B_{j} \cap \bigcup_{i=1}^{m_{k}} A_{i} \right) = m(B_{j} \cap E) = m(B_{j}),
$$

and in the same way we have

$$
\sum_{j=1}^{\ell_{k}} m(A_{i} \cap B_{j}) = m(A_{i}).
$$

Finally,

$$
\begin{aligned}
\int_{E} \big( f_{k}(x) + g_{k}(x) \big) \, dx &= \sum_{j=1}^{\ell_{k}} \sum_{i=1}^{m_{k}} (a_{i} + b_{j})\, m(A_{i} \cap B_{j}) \\
&= \sum_{j=1}^{\ell_{k}} b_{j} \sum_{i=1}^{m_{k}} m(A_{i} \cap B_{j}) + \sum_{i=1}^{m_{k}} a_{i} \sum_{j=1}^{\ell_{k}} m(A_{i} \cap B_{j}) \\
&= \sum_{j=1}^{\ell_{k}} b_{j}\, m(B_{j}) + \sum_{i=1}^{m_{k}} a_{i}\, m(A_{i}) \\
&= \int_{E} g_{k}(x) \, dx + \int_{E} f_{k}(x) \, dx.
\end{aligned}
$$

Since $$\{f_{k} + g_{k}\}$$ is an increasing sequence of simple functions converging to $$f + g$$, the monotone convergence theorem applied three times gives us

$$
\int_{E} (f + g) \, dx = \lim_{k \to \infty} \int_{E} (f_{k} + g_{k}) \, dx = \lim_{k \to \infty} \left( \int_{E} f_{k} \, dx + \int_{E} g_{k} \, dx \right) = \int_{E} f \, dx + \int_{E} g \, dx.
$$

Combining homogeneity with additivity, applied to $$cf$$ and $$g$$, we obtain the statement.
{% endraw %}
