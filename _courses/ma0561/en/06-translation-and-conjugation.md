---
layout: chapter
course: ma0561
chapter: 6
title: "Translation and Conjugation"
slug: 06-translation-and-conjugation
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/06-translation-and-conjugation/
---

{% raw %}
## Translation and conjugation

### Definition (Translation)

Let $$(G, \ast)$$ be a group and let $$a \in G$$. The left (right) translation by $$a$$ is $$T_{a}:G\to G$$ such that $$x \mapsto a \ast x$$ ($$x \mapsto x \ast a$$).

### Note (Translation is bijective)

1. $$T_{a}$$ is injective, since $$T_{a}(x)=T_{a}(y) \iff a \ast x = a \ast y \iff x = y$$.
2. $$T_{a}$$ is surjective, since if $$y \in G$$, $$T_{a}(a^{-1} \ast y) = y$$.

Hence $$T_{a}$$ is bijective. Conclude that $$T_{a} \in S_{G} = \{ \sigma:G\to G \text{ bijective}\}$$.

### Theorem (Translations of $$G$$ are a monomorphism)

Let $$f:G\to S_{G}$$ be such that $$f(a) = T_{a}$$. Then $$f$$ is a monomorphism.

***Proof:*** We first show that $$f$$ is a homomorphism, i.e., that $$f(a \ast b) = T_{a \ast b} = T_{a} \ast T_{b}$$. Let $$x \in G$$. We have that

$$
\begin{aligned}
(T_{a} \circ T_{b})(x) = T_{a}(T_{b}(x)) &= T_{a} (b \ast x)\\
&= a \ast (b \ast x) \\
&=(a \ast b) \ast x \\
&= T_{a \ast b} (x)
\end{aligned},
$$

from which we have that $$f$$ is a homomorphism. We now show that $$f$$ is injective. Let $$a \in \operatorname{Ker}(f)$$. Let $$a \in  G$$ be such that $$f(a) = T_{a} = \mathrm{id}_{G}$$. Hence,

$$
\forall x \in G  \quad(T_{a}(x)= x) \implies \forall x \in G  \quad(a \ast x = x) \implies a = 1_{G}.
$$

Thus $$\operatorname{Ker}(f) = \{ \mathrm{id_{G}} \}$$. We conclude that $$f$$ is a monomorphism.

### Definition (Conjugation)

Let $$G$$ be a group and $$a \in G$$. Define conjugation by $$a$$ $$C_{a}: G\to G$$ such that $$x \mapsto a \ast x \ast a^{-1}$$.

### Theorem (Conjugation in the automorphism)

Let $$G$$ be a group and $$a \in G$$. Then $$C_{a} \in \mathrm{Aut}(G)$$.

***Proof:*** Note that $$C_{a}(x \ast y) = C_{a}(x) \ast C_{a}(y)$$ (exercise), so $$C_{a}$$ is a homomorphism. To show that it is injective, take $$x \in \operatorname{Ker}(C_{a})$$. Hence

$$
C_{a}(x) = 1_{G} \implies a \ast x \ast a ^{-1} = 1_{G} \implies x = 1_{G}
$$

To show that it is surjective, let $$x \in G$$. Note that $$C_{a}(a^{-1} \ast x \ast a) = x$$, from which we conclude surjectivity.

### Theorem (Conjugations of $$G$$ are a homomorphism)

Let $$f:G\to \mathrm{Aut}(G) \leq S_{G}$$ be such that $$f(a) = C_{a}$$. Then $$f$$ is a homomorphism.

***Proof:*** Let $$x \in G$$. Then

$$
\begin{aligned}
(C_{a} \circ C_{b})(x) &= C_{a} (C_{b}(x))\\
&=C_{a} ( b \ast x \ast b^{-1})\\
&=a \ast ( b \ast x \ast b^{-1}) \ast a ^{-1} \\
&=(a \ast b) \ast x \ast (a \ast b) ^{-1} \\
&=C_{a \ast b}(x).
\end{aligned}
$$
{% endraw %}
