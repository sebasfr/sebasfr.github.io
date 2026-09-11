---
layout: chapter
course: ma0561
chapter: 9
title: "Grupo cociente"
slug: 09-grupo-cociente
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/09-grupo-cociente/
---

{% raw %}
## Grupo cociente

### Proposición (Grupos normales y operaciones)

Si $$H \triangleleft G$$ y $$a,b \in G$$, entonces $$aH \cdot bH = (a \ast b) H$$

***Prueba:*** Note que

$$
\begin{aligned}
aH \cdot bH
\end{aligned} = aH \cdot Hb = a Hb = a b H = (a \ast b) H.
$$

### Teorema (Existencia del grupo cociente)

Sea $$H \triangleleft G$$. Entonces $$G / H$$ es un grupo bajo la operación $$\cdot$$

$$
a H \cdot bH = (a \ast b) H.
$$

***Prueba:*** La operación está bien definida y es asociativa (véase proposición anterior).

1. Pertenencia de la identidad: $$1_{G} \cdot H = H$$
2. Existencia de inversos: $$aH \cdot a^{-1}H = (a \ast a^{-1}) H = H = id_{G / H }$$.

### Nota (Independencia del representante)

¿Por qué no depende del representante? Suponga que $$aH = \hat{a}H$$ y $$bH = \hat{b}H$$. Entonces

$$
aH \cdot bH = \hat{a} H \cdot \hat{b}H \iff (a \ast b) H = (\hat{a} \ast \hat{b}) H \iff (a \ast b) \ast (\hat{ a} \ast \hat{b})^{-1} \in H,
$$

que es claramente cierto.

### Teorema (Todo subgrupo normal es kernel de un homomorfismo)

Sea $$H \triangleleft G$$ y considere $$f:G\to G / H$$ tal que $$f(a) = a H$$. Entonces $$f$$ es un epimorfismo y $$\operatorname{Ker}(f) = H$$.

***Prueba:*** Probaremos primero que $$f$$ es un homomorfismo. Note que $$f(a \ast b) = (a \ast b) H = aH \cdot bH = f(a) \cdot f(b)$$. La sobreyectividad se sigue por la definición. Ahora, si $$x \in H$$, entonces $$f(x) = xH = H =id_{G / H}$$, luego, $$x \in \operatorname{Ker} f$$. Si $$x \in \operatorname{Ker} f$$, entonces $$f(x) = xH = H$$, luego $$x \in H$$.

### Ejemplo (Cocientes triviales)

1. Note que $$\{ 1_{G} \} \triangleleft G \implies G / \{ 1_{G} \} = \{ a \cdot \{ 1_{G}: a \in G \} \} = \{ \{ a \}: a \in G \} \cong G$$.
2. $$G \triangleleft G \implies G / G = \{ a \cdot G: a \in G \} = \{ G \} = \{ 1_{G / G} \}$$.

### Ejemplo (Cocientes en $$\mathbb{Z}$$ y en grupo cíclico)

1. Sea $$G = (\mathbb{Z}, + )$$, $$H = 4\mathbb{Z}$$. Note que $$H \triangleleft G$$ pues $$G$$ es abeliano. Note que $$G / H \cong \mathbb{Z}_{4}$$, pues $$aH = bH \iff a + (-b) \in 4\mathbb{Z} \iff 4 \mid a-b \iff a \cong b  \quad \text{mod }4$$.
2. Sea $$G$$ un grupo y sea $$a \in G$$ tal que $$\lvert a \rvert = 8$$. y $$G=\langle a \rangle$$. Sea $$H = \langle a^{4}. \rangle$$ Como $$G$$ es conmutativo. $$H \triangleleft G$$. Tenemos que $$H = \{ 1_{G, }a^{4} \}$$ y $$G = \{ 1_{G}, a, a^{2},\dots,a^{7} \}$$. ¿Quién es $$G/H$$? Encontremos las coclases:

    1. $$H = a^{4}H$$
    2. $$aH = \{ a, a^{5} \} = a^{5} H$$
    3. $$a^{2}H = \{ a^{2}, a^{6} \} = a^{6}H$$
    4. $$a^{3}H = \{ a^{3},a^{7} \}= a^{7}H$$
        Así, $$G/H = \{ H, aH, a^{2}H, a^{3}H \}$$ y $$G = H  \hspace{2mm}  \dot{\cup} \hspace{2mm} aH \hspace{2mm} \dot{\cup} \hspace{2mm} a^{2}H \hspace{2mm}\dot{\cup} \hspace{2mm} a^{3}H$$.

### Definición (Conmutador y subgrupo conmutador)

Sea $$(G,\ast)$$ un grupo. Sean $$a,b \in G$$. Defina el conmutador de $$a,b$$ como

$$
[a,b] = a \ast b \ast a^{-1} \ast b ^{-1} \in G
$$

Defina el subgrupo conmutador de $$G$$ como $$G':=  \langle [a,b]:a,b \in G \rangle$$.

### Ejercicio (Caracterización via conjugación)

Sea $$S < G$$. Entonces $$S \triangleleft G$$ si y solo si $$C_{a}(S) \leq S$$ para todo $$a \in G$$.

### Teorema (Subgrupo conmutador y cocientes abelianos)

Sea $$G$$ un grupo y $$G'$$ su subgrupo conmutador. Entonces $$G' \triangleleft G$$. Además, si $$H \triangleleft G$$, entonces $$G/H$$ es abeliano si y solo si $$G' \triangleleft H$$.

***Prueba:*** Hay que probar que, para todo $$g \in G$$, $$gG'g^{-1} \subseteq G'$$. Basta mostrar que si $$a, b \in G$$, $$g \in G$$ , entonces $$g[a,b]g^{-1} \in G'$$, ¿por qué? Si $$z = [a_{1} , b_{1}] [a_{2}, b_{2}]$$, entonces

$$
gzg^{-1} = g [a_{1},b_{1}] [a_{2}, b_{2}] g^{-1} = (g[a_{1},b_{1}]g^{-1})(g [a_{2},b_{2}] g^{-1}),
$$

luego, basta probar el resultado para cualquier conmutador y se sigue inmediatamente para todo $$z \in G'$$, Sea $$[a,b] \in G'$$. Entonces,

$$
\begin{aligned}
g \ast a \ast b \ast a^{-1} \ast b^{-1} \ast g^{-1}
\end{aligned}
$$

$$
= (g \ast a \ast g^{-1}) \ast (g \ast b \ast g^{-1}) \ast(g \ast a^{-1} \ast g ^{-1}) \ast (g \ast b ^{-1} \ast g ^{-1}) = [g \ast a \ast g ^{-1},g \ast b \ast g ^{-1} ]\in G'.
$$

Suponga ahora que $$G/H$$ es abeliano. Entonces para todos $$a,b \in G$$, $$aH \cdot b H = b H \cdot a H$$, por lo que $$(a \ast b) H = (b \ast a)H$$. Luego , $$(a \ast b) \ast (b \ast a) ^{-1} = a \ast b \ast a^{-1} \ast b ^{-1} = [a,b] \in H$$. Así, $$\{ [a,b]: a,b \in G \} \subseteq H \implies G' \subseteq H \implies G' \leq H$$. (Escribir la otra dirección).

### Ejemplo ($$A_3 \triangleleft S_3$$)

Considere $$S_{3} = \{ (1),\begin{pmatrix}1 & 2\end{pmatrix}, \begin{pmatrix}2 & 3\end{pmatrix}, \begin{pmatrix}1 & 3\end{pmatrix}, \begin{pmatrix}1 & 2 & 3\end{pmatrix} \begin{pmatrix}3 & 2 & 1\end{pmatrix} \}$$ y $$A_{3} = \{ \sigma \in S_{3}: \sigma \text{ es par} \} = \{ \begin{pmatrix}1\end{pmatrix}, \begin{pmatrix}1 & 2 & 3\end{pmatrix}, \begin{pmatrix}3 & 2 & 1\end{pmatrix}\}$$. Probaremos que $$A_{3} \triangleleft S_{3}$$. Considere $$S = \{ -1,1 \}$$. Note que $$(S, \cdot) = (\mathbb{Z}_{2}, +)$$. Sea $$f:S_{3} \to S$$ tal que $$\sigma \mapsto \operatorname{sgn}( \sigma )$$. Note que $$f$$ es un homomorfismo, pues

$$
\begin{aligned}
f(\sigma_{1} \circ \sigma_{2}) &= \operatorname{sgn}(\sigma_{1} \circ \sigma_{2}  )\\
&= \operatorname{sgn}( \sigma_{1} ) \cdot \operatorname{sgn}( \sigma_{2} )\\
&= f(\sigma_{1}) \cdot f(\sigma_{2}).
\end{aligned}
$$

Note que $$\operatorname{Ker} f = A_{3}$$, de donde concluimos que $$A_{3} \triangleleft S_{3}$$. ¿Quién es $$S_{3}/A_{3}$$? Construyamos las coclases

1. $$A_{3}$$
2. $$\begin{pmatrix}1 & 2\end{pmatrix} A_{3} = \{ \begin{pmatrix}1 & 2\end{pmatrix}, \begin{pmatrix}3 & 2\end{pmatrix}, \begin{pmatrix}1 & 3\end{pmatrix} \}$$.

Así, $$S_{3}/A_{3} = \{ A_{3}, \begin{pmatrix}1&2\end{pmatrix}A_{3} \} \cong \mathbb{Z}_{2}$$.

### Ejemplo ($$\langle r_1\rangle \triangleleft D_4$$)

Considere $$D_{4} = \{ r_{0},r_{1},r_{2},r_{3},s_{1},s_{2},s_{3},s_{4} \}$$ el grupo de simetrías del cuadrado y $$H = \langle r_{1} \rangle = \{ r_{0},r_{1},r_{2},r_{3} \}$$. Debemos probar que para todo $$i \in \{ 1,\dots,4 \}$$, $$s_{i} H s_{i} ^{-1} \subseteq H$$. Note en primer lugar que para todo $$i$$, $$s_{i}^{2} = r_{0}$$, luego, $$s_{i} = s_{i}^{-1}$$. Luego, hay que probar que para todos $$j \in \{ 0,1,2,3 \}, i \in\{ 1,2,3,4 \}$$, $$s_{i} r_{j} s_{i} ^{-1} \in H$$
{% endraw %}
