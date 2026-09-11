---
layout: chapter
course: ma0505
chapter: 7
title: "The Arzelà–Ascoli Theorem"
slug: 07-the-arzela-ascoli-theorem
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/07-the-arzela-ascoli-theorem/
---

{% raw %}
## The space C(K,R)

### Definition (Space of continuous functions on a compact set)

Let $$(X, d)$$ be a metric space and $$K \subseteq X$$ compact. We define

$$
\mathcal{C}(K, \mathbb{R}) = \{ f : K \to \mathbb{R} \;:\; f \text{ continuous}\}
$$

and, for $$f, g \in \mathcal{C}(K, \mathbb{R})$$,

$$
d_{\infty}(f, g) = \sup_{x \in K} |f(x) - g(x)|.
$$

$$(\mathcal{C}(K, \mathbb{R}), d_{\infty})$$ is a metric space whose convergence coincides with uniform convergence.

## Equicontinuity

### Definition (Equicontinuous family)

Let $$\{f_{\alpha}\}_{\alpha \in \Omega}$$ be a family of functions $$f_{\alpha} : X \to Y$$ with $$(X, d), (Y, \rho)$$ metric spaces. We say that $$\{f_{\alpha}\}_{\alpha \in \Omega}$$ is *equicontinuous* at $$x_{0} \in X$$ if for every $$\varepsilon > 0$$ there exists $$\delta > 0$$ such that

$$
d(x_{0}, y) < \delta \implies \rho(f_{\alpha}(y), f_{\alpha}(x_{0})) < \varepsilon \quad \text{for every } \alpha \in \Omega.
$$

The family is *equicontinuous* if it is so at every point of $$X$$.

### Lemma (Compact subsets of $$\mathcal{C}(K, \mathbb{R})$$ are equicontinuous)

Let $$C \subseteq \mathcal{C}(K, \mathbb{R})$$ be compact. Then $$C$$ is equicontinuous: given $$\varepsilon > 0$$ and $$x_{0} \in K$$, there exists $$\delta > 0$$ such that for every $$f \in C$$ and every $$y \in K$$ with $$d(x_{0}, y) < \delta$$ we have $$|f(y) - f(x_{0})| < \varepsilon$$.

***Proof:*** By contradiction: if it were to fail, there would exist $$\varepsilon > 0$$ and $$x_{0} \in K$$ such that for every $$n \in \mathbb{N}$$ there exist $$y_{n}, k_{n}$$ with $$d(x_{0}, y_{n}) < 1/n$$ and $$|f_{k_{n}}(x_{0}) - f_{k_{n}}(y_{n})| \geq \varepsilon$$, where $$\{f_{k_{n}}\} \subseteq C$$. By compactness there exists a subsequence $$\{f_{k_{n_{l}}}\}_{l \geq 1}$$ which converges uniformly to a continuous function $$f : K \to \mathbb{R}$$. To simplify the notation, write $$\tilde{f}_{l} := f_{k_{n_{l}}}$$ and $$\tilde{y}_{l} := y_{n_{l}}$$. Then $$\tilde{y}_{l} \to x_{0}$$ and $$|\tilde{f}_{l}(x_{0}) - \tilde{f}_{l}(\tilde{y}_{l})| \geq \varepsilon$$.

Since $$\tilde{y}_{l} \to x_{0}$$ and $$f$$ is continuous, there exists $$l_{0}$$ such that $$|f(\tilde{y}_{l}) - f(x_{0})| < \varepsilon/3$$ for $$l \geq l_{0}$$. Then, for $$l$$ large,

$$
|\tilde{f}_{l}(\tilde{y}_{l}) - \tilde{f}_{l}(x_{0})| \leq d_{\infty}(\tilde{f}_{l}, f) + |f(\tilde{y}_{l}) - f(x_{0})| + d_{\infty}(\tilde{f}_{l}, f) < \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} = \varepsilon,
$$

contradicting that $$|f_{m_{l}}(y_{l}) - f_{m_{l}}(x_{0})| \geq \varepsilon$$.

### Lemma (Equicontinuity and pointwise convergence to a continuous function give uniform convergence)

Let $$\{f_{n}\}_{n=1}^{\infty}$$ be an equicontinuous family of functions $$f_{n} : X \to Y$$ and $$K \subseteq X$$ compact such that $$\lim_{n \to \infty} f_{n}(x) = f_{0}(x)$$ for every $$x \in K$$, with $$f_{0}$$ continuous on $$K$$. Then $$\{f_{n}\}$$ converges uniformly to $$f_{0}$$ on $$K$$.

***Proof:*** Let $$\varepsilon > 0$$. By equicontinuity, for each $$x \in K$$ there exists $$\delta_{x} > 0$$ such that $$y \in B(x, \delta_{x})$$ implies $$\rho(f_{n}(x), f_{n}(y)) < \varepsilon/3$$ for every $$n \geq 0$$. Since $$K$$ is compact, there exist $$x_{1}, \dots, x_{m}$$ with $$K \subseteq \bigcup_{i=1}^{m} B(x_{i}, \delta_{x_{i}})$$. Take $$n_{0}$$ such that $$\rho(f_{n}(x_{i}), f_{0}(x_{i})) < \varepsilon/3$$ for every $$1 \leq i \leq m$$ and every $$n \geq n_{0}$$.

For $$y \in K$$, there exists $$i$$ with $$y \in B(x_{i}, \delta_{x_{i}})$$, so

$$
\rho(f_{n}(y), f_{0}(y)) \leq \rho(f_{n}(y), f_{n}(x_{i})) + \rho(f_{n}(x_{i}), f_{0}(x_{i})) + \rho(f_{0}(x_{i}), f_{0}(y)) < \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} = \varepsilon
$$

for $$n \geq n_{0}$$.

### Lemma (Convergence on a dense set for an equicontinuous family yields continuity)

Let $$D \subseteq X$$ be dense and $$\{f_{n}\}_{n=1}^{\infty}$$ an equicontinuous sequence of functions $$f_{n} : X \to Y$$. Suppose that $$\{f_{n}(x)\}_{n=1}^{\infty}$$ converges for every $$x \in D$$ and that for each $$x \in X$$ the set $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ is complete (in particular this holds if $$Y$$ is complete, or if $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ is compact). Then $$\{f_{n}(x)\}$$ converges for every $$x \in X$$ and its limit is continuous.

***Proof:*** *Convergence.* Let $$x \in X$$ and $$\varepsilon > 0$$. By equicontinuity there exists $$\delta > 0$$ with

$$
d(x, y) < \delta \implies \rho(f_{n}(x), f_{n}(y)) < \varepsilon/3 \quad \text{for every } n \geq 1.
$$

By density there exists $$y \in B(x, \delta) \cap D$$ and, since $$\{f_{n}(y)\}$$ converges, there exists $$n_{0}$$ with $$\rho(f_{n}(y), f_{m}(y)) < \varepsilon/3$$ for $$n, m \geq n_{0}$$. Then

$$
\rho(f_{n}(x), f_{m}(x)) \leq \rho(f_{n}(x), f_{n}(y)) + \rho(f_{n}(y), f_{m}(y)) + \rho(f_{m}(y), f_{m}(x)) < \varepsilon,
$$

so $$\{f_{n}(x)\}$$ is Cauchy. Since $$\{f_{n}(x)\} \subseteq \overline{\{f_{n}(x)\}}$$ and the latter is complete by hypothesis, $$\{f_{n}(x)\}$$ converges in $$\overline{\{f_{n}(x)\}} \subseteq Y$$.

*Continuity of the limit.* Define $$f(x) = \lim_{n} f_{n}(x)$$. For $$d(x, y) < \delta$$,

$$
\rho(f(x), f(y)) = \lim_{n \to \infty} \rho(f_{n}(x), f_{n}(y)) \leq \tfrac{\varepsilon}{3},
$$

so $$f$$ is continuous at $$x$$.

### Note (Sufficient hypotheses on the codomain)

The hypothesis “$$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ complete” of the previous lemma is satisfied, for example, when $$Y$$ is complete (every closed subset of a complete space is complete) or when $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ is compact (since compact $$\Rightarrow$$ complete). The second case is the one used in the Arzelà-Ascoli Theorem below.

### Lemma (Pointwise convergence on a compact set under equicontinuity implies uniform convergence)

Let $$\{f_{n}\}_{n=1}^{\infty}$$ be an equicontinuous family, $$f_{n} : X \to Y$$, and $$K \subseteq X$$ compact. If $$\lim_{n \to \infty} f_{n}(x) = f_{0}(x)$$ exists in $$Y$$ for every $$x \in K$$, then $$f_{0}$$ is continuous and $$f_{n}$$ converges uniformly to $$f_{0}$$ on $$K$$.

***Proof:*** *Continuity of $$f_{0}$$.* Let $$x \in K$$ and $$\varepsilon > 0$$. By equicontinuity there exists $$\delta > 0$$ such that for every $$n \geq 1$$, $$d(x, y) < \delta$$ implies $$\rho(f_{n}(x), f_{n}(y)) < \varepsilon/3$$. Passing to the limit $$n \to \infty$$,

$$
\rho(f_{0}(x), f_{0}(y)) = \lim_{n \to \infty} \rho(f_{n}(x), f_{n}(y)) \leq \tfrac{\varepsilon}{3} < \varepsilon
$$

for $$d(x, y) < \delta$$, which proves the continuity of $$f_{0}$$ without requiring any additional hypothesis on $$Y$$.

*Uniform convergence.* Applying the first equicontinuity lemma (*Equicontinuity and pointwise convergence to a continuous function give uniform convergence*) with the continuous limit $$f_{0}$$ just obtained, $$f_{n} \to f_{0}$$ uniformly on $$K$$.

## The theorem

### Theorem (Arzelà-Ascoli)

Let $$X$$ be separable and $$\{f_{n}\}_{n=1}^{\infty}$$ an equicontinuous family of functions $$f_{n} : X \to Y$$. Suppose that $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ is compact for every $$x \in X$$. Then there exists a subsequence of $$\{f_{n}\}$$ which converges pointwise to a continuous function $$f : X \to Y$$. Moreover, the convergence is uniform on every compact set $$K \subseteq X$$.

***Proof:*** Let $$D = \{x_{n}\}_{n=1}^{\infty} \subseteq X$$ be dense (it exists by separability). Since $$\overline{\{f_{n}(x_{1})\}_{n=1}^{\infty}}$$ is compact, there exists a subsequence $$\{f_{n_{k}}^{1}\}_{k}$$ such that $$\{f_{n_{k}}^{1}(x_{1})\}$$ converges. Likewise $$\overline{\{f_{n_{k}}^{1}(x_{2})\}_{k}}$$ is compact (it is a closed set contained in the compact set $$\overline{\{f_{n}(x_{2})\}_{n=1}^{\infty}}$$, hence compact), so that there exists a subsequence $$\{f_{n_{k}}^{2}\}$$ of $$\{f_{n_{k}}^{1}\}$$ such that $$\{f_{n_{k}}^{2}(x_{2})\}$$ converges.

Iterating, given $$\{f_{n_{k}}^{m}\}$$ with $$\{f_{n_{k}}^{m}(x_{j})\}$$ convergent for $$1 \leq j \leq m$$, we extract a subsequence $$\{f_{n_{k}}^{m+1}\}$$ of $$\{f_{n_{k}}^{m}\}$$ such that $$\{f_{n_{k}}^{m+1}(x_{m+1})\}$$ converges. By construction, $$\{f_{n_{k}}^{m}(x_{j})\}$$ converges for $$1 \leq j \leq m$$.

We take the *diagonal* subsequence $$\{f_{n_{m}}^{m}\}_{m=1}^{\infty}$$. For $$j \leq m$$, $$\{f_{n_{m}}^{m}(x_{j})\}_{m \geq j}$$ is a subsequence of $$\{f_{n_{k}}^{j}\}$$ and therefore converges. Thus $$\{f_{n_{m}}^{m}\}$$ converges pointwise on $$D$$ and is equicontinuous. Moreover, for each $$x \in X$$, $$\overline{\{f_{n_{m}}^{m}(x)\}_{m=1}^{\infty}}$$ is a closed set contained in the compact set $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$, hence compact and in particular complete. By the previous lemma (applied with this completeness condition on the closures of the values), $$\{f_{n_{m}}^{m}\}$$ converges on all of $$X$$ to a continuous function $$f$$, and the convergence is uniform on compact sets.
{% endraw %}
