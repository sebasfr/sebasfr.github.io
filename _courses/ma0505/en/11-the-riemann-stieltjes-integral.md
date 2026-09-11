---
layout: chapter
course: ma0505
chapter: 11
title: "The Riemann–Stieltjes Integral"
slug: 11-the-riemann-stieltjes-integral
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/11-the-riemann-stieltjes-integral/
---

{% raw %}
## Sums and definition of the integral

### Definition (Riemann–Stieltjes sum)

Let $$f, \phi : [a,b] \to \mathbb{R}$$ with $$f$$ bounded. Given a partition $$\Gamma = \{a = x_{0} < x_{1} < \dots < x_{n} = b\}$$ and intermediate points $$\xi_{i} \in [x_{i-1}, x_{i}]$$ for $$1 \leq i \leq n$$, the *Riemann–Stieltjes sum* of $$f$$ with respect to $$\phi$$ is

$$
R(f, \Gamma, \phi) = \sum_{i=1}^{n} f(\xi_{i})\,\big[\phi(x_{i}) - \phi(x_{i-1})\big].
$$

### Definition (Riemann–Stieltjes integral)

We say that $$f$$ is *Riemann–Stieltjes integrable* with respect to $$\phi$$ on $$[a,b]$$ if there exists $$I \in \mathbb{R}$$ such that for every $$\varepsilon > 0$$ there exists $$\delta > 0$$ with

$$
|\Gamma| < \delta \implies |R(f, \Gamma, \phi) - I| < \varepsilon
$$

for any choice of intermediate points $$\xi_{1}, \dots, \xi_{n}$$, where $$|\Gamma| = \max_{i}(x_{i} - x_{i-1})$$. In that case we write $$I = \int_{a}^{b} f \, d\phi$$.

### Exercise (Cauchy criterion for Riemann–Stieltjes integrability)

Prove that $$f$$ is Riemann–Stieltjes integrable with respect to $$\phi$$ if and only if for every $$\varepsilon > 0$$ there exists $$\delta > 0$$ such that

$$
|\Gamma| < \delta \ \text{ and }\ |\Gamma'| < \delta \implies |R(f, \Gamma, \phi) - R(f, \Gamma', \phi)| < \varepsilon
$$

for any choices of intermediate points.

### Lemma (A common discontinuity prevents integrability)

Let $$\phi : [a,b] \to \mathbb{R}$$ and let $$f : [a,b] \to \mathbb{R}$$ be bounded. If there exists $$z_{0} \in (a,b)$$ at which both $$f$$ and $$\phi$$ are discontinuous, then $$f$$ is not Riemann–Stieltjes integrable with respect to $$\phi$$.

***Proof:*** We show that the Cauchy criterion fails. Since $$f$$ and $$\phi$$ are discontinuous at $$z_{0}$$, there exists $$\varepsilon > 0$$ such that, for every $$\delta > 0$$, there is a point $$w_{\delta}$$ with $$0 < |w_{\delta} - z_{0}| < \delta$$ and $$|\phi(w_{\delta}) - \phi(z_{0})| \geq \sqrt{\varepsilon}$$, and a point $$\xi_{\delta}$$ with $$|\xi_{\delta} - z_{0}| < |w_{\delta} - z_{0}|$$ and $$|f(\xi_{\delta}) - f(z_{0})| \geq \sqrt{\varepsilon}$$; in particular $$\xi_{\delta}$$ lies strictly between $$z_{0}$$ and $$w_{\delta}$$. Take a partition $$\Gamma$$ with $$|\Gamma| < \delta$$ having $$z_{0}$$ and $$w_{\delta}$$ as consecutive nodes $$x_{i_{0}-1} = z_{0}$$, $$x_{i_{0}} = w_{\delta}$$, so that $$\xi_{\delta} \in (x_{i_{0}-1}, x_{i_{0}})$$. Construct two Riemann–Stieltjes sums with the same $$\Gamma$$ and the same intermediate points except on the subinterval $$[x_{i_{0}-1}, x_{i_{0}}]$$, where one takes $$\xi_{i_{0}} = \xi_{\delta}$$ and the other $$\xi_{i_{0}} = z_{0}$$. Then

$$
|R(f, \Gamma, \phi) - R'(f, \Gamma, \phi)| = |f(\xi_{\delta}) - f(z_{0})|\,|\phi(x_{i_{0}}) - \phi(x_{i_{0}-1})| = |f(\xi_{\delta}) - f(z_{0})|\,|\phi(w_{\delta}) - \phi(z_{0})| \geq \sqrt{\varepsilon}\cdot\sqrt{\varepsilon} = \varepsilon.
$$

Thus, for every $$\delta > 0$$ there are sums with norm smaller than $$\delta$$ that differ by at least $$\varepsilon$$, and the Cauchy criterion fails. The case in which the witnesses $$w_{\delta}$$ (for $$\phi$$) and $$\xi_{\delta}$$ (for $$f$$) cannot be taken on the same side of $$z_{0}$$ is handled analogously and is left as an exercise.

## Upper and lower sums

### Definition (Lower and upper Darboux–Stieltjes sums)

Let $$f : [a,b] \to \mathbb{R}$$ be bounded and $$\Gamma = \{a = x_{0} < \dots < x_{n} = b\}$$. For $$1 \leq i \leq n$$ let

$$
m_{i} = \inf_{x_{i-1} \leq \xi \leq x_{i}} f(\xi), \qquad M_{i} = \sup_{x_{i-1} \leq \xi \leq x_{i}} f(\xi).
$$

The *lower and upper sums* with respect to $$\phi$$ are

$$
L(f, \Gamma, \phi) = \sum_{i=1}^{n} m_{i}\,\big[\phi(x_{i}) - \phi(x_{i-1})\big], \qquad
U(f, \Gamma, \phi) = \sum_{i=1}^{n} M_{i}\,\big[\phi(x_{i}) - \phi(x_{i-1})\big].
$$

### Note (Sandwiching of the sums and the Riemann case)

If $$\phi$$ is increasing, then $$\phi(x_{i}) - \phi(x_{i-1}) \geq 0$$ and for every choice of intermediate points

$$
L(f, \Gamma, \phi) \leq R(f, \Gamma, \phi) \leq U(f, \Gamma, \phi).
$$

If $$\phi(x) = x$$ we recover the usual Riemann sums and the usual Riemann integral.

### Lemma (Monotonicity properties of the Darboux–Stieltjes sums)

Let $$f : [a,b] \to \mathbb{R}$$ be bounded and $$\phi : [a,b] \to \mathbb{R}$$ increasing.

1. If $$\Gamma_{1} \subseteq \Gamma_{2}$$ (refinement), then $$L(f, \Gamma_{1}, \phi) \leq L(f, \Gamma_{2}, \phi)$$ and $$U(f, \Gamma_{2}, \phi) \leq U(f, \Gamma_{1}, \phi)$$.
2. For any partitions $$\Gamma_{1}, \Gamma_{2}$$, $$\ L(f, \Gamma_{1}, \phi) \leq U(f, \Gamma_{2}, \phi)$$.

***Proof:*** *(1).* It suffices to insert a point $$y$$ into a subinterval $$[x_{i-1}, x_{i}]$$ of $$\Gamma_{1}$$. Since

$$
\sup_{[x_{i-1}, y]} f, \ \sup_{[y, x_{i}]} f \ \leq\ \sup_{[x_{i-1}, x_{i}]} f,
$$

and $$\phi(y) - \phi(x_{i-1}) \geq 0$$, $$\phi(x_{i}) - \phi(y) \geq 0$$ with sum $$\phi(x_{i}) - \phi(x_{i-1})$$, we obtain

$$
\big(\textstyle\sup_{[x_{i-1}, y]} f\big)\big(\phi(y) - \phi(x_{i-1})\big) + \big(\textstyle\sup_{[y, x_{i}]} f\big)\big(\phi(x_{i}) - \phi(y)\big) \leq \big(\textstyle\sup_{[x_{i-1}, x_{i}]} f\big)\big(\phi(x_{i}) - \phi(x_{i-1})\big),
$$

that is, refinement can only decrease $$U$$. Iterating over the added points, $$U(f, \Gamma_{2}, \phi) \leq U(f, \Gamma_{1}, \phi)$$. The argument for $$L$$ (with infima) is symmetric and gives $$L(f, \Gamma_{1}, \phi) \leq L(f, \Gamma_{2}, \phi)$$.

*(2).* Let $$\Gamma = \Gamma_{1} \cup \Gamma_{2}$$, a common refinement. By (1) and the previous note,

$$
L(f, \Gamma_{1}, \phi) \leq L(f, \Gamma, \phi) \leq U(f, \Gamma, \phi) \leq U(f, \Gamma_{2}, \phi).
$$

## Existence of the integral

### Note (Reduction to an increasing integrator)

From the definition one checks that if $$\int_{a}^{b} f\,d\phi_{1}$$ and $$\int_{a}^{b} f\,d\phi_{2}$$ exist and $$\phi = \phi_{1} - \phi_{2}$$, then $$\int_{a}^{b} f\,d\phi$$ exists and

$$
\int_{a}^{b} f\,d\phi = \int_{a}^{b} f\,d\phi_{1} - \int_{a}^{b} f\,d\phi_{2}.
$$

Since every function of bounded variation is a difference of two increasing functions (Jordan's characterisation), the study of integrability with respect to an integrator of bounded variation reduces to the case in which $$\phi$$ is increasing.

### Theorem (Existence of the integral for a continuous integrand and an integrator of bounded variation)

Let $$f : [a,b] \to \mathbb{R}$$ be continuous and $$\phi : [a,b] \to \mathbb{R}$$ of bounded variation. Then $$\int_{a}^{b} f\,d\phi$$ exists and

$$
\left| \int_{a}^{b} f\,d\phi \right| \leq \Big(\sup_{[a,b]} |f|\Big)\,\operatorname{Var}(\phi, [a,b]).
$$

***Proof:*** By the previous note it suffices to prove existence when $$\phi$$ is increasing; if $$\phi$$ is constant every sum vanishes and the integral equals $$0$$, so we assume $$\phi(b) > \phi(a)$$. Let $$\varepsilon > 0$$. Since $$f$$ is uniformly continuous, there exists $$\delta_{1} > 0$$ such that

$$
|x - y| < \delta_{1} \implies |f(x) - f(y)| < \frac{\varepsilon}{2\big(\phi(b) - \phi(a)\big)}.
$$

*The upper and lower sums approach each other.* If $$|\Gamma| < \delta_{1}$$, by continuity there exist $$\xi_{i}, \eta_{i} \in [x_{i-1}, x_{i}]$$ with $$f(\xi_{i}) = M_{i}$$, $$f(\eta_{i}) = m_{i}$$; since $$|\xi_{i} - \eta_{i}| \leq |\Gamma| < \delta_{1}$$,

$$
U(f, \Gamma, \phi) - L(f, \Gamma, \phi) = \sum_{i=1}^{n} (M_{i} - m_{i})\big(\phi(x_{i}) - \phi(x_{i-1})\big) \leq \frac{\varepsilon}{2(\phi(b) - \phi(a))}\big(\phi(b) - \phi(a)\big) = \frac{\varepsilon}{2}.
$$

*Stability of $$U$$.* If $$|\Gamma| < \delta_{1}$$ and $$|\Gamma'| < \delta_{1}$$, using $$U - L \leq \varepsilon/2$$ and $$L(f, \cdot, \phi) \leq U(f, \cdot, \phi)$$ between distinct partitions,

$$
U(f, \Gamma, \phi) \leq L(f, \Gamma, \phi) + \tfrac{\varepsilon}{2} \leq U(f, \Gamma', \phi) + \tfrac{\varepsilon}{2},
$$

and symmetrically, so that $$|U(f, \Gamma, \phi) - U(f, \Gamma', \phi)| \leq \varepsilon/2$$.

*Construction of the limit.* Take partitions $$\{\Gamma_{k}\}_{k=1}^{\infty}$$ with $$|\Gamma_{k}| \to 0$$ and let $$\Gamma_{k}' = \bigcup_{j=1}^{k} \Gamma_{j}$$, so that $$\Gamma_{k}' \subseteq \Gamma_{k+1}'$$ and $$\Gamma_{k} \subseteq \Gamma_{k}'$$. By monotonicity (1), $$\{U(f, \Gamma_{k}', \phi)\}_{k}$$ is decreasing and bounded below (by any lower sum), so that

$$
U := \inf_{k \geq 1} U(f, \Gamma_{k}', \phi) = \lim_{k \to \infty} U(f, \Gamma_{k}', \phi)
$$

exists. Given $$\varepsilon$$, let $$k_{0}$$ be such that $$0 \leq U(f, \Gamma_{k}', \phi) - U < \varepsilon/2$$ for $$k \geq k_{0}$$, and $$k_{1}$$ such that $$|\Gamma_{k}| < \delta_{1}$$ for $$k \geq k_{1}$$. Since $$\Gamma_{k} \subseteq \Gamma_{k}'$$ and both have norm $$< \delta_{1}$$, the stability of $$U$$ gives $$|U(f, \Gamma_{k}, \phi) - U(f, \Gamma_{k}', \phi)| \leq \varepsilon/2$$, hence for $$k \geq \max\{k_{0}, k_{1}\}$$,

$$
|U(f, \Gamma_{k}, \phi) - U| \leq |U(f, \Gamma_{k}, \phi) - U(f, \Gamma_{k}', \phi)| + |U(f, \Gamma_{k}', \phi) - U| < \varepsilon.
$$

*Independence of the sequence.* If $$\{\widetilde{\Gamma}_{k}\}$$ is another sequence with $$|\widetilde{\Gamma}_{k}| \to 0$$, for large $$k$$ both norms are $$< \delta_{1}$$ and the stability of $$U$$ gives $$|U(f, \Gamma_{k}, \phi) - U(f, \widetilde{\Gamma}_{k}, \phi)| \leq \varepsilon/2$$; hence $$U(f, \widetilde{\Gamma}_{k}, \phi) \to U$$ as well. Thus, $$U(f, \Gamma, \phi) \to U$$ as $$|\Gamma| \to 0$$.

*Conclusion.* It has already been shown that $$U(f, \Gamma, \phi) \to U$$ as $$|\Gamma| \to 0$$. Moreover, for $$|\Gamma| < \delta_{1}$$ we have that $$L(f, \Gamma, \phi) \geq U(f, \Gamma, \phi) - \tfrac{\varepsilon}{2}$$, so that also $$L(f, \Gamma, \phi) \to U$$. The sandwiching $$L(f, \Gamma, \phi) \leq R(f, \Gamma, \phi) \leq U(f, \Gamma, \phi)$$ then gives $$R(f, \Gamma, \phi) \to U$$ as $$|\Gamma| \to 0$$. Hence $$\int_{a}^{b} f\,d\phi = U$$ exists. Finally, for $$\phi$$ of bounded variation and any $$\Gamma$$,

$$
|R(f, \Gamma, \phi)| \leq \Big(\sup_{[a,b]}|f|\Big)\sum_{i=1}^{n}|\phi(x_{i}) - \phi(x_{i-1})| \leq \Big(\sup_{[a,b]}|f|\Big)\operatorname{Var}(\phi, [a,b]),
$$

and passing to the limit we obtain the stated bound.

## Properties: linearity, mean value and integration by parts

### Theorem (Linearity of the Riemann–Stieltjes integral)

Let $$f_{1}, f_{2} : [a,b] \to \mathbb{R}$$ be Riemann–Stieltjes integrable with respect to $$\phi_{1}, \phi_{2} : [a,b] \to \mathbb{R}$$, $$c \in \mathbb{R}$$ and $$a < c' < b$$. Then:

1. $$\displaystyle \int_{a}^{b}(c f_{1} + f_{2})\,d\phi_{1} = c\int_{a}^{b} f_{1}\,d\phi_{1} + \int_{a}^{b} f_{2}\,d\phi_{1}$$;
2. $$\displaystyle \int_{a}^{b} f_{1}\,d(c\phi_{1}) = c\int_{a}^{b} f_{1}\,d\phi_{1}$$;
3. $$\displaystyle \int_{a}^{b} f_{1}\,d(\phi_{1} + \phi_{2}) = \int_{a}^{b} f_{1}\,d\phi_{1} + \int_{a}^{b} f_{1}\,d\phi_{2}$$;
4. $$\displaystyle \int_{a}^{b} f_{1}\,d\phi_{1} = \int_{a}^{c'} f_{1}\,d\phi_{1} + \int_{c'}^{b} f_{1}\,d\phi_{1}$$.

***Proof:*** Exercise.

### Note (Bounds by the supremum and the infimum of the integrand)

If $$\phi$$ is increasing, from $$L(f, \Gamma, \phi) \leq R(f, \Gamma, \phi) \leq U(f, \Gamma, \phi)$$, $$U(f, \Gamma, \phi) \leq (\phi(b) - \phi(a))\sup_{[a,b]} f$$ and $$L(f, \Gamma, \phi) \geq (\phi(b) - \phi(a))\inf_{[a,b]} f$$ we obtain, passing to the limit,

$$
\Big(\inf_{[a,b]} f\Big)\big(\phi(b) - \phi(a)\big) \leq \int_{a}^{b} f\,d\phi \leq \Big(\sup_{[a,b]} f\Big)\big(\phi(b) - \phi(a)\big).
$$

### Lemma (Mean value theorem for the Riemann–Stieltjes integral)

Let $$f : [a,b] \to \mathbb{R}$$ be continuous and $$\phi : [a,b] \to \mathbb{R}$$ increasing, with $$f$$ Riemann–Stieltjes integrable with respect to $$\phi$$. Then there exists $$\xi \in [a,b]$$ such that

$$
\int_{a}^{b} f\,d\phi = f(\xi)\big(\phi(b) - \phi(a)\big).
$$

***Proof:*** If $$\phi(b) = \phi(a)$$, the bounds of the previous note give $$\int_{a}^{b} f\,d\phi = 0$$ and any $$\xi$$ will do. If $$\phi(b) > \phi(a)$$, dividing the same bounds by $$\phi(b) - \phi(a)$$,

$$
\inf_{[a,b]} f \ \leq\ \frac{1}{\phi(b) - \phi(a)}\int_{a}^{b} f\,d\phi \ \leq\ \sup_{[a,b]} f.
$$

Since $$f$$ is continuous on the compact set $$[a,b]$$, it attains its infimum and its supremum, and by the intermediate value theorem it takes every value between them; in particular there exists $$\xi \in [a,b]$$ at which $$f(\xi)$$ equals the quotient above, which gives the identity.

### Theorem (Integration by parts)

If $$\int_{a}^{b} f\,d\phi$$ exists, then $$\int_{a}^{b} \phi\,df$$ exists and

$$
\int_{a}^{b} f\,d\phi + \int_{a}^{b} \phi\,df = f(b)\phi(b) - f(a)\phi(a).
$$

***Proof:*** Let $$\Gamma = \{a = x_{0} < \dots < x_{n} = b\}$$ with intermediate points $$\xi_{i} \in [x_{i-1}, x_{i}]$$. Consider the points $$\xi_{0} = a$$, $$\xi_{n+1} = b$$ and the partition $$\Gamma' = \{\xi_{0}, \xi_{1}, \dots, \xi_{n+1}\}$$, which satisfies $$x_{i-1} \leq \xi_{i} \leq x_{i} \leq \xi_{i+1}$$, so that each $$x_{i}$$ is a valid intermediate point of $$\Gamma'$$. By summation by parts (Abel),

$$
R(f, \Gamma, \phi) = \sum_{i=1}^{n} f(\xi_{i})\big(\phi(x_{i}) - \phi(x_{i-1})\big) = -\sum_{i=0}^{n} \phi(x_{i})\big(f(\xi_{i+1}) - f(\xi_{i})\big) + f(b)\phi(b) - f(a)\phi(a),
$$

that is, $$R(f, \Gamma, \phi) = -R(\phi, \Gamma', f) + f(b)\phi(b) - f(a)\phi(a)$$, where $$R(\phi, \Gamma', f)$$ is a Riemann–Stieltjes sum of $$\phi$$ with respect to $$f$$ with partition $$\Gamma'$$ and intermediate points $$x_{i}$$. Since $$\xi_{i} \in [x_{i-1}, x_{i}]$$, each gap satisfies $$\xi_{i+1} - \xi_{i} \leq x_{i+1} - x_{i-1} \leq 2|\Gamma|$$, so that $$|\Gamma'| \leq 2|\Gamma| \to 0$$. Since $$\int_{a}^{b} f\,d\phi$$ exists, $$R(f, \Gamma, \phi) \to \int_{a}^{b} f\,d\phi$$ as $$|\Gamma| \to 0$$, and the algebraic identity above forces $$R(\phi, \Gamma', f) \to f(b)\phi(b) - f(a)\phi(a) - \int_{a}^{b} f\,d\phi$$. Since $$|\Gamma'| \to 0$$ and this limit does not depend on the chosen sequence of partitions, $$\int_{a}^{b} \phi\,df$$ exists and equals $$f(b)\phi(b) - f(a)\phi(a) - \int_{a}^{b} f\,d\phi$$, which is the desired identity.

## Passing to the limit under the integral sign

### Example (An increasing sequence of Riemann-integrable functions with a non-integrable limit)

Let $$\{r_{n}\}_{n=1}^{\infty}$$ be an enumeration of $$\mathbb{Q} \cap [0,1]$$ and

$$
f_{n} : [0,1] \to \mathbb{R}, \qquad f_{n}(x) = \begin{cases} 1, & x \in \{r_{1}, \dots, r_{n}\},\\ 0, & \text{otherwise.}\end{cases}
$$

Then $$f_{n} \leq f_{n+1}$$ and $$f_{n} \to f = \mathbf{1}_{\mathbb{Q} \cap [0,1]}$$ pointwise. It is an exercise to check that $$\int_{0}^{1} f_{n}(x)\,dx = 0$$ for every $$n$$, whereas $$f$$ is not Riemann integrable. Thus, the pointwise limit of Riemann-integrable functions need not be one, which motivates a more flexible notion of integral.

### Lemma (Passing to the limit under uniform convergence)

Let $$\phi : [a,b] \to \mathbb{R}$$ be of bounded variation and $$\{f_{n}\}_{n=1}^{\infty}$$ a sequence of functions Riemann–Stieltjes integrable with respect to $$\phi$$. If $$f_{n} \to f$$ uniformly on $$[a,b]$$ and $$f$$ is Riemann–Stieltjes integrable with respect to $$\phi$$, then

$$
\lim_{n \to \infty} \int_{a}^{b} f_{n}\,d\phi = \int_{a}^{b} f\,d\phi.
$$

***Proof:*** For any function $$g$$ Riemann–Stieltjes integrable with respect to $$\phi$$ and every partition $$\Gamma$$,

$$
|R(g, \Gamma, \phi)| \leq \Big(\sup_{[a,b]}|g|\Big)\sum_{i}|\phi(x_{i}) - \phi(x_{i-1})| \leq \Big(\sup_{[a,b]}|g|\Big)\operatorname{Var}(\phi, [a,b]),
$$

and passing to the limit, $$\big|\int_{a}^{b} g\,d\phi\big| \leq (\sup_{[a,b]}|g|)\operatorname{Var}(\phi, [a,b])$$. Applying this to $$g = f_{n} - f$$ (integrable, since $$f_{n}$$ and $$f$$ are) and using linearity,

$$
\left| \int_{a}^{b} f_{n}\,d\phi - \int_{a}^{b} f\,d\phi \right| = \left| \int_{a}^{b} (f_{n} - f)\,d\phi \right| \leq \Big(\sup_{[a,b]}|f_{n} - f|\Big)\operatorname{Var}(\phi, [a,b]).
$$

Since $$f_{n} \to f$$ uniformly, $$\sup_{[a,b]}|f_{n} - f| \to 0$$, and the right-hand side tends to zero.
{% endraw %}
