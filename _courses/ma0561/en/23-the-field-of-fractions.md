---
layout: chapter
course: ma0561
chapter: 23
title: "The Field of Fractions"
slug: 23-the-field-of-fractions
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/23-the-field-of-fractions/
---

{% raw %}
## The construction

### Definition (The proportionality relation on $$D \times (D \setminus \{0\})$$)

Let $$D$$ be an integral domain and let $$S = D \times (D \setminus \{0\})$$. Define the relation $$\sim$$ on $$S$$ such that

$$
(a, b) \sim (c, d) \iff a \cdot d = b \cdot c.
$$

We use the notation $$\frac{a}{b} := [(a, b)]$$ for the equivalence class of $$(a, b)$$.

### Lemma (The proportionality relation is an equivalence relation)

The relation $$\sim$$ is an equivalence relation on $$S$$.

***Proof:*** Reflexivity and symmetry are immediate from the commutativity of $$D$$: $$a \cdot b = b \cdot a$$ gives $$(a,b) \sim (a,b)$$, and if $$a d = b c$$, then $$c b = d a$$, that is, $$(c, d) \sim (a, b)$$.

For transitivity we use that $$D$$ is an integral domain. Suppose that $$(a, b) \sim (c, d)$$ and $$(c, d) \sim (e, f)$$, that is, $$a d = b c$$ and $$c f = d e$$. Multiplying the first equality by $$f$$ and using the second,

$$
a d f = b c f = b d e,
$$

and rearranging with commutativity, $$d (a f) = d (b e)$$, that is, $$d (a f - b e) = 0$$. Since $$d \neq 0$$ and $$D$$ has no zero divisors, we conclude that $$a f - b e = 0$$, that is, $$a f = b e$$, which is exactly $$(a, b) \sim (e, f)$$.

### Definition (The field of fractions and its operations)

Let $$F := \left\{ \frac{a}{b} :\ (a, b) \in S \right\}$$. Note that if $$x \in D \setminus \{0\}$$, then $$\frac{a}{b} = \frac{a \cdot x}{b \cdot x}$$. Moreover, we can define operations on $$F$$ in the following way:

$$
\frac{a}{b} + \frac{c}{d} = \frac{a d + b c}{b d}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}.
$$

Note that the denominators $$b d$$ are non-zero because $$D$$ is an integral domain, that $$\frac{0}{1}$$ is the identity element for $$+$$ and that $$\frac{1}{1}$$ is the identity element for $$\cdot$$. That these operations are well defined (their independence of the representatives) is verified in the proof of the following theorem.

### Theorem (The field of fractions is a field)

$$(F, +, \cdot, \frac{0}{1}, \frac{1}{1})$$ is a commutative ring and, more interestingly, it is in fact a field.

***Proof:*** *The operations are well defined.* Suppose that $$\frac{a}{b} = \frac{a'}{b'}$$ and $$\frac{c}{d} = \frac{c'}{d'}$$, that is, $$a b' = a' b$$ and $$c d' = c' d$$. For the sum we must show that $$\frac{a d + b c}{b d} = \frac{a' d' + b' c'}{b' d'}$$, that is, that $$(a d + b c) b' d' = (a' d' + b' c') b d$$. Using commutativity and the two relations,

$$
(a d + b c)\, b' d' = (a b')\, d d' + (c d')\, b b' = (a' b)\, d d' + (c' d)\, b b' = (a' d' + b' c')\, b d.
$$

For the product, $$(a c)(b' d') = (a b')(c d') = (a' b)(c' d) = (a' c')(b d)$$, that is, $$\frac{a c}{b d} = \frac{a' c'}{b' d'}$$.

*$$F$$ is a commutative ring.* The denominators $$b d$$ are non-zero, since $$D$$ is an integral domain. Associativity, commutativity of both operations and distributivity are verified with representatives and reduce to the corresponding properties of $$D$$; the additive identity element is $$\frac{0}{1}$$, the additive inverse of $$\frac{a}{b}$$ is $$\frac{-a}{b}$$, and the multiplicative identity element is $$\frac{1}{1}$$.

*$$F$$ is a field.* Note first that $$1 \neq 0$$ in $$D$$ (if $$1 = 0$$, then $$D = \{0\}$$ and there would be no denominators available), and hence $$\frac{1}{1} \neq \frac{0}{1}$$ in $$F$$, since $$1 \cdot 1 \neq 0 \cdot 1$$. Now let $$\frac{a}{b} \neq \frac{0}{1}$$; this means that $$a \cdot 1 \neq b \cdot 0$$, that is, $$a \neq 0$$. Then $$\frac{b}{a} \in F$$ (the denominator $$a$$ is non-zero) and

$$
\frac{a}{b} \cdot \frac{b}{a} = \frac{a b}{b a} = \frac{1}{1},
$$

since $$(a b) \cdot 1 = (b a) \cdot 1$$. That is, every non-zero element of $$F$$ is invertible, and $$F$$ is a field.

### Note (Examples of fields of fractions)

We write $$F = \operatorname{Frac}(D)$$ for the *field of fractions* of $$D$$.

- $$\operatorname{Frac}(\mathbb{Z}) \cong \mathbb{Q}$$.
- If $$D$$ is a field, then $$\operatorname{Frac}(D) \cong D$$.
- If $$D = \Bbbk[x_{1}, \dots, x_{n}]$$ with $$\Bbbk$$ a field, then

    $$
    \operatorname{Frac}(D) = \Bbbk(x_{1}, \dots, x_{n}) = \left\{ \frac{p(x_{1}, \dots, x_{n})}{q(x_{1}, \dots, x_{n})} :\ q \neq 0 \right\},
    $$

    the field of rational functions in $$n$$ variables.

### Note (The domain embeds in its field of fractions)

We may assume that $$D \subseteq \operatorname{Frac}(D)$$, since $$i : D \to \operatorname{Frac}(D)$$, $$x \mapsto \frac{x}{1}$$, is an injective homomorphism, so that $$D$$ “embeds” in $$\operatorname{Frac}(D)$$; that is,

$$
D \cong \operatorname{Im}(i) = \left\{ \frac{x}{1} :\ x \in D \right\} \subseteq \operatorname{Frac}(D).
$$

## The universal property

### Theorem (Universal property of the field of fractions)

Let $$D$$ be an integral domain, $$K$$ a field and $$f : D \to K$$ an injective homomorphism. Then there exists a unique injective homomorphism $$\tilde{f} : \operatorname{Frac}(D) \to K$$ such that

$$
\tilde{f}\left( \frac{x}{1} \right) = f(x) \quad \text{for all } x \in D.
$$

Explicitly,

$$
\tilde{f}\left( \frac{a}{b} \right) = \frac{f(a)}{f(b)} := f(a) \cdot f(b)^{-1} \quad \text{for all } a, b \in D,\ b \neq 0.
$$

***Proof:*** *$$\tilde{f}$$ is well defined.* If $$\frac{a}{b} = \frac{c}{d}$$, then $$a d = b c$$, and applying $$f$$ we obtain $$f(a) \cdot f(d) = f(b) \cdot f(c)$$. Note that $$f(b) \neq 0$$ and $$f(d) \neq 0$$, since $$b, d \neq 0$$ and $$f$$ is injective (its kernel is trivial). Then, rearranging in the field $$K$$, we have that

$$
\frac{f(a)}{f(b)} = \frac{f(c)}{f(d)} \in K \implies \tilde{f}\left( \frac{a}{b} \right) = \tilde{f}\left( \frac{c}{d} \right).
$$

Proving that $$\tilde{f}$$ is an injective homomorphism is left as an exercise.

*Uniqueness.* Suppose that $$h : \operatorname{Frac}(D) \to K$$ is a homomorphism such that $$h\left( \frac{x}{1} \right) = f(x)$$ for all $$x \in D$$. Let $$b \neq 0$$; since $$\frac{b}{1} \cdot \frac{1}{b} = \frac{b}{b} = \frac{1}{1}$$ and homomorphisms preserve units, we have that $$h\left( \frac{1}{b} \right) = h\left( \frac{b}{1} \right)^{-1} = f(b)^{-1}$$. Then

$$
h\left( \frac{a}{b} \right) = h\left( \frac{a}{1} \cdot \frac{1}{b} \right) = h\left( \frac{a}{1} \right) \cdot h\left( \frac{1}{b} \right) = f(a) \cdot f(b)^{-1} = \frac{f(a)}{f(b)} = \tilde{f}\left( \frac{a}{b} \right),
$$

that is, $$h = \tilde{f}$$.

### Theorem (The prime field as the field of fractions of the prime ring)

Let $$\Bbbk$$ be a field.

1. If $$R$$ is the prime subring of $$\Bbbk$$ and $$F$$ is the prime subfield of $$\Bbbk$$, then $$F \cong \operatorname{Frac}(R)$$.
2. The prime subfield of $$\Bbbk$$ is isomorphic to $$\mathbb{Q}$$ or to $$\mathbb{Z}_{p}$$ (also denoted $$\mathbb{F}_{p}$$), according as $$\operatorname{char}(\Bbbk) = 0$$ or $$\operatorname{char}(\Bbbk) = p > 0$$.

***Proof:*** *Part 1.* Since every subfield of $$\Bbbk$$ is in particular a subring, the prime subring $$R$$ is contained in the prime subfield $$F$$, and hence the inclusion $$i : R \to F$$, $$x \mapsto x$$, is an injective homomorphism from $$R$$ into the field $$F$$. Moreover, $$R$$ is an integral domain, being a subring of a field. By the universal property of the field of fractions, there exists an injective homomorphism $$\tilde{\imath} : \operatorname{Frac}(R) \to F$$ with $$\tilde{\imath}\left(\frac{a}{b}\right) = a b^{-1}$$. Let

$$
F_{0} = \operatorname{Im}(\tilde{\imath}) = \{ a b^{-1} :\ a, b \in R,\ b \neq 0 \} \subseteq F.
$$

Since $$\tilde{\imath}$$ is an injective homomorphism from a field, $$F_{0} \cong \operatorname{Frac}(R)$$ and $$F_{0}$$ is a subfield of $$\Bbbk$$: it is a subring (the image of a homomorphism), and the inverse of $$a b^{-1} \neq 0$$ is $$b a^{-1} \in F_{0}$$. By the minimality of the prime subfield, $$F \subseteq F_{0}$$; and we have already seen that $$F_{0} \subseteq F$$. We conclude that

$$
F = F_{0} \cong \operatorname{Frac}(R).
$$

*Part 2.* By the prime subring theorem, $$R \cong \mathbb{Z}$$ or $$R \cong \mathbb{Z}_{n}$$; and since $$\Bbbk$$ is a field, in particular an integral domain, its characteristic is $$0$$ or a prime $$p$$. If $$\operatorname{char}(\Bbbk) = 0$$, then $$R \cong \mathbb{Z}$$ and, by part 1 (an isomorphism of domains extends to the fields of fractions via the universal property),

$$
F \cong \operatorname{Frac}(R) \cong \operatorname{Frac}(\mathbb{Z}) \cong \mathbb{Q}.
$$

If $$\operatorname{char}(\Bbbk) = p$$ is prime, then $$R \cong \mathbb{Z}_{p}$$, which is already a field (since $$p$$ is prime), and the field of fractions of a field is itself:

$$
F \cong \operatorname{Frac}(\mathbb{Z}_{p}) \cong \mathbb{Z}_{p} = \mathbb{F}_{p}.
$$
{% endraw %}
