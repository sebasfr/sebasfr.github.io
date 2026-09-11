---
layout: chapter
course: ma0561
chapter: 10
title: "Teoremas del isomorfismo"
slug: 10-teoremas-del-isomorfismo
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/10-teoremas-del-isomorfismo/
---

{% raw %}
## Teoremas del Isomorfismo

### Teorema (Primer teorema del isomorfismo)

Sean $$G, G'$$ grupos y sea $$f:G \to G'$$ un homomorfismo y sea $$H = \operatorname{Ker}(f)$$. Entonces, $$G / H \cong \operatorname{Im}(f)$$.

***Prueba:*** Como $$H \triangleleft G$$, $$G / H$$ es un grupo. Sea $$f':G / H \to G'$$ tal que $$aH \mapsto f(a)$$. Probaremos que $$f'$$ está bien definida, i.e., que envía miembros de la misma clase de equivalencia a las mismas imágenes. Dados $$a,b \in G$$, suponga que $$aH = bH$$, i.e., que $$b^{-1}a \in H$$. Así,

$$
f(b^{-1}a)=1_{G'} \implies (f(b))^{-1} f(a) = 1_{G'}\implies f(b) = f(a) \implies f'(aH) = f'(bH).
$$

Probaremos ahora que $$f'$$ es un homomorfismo. Dados, $$aH, bH \in G / H$$, note que

$$
f'(aH \cdot bH) = f'((a \ast b)H)= f(a \ast b) =f(a) \ast_{G'}f(b) = f'(aH)\ast_{G'} f'(bH).
$$

Así, $$f$$ es homomorfismo. Para la inyectividad, sea $$aH \in \operatorname{Ker}(f')$$. Luego,

$$
f'(aH) = 1_{G'} \implies f(a) = 1_{G'} \implies a \in \operatorname{Ker}(f) = H \implies aH=H.
$$

Finalmente, probaremos que $$f'$$ es sobreyectiva, i.e, que $$\operatorname{Im}(f') = \operatorname{Im}(f)$$. Note que

$$
b \in \operatorname{Im}(f') \iff \exists a \in G (f'(aH)=b) \iff \exists a \in G (f(a)=b) \iff b \in \operatorname{Im}(f).
$$

Así, $$f'$$ es un isomorfismo, de donde concluimos el resultado.

### Teorema (Tercer teorema del isomorfismo)

Sean $$K \leq H \leq G$$ grupos tales que $$K \triangleleft G$$ y $$H \triangleleft G$$. Entonces $$H / K \triangleleft G / K$$ y $$G / H \cong (G/K) / (H / K)$$.

***Prueba:*** Probaremos primero que $$H / K \triangleleft G / K$$. Sea $$aK \in G / K$$. Hay que mostrar que $$(aK) \cdot H /K \cdot (aK)^{-1} \subseteq H / K$$. Sea $$bK \in H / K$$, luego

$$
(aK) \cdot (bK) \cdot (aK)^{-1} = (aba^{-1})K \in H / K.
$$

Concluimos que $$H / K \triangleleft G / K$$. Ahora, defina $$f:G/K \to G / H$$ tal que $$aK \mapsto aH$$. Probaremos que $$f$$ está bien definida. Tome $$a,b \in G$$ tales $$aK = bK$$. Entonces,

$$
b^{-1}a \in K \subseteq H \iff b^{-1} a \in H \iff aH = bH \implies f(aK) = f(bK).
$$

Probemos que $$f$$ es un homomorfismo:

$$
f(aK \cdot bK) = f(a \cdot b \cdot K) \quad= ab H = aH \cdot bH =f(aK) \cdot f(bK),
$$

de donde concluimos que $$f$$ es un homomorfismo. Finalmente, note que

$$
aK \in\operatorname{Ker}(f) \iff f(aK) =H \iff aH =H \iff a \in H \iff aK \in H / K,
$$

de modo que $$\operatorname{Ker}(f)  = H / K$$. Finalmente, aplicando el primer teorema del isomorfismo, concluimos el resultado.

### Teorema (conmutatividad de subgrupos normales)

Sea $$N,H \leq G$$ con $$N \triangleleft G$$. Entonces $$NH=HN$$.

***Prueba:*** Ejercicio

### Teorema (Segundo teorema del isomorfismo)

Sea $$(G, \cdot)$$ un grupo, $$H \leq G$$, $$N \triangleleft G$$. Entonces $$N \cap H \triangleleft H$$, $$NH \leq G$$ y $$H / (N \cap H) \cong NH / N$$.

***Prueba:*** Sabemos que $$N \cap H \subseteq H$$, $$N \cap H \subseteq N$$. Sea $$x \in H$$. Entonces $$x \in G$$. Hay que mostrar que $$x(N \cap H)x ^{-1} \subseteq N \cap H$$. Evidentemente, $$x(N \cap H)x ^{-1} \subseteq H$$. Como $$N \triangleleft G$$, entonces $$x(N \cap H)x ^{-1} \subseteq x N x ^{-1} \subseteq N$$. Así, $$x(N \cap H)x ^{-1} \subseteq N \cap H$$ y probamos normalidad de $$N \cap H$$.
La prueba de $$NH\leq G$$ se deja como ejercicio.
Finalmente, defina $$f:H \to G / N$$ tal que $$h \mapsto h N$$. Note que $$f$$ es un homomorfismo, pues $$f(g \cdot h) = g h N = (gN)(hN) = f(g) \cdot f(h)$$. Además,

$$
h \in \operatorname{Ker}(f) \iff f(h) = N \iff hN =N \iff h \in N,
$$

por lo que $$\operatorname{Ker}(f) = N \cap H$$. Finalmente, probamos que $$\operatorname{Im}(f) = NH /N$$. Sea $$gN \in \operatorname{Im}(f)$$. Luego, existe $$h \in H$$ tal que $$hN = gN$$. Luego, $$g \in HN = NH$$, entonces $$gN \in NH / N$$. Ahora, sea $$g \in HN / N$$. Entonces, existe $$x \in HN$$ tal que $$g = xN \in HN / N$$. Luego, $$x = h_{1} n_{1}$$, con $$h_{1} \in H$$, $$n_{1} \in N$$. Así,

$$
g = xN = (h_{1} \cdot n_{1})N = h_{1} N,
$$

entonces $$g = f(h_{1}) \in \operatorname{Im}(f)$$. El resultado se sigue al aplicar el primer teorema del isomorfismo.

### Ejercicio (Imagen inversa de un subgrupo)

Si $$f:G \to G^{\ast}$$ es un homomorfismo y $$S^{\ast}\leq G^{\ast}$$. Entonces $$f^{-1}(S^{\ast}) = \{ x \in G  : f(x)\in S^{\ast} \}$$

### Teorema (Correspondencia)

Sea $$(G, \cdot)$$ un grupo, $$H \triangleleft G$$ y $$p:G \to G / H$$ tal que $$p(g)=gH$$. Entonces $$K \mapsto p(K) = K / H$$ es una biyección entre los subgrupos de $$G$$ que contienen a $$H$$ y los subgrupos de $$G/H$$. Además, si $$K$$ es tal que $$H\leq K\leq G$$ y $$K^{\ast}:=K / H$$, tenemos que

1. $$L\leq K \iff L^{\ast} \leq K^{\ast}$$ y en este caso $$[K:L] =[K^{\ast}:L^{\ast}]$$.
2. $$L \triangleleft K \iff L^{\ast} \triangleleft K^{\ast}$$, y en este caso, $$K / L \cong K^{\ast} / L^{\ast}$$.

***Prueba:*** Sean $$A = \{ L: H\leq L \leq G \}$$ y $$B = \{ \tilde{G}: \tilde{G} \leq G / H \}$$. Defina $$\Phi:A \to B$$ tal que $$\Phi(L) = L / H$$. Suponga que $$L,K \in A$$ y $$L / H = K /H$$. Probaremos que $$L = K$$. Sea $$\ell \in L$$. Entonces, $$\ell H \in L / H$$, i.e., existe $$k \in K$$ tal que $$\ell H = k H$$. Así, $$\ell ^{-1} k \in H \subseteq K$$. Como $$k \in K$$ y $$\ell^{-1}k \in K$$, tenemos $$\ell = k \cdot (\ell^{-1}k)^{-1} \in K$$, de donde $$L \subseteq K$$. La otra inclusión es igual. Luego $$\Phi$$ es inyectiva. Ahora, sea $$C \in B$$, i.e, $$C \leq G / H$$. Sea $$K = p ^{-1}(C) \leq G$$ y $$\operatorname{Ker}(p) \subseteq K$$. Entonces, $$H \subseteq K$$. Así, $$\Phi(K)=C$$. Concluya que que $$\Phi$$ es una biyección. Probaremos ahora los puntos 1 y 2:

1. Es claro que $$L \leq K \iff L ^\ast \leq K^{\ast}$$. Para probar que los indices coinciden, basta probar que existe una biyección entre las coclases de $$K/L$$ y $$K^\ast/L^{\ast}$$. Sea $$f:K/L \to K^{\ast}/L^{\ast}$$ tal que $$kL \mapsto p(k)L^{\ast} = kH (L / H)$$.

    - **Bien-definición de $$f$$**: Si $$k_{1}, k_{2} \in K$$ son tales que $$k_{1}L = k_{2}L$$, entonces $$k_{2}^{-1} k_{1} \in L$$ y en consecuencia $$k_{2}^{-1} k_{1} H \in L/H = L^{\ast}$$, lo que implica que $$f(k_{1}L) = p(k_{1}) L^\ast = p(k_{2}) L^{\ast} = f(k_{2}L)$$, y por tanto, $$f$$ está bien definida.
    - **Inyectividad de $$f$$**: Sean $$k_{1}, k_{2} \in K$$ tales que $$f(k_{1}L) = f(k_{2}L)$$. Note que $$f$$ es inyectiva, pues

        $$
        \begin{aligned}
        p(k_{1})L^{\ast} = p(k_{2}) L^{\ast} &\implies p(k_{2})^{-1} \ast p(k_{1}) \in L^{\ast} \implies p(k_{2}^{-1} k_{1}) \in L^\ast = L/H \\
        k_{2}^{-1} k_{1} H \in L / H &\implies k_{2}^{-1} k_{1} \in L \implies k_{1}L = k_{2}L,
        \end{aligned}
        $$
    - **Sobreyectividad de $$f$$**: Esto se sigue directamente de la sobreyectividad de $$p$$.
        Así, $$[K:L] = [K^{\ast}:L^{\ast}]$$.
2. El isomorfismo entre $$K/L$$ y $$K^{\ast}/L^{\ast}$$ se sigue del tercer teorema del isomorfismo.
{% endraw %}
