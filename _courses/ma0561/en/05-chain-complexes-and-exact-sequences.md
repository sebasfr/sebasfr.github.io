---
layout: chapter
course: ma0561
chapter: 5
title: "Chain Complexes and Exact Sequences"
slug: 05-chain-complexes-and-exact-sequences
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/05-chain-complexes-and-exact-sequences/
---

{% raw %}
## Chain complexes and exact sequences

### Definition (Chain complex)

A chain complex is a set $$\mathcal{S} = (G_{i}, \phi_{i})_{i \in \mathbb{Z}}$$ where:

1. For every $$i \in \mathbb{Z}$$, $$G_{i}$$ is a group,
2. For every $$i \in \mathbb{Z}$$, $$\phi_{i}: G_{i} \to G_{i-1}$$ is a group homomorphism.
3. $$\phi_i \circ \phi_{i+1}: G_{i+1} \to G_{i-1}$$ is such that $$(\phi_{i} \circ \phi_{i+1})(x) = 1_{G_{i-1}}$$ for every $$x \in G_{i+1}$$.

$$
\cdots \to G_{3} \overset{\phi_{3}}{\to} G_{2} \overset{\phi_{2}}{\to} G_{1} \overset{\phi_{1}}{\to} G_{0} \overset{\phi_{-1}}{\to} G_{-1} \overset{\phi_{-2}}{\to} \cdots
$$

Note that $$(\phi_{i} \circ \phi_{i+1})(x) = \phi_{i} \big(\phi_{i+1}(x)\big)= 1_{G_{i-1}}$$, hence $$\phi_{i+1}(x) \in \operatorname{Ker}(\phi_{i})$$ for every $$i \in \mathbb{N}$$. Let $$Z_{n}(\mathcal{S}) = \operatorname{Ker}(\phi_{n}) \subseteq G_{n}$$. $$B_{n}(\mathcal{S})=\operatorname{Im}(\phi_{n+1}) \subseteq G_{n}$$. Note that

$$
B_{n}(\mathcal{S}) \leq  Z_{n}(\mathcal{S}) \leq  G_{n}
$$

### Definition (Exact sequence)

Take $$\mathcal{S} = (G_{i}, \phi_{i})_{i \in \mathbb{Z}}$$ to be a chain complex. If for every $$i$$ we have that $$\operatorname{Im}(\phi_{i+1}) = \operatorname{Ker}(\phi_{i})$$. We say that $$\mathcal{S}$$ is an exact sequence.

### Definition (Short sequence)

A sequence is short if it is finite.

### Example (Short exact sequence)

Consider

$$
0 \rightarrow G_{2} \overset{ f }{\rightarrow} G_{1} \overset{ g }{\rightarrow} G_{0} \rightarrow 0,
$$

where $$0$$ denotes the trivial group. The unnamed homomorphisms are the trivial ones.

### Theorem (Exactness of the sequence and injectivity/surjectivity)

Let $$\phi_{0}:G_{0}\to G_{1}$$ be a homomorphism:

1. If $$0 \overset{ f }{\rightarrow} G_{0} \overset{ \phi_{0} }{\rightarrow} G_{1}$$ is exact, then $$\phi_{0}$$ is injective.
2. If $$G_{0} \overset{ \phi_{0} }{\rightarrow} G_{1} \overset{ f }{\rightarrow} 0$$ is exact, then $$\phi_{0}$$ is surjective.
3. If $$0 \overset{  f }{\rightarrow} G_{0} \overset{ \phi_{0} }{\rightarrow} G_{1} \overset{ g }{\rightarrow} 0$$, then $$\phi_{0}$$ is an isomorphism.

***Proof:*** For (1), note that $$\operatorname{Ker}(\phi_{0}) = \operatorname{Im}(f) = \{ 1_{G_{0}} \}$$, so $$\phi_{0}$$ is injective. For (2), note that $$\operatorname{Im}(\phi_{0}) = \operatorname{Ker} f = G_{1}$$. We combine both results for (3).

### Example (Exact sequence $$\mathbb{Z} \to \mathbb{Z}_2$$)

Consider

$$
0 \rightarrow 2\mathbb{Z} \overset{ i }{\rightarrow}  \mathbb{Z} \overset{ \pi }{\rightarrow} \mathbb{Z}_{2} \rightarrow 0,
$$

where $$i(x) = x$$ and $$\pi(x) = [x]$$ for every $$x \in \mathbb{Z}$$. It suffices to show that $$\operatorname{Im}(i) = \operatorname{Ker}(\pi)$$.
{% endraw %}
