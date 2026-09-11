---
layout: chapter
course: ma0561
chapter: 22
title: "Prime Subrings and Characteristic"
slug: 22-prime-subrings-and-characteristic
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/22-prime-subrings-and-characteristic/
---

{% raw %}
## The prime subring and the prime field

### Definition (Prime field)

Let $$F$$ be a field. We define the *prime field* of $$F$$ as the intersection of all subfields of $$F$$.

### Definition (Prime subring)

Let $$R$$ be a ring. The *prime subring* (or *prime ring*) of $$R$$ is the intersection of all subrings of $$R$$; that is, the smallest subring of $$R$$.

### Note (The prime ring of a field lives inside its prime field)

If $$(F, +, \cdot)$$ is a field, then it is a ring; since every subfield of $$F$$ is in particular a subring, the prime ring of $$F$$ is a subring of the prime field of $$F$$.

### Example (Well-known prime subrings)

The following examples illustrate the definition:

1. $$\mathbb{Z}$$ is the prime subring of $$\mathbb{Z}$$, and $$\mathbb{Z}_{n}$$ is the prime subring of $$\mathbb{Z}_{n}$$.
2. Let $$R$$ be a ring and consider $$M_{n \times n}(R)$$. Then $$\{ z \cdot I_{n} :\ z \in \mathbb{Z} \}$$ is the prime ring of $$M_{n \times n}(R)$$.
3. If $$R_{1} \subseteq R_{2}$$ are rings (respectively, fields), then $$R_{1}$$ and $$R_{2}$$ have the same prime ring (respectively, prime field).

### Note (The chain of number rings)

Note that $$\mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C} \subseteq \mathbb{H}$$ (as rings):

- they all have the same prime ring, $$\mathbb{Z}$$;
- $$\mathbb{Q}$$ is the prime field of $$\mathbb{Q}$$, $$\mathbb{R}$$ and $$\mathbb{C}$$.

## The characteristic

### Definition (Characteristic of a ring)

If $$R$$ is a ring and $$R_{0}$$ is its prime ring, we define

$$
\operatorname{char}(R) =
\begin{cases}
|R_{0}| & \text{if } R_{0} \text{ is finite}, \\
0 & \text{otherwise}.
\end{cases}
$$

### Theorem (The prime subring is $$\mathbb{Z}$$ or $$\mathbb{Z}_{n}$$)

Let $$R$$ be a ring.

1. The prime subring $$R_{0}$$ of $$R$$ is isomorphic to $$\mathbb{Z}$$ or to $$\mathbb{Z}_{n}$$, and in that case

    $$
    \operatorname{char}(R) =
    \begin{cases}
    n & \text{if } R_{0} \cong \mathbb{Z}_{n}, \\
    0 & \text{if } R_{0} \cong \mathbb{Z}.
    \end{cases}
    $$
2. If $$D$$ is an integral domain, then $$\operatorname{char}(D)$$ is $$0$$ or a prime number $$p$$.

***Proof:*** *Part 1.* Let $$R_{0}$$ be the prime ring of $$R$$ and let $$f_{R} : \mathbb{Z} \longrightarrow R$$ be such that $$n \longmapsto n \cdot 1_{R}$$, which is a ring homomorphism (in fact, the only one; see the exercise on homomorphisms from $$\mathbb{Z}$$). We claim that $$\operatorname{Im}(f_{R}) = R_{0}$$: on the one hand, $$\operatorname{Im}(f_{R})$$ is a subring of $$R$$; on the other, every subring $$S$$ of $$R$$ contains $$1_{R}$$ and is closed under sums and differences, so it contains $$n \cdot 1_{R}$$ for every $$n \in \mathbb{Z}$$, that is, $$\operatorname{Im}(f_{R}) \subseteq S$$. Then $$\operatorname{Im}(f_{R})$$ is the smallest subring of $$R$$, that is, $$\operatorname{Im}(f_{R}) = R_{0}$$. By the first isomorphism theorem,

$$
R_{0} = \operatorname{Im}(f_{R}) \cong \mathbb{Z}/\operatorname{Ker}(f_{R}).
$$

Note that $$\operatorname{Ker}(f_{R})$$ is an ideal of $$\mathbb{Z}$$, and since $$\mathbb{Z}$$ is a PID, we have that $$\operatorname{Ker}(f_{R}) = (n)$$ with $$n \in \mathbb{N}$$. If $$n = 0$$, then $$\operatorname{Ker}(f_{R}) = \{0\}$$, so that $$R_{0} \cong \mathbb{Z}$$, which is infinite, and $$\operatorname{char}(R) = 0$$. If $$n \neq 0$$, then $$R_{0} \cong \mathbb{Z}/(n) \cong \mathbb{Z}_{n}$$, which has $$n$$ elements, and $$\operatorname{char}(R) = n$$.

*Part 2.* It was proved in the homework; it is left as an exercise.

## The Frobenius homomorphism and Fermat's little theorem

### Theorem (Frobenius: raising to the $$p$$-th power is a homomorphism)

Let $$R$$ be a commutative ring such that $$\operatorname{char}(R) = p > 0$$ with $$p$$ prime. Then $$\varphi : R \to R$$ such that $$x \mapsto x^{p}$$ is a homomorphism. In particular,

$$
(x + y)^{p} = x^{p} + y^{p} \quad \text{for all } x, y \in R.
$$

***Proof:*** Note first that $$\varphi(1) = 1^{p} = 1$$, and that, since $$R$$ is commutative,

$$
\varphi(x \cdot y) = (x y)^{p} = x^{p} y^{p} = \varphi(x) \cdot \varphi(y).
$$

It remains to prove that $$\varphi(x + y) = \varphi(x) + \varphi(y)$$, that is, that $$(x + y)^{p} = x^{p} + y^{p}$$.

Let $$a, b \in R$$. By Newton's binomial theorem, valid in commutative rings,

$$
(a + b)^{p} = \sum_{i=0}^{p} \binom{p}{i} a^{i} b^{p-i},
$$

where $$\binom{p}{i} a^{i} b^{p-i}$$ denotes the corresponding integer multiple. We claim that if $$0 < i < p$$, then $$\binom{p}{i}$$ is a multiple of $$p$$: from the identity

$$
i!\,(p - i)!\, \binom{p}{i} = p!
$$

we see that $$p$$ divides the right-hand side; but $$p$$ is prime and divides neither $$i!$$ nor $$(p-i)!$$, since all their factors are smaller than $$p$$; hence $$p \mid \binom{p}{i}$$. Now, since $$\operatorname{char}(R) = p$$, we have that $$p \cdot 1_{R} = 0$$, and if $$\binom{p}{i} = p \cdot t$$ with $$t \in \mathbb{Z}$$, then

$$
\binom{p}{i} \cdot a^{i} b^{p-i} = \big( \binom{p}{i} \cdot 1_{R} \big)\, a^{i} b^{p-i} = \big( t \cdot (p \cdot 1_{R}) \big)\, a^{i} b^{p-i} = 0.
$$

That is, in the binomial sum only the terms $$i = 0$$ and $$i = p$$ survive, so that $$(a + b)^{p} = a^{p} + b^{p}$$.

### Note (Frobenius on finite fields and its iterates)

Three remarks on the previous homomorphism:

1. $$\varphi$$ is called the *Frobenius homomorphism*.
2. If $$R$$ is a finite field, then $$\operatorname{Ker}(\varphi) = \{0\}$$ (the kernel is a proper ideal of a field), so that $$\varphi$$ is injective. Since $$R$$ is finite, $$\varphi$$ is also surjective, and hence $$\varphi$$ is an automorphism.
3. $$\varphi^{n} : R \to R$$, $$x \mapsto x^{p^{n}}$$, is a homomorphism for every $$n \in \mathbb{N}$$, being a composition of homomorphisms. In particular,

    $$
    (a + b)^{p^{n}} = a^{p^{n}} + b^{p^{n}} \quad \text{for all } a, b \in R,\ n \in \mathbb{N}.
    $$

### Theorem (Fermat's little theorem)

Let $$p$$ be prime. Then $$n^{p} \equiv n \pmod{p}$$ for every $$n > 0$$.

***Proof:*** We proceed by induction on $$n$$. The base case $$n = 1$$ is trivial, since $$1^{p} = 1$$. Now, suppose as inductive hypothesis that $$n^{p} \equiv n \pmod{p}$$ for some $$n \in \mathbb{N}$$. The ring $$\mathbb{Z}_{p}$$ is its own prime ring, so $$\operatorname{char}(\mathbb{Z}_{p}) = p$$. Using the Frobenius homomorphism on $$\mathbb{Z}_{p}$$ and the inductive hypothesis, we have that

$$
(n + 1)^{p} = n^{p} + 1^{p} = n + 1 \pmod{p},
$$

which proves the inductive step. Conclude the result.
{% endraw %}
