---
layout: chapter
course: ma0561
chapter: 19
title: "Products of Rings"
slug: 19-products-of-rings
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/19-products-of-rings/
---

{% raw %}
## The direct product and its properties

### Definition (The product of two rings)

Let $$R_{1}, R_{2}$$ be rings, with structures $$(R_{1}, +_{R_{1}}, \cdot_{R_{1}}, 0_{R_{1}}, 1_{R_{1}})$$ and $$(R_{2}, +_{R_{2}}, \cdot_{R_{2}}, 0_{R_{2}}, 1_{R_{2}})$$. Define

$$
R_{1} \times R_{2} := \{ (x_{1}, x_{2}) :\ x_{1} \in R_{1},\ x_{2} \in R_{2} \},
$$

with the componentwise operations:

$$
(x_{1}, x_{2}) + (y_{1}, y_{2}) = (x_{1} +_{R_{1}} y_{1},\ x_{2} +_{R_{2}} y_{2}), \qquad (x_{1}, x_{2}) \cdot (y_{1}, y_{2}) = (x_{1} y_{1},\ x_{2} y_{2}).
$$

The zero in $$R_{1} \times R_{2}$$ is $$\vec{0} = (0_{R_{1}}, 0_{R_{2}})$$ and the one is $$\vec{1} = (1_{R_{1}}, 1_{R_{2}})$$. Then $$(R_{1} \times R_{2}, +, \cdot, \vec{0}, \vec{1})$$ is a ring.

### Definition (The direct product of a family of rings)

In general, if $$\{R_{i}\}_{i \in I}$$ is a set of rings, we can construct the ring

$$
\prod_{i \in I} R_{i}
$$

in an analogous way, with the operations defined componentwise.

### Example ($$\mathbb{R}^{2}$$ has zero divisors)

$$\mathbb{R}^{2} = \mathbb{R} \times \mathbb{R}$$ is a ring, and

$$
\underbrace{(1, 0)}_{\neq (0,0)} \cdot \underbrace{(0, 1)}_{\neq (0,0)} = (0, 0).
$$

So, even though $$\mathbb{R}$$ has no zero divisors, $$\mathbb{R}^{2}$$ does.

### Note (The units of the product)

Let $$\{R_{i} :\ i \in I\}$$ be a set of rings and $$R = \prod_{i \in I} R_{i}$$. Considering the units $$R^{\times}$$, we have that

$$
R^{\times} = \prod_{i \in I} R_{i}^{\times}.
$$

### Theorem (Subrings and ideals of a product)

Let $$\{R_{i} :\ i \in I\}$$ be a set of rings and $$R = \prod_{i \in I} R_{i}$$. Then:

1. if for each $$i \in I$$, $$S_{i}$$ is a subring of $$R_{i}$$, then $$\prod_{i \in I} S_{i}$$ is a subring of $$R$$;
2. if for each $$i \in I$$, $$A_{i} \subseteq R_{i}$$ is an $$R_{i}$$-ideal, then $$\prod_{i \in I} A_{i}$$ is an $$R$$-ideal;
3. if $$K$$ is an ideal of $$R \times S$$, then there exist $$I$$, an $$R$$-ideal, and $$J$$, an $$S$$-ideal, such that $$K = I \times J$$.

***Proof:*** For (1): we use the subring criterion. Since $$1_{R_{i}} \in S_{i}$$ for each $$i$$, we have that $$\vec{1} = (1_{R_{i}})_{i} \in \prod_{i} S_{i}$$; and if $$a = (a_{i})_{i}$$ and $$b = (b_{i})_{i}$$ lie in $$\prod_{i} S_{i}$$, then $$a - b = (a_{i} - b_{i})_{i}$$ and $$a b = (a_{i} b_{i})_{i}$$ have all their components in the $$S_{i}$$, since each $$S_{i}$$ is a subring.

For (2): $$\prod_{i} A_{i} \neq \emptyset$$ since it contains $$\vec{0}$$; it is closed under componentwise sums; and if $$r = (r_{i})_{i} \in R$$ and $$x = (x_{i})_{i} \in \prod_{i} A_{i}$$, then $$r x = (r_{i} x_{i})_{i}$$ has each component in $$A_{i}$$ by the absorption of each $$A_{i}$$.

For (3): let $$K$$ be an ideal of $$R \times S$$. If $$(r, s) \in K$$, absorption with $$(1, 0)$$ and $$(0, 1)$$ gives

$$
(r, 0) = (1, 0) \cdot (r, s) \in K, \qquad (0, s) = (0, 1) \cdot (r, s) \in K.
$$

Define

$$
I = \{ r \in R :\ (r, 0) \in K \}, \qquad J = \{ s \in S :\ (0, s) \in K \}.
$$

Then $$I$$ is an $$R$$-ideal: $$0 \in I$$; if $$r, r' \in I$$, then $$(r + r', 0) = (r, 0) + (r', 0) \in K$$; and if $$a \in R$$, then $$(a r, 0) = (a, 0) \cdot (r, 0) \in K$$ by the absorption of $$K$$. Analogously $$J$$ is an $$S$$-ideal. Let us see that $$K = I \times J$$. “$$\subseteq$$”: if $$(r, s) \in K$$, by the above $$(r, 0), (0, s) \in K$$, that is, $$r \in I$$ and $$s \in J$$. “$$\supseteq$$”: if $$r \in I$$ and $$s \in J$$, then

$$
(r, s) = (r, 0) + (0, s) \in K,
$$

by the closure of $$K$$ under sums.
{% endraw %}
