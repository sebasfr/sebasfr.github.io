---
layout: chapter
course: ma0561
chapter: 15
title: "Rings"
slug: 15-rings
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/15-rings/
---

{% raw %}
## The definition of a ring and first properties

### Definition (Ring and commutative ring)

A *ring* is a set $$R$$ together with two binary operations $$+, \cdot$$ such that:

1. $$(R, +)$$ is an abelian group;
2. the operation $$\cdot$$ is associative and has an identity element;
3. if $$a, b, c \in R$$, then $$a \cdot (b + c) = a \cdot b + a \cdot c$$ and $$(a + b) \cdot c = a \cdot c + b \cdot c$$.

If moreover $$(R, +, \cdot)$$ satisfies that for all $$a, b \in R$$, $$a \cdot b = b \cdot a$$, then $$R$$ is a *commutative ring*.

### Note (We do not assume that $$1 \neq 0$$)

If $$0$$ is the identity element of $$+$$ and $$1$$ is the identity element of $$\cdot$$, we are not assuming that $$1 \neq 0$$.

### Proposition (Basic arithmetic rules in a ring)

Let $$(R, +, \cdot)$$ be a ring. Then:

1. for every $$a \in R$$, $$a \cdot 0 = 0 \cdot a = 0$$;
2. for all $$a, b \in R$$, $$(-a) \cdot b = -(a \cdot b) = a \cdot (-b)$$;
3. for all $$a, b \in R$$, $$(-a) \cdot (-b) = a \cdot b$$;
4. the identity element of $$\cdot$$ is unique and $$(-1) \cdot a = -a$$.

***Proof:*** Exercise.

### Note (The trivial ring)

If $$0 = 1$$, then

$$
a = a \cdot 1 = a \cdot 0 = 0
$$

for every $$a \in R$$, whence $$R = \{0\}$$ and the ring is the trivial ring with a single element.

### Example (First examples of rings)

The following are basic examples:

1. $$(\mathbb{Z}, +, \cdot)$$ is a commutative ring.
2. Let $$n > 1$$ and let $$R$$ be a ring. Then $$M_{n}(R)$$ is a ring with the matrix operations $$+, \cdot$$. It is not a commutative ring.
3. $$(\mathbb{R}, +, \cdot)$$, $$(\mathbb{Q}, +, \cdot)$$ and $$(\mathbb{C}, +, \cdot)$$ are commutative rings.

## Fields and subrings

### Definition (Field)

A *field* $$(F, +, \cdot)$$ is a commutative ring such that $$1 \neq 0$$ and for every $$a \in F$$,

$$
a \neq 0 \implies \exists b \in F\ (a \cdot b = 1).
$$

### Exercise (The usual number rings are fields)

Show that $$(\mathbb{R}, +, \cdot)$$, $$(\mathbb{Q}, +, \cdot)$$ and $$(\mathbb{C}, +, \cdot)$$ are fields.

### Definition (Subring)

Let $$(R, +, \cdot)$$ be a ring and $$S \subseteq R$$. We say that $$S$$ is a *subring* of $$R$$ if $$(S, +\mid_{S \times S}, \cdot\mid_{S \times S})$$ is a ring.

### Note (Subring criterion)

$$S \subseteq R$$ is a subring if and only if $$1 \in S$$ and for all $$a, b \in S$$ we have that $$a - b \in S$$ and $$a \cdot b \in S$$. (Exercise.)

## Units, zero divisors and integral domains

### Definition (Units and the group of units)

Let $$(R, +, \cdot)$$ be a ring. An element $$a \in R$$ is a *unit* if there exists $$b \in R$$ such that

$$
a \cdot b = 1 = b \cdot a.
$$

If $$a$$ is a unit, then $$b$$ is unique; in this case we write $$b = a^{-1}$$. Moreover, we define the set

$$
U_{R} = \{ a \in R :\ a \text{ is a unit} \}.
$$

Sometimes one writes $$U_{R} = R^{\times}$$.

### Note (The units form a group)

$$(U_{R}, \cdot)$$ is a group.

### Note (The units of a field)

If $$(F, +, \cdot)$$ is a field, then $$U_{F} = F \setminus \{0\}$$.

### Definition (Zero divisors, division rings and integral domains)

Let $$(R, +, \cdot)$$ be a ring.

1. $$a \in R$$ is a *zero divisor* if $$a \neq 0$$ and there exists $$b \in R$$ such that $$b \neq 0$$ and $$a \cdot b = 0$$ or $$b \cdot a = 0$$.
2. A ring without zero divisors is called a *division ring*.
3. A commutative ring without zero divisors is called an *integral domain*.

### Note (Units are not zero divisors)

Every field is an integral domain. More generally, if $$a \in R$$ is a unit, then $$a$$ is not a zero divisor.

### Lemma (Subrings of a field are integral domains)

Let $$(F, +, \cdot)$$ be a field and $$R \subseteq F$$ a subring. Then $$R$$ is an integral domain.

***Proof:*** First, $$R$$ is commutative, since the operation $$\cdot$$ of $$R$$ is the restriction of that of $$F$$, which is commutative. Now, suppose that there exists a zero divisor $$a \in R$$. Then $$a \neq 0$$ and there exists $$b \in R$$ with $$b \neq 0$$ such that $$a \cdot b = 0$$ or $$b \cdot a = 0$$. Since $$R \subseteq F$$, we have that $$a, b \in F$$, and so $$a$$ is a zero divisor in $$F$$. But $$F$$ is a field and therefore an integral domain, so $$F$$ has no zero divisors, a contradiction. We conclude that $$R$$ has no zero divisors, that is, $$R$$ is an integral domain.

### Proposition (Cancellation law)

Let $$(R, +, \cdot)$$ be a ring and $$a \in R$$ such that $$a \neq 0$$ and $$a$$ is not a zero divisor. If $$a \cdot x = a \cdot y$$, then $$x = y$$.

***Proof:*** Suppose that $$ax = ay$$. Then, subtracting and using distributivity,

$$
ax = ay \implies ax - ay = 0 \implies a(x - y) = 0.
$$

If we had $$x - y \neq 0$$, the equality $$a(x - y) = 0$$ would exhibit $$a$$ as a zero divisor, since $$a \neq 0$$. As $$a$$ is not a zero divisor, necessarily $$x - y = 0$$, that is, $$x = y$$.

### Lemma (Every finite integral domain is a field)

Let $$R \neq \{0\}$$ be a finite integral domain. Then $$R$$ is a field.

***Proof:*** Note first that, since $$R \neq \{0\}$$, we have that $$1 \neq 0$$. Let $$a \in R$$ with $$a \neq 0$$, and consider the function $$\mu : R \to R$$ given by $$\mu(x) = a \cdot x$$. Note that $$\mu$$ is injective: if $$\mu(x) = \mu(y)$$, then $$a \cdot x = a \cdot y$$, and since $$a \neq 0$$ is not a zero divisor (as $$R$$ is an integral domain), the cancellation law implies that $$x = y$$. Moreover, since $$R$$ is finite and $$\mu : R \to R$$ is injective, $$\mu$$ is surjective. In particular, there exists $$b \in R$$ such that

$$
\mu(b) = a \cdot b = 1.
$$

Note that $$b \neq 0$$, since if $$b = 0$$ we would have $$1 = a \cdot 0 = 0$$, and we know that $$0 \neq 1$$ in $$R$$. We conclude that $$a$$ is invertible and, since $$a \neq 0$$ was arbitrary and $$R$$ is commutative with $$1 \neq 0$$, $$R$$ is a field.

### Example (The integers and the integers modulo $$n$$)

The following examples will recur:

1. $$(\mathbb{Z}, +, \cdot)$$ is a ring, $$\mathbb{Z}^{\times} = \{1, -1\}$$ and $$\mathbb{Z}$$ is an integral domain.
2. $$(\mathbb{Z}_{n}, +, \cdot)$$, with $$n > 1$$, is a ring. It is a field if and only if $$n$$ is prime, and

    $$
    \mathbb{Z}_{n}^{\times} = \{ [k] \in \mathbb{Z}_{n} :\ \operatorname{gcd}(k, n) = 1 \ \text{and}\ 0 \leq k \leq n - 1 \}.
    $$

    If $$[x] \in \mathbb{Z}_{n}$$, there are exactly two possibilities: $$[x] \in \mathbb{Z}_{n}^{\times}$$ or $$[x]$$ is a zero divisor (exercise).

### Example (The endomorphism ring of an abelian group)

Let $$G$$ be an abelian group and let

$$
\operatorname{End}(G) := \{ f : G \to G\ \text{homomorphism} \}.
$$

Define $$+, \cdot$$ on $$\operatorname{End}(G)$$ as follows: if $$f, g \in \operatorname{End}(G)$$, then $$f + g : G \to G$$ is such that $$(f + g)(x) = f(x) + g(x)$$, and $$f \cdot g : G \to G$$ is such that $$(f \cdot g)(x) = f(g(x))$$. **Exercise:** $$\operatorname{End}(G)$$ is a non-commutative ring.

### Example (The ring of functions with values in a ring)

Let $$R \neq \{0\}$$ be a ring and $$X$$ a non-empty set. Define

$$
\mathcal{F}(X, R) := \{ f : X \to R\ \text{functions} \},
$$

with the operations $$+, \cdot$$ given pointwise: if $$f, g \in \mathcal{F}(X, R)$$, then

$$
f + g : X \to R, \quad x \mapsto f(x) +_{R} g(x), \qquad f \cdot g : X \to R, \quad x \mapsto f(x) \cdot_{R} g(x).
$$

**Exercise:** $$\mathcal{F}(X, R)$$ is a ring, and it is commutative if and only if $$R$$ is commutative.

### Example (The Gaussian integers)

Let $$\mathbb{Z}[i] := \{ a + bi :\ a, b \in \mathbb{Z} \} \subseteq \mathbb{C}$$. This set is called the set of *Gaussian integers*. Since $$\mathbb{Z}[i]$$ is a subring of the field $$\mathbb{C}$$, we can see that it is an integral domain.
{% endraw %}
