---
layout: chapter
course: ma0505
chapter: 5
title: "Compactness"
slug: 05-compactness
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/05-compactness/
---

{% raw %}
## Sequential compactness

### Definition (Sequentially compact set)

$$C \subseteq X$$ is *sequentially compact* if every sequence $$\{ x_{n}\}_{n=1}^{\infty} \subseteq C$$ has a subsequence converging to a point of $$C$$.

### Lemma (Characterisation by intersection of the closures of the tails)

Let $$(X, d)$$ be a metric space and $$C \subseteq X$$. The following are equivalent:

1. $$C$$ is sequentially compact;
2. for every $$\{ x_{n}\}_{n=1}^{\infty} \subseteq C$$,

    $$
    C \cap \left( \bigcap_{k=1}^{\infty} \overline{ \{ x_{m} : m \geq k\}} \right) \neq \emptyset.
    $$

***Proof:*** $$(1) \implies (2)$$: If $$\{ x_{n_{k}}\}_{k=1}^{\infty}$$ is a subsequence converging to $$x_{0} \in C$$, then given $$\varepsilon > 0$$ there exists $$k_{0}$$ such that $$k \geq k_{0}$$ implies $$d(x_{n_{k}}, x_{0}) < \varepsilon$$. Since $$n_{k} \geq k$$, it follows that $$B(x_{0}, \varepsilon) \cap \{ x_{m} : m \geq k\} \neq \emptyset$$ for every $$k \geq 1$$, so $$x_{0} \in \overline{ \{ x_{m} : m \geq k\}}$$ for every $$k$$.

$$(2) \implies (1)$$: Let $$x_{0} \in C \cap \bigcap_{k=1}^{\infty} \overline{ \{ x_{m} : m \geq k\}}$$. We iteratively construct a subsequence converging to $$x_{0}$$: we take $$x_{n_{1}} \in B(x_{0}, 1) \cap \{ x_{m} : m \geq 1\}$$, then $$x_{n_{2}} \in B(x_{0}, \tfrac{1}{2}) \cap \{ x_{m} : m \geq n_{1} + 1\}$$, and in general $$x_{n_{k+1}} \in B(x_{0}, \tfrac{1}{k}) \cap \{ x_{m} : m \geq n_{k} + 1\}$$. Then $$x_{n_{k}} \to x_{0}$$.

### Lemma (Sequentially compact implies closed and bounded)

Let $$C \subseteq X$$ be sequentially compact. Then $$C$$ is closed and bounded.

***Proof:*** *Closed:* Let $$x \in \overline{C}$$. There exists $$\{x_{n}\}_{n=1}^{\infty} \subseteq C$$ with $$x_{n} \to x$$. By sequential compactness there exists a subsequence $$\{x_{n_{k}}\}_{k=1}^{\infty}$$ converging to a point of $$C$$. By uniqueness of the limit, $$x \in C$$, so $$\overline{C} \subseteq C$$.

*Bounded:* If $$C$$ were not bounded, then, fixing $$x_{0} \in X$$, we could choose $$x_{n} \in C$$ with $$d(x_{0}, x_{n}) \geq n$$. Every subsequence $$\{x_{n_{k}}\}$$ would satisfy $$d(x_{0}, x_{n_{k}}) \to \infty$$ and hence could not be convergent, contradicting sequential compactness.

## Open covers and compactness

### Definition (Open cover)

A collection $$\mathcal{U} = \{ U_{\alpha} : \alpha \in \Lambda\}$$ of open sets is a *cover* (or *covering*) of $$A \subseteq X$$ if

$$
A \subseteq \bigcup_{\alpha \in \Lambda} U_{\alpha}.
$$

### Lemma (Technical covering lemma for sequentially compact sets (Lebesgue))

Let $$C \subseteq X$$ be sequentially compact and $$\mathcal{U}$$ an open cover of $$C$$. Then there exists $$\varepsilon > 0$$ such that for every $$x \in C$$ there exists $$U \in \mathcal{U}$$ with $$B(x, \varepsilon) \subseteq U$$.

***Proof:*** By contradiction: suppose that for every $$\varepsilon > 0$$ there exists $$x_{\varepsilon} \in C$$ such that $$B(x_{\varepsilon}, \varepsilon) \not\subseteq U$$ for any $$U \in \mathcal{U}$$. In particular, for $$\varepsilon = 1/n$$ there exists $$x_{n} \in C$$ with $$B(x_{n}, 1/n) \not\subseteq U_{\alpha}$$ for every $$\alpha \in \Lambda$$.

By sequential compactness there exist $$\{x_{n_{k}}\}_{k=1}^{\infty}$$ and $$x_{0} \in C$$ such that $$x_{n_{k}} \to x_{0}$$. Since $$\mathcal{U}$$ covers $$C$$, there exists $$U_{\alpha_{0}} \in \mathcal{U}$$ with $$x_{0} \in U_{\alpha_{0}}$$ and $$\varepsilon > 0$$ such that $$B(x_{0}, \varepsilon) \subseteq U_{\alpha_{0}}$$. Take $$k_{0}$$ such that $$k \geq k_{0}$$ implies $$d(x_{n_{k}}, x_{0}) < \varepsilon/2$$ and $$1/n_{k} < \varepsilon/2$$. Then, for $$y \in B(x_{n_{k}}, 1/n_{k})$$,

$$
d(y, x_{0}) \leq d(y, x_{n_{k}}) + d(x_{n_{k}}, x_{0}) < \tfrac{1}{n_{k}} + \tfrac{\varepsilon}{2} < \varepsilon,
$$

so $$B(x_{n_{k}}, 1/n_{k}) \subseteq B(x_{0}, \varepsilon) \subseteq U_{\alpha_{0}}$$, which contradicts the construction.

### Definition (Compact set)

$$C \subseteq X$$ is *compact* if, given an open cover $$\mathcal{U} = \{U_{\alpha} : \alpha \in \Lambda\}$$ of $$C$$, there exist $$U_{\alpha_{1}}, \dots, U_{\alpha_{m}} \in \mathcal{U}$$ such that

$$
C \subseteq \bigcup_{k=1}^{m} U_{\alpha_{k}}.
$$

That is, every open cover admits a finite subcover.

## Equivalence of the two notions of compactness

### Lemma (Sequential compactness is equivalent to compactness)

For $$C \subseteq X$$ the following are equivalent:

1. $$C$$ is sequentially compact;
2. $$C$$ is compact.

***Proof:*** $$(1) \implies (2)$$: Let $$\mathcal{U}$$ be an open cover of $$C$$. By the technical lemma above there exists $$\varepsilon > 0$$ such that for each $$x \in C$$ some ball $$B(x, \varepsilon)$$ is contained in some $$U_{\alpha}$$. Take $$x_{1} \in C$$ and $$\alpha_{1}$$ with $$B(x_{1}, \varepsilon) \subseteq U_{\alpha_{1}}$$. If $$C \subseteq B(x_{1}, \varepsilon)$$ we already have a finite subcover; if not, we choose $$x_{2} \in C \setminus B(x_{1}, \varepsilon)$$ and $$U_{\alpha_{2}}$$ with $$B(x_{2}, \varepsilon) \subseteq U_{\alpha_{2}}$$. Iterating, if at some step $$C \subseteq \bigcup_{i=1}^{m} B(x_{i}, \varepsilon) \subseteq \bigcup_{i=1}^{m} U_{\alpha_{i}}$$, we are done. Otherwise, we obtain $$\{x_{k}\}_{k=1}^{\infty} \subseteq C$$ with $$d(x_{i}, x_{j}) \geq \varepsilon$$ for $$i \neq j$$. This sequence admits no convergent subsequence: every convergent subsequence would be Cauchy, so its terms would eventually be at distance $$< \varepsilon$$, contradicting $$d(x_{i}, x_{j}) \geq \varepsilon$$. This contradicts sequential compactness.

$$(2) \implies (1)$$: Let $$\{x_{m}\}_{m=1}^{\infty} \subseteq C$$ and suppose, by contradiction, that it admits no subsequence converging in $$C$$. Define $$U_{n} = X \setminus \overline{\{x_{m} : m \geq n\}}$$. Then $$U_{n} \subseteq U_{n+1}$$ and $$X \setminus \bigcup_{n=1}^{\infty} U_{n} = \bigcap_{n=1}^{\infty} \overline{\{x_{m} : m \geq n\}}$$. Since $$\{x_{m}\}$$ has no subsequence converging in $$C$$, $$C \cap \bigcap_{k=1}^{\infty} \overline{\{x_{m} : m \geq k\}} = \emptyset$$, so $$C \subseteq \bigcup_{n=1}^{\infty} U_{n}$$. By compactness there exists a finite subcover; by monotonicity of $$\{U_{n}\}$$, there exists $$m_{0}$$ with $$C \subseteq U_{m_{0}}$$. But then $$\{x_{k} : k \geq m_{0}\} \subseteq C \subseteq X \setminus \overline{\{x_{k} : k \geq m_{0}\}}$$, a contradiction.

## Compactness and continuous functions

### Lemma (The continuous image of a compact set is compact)

Let $$f : X \to Y$$ be continuous and $$K \subseteq X$$ compact. Then $$f(K)$$ is compact in $$Y$$.

***Proof:*** Let $$\mathcal{U} = \{ U_{\alpha} : \alpha \in \Lambda_{1}\}$$ be an open cover of $$f(K)$$. Then $$K \subseteq f^{-1}\!\left( \bigcup_{\alpha \in \Lambda_{1}} U_{\alpha}\right) = \bigcup_{\alpha \in \Lambda_{1}} f^{-1}(U_{\alpha})$$, and each $$f^{-1}(U_{\alpha})$$ is open in $$X$$. By compactness of $$K$$, there exist $$\alpha_{1}, \dots, \alpha_{m}$$ such that

$$
K \subseteq \bigcup_{i=1}^{m} f^{-1}(U_{\alpha_{i}}),
$$

from which $$f(K) \subseteq \bigcup_{i=1}^{m} U_{\alpha_{i}}$$.

### Theorem (Characterisation by the finite intersection property)

Let $$(X, d)$$ be a metric space. The following are equivalent:

1. $$X$$ is compact;
2. if $$\mathcal{F} = \{ F_{\alpha} : \alpha \in \Lambda\}$$ is a family of closed sets such that $$\bigcap_{\alpha \in A} F_{\alpha} \neq \emptyset$$ for every finite $$A \subseteq \Lambda$$, then $$\bigcap_{\alpha \in \Lambda} F_{\alpha} \neq \emptyset$$.

***Proof:*** For both directions we use that $$\bigcap_{\alpha \in \Lambda} F_{\alpha} = \emptyset$$ if and only if $$X = \bigcup_{\alpha \in \Lambda} (X \setminus F_{\alpha})$$, that is, $$\{X \setminus F_{\alpha}\}_{\alpha}$$ is an open cover of $$X$$.

If $$X$$ is compact and the finite intersection property holds but $$\bigcap_{\alpha} F_{\alpha} = \emptyset$$, then there would exist $$\alpha_{1}, \dots, \alpha_{m}$$ with $$X = \bigcup_{i=1}^{m} (X \setminus F_{\alpha_{i}})$$, i.e. $$\bigcap_{i=1}^{m} F_{\alpha_{i}} = \emptyset$$, a contradiction.

Conversely, given an open cover $$\{ U_{\alpha}\}$$ with no finite subcover, $$\{X \setminus U_{\alpha}\}$$ is a family of closed sets with the finite intersection property but with empty total intersection.

## Compactness in Rd

### Note (Boxes in $$\mathbb{R}^{d}$$ are sequentially compact)

By the Bolzano-Weierstrass theorem, $$C = [a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}]$$ with $$a_{i} \leq b_{i}$$ is sequentially compact. Moreover every compact set is closed and bounded.

### Theorem (Heine-Borel in $$\mathbb{R}^{d}$$)

Let $$C \subseteq \mathbb{R}^{d}$$. Then $$C$$ is compact with respect to the Euclidean norm if and only if $$C$$ is closed and bounded.

***Proof:*** $$(\implies)$$: Every compact set is closed and bounded by the general lemma.

$$(\impliedby)$$: Let $$F \subseteq \mathbb{R}^{d}$$ be closed and bounded. There exists $$n$$ such that $$F \subseteq C_{n} = [-n, n]^{d}$$. Let $$\{x_{m}\}_{m=1}^{\infty} \subseteq F$$. Since $$C_{n}$$ is sequentially compact, there exists a subsequence $$\{x_{m_{k}}\}_{k=1}^{\infty}$$ converging to $$x_{0} \in C_{n}$$. Since $$\{x_{m_{k}}\} \subseteq F$$ and $$F$$ is closed, $$x_{0} \in F$$. Thus $$F$$ is sequentially compact and, by the equivalence, compact.

### Theorem (Extreme values)

Let $$K \subseteq X$$ be compact and $$f : X \to \mathbb{R}$$ continuous. Then $$f(K)$$ is compact and, in particular, $$f$$ attains its infimum and its supremum on $$K$$.

***Proof:*** $$f(K)$$ is compact, hence closed and bounded in $$\mathbb{R}$$. Let $$a = \inf_{x \in K} f(x)$$ and $$b = \sup_{x \in K} f(x)$$. For each $$n \in \mathbb{N}^{\ast}$$ there exists $$x_{n} \in K$$ with $$a \leq f(x_{n}) \leq a + 1/n$$. By compactness of $$K$$, there exists a subsequence $$\{x_{n_{k}}\}$$ converging to $$y_{0} \in K$$, and by continuity $$f(x_{n_{k}}) \to f(y_{0})$$; but $$f(x_{n_{k}}) \to a$$, hence $$f(y_{0}) = a$$. Analogously, $$b$$ is attained.
{% endraw %}
