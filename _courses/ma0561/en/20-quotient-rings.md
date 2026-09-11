---
layout: chapter
course: ma0561
chapter: 20
title: "Quotient Rings"
slug: 20-quotient-rings
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/20-quotient-rings/
---

{% raw %}
## Congruence modulo an ideal and the quotient

### Definition (The congruence relation modulo an ideal)

Let $$R$$ be a ring and $$I$$ an $$R$$-ideal. For $$a, b \in R$$, define the relation $$\sim_{I}$$ such that

$$
a \sim_{I} b \iff a - b \in I.
$$

### Lemma (Congruence modulo an ideal is an equivalence relation)

The relation $$\sim_{I}$$ is an equivalence relation on $$R$$.

***Proof:*** We verify the three properties:

1. *Reflexivity:* $$a \sim_{I} a$$, since $$a - a = 0 \in I$$.
2. *Symmetry:* if $$a \sim_{I} b$$, then $$a - b \in I$$; since $$I$$ is closed under additive inverses, $$b - a = -(a - b) \in I$$, that is, $$b \sim_{I} a$$.
3. *Transitivity:* if $$a \sim_{I} b$$ and $$b \sim_{I} c$$, then $$a - b \in I$$ and $$b - c \in I$$. Since $$I$$ is closed under sums,

    $$
    a - c = (a - b) + (b - c) \in I,
    $$

    that is, $$a \sim_{I} c$$.

### Note (The equivalence classes are cosets)

Let $$R/I = \{ [a]_{I} :\ a \in R \}$$ be the set of equivalence classes of $$\sim_{I}$$. Then

$$
\begin{aligned}
[a]_{I} &= \{ b \in R :\ a \sim_{I} b \} = \{ b \in R :\ a - b \in I \} \\
&= \{ b \in R :\ \exists x \in I\ (x = a - b) \} = \{ b \in R :\ \exists x \in I\ (b = a - x) \} \\
&= \{ a - x :\ x \in I \} = a + I,
\end{aligned}
$$

where the last equality uses that $$I$$ is closed under additive inverses, so that $$\{-x : x \in I\} = I$$. **Notation:** $$[a]_{I} = a + I$$.

### Definition (The operations of the quotient ring)

We define $$\tilde{+}$$ on $$R/I$$ such that

$$
(a + I)\ \tilde{+}\ (b + I) = (a + b) + I.
$$

The ideal $$I$$ is the “$$0$$” of $$R/I$$ (that is, $$[0]_{I}$$). We define $$\tilde{\cdot}$$ on $$R/I$$ such that

$$
(a + I)\ \tilde{\cdot}\ (b + I) = (a \cdot b) + I.
$$

The class $$1_{R} + I$$ is the “$$1$$” of $$R/I$$.

### Theorem (The quotient is a ring)

$$R/I$$ is a ring under these operations. It is called the *quotient ring* of $$R$$ by $$I$$.

***Proof:*** The delicate part is to verify that $$\tilde{+}$$ and $$\tilde{\cdot}$$ are well defined, that is, that they do not depend on the representatives. Suppose that $$a + I = a' + I$$ and $$b + I = b' + I$$, that is, $$a - a' \in I$$ and $$b - b' \in I$$. For the sum,

$$
(a + b) - (a' + b') = (a - a') + (b - b') \in I,
$$

so that $$(a + b) + I = (a' + b') + I$$. For the product, we add and subtract $$a' b$$:

$$
a b - a' b' = (a - a') b + a' (b - b'),
$$

and here $$(a - a') b \in I$$ by absorption on the right and $$a' (b - b') \in I$$ by absorption on the left; hence $$a b - a' b' \in I$$, that is, $$(a b) + I = (a' b') + I$$. This is where it is essential that $$I$$ is a two-sided ideal.

The ring axioms are inherited from $$R$$ by operating with representatives; for example,

$$
\big( (a + I)\, \tilde{\cdot}\, (b + I) \big)\, \tilde{\cdot}\, (c + I) = (a b) c + I = a (b c) + I = (a + I)\, \tilde{\cdot}\, \big( (b + I)\, \tilde{\cdot}\, (c + I) \big),
$$

and likewise the associativity and commutativity of $$\tilde{+}$$, distributivity, the identity elements $$I = 0 + I$$ and $$1 + I$$, and the additive inverse $$(-a) + I$$.

### Definition (The canonical projection)

If $$R$$ is a ring and $$I$$ is an $$R$$-ideal, let $$\pi_{I} : R \to R/I$$ be such that $$a \mapsto a + I$$, the *canonical projection* of $$R$$ onto $$R/I$$.

### Proposition (Properties of the canonical projection)

The canonical projection $$\pi_{I}$$ is surjective and $$\operatorname{Ker}(\pi_{I}) = I$$.

***Proof:*** Surjectivity is immediate: every class $$a + I \in R/I$$ is $$\pi_{I}(a)$$. For the kernel, we have the two inclusions:

$$
\text{if } x \in I \implies \pi_{I}(x) = x + I = I = [0]_{I} \implies x \in \operatorname{Ker}(\pi_{I}),
$$

since $$x - 0 = x \in I$$; and conversely,

$$
\text{if } x \in \operatorname{Ker}(\pi_{I}) \implies \pi_{I}(x) = x + I = I \implies x \in I,
$$

since $$x = x - 0 \in I$$. We conclude that $$\operatorname{Ker}(\pi_{I}) = I$$.

## Examples of quotients

### Example (The integers modulo $$n$$ as a quotient)

$$\mathbb{Z}/(n) = \mathbb{Z}_{n}$$.

### Example (The quotient $$\mathbb{Z}[x]/(x^{2})$$)

If $$p(x) + (x^{2}) \in \mathbb{Z}[x]/(x^{2})$$, then there exist unique $$a, b \in \mathbb{Z}$$ such that

$$
[p(x)]_{(x^{2})} = [a + b x]_{(x^{2})}.
$$

For existence, write $$p(x) = a + b x + x^{2} q(x)$$ with $$q(x) \in \mathbb{Z}[x]$$; then $$p(x) - (a + bx) = x^{2} q(x) \in (x^{2})$$. We now prove uniqueness. Let $$a_{0}, a_{1}, b_{0}, b_{1} \in \mathbb{Z}$$ be such that

$$
[a_{0} + a_{1} x]_{(x^{2})} = [b_{0} + b_{1} x]_{(x^{2})}.
$$

Then

$$
(a_{0} - b_{0}) + (a_{1} - b_{1}) x \in (x^{2}).
$$

But every non-zero element of $$(x^{2}) = x^{2} \cdot \mathbb{Z}[x]$$ has degree at least $$2$$, that is, its coefficients of degrees $$0$$ and $$1$$ vanish; hence $$a_{0} = b_{0}$$ and $$a_{1} = b_{1}$$. We conclude that

$$
\mathbb{Z}[x]/(x^{2}) = \{ [a + b x]_{(x^{2})} :\ a, b \in \mathbb{Z} \}.
$$

Note moreover that

$$
[3x]_{(x^{2})} \cdot [5x]_{(x^{2})} = [15 x^{2}]_{(x^{2})} = [0]_{(x^{2})},
$$

so that $$\mathbb{Z}[x]/(x^{2})$$ has zero divisors.

### Exercise (Zero divisors and units of $$\mathbb{Z}[x]/(x^{2})$$)

Show that the zero divisors of $$\mathbb{Z}[x]/(x^{2})$$ are $$\{ [b x] :\ b \neq 0 \}$$ and that the units are $$\{ [\pm 1 + b x] :\ b \in \mathbb{Z} \}$$.

### Example (A quotient of the Gaussian integers)

Let $$\mathbb{Z}[i] = \{ a + b i :\ a, b \in \mathbb{Z} \}$$. Then $$\mathbb{Z}[i]/(1 + i) = \{ [0], [1] \}$$ (exercise).

### Example (The quotient $$\mathbb{R}[x]/(x^{2} + 1)$$)

Let $$R = \mathbb{R}[x]/(x^{2} + 1)$$ and $$\alpha = [x]$$. Then

$$
\alpha^{2} = [x^{2}] = [-1],
$$

since $$x^{2} - (-1) = x^{2} + 1 \in (x^{2} + 1)$$. That is, in $$R$$ the equation “$$t^{2} + 1 = 0$$” has a solution. We shall see that $$R \cong \mathbb{C}$$.

## The correspondence theorem

### Definition (Quotient of a subset)

Let $$R$$ be a ring, $$I$$ an $$R$$-ideal and $$S \subseteq R$$ (merely a subset). We define

$$
S/I := \{ s + I :\ s \in S \} \subseteq R/I.
$$

### Theorem (Correspondence between ideals and subrings of the quotient)

The map $$S \mapsto S/I$$ induces inclusion-preserving bijections between the following sets:

1. $$\{ J :\ J \text{ ideal of } R \text{ such that } J \supseteq I \} \to \{ \text{ideals of } R/I \}$$;
2. $$\{ \text{subrings of } R \text{ that contain } I \} \to \{ \text{subrings of } R/I \}$$.

In both cases the inverse function is $$A \mapsto \{ r \in R :\ r + I \in A \}$$.

***Proof:*** We prove the case of ideals; that of subrings is identical, using the subring criterion instead of the definition of an ideal. Write $$\Phi(J) = J/I$$ and $$\Psi(A) = \{ r \in R :\ r + I \in A \}$$.

*$$\Phi$$ lands where it should.* If $$J \supseteq I$$ is an ideal of $$R$$, then $$J/I$$ is an ideal of $$R/I$$: it is non-empty; it is closed under sums, since $$(j + I) + (j' + I) = (j + j') + I$$ with $$j + j' \in J$$; and it absorbs products, since $$(r + I)(j + I) = r j + I$$ with $$r j \in J$$ by the absorption of $$J$$ in $$R$$.

*$$\Psi$$ lands where it should.* If $$A$$ is an ideal of $$R/I$$, then $$\Psi(A)$$ is an ideal of $$R$$: if $$r, r' \in \Psi(A)$$, then $$(r + r') + I = (r + I) + (r' + I) \in A$$, so $$r + r' \in \Psi(A)$$; and if $$s \in R$$, then $$(s r) + I = (s + I)(r + I) \in A$$ by the absorption of $$A$$. Moreover $$I \subseteq \Psi(A)$$: if $$x \in I$$, then $$x + I = I = [0] \in A$$, since every ideal contains zero.

*They are mutually inverse.* First, $$\Psi(\Phi(J)) = \{ r :\ r + I \in J/I \} = J$$: the inclusion “$$\supseteq$$” is clear, and if $$r + I = j + I$$ for some $$j \in J$$, then $$r - j \in I \subseteq J$$, whence $$r = j + (r - j) \in J$$. Second, $$\Phi(\Psi(A)) = \{ r + I :\ r + I \in A \} = A$$, since every element of $$A$$ is a class $$r + I$$ for some $$r \in R$$.

*They preserve inclusion.* If $$J \subseteq J'$$, then $$J/I \subseteq J'/I$$ directly; and if $$A \subseteq A'$$, then $$\Psi(A) \subseteq \Psi(A')$$ directly. (In the case of subrings, $$\Psi(B) \supseteq I$$ holds because $$[0] \in B$$, and the computation of the inverses uses $$I \subseteq S$$ in the same way.)
{% endraw %}
