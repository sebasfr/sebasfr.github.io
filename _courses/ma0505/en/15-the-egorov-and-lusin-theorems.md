---
layout: chapter
course: ma0505
chapter: 15
title: "The Egorov and Lusin Theorems"
slug: 15-the-egorov-and-lusin-theorems
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/15-the-egorov-and-lusin-theorems/
---

{% raw %}
## Egorov's theorem

Throughout this section, $$m$$ denotes Lebesgue measure on $$\mathbb{R}^{d}$$, $$m_{e}$$ the outer measure, and “a.e.” abbreviates *almost everywhere*.

### Note (Pointwise convergence does not imply uniform convergence)

Recall that there exist sequences of continuous functions $$f_{k} : E \to \mathbb{R}$$ such that

$$
\lim_{k \to \infty} f_{k} = f
$$

pointwise on $$E$$, but such that $$f_{k}$$ does not converge uniformly to $$f$$ on compact sets. Egorov's theorem shows that, for measurable functions on a set of finite measure, pointwise convergence a.e. is indeed uniform outside a set of arbitrarily small measure.

### Example (The finite measure hypothesis is essential in Egorov)

Let $$E = \mathbb{R}^{d}$$ and

$$
f_{k}(x) = \mathbf{1}_{B(0,k)}(x).
$$

Then $$\lim_{k \to \infty} f_{k} = 1$$ pointwise on $$\mathbb{R}^{d}$$. Let $$F$$ be closed and unbounded; then for every $$k \in \mathbb{N}$$ there exists $$x \in F$$ such that

$$
|1 - f_{k}(x)| = 1,
$$

since $$F$$ has points outside $$B(0,k)$$. That is, the convergence cannot be uniform on $$F$$. Note moreover that, if $$F$$ is closed and $$m(\mathbb{R}^{d} \setminus F) < \infty$$, then $$F$$ is unbounded. Hence the conclusion of Egorov's theorem fails for this sequence: no closed set leaving out a set of finite measure admits uniform convergence.

### Lemma (Technical lemma preceding Egorov's theorem)

Let $$E \subseteq \mathbb{R}^{d}$$ be measurable with $$m(E) < \infty$$ and let $$\{f_{k}\}_{k=1}^{\infty}$$ be measurable functions on $$E$$ such that

$$
\lim_{k \to \infty} f_{k} = f \quad \text{a.e. on } E, \qquad |f(x)| \neq \infty \ \text{a.e. on } E.
$$

Then, given $$\varepsilon > 0$$ and $$\eta > 0$$, there exist a closed set $$F \subseteq E$$ and $$k_{0} = k_{0}(\varepsilon, \eta) \geq 0$$ such that

$$
m(E \setminus F) < \eta
$$

and

$$
|f_{k}(x) - f(x)| < \varepsilon \quad \text{for every } x \in F \text{ and } k \geq k_{0}.
$$

***Proof:*** Define

$$
\tilde{E} = \{ x \in E :\ \lim_{k \to \infty} f_{k}(x) = f(x),\ |f(x)| < \infty \}.
$$

By hypothesis, $$m(E \setminus \tilde{E}) = 0$$. For fixed $$\varepsilon > 0$$ and $$\eta > 0$$, define

$$
E_{m} = \{ x \in \tilde{E} :\ k \geq m \implies |f(x) - f_{k}(x)| < \varepsilon \}.
$$

Then each $$E_{m}$$ is measurable, since

$$
E_{m} = \tilde{E} \cap \bigcap_{k \geq m} \{ x \in E :\ |f(x) - f_{k}(x)| < \varepsilon \}
$$

is a countable intersection of measurable sets, and moreover $$E_{m} \subseteq E_{m+1}$$, since the condition is imposed on fewer indices $$k$$ as $$m$$ grows. We have that $$\bigcup_{m=1}^{\infty} E_{m} = \tilde{E}$$ (exercise; see the exercise below).

By continuity from below of the measure, we have that

$$
m(\tilde{E}) = \lim_{m \to \infty} m(E_{m}).
$$

Since $$m(\tilde{E}) \leq m(E) < \infty$$, we may subtract and obtain

$$
\lim_{m \to \infty} m(\tilde{E} \setminus E_{m}) = \lim_{m \to \infty} \big( m(\tilde{E}) - m(E_{m}) \big) = 0.
$$

Moreover $$E \setminus E_{m} = (E \setminus \tilde{E}) \cup (\tilde{E} \setminus E_{m})$$ and $$m(E \setminus \tilde{E}) = 0$$, so $$m(E \setminus E_{m}) = m(\tilde{E} \setminus E_{m}) \to 0$$. Let then $$k_{0}$$ be such that

$$
m(E \setminus E_{k_{0}}) < \frac{\eta}{2}.
$$

Note that if $$x \in E_{k_{0}}$$, then, by definition of $$E_{k_{0}}$$,

$$
|f(x) - f_{k}(x)| < \varepsilon \quad \text{for } k \geq k_{0}.
$$

Finally, since $$E_{k_{0}}$$ is measurable, by inner regularity there exists a closed set $$F$$ with $$F \subseteq E_{k_{0}}$$ satisfying

$$
m(E_{k_{0}} \setminus F) < \frac{\eta}{2}.
$$

Then

$$
m(E \setminus F) \leq m(E \setminus E_{k_{0}}) + m(E_{k_{0}} \setminus F) < \eta,
$$

and if $$x \in F \subseteq E_{k_{0}}$$ and $$k \geq k_{0}$$, we have that $$|f_{k}(x) - f(x)| < \varepsilon$$.

### Exercise (The union of the $$E_{m}$$ recovers $$\tilde{E}$$)

With the notation of the preceding proof, show that $$\bigcup_{m=1}^{\infty} E_{m} = \tilde{E}$$.

### Theorem (Egorov: a.e. convergence is almost uniform in finite measure)

Let $$E \subseteq \mathbb{R}^{d}$$ be measurable, with $$m(E) < \infty$$, and let $$\{f_{k}\}_{k=1}^{\infty}$$ be measurable functions on $$E$$. Suppose that

$$
\lim_{k \to \infty} f_{k} = f
$$

a.e. on $$E$$ and that $$|f(x)| \neq \infty$$ a.e. on $$E$$. Then, given $$\varepsilon > 0$$, there exists a closed set $$F_{\varepsilon} \subseteq E$$ such that:

1. $$m(E \setminus F_{\varepsilon}) < \varepsilon$$.
2. $$f_{k}$$ converges to $$f$$ uniformly on $$F_{\varepsilon}$$.

***Proof:*** Let $$\varepsilon > 0$$. Applying the preceding lemma with $$\varepsilon_{m} = \tfrac{1}{m}$$ and $$\eta_{m} = \tfrac{\varepsilon}{2^{m}}$$ for each $$m \geq 1$$, there exist closed sets $$F_{m} \subseteq E$$ and integers $$\kappa_{m}^{\varepsilon}$$ such that

$$
m(E \setminus F_{m}) < \frac{\varepsilon}{2^{m}}
$$

and

$$
|f(x) - f_{k}(x)| < \frac{1}{m} \quad \text{for every } k \geq \kappa_{m}^{\varepsilon} \text{ and } x \in F_{m}.
$$

Let

$$
F_{\varepsilon} = \bigcap_{m=1}^{\infty} F_{m}.
$$

Then $$F_{\varepsilon}$$ is closed, being an intersection of closed sets, and

$$
m(E \setminus F_{\varepsilon}) = m\left( E \cap \bigcup_{m=1}^{\infty} F_{m}^{c} \right) \leq \sum_{m=1}^{\infty} m(E \setminus F_{m}) < \sum_{m=1}^{\infty} \frac{\varepsilon}{2^{m}} = \varepsilon.
$$

Let us see that the convergence is uniform on $$F_{\varepsilon}$$. Given $$\delta > 0$$, take $$m \geq 1$$ with $$\tfrac{1}{m} < \delta$$. If $$x \in F_{\varepsilon} \subseteq F_{m}$$ and $$k \geq \kappa_{m}^{\varepsilon}$$, then

$$
|f(x) - f_{k}(x)| < \frac{1}{m} < \delta.
$$

Since $$\kappa_{m}^{\varepsilon}$$ does not depend on $$x$$, we conclude that $$f_{k} \to f$$ uniformly on $$F_{\varepsilon}$$.

## Lusin's theorem

### Definition (Property $$C$$ of a function)

A function $$f : E \to \mathbb{R}$$ has *property $$C$$* on $$E$$ if, given $$\varepsilon > 0$$, there exists a closed set $$F \subseteq E$$ such that

1. $$m(E \setminus F) < \varepsilon$$;
2. $$f$$ is continuous relative to $$F$$, that is, $$f : F \to \mathbb{R}$$ is continuous.

### Note (Sequential characterisation of relative continuity)

The second condition of the preceding definition is equivalent to the following: if $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ with

$$
\lim_{n \to \infty} x_{n} = x \in F,
$$

then

$$
\lim_{n \to \infty} f(x_{n}) = f(x).
$$

### Lemma (Measurable simple functions have property $$C$$)

Let $$\phi$$ be a simple, measurable function on $$E$$. Then $$\phi$$ has property $$C$$.

***Proof:*** Write

$$
\phi(x) = \sum_{\ell=1}^{m} b_{\ell} \mathbf{1}_{B_{\ell}}(x)
$$

with the $$B_{\ell} \subseteq E$$ measurable, $$B_{i} \cap B_{j} = \emptyset$$ and $$b_{i} \neq b_{j}$$ if $$i \neq j$$, and $$E = \bigcup_{\ell=1}^{m} B_{\ell}$$.

Given $$\varepsilon > 0$$, by inner regularity take, for each $$1 \leq \ell \leq m$$, a closed set $$F_{\ell} \subseteq B_{\ell}$$ such that

$$
m(B_{\ell} \setminus F_{\ell}) < \frac{\varepsilon}{m}.
$$

Then

$$
F = \bigcup_{\ell=1}^{m} F_{\ell}
$$

is closed, being a finite union of closed sets. Moreover, since the $$B_{\ell}$$ cover $$E$$, we have that $$E \setminus F \subseteq \bigcup_{\ell=1}^{m} (B_{\ell} \setminus F_{\ell})$$, and hence

$$
m(E \setminus F) \leq \sum_{\ell=1}^{m} m(B_{\ell} \setminus F_{\ell}) < m \cdot \frac{\varepsilon}{m} = \varepsilon.
$$

It remains to see that $$\phi$$ is continuous relative to $$F$$. Take $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ such that

$$
\lim_{n \to \infty} x_{n} = y \in F.
$$

Then there exists $$\ell_{0}$$ such that $$y \in F_{\ell_{0}}$$. We claim that, given $$\ell \neq \ell_{0}$$, the set

$$
\{x_{n}\}_{n=1}^{\infty} \cap F_{\ell}
$$

is finite. Otherwise, there exists a subsequence

$$
\{x_{n_{k}}\}_{k=1}^{\infty} \subseteq F_{\ell} \quad \text{with} \quad \lim_{k \to \infty} x_{n_{k}} = y.
$$

Since $$F_{\ell}$$ is closed, this implies that $$y \in F_{\ell}$$; but $$F_{\ell} \cap F_{\ell_{0}} \subseteq B_{\ell} \cap B_{\ell_{0}} = \emptyset$$, which leads to a contradiction.

Hence, since the $$x_{n}$$ are distributed among the $$F_{\ell}$$ and only finitely many fall outside $$F_{\ell_{0}}$$, there exists $$k_{0}$$ such that $$x_{n} \in F_{\ell_{0}}$$ for $$n \geq k_{0}$$. Then

$$
\phi(x_{n}) = b_{\ell_{0}} = \phi(y) \quad \text{for } n \geq k_{0},
$$

that is,

$$
\lim_{n \to \infty} \phi(x_{n}) = \phi(y).
$$

### Theorem (Lusin: measurability is equivalent to property $$C$$)

Let $$f : E \to \mathbb{R}$$ with $$E$$ measurable. Then $$f$$ is measurable if and only if $$f$$ has property $$C$$ on $$E$$.

***Proof:*** *Measurable implies property $$C$$, case $$m(E) < \infty$$.* Let $$f : E \to \mathbb{R}$$ be measurable; then there exists a sequence $$\{f_{k}\}_{k=1}^{\infty}$$ of simple, measurable functions such that

$$
\lim_{k \to \infty} f_{k}(x) = f(x)
$$

a.e. on $$E$$. Let $$\varepsilon > 0$$. By the preceding lemma, for each $$k \geq 1$$ there exists a closed set $$F_{k} \subseteq E$$ satisfying

$$
m(E \setminus F_{k}) < \frac{\varepsilon}{2^{k+1}},
$$

and such that $$f_{k}$$ is continuous relative to $$F_{k}$$. Since $$m(E) < \infty$$, by Egorov's theorem there exists a closed set $$F_{0} \subseteq E$$ such that

$$
m(E \setminus F_{0}) < \frac{\varepsilon}{2} \qquad \text{and} \qquad \lim_{k \to \infty} f_{k} = f \ \text{uniformly on } F_{0}.
$$

If we take

$$
F = F_{0} \cap \bigcap_{k=1}^{\infty} F_{k},
$$

then $$F$$ is closed, and since

$$
E \setminus F = (E \setminus F_{0}) \cup \bigcup_{k=1}^{\infty} (E \setminus F_{k}),
$$

we have that

$$
m(E \setminus F) \leq m(E \setminus F_{0}) + \sum_{k=1}^{\infty} m(E \setminus F_{k}) < \frac{\varepsilon}{2} + \sum_{k=1}^{\infty} \frac{\varepsilon}{2^{k+1}} = \varepsilon.
$$

Each $$f_{k}$$ is continuous relative to $$F_{k} \supseteq F$$, and hence continuous relative to $$F$$. Since

$$
\lim_{k \to \infty} f_{k} = f
$$

uniformly on $$F$$, and the uniform limit of continuous functions is continuous, we have that $$f$$ is continuous relative to $$F$$.

*Measurable implies property $$C$$, case $$m(E) = \infty$$.* Set

$$
E_{k} = E \cap \{ x \in \mathbb{R}^{d} :\ k-1 \leq |x| < k \}, \quad k \geq 1.
$$

The $$E_{k}$$ are measurable, pairwise disjoint, cover $$E$$ and $$m(E_{k}) \leq m(B(0,k)) < \infty$$. By the previous case, for each $$k$$ there exists a closed set $$F_{k} \subseteq E_{k}$$ such that $$f$$ is continuous relative to $$F_{k}$$ and

$$
m(E_{k} \setminus F_{k}) \leq \frac{\varepsilon}{2^{k}}.
$$

Take

$$
F = \bigcup_{k=1}^{\infty} F_{k}.
$$

Since $$E \setminus F \subseteq \bigcup_{k=1}^{\infty} (E_{k} \setminus F_{k})$$, we have that $$m(E \setminus F) \leq \sum_{k=1}^{\infty} \varepsilon/2^{k} = \varepsilon$$.

Let us see that $$F$$ is closed. Let $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ with $$\lim_{n \to \infty} x_{n} = y \in \mathbb{R}^{d}$$. Since the sequence converges, it is bounded: there exists $$k_{0}$$ such that

$$
n \geq k_{0} \implies |x_{n}| \leq |y| + 1.
$$

Let $$M$$ be an integer with $$M \geq |y| + 2$$. If $$x_{n} \in F_{k} \subseteq E_{k}$$ with $$n \geq k_{0}$$, then $$k - 1 \leq |x_{n}| \leq |y| + 1$$, that is $$k \leq |y| + 2 \leq M$$. Hence

$$
x_{n} \in \bigcup_{k=1}^{M} F_{k} \quad \text{for } n \geq k_{0},
$$

which is a finite union of closed sets and therefore closed. Then $$y \in \bigcup_{k=1}^{M} F_{k} \subseteq F$$, and $$F$$ is closed.

Let us see that $$f$$ is continuous relative to $$F$$. Let $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ with $$\lim_{n \to \infty} x_{n} = y \in F$$. By the above, there exists $$k_{0}$$ such that $$x_{n} \in \bigcup_{k=1}^{M} F_{k}$$ for $$n \geq k_{0}$$. Since the $$F_{k}$$ are closed and pairwise disjoint, by the argument in the proof of the preceding lemma there exist $$k_{1}$$ and $$\ell_{1}$$ such that

$$
n \geq k_{1} \implies x_{n} \in F_{\ell_{1}},
$$

with $$y \in F_{\ell_{1}}$$. Since $$f$$ is continuous relative to $$F_{\ell_{1}}$$, we conclude that $$\lim_{n \to \infty} f(x_{n}) = f(y)$$.

*Property $$C$$ implies measurable.* If $$f$$ has property $$C$$, then for each $$k \geq 1$$ there exists a closed set $$F_{k} \subseteq E$$ satisfying:

1. $$m(E \setminus F_{k}) < \frac{1}{k}$$;
2. $$f$$ is continuous relative to $$F_{k}$$.

Let

$$
H = \bigcup_{k=1}^{\infty} F_{k},
$$

then $$H \subseteq E$$ and $$m(E \setminus H) = 0$$ (exercise; see the exercise below). Write $$Z = E \setminus H$$. Finally, for each $$a \in \mathbb{R}$$,

$$
\begin{aligned}
\{ x \in E :\ f(x) > a \} &= \{ x \in H :\ f(x) > a \} \cup \{ x \in Z :\ f(x) > a \} \\
&= \bigcup_{k=1}^{\infty} \{ x \in F_{k} :\ f(x) > a \} \cup \{ x \in Z :\ f(x) > a \}.
\end{aligned}
$$

Each $$\{ x \in F_{k} :\ f(x) > a \}$$ is measurable: since $$f$$ is continuous relative to $$F_{k}$$, this set is open relative to $$F_{k}$$, that is, of the form $$F_{k} \cap G$$ with $$G$$ open in $$\mathbb{R}^{d}$$, which is measurable. On the other hand, $$\{ x \in Z :\ f(x) > a \} \subseteq Z$$ has outer measure zero and is therefore measurable. Then $$\{ f > a \}$$ is measurable for every $$a \in \mathbb{R}$$, that is, $$f$$ is measurable.

### Exercise (The complement of the union of the $$F_{k}$$ is null)

With the notation of the preceding proof, show that if $$H = \bigcup_{k=1}^{\infty} F_{k}$$ with $$m(E \setminus F_{k}) < \tfrac{1}{k}$$ for every $$k \geq 1$$, then $$m(E \setminus H) = 0$$.
{% endraw %}
