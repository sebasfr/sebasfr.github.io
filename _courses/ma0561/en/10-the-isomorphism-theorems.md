---
layout: chapter
course: ma0561
chapter: 10
title: "The Isomorphism Theorems"
slug: 10-the-isomorphism-theorems
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/10-the-isomorphism-theorems/
---

{% raw %}
## The Isomorphism Theorems

### Theorem (First isomorphism theorem)

Let $$G, G'$$ be groups, let $$f:G \to G'$$ be a homomorphism and let $$H = \operatorname{Ker}(f)$$. Then $$G / H \cong \operatorname{Im}(f)$$.

***Proof:*** Since $$H \triangleleft G$$, $$G / H$$ is a group. Let $$f':G / H \to G'$$ be such that $$aH \mapsto f(a)$$. We shall prove that $$f'$$ is well defined, i.e., that it sends members of the same equivalence class to the same images. Given $$a,b \in G$$, suppose that $$aH = bH$$, i.e., that $$b^{-1}a \in H$$. Thus,

$$
f(b^{-1}a)=1_{G'} \implies (f(b))^{-1} f(a) = 1_{G'}\implies f(b) = f(a) \implies f'(aH) = f'(bH).
$$

We shall now prove that $$f'$$ is a homomorphism. Given $$aH, bH \in G / H$$, note that

$$
f'(aH \cdot bH) = f'((a \ast b)H)= f(a \ast b) =f(a) \ast_{G'}f(b) = f'(aH)\ast_{G'} f'(bH).
$$

Thus, $$f$$ is a homomorphism. For injectivity, let $$aH \in \operatorname{Ker}(f')$$. Hence,

$$
f'(aH) = 1_{G'} \implies f(a) = 1_{G'} \implies a \in \operatorname{Ker}(f) = H \implies aH=H.
$$

Finally, we shall prove that $$f'$$ is surjective, i.e., that $$\operatorname{Im}(f') = \operatorname{Im}(f)$$. Note that

$$
b \in \operatorname{Im}(f') \iff \exists a \in G (f'(aH)=b) \iff \exists a \in G (f(a)=b) \iff b \in \operatorname{Im}(f).
$$

Thus, $$f'$$ is an isomorphism, from which we conclude the result.

### Theorem (Third isomorphism theorem)

Let $$K \leq H \leq G$$ be groups such that $$K \triangleleft G$$ and $$H \triangleleft G$$. Then $$H / K \triangleleft G / K$$ and $$G / H \cong (G/K) / (H / K)$$.

***Proof:*** We shall first prove that $$H / K \triangleleft G / K$$. Let $$aK \in G / K$$. We must show that $$(aK) \cdot H /K \cdot (aK)^{-1} \subseteq H / K$$. Let $$bK \in H / K$$, hence

$$
(aK) \cdot (bK) \cdot (aK)^{-1} = (aba^{-1})K \in H / K.
$$

We conclude that $$H / K \triangleleft G / K$$. Now, define $$f:G/K \to G / H$$ such that $$aK \mapsto aH$$. We shall prove that $$f$$ is well defined. Take $$a,b \in G$$ such that $$aK = bK$$. Then,

$$
b^{-1}a \in K \subseteq H \iff b^{-1} a \in H \iff aH = bH \implies f(aK) = f(bK).
$$

Let us prove that $$f$$ is a homomorphism:

$$
f(aK \cdot bK) = f(a \cdot b \cdot K) \quad= ab H = aH \cdot bH =f(aK) \cdot f(bK),
$$

from which we conclude that $$f$$ is a homomorphism. Finally, note that

$$
aK \in\operatorname{Ker}(f) \iff f(aK) =H \iff aH =H \iff a \in H \iff aK \in H / K,
$$

so that $$\operatorname{Ker}(f)  = H / K$$. Finally, applying the first isomorphism theorem, we conclude the result.

### Theorem (commutativity of normal subgroups)

Let $$N,H \leq G$$ with $$N \triangleleft G$$. Then $$NH=HN$$.

***Proof:*** Exercise

### Theorem (Second isomorphism theorem)

Let $$(G, \cdot)$$ be a group, $$H \leq G$$, $$N \triangleleft G$$. Then $$N \cap H \triangleleft H$$, $$NH \leq G$$ and $$H / (N \cap H) \cong NH / N$$.

***Proof:*** We know that $$N \cap H \subseteq H$$, $$N \cap H \subseteq N$$. Let $$x \in H$$. Then $$x \in G$$. We must show that $$x(N \cap H)x ^{-1} \subseteq N \cap H$$. Clearly, $$x(N \cap H)x ^{-1} \subseteq H$$. Since $$N \triangleleft G$$, we have $$x(N \cap H)x ^{-1} \subseteq x N x ^{-1} \subseteq N$$. Thus, $$x(N \cap H)x ^{-1} \subseteq N \cap H$$ and we have proved the normality of $$N \cap H$$.
The proof that $$NH\leq G$$ is left as an exercise.
Finally, define $$f:H \to G / N$$ such that $$h \mapsto h N$$. Note that $$f$$ is a homomorphism, since $$f(g \cdot h) = g h N = (gN)(hN) = f(g) \cdot f(h)$$. Moreover,

$$
h \in \operatorname{Ker}(f) \iff f(h) = N \iff hN =N \iff h \in N,
$$

so that $$\operatorname{Ker}(f) = N \cap H$$. Finally, we prove that $$\operatorname{Im}(f) = NH /N$$. Let $$gN \in \operatorname{Im}(f)$$. Hence, there exists $$h \in H$$ such that $$hN = gN$$. Hence, $$g \in HN = NH$$, so $$gN \in NH / N$$. Now, let $$g \in HN / N$$. Then, there exists $$x \in HN$$ such that $$g = xN \in HN / N$$. Hence, $$x = h_{1} n_{1}$$, with $$h_{1} \in H$$, $$n_{1} \in N$$. Thus,

$$
g = xN = (h_{1} \cdot n_{1})N = h_{1} N,
$$

so $$g = f(h_{1}) \in \operatorname{Im}(f)$$. The result follows by applying the first isomorphism theorem.

### Exercise (Inverse image of a subgroup)

If $$f:G \to G^{\ast}$$ is a homomorphism and $$S^{\ast}\leq G^{\ast}$$. Then $$f^{-1}(S^{\ast}) = \{ x \in G  : f(x)\in S^{\ast} \}$$

### Theorem (Correspondence)

Let $$(G, \cdot)$$ be a group, $$H \triangleleft G$$ and $$p:G \to G / H$$ such that $$p(g)=gH$$. Then $$K \mapsto p(K) = K / H$$ is a bijection between the subgroups of $$G$$ that contain $$H$$ and the subgroups of $$G/H$$. Moreover, if $$K$$ is such that $$H\leq K\leq G$$ and $$K^{\ast}:=K / H$$, we have that

1. $$L\leq K \iff L^{\ast} \leq K^{\ast}$$ and in this case $$[K:L] =[K^{\ast}:L^{\ast}]$$.
2. $$L \triangleleft K \iff L^{\ast} \triangleleft K^{\ast}$$, and in this case, $$K / L \cong K^{\ast} / L^{\ast}$$.

***Proof:*** Let $$A = \{ L: H\leq L \leq G \}$$ and $$B = \{ \tilde{G}: \tilde{G} \leq G / H \}$$. Define $$\Phi:A \to B$$ such that $$\Phi(L) = L / H$$. Suppose that $$L,K \in A$$ and $$L / H = K /H$$. We shall prove that $$L = K$$. Let $$\ell \in L$$. Then, $$\ell H \in L / H$$, i.e., there exists $$k \in K$$ such that $$\ell H = k H$$. Thus, $$\ell ^{-1} k \in H \subseteq K$$. Since $$k \in K$$ and $$\ell^{-1}k \in K$$, we have $$\ell = k \cdot (\ell^{-1}k)^{-1} \in K$$, whence $$L \subseteq K$$. The other inclusion is the same. Hence $$\Phi$$ is injective. Now, let $$C \in B$$, i.e., $$C \leq G / H$$. Let $$K = p ^{-1}(C) \leq G$$ and $$\operatorname{Ker}(p) \subseteq K$$. Then, $$H \subseteq K$$. Thus, $$\Phi(K)=C$$. Conclude that $$\Phi$$ is a bijection. We shall now prove points 1 and 2:

1. It is clear that $$L \leq K \iff L ^\ast \leq K^{\ast}$$. To prove that the indices coincide, it suffices to prove that there is a bijection between the cosets of $$K/L$$ and $$K^\ast/L^{\ast}$$. Let $$f:K/L \to K^{\ast}/L^{\ast}$$ be such that $$kL \mapsto p(k)L^{\ast} = kH (L / H)$$.

    - **Well-definedness of $$f$$**: If $$k_{1}, k_{2} \in K$$ are such that $$k_{1}L = k_{2}L$$, then $$k_{2}^{-1} k_{1} \in L$$ and consequently $$k_{2}^{-1} k_{1} H \in L/H = L^{\ast}$$, which implies that $$f(k_{1}L) = p(k_{1}) L^\ast = p(k_{2}) L^{\ast} = f(k_{2}L)$$, and therefore $$f$$ is well defined.
    - **Injectivity of $$f$$**: Let $$k_{1}, k_{2} \in K$$ be such that $$f(k_{1}L) = f(k_{2}L)$$. Note that $$f$$ is injective, since

        $$
        \begin{aligned}
        p(k_{1})L^{\ast} = p(k_{2}) L^{\ast} &\implies p(k_{2})^{-1} \ast p(k_{1}) \in L^{\ast} \implies p(k_{2}^{-1} k_{1}) \in L^\ast = L/H \\
        k_{2}^{-1} k_{1} H \in L / H &\implies k_{2}^{-1} k_{1} \in L \implies k_{1}L = k_{2}L,
        \end{aligned}
        $$
    - **Surjectivity of $$f$$**: This follows directly from the surjectivity of $$p$$.
        Thus, $$[K:L] = [K^{\ast}:L^{\ast}]$$.
2. The isomorphism between $$K/L$$ and $$K^{\ast}/L^{\ast}$$ follows from the third isomorphism theorem.
{% endraw %}
