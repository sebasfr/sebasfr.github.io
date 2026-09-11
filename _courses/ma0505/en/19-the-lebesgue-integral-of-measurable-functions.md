---
layout: chapter
course: ma0505
chapter: 19
title: "The Lebesgue Integral of Measurable Functions"
slug: 19-the-lebesgue-integral-of-measurable-functions
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/19-the-lebesgue-integral-of-measurable-functions/
---

{% raw %}
## The definition and integrable functions

### Definition (Positive part, negative part and the general integral)

Let $$f : E \to \overline{\mathbb{R}}$$ be a measurable function. Then

$$
f = f^{+} - f^{-}
$$

with

$$
f^{+} = \max(0, f) \qquad \text{and} \qquad f^{-} = \max(0, -f).
$$

We know that $$f^{+}$$ and $$f^{-}$$ are measurable and non-negative, so

$$
\int_{E} f^{+} \, dx, \qquad \int_{E} f^{-} \, dx
$$

are well defined. Therefore we may define

$$
\int_{E} f \, dx = \int_{E} f^{+} \, dx - \int_{E} f^{-} \, dx
$$

provided that

$$
\int_{E} f^{+} \, dx < \infty \qquad \text{or} \qquad \int_{E} f^{-} \, dx < \infty.
$$

In that case we say that the integral of $$f$$ over $$E$$ *exists* (with value possibly $$\pm\infty$$).

### Definition (Integrable function and the space $$L(E)$$)

We say that $$f$$ is *integrable*, or that $$f \in L(E)$$, if

$$
\int_{E} f^{+} \, dx < \infty \qquad \text{and} \qquad \int_{E} f^{-} \, dx < \infty.
$$

### Note (Integral triangle inequality and a.e. finiteness)

Since $$|f| = f^{+} + f^{-}$$, for $$f \in L(E)$$ we have that

$$
\left| \int_{E} f \, dx \right| \leq \int_{E} f^{+} \, dx + \int_{E} f^{-} \, dx = \int_{E} |f| \, dx,
$$

where the last equality uses linearity for non-negative functions. In particular, $$f \in L(E)$$ if and only if $$\int_{E} |f| \, dx < \infty$$. Moreover, if $$\int_{E} |f| \, dx < \infty$$, then $$f \in \mathbb{R}$$ a.e., by the proposition on functions with finite integral.

## Monotonicity and basic properties

### Theorem (Monotonicity of the general integral)

Let $$f : E \to \overline{\mathbb{R}}$$ and $$g : E \to \overline{\mathbb{R}}$$ be measurable such that

$$
\int_{E} f \, dx \qquad \text{and} \qquad \int_{E} g \, dx
$$

exist. If $$f \leq g$$ a.e. on $$E$$, then

$$
\int_{E} f \, dx \leq \int_{E} g \, dx.
$$

In particular, if $$f = g$$ a.e. on $$E$$, then

$$
\int_{E} f \, dx = \int_{E} g \, dx.
$$

***Proof:*** Note that if $$f \leq g$$ a.e., then, pointwise where the inequality holds,

$$
f^{+} = \max\{0, f\} \leq \max\{0, g\} = g^{+}, \qquad g^{-} = \max\{0, -g\} \leq \max\{0, -f\} = f^{-},
$$

that is, $$f^{+} \leq g^{+}$$ and $$g^{-} \leq f^{-}$$ a.e. Hence, by the a.e. monotonicity of the integral of non-negative functions,

$$
\int_{E} f^{+} \, dx \leq \int_{E} g^{+} \, dx, \qquad \int_{E} g^{-} \, dx \leq \int_{E} f^{-} \, dx,
$$

and so, subtracting in the extended sense (the existence of both integrals guarantees that the form $$\infty - \infty$$ does not appear),

$$
\int_{E} f \, dx = \int_{E} f^{+} \, dx - \int_{E} f^{-} \, dx \leq \int_{E} g^{+} \, dx - \int_{E} g^{-} \, dx = \int_{E} g \, dx.
$$

If $$f = g$$ a.e., the two inequalities give the equality.

### Theorem (Restriction of the domain, countable additivity and null sets)

Let $$f : E \to \overline{\mathbb{R}}$$ be measurable such that $$\int_{E} f \, dx$$ exists.

1. If $$E_{1} \subseteq E$$ is measurable, then $$\int_{E_{1}} f \, dx$$ exists.
2. If $$E = \bigcup_{k=1}^{\infty} E_{k}$$ with the $$E_{k}$$ measurable and pairwise disjoint, then

    $$
    \int_{E} f \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f \, dx.
    $$
3. If $$E_{1} \subseteq E$$ with $$m(E_{1}) = 0$$, then $$\int_{E_{1}} f \, dx = 0$$.

***Proof:*** For (i), note that, by monotonicity with respect to the domain for non-negative functions,

$$
0 \leq \int_{E_{1}} f^{+} \, dx \leq \int_{E} f^{+} \, dx, \qquad 0 \leq \int_{E_{1}} f^{-} \, dx \leq \int_{E} f^{-} \, dx.
$$

Since one of the two integrals over $$E$$ is finite, so is the corresponding one over $$E_{1}$$, and $$\int_{E_{1}} f \, dx$$ exists.

For (ii), we know, by additivity of the domain for non-negative functions, that

$$
\int_{E} f^{+} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{+} \, dx, \qquad \int_{E} f^{-} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{-} \, dx.
$$

Since

$$
\int_{E} f^{+} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{+} \, dx < \infty \qquad \text{or} \qquad \int_{E} f^{-} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{-} \, dx < \infty,
$$

at least one of the two series converges, and we may subtract term by term without ambiguity. Then

$$
\int_{E} f \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{+} \, dx - \sum_{k=1}^{\infty} \int_{E_{k}} f^{-} \, dx = \sum_{k=1}^{\infty} \left( \int_{E_{k}} f^{+} \, dx - \int_{E_{k}} f^{-} \, dx \right) = \sum_{k=1}^{\infty} \int_{E_{k}} f \, dx.
$$

Finally, for (iii), if $$m(E_{1}) = 0$$, the lemma on the integral over null sets applied to $$f^{+}$$ and $$f^{-}$$ gives

$$
\int_{E_{1}} f \, dx = \int_{E_{1}} f^{+} \, dx - \int_{E_{1}} f^{-} \, dx = 0 - 0 = 0.
$$

## Linearity and differences of functions

### Theorem (Linearity of the general integral)

Let $$f, g : E \to \overline{\mathbb{R}}$$ be measurable such that $$\int_{E} f \, dx$$ exists, and let $$c \in \mathbb{R}$$. Then

$$
\int_{E} c f \, dx = c \int_{E} f \, dx.
$$

Moreover, if $$f, g \in L(E)$$, then $$f + g \in L(E)$$ and

$$
\int_{E} (f + g) \, dx = \int_{E} f \, dx + \int_{E} g \, dx.
$$

***Proof:*** *Homogeneity.* If $$c \geq 0$$, then $$(cf)^{+} = c f^{+}$$ and $$(cf)^{-} = c f^{-}$$, and the result follows from homogeneity for non-negative functions. If $$c < 0$$, then

$$
(cf)^{+} = -c f^{-}, \qquad (cf)^{-} = -c f^{+},
$$

since $$cf \geq 0$$ exactly where $$f \leq 0$$. Then

$$
\int_{E} c f \, dx = \int_{E} (-c) f^{-} \, dx - \int_{E} (-c) f^{+} \, dx = -c \int_{E} f^{-} \, dx + c \int_{E} f^{+} \, dx = c \int_{E} f \, dx.
$$

*Additivity.* If $$f, g$$ are integrable, then they are finite a.e., so that $$f + g$$ is defined a.e., and since $$|f + g| \leq |f| + |g|$$,

$$
0 \leq \int_{E} |f + g| \, dx \leq \int_{E} |f| \, dx + \int_{E} |g| \, dx < \infty,
$$

using monotonicity and linearity for non-negative functions; that is, $$f + g \in L(E)$$. Note that the following measurable, pairwise disjoint sets cover $$E$$ up to a null set (where $$f$$ or $$g$$ take infinite values):

$$
\begin{aligned}
&E_{1} = \{ f \geq 0,\ g \geq 0 \}, \\
&E_{2} = \{ f < 0,\ g < 0 \}, \\
&E_{3} = \{ f \geq 0,\ g < 0,\ f + g \geq 0 \}, \\
&E_{4} = \{ f < 0,\ g \geq 0,\ f + g \geq 0 \}, \\
&E_{5} = \{ f \geq 0,\ g < 0,\ f + g < 0 \}, \\
&E_{6} = \{ f < 0,\ g \geq 0,\ f + g < 0 \}.
\end{aligned}
$$

By additivity of the domain, it suffices to prove the additivity of the integral on each $$E_{i}$$.

On $$E_{1}$$ the three functions $$f, g, f+g$$ are non-negative, so, by linearity for non-negative functions,

$$
\int_{E_{1}} (f + g) \, dx = \int_{E_{1}} (f^{+} + g^{+}) \, dx = \int_{E_{1}} f^{+} \, dx + \int_{E_{1}} g^{+} \, dx = \int_{E_{1}} f \, dx + \int_{E_{1}} g \, dx,
$$

and likewise, on $$E_{2}$$, where all three are negative,

$$
\begin{aligned}
\int_{E_{2}} (f + g) \, dx &= \int_{E_{2}} -(f^{-} + g^{-}) \, dx = -\int_{E_{2}} (f^{-} + g^{-}) \, dx \\
&= -\int_{E_{2}} f^{-} \, dx - \int_{E_{2}} g^{-} \, dx = \int_{E_{2}} f \, dx + \int_{E_{2}} g \, dx.
\end{aligned}
$$

On $$E_{3}$$ we have $$f = (f + g) + (-g)$$ with $$f + g \geq 0$$ and $$-g > 0$$; hence, by linearity for non-negative functions,

$$
\int_{E_{3}} f \, dx = \int_{E_{3}} \big( (f+g) - g \big) \, dx = \int_{E_{3}} (f + g) \, dx + \int_{E_{3}} (-g) \, dx = \int_{E_{3}} (f + g) \, dx - \int_{E_{3}} g \, dx,
$$

where the last step uses homogeneity with $$c = -1$$ and that $$g \in L(E_{3})$$. Therefore

$$
\int_{E_{3}} (f + g) \, dx = \int_{E_{3}} f \, dx + \int_{E_{3}} g \, dx.
$$

Moreover, on $$E_{5}$$ we have $$-g = -(f+g) + f$$ with $$-(f+g) > 0$$ and $$f \geq 0$$, so

$$
\int_{E_{5}} (-g) \, dx = \int_{E_{5}} \big( -(f+g) + f \big) \, dx = \int_{E_{5}} -(f+g) \, dx + \int_{E_{5}} f \, dx.
$$

Thus, multiplying by $$-1$$ and rearranging, we have that

$$
\int_{E_{5}} f \, dx + \int_{E_{5}} g \, dx = \int_{E_{5}} (f + g) \, dx.
$$

The cases $$E_{4}$$ and $$E_{6}$$ are analogous, interchanging the roles of $$f$$ and $$g$$; finishing the rest of the proof is an exercise.

### Note (Linear combinations and a warning about subtraction)

Let $$f_{1}, \dots, f_{n} \in L(E)$$ and $$a_{1}, \dots, a_{n} \in \mathbb{R}$$. Then, iterating the previous theorem, $$\sum_{k=1}^{n} a_{k} f_{k} \in L(E)$$ and

$$
\int_{E} \left( \sum_{k=1}^{n} a_{k} f_{k} \right) \, dx = \sum_{k=1}^{n} a_{k} \int_{E} f_{k} \, dx.
$$

Beware: when the integrals are not finite, it is in general *not* true that

$$
\int_{E} (f - g) \, dx = \int_{E} f \, dx - \int_{E} g \, dx.
$$

For example, consider $$f = \mathbf{1}_{[n,\infty)}$$ and $$g = \mathbf{1}_{[n+1,\infty)}$$: the difference $$f - g = \mathbf{1}_{[n,n+1)}$$ has integral $$1$$, but $$\int f \, dx = \int g \, dx = \infty$$ and the difference $$\infty - \infty$$ is not defined.

### Proposition (Subtracting an integrable minorant)

Let $$f$$ and $$\phi$$ be measurable on $$E$$ such that $$\phi \leq f$$ a.e. and $$\phi \in L(E)$$. Then $$\int_{E} f \, dx$$ and $$\int_{E} (f - \phi) \, dx$$ exist and

$$
\int_{E} (f - \phi) \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx.
$$

***Proof:*** Since $$\phi \leq f$$ a.e., we have $$-f \leq -\phi$$ a.e. and so

$$
f^{-} = \max(0, -f) \leq \max(0, -\phi) = \phi^{-} \quad \text{a.e.},
$$

whence

$$
0 \leq \int_{E} f^{-} \, dx \leq \int_{E} \phi^{-} \, dx < \infty.
$$

That is, $$\int_{E} f \, dx$$ exists, with value in $$(-\infty, \infty]$$, and two cases remain according to the value of $$\int_{E} f^{+} \, dx$$.

If $$\int_{E} f^{+} \, dx < \infty$$, then $$f \in L(E)$$, and since also $$-\phi \in L(E)$$, linearity gives directly

$$
\int_{E} (f - \phi) \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx.
$$

Now, if $$\int_{E} f^{+} \, dx = \infty$$, that is $$f \notin L(E)$$, we claim that $$f - \phi \notin L(E)$$. Indeed, where both are finite we have $$f = \phi + (f - \phi) \leq \phi^{+} + (f - \phi)$$, and since the right-hand side is non-negative,

$$
f^{+} \leq \phi^{+} + (f - \phi) \quad \text{a.e.}
$$

Integrating, by a.e. monotonicity and linearity for non-negative functions,

$$
\infty = \int_{E} f^{+} \, dx \leq \int_{E} \phi^{+} \, dx + \int_{E} (f - \phi) \, dx,
$$

and since $$\int_{E} \phi^{+} \, dx < \infty$$, it follows that $$\int_{E} (f - \phi) \, dx = \infty$$. Moreover $$f - \phi \geq 0$$ a.e., so

$$
\int_{E} (f - \phi) \, dx = \int_{E} (f - \phi)^{+} \, dx = \infty.
$$

We conclude that, in this case, both sides equal $$\infty$$:

$$
\int_{E} (f - \phi) \, dx = \infty = \int_{E} f \, dx - \int_{E} \phi \, dx,
$$

since $$\int_{E} f \, dx = \infty$$ and $$\int_{E} \phi \, dx \in \mathbb{R}$$.

### Note (Products of integrable functions)

The conditions for $$fg$$ to be integrable are more complex than for the sum. For example, if $$f \in L(E)$$ and $$g$$ is measurable with $$|g(x)| \leq M$$ for $$x \in E$$, then $$fg \in L(E)$$, since $$|fg| \leq M |f|$$ and monotonicity gives $$\int_{E} |fg| \, dx \leq M \int_{E} |f| \, dx < \infty$$.

## The convergence theorems

### Theorem (Monotone convergence with an integrable minorant or majorant)

Let $$\{f_{k}\}_{k=1}^{\infty}$$ be a sequence of measurable functions on $$E$$, such that $$\lim_{k \to \infty} f_{k} = f$$ a.e. on $$E$$.

1. If there exists $$\phi \in L(E)$$ such that $$\phi \leq f_{k} \leq f_{k+1}$$ a.e. for every $$k \geq 1$$, then

    $$
    \lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx.
    $$
2. If there exists $$\phi \in L(E)$$ such that $$f_{k+1} \leq f_{k} \leq \phi$$ a.e. for every $$k \geq 1$$, then

    $$
    \lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx.
    $$

***Proof:*** We shall prove only the increasing case; part (ii) is left as an exercise for the reader. If the first condition holds, then

$$
f_{k} - \phi \geq 0 \qquad \text{and} \qquad f_{k+1} - \phi \geq f_{k} - \phi \quad \text{a.e.}
$$

for $$k \geq 1$$, and moreover $$f_{k} - \phi \to f - \phi$$ a.e. Then, by the monotone convergence theorem for non-negative functions,

$$
\lim_{k \to \infty} \int_{E} (f_{k} - \phi) \, dx = \int_{E} (f - \phi) \, dx.
$$

By the proposition on subtracting an integrable minorant, applied to each $$f_{k}$$ and to $$f$$ (with minorant $$\phi$$),

$$
\int_{E} (f_{k} - \phi) \, dx = \int_{E} f_{k} \, dx - \int_{E} \phi \, dx, \qquad \int_{E} (f - \phi) \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx.
$$

That is,

$$
\lim_{k \to \infty} \int_{E} f_{k} \, dx - \int_{E} \phi \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx,
$$

and since $$\int_{E} \phi \, dx \in \mathbb{R}$$, we may cancel and conclude that $$\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx$$.

### Example (Term-by-term integration of series of non-negative functions)

Let $$f_{k} : E \to [0,\infty]$$ be measurable for $$k \geq 1$$. Then, if we set

$$
g_{m} = \sum_{k=1}^{m} f_{k},
$$

we have that $$0 \leq g_{m} \leq g_{m+1}$$. Hence, by the monotone convergence theorem and linearity,

$$
\begin{aligned}
\int_{E} \left( \sum_{k=1}^{\infty} f_{k} \right) \, dx &= \int_{E} \lim_{m \to \infty} g_{m}(x) \, dx = \lim_{m \to \infty} \int_{E} g_{m}(x) \, dx \\
&= \lim_{m \to \infty} \int_{E} \sum_{k=1}^{m} f_{k}(x) \, dx = \lim_{m \to \infty} \sum_{k=1}^{m} \int_{E} f_{k}(x) \, dx = \sum_{k=1}^{\infty} \int_{E} f_{k}(x) \, dx.
\end{aligned}
$$

### Example (A sequence converging to zero with constant integrals)

Let $$E = [0,1]$$ and define

$$
f_{k}(x) =
\begin{cases}
k & \text{if } 0 \leq x \leq \frac{1}{k}, \\
0 & \text{if } \frac{1}{k} < x \leq 1.
\end{cases}
$$

Then

$$
\int_{E} f_{k}(x) \, dx = k \cdot m\left( \left[0, \tfrac{1}{k}\right] \right) = 1 \quad \text{for every } k,
$$

but $$\lim_{k \to \infty} f_{k} = 0$$ a.e. on $$[0,1]$$: for $$x > 0$$, $$f_{k}(x) = 0$$ as soon as $$k > \tfrac{1}{x}$$. We ask:

When is $$\displaystyle \lim_{k \to \infty} \int_{E} f_{k}(x) \, dx = \int_{E} \lim_{k \to \infty} f_{k}(x) \, dx$$?

This example shows that some additional hypothesis (monotonicity, domination, etc.) is necessary.

### Theorem (Fatou's lemma)

Let $$f_{k} : E \to [0,\infty]$$ be a sequence of non-negative measurable functions. Then

$$
\int_{E} \liminf_{k \to \infty} f_{k} \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k} \, dx.
$$

***Proof:*** Recall that

$$
\liminf_{k \to \infty} f_{k} = \sup_{k \geq 1} \inf_{m \geq k} f_{m} = \lim_{k \to \infty} \inf_{m \geq k} f_{m}.
$$

Consider

$$
g_{k} = \inf_{m \geq k} f_{m};
$$

then $$\{g_{k}\}$$ is an increasing sequence of non-negative measurable functions with $$g_{k} \to \liminf_{k \to \infty} f_{k}$$. By the monotone convergence theorem,

$$
\int_{E} \Big( \liminf_{k \to \infty} f_{k} \Big) \, dx = \lim_{k \to \infty} \int_{E} \inf_{m \geq k} f_{m} \, dx.
$$

Note that

$$
\inf_{m \geq k} f_{m} \leq f_{n} \quad \text{for } n \geq k \geq 1.
$$

Then, by monotonicity, for $$n \geq k$$,

$$
\int_{E} \inf_{m \geq k} f_{m}(x) \, dx \leq \int_{E} f_{n}(x) \, dx,
$$

and taking the infimum over $$n \geq k$$,

$$
\int_{E} \inf_{m \geq k} f_{m}(x) \, dx \leq \inf_{n \geq k} \int_{E} f_{n}(x) \, dx.
$$

Now taking the limit as $$k \to \infty$$ on both sides,

$$
\lim_{k \to \infty} \int_{E} \inf_{m \geq k} f_{m}(x) \, dx \leq \lim_{k \to \infty} \inf_{n \geq k} \int_{E} f_{n}(x) \, dx = \liminf_{k \to \infty} \int_{E} f_{k}(x) \, dx.
$$

Combining with the first identity, we conclude that

$$
\int_{E} \liminf_{k \to \infty} f_{k} \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k} \, dx.
$$

### Note (Uniform bound on the integrals and the lower limit)

Note that if $$f_{k} : E \to [0,\infty]$$ is measurable for each $$k$$ and

$$
\int_{E} f_{k}(x) \, dx \leq M \quad \text{for every } k,
$$

then, by Fatou's lemma,

$$
\int_{E} \liminf_{k \to \infty} f_{k} \, dx \leq M.
$$

### Theorem (Lebesgue dominated convergence for non-negative functions)

Let $$\{f_{k}\}_{k=1}^{\infty}$$ be a sequence of non-negative measurable functions such that

$$
\lim_{k \to \infty} f_{k} = f
$$

a.e. on $$E$$. If there exists $$\phi$$ measurable with

$$
0 \leq f_{k} \leq \phi \quad \text{a.e. for every } k \geq 1, \qquad \int_{E} \phi(x) \, dx < \infty,
$$

then

$$
\lim_{k \to \infty} \int_{E} f_{k}(x) \, dx = \int_{E} f(x) \, dx.
$$

***Proof:*** Since $$f = \liminf_{k \to \infty} f_{k}$$ a.e., Fatou's lemma and the a.e. equality of the integrals give

$$
\int_{E} f(x) \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k} \, dx.
$$

Note moreover that $$0 \leq f \leq \phi$$ a.e., so $$f, f_{k} \in L(E)$$, since their integrals are dominated by $$\int_{E} \phi \, dx < \infty$$.

Now consider $$h_{k} = \phi - f_{k} \geq 0$$ a.e. By Fatou's lemma applied to $$\{h_{k}\}$$,

$$
\int_{E} \liminf_{k \to \infty} (\phi - f_{k}) \, dx \leq \liminf_{k \to \infty} \int_{E} (\phi - f_{k}) \, dx.
$$

Note that, since the limit of $$f_{k}$$ exists a.e.,

$$
\liminf_{k \to \infty} (\phi - f_{k}) = \lim_{k \to \infty} (\phi - f_{k}) = \phi - f \quad \text{a.e.}
$$

On the other hand, using linearity (all the functions involved are integrable), we have that

$$
\liminf_{k \to \infty} \int_{E} (\phi - f_{k})(x) \, dx = \liminf_{k \to \infty} \left( \int_{E} \phi(x) \, dx - \int_{E} f_{k}(x) \, dx \right) = \int_{E} \phi(x) \, dx - \limsup_{k \to \infty} \int_{E} f_{k}(x) \, dx.
$$

The last equality holds because $$\liminf_{k}(-a_{k}) = -\limsup_{k} a_{k}$$ for every real sequence $$\{a_{k}\}$$, and adding the finite constant $$\int_{E} \phi \, dx$$ commutes with the lower limit. Combining the three relations above and cancelling $$\int_{E} \phi \, dx \in \mathbb{R}$$, we conclude that

$$
\limsup_{k \to \infty} \int_{E} f_{k}(x) \, dx \leq \int_{E} f(x) \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k}(x) \, dx,
$$

that is, the limit exists and $$\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx$$.

### Theorem (Uniform convergence on domains of finite measure)

Let $$f_{k} \in L(E)$$ for $$k \geq 1$$. If $$\lim_{k \to \infty} f_{k} = f$$ uniformly on $$E$$ with $$m(E) < \infty$$, then $$f \in L(E)$$ and

$$
\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx.
$$

***Proof:*** Exercise.

### Note (The finite-measure hypothesis is essential for uniform convergence)

Note that $$f_{k}(x) = \frac{1}{k}$$ converges to zero uniformly on $$\mathbb{R}$$, but

$$
\int_{\mathbb{R}} f_{k} \, dx = \infty
$$

for every $$k$$, so the conclusion of the previous theorem fails without the hypothesis $$m(E) < \infty$$.
{% endraw %}
