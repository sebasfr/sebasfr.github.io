---
layout: chapter
course: ma0505
chapter: 8
title: "Connectedness"
slug: 08-connectedness
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/08-connectedness/
---

{% raw %}
## Disconnected and connected sets

### Definition (Disconnected and connected space)

A space $$(X, d)$$ is *disconnected* if there exist non-empty open sets $$A, B$$ such that

$$
X = A \cup B, \quad A \cap B = \emptyset.
$$

A space is said to be *connected* if it is not disconnected. Equivalently, if $$X = A \cup B$$ with $$A, B$$ disjoint open sets, then $$A = X$$ or $$B = X$$.

### Definition (Disconnectedness of a subset)

$$E \subseteq X$$ is *disconnected* if there exist sets $$A, B$$ open in $$(X, d)$$ such that

$$
E = (A \cap E) \cup (B \cap E), \quad (A \cap B) \cap E = \emptyset, \quad A \cap E \neq \emptyset \neq B \cap E.
$$

That is, $$E$$ splits into two non-empty disjoint relatively open sets.

### Exercise (Characterisation of the open sets in subspaces)

Given $$E \subseteq X$$, define $$d_{E} : E \times E \to \mathbb{R}$$ by $$(x, y) \mapsto d(x, y)$$. Then $$(E, d_{E})$$ is a metric space. Prove that $$D \subseteq E$$ is open in $$(E, d_{E})$$ if and only if there exists $$O \subseteq X$$ open in $$(X, d)$$ such that $$D = E \cap O$$.

## Connected sets in R and properties

### Lemma (Open intervals are connected)

For $$a < b$$, the interval $$I = (a, b)$$ is connected.

***Proof:*** Suppose that $$I = (I \cap A) \cup (I \cap B)$$ with $$A, B$$ disjoint open sets and both pieces non-empty. Let $$s \in I \cap A$$, $$t \in I \cap B$$ with $$s < t$$; then $$[s, t] \subseteq I$$. Since $$s \in A$$ there exists $$\delta_{1} > 0$$ with $$(s - \delta_{1}, s + \delta_{1}) \subseteq A$$, so $$[s, s + \delta_{1}/2] \subseteq [s, t] \cap A$$.

Define $$u = \sup\{ x \in [s, t] : [s, x] \subseteq A\}$$. By construction $$s < u \leq t$$. If $$u \in B$$, there exists $$\delta_{2} > 0$$ with $$(u - \delta_{2}, u + \delta_{2}) \subseteq B \cap [s,t]$$; but by properties of the supremum there exists $$w \in [s, t] \cap A$$ with $$u - \delta_{2} < w \leq u$$, which would imply $$w \in A \cap B$$ (since $$w \in [s, t] \cap A$$ by the definition of the supremum and $$w \in (u - \delta_{2}, u + \delta_{2}) \subseteq B$$), contradicting $$A \cap B = \emptyset$$. If $$u \in A$$, there exists $$\delta_{3} > 0$$ with $$[u, u + \delta_{3}] \subseteq [s, t] \cap A$$, which contradicts the definition of the supremum when $$u < t$$, or contradicts $$t \in B$$ when $$u = t$$.

### Lemma (Continuous functions preserve connectedness)

Let $$f : X \to Y$$ be continuous. If $$E \subseteq X$$ is connected, then $$f(E)$$ is connected.

***Proof:*** Suppose that there exist open sets $$B, C \subseteq Y$$ such that $$f(E) = (f(E) \cap C) \cup (f(E) \cap B)$$ with both pieces non-empty and disjoint. Then

$$
\emptyset \neq f^{-1}(f(E) \cap C) = E \cap f^{-1}(C), \quad \emptyset \neq f^{-1}(f(E) \cap B) = E \cap f^{-1}(B),
$$

and $$E = (E \cap f^{-1}(C)) \cup (E \cap f^{-1}(B))$$ with $$f^{-1}(C), f^{-1}(B)$$ disjoint open sets in $$X$$, contradicting that $$E$$ is connected.

### Corollary ($$\mathbb{R}^{d}$$ is connected)

$$\mathbb{R}^{d}$$ is connected for every $$d \geq 1$$.

***Proof:*** Suppose $$\mathbb{R}^{d} = A \cup B$$ with $$A, B$$ non-empty disjoint open sets. Take $$x \in A$$, $$y \in B$$ and $$f : [0, 1] \to \mathbb{R}^{d}$$, $$t \mapsto (1-t)x + ty$$, which is continuous. Since $$[0, 1]$$ is connected, $$[x, y] = f([0,1])$$ is connected. But $$[x, y] = ([x,y] \cap A) \cup ([x,y] \cap B)$$ with both pieces non-empty, a contradiction.

### Lemma (Union of connected sets with a common point)

Let $$\{ E_{\alpha} : \alpha \in A\}$$ be a family of connected sets such that $$\bigcap_{\alpha \in A} E_{\alpha} \neq \emptyset$$. Then $$E = \bigcup_{\alpha \in A} E_{\alpha}$$ is connected.

***Proof:*** Let $$x \in \bigcap_{\alpha \in A} E_{\alpha}$$ and suppose, for a contradiction, that there exist open sets $$A', B'$$ with $$E = (A' \cap E) \cup (B' \cap E)$$, $$A' \cap E \neq \emptyset$$, $$B' \cap E \neq \emptyset$$ and $$A' \cap B' \cap E = \emptyset$$. Without loss of generality $$x \in B'$$.

Since $$A' \cap E \neq \emptyset$$, take $$y \in A' \cap E$$; since $$E = \bigcup_{\alpha} E_{\alpha}$$, there exists $$\alpha_{0}$$ with $$y \in E_{\alpha_{0}}$$, hence $$A' \cap E_{\alpha_{0}} \neq \emptyset$$. On the other hand $$x \in E_{\alpha_{0}}$$ (since $$x$$ lies in *every* $$E_{\alpha}$$) and $$x \in B'$$, so $$B' \cap E_{\alpha_{0}} \neq \emptyset$$.

Let us see that this splits $$E_{\alpha_{0}}$$ into two non-empty disjoint relatively open sets:

- **Cover:** every $$z \in E_{\alpha_{0}}$$ satisfies $$z \in E$$, hence (by the global decomposition) $$z \in A'$$ or $$z \in B'$$. Therefore

    $$
    E_{\alpha_{0}} \;\subseteq\; (E_{\alpha_{0}} \cap A') \cup (E_{\alpha_{0}} \cap B');
    $$

    the reverse inclusion is immediate. We conclude $$E_{\alpha_{0}} = (E_{\alpha_{0}} \cap A') \cup (E_{\alpha_{0}} \cap B')$$.
- **Disjointness:** $$(E_{\alpha_{0}} \cap A') \cap (E_{\alpha_{0}} \cap B') = E_{\alpha_{0}} \cap (A' \cap B') \subseteq E \cap (A' \cap B') = \emptyset$$.
- **Both non-empty:** already proved above.

This contradicts that $$E_{\alpha_{0}}$$ is connected.

## Connected components

### Definition (Connected component of a point)

Let $$(X, d)$$ be a metric space and $$x \in X$$. The *connected component* of $$x$$ is

$$
C(x) = \bigcup\{ E \subseteq X : E \text{ connected}, \; x \in E\}.
$$

### Note (The connected component is connected)

By the lemma on unions of connected sets with a common point, $$C(x)$$ is connected for every $$x \in X$$.

### Exercise (The components are equivalence classes)

Define the relation $$\mathcal{R}$$ on $$X$$ by $$x \mathcal{R} y \iff \exists\, C \text{ connected}\,(x, y \in C)$$. Prove that $$\mathcal{R}$$ is an equivalence relation and that $$[x] = C(x)$$.

## Characterisation of the connected sets in R

### Lemma (A connected subset of $$\mathbb{R}$$ contains the segments between its points)

Let $$E \subseteq \mathbb{R}$$ be connected and $$a, b \in E$$ with $$a \leq b$$. Then $$[a, b] \subseteq E$$.

***Proof:*** Suppose that there exists $$x \in [a, b] \setminus E$$. Then

$$
E = (E \cap (-\infty, x)) \cup (E \cap (x, \infty)),
$$

a decomposition of $$E$$ into two non-empty disjoint relatively open sets, contradicting that $$E$$ is connected.

### Theorem (The connected subsets of $$\mathbb{R}$$ are the intervals)

$$E \subseteq \mathbb{R}$$ is connected if and only if $$E$$ is an interval (bounded or not, open, closed or half-open).

***Proof:*** $$(\impliedby)$$: Open intervals are connected by a previous lemma, and the increasing union $$\bigcup_{n} (a + 1/n, b - 1/n)$$, $$\bigcup_{n} [a, b - 1/n]$$, etc., with non-empty intersection yields all the remaining types by applying the union lemma.

$$(\implies)$$: If $$E$$ is connected and bounded, define $$\alpha = \inf E$$, $$\beta = \sup E$$. Take $$\{a_{n}\}, \{b_{n}\} \subseteq E$$ with $$a_{n} \downarrow \alpha$$ and $$b_{n} \uparrow \beta$$. Then, by the previous lemma, $$[a_{n}, b_{n}] \subseteq E$$, and therefore $$(\alpha, \beta) = \bigcup_{n} [a_{n}, b_{n}] \subseteq E \subseteq [\alpha, \beta]$$. Thus $$E$$ is one of $$[\alpha, \beta], (\alpha, \beta], [\alpha, \beta), (\alpha, \beta)$$, according to whether $$\alpha, \beta \in E$$. If $$E$$ is not bounded above, define $$\beta = +\infty$$ and take $$b_{n} \in E$$ with $$b_{n} \to +\infty$$; then $$(\alpha, +\infty) = \bigcup_{n} [a_{n}, b_{n}] \subseteq E$$, so $$E \in \{ (\alpha, +\infty),\; [\alpha, +\infty) \}$$. Analogously for $$E$$ not bounded below, and the case $$E = \mathbb{R}$$ is obtained by combining the two.

### Exercise (Structure of the open sets in $$\mathbb{R}$$)

Let $$G \subseteq \mathbb{R}$$ be open. Prove that there exist disjoint open intervals $$\{ (a_{i}, b_{i})\}_{i=1}^{\infty}$$ such that $$G = \bigcup_{i=1}^{\infty} (a_{i}, b_{i})$$.

## Path-connectedness

### Definition (Path-connected set in $$\mathbb{R}^{d}$$)

$$E \subseteq \mathbb{R}^{d}$$ is *path-connected* if for all $$x_{0}, x_{1} \in E$$ there exists a curve $$\gamma : [0, 1] \to \mathbb{R}^{d}$$ such that

1. $$\gamma(0) = x_{0}$$ and $$\gamma(1) = x_{1}$$;
2. $$\gamma(t) \in E$$ for every $$t \in [0, 1]$$.

### Example (The topologist's sine curve: connected but not path-connected)

Consider

$$
E = \{(0, 0)\} \cup \left\{ (x, y) : 0 < x \leq 1,\; y = \sin\!\left(\tfrac{1}{x}\right) \right\}.
$$

*$$E$$ is connected.* Let $$A, B$$ be open with $$A \cap E \neq \emptyset \neq B \cap E$$, $$E \subseteq A \cup B$$ and $$A \cap B = \emptyset$$, and suppose $$(0, 0) \in A$$. For $$n \in \mathbb{N}$$ with $$n$$ large, $$x_{n} = (\tfrac{1}{\pi n}, \sin(\pi n)) = (\tfrac{1}{\pi n}, 0) \in A$$ (by convergence to $$(0,0)$$ and $$A$$ open). For each $$n$$,

$$
E_{n} = \left\{ (x, y) : \tfrac{1}{n\pi} \leq x \leq 1,\; y = \sin\!\left(\tfrac{1}{x}\right)\right\}
$$

is the continuous image of the interval $$[\tfrac{1}{\pi n}, 1]$$ and therefore is connected. Since $$E_{n} \cap A \neq \emptyset$$, $$E_{n} \cap B = \emptyset$$, so $$E_{n} \subseteq A$$, and taking unions $$\{(x, \sin(1/x)) : 0 < x \leq 1\} \subseteq A$$. We conclude $$E \subseteq A$$, contradicting $$B \cap E \neq \emptyset$$.

*$$E$$ is not path-connected.* Suppose that there exists a continuous $$\tilde{\gamma} : [0, 1] \to E$$ with $$\tilde{\gamma}(0) = (0, 0)$$ and $$\tilde{\gamma}(1) = (1/(n_{0}\pi), 0)$$. Let $$t_{0} = \sup\{ t > 0 : \tilde{\gamma}(t) = (0, 0)\}$$. Taking $$\{t_{n}\}$$ decreasing with $$t_{n} \to t_{0}$$, $$\tilde{\gamma}(t_{n}) \to (0, 0)$$, so $$\tilde{\gamma}_{1}(t_{n}) \to 0$$ and $$\tilde{\gamma}_{2}(t_{n}) = \sin(1/\tilde{\gamma}_{1}(t_{n}))$$ does not converge (it oscillates between $$-1$$ and $$1$$ along suitable $$t_{n}$$), contradicting the continuity of $$\tilde{\gamma}_{2}$$ at $$t_{0}$$.

### Exercise (Details of the path-connectedness counterexample)

In the previous example, prove:

1. If $$x_{n} < x_{n+1}$$ then, for $$x_{n} \leq x \leq x_{n+1}$$, $$(x, \sin(1/x)) \in \tilde{\gamma}([0,1])$$.
2. $$B = \{ (x, \sin(1/x)) : 0 < x < 1/(n_{0}\pi)\} \subseteq \tilde{\gamma}([0,1])$$.
3. $$\tilde{\gamma}([t_{0}, 1]) \setminus B = \{ (0, 0)\}$$.
4. $$\tilde{\gamma}$$ is not continuous at $$t_{0}$$.

### Lemma (On open subsets of $$\mathbb{R}^{d}$$, connected is equivalent to path-connected)

Let $$E \subseteq \mathbb{R}^{d}$$ be open. Then $$E$$ is connected if and only if $$E$$ is path-connected.

***Proof:*** $$(\impliedby)$$: By the general theorem, every path-connected set is connected.

$$(\implies)$$: Fix $$x_{0} \in E$$ and consider $$A = \{ x \in E : x \text{ is joined to } x_{0} \text{ by a curve in } E\}$$. Since $$E$$ is open and curves may be concatenated with balls, $$A$$ and $$E \setminus A$$ are both open in $$E$$ (around any $$y \in A$$ a ball in $$E$$ is joined to $$y$$ by a straight segment and, by concatenation, to $$x_{0}$$). By connectedness and $$A \neq \emptyset$$, $$A = E$$. (Details: *exercise*.)
{% endraw %}
