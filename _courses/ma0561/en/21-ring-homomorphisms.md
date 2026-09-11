---
layout: chapter
course: ma0561
chapter: 21
title: "Ring Homomorphisms"
slug: 21-ring-homomorphisms
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/21-ring-homomorphisms/
---

{% raw %}
## Definitions and first examples

### Definition (Ring homomorphism)

Let $$R, S$$ be rings. Then $$\varphi : R \to S$$ is a *ring homomorphism* if:

1. $$\varphi(a +_{R} b) = \varphi(a) +_{S} \varphi(b)$$ for all $$a, b \in R$$;
2. $$\varphi(a \cdot_{R} b) = \varphi(a) \cdot_{S} \varphi(b)$$ for all $$a, b \in R$$;
3. $$\varphi(1_{R}) = 1_{S}$$.

### Note (Homomorphisms preserve zero)

The definition implies that $$\varphi(0_{R}) = 0_{S}$$, since

$$
\varphi(0_{R}) = \varphi(0_{R} + 0_{R}) = \varphi(0_{R}) +_{S} \varphi(0_{R}) \implies 0_{S} = \varphi(0_{R}),
$$

cancelling $$\varphi(0_{R})$$ in the group $$(S, +)$$.

### Definition (Monomorphisms, isomorphisms and automorphisms)

Let $$\varphi : R \to S$$ be a ring homomorphism.

- If $$\varphi$$ is injective, then $$\varphi$$ is a *monomorphism*.
- If $$\varphi$$ is bijective, then $$\varphi$$ is an *isomorphism*.
- If $$\varphi$$ is bijective and $$R = S$$, then $$\varphi$$ is an *automorphism*.

If $$R$$ and $$S$$ are rings such that there exists an isomorphism $$\varphi : R \to S$$, we say that $$R$$ and $$S$$ are *isomorphic* and write $$R \cong S$$.

### Example ($$\mathbb{R}[x]/(x^{2}+1)$$ is isomorphic to $$\mathbb{C}$$)

We have already seen that $$\mathbb{R}[x]/(x^{2} + 1) = \{ [a + b x] :\ a, b \in \mathbb{R} \}$$ (the normal form argument is the same as for $$\mathbb{Z}[x]/(x^{2})$$). The map

$$
\varphi : \mathbb{C} \longrightarrow \mathbb{R}[x]/(x^{2} + 1), \qquad a + i b \longmapsto [a + b x],
$$

is an isomorphism (exercise). In particular, $$\mathbb{R}[x]/(x^{2}+1) \cong \mathbb{C}$$.

### Lemma (Homomorphisms preserve units)

Let $$R, S$$ be rings and $$\varphi : R \to S$$ a homomorphism. If $$a \in R^{\times}$$, then $$\varphi(a) \in S^{\times}$$ and $$\varphi(a^{-1}) = (\varphi(a))^{-1}$$.

***Proof:*** Let $$a \in R^{\times}$$ with inverse $$a^{-1} \in R$$, so that $$a \cdot a^{-1} = 1_{R} = a^{-1} \cdot a$$. Applying $$\varphi$$,

$$
\varphi(a \cdot a^{-1}) = \varphi(1_{R}) \implies \varphi(a) \cdot_{S} \varphi(a^{-1}) = 1_{S} = \varphi(a^{-1}) \cdot_{S} \varphi(a),
$$

where the second equality is obtained by applying $$\varphi$$ to $$a^{-1} \cdot a = 1_{R}$$. Hence $$\varphi(a^{-1})$$ is a multiplicative inverse of $$\varphi(a)$$, that is, $$\varphi(a^{-1}) = (\varphi(a))^{-1}$$ and $$\varphi(a) \in S^{\times}$$.

### Example (The inclusion of a subring and reduction modulo $$n$$)

Two basic examples of homomorphisms:

1. Let $$S$$ be a subring of $$R$$. The map $$\varphi : S \to R$$ such that $$x \mapsto x$$ is a monomorphism.
2. The map $$\varphi : \mathbb{Z} \to \mathbb{Z}_{n}$$ such that $$x \mapsto [x]$$ is a homomorphism.

## Kernel and image

### Definition (Kernel and image of a homomorphism)

Let $$R, S$$ be rings and $$\varphi : R \to S$$ a homomorphism.

1. $$\operatorname{Ker}(\varphi) = \{ x \in R :\ \varphi(x) = 0_{S} \} \subseteq R$$;
2. $$\operatorname{Im}(\varphi) = \{ \varphi(x) :\ x \in R \} = \varphi(R) \subseteq S$$.

### Note (The kernel is an ideal and detects injectivity)

$$\operatorname{Ker}(\varphi)$$ is an $$R$$-ideal. Moreover, $$\operatorname{Ker}(\varphi) = \{0_{R}\}$$ if and only if $$\varphi$$ is injective.

### Note (Composition of homomorphisms)

The composition of homomorphisms is a homomorphism, and the inverse of an isomorphism is an isomorphism. Moreover,

$$
\varphi_{1} \circ (\varphi_{2} \circ \varphi_{3}) = (\varphi_{1} \circ \varphi_{2}) \circ \varphi_{3}.
$$

### Example (Reduction of coefficients modulo $$n$$ and its kernel)

Let $$r_{n} : \mathbb{Z}[x] \longrightarrow \mathbb{Z}_{n}[x]$$ be such that

$$
r_{n}(a_{0} + a_{1} x + \dots + a_{m} x^{m}) = [a_{0}] + [a_{1}] x + \dots + [a_{m}] x^{m}.
$$

The map $$r_{n}$$ is a homomorphism (exercise) and is surjective. Moreover, $$\operatorname{Ker}(r_{n}) = (n\mathbb{Z})[x]$$, since

$$
\begin{aligned}
a_{0} + a_{1} x + \dots + a_{m} x^{m} \in \operatorname{Ker}(r_{n})
&\iff [a_{i}] = [0] \quad \forall i \in \{0, 1, \dots, m\} \\
&\iff n \mid a_{i} \quad \forall i \in \{0, 1, \dots, m\}.
\end{aligned}
$$

### Example (The evaluation homomorphism and its kernel)

Let $$a \in \mathbb{R}$$ and let $$\varphi_{a} : \mathbb{R}[x] \to \mathbb{R}$$ be such that $$\varphi_{a}(p(x)) = p(a)$$. Then $$\varphi_{a}$$ is a homomorphism (exercise). Its kernel is

$$
\begin{aligned}
\operatorname{Ker}(\varphi_{a}) &= \{ p(x) \in \mathbb{R}[x] :\ p(a) = 0 \} \\
&= \{ p(x) \in \mathbb{R}[x] :\ \exists q(x) \in \mathbb{R}[x]\ \big( p(x) = (x - a) \cdot q(x) \big) \} \\
&= \{ (x - a) \cdot q(x) :\ q(x) \in \mathbb{R}[x] \} \\
&= (x - a) \cdot \mathbb{R}[x] \neq \{ 0_{\mathbb{R}[x]} \},
\end{aligned}
$$

where the second equality is the root factorisation theorem.

### Lemma (Properties invariant under isomorphisms)

Let $$R, S$$ be rings and $$\varphi : R \to S$$ an isomorphism. Then:

1. $$R$$ is commutative $$\iff$$ $$S$$ is commutative;
2. $$x \in R^{\times} \iff \varphi(x) \in S^{\times}$$;
3. $$R$$ is a field $$\iff$$ $$S$$ is a field;
4. $$x \in R$$ is a zero divisor $$\iff$$ $$\varphi(x) \in S$$ is a zero divisor.

***Proof:*** Exercise.

### Example ($$\mathbb{R} \times \mathbb{R}$$ is not isomorphic to $$\mathbb{C}$$ as a ring)

Let $$\varphi : \mathbb{R} \times \mathbb{R} \to \mathbb{C}$$ be such that $$(a, b) \mapsto a + i b$$. It is an isomorphism of abelian groups, but not of rings, since $$\mathbb{C}$$ is an integral domain and $$\mathbb{R} \times \mathbb{R}$$ is not (it has zero divisors).

### Example ($$\mathbb{Q}(i)$$ is not isomorphic to $$\mathbb{Q}$$)

Let $$\mathbb{Q}(i) = \{ a + i b :\ a, b \in \mathbb{Q} \}$$. Then $$\mathbb{Q}(i)$$ is a field and $$\mathbb{Q}(i) \not\cong \mathbb{Q}$$. Indeed, there exists $$\alpha \in \mathbb{Q}(i)$$ such that $$\alpha^{2} = -1$$ (namely, $$\alpha = i$$), that is, such that $$\alpha^{2} + 1 = 0$$. If $$f : \mathbb{Q}(i) \to \mathbb{Q}$$ were an isomorphism, we would have that

$$
f(\alpha^{2} + 1) = f(0) = 0 \implies (f(\alpha))^{2} + f(1) = 0 \implies (f(\alpha))^{2} + 1 = 0.
$$

This would imply that in $$\mathbb{Q}$$ the equation $$x^{2} + 1 = 0$$ has a solution, which is impossible, since $$x^{2} \geq 0$$ for every $$x \in \mathbb{Q}$$. We conclude that no such isomorphism exists.

### Example (The only automorphism of $$\mathbb{Z}$$ is the identity)

$$\operatorname{Aut}(\mathbb{Z}) = \{\mathrm{id}_{\mathbb{Z}}\}$$. Indeed, let $$f \in \operatorname{Aut}(\mathbb{Z})$$. Then

$$
\begin{aligned}
f(0) &= 0, \\
f(1) &= 1, \\
f(2) &= f(1) + f(1) = 2, \\
&\ \,\vdots \\
f(n) &= n \quad \text{if } n \in \mathbb{N},
\end{aligned}
$$

where each step uses additivity: $$f(n + 1) = f(n) + f(1)$$. In general, $$f(-n) = -f(n) = -n$$ if $$n > 0$$, since homomorphisms preserve additive inverses. We conclude that $$f = \mathrm{id}_{\mathbb{Z}}$$.

### Example (Conjugation is an automorphism of matrices)

Let $$U \in GL_{n}(\mathbb{R})$$. The map $$\varphi : M_{n \times n}(\mathbb{R}) \longrightarrow M_{n \times n}(\mathbb{R})$$ given by $$A \longmapsto U \cdot A \cdot U^{-1}$$ is an automorphism.

## Extension and contraction of ideals

### Lemma (The inverse image of an ideal is an ideal)

Let $$R, S$$ be rings, $$\varphi : R \to S$$ a homomorphism and $$J \subseteq S$$ an $$S$$-ideal. Then $$\varphi^{-1}(J)$$ is an $$R$$-ideal.

***Proof:*** Exercise.

### Note (The direct image of an ideal is not necessarily an ideal)

If $$I \subseteq R$$ is an $$R$$-ideal, $$\varphi(I)$$ need not be an ideal of $$S$$. Why?

### Definition (Extension and contraction of ideals)

Let $$\varphi : R \to S$$ be a ring homomorphism.

1. Let $$I$$ be an $$R$$-ideal. Define the *extension* of $$I$$, denoted $$I^{e}$$, to be the smallest ideal of $$S$$ containing $$\varphi(I)$$.
2. If $$J \subseteq S$$ is an $$S$$-ideal, the *contraction* of $$J$$, denoted $$J^{c}$$, is $$\varphi^{-1}(J)$$.

### Proposition (Iterated contractions and extensions)

Let $$\varphi : R \to S$$ be a ring homomorphism, $$I \subseteq R$$ an $$R$$-ideal and $$J \subseteq S$$ an $$S$$-ideal. Then:

1. $$I \subseteq (I^{e})^{c}$$ and $$J \supseteq (J^{c})^{e}$$;
2. $$I^{e} = I^{ece}$$;
3. $$J^{c} = J^{cec}$$.

***Proof:*** We shall use two monotonicity properties. If $$I_{1} \subseteq I_{2}$$ are $$R$$-ideals, then $$I_{1}^{e} \subseteq I_{2}^{e}$$: indeed, $$\varphi(I_{1}) \subseteq \varphi(I_{2}) \subseteq I_{2}^{e}$$, and since $$I_{1}^{e}$$ is the smallest ideal containing $$\varphi(I_{1})$$, we have that $$I_{1}^{e} \subseteq I_{2}^{e}$$. If $$J_{1} \subseteq J_{2}$$ are $$S$$-ideals, then $$J_{1}^{c} = \varphi^{-1}(J_{1}) \subseteq \varphi^{-1}(J_{2}) = J_{2}^{c}$$, directly.

For (a): if $$x \in I$$, then $$\varphi(x) \in \varphi(I) \subseteq I^{e}$$, so $$x \in \varphi^{-1}(I^{e}) = (I^{e})^{c}$$; that is, $$I \subseteq I^{ec}$$. On the other hand, $$\varphi(J^{c}) = \varphi(\varphi^{-1}(J)) \subseteq J$$, and since $$J$$ is an ideal containing $$\varphi(J^{c})$$, the smallest ideal with that property satisfies $$(J^{c})^{e} \subseteq J$$.

For (b): applying the first part of (a) to the ideal $$I$$ and then the monotonicity of the extension, $$I \subseteq I^{ec}$$ implies $$I^{e} \subseteq I^{ece}$$. And applying the second part of (a) with $$J = I^{e}$$, we obtain $$I^{ece} = (I^{ec})^{e} = ((I^{e})^{c})^{e} \subseteq I^{e}$$. Both inclusions give $$I^{e} = I^{ece}$$.

For (c): applying the first part of (a) with $$I = J^{c}$$, we obtain $$J^{c} \subseteq (J^{c})^{ec} = J^{cec}$$. And applying the monotonicity of the contraction to $$(J^{c})^{e} \subseteq J$$, we obtain $$J^{cec} = ((J^{c})^{e})^{c} \subseteq J^{c}$$. Both inclusions give $$J^{c} = J^{cec}$$.

### Example (An extension that grows: $$n\mathbb{Z}$$ inside $$\mathbb{Q}$$)

Let $$\varphi : \mathbb{Z} \to \mathbb{Q}$$ be such that $$n \mapsto n$$, and let $$n \neq 0, 1$$. Then $$\varphi(n) = n \in \mathbb{Q}^{\times}$$, and since the only ideal of $$\mathbb{Q}$$ containing a unit is all of $$\mathbb{Q}$$, we have that

$$
\langle \varphi((n)) \rangle = \mathbb{Q} \implies (n\mathbb{Z})^{e} = \mathbb{Q} \implies ((n\mathbb{Z})^{e})^{c} = \mathbb{Q}^{c} = \varphi^{-1}(\mathbb{Q}) = \mathbb{Z}.
$$

That is, $$I = n\mathbb{Z} \subsetneq I^{ec} = \mathbb{Z}$$: the contraction of the extension may be strictly larger than the original ideal.

## The isomorphism theorems

### Theorem (First isomorphism theorem)

Let $$R, S$$ be rings and $$f : R \to S$$ a ring homomorphism. Let $$F : R/\operatorname{Ker}(f) \to \operatorname{Im}(f)$$ be such that $$[a] \longmapsto f(a)$$. Then $$F$$ is an isomorphism and, in particular,

$$
R/\operatorname{Ker}(f) \cong \operatorname{Im}(f).
$$

***Proof:*** *$$F$$ is well defined.* If $$[a] = [b]$$, then $$a - b \in \operatorname{Ker}(f)$$, so that

$$
f(a - b) = 0 \implies f(a) = f(b) \implies F([a]) = F([b]).
$$

*$$F$$ is a homomorphism.* Using that $$f$$ is one,

$$
\begin{aligned}
F([a] + [b]) &= F([a + b]) = f(a + b) = f(a) + f(b) = F([a]) + F([b]), \\
F([a] \cdot [b]) &= F([a \cdot b]) = f(a \cdot b) = f(a) \cdot f(b) = F([a]) \cdot F([b]), \\
F([1]) &= f(1) = 1.
\end{aligned}
$$

*$$F$$ is surjective.* Every element of $$\operatorname{Im}(f)$$ is of the form $$f(a) = F([a])$$ for some $$a \in R$$.

*$$F$$ is injective.* We compute the kernel:

$$
F([a]) = 0_{S} \implies f(a) = 0_{S} \implies a \in \operatorname{Ker}(f) \implies [a] = [0],
$$

that is, $$\operatorname{Ker}(F) = \{ 0_{R/\operatorname{Ker}(f)} \} = \{ [0] \}$$, and therefore $$F$$ is injective. We conclude that $$F$$ is an isomorphism.

### Example (The quotient of a product by a factor)

Let $$R, S$$ be rings and $$\pi : R \times S \to S$$ such that $$(x, s) \mapsto s$$, which is a surjective homomorphism. Its kernel is

$$
\operatorname{Ker}(\pi) = R \times \{0\},
$$

since $$\pi(x, s) = 0_{S}$$ if and only if $$s = 0_{S}$$. Hence, by the first isomorphism theorem,

$$
(R \times S)/(R \times \{0\}) \cong S.
$$

### Example (The quotient of a product by a product of ideals)

Let $$R, S$$ be rings, $$I$$ an $$R$$-ideal and $$J$$ an $$S$$-ideal. Then

$$
(R \times S)/(I \times J) \cong R/I \times S/J,
$$

using the homomorphism $$\varphi : R \times S \to R/I \times S/J$$ such that $$(r, s) \mapsto (r + I, s + J)$$ (exercise).

### Theorem (Second isomorphism theorem)

Let $$R$$ be a ring, $$S \leq R$$ a subring and $$I$$ an $$R$$-ideal. Then:

1. $$S \cap I$$ is an $$S$$-ideal;
2. $$S + I$$ is a subring of $$R$$;
3. $$I$$ is an $$(S + I)$$-ideal;
4. $$S/(S \cap I) \cong (S + I)/I$$.

***Proof:*** For (1): $$0 \in S \cap I$$, and $$S \cap I$$ is closed under sums because $$S$$ and $$I$$ are. For absorption, let $$s \in S$$ and $$x \in S \cap I$$; then $$s x \in S$$, since $$S$$ is closed under products, and $$s x \in I$$, by the absorption of $$I$$ in $$R$$ (note that $$s \in S \subseteq R$$); that is, $$s x \in S \cap I$$, and similarly $$x s \in S \cap I$$.

For (2): we use the subring criterion. First, $$1 = 1 + 0 \in S + I$$. If $$s + x, s' + x' \in S + I$$, then

$$
(s + x) - (s' + x') = (s - s') + (x - x') \in S + I,
$$

and for the product,

$$
(s + x)(s' + x') = s s' + (s x' + x s' + x x'),
$$

where $$s s' \in S$$ and the three terms in brackets lie in $$I$$ by absorption; hence the product lies in $$S + I$$.

For (3): $$I \subseteq S + I$$ (since $$x = 0 + x$$), $$I$$ is non-empty and closed under sums, and absorption by elements of $$S + I \subseteq R$$ is a particular case of the absorption of $$I$$ in $$R$$.

For (4): consider $$\varphi : S \to (S + I)/I$$ given by $$\varphi(s) = s + I$$, the restriction to $$S$$ of the canonical projection. It is a homomorphism, since the operations of $$(S+I)/I$$ are computed with representatives. It is surjective: every class of $$(S + I)/I$$ is of the form $$(s + x) + I$$ with $$s \in S$$, $$x \in I$$, and $$(s + x) + I = s + I = \varphi(s)$$, since $$x \in I$$. Its kernel is

$$
\operatorname{Ker}(\varphi) = \{ s \in S :\ s + I = I \} = \{ s \in S :\ s \in I \} = S \cap I.
$$

By the first isomorphism theorem, $$S/(S \cap I) \cong \operatorname{Im}(\varphi) = (S + I)/I$$.

### Theorem (Third isomorphism theorem)

Let $$R$$ be a ring and let $$I \subseteq J \subseteq R$$ be ideals. Then

$$
(R/I)\big/(J/I) \cong R/J.
$$

***Proof:*** Consider $$f : R/I \to R/J$$ given by $$f([x]_{I}) = [x]_{J}$$. It is well defined: if $$[x]_{I} = [y]_{I}$$, then $$x - y \in I \subseteq J$$, so that $$[x]_{J} = [y]_{J}$$. It is a homomorphism, since the operations in both quotients are computed with representatives:

$$
f([x]_{I} + [y]_{I}) = f([x + y]_{I}) = [x + y]_{J} = [x]_{J} + [y]_{J},
$$

and similarly for the product; moreover $$f([1]_{I}) = [1]_{J}$$. It is surjective: every class $$[x]_{J}$$ is $$f([x]_{I})$$. Its kernel is

$$
\operatorname{Ker}(f) = \{ [x]_{I} :\ [x]_{J} = [0]_{J} \} = \{ [x]_{I} :\ x \in J \} = J/I.
$$

By the first isomorphism theorem,

$$
(R/I)\big/(J/I) = (R/I)\big/\operatorname{Ker}(f) \cong \operatorname{Im}(f) = R/J.
$$
{% endraw %}
