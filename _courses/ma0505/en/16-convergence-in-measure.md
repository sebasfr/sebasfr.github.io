---
layout: chapter
course: ma0505
chapter: 16
title: "Convergence in Measure"
slug: 16-convergence-in-measure
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/16-convergence-in-measure/
---

{% raw %}
## Definition and relation to convergence a.e.

### Definition (Convergence in measure)

Let $$f, f_{n} : E \to \overline{\mathbb{R}}$$ be measurable and finite almost everywhere. We say that $$f_{n}$$ *converges to $$f$$ in measure* if, for every $$\varepsilon > 0$$,

$$
\lim_{n \to \infty} m\{ |f_{n} - f| > \varepsilon \} = 0.
$$

We write $$f_{n} \xrightarrow{m} f$$.

### Note (Convergence in measure is the weakest convergence in the course)

This convergence is the weakest convergence we shall see in the course: uniform convergence implies pointwise convergence, pointwise convergence implies convergence a.e., and on sets of finite measure convergence a.e. implies convergence in measure, as the following theorem shows. None of the converse implications holds in general.

### Theorem (In finite measure, convergence a.e. implies convergence in measure)

Let $$f, f_{n} : E \to \overline{\mathbb{R}}$$ be measurable and finite almost everywhere. If

$$
\lim_{n \to \infty} f_{n} = f
$$

almost everywhere on $$E$$ and $$m(E) < \infty$$, then $$f_{n} \xrightarrow{m} f$$ on $$E$$.

***Proof:*** Let $$\eta > 0$$ and $$\varepsilon > 0$$; we must show that there exists $$n_{0}$$ such that

$$
m\{ |f_{n} - f| > \varepsilon \} < \eta
$$

whenever $$n \geq n_{0}$$. Since $$m(E) < \infty$$, by Egorov's theorem there exists a closed $$F \subseteq E$$ such that

$$
m(E \setminus F) < \eta
$$

and $$f_{n} \to f$$ uniformly on $$F$$. Then there exists $$n_{0}$$ such that

$$
|f_{n}(x) - f(x)| < \varepsilon \quad \text{for every } n \geq n_{0} \text{ and } x \in F.
$$

Hence

$$
\{ x \in E :\ |f_{n}(x) - f(x)| > \varepsilon \} \subseteq E \setminus F
$$

whenever $$n \geq n_{0}$$, and by monotonicity of the measure,

$$
m\{ x \in E :\ |f_{n}(x) - f(x)| > \varepsilon \} \leq m(E \setminus F) < \eta.
$$

### Example (The typewriter: convergence in measure without pointwise convergence)

Consider the sequence of indicator functions of dyadic intervals of $$[0,1]$$:

$$
\begin{gathered}
I_{0} = \mathbf{1}_{[0,1]}, \\
I_{1,1} = \mathbf{1}_{[0,\frac{1}{2}]}, \quad I_{1,2} = \mathbf{1}_{[\frac{1}{2},1]}, \\
I_{2,i} = \mathbf{1}_{[\frac{i-1}{2^{2}},\frac{i}{2^{2}}]}, \quad 1 \leq i \leq 4.
\end{gathered}
$$

In general, $$I_{n,i} = \mathbf{1}_{[\frac{i-1}{2^{n}},\frac{i}{2^{n}}]}$$ with $$1 \leq i \leq 2^{n}$$. To obtain a sequence we order the indices lexicographically:

$$
(m,i) \leq (n,j) \iff (m < n) \lor \big( (m = n) \land i \leq j \big).
$$

This sequence converges to zero in measure, since for $$0 < \varepsilon < 1$$ the set $$\{ I_{n,i} > \varepsilon \}$$ is an interval of measure $$2^{-n}$$, and $$n \to \infty$$ along the sequence. However, it converges at no point: for each $$x \in [0,1]$$ and each $$n$$ there exists some $$i$$ with $$x \in [\frac{i-1}{2^{n}},\frac{i}{2^{n}}]$$, so that the sequence takes the values $$1$$ and $$0$$ infinitely often at $$x$$.

### Theorem (Every sequence convergent in measure has a subsequence convergent a.e.)

Let $$f_{n} \xrightarrow{m} f$$ on $$E$$. Then there exist indices $$n_{1} < n_{2} < \dots$$ such that

$$
f_{n_{j}} \to f
$$

almost everywhere on $$E$$.

***Proof:*** Given $$j \geq 1$$, by convergence in measure there exists $$n_{j}$$ such that

$$
m\left\{ |f_{n} - f| > \frac{1}{j} \right\} \leq \frac{1}{2^{j}} \quad \text{if } n \geq n_{j}.
$$

Without loss of generality we may assume $$n_{j} < n_{j+1}$$, choosing the indices to be increasing. Then

$$
m\left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\} \leq \frac{1}{2^{j}}.
$$

Take

$$
H_{m} = \bigcup_{j \geq m} \left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\}.
$$

Then $$H_{m+1} \subseteq H_{m}$$ and, by countable subadditivity,

$$
m(H_{m}) \leq \sum_{j \geq m} m\left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\} \leq \sum_{j \geq m} \frac{1}{2^{j}} = \frac{1}{2^{m-1}}.
$$

Consider

$$
Z = \bigcap_{m \in \mathbb{N}} H_{m}.
$$

Since $$Z \subseteq H_{m}$$ for every $$m$$, we have that $$m(Z) \leq 2^{-(m-1)}$$ for every $$m$$, and hence $$Z$$ has measure zero. Moreover, if

$$
x \in E \setminus Z = \bigcup_{m \in \mathbb{N}} (E \setminus H_{m}),
$$

then there exists $$m_{0}$$ such that $$x \in E \setminus H_{m_{0}}$$. Since

$$
E \setminus H_{m_{0}} = E \setminus \bigcup_{j \geq m_{0}} \left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\} = \bigcap_{j \geq m_{0}} \left\{ |f_{n_{j}} - f| \leq \frac{1}{j} \right\},
$$

we obtain that, given $$x \in E \setminus Z$$, there exists $$m_{0}$$ such that

$$
|f_{n_{j}}(x) - f(x)| \leq \frac{1}{j} \quad \text{for } j \geq m_{0}.
$$

Finally, given $$\varepsilon > 0$$, there exists $$j_{0}$$ such that $$\tfrac{1}{j_{0}} < \varepsilon$$, and hence

$$
|f_{n_{j}}(x) - f(x)| \leq \frac{1}{j} \leq \frac{1}{j_{0}} < \varepsilon
$$

for $$j \geq \max(j_{0}, m_{0})$$. That is, $$f_{n_{j}}(x) \to f(x)$$ for every $$x$$ outside the null set $$Z$$.

## Cauchy sequences in measure

### Definition (Cauchy sequence in measure)

We say that $$(f_{n})_{n \in \mathbb{N}}$$ is *Cauchy in measure* if for all $$\varepsilon, \eta > 0$$ there exists $$N \in \mathbb{N}$$ such that

$$
m\{ |f_{n} - f_{m}| > \varepsilon \} < \eta
$$

for $$n, m \geq N$$.

### Lemma (Every Cauchy sequence in measure converges in measure)

A sequence that is Cauchy in measure is convergent in measure.

***Proof:*** Exercise.
{% endraw %}
