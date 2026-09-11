---
layout: chapter
course: ma0561
chapter: 16
title: "The Polynomial Ring"
slug: 16-the-polynomial-ring
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/16-the-polynomial-ring/
---

{% raw %}
## The construction of R[x]

### Definition (Eventually zero sequences in $$R$$)

Let $$R$$ be a ring. We define the set of sequences of $$R$$ as

$$
R^{\mathbb{N}} := \{ (a_{i})_{i \in \mathbb{N}} :\ a_{i} \in R \} = \{ (a_{0}, a_{1}, \dots, a_{n}, \dots) :\ a_{i} \in R \}.
$$

We call $$P \subseteq R^{\mathbb{N}}$$ the subset of *eventually zero* sequences, that is,

$$
P := \{ (a_{i})_{i \in \mathbb{N}} :\ \exists N \in \mathbb{N}\ (a_{k} = 0,\ \forall k > N) \}.
$$

### Definition (Addition and the identity elements in $$P$$)

Define the operation $$+$$ on $$P$$ as follows:

$$
(a_{i})_{i \in \mathbb{N}} + (b_{i})_{i \in \mathbb{N}} = (a_{i} + b_{i})_{i \in \mathbb{N}}.
$$

Note that this operation is closed on $$P$$. Define the one and the zero in $$P$$ as

$$
\begin{aligned}
1 &:= (1, 0, 0, \dots, 0, \dots), \\
0 &:= (0, 0, \dots, 0, \dots).
\end{aligned}
$$

### Definition (Scalar multiplication in $$P$$)

If $$c \in R$$ and $$(a_{i})_{i \in \mathbb{N}} \in P$$, define

$$
c \cdot (a_{i})_{i \in \mathbb{N}} = (c \cdot a_{0},\ c \cdot a_{1},\ \dots) \in P.
$$

### Notation (The powers $$x^{k}$$)

If $$k \in \mathbb{N}$$, define $$x^{k} := (\delta_{i,k})_{i \in \mathbb{N}}$$, where $$\delta_{i,k}$$ is the Kronecker delta. For example:

$$
\begin{aligned}
x^{1} &:= (0, 1, 0, \dots), \\
x^{2} &:= (0, 0, 1, \dots), \\
1 &= x^{0} = (1, 0, \dots, 0).
\end{aligned}
$$

### Example (A polynomial as a sequence)

$$
5 + 7x + 3x^{2} = 5 \cdot (1, 0, \dots, 0) + 7 \cdot (0, 1, 0, \dots, 0) + 3 \cdot (0, 0, 1, \dots) \in P.
$$

### Definition (The product of polynomials and the ring $$R[x]$$)

Let $$p = (a_{i})_{i \in \mathbb{N}}$$ and $$q = (b_{i})_{i \in \mathbb{N}}$$, with $$p, q \in P$$. Define $$p \cdot q = (c_{i})_{i \in \mathbb{N}}$$ such that

$$
c_{k} = \sum_{i=0}^{k} a_{i} \cdot b_{k-i}.
$$

Note that $$p \cdot q \in P$$. Thus, $$P$$ is a ring with these operations and we denote it by $$R[x]$$. This ring is called the *polynomial ring* over $$R$$.

## The degree of a polynomial

### Definition (Degree of a polynomial and leading coefficient)

Before defining the degree of a polynomial, we set out some conventions on the set $$\mathbb{N} \cup \{-\infty\}$$. In particular:

1. $$\forall n \in \mathbb{N}\ (-\infty < n)$$;
2. $$r + (-\infty) = -\infty$$ for $$r \in \mathbb{N}$$;
3. $$(-\infty) + (-\infty) = -\infty$$.

Let $$R$$ be a ring and $$p \in R[x]$$. We define the degree function $$\deg : R[x] \to \mathbb{N} \cup \{-\infty\}$$ such that

$$
\deg(p) =
\begin{cases}
-\infty & \text{if } p = 0, \\
n & \text{if } p = (a_{i})_{i \in \mathbb{N}},\ a_{n} \neq 0\ \text{and } n \text{ is the largest element of } \mathbb{N} \text{ such that } a_{n} \neq 0.
\end{cases}
$$

If $$\deg(p) = n$$, we say that $$a_{n}$$ is the *leading coefficient* of $$p$$.

### Proposition (Properties of the degree)

Let $$R$$ be a ring and let $$p, q \in R[x]$$. Then:

1. $$\deg(p + q) \leq \max\{\deg(p), \deg(q)\}$$;
2. $$\deg(p \cdot q) \leq \deg(p) + \deg(q)$$;
3. if $$p \neq 0$$, $$q \neq 0$$ and the leading coefficients of $$p$$ and $$q$$ are not zero divisors, then $$\deg(p \cdot q) = \deg(p) + \deg(q)$$.

***Proof:*** If $$p = 0$$ or $$q = 0$$, the three statements are immediate from the conventions concerning $$-\infty$$. Suppose then that $$p = (a_{i})_{i \in \mathbb{N}}$$ and $$q = (b_{i})_{i \in \mathbb{N}}$$ are non-zero, with $$\deg(p) = n$$ and $$\deg(q) = m$$.

For (1), if $$k > \max\{n, m\}$$, then $$a_{k} = 0$$ and $$b_{k} = 0$$, so that the $$k$$-th coefficient of $$p + q$$ is $$a_{k} + b_{k} = 0$$. That is, every coefficient of $$p + q$$ above $$\max\{n, m\}$$ vanishes, and therefore $$\deg(p + q) \leq \max\{\deg(p), \deg(q)\}$$.

For (2), write $$p \cdot q = (c_{k})_{k \in \mathbb{N}}$$ with $$c_{k} = \sum_{i=0}^{k} a_{i} b_{k-i}$$. If $$k > n + m$$, then in each summand $$a_{i} b_{k-i}$$ one of two things happens: either $$i > n$$, and then $$a_{i} = 0$$; or $$i \leq n$$, and then $$k - i \geq k - n > m$$, so that $$b_{k-i} = 0$$. In both cases the summand is zero, so $$c_{k} = 0$$ for $$k > n + m$$, and we conclude that $$\deg(p \cdot q) \leq \deg(p) + \deg(q)$$.

For (3), we examine the coefficient $$c_{n+m}$$: a summand $$a_{i} b_{n+m-i}$$ can only be non-zero if $$i \leq n$$ and $$n + m - i \leq m$$, that is, if $$i \geq n$$; hence the only possibly non-zero summand is the one with $$i = n$$, and $$c_{n+m} = a_{n} b_{m}$$. Since $$a_{n}$$ is not a zero divisor, $$a_{n} \neq 0$$ (it is the leading coefficient) and $$b_{m} \neq 0$$, we have that $$a_{n} b_{m} \neq 0$$. Hence $$c_{n+m} \neq 0$$ and, together with (2), $$\deg(p \cdot q) = n + m$$.

### Definition (The polynomial ring in $$n$$ variables)

Let $$R$$ be a commutative ring and $$n \geq 1$$. We define the polynomial ring in $$n$$ variables as

$$
R[x_{1}, \dots, x_{n}] =
\begin{cases}
R[x_{1}] & \text{if } n = 1, \\
R[x_{1}, \dots, x_{n-1}][x_{n}] & \text{if } n > 1.
\end{cases}
$$

### Note (Interpretation of polynomials as functions)

If $$p \in R[x]$$, then $$p$$ defines a function $$\tilde{p} : R \to R$$: if $$p = (a_{i})_{i \in \mathbb{N}} = a_{0} + a_{1} x + \dots + a_{n} x^{n}$$, then

$$
\tilde{p} :\ c \mapsto a_{0} + a_{1} c + \dots + a_{n} c^{n}.
$$

**Important:** the polynomial must not be confused with its associated function.

### Example (Distinct polynomials with the same associated function)

Consider the following polynomials in $$\mathbb{Z}_{3}[x]$$:

$$
\begin{aligned}
p &= x^{2} + 1, \\
q &= x^{3} + x^{2} + 2x + 1.
\end{aligned}
$$

Note that $$p \neq q$$ but $$\tilde{p} = \tilde{q}$$:

$$
\begin{aligned}
\tilde{p}(0) &= 1 = \tilde{q}(0), \\
\tilde{p}(1) &= 2 = \tilde{q}(1), \\
\tilde{p}(2) &= 2 = \tilde{q}(2).
\end{aligned}
$$

## The division algorithm and roots

### Theorem (Division algorithm for commutative rings)

Let $$R$$ be a commutative ring. Let $$f, g \in R[x]$$ be such that $$g \neq 0$$, and let $$b$$ be the leading coefficient of $$g$$. Then there exist $$m \geq 0$$ and $$q, r \in R[x]$$ such that

$$
b^{m} \cdot f = q \cdot g + r, \quad \text{with } \deg(r) < \deg(g) \ \text{and}\ m \leq \max\{0,\ \deg(f) - \deg(g) + 1\}.
$$

***Proof:*** We proceed by strong induction on $$\deg(f)$$. If $$\deg(f) < \deg(g)$$ (in particular, if $$f = 0$$), take $$m = 0$$, $$q = 0$$ and $$r = f$$; then $$b^{0} f = 0 \cdot g + f$$, $$\deg(r) = \deg(f) < \deg(g)$$ and $$m = 0 \leq \max\{0, \deg(f) - \deg(g) + 1\}$$.

Suppose now that $$\deg(f) \geq \deg(g)$$, and that the result holds for every polynomial of degree smaller than $$\deg(f)$$. Let $$a$$ be the leading coefficient of $$f$$, $$n = \deg(f)$$ and $$k = \deg(g)$$, so that $$n \geq k$$. Define

$$
h := b \cdot f - a \cdot x^{\,n-k} \cdot g.
$$

Then $$\deg(h) < \deg(f)$$: indeed, both $$b \cdot f$$ and $$a \cdot x^{\,n-k} \cdot g$$ have degree at most $$n$$, and their coefficients of degree $$n$$ are $$b \cdot a$$ and $$a \cdot b$$ respectively, which coincide because $$R$$ is commutative; on subtracting, the term of degree $$n$$ cancels. By the inductive hypothesis applied to $$h$$, there exist $$m_{1} \geq 0$$ and $$q_{1}, r_{1} \in R[x]$$ such that

$$
b^{m_{1}} \cdot h = q_{1} \cdot g + r_{1}, \qquad \deg(r_{1}) < \deg(g), \qquad m_{1} \leq \max\{0,\ \deg(h) - \deg(g) + 1\}.
$$

Thus, substituting the definition of $$h$$, we have that

$$
\begin{aligned}
q_{1} \cdot g + r_{1} = b^{m_{1}} \cdot h &= b^{m_{1}} \big( b \cdot f - a \cdot x^{\,n-k} \cdot g \big) \\
&= b^{m_{1} + 1} \cdot f - b^{m_{1}} \cdot a \cdot x^{\,n-k} \cdot g,
\end{aligned}
$$

and rearranging we obtain

$$
b^{m_{1} + 1} \cdot f = \big( q_{1} + b^{m_{1}} \cdot a \cdot x^{\,n-k} \big) \cdot g + r_{1}.
$$

Taking $$m = m_{1} + 1$$, $$q = q_{1} + b^{m_{1}} \cdot a \cdot x^{\,n-k}$$ and $$r = r_{1}$$, the identity holds with $$\deg(r) < \deg(g)$$. Finally, since $$\deg(h) \leq n - 1$$, we have that

$$
m = m_{1} + 1 \leq \max\{0,\ (n - 1) - k + 1\} + 1 \leq (n - k) + 1 = \max\{0,\ \deg(f) - \deg(g) + 1\},
$$

where the last equality uses that $$n \geq k$$. This completes the inductive step and the proof.

### Definition (Root of a polynomial)

Let $$p(x) \in R[x]$$. We say that $$\alpha \in R$$ is a *root* of $$p$$ if $$\tilde{p}(\alpha) = 0$$.

### Theorem (Factorisation of a root of a polynomial)

Let $$R$$ be a commutative ring and $$p(x) \in R[x]$$. Then $$\alpha$$ is a root of $$p(x)$$ if and only if there exists $$t \in R[x]$$ such that $$p = (x - \alpha) \cdot t$$.

***Proof:*** Exercise.

### Theorem (Division algorithm for fields)

Let $$F$$ be a field. Let $$f, g \in F[x]$$ be such that $$g \neq 0$$. Then there exist unique $$q, r \in F[x]$$ such that

$$
f = q \cdot g + r, \quad \text{with } \deg(r) < \deg(g).
$$

***Proof:*** For existence we apply the division algorithm for rings: if $$b$$ is the leading coefficient of $$g$$, there exist $$m \geq 0$$ and $$q_{0}, r_{0} \in F[x]$$ such that $$b^{m} f = q_{0} g + r_{0}$$ with $$\deg(r_{0}) < \deg(g)$$. Since $$g \neq 0$$, we have that $$b \neq 0$$, and hence $$b$$ is a unit of $$F$$; in particular $$b^{m}$$ is invertible. Multiplying by $$b^{-m}$$ we obtain

$$
f = \big( b^{-m} q_{0} \big) g + b^{-m} r_{0},
$$

and it suffices to take $$q = b^{-m} q_{0}$$ and $$r = b^{-m} r_{0}$$. Note that $$\deg(r) = \deg(r_{0}) < \deg(g)$$, since multiplying by the non-zero constant $$b^{-m}$$ does not alter the degree (in a field there are no zero divisors). Uniqueness is left as an exercise.

### Theorem (Polynomials over an integral domain)

Let $$A$$ be an integral domain. Then:

1. $$A[x]$$ is an integral domain and $$(A[x])^{\times} = A^{\times}$$;
2. if $$p \in A[x]$$, $$p \neq 0$$ and $$\deg(p) = n$$, then $$p$$ has at most $$n$$ distinct roots.

***Proof:*** *Part 1.* Suppose there exist $$p, q \in A[x]$$, with $$p \neq 0$$ and $$q \neq 0$$, such that $$p \cdot q = 0$$. Then $$\deg(p \cdot q) = -\infty$$. But the leading coefficients of $$p$$ and $$q$$ are non-zero, and in an integral domain the non-zero elements are not zero divisors; hence, by the properties of the degree,

$$
\deg(p \cdot q) = \deg(p) + \deg(q) \in \mathbb{N},
$$

a contradiction. We conclude that $$A[x]$$ is an integral domain.

For the units, note first that $$A^{\times} \subseteq (A[x])^{\times}$$, since the equality $$a \cdot a^{-1} = 1$$ in $$A$$ also holds in $$A[x]$$ upon identifying the constants. Conversely, let $$p \in (A[x])^{\times}$$. Then there exists $$q \in A[x]$$ such that $$p \cdot q = 1$$; in particular $$p \neq 0$$ and $$q \neq 0$$. Thus,

$$
\deg(p \cdot q) = \underbrace{\deg(p) + \deg(q)}_{\in\, \mathbb{N}} = \deg(1) = 0,
$$

from which $$\deg(p) = \deg(q) = 0$$, and hence $$p$$ and $$q$$ are constants, that is, $$p, q \in A$$ with $$p \cdot q = 1$$. We conclude that $$p \in A^{\times}$$, and therefore $$(A[x])^{\times} = A^{\times}$$.

*Part 2.* We proceed by induction on $$n = \deg(p)$$. If $$n = 0$$, then $$p = a_{0} \neq 0$$ is constant, so $$\tilde{p}(\alpha) = a_{0} \neq 0$$ for every $$\alpha \in A$$, and $$p$$ has $$0 \leq 0$$ roots. Suppose now that the result holds for non-zero polynomials of degree $$n - 1$$, and let $$p$$ have degree $$n \geq 1$$. If $$p$$ has no roots, there is nothing to prove. If $$\alpha$$ is a root of $$p$$, by the theorem on the factorisation of a root there exists $$t \in A[x]$$ such that $$p = (x - \alpha) \cdot t$$; note that $$t \neq 0$$, since $$p \neq 0$$. As the leading coefficient of $$x - \alpha$$ is $$1$$, which is not a zero divisor, the properties of the degree give $$n = \deg(p) = 1 + \deg(t)$$, that is, $$\deg(t) = n - 1$$. Now, if $$\beta \neq \alpha$$ is another root of $$p$$, evaluating at $$\beta$$ we have that

$$
0 = \tilde{p}(\beta) = (\beta - \alpha) \cdot \tilde{t}(\beta),
$$

where we use that the associated function of a product is the product of the associated functions when the ring is commutative (a direct verification with the formula $$c_{k} = \sum_{i} a_{i} b_{k-i}$$). Since $$\beta - \alpha \neq 0$$ and $$A$$ is an integral domain, necessarily $$\tilde{t}(\beta) = 0$$, that is, every root of $$p$$ other than $$\alpha$$ is a root of $$t$$. By the inductive hypothesis, $$t$$ has at most $$n - 1$$ distinct roots, and hence $$p$$ has at most $$1 + (n - 1) = n$$ distinct roots.
{% endraw %}
