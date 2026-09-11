---
layout: chapter
course: ma0505
chapter: 1
title: "Review: Norms on Rd and Connectedness"
slug: 01-review-norms-on-rd-and-connectedness
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/01-review-norms-on-rd-and-connectedness/
---

{% raw %}
## Norms on Rd

### Definition (Family of $$p$$ norms on $$\mathbb{R}^{d}$$)

On $$\mathbb{R}^{d}$$ we consider the following norms:

1. *Euclidean*: $$\|(x_{1},\dots,x_{d})\| = (x_{1}^{2}+\dots+x_{d}^{2})^{1/2}$$.
2. *Supremum norm*: $$\|(x_{1},\dots,x_{d})\|_{\infty} = \max\{ |x_{i}| : 1 \leq i \leq d\}$$.
3. *$$p$$ norm* ($$1 \leq p < \infty$$): $$\|(x_{1},\dots,x_{d})\|_{p} = (|x_{1}|^{p}+\dots+|x_{d}|^{p})^{1/p}$$.

The case $$p = 2$$ coincides with the Euclidean norm, that is,

$$
\|(x_{1},\dots,x_{d})\| = \|(x_{1},\dots,x_{d})\|_{2}.
$$

### Definition (Ball associated with a $$p$$ norm)

For $$x_{0} \in \mathbb{R}^{d}$$ and $$r > 0$$ we define

$$
B_{p}(x_{0},r) = \{ x \in \mathbb{R}^{d} : \|x - x_{0}\|_{p} < r \}.
$$

When $$p = 2$$ we simply write $$B(x_{0},r)$$.

### Definition (Open set in $$\mathbb{R}^{d}$$)

$$D \subseteq \mathbb{R}^{d}$$ is an *open set* if for every $$x_{0} \in D$$ there exists $$r > 0$$ such that

$$
B(x_{0},r) \subseteq D.
$$

In particular $$\emptyset$$ and $$\mathbb{R}^{d}$$ are open, and every ball is open.

## Equivalence of p norms on Rd

### Proposition (Bounds between the Euclidean norm and the supremum norm)

For every $$(x_{1},\dots,x_{d}) \in \mathbb{R}^{d}$$,

$$
\|(x_{1},\dots,x_{d})\|_{\infty} \leq \|(x_{1},\dots,x_{d})\| \leq \sqrt{d}\,\|(x_{1},\dots,x_{d})\|_{\infty}.
$$

***Proof:*** For $$1 \leq i \leq d$$, $$|x_{i}| \leq \sqrt{x_{1}^{2}+\dots+x_{d}^{2}} = \|(x_{1},\dots,x_{d})\|$$, which gives $$\|(x_{1},\dots,x_{d})\|_{\infty} \leq \|(x_{1},\dots,x_{d})\|$$. Conversely,

$$
\|(x_{1},\dots,x_{d})\| = \sqrt{x_{1}^{2}+\dots+x_{d}^{2}} \leq \left(d \max_{1 \leq i \leq d} |x_{i}|^{2}\right)^{1/2} = \sqrt{d}\,\|(x_{1},\dots,x_{d})\|_{\infty}.
$$

### Proposition (Bounds between the $$p$$ norm and the supremum norm)

For every $$1 \leq p < \infty$$ and every $$(x_{1},\dots,x_{d}) \in \mathbb{R}^{d}$$,

$$
\|(x_{1},\dots,x_{d})\|_{\infty} \leq \|(x_{1},\dots,x_{d})\|_{p} \leq d^{1/p} \|(x_{1},\dots,x_{d})\|_{\infty}.
$$

Consequently $$\|(x_{1},\dots,x_{d})\| \leq \sqrt{d}\,\|(x_{1},\dots,x_{d})\|_{p}$$.

***Proof:*** For each $$1\leq i\leq d$$, $$|x_{i}|^{p}\leq \sum_{j=1}^{d}|x_{j}|^{p}$$, and taking $$p$$-th roots yields the lower bound. For the upper bound,

$$
\sum_{j=1}^{d} |x_{j}|^{p} \leq d \max_{1\leq j\leq d} |x_{j}|^{p},
$$

and taking $$p$$-th roots concludes the argument. The last inequality combines both with the Euclidean bound $$\leq \sqrt{d} \|\cdot\|_{\infty}$$.

### Lemma (The $$p$$ norms define the same open sets in $$\mathbb{R}^{d}$$)

The norms $$\|\cdot\|_{p}$$ ($$1\leq p\leq\infty$$) determine the same family of open sets in $$\mathbb{R}^{d}$$.

***Proof:*** It suffices to show that given $$r > 0$$ there exists $$r_{p} > 0$$ with $$B_{p}(x,r_{p}) \subseteq B(x,r)$$ and, conversely, there exists $$r' > 0$$ with $$B(x,r') \subseteq B_{p}(x,r)$$. By the previous proposition, if $$\|x-y\|_{p} < r/\sqrt{d}$$ then $$\|x-y\| \leq \sqrt{d}\,\|x-y\|_{p} < r$$, so that $$r_{p} = r/\sqrt{d}$$ satisfies

$$
B_{p}\!\left(x,\tfrac{r}{\sqrt{d}}\right) \subseteq B(x,r).
$$

Analogously, $$B(x, r/d^{1/p}) \subseteq B_{p}(x,r)$$. Hence every set open with respect to one norm is open with respect to the other.

## Connectedness and path-connectedness in Rd

### Definition (Disconnected and connected set)

$$G \subseteq \mathbb{R}^{d}$$ is *disconnected* if there exist open sets $$G_{0}, G_{1}$$ such that

$$
G_{0} \cap G \neq \emptyset, \quad G_{1} \cap G \neq \emptyset, \quad G_{0} \cap G_{1} = \emptyset \quad\text{and}\quad G \subseteq G_{0} \cup G_{1}.
$$

A set is said to be *connected* if it is not disconnected.

### Definition (Curve)

A *curve* is a continuous function $$\gamma : [a,b] \to \mathbb{R}^{d}$$.

### Definition (Path-connected set)

$$E \subseteq \mathbb{R}^{d}$$ is *path-connected* if for all $$x_{0}, x_{1} \in E$$ there exists a curve $$\gamma : [a,b] \to \mathbb{R}^{d}$$ such that

$$
\gamma(a) = x_{0}, \quad \gamma(b) = x_{1} \quad\text{and}\quad \gamma(t) \in E \text{ for every } t \in [a,b].
$$

### Note (Reparametrisation to the interval $$[0,1]$$)

If $$\gamma : [a,b] \to \mathbb{R}^{d}$$ is continuous, then $$\gamma_{1} : [0,1] \to \mathbb{R}^{d}$$ given by $$\gamma_{1}(s) = \gamma((b-a)s + a)$$ is continuous. Hence, in the definition of path-connectedness one may assume $$a = 0$$ and $$b = 1$$.

### Lemma (A path-connected set admits no decomposition into disjoint open sets)

Let $$E \subseteq \mathbb{R}^{d}$$ be path-connected. Then there exist no non-empty open sets $$G_{0}, G_{1}$$ such that $$E \subseteq G_{0} \cup G_{1}$$ and $$G_{0} \cap G_{1} = \emptyset$$.

***Proof:*** Suppose such $$G_{0}, G_{1}$$ exist and take $$x_{0} \in G_{0} \cap E$$, $$x_{1} \in G_{1} \cap E$$. By path-connectedness there exists $$\gamma : [0,1] \to E$$ with $$\gamma(0)=x_{0}$$ and $$\gamma(1)=x_{1}$$. Since $$G_{0}$$ is open, there exists $$r > 0$$ with $$B(x_{0}, r) \subseteq G_{0}$$. By continuity of $$\gamma$$ there exists $$\delta > 0$$ such that $$|t| < \delta$$ implies $$\|\gamma(0) - \gamma(t)\| < r$$, so that $$\gamma(t) \in B(x_{0}, r) \subseteq G_{0}$$ for $$0 < t < \delta$$.

Define

$$
t_{0} = \sup \{ t > 0 : \gamma(s) \in G_{0},\ 0 \leq s < t \}.
$$

The set is bounded by $$1$$ and contains $$\delta/2$$ (since $$\gamma(s) \in G_{0}$$ for $$0 \leq s < \delta$$ by the above), so $$\delta/2 \leq t_{0} \leq 1$$. If $$\gamma(t_{0}) \in G_{0}$$, there exists $$r_{1} > 0$$ with $$B(\gamma(t_{0}), r_{1}) \subseteq G_{0}$$ and, by continuity, there exists $$\delta_{1} > 0$$ with $$|t_{0} - s| < \delta_{1} \implies \gamma(s) \in B(\gamma(t_{0}), r_{1}) \subseteq G_{0}$$. This contradicts the definition of the supremum.

Hence $$\gamma(t_{0}) \in E \setminus G_{0} \subseteq G_{1}$$. But then there would exist $$r_{2}, \delta_{2} > 0$$ such that $$|t_{0} - s| < \delta_{2} \implies \gamma(s) \in B(\gamma(t_{0}), r_{2}) \subseteq G_{1}$$. By definition of the supremum there exists $$s' \in (t_{0} - \delta_{2}, t_{0})$$ with $$\gamma(s') \in G_{0}$$; but then $$\gamma(s') \in G_{0} \cap G_{1} = \emptyset$$, a contradiction.

### Theorem (Relation between connectedness and path-connectedness in $$\mathbb{R}^{d}$$)

Let $$G \subseteq \mathbb{R}^{d}$$. Then:

1. If $$G$$ is path-connected, then $$G$$ is connected.
2. If $$G$$ is open and connected, then $$G$$ is path-connected.

***Proof:*** Part (1) is a direct consequence of the previous lemma. Part (2) is proved by fixing $$x_{0} \in G$$ and considering the set $$A = \{ x \in G : x \text{ can be joined to } x_{0} \text{ by a curve in } G\}$$; using that $$G$$ is open one shows that $$A$$ and $$G \setminus A$$ are both open, and by connectedness together with $$A \neq \emptyset$$ one concludes $$A = G$$.
{% endraw %}
