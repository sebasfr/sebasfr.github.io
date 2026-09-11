---
layout: chapter
course: ma0561
chapter: 7
title: "Coclases"
slug: 07-coclases
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/07-coclases/
---

{% raw %}
## Coclases

### Definición (Coclases)

Sea $$G$$ un grupo y $$H \leq G$$:

1. Una coclase izquierda (derecha) de $$H$$ es $$aH = \{ a \ast h:h \in H \}$$ ($$Ha = \{ h \ast a:h \in H \}$$), con $$a \in G$$.

Se suele escribir "$$a+H$$" o "$$H+a$$" en grupos aditivos.

### Ejemplos (Coclases en $$\mathbb{Z}$$ y $$S_3$$)

1. Considere $$G = (\mathbb{Z}, +)$$ y sea $$n \in \mathbb{Z}$$. Tome $$H = \langle n \rangle = n \mathbb{Z}$$. Sea $$a \in \mathbb{Z}$$. Note que

    $$
    \begin{aligned}
    a + H &= \{ a+h:h \in H \} \\
    &=\{ a + nk: k \in \mathbb{Z} \} \\
    &=\{ t: t \equiv a  \quad \mathrm{mod } \hspace{2mm}n \}.
    \end{aligned}
    $$
2. Considere $$G = S_{3}$$ y $$\tau = \begin{pmatrix}1 & 2\end{pmatrix}$$. Tome $$H = \langle \tau \rangle = \{ \mathrm{id}, \tau \}$$. Tenemos que

    $$
    \begin{aligned}
    H \cdot \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix} &= \{ \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix}, \begin{pmatrix}
    1 & 2
    \end{pmatrix} \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix} \} \\
    &=\{ \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix}, \begin{pmatrix}
    2 & 3
    \end{pmatrix} \},\\
    \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix} \cdot H &= \{ \begin{pmatrix}
    1 & 2 & 3
    \end{pmatrix}, \begin{pmatrix}
    3 & 1
    \end{pmatrix} \},\\
    H \cdot \begin{pmatrix}
    3 & 2 & 1
    \end{pmatrix} &= \{ \begin{pmatrix}
    3 & 2 & 1
    \end{pmatrix}, \begin{pmatrix}
    1 & 3
    \end{pmatrix} \}
    \end{aligned}
    $$

Note que $$H \cdot \begin{pmatrix}3 & 2 & 1\end{pmatrix} \quad \cap \quad H \ast \begin{pmatrix}1 & 2 & 3\end{pmatrix} = \emptyset$$.

### Lema (Criterio de igualdad de coclases)

Sea $$H \leq G$$ y $$a,b \in G$$. Entonces

$$
aH = bH \iff (b^{-1} \ast a) \in H.
$$

***Prueba:*** ($$\implies$$): Tenemos que $$a \in bH$$. Luego, existe $$h \in H$$ tal que $$a = b \ast h \implies b^{-1} \ast a = h \in H$$.
($$\impliedby$$): Suponga que $$b ^{-1} \ast a \in H$$. Luego, existe $$h_{0} \in H$$ tal que $$b ^{-1} \ast a = h_{0}$$. Entonces $$a = b \ast h_{0}$$, entonces $$a \in bH$$. Luego, $$aH \subseteq bH$$, pues si $$x \in aH$$, tenemos que

$$
x = a \ast h = b \ast\underbrace{ h_{0} \ast h }_{ \in H }\in bH
$$

La otra inclusión se prueba de manera análoga.

### Teorema (Dos cualesquiera coclases son iguales o disjuntas)

Sea $$H\leq G$$ y sean $$a,b \in G$$. Entonces $$aH = bH$$ o $$aH \cap bH = \emptyset$$.

***Prueba:*** Suponga que $$aH \cap bH \neq \emptyset$$. Sea $$x \in aH \cap bH$$. Luego, existen $$h_{1}, h_{2} \in H$$ tal que $$x= a \ast h_{1} = b \ast h_{2}$$. Entonces, $$b^{-1} \ast x = b^{-1} \ast a \ast h_{1} \in H$$ , de modo que $$b ^{-1} \ast a \in H$$. Por el lema anterior $$aH = bH$$., de donde concluimos el resultado.

### Nota (Coclases como partición)

Esto nos muestra que las coclases forman una partición del grupo. Más aún, si definimos la relación $$\sim$$ en $$G$$ como $$a \sim b \iff aH = bH$$, esta es una relación de equivalencia.

### Definición (Conjunto cociente)

Definimos el conjunto cociente de $$G$$ sobre $$H$$ como $$G/H := \{ aH:a \in G \}$$, esto es, el conjunto de representantes de $$G$$ cocientado con la clase de equivalencia de coclases de $$H$$.

### Teorema (Igualdad del número de coclases izquierdas/derechas)

Sea $$H\leq G$$. Entonces el número de coclases derechas es igual al número de coclases izquierdas.

***Prueba:*** Sean $$A = \{ aH: a \in G \}$$ y $$B = \{ Hb:b \in G \}$$. Sea $$f:A\to B$$ tal que $$f(aH) = Ha^{-1}$$. $$f$$ está bien definida: Si $$aH = a'H$$, entonces $$H a^{-1} = H(a')^{-1}$$. Terminar la prueba (ejercicio).

### Proposición (Cardinalidad de subgrupo y coclases)

Si $$H\leq G$$ y $$a \in G$$, entonces $$\lvert a H \rvert = \lvert H \rvert$$ (como cardinalidad pues $$aH$$ no es necesariamente un grupo)

***Prueba:*** Defina $$f:H\to aH$$ tal que $$h \mapsto a \ast h$$. Note que

$$
\begin{aligned}
f(h_{1}) = f(h_{2}) \implies a \ast h_{1} = a \ast h_{2} \implies a^{-1} \ast a \ast h_{1} = a^{-1} \ast a \ast h_{2} \implies h_{1}=h_{2}.
\end{aligned}
$$

### Definición (Índices)

Sea $$H \leq G$$. Definimos el índice de $$H$$ en $$G$$ como $$[G:H] = \lvert G/H \rvert$$ es el número de coclases diferentes de $$H$$ en $$G$$.

### Teorema (Lagrange para grupos finitos)

Sea $$G$$ un grupo finito y $$H\leq G$$. Entonces, $$\lvert G \rvert = [G:H] \cdot \lvert H \rvert$$. En particular, $$\lvert H \rvert \Big\lvert \lvert G \rvert$$.

***Prueba:*** Sea $$k = [G :H]$$. Sean $$a_{1}H, a_{2}H, \dots, a_{k}H$$ las coclases diferentes de $$H$$ en $$G$$. Entonces $$G = \bigcup_{i=1}^{k} a_{i} H$$. Como $$a_{1}H, a_{2}H, \dots, a_{k}H$$ son disjuntos, entonces $$\lvert G \rvert = \sum_{i=1}^{k} \lvert a_{i} H \rvert = k \lvert H \rvert$$.

### Corolario (Orden de un elemento divide al orden del grupo)

Sea $$a \in G$$. Entonces $$\lvert a \rvert \Big\lvert \lvert G \rvert$$.

***Prueba:*** Tome $$H = \langle a \rangle$$. Entonces $$\lvert H \rvert = \lvert a \rvert$$ y el resultado se sigue del teorema de Lagrange.

### Corolario (Multiplicatividad del índice)

Sean $$K,H,G$$ grupos tales que $$K \leq H\leq G$$. Entonces, $$[G:K] = [G:H] [H:K]$$.

***Prueba:*** Aplicando el teorema de Lagrange sobre los tres índices:

$$
[G:H] \cdot \lvert H \rvert = \lvert G \rvert, \quad [H:K] \cdot \lvert K \rvert = \lvert H \rvert, \quad [G:H] \cdot [H : K] = \lvert G \rvert.
$$

Así,

$$
[G:H] \cdot [H:K] = \frac{\lvert G \rvert}{\lvert H \rvert } \cdot \frac{\lvert H \rvert}{\lvert K \rvert }  = \frac{\lvert G \rvert}{\lvert K \rvert } = [G:K].
$$

### Proposición (Coclases sobre el kernel de un homomorfismo)

Sean $$G, G'$$ y $$f:G \to G'$$ un homomorfismo. Sea $$H = \operatorname{Ker}(f) \leq G$$. Sea $$a \in G$$ y $$a' = f(a)$$. Entonces $$aH = \{ x \in G:f(x) = a' \}$$.

***Prueba:*** Sea $$x \in aH$$, entonces existe $$h \in H$$ tal que $$x = a \ast h$$. Luego, $$f(x) = f(a) \ast_{G'} f(h) = f(a) = a'$$. Luego, $$aH \subseteq \{ x \in G:f(x) = a' \}$$. Por otro lado, si $$x \in G$$ tal que $$f(x) = a'$$, tenemos que

$$
f(x) = f(a) \iff \big(f(a)\big)^{-1} \ast_{G'} f(x) = 1_{G'} \iff f(a^{-1} \ast x) = 1_{G'},
$$

de donde tenemos que $$a^{-1} \ast x \in H$$ y, por el criterio de igualdad de coclases, $$xH = aH$$, de donde $$x \in aH$$. Así, $$\{ x \in G: f(x) = a' \} \subseteq aH$$, y por tanto $$aH \subseteq \{ x \in G:f(x) = a' \}$$.
{% endraw %}
