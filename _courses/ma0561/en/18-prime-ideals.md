---
layout: chapter
course: ma0561
chapter: 18
title: "Prime Ideals"
slug: 18-prime-ideals
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/18-prime-ideals/
---

{% raw %}
## Definition and characterisations

### Definition (Prime ideal)

Let $$R$$ be a ring and $$I$$ an $$R$$-ideal. We say that $$I$$ is *prime* if for all $$x, y \in R$$, if $$x y \in I$$ then $$x \in I$$ or $$y \in I$$.

### Notation (The prime spectrum)

We denote by $$\operatorname{Spec}(R)$$ the set of prime ideals of $$R$$.

### Proposition (Characterisation of primality via products of ideals)

Let $$R$$ be a ring and let $$I$$ be an $$R$$-ideal. The following are equivalent:

1. $$I$$ is prime;
2. for all ideals $$J_{1}, J_{2}$$ of $$R$$: if $$J_{1} J_{2} \subseteq I$$, then $$J_{1} \subseteq I$$ or $$J_{2} \subseteq I$$.

***Proof:*** Exercise.

### Proposition (The zero ideal is prime if and only if the ring is an integral domain)

Let $$R$$ be a commutative ring with $$R \neq \{0\}$$. Then $$R$$ is an integral domain if and only if $$\{0\}$$ is prime.

***Proof:*** “$$\Rightarrow$$”: Let $$x, y \in R$$ be such that $$x \cdot y \in \{0\}$$, that is, $$x \cdot y = 0$$. Since $$R$$ is an integral domain, it has no zero divisors, and hence $$x = 0$$ or $$y = 0$$; that is, $$x \in \{0\}$$ or $$y \in \{0\}$$. We conclude that $$\{0\}$$ is prime.

“$$\Leftarrow$$”: We argue by contraposition. If $$R$$ is not an integral domain, then, since $$R$$ is commutative, the only possibility is that it has zero divisors: there exist $$x, y \in R$$ such that $$x \neq 0$$, $$y \neq 0$$, but $$x \cdot y = 0$$. Then $$x \cdot y \in \{0\}$$, but $$x \notin \{0\}$$ and $$y \notin \{0\}$$, so that $$\{0\}$$ is not prime.

## Maximal ideals, primes and the nilradical

### Proposition (Every maximal ideal is prime)

Let $$R$$ be a commutative ring with $$R \neq \{0\}$$. Then every maximal ideal is prime. In particular, $$\operatorname{Spec}(R) \neq \emptyset$$.

***Proof:*** Let $$\mathfrak{m}$$ be a maximal ideal, and let $$x, y \in R$$ be such that $$x \cdot y \in \mathfrak{m}$$. Suppose, for a contradiction, that $$x \notin \mathfrak{m}$$ and $$y \notin \mathfrak{m}$$. Consider

$$
(x) + \mathfrak{m} = \{ r \cdot x + m :\ r \in R,\ m \in \mathfrak{m} \} \subseteq R,
$$

which is an ideal, being a sum of ideals. Note that $$\mathfrak{m} \subseteq (x) + \mathfrak{m}$$, and the inclusion is strict: $$x = 1 \cdot x + 0 \in (x) + \mathfrak{m}$$, but $$x \notin \mathfrak{m}$$. That is, $$\mathfrak{m} \subsetneq (x) + \mathfrak{m}$$, and analogously $$\mathfrak{m} \subsetneq (y) + \mathfrak{m}$$.

Since $$\mathfrak{m}$$ is maximal and both are ideals properly containing $$\mathfrak{m}$$, we have that

$$
(x) + \mathfrak{m} = R = (y) + \mathfrak{m}.
$$

Since $$1 \in R$$, there exist $$m_{1}, m_{2} \in \mathfrak{m}$$ and $$r_{1}, r_{2} \in R$$ such that

$$
1 = r_{1} x + m_{1}, \qquad 1 = r_{2} y + m_{2}.
$$

Multiplying the two equalities,

$$
1 = (r_{1} x + m_{1})(r_{2} y + m_{2}) = \underbrace{r_{1} r_{2}\, x y}_{\in\, \mathfrak{m}} + \underbrace{r_{1} x\, m_{2}}_{\in\, \mathfrak{m}} + \underbrace{m_{1}\, r_{2} y}_{\in\, \mathfrak{m}} + \underbrace{m_{1} m_{2}}_{\in\, \mathfrak{m}} \in \mathfrak{m},
$$

where the first summand lies in $$\mathfrak{m}$$ because $$x y \in \mathfrak{m}$$ and $$\mathfrak{m}$$ absorbs products, and the remaining ones by direct absorption. Then $$1 \in \mathfrak{m}$$, whence $$\mathfrak{m} = R$$, which contradicts the definition of a maximal ideal. We conclude that $$x \in \mathfrak{m}$$ or $$y \in \mathfrak{m}$$, that is, $$\mathfrak{m}$$ is prime.

Finally, by the corollary to Krull's theorem, $$\operatorname{mSpec}(R) \neq \emptyset$$, and since every maximal ideal is prime, $$\operatorname{Spec}(R) \supseteq \operatorname{mSpec}(R) \neq \emptyset$$.

### Example (Well-known prime spectra)

We compute $$\operatorname{Spec}$$ in the basic examples:

1. Let $$K$$ be a field. Then $$\operatorname{mSpec}(K) = \operatorname{Spec}(K) = \{ \{0\} \}$$.
2. Let $$R = \mathbb{Z}$$. Then

    $$
    \operatorname{mSpec}(\mathbb{Z}) = \{ p\mathbb{Z} :\ p \text{ prime} \}, \qquad \operatorname{Spec}(\mathbb{Z}) = \operatorname{mSpec}(\mathbb{Z}) \cup \{ \{0\} \}.
    $$
3. Let $$R = \mathbb{R}[x]$$. The ideal $$\langle x^{2} - 1 \rangle$$ is not prime:

    $$
    x^{2} - 1 = (x - 1)(x + 1) \in \langle x^{2} - 1 \rangle,
    $$

    but (exercise) $$(x - 1), (x + 1) \notin \langle x^{2} - 1 \rangle$$.

### Theorem (The nilradical is the intersection of the prime ideals)

Let $$R$$ be a commutative ring. Then

$$
\bigcap_{I \text{ prime}} I = \operatorname{Nil}(R) = \{ x \in R :\ \exists n \in \mathbb{N}\ (x^{n} = 0) \}.
$$

***Proof:*** Exercise.
{% endraw %}
