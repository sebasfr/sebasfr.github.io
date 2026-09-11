---
layout: chapter
course: ma0505
chapter: 20
title: "The Relationship Between the Riemann and Lebesgue Integrals"
slug: 20-the-relationship-between-the-riemann-and-lebesgue-integrals
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/20-the-relationship-between-the-riemann-and-lebesgue-integrals/
---

{% raw %}
## Partitions and step functions

### Notation (Partitions and associated step functions)

Let $$f : [a,b] \to \mathbb{R}$$ be bounded by $$M$$, that is $$|f(x)| \leq M$$ on $$[a,b]$$, and let

$$
\Gamma_{k} = \{ a = x_{0}^{k} < x_{1}^{k} < \dots < x_{n_{k}}^{k} = b \}
$$

be a sequence of partitions of $$[a,b]$$ such that $$\Gamma_{k} \subseteq \Gamma_{k+1}$$ (each one refines the previous one) and whose mesh $$|\Gamma_{k}| = \max_{i} (x_{i}^{k} - x_{i-1}^{k})$$ tends to zero. Writing $$x_{i} = x_{i}^{k}$$ and $$n = n_{k}$$ to lighten the notation, consider:

1. if $$m_{i} = \inf_{[x_{i-1},x_{i}]} f(x)$$, the *lower step function*

    $$
    \ell_{k}(x) = \sum_{i=1}^{n-1} m_{i} \mathbf{1}_{[x_{i-1},x_{i})} + m_{n} \mathbf{1}_{[x_{n-1},x_{n}]};
    $$
2. if $$M_{i} = \sup_{[x_{i-1},x_{i}]} f(x)$$, the *upper step function*

    $$
    u_{k}(x) = \sum_{i=1}^{n-1} M_{i} \mathbf{1}_{[x_{i-1},x_{i})} + M_{n} \mathbf{1}_{[x_{n-1},x_{n}]}.
    $$

The integrals of these simple functions are the Darboux sums:

$$
\int_{[a,b]} \ell_{k}(x) \, dx = \sum_{i=1}^{n} m_{i} (x_{i} - x_{i-1}), \qquad \int_{[a,b]} u_{k}(x) \, dx = \sum_{i=1}^{n} M_{i} (x_{i} - x_{i-1}).
$$

### Note (Monotonicity of the step functions under refinement)

Note that

$$
\ell_{k}(x) \leq f(x) \leq u_{k}(x) \quad \text{for every } x \in [a,b].
$$

Recall that if $$\Gamma_{k} \subseteq \Gamma_{k+1}$$, then

1. $$\ell_{k} \leq \ell_{k+1}$$;
2. $$u_{k} \geq u_{k+1}$$.

Since $$|f(x)| \leq M$$ for $$x \in [a,b]$$, we have $$|\ell_{k}| \leq M$$ and $$|u_{k}| \leq M$$ on $$[a,b]$$. By monotonicity and boundedness, the pointwise limits

$$
\ell = \lim_{k \to \infty} \ell_{k}, \qquad u = \lim_{k \to \infty} u_{k},
$$

exist; they are measurable, being limits of measurable functions, and satisfy $$\ell(x) \leq f(x) \leq u(x)$$ for every $$x \in [a,b]$$.

### Proposition (The Darboux sums converge to the integrals of $$\ell$$ and $$u$$)

With the notation above,

$$
\lim_{k \to \infty} \int_{[a,b]} \ell_{k}(x) \, dx = \int_{[a,b]} \ell(x) \, dx, \qquad \lim_{k \to \infty} \int_{[a,b]} u_{k}(x) \, dx = \int_{[a,b]} u(x) \, dx.
$$

That is, these integrals are the limit of the lower and upper Darboux sums. Moreover,

$$
\int_{[a,b]} u(x) \, dx = \int_{[a,b]} \ell(x) \, dx \iff \int_{[a,b]} \big( u(x) - \ell(x) \big) \, dx = 0 \iff u = \ell \ \text{a.e.}
$$

***Proof:*** The functions $$\ell_{k} + M$$ and $$u_{k} + M$$ are measurable, non-negative, converge pointwise to $$\ell + M$$ and $$u + M$$ respectively, and are dominated by the constant $$2M$$, which is integrable on $$[a,b]$$ since $$m([a,b]) = b - a < \infty$$. The dominated convergence theorem then implies that

$$
\lim_{k \to \infty} \int_{[a,b]} (\ell_{k} + M) \, dx = \int_{[a,b]} (\ell + M) \, dx,
$$

and subtracting the constant $$M(b-a)$$ from both sides (linearity) gives the claim for $$\ell_{k}$$; the argument for $$u_{k}$$ is identical.

For the equivalences: since $$u - \ell \geq 0$$ and both are integrable (they are bounded by $$M$$ on a domain of finite measure), linearity gives

$$
\int_{[a,b]} u \, dx - \int_{[a,b]} \ell \, dx = \int_{[a,b]} (u - \ell) \, dx,
$$

so the first equivalence is immediate. The second is the corollary of Markov's inequality: a non-negative function has zero integral if and only if it is zero a.e.

### Note (If the sums agree, the Riemann integral is the Lebesgue integral)

We conclude that, if the lower and upper Darboux sums converge to the same value, then

$$
u = \ell = f \quad \text{a.e.}
$$

(since $$\ell \leq f \leq u$$), the function $$f$$ is measurable, as it agrees a.e. with the measurable function $$\ell$$, and therefore

$$
\lim_{k \to \infty} \sum_{i=1}^{n} m_{i} (x_{i} - x_{i-1}) = \lim_{k \to \infty} \sum_{i=1}^{n} M_{i} (x_{i} - x_{i-1}) = \int_{[a,b]} f(x) \, dx,
$$

where the integral is the Lebesgue one. That is, when $$f$$ is Riemann integrable, its Riemann integral coincides with its Lebesgue integral.

## Lebesgue's characterisation of Riemann integrability

### Theorem (Lebesgue's criterion: Riemann integrable is equivalent to continuous a.e.)

Let $$f : [a,b] \to \mathbb{R}$$ be bounded. Then the following are equivalent:

1. $$f$$ is Riemann integrable;
2. $$f$$ is continuous a.e. on $$[a,b]$$.

In that case, the Riemann and Lebesgue integrals of $$f$$ over $$[a,b]$$ coincide.

***Proof:*** We fix a sequence of partitions $$\Gamma_{k}$$ with $$\Gamma_{k} \subseteq \Gamma_{k+1}$$ and $$\lim_{k \to \infty} |\Gamma_{k}| = 0$$, and we use the notation of the previous subsection.

*(i) implies (ii).* We begin by assuming that $$f$$ is Riemann integrable; then the lower and upper sums both converge to the Riemann integral, and by the previous proposition $$u = \ell = f$$ a.e. Let

$$
Z = \{ \ell \neq f \} \cup \{ \ell \neq u \} \cup \{ f \neq u \} \cup \bigcup_{k=1}^{\infty} \Gamma_{k}.
$$

Then $$m(Z) = 0$$, since it is a countable union of null sets: the first three by the above, and each $$\Gamma_{k}$$ because it is finite. If $$x \notin Z$$, then

$$
u(x) = \ell(x) = f(x), \qquad x \notin \Gamma_{k} \ \text{for every } k \geq 1.
$$

We claim that $$f$$ is continuous at every $$x \notin Z$$. Suppose that $$f$$ is not continuous at $$x$$. Then there exists an $$\varepsilon > 0$$ such that for every $$\delta > 0$$ there exists $$x_{\delta}$$ with

$$
|x_{\delta} - x| < \delta \qquad \text{and} \qquad |f(x) - f(x_{\delta})| > \varepsilon.
$$

Given $$k$$, since $$x \notin \Gamma_{k}$$, there exist consecutive nodes $$x_{i-1}^{k}, x_{i}^{k}$$ such that $$x \in (x_{i-1}^{k}, x_{i}^{k})$$, which is open. Take $$\delta > 0$$ such that

$$
(x - \delta, x + \delta) \subseteq (x_{i-1}^{k}, x_{i}^{k}).
$$

Then $$x_{\delta} \in (x_{i-1}^{k}, x_{i}^{k})$$ and, since both points belong to the same subinterval of the partition,

$$
\varepsilon < |f(x) - f(x_{\delta})| \leq M_{i} - m_{i} = u_{k}(x) - \ell_{k}(x).
$$

Since this holds for every $$k$$, letting $$k \to \infty$$ we obtain

$$
u(x) - \ell(x) \geq \varepsilon > 0,
$$

which contradicts $$u(x) = \ell(x)$$. We conclude that $$f$$ is continuous at every point outside the null set $$Z$$, that is, $$f$$ is continuous a.e.

*(ii) implies (i).* Assume now that

$$
Z = \{ x \in [a,b] :\ f\ \text{is discontinuous at } x \}
$$

has measure zero. Let $$x \notin Z \cup \{a, b\}$$ and $$\varepsilon > 0$$. By continuity of $$f$$ at $$x$$, there exists $$\delta > 0$$ such that

$$
|x - y| < \delta \implies |f(x) - f(y)| < \frac{\varepsilon}{2}.
$$

Now take $$k_{0}$$ such that

$$
|\Gamma_{k}| < \frac{\delta}{2} \quad \text{if } k \geq k_{0}.
$$

For $$k \geq k_{0}$$, let $$i$$ be such that $$x \in [x_{i-1}, x_{i})$$. Then every point $$y$$ of the closed subinterval $$[x_{i-1}, x_{i}]$$ satisfies $$|y - x| \leq x_{i} - x_{i-1} \leq |\Gamma_{k}| < \delta$$, that is,

$$
[x_{i-1}, x_{i}] \subseteq (x - \delta, x + \delta).
$$

Therefore,

$$
f(x) - \frac{\varepsilon}{2} \leq f(y) \leq f(x) + \frac{\varepsilon}{2} \quad \text{for } y \in [x_{i-1}, x_{i}],
$$

and taking the infimum and supremum over that subinterval,

$$
f(x) - \frac{\varepsilon}{2} \leq m_{i} \leq M_{i} \leq f(x) + \frac{\varepsilon}{2}.
$$

That is, for $$k \geq k_{0}$$,

$$
|u_{k}(x) - f(x)| \leq \frac{\varepsilon}{2} < \varepsilon, \qquad |\ell_{k}(x) - f(x)| \leq \frac{\varepsilon}{2} < \varepsilon.
$$

The above tells us that

$$
\lim_{k \to \infty} \ell_{k}(x) = f(x), \qquad \lim_{k \to \infty} u_{k}(x) = f(x)
$$

for every $$x$$ outside the null set $$Z \cup \{a,b\}$$, that is, $$\ell = u = f$$ a.e.; in particular $$f$$ is measurable. By the dominated convergence theorem (applied as in the previous proposition, with domination by the constant $$M$$ on the finite-measure domain $$[a,b]$$), we have that

$$
\lim_{k \to \infty} \int_{[a,b]} \ell_{k}(x) \, dx = \int_{[a,b]} f(x) \, dx, \qquad \lim_{k \to \infty} \int_{[a,b]} u_{k}(x) \, dx = \int_{[a,b]} f(x) \, dx.
$$

That is, the lower and upper Darboux sums both converge to the same value; in particular, given $$\varepsilon > 0$$ there exists a partition whose upper sum and lower sum differ by less than $$\varepsilon$$, and by Darboux's criterion $$f$$ is Riemann integrable. In conclusion, $$f$$ is Riemann integrable and the Riemann and Lebesgue integrals agree.
{% endraw %}
