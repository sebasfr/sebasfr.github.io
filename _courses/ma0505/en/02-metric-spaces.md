---
layout: chapter
course: ma0505
chapter: 2
title: "Metric Spaces"
slug: 02-metric-spaces
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/02-metric-spaces/
---

{% raw %}
## Norms, distances and metrics

### Definition (Norm)

A *norm* on $$\mathbb{R}^{d}$$ is a function $$\|\cdot\| : \mathbb{R}^{d} \to [0, +\infty)$$ that satisfies:

1. $$\|x\| \geq 0$$ for every $$x \in \mathbb{R}^{d}$$, with $$\|x\| = 0$$ if and only if $$x = 0$$;
2. $$\|\lambda x\| = |\lambda|\,\|x\|$$ for every $$\lambda \in \mathbb{R}$$ and $$x \in \mathbb{R}^{d}$$;
3. $$\|x + y\| \leq \|x\| + \|y\|$$ for all $$x, y \in \mathbb{R}^{d}$$.

### Note (Distance induced by a norm on $$\mathbb{R}^{d}$$)

A norm induces a *distance* (or metric) $$d : \mathbb{R}^{d} \times \mathbb{R}^{d} \to [0, +\infty)$$ by $$d(x,y) = \|x - y\|$$, which satisfies:

1. $$d(x,y) = d(y,x)$$;
2. $$d(x,y) = 0 \iff x = y$$;
3. $$d(x,z) = \|x-z\| = \|x-y+y-z\| \leq \|x-y\| + \|y-z\| = d(x,y) + d(y,z)$$.

### Definition (Metric space)

Let $$E$$ be a set. A *metric* is a function $$d : E \times E \to [0, +\infty)$$ that satisfies:

1. $$d(x,y) = d(y,x)$$;
2. $$d(x,y) = 0$$ if and only if $$x = y$$;
3. $$d(x,y) \leq d(x,z) + d(z,y)$$ *(triangle inequality)*.

The pair $$(E, d)$$ is called a *metric space*.

### Example (The usual metric on $$\mathbb{R}^{d}$$)

On $$\mathbb{R}^{d}$$ with the Euclidean norm, $$d(x,y) = \|x - y\|$$ is a metric; the triangle inequality is the usual one for the modulus.

## Metric topology: balls, open sets and closed sets

### Definition (Open ball in a metric space)

Let $$(E, d)$$ be a metric space. For $$x_{0} \in E$$ and $$r > 0$$ we define

$$
B(x_{0}, r) = \{ y \in E : d(x_{0}, y) < r \}.
$$

### Definition (Open set in a metric space)

$$D \subseteq E$$ is an *open set* if for every $$x_{0} \in D$$ there exists $$r > 0$$ such that $$B(x_{0}, r) \subseteq D$$. In particular $$\emptyset$$ and $$E$$ are open.

### Lemma (Balls are open sets)

For all $$x_{0} \in E$$ and $$r > 0$$, $$B(x_{0}, r)$$ is an open set.

***Proof:*** Let $$x_{1} \in B(x_{0}, r)$$. We shall show that if $$0 < r_{1} < r - d(x_{0}, x_{1})$$, then $$B(x_{1}, r_{1}) \subseteq B(x_{0}, r)$$. Indeed, if $$y \in B(x_{1}, r_{1})$$, then

$$
d(x_{0}, y) \leq d(x_{0}, x_{1}) + d(x_{1}, y) < d(x_{0}, x_{1}) + r_{1} < d(x_{0}, x_{1}) + r - d(x_{0}, x_{1}) = r,
$$

whence $$y \in B(x_{0}, r)$$.

### Lemma (A finite intersection of open sets is open)

If $$G_{1}, G_{2}, \dots, G_{m}$$ are open in $$(E, d)$$, then $$\bigcap_{i=1}^{m} G_{i}$$ is open.

***Proof:*** It suffices to prove it for $$m = 2$$ and apply induction. Let $$x_{0} \in G_{1} \cap G_{2}$$. There exist $$r_{1}, r_{2} > 0$$ such that $$B(x_{0}, r_{1}) \subseteq G_{1}$$ and $$B(x_{0}, r_{2}) \subseteq G_{2}$$. Taking $$r = \min(r_{1}, r_{2})$$,

$$
B(x_{0}, r) \subseteq B(x_{0}, r_{1}) \cap B(x_{0}, r_{2}) \subseteq G_{1} \cap G_{2}.
$$

### Lemma (An arbitrary union of open sets is open)

If $$\{ G_{\lambda} \}_{\lambda \in \Lambda}$$ is any collection of open sets in $$(E, d)$$, then $$\bigcup_{\lambda \in \Lambda} G_{\lambda}$$ is open.

***Proof:*** If $$x_{0} \in \bigcup_{\lambda \in \Lambda} G_{\lambda}$$, then there exists $$\lambda_{0}$$ with $$x_{0} \in G_{\lambda_{0}}$$. Since $$G_{\lambda_{0}}$$ is open, there exists $$r > 0$$ such that $$B(x_{0}, r) \subseteq G_{\lambda_{0}} \subseteq \bigcup_{\lambda \in \Lambda} G_{\lambda}$$.

### Definition (Closed set)

$$F \subseteq E$$ is *closed* if $$E \setminus F$$ is open.

### Note (Basic properties of closed sets)

1. If $$\{ F_{\lambda} \}_{\lambda \in \Lambda}$$ is a family of closed sets, $$\bigcap_{\lambda \in \Lambda} F_{\lambda}$$ is closed, since

    $$
    E \setminus \bigcap_{\lambda \in \Lambda} F_{\lambda} = \bigcup_{\lambda \in \Lambda} (E \setminus F_{\lambda})
    $$

    is a union of open sets.
2. If $$F_{1}, \dots, F_{m}$$ are closed, then $$\bigcup_{i=1}^{m} F_{i}$$ is closed.

### Example (The properties of closed/open sets are not preserved when passing to arbitrary collections)

1. $$\bigcap_{n=1}^{\infty} \left( a - \tfrac{1}{n}, a + \tfrac{1}{n}\right) = \{ a\}$$ is not open. That is, a countable intersection of open sets is not necessarily open.
2. $$\left( a, b \right) = \bigcup_{n=1}^{\infty} \left[a + \tfrac{1}{n}, b - \tfrac{1}{n}\right]$$ is not closed. That is, a countable union of closed sets is not necessarily closed.
{% endraw %}
