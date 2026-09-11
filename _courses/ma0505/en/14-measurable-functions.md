---
layout: chapter
course: ma0505
chapter: 14
title: "Measurable Functions"
slug: 14-measurable-functions
toc:
  sidebar: right
lang: en
permalink: /notes/ma0505/14-measurable-functions/
---

{% raw %}
## Definition and equivalences

### Definition (Measurable function)

Let $$f : E \to \overline{\mathbb{R}} = \mathbb{R} \cup \{\pm\infty\}$$. We say that $$f$$ is *measurable* if for every $$a \in \mathbb{R}$$

$$
\{f > a\} := \{x \in E : f(x) > a\} \in \mathcal{M}.
$$

Since $$E = \bigcup_{k=1}^{\infty}\{f > -k\} \cup \{f = -\infty\}$$, if $$f$$ is measurable then $$E$$ is measurable if and only if $$\{f = -\infty\}$$ is measurable. In what follows $$E$$ is assumed to be measurable.

### Example (Continuous and indicator functions)

1. If $$f : \mathbb{R}^{d} \to \mathbb{R}$$ is continuous, $$\{f > a\} = f^{-1}((a, \infty))$$ is open, hence measurable; every continuous function is measurable.
2. If $$f = \mathbf{1}_{A}$$ with $$A$$ measurable, then $$\{f > a\}$$ equals $$E$$ if $$a < 0$$, $$A$$ if $$0 \leq a < 1$$ and $$\emptyset$$ if $$a \geq 1$$; in every case it is measurable.

### Theorem (Equivalent conditions for measurability)

Let $$f : E \to \overline{\mathbb{R}}$$ with $$E$$ measurable. The following conditions, for every $$a \in \mathbb{R}$$, are equivalent:

$$
\text{(i) } \{f > a\} \in \mathcal{M}, \quad \text{(ii) } \{f < a\} \in \mathcal{M}, \quad \text{(iii) } \{f \leq a\} \in \mathcal{M}, \quad \text{(iv) } \{f \geq a\} \in \mathcal{M}.
$$

***Proof:*** $$\{f \leq a\} = \{f > a\}^{c}$$ and $$\{f < a\} = \{f \geq a\}^{c}$$, so that (i)$$\Leftrightarrow$$(iii) and (ii)$$\Leftrightarrow$$(iv) by closure under complements. Moreover

$$
\{f \geq a\} = \bigcap_{n=1}^{\infty}\Big\{f > a - \tfrac{1}{n}\Big\}, \qquad \{f > a\} = \bigcup_{n=1}^{\infty}\Big\{f \geq a + \tfrac{1}{n}\Big\},
$$

which shows (i)$$\Rightarrow$$(iv) and (iv)$$\Rightarrow$$(i) by closure under countable intersections and unions. The four conditions are therefore equivalent.

### Note (Other measurable sets associated with $$f$$)

If $$f : E \to \overline{\mathbb{R}}$$ is measurable, then the following are measurable

$$
\{f > -\infty\} = \bigcup_{k}\{f > -k\}, \quad \{f < \infty\} = \bigcup_{k}\{f \leq k\}, \quad \{f = \infty\}, \quad \{a \leq f \leq b\}, \quad \{a \leq f < b\},
$$

since they are countable intersections and unions of the sets $$\{f > a\}$$, $$\{f \leq a\}$$, etc.

### Definition (Borel measurable function)

$$f : E \to \mathbb{R}$$ is *Borel measurable* if $$E \in \mathcal{B}$$ and $$\{f > a\} \in \mathcal{B}$$ for every $$a \in \mathbb{R}$$.

### Theorem (Measurability via preimages of open sets)

Let $$f : E \to \mathbb{R}$$. Then $$f$$ is measurable if and only if $$f^{-1}(G)$$ is measurable for every open $$G \subseteq \mathbb{R}$$.

***Proof:*** If the preimages of open sets are measurable, taking $$G = (a, \infty)$$ gives $$\{f > a\} = f^{-1}(G)$$ measurable, hence $$f$$ is measurable. Conversely, let $$f$$ be measurable and $$G \subseteq \mathbb{R}$$ open; write $$G = \bigcup_{k}(a_{k}, b_{k})$$. Since

$$
f^{-1}\big((a_{k}, b_{k})\big) = \{a_{k} < f\} \cap \{f < b_{k}\}
$$

is measurable, $$f^{-1}(G) = \bigcup_{k} f^{-1}\big((a_{k}, b_{k})\big)$$ is a countable union of measurable sets, hence measurable.

## Composition, equality almost everywhere and operations

### Lemma (Composition of a measurable function with a continuous one)

Let $$f : E \to \mathbb{R}$$ be measurable and $$\phi : \mathbb{R} \to \mathbb{R}$$ continuous. Then $$\phi \circ f$$ is measurable.

***Proof:*** Let $$G \subseteq \mathbb{R}$$ be open. Then $$(\phi \circ f)^{-1}(G) = f^{-1}\big(\phi^{-1}(G)\big)$$. Since $$\phi$$ is continuous, $$\phi^{-1}(G)$$ is open, and since $$f$$ is measurable, $$f^{-1}\big(\phi^{-1}(G)\big)$$ is measurable. By the previous theorem, $$\phi \circ f$$ is measurable.

### Note (Immediate consequences)

If $$f$$ is measurable, then $$|f|$$, $$|f|^{p}$$ ($$p > 0$$), $$e^{cf}$$ ($$c \in \mathbb{R}$$) and the positive and negative parts

$$
f^{+} = \max\{f, 0\}, \qquad f^{-} = \max\{-f, 0\}
$$

are measurable. (Here $$f^{+}, f^{-} \geq 0$$, $$f = f^{+} - f^{-}$$ and $$|f| = f^{+} + f^{-}$$, in agreement with the notation for the positive and negative parts of a real number.)

### Definition (Almost everywhere)

A property holds *almost everywhere* (a.e.) if it holds except on a set of measure zero.

### Lemma (Equality almost everywhere preserves measurability)

Let $$f, g : E \to \mathbb{R}$$ with $$f$$ measurable and $$g = f$$ almost everywhere. Then $$g$$ is measurable.

***Proof:*** Let $$a \in \mathbb{R}$$. Decomposing according to where $$f$$ and $$g$$ agree,

$$
\{g > a\} = \big(\{g > a\} \cap \{f = g\}\big) \cup \big(\{g > a\} \cap \{f \neq g\}\big).
$$

The first set is $$\{f > a\} \cap \{f = g\}$$, which is measurable (an intersection of measurable sets, apart from the set $$\{f \neq g\}$$ of measure zero, which is measurable). The second is contained in $$\{f \neq g\}$$, of measure zero, hence measurable. Therefore $$\{g > a\}$$ is a union of measurable sets and $$g$$ is measurable.

### Lemma (Composition with a continuous function for functions finite a.e.)

Let $$f : E \to \overline{\mathbb{R}}$$ be measurable with $$m(\{f = \infty\}) = m(\{f = -\infty\}) = 0$$. Then $$\phi \circ f$$ is measurable for every continuous $$\phi : \mathbb{R} \to \mathbb{R}$$.

***Proof:*** Let $$F = \{x \in E : f(x) \in \mathbb{R}\}$$ and define $$f_{1} = f$$ on $$F$$ and $$f_{1} = 0$$ on $$E \setminus F$$. Since $$E \setminus F = \{f = \infty\} \cup \{f = -\infty\}$$ has measure zero, $$f_{1}$$ is measurable and $$f_{1} = f$$ almost everywhere. By the composition lemma, $$\phi \circ f_{1}$$ is measurable, and since $$\phi \circ f_{1} = \phi \circ f$$ a.e., the previous lemma gives that $$\phi \circ f$$ is measurable.

### Lemma (The set where one measurable function exceeds another is measurable)

Let $$f, g : E \to \mathbb{R}$$ be measurable. Then $$\{f > g\}$$ is measurable.

***Proof:*** Let $$\{q_{n}\}_{n=1}^{\infty}$$ be an enumeration of $$\mathbb{Q}$$. Since $$f(x) > g(x)$$ if and only if there exists a rational strictly between $$g(x)$$ and $$f(x)$$,

$$
\{f > g\} = \bigcup_{n=1}^{\infty}\big(\{f > q_{n}\} \cap \{q_{n} > g\}\big),
$$

a countable union of intersections of measurable sets, hence measurable.

### Lemma (Vector space structure of the measurable functions)

Let $$f, g : E \to \mathbb{R}$$ be measurable. Then:

1. $$f + \lambda$$ and $$\lambda f$$ are measurable for every $$\lambda \in \mathbb{R}$$;
2. $$f + g$$ is measurable.

***Proof:*** Part (i) is left as an exercise (direct from the definition: $$\{f + \lambda > a\} = \{f > a - \lambda\}$$ and, for $$\lambda > 0$$, $$\{\lambda f > a\} = \{f > a/\lambda\}$$, etc.). For (ii), $$g$$ and $$\lambda - g$$ are measurable by (i), and by the previous lemma applied to $$f$$ and $$\lambda - g$$,

$$
\{f + g > \lambda\} = \{f > \lambda - g\}
$$

is measurable for every $$\lambda \in \mathbb{R}$$, hence $$f + g$$ is measurable.

### Exercise (The case of infinite values in the sum)

The previous lemma still holds for $$f, g : E \to \overline{\mathbb{R}}$$ provided that $$f + g$$ is well defined (that is, avoiding the indeterminate form $$\infty - \infty$$). Prove this variant.

### Corollary (Product and quotient of measurable functions)

Let $$f, g : E \to \overline{\mathbb{R}}$$ be measurable. Then $$fg$$ is measurable (with the convention $$0 \cdot (\pm\infty) = 0$$, so that the product is always defined), and $$f/g$$ is measurable if $$g \neq 0$$.

***Proof:*** Let $$F = \{f \in \mathbb{R}\} \cap \{g \in \mathbb{R}\}$$. For $$a \geq 0$$,

$$
\{fg > a\} = \big(\{fg > a\} \cap F\big) \cup \big(\{f = \infty\} \cap \{g > 0\}\big) \cup \big(\{g = \infty\} \cap \{f > 0\}\big) \cup \big(\{f = -\infty\} \cap \{g < 0\}\big) \cup \big(\{g = -\infty\} \cap \{f < 0\}\big),
$$

and every set on the right-hand side is measurable except, a priori, the first. On $$F$$ the polarisation identity holds

$$
fg = \tfrac{1}{4}\big((f + g)^{2} - (f - g)^{2}\big);
$$

since $$f + g$$ and $$f - g$$ are measurable (previous lemma) and squaring is composition with the continuous map $$t \mapsto t^{2}$$, $$fg$$ is measurable on $$F$$, so that $$\{fg > a\} \cap F$$ is measurable. The treatment of $$a < 0$$ and of the quotient $$f/g$$ (composing with $$t \mapsto 1/t$$ where $$g \neq 0$$) is left as an exercise.

## Sequences of measurable functions and simple functions

### Theorem (Sup, inf, limit superior and limit inferior of measurable functions)

Let $$\{f_{k}\}_{k=1}^{\infty}$$ be a sequence of measurable functions $$E \to \overline{\mathbb{R}}$$. Then $$\sup_{k} f_{k}$$, $$\inf_{k} f_{k}$$, $$\limsup_{k} f_{k}$$ and $$\liminf_{k} f_{k}$$ are measurable.

***Proof:*** For every $$a \in \mathbb{R}$$,

$$
\Big\{\sup_{k \geq 1} f_{k} > a\Big\} = \bigcup_{k=1}^{\infty}\{f_{k} > a\}
$$

is measurable, hence $$\sup_{k} f_{k}$$ is measurable. The remaining ones reduce to this one:

$$
\inf_{k} f_{k} = -\sup_{k}(-f_{k}), \qquad \limsup_{k} f_{k} = \inf_{k \geq 1}\sup_{\ell \geq k} f_{\ell}, \qquad \liminf_{k} f_{k} = \sup_{k \geq 1}\inf_{\ell \geq k} f_{\ell}.
$$

### Definition (Simple function)

A function $$\phi$$ is *simple* if there exist measurable sets $$A_{1}, \dots, A_{m}$$ and reals $$a_{1}, \dots, a_{m}$$ with

$$
\phi = \sum_{k=1}^{m} a_{k}\, \mathbf{1}_{A_{k}}.
$$

### Exercise (Canonical form of a simple function)

Prove that every simple function $$\phi$$ admits a representation $$\phi = \sum_{k=1}^{\ell} b_{k}\, \mathbf{1}_{B_{k}}$$ with $$B_{1}, \dots, B_{\ell}$$ measurable and pairwise disjoint and $$b_{1}, \dots, b_{\ell}$$ pairwise distinct.

### Note (Dyadic approximation of a non-negative function)

Let $$f : E \to [0, \infty]$$. For $$k \in \mathbb{N}$$ define

$$
f_{k} = k\,\mathbf{1}_{B_{k}} + \sum_{j=1}^{k 2^{k}} \frac{j-1}{2^{k}}\,\mathbf{1}_{A_{k}^{j}}, \qquad B_{k} = f^{-1}\big([k, \infty]\big), \quad A_{k}^{j} = f^{-1}\Big(\Big[\tfrac{j-1}{2^{k}}, \tfrac{j}{2^{k}}\Big)\Big),
$$

that is, $$f_{k}(x) = \tfrac{j-1}{2^{k}}$$ if $$\tfrac{j-1}{2^{k}} \leq f(x) < \tfrac{j}{2^{k}}$$ and $$f_{k}(x) = k$$ if $$f(x) \geq k$$. If $$0 \leq f(x) < k$$, then $$0 \leq f(x) - f_{k}(x) < \tfrac{1}{2^{k}}$$, so that $$f_{k}(x) \to f(x)$$ when $$f(x) < \infty$$; and if $$f(x) = \infty$$, $$f_{k}(x) = k \to \infty$$. Moreover $$f_{k} \leq f_{k+1}$$: on passing from $$k$$ to $$k+1$$ each dyadic interval is split in two, and the value of $$f_{k+1}$$ is equal to or one dyadic unit greater than that of $$f_{k}$$. If $$f$$ is measurable, the $$A_{k}^{j}$$ and $$B_{k}$$ are measurable and each $$f_{k}$$ is simple and measurable.

### Theorem (Approximation by simple functions)

Let $$f : E \to \overline{\mathbb{R}}$$. Then there exists a sequence of simple functions $$\psi_{k}$$ with $$\psi_{k} \to f$$ pointwise. If $$f \geq 0$$, the sequence may be taken increasing; if $$f$$ is measurable, the $$\psi_{k}$$ may be taken measurable.

***Proof:*** For $$f \geq 0$$ the dyadic sequence $$\psi_{k} = f_{k}$$ of the previous note is simple, increasing and converges pointwise to $$f$$ (and measurable if $$f$$ is). For $$f$$ of arbitrary sign one applies the above to $$f^{+}$$ and $$f^{-}$$ and takes $$\psi_{k} = (f^{+})_{k} - (f^{-})_{k}$$; the details of this case are left as an exercise.
{% endraw %}
