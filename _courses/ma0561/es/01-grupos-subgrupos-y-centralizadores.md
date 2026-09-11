---
layout: chapter
course: ma0561
chapter: 1
title: "Grupos, subgrupos y centralizadores"
slug: 01-grupos-subgrupos-y-centralizadores
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/01-grupos-subgrupos-y-centralizadores/
---

{% raw %}
## Definiciones elementales

### Definición (Operación binaria)

Sea $$G$$ un conjunto no vacío. Una operación binaria es una aplicación $$G \times G \to G$$ con $$(g_{1},g_{2}) \mapsto g_{3}$$.

### Definición (Grupo)

Un grupo $$G$$ es un conjunto no vacío junto con una operación binaria $$\ast: G \times G \to G$$ tal que:

1. $$\ast$$ es asociativa:

    $$
    \forall g_{1},g_{2},g_{3} \in G \quad  (g_{1} \ast g_{2}) \ast g_{3} = g_{1} \ast (g_{2} \ast g_{3});
    $$
2. existe un elemento neutro $$e \in G$$ tal que $$e \ast g = g\ast e = g$$ para todo $$g \in G$$. Muchas veces, escribimos $$1_{G}$$ para denotar el elemento neutro del grupo $$G$$;
3. existe un inverso para todo elemento, esto es,

    $$
    \forall g \in G  \quad \exists h \in G  \quad (g \ast h = h \ast g = e).
    $$

### Definición (Grupo Abeliano)

Si $$(G, \ast)$$ es un grupo que además cumple que para todos $$g_{1},g_{2} \in G$$, $$g_{1} \ast g_{2} = g_{2} \ast g_{1}$$, decimos que $$G$$ es *conmutativo* o *abeliano*.

### Definición (Monoide)

Un monoide es una estructura más general, dotada por un conjunto, una operación binaria asociativa con elemento neutro, pero en donde no necesariamente todo elemento tiene un inverso.

## Propiedades de los grupos

### Proposición (Unicidad del neutro)

Si $$e, e'$$ son dos elementos neutros, $$e' = e' \ast e = e$$.

### Proposición (Unicidad del inverso)

Sea $$g \in G$$ y sean $$h, h'$$ inversos de $$g$$. Entonces

$$
h' = e \ast h' = (h \ast g) \ast h' = h \ast (g \ast h') = h \ast e = h.
$$

### Notación (Inverso)

Si $$(G, \ast)$$ es un grupo y $$g \in G$$, denotamos por $$g^{-1}$$ al inverso de $$g$$.

### Nota (Propiedades del inverso)

1. $$(g^{-1})^{-1} = g$$ para todo $$g \in G$$
2. $$(g \ast h)^{-1} = h ^{-1} \ast g ^{-1}$$ para todos $$g,h \in G$$.

### Proposición (Leyes de cancelación)

Si $$g, h_{1}, h_{2} \in G$$, entonces

1. $$g \ast h_{1} = g \ast h_{2} \implies h_{1}=h_{2}$$,
2. $$h_{1} \ast g = h_{2} \ast g \implies h_{1} = h_{2}$$.

## Ejemplos de grupos

Algunos ejemplos son muy importantes dentro de la estructura

### Ejemplo (Grupo trivial)

Sea $$G = \{  e \}$$ tal que $$e \ast e = e$$. $$(G, \ast)$$ es un grupo y es llamado grupo trivial.

### Ejemplo (Grupos aditivos)

$$(\mathbb{Z}, + )$$ es un grupo con elemento neutro $$0$$ y en donde el inverso de $$z \in Z$$ es $$-z$$. $$(\mathbb{N}, +)$$ no es grupo pero sí es monoide, pero $$(\mathbb{N}^{\ast},+)$$ no es monoide. $$(\mathbb{R},+), (\mathbb{Q},+), (\mathbb{C}, +), (\mathbb{Z},+)$$ son todos grupos abelianos.

### Ejemplo (Grupos multiplicativos)

$$(\mathbb{R}^{\ast}, \cdot), (\mathbb{Q}^{\ast}, \cdot), (\mathbb{C}^{\ast}, \cdot)$$ son grupos abelianos con neutro $$1$$ y donde el inverso de $$x$$ es $$\frac{1}{x}$$. En general, si $$\mathbb{F}$$ es un cuerpo, $$(\mathbb{F}^{\ast}, \cdot)$$ es un grupo. $$(\mathbb{Z}^{\ast}, \cdot)$$ no es un grupo porque no todo elemento posee un inverso.

### Ejemplo (Grupos lineales)

Sea $$n \in \mathbb{N}^{\ast}$$ y $$\mathbb{F}$$ un cuerpo. Definimos

$$
GL_{n}(\mathbb{F}) = \{\text{matrices }n \times n \text{ invertibles con entradas en }\mathbb{F} \}.
$$

$$(GL_{n}(\mathbb{F}), \cdot)$$, donde $$\cdot$$ es la multiplicación estándar de matrices. A este grupo se le llama el grupo lineal sobre $$\mathbb{F}$$.

### Ejemplo (Grupos sobre congruencias)

Sea $$m>0$$ y considere $$\mathbb{Z}_{m} = \mathbb{Z}/{\equiv_{m}}$$ ($$\mathbb{Z}$$ cocientado en la relación de congruencia módulo $$m$$), i.e., $$\mathbb{Z}_{m} = \{ [0], [1],\dots, [m-1] \}$$. Defina la operación $$\hat{+}$$ en $$\mathbb{Z}_{m}$$ tal que $$[a]\hat{+}[b] = [a+b]$$ (hay que mostrar que está bien definida). $$(\mathbb{Z}_{m}, \hat{+})$$ es un grupo con elemento neutro $$[0]$$. Si $$[n] \in \mathbb{Z}_{m}$$, el inverso es $$[-n]$$. Consideremos el ejemplo con $$m=2$$.

Para $$\mathbb{Z}_{2}$$, tenemos $$\mathbb{Z}_{2} = \{ [0]. [1] \}$$. Observe la tabla de operaciones

| $$\hat{+}$$ | $$[0]$$ | $$[1]$$ |
| --- | --- | --- |
| $$[0]$$ | $$[0]$$ | $$[1]$$ |
| $$[1]$$ | $$[1]$$ | $$[0]$$ |

Definamos ahora sobre $$\mathbb{Z}_{m}^{\ast} = \mathbb{Z}_{m} \setminus \{ [0] \}$$. Definamos la operación $$\hat{\cdot}$$ como

$$
[a] \hat{\cdot} [b] = [a \cdot b]
$$

Queremos construir un grupo multiplicativo con esta nueva operación. ¿Para cuales casos de $$m$$ está esto bien definido y existen inversos? Para $$m$$ compuesto, la multiplicación no está bien definida en $$\mathbb{Z}_{m}^{\ast}$$ porque puedo tomar elementos de ciertas clases de equivalencia cuyo producto tiene resultado $$[0]$$.

Para primos, la operación está bien definidos. Sea $$n$$ primo y asuma que existen $$[a], [b] \in \mathbb{Z}_{n}^{\ast}$$ tales que $$[a] \hat{\cdot} [b] = [a \cdot b] = [0]$$. Esto implica que $$n \mid a \cdot b$$, pero como $$n$$ es primo, $$n \mid a$$ o $$n \mid b$$, de modo que $$[a] = [0]$$ o $$[b]=[0]$$, una contradicción pues $$[0] \not\in \mathbb{Z}_{n}^{\ast}$$.

Probaremos que $$(\mathbb{Z}_{n}^{\ast}, \hat{\cdot})$$ es un grupo para $$n$$ primo. Note que $$\mathbb{Z}_{n}^{\ast} = \{ [1],\dots,[n-1] \}$$. Sea $$r \in \{ 1,\dots,n-1 \}$$. Como $$n$$ es primo, tenemos que $$\operatorname{MCD}(r,n) = 1$$. Luego, existen enteros $$q,s$$ tales que $$qr+sn = 1$$. Esto implica que

$$
[q \cdot r] = [1] \implies [q] \hat{\cdot} [r] = [1].
$$

Podemos suponer que $$q \in \{ 1,\dots,n-1 \}$$, pues de lo contrario tomamos el representante de su clase de equivalencia. Así, $$[q]$$ es el inverso de $$[r]$$. Así, $$(\mathbb{Z}_{n}^{\ast}. \hat{\cdot})$$ tiene inversos para todo elemento, y por tanto es un grupo (las otras propiedades son triviales).

### Nota (Cuerpo $$\mathbb{Z}_p$$)

Es fácil verificar que si $$p$$ es primo $$(\mathbb{Z}_{p}, \hat{+}, \hat{\cdot}, [0], [1])$$ es un cuerpo.

### Ejemplo (Grupos de simetrías de un cuadrado)

Considere un cuadrado con sus vértices numerados. ¿De cuántas maneras puedo mover sus vértices para que el cuadrado siga manteniendo el mismo espacio? Puede hacer cuatro rotaciones ($$0^{\circ}, 90^{\circ}, 180^{\circ}, 270^{\circ}$$) en el sentido contrario a las agujas del reloj, ($$r_{0},r_{90},r_{180},r_{270}$$). Además, puedo hacer cuatro reflexiones: vertical ($$s_{1}$$), horizontal ($$s_{2}$$), diagonal comenzando abajo-izquierda ($$s_{3}$$) y diagonal comenzando arriba-izquierda ($$s_{4}$$).

Llamamos $$D_{4}= \{ r_{0},r_{90},r_{180},r_{270}, s_{1},s_{2},s_{3},s_{4} \}$$. Definimos una operación $$\circ$$ en $$D_{4}$$, como la "composición de movimientos", p.e., $$r_{90} \circ s_{2}$$.

### Ejercicio (Grupo diédrico $$D_4$$)

$$(D_{4},\circ)$$ es un grupo pero **no** es conmutativo.

En general $$D_{n}$$ es el grupo de simetrías de un polígono regular de $$n$$ lados. Está compuesto por $$r_{0},\dots,r_{n-1}$$ rotaciones, donde $$r_{k}$$ rota la figura en un ángulo de $$\frac{2\pi k}{n}$$ y $$s_{0}, \dots, s_{n-1}$$ son $$n$$ reflexiones sobre las líneas $$\theta = \frac{\pi k}{n}$$. $$D_{n}$$ tiene $$2n$$ elemmentos, y se le llama el grupo diédrico o grupo diedral.

### Ejemplo (Grupo de permutaciones de $$n$$ elementos)

Una permutación de $$n$$ elementos es una función biyectiva

$$
\begin{aligned}
\sigma:\{ 1,\dots,n \} &\to \{ 1,\dots,n \}, \text{ tal que} \\
1 &\mapsto \sigma(1)\\
& \quad\vdots \\
n &\mapsto \sigma(n).
\end{aligned}
$$

Definimos $$S_{n} = \{ \sigma: \sigma \text{ es una permutación de }n \text{ elementos}\}$$. $$S_{n}$$ es un grupo bajo la composición de funciones (ejercicio).

### Notación (Permutaciones)

$$\sigma: \begin{pmatrix}1 & 2 & 3 \\ 2 & 3 & 1\end{pmatrix}$$ representa $$\sigma:\{ 1,2,3 \} \to \{ 1,2,3 \}$$, con $$\sigma(1)=2, \sigma(2)=3,\sigma(3)=1$$. Su inversa es $$\sigma ^{-1}:\begin{pmatrix}1 & 2 & 3 \\ 3 & 1 & 2\end{pmatrix}$$.

### Ejemplo (Producto de grupos)

Sean $$(G_{1}, \ast_{1})$$ y $$(G_{2}, \ast_{2})$$ dos grupos. Considere el producto cartesiano $$G_{1} \times G_{2}$$. Defina la operación $$\ast$$ en $$G_{1} \times G_{2}$$ tal que

$$
(g_{1}, g_{2}) \ast (h_{1},h_{2}) := (g_{1} \ast_{1} h_{1}, g_{2} \ast_{2} h_{2}) \in G_{1} \times G_{2}.
$$

Entonces, $$(G_{1} \times G_{2}, \ast)$$ es un grupo con elemento neutro $$(1_{G_{1}}, 1_{G_{2}})$$. Si $$(g_{1},g_{2}) \in G_{1} \times G_{2}$$, entonces $$(g_{1}, g_{2})^{-1} = (g_{1}^{-1}, g_{2}^{-1})$$. Se puede generalizar para el producto de $$n$$ grupos.

## Operaciones iteradas en grupos

Si $$(G, \ast)$$ es un grupo denotamos por $$g^{n} = \underbrace{ g \ast g \ast \dots \ast g }_{ n \text{ veces} }$$,, $$g^{0} = 1_{G}$$, $$g^{-n}:= (g^{-1})^{n}$$.

### Proposición (Propiedades de la potenciación)

Sea $$(G, \ast)$$ un grupo, $$g,h \in G$$. Entonces

1. $$g^{-n} = (g^{n}) ^{-1}$$
2. $$g^{n+m} = g^{n} \ast g^{m}$$
3. Si $$g \ast h = h \ast g$$, entonces $$(g \ast h)^{m} = g^{m} \ast h^{m}$$.

## Subgrupos

Sea $$(G, \ast)$$ un grupo y $$H \subseteq G$$. Decimos que $$H$$ es un subgrupo de $$G$$ si $$(H, \ast \mid_{H})$$ es un grupo. En ese caso escribirnos $$H \leq G$$

### Nota (Verificación de subgrupo)

Para verificar que $$H \leq G$$, basta ver (1) que $$h_{1}\ast h_{2} \in H  \quad \forall h_{1}, h_{2} \in H$$, (2) que $$1_{G} \in H$$ y que (3), si $$h \in H$$ entonces $$h^{-1} \in H$$.

### Teorema (Caracterización de subgrupo)

Se $$\emptyset \neq H \subseteq G$$. Entonces $$H \leq G$$ si y solo si

$$
\forall x,y \in H  \quad (x \ast y^{-1} \in H).
$$

***Prueba:*** $$(\implies)$$ es trivial. Probemos $$(\impliedby)$$. Si $$x \in H$$, entonces $$x \ast x ^{-1} = 1_{G}  \in H$$. Por otro lado, como $$1_{G} \in H$$, $$1_{G} \ast x^{-1} = x^{-1} \in H$$. Finalmente, si $$x,y \in H$$, como $$y^{-1} \in H$$, entonces $$x \ast (y ^{-1}) ^{-1} = x \ast y \in H$$. Por tanto, $$H$$ es subgrupo.

### Lema (Intersección de subgrupos es subgrupo)

Sea $$(G, \ast)$$ y sea $$\{ H_{i}:i \in I \}$$ una familia de subgrupos de $$G$$. Entonces $$H:=\bigcap_{i \in I} H_{i} \leq G_{i}$$.

***Prueba:*** Note que $$H\neq \emptyset$$, pues $$1_{G} \in H_{i}$$ para todo $$i$$. Sea $$x,y \in H$$. Como $$x,y \in H_{i}$$ para todo $$i \in I$$. Entonces $$x \ast y^{-1} \in H_{i}$$ para todo $$i$$. Luego, $$x \ast y ^{-1} \in H$$.

### Definición (Grupo generado por un subconjunto)

Sea $$(G, \ast)$$ un grupo y $$S \subseteq G$$. Defina

$$
\langle S \rangle := \bigcap \{ H:H\leq G  \quad \land  \quad S \subseteq H\}
$$

como el grupo generado por $$S$$.

### Teorema (Generado es el grupo más pequeño que contiene al conjunto)

$$\langle S \rangle$$ es el grupo más pequeño que contiene a $$S$$, i.e., si $$K\leq G$$ tal que $$S \subseteq K$$, entonces $$\langle S \rangle \subseteq K$$.

***Prueba:*** Si $$K \leq G$$ y $$S \subseteq K$$, entonces $$K \in \{ H \leq G : S \subseteq H \}$$, por lo que $$\bigcap \{ H:H\leq G  \quad \land  \quad S \subseteq H\} = \langle S \rangle \subseteq K$$.

### Teorema (Caracterización del grupo generado)

Si $$(G, \ast)$$ es un grupo y $$S \neq \emptyset$$, entonces

$$
\langle S \rangle = \{ x_{1}^{\alpha_{1}} \ast \dots \ast x_{n}^{\alpha_{n}}: n \in \mathbb{N}^{\ast}, x_{i} \in S, \alpha_{i} \in \{ -1,1\} \}.
$$

***Prueba:*** Sea $$H = \{ x_{1}^{\alpha_{1}} \ast \dots \ast x_{n}^{\alpha_{n}}: n \in \mathbb{N}^{\ast}, x_{i} \in S, \alpha_{i} \in \{ -1,1\} \}$$. Note que $$H \neq \emptyset$$. Sean $$x,y \in H$$. Entonces existen $$k, \ell \in \mathbb{N}^{\ast}; \{ \alpha_{i} \}_{i=1}^{k}, \{ \beta_{i} \}_{i=1}^{\ell}$$ con $$\alpha_{i}, \beta_{i} \in \{ -1,1 \}$$ para todo $$i$$, y $$x_{1},\dots,x_{k},y_{1},\dots y_{\ell} \in S$$ tales que

$$
x = x_{1}^{\alpha_{1}} \ast \dots \ast x_{k}^{\alpha_{k}}, y = y_{1}^{\beta_{1}}\dots y_{\ell}^{\beta_{\ell}}.
$$

Note que $$x \ast y^{-1} = x_{1}^{\alpha_{1}} \ast \dots \ast x_{k}^{\alpha_{k}} \ast y_{1}^{-\beta_{1}}\dots y_{\ell}^{\beta_{-\ell}} \in H$$. Así, $$H \leq G$$ y por tanto $$\langle S \rangle \subseteq H$$.
Por otro lado, como $$\langle S \rangle$$ es un grupo, $$H \subseteq \langle S \rangle$$.

### Definición (Grupo generado)

SI $$(G, \ast)$$ es un grupo y $$S \subseteq G$$ tal que $$\langle S \rangle = G$$, decimos que $$G$$ es generado por $$S$$. Si $$S$$ es finito, decimos que $$G$$ es finitamente generado.

### Ejemplos (de grupos generados)

1. Sea $$(G, \ast)$$ un grupo. Entonces

    $$
    \begin{aligned}
    \langle \emptyset \rangle &= \bigcap \{ H: H\leq  G \} \\
    &= \{ 1_{G} \}.
    \end{aligned}
    $$
2. Si $$(G, \ast)$$ es un grupo y $$S \leq G$$, $$\langle S \rangle = \langle S \rangle$$.
3. Si $$S = \{ i \} \subseteq (\mathbb{C}^{\ast}, \cdot)$$, entonces $$\langle S \rangle = \{ i,-1,1,-i \}$$.
4. Si $$S = \{ 2 \} \subseteq (\mathbb{Z},+)$$, $$\langle S \rangle = \{ 2k:k \in \mathbb{Z} \}$$.
5. Si $$S=\{ 12,-8 \} \subseteq (\mathbb{Z}, +)$$, entonces $$\langle S \rangle = \{ 12 a + (-8)b: a,b \in \mathbb{Z} \} = \{ 4k: k \in \mathbb{Z} \}$$ .
6. En general, si $$a \in (G, \ast)$$,

    $$
    \begin{aligned}
    \langle a \rangle &= \bigcap \{ H: H<a  \quad\land  \quad a \in H \}\\
    &= \{ a^{n}: n \in \mathbb{Z} \}.
    \end{aligned}
    $$

## Centro y centralizador

### Definición (centro de $$G$$)

Sea $$(G, \ast)$$ un grupo. Defina

$$
Z(G) = \{ g \in G: \forall h \in G (gh = hg)\}
$$

### Nota (Propiedades del centro)

1. $$e \in Z(G)$$,
2. $$G$$ es abeliano si y solo si $$Z(G) = G$$.
3. Si $$g \in Z(G)$$, entonces para todo $$h \in G$$, $$h = g \ast h \ast g^{-1}$$.

### Teorema (Centro es subgrupo)

Si $$G$$ es un grupo, entonces $$Z(G) \leq G$$ y $$Z(G)$$ es conmutativo.

### Definición (Centralizador)

Sea $$G$$ un grupo y $$a \in G$$. Defina el centralizador como

$$
C(a):= \{ g \in G: a \ast g = g \ast a \}
$$

### Ejercicio (Centralizador es subgrupo)

$$C(a) \leq G$$.

Se puede probar que $$Z(G) = \bigcap_{a \in G} C(a)$$.
{% endraw %}
