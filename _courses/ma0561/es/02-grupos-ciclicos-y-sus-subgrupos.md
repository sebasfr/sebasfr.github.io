---
layout: chapter
course: ma0561
chapter: 2
title: "Grupos cíclicos y sus subgrupos"
slug: 02-grupos-ciclicos-y-sus-subgrupos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/02-grupos-ciclicos-y-sus-subgrupos/
---

{% raw %}
## Grupos cíclicos

### Definición (Orden de un grupo y de un elemento)

Sea $$(G, \ast)$$ un grupo. El orden de $$G$$ es la cantidad de elementos de $$G$$ y se denota por $$\lvert  G \rvert$$.

1. Si existe $$p$$ primo tal que tal que $$\lvert  G \rvert = p^{k}$$ con $$k \in \mathbb{N}$$. decimos que $$G$$ es un $$p$$-grupo.
2. Si $$G$$ es un grupo y $$g \in G$$. el orden de $$g$$ ($$\lvert  g \rvert$$) es el menor $$n \in \mathbb{N}$$ tal que $$g^{n} = 1_{G}$$. Si tal $$n$$ no extiste, decimos que tal $$\lvert g \rvert = \infty$$.

### Ejemplos (Órdenes en $$\mathbb{Z}_n$$)

1. $$(\mathbb{Z}_{n}, +) = \{ [0],[1],\dots,[n-1] \}$$, $$\lvert \mathbb{Z}_{n} \rvert = n$$.
2. Considere $$(\mathbb{Z}_{4}, +) = \{ [0], [1], [2], [3] \}$$, $$\lvert \mathbb{Z}_{4} \rvert = 4$$. Note que

    $$
    [2] \neq [0] \quad \land  \quad [2]+[2] = [0],
    $$

por lo que $$\lvert [2] \rvert = 2$$. De la misma manera, verificamos que $$\lvert [1] \rvert = 4$$ y $$\langle [1] \rangle = \mathbb{Z}_{4}$$.

### Teorema (Orden y divisibilidad)

Sea $$G$$ un grupo y $$g \in G$$, $$n \in \mathbb{Z}$$. Entonces

$$
g^{n} = 1_{G} \iff \lvert g \rvert \mid n.
$$

***Prueba:*** Hagamos el caso de $$n \in \mathbb{N}$$.
($$\impliedby$$): Si $$\lvert g \rvert \mid n$$, existe $$k \in \mathbb{N}$$ tal que $$k \lvert g \rvert = n$$. Entonces

$$
g^{n} = g^{k \lvert  g \rvert } = (g^{\lvert g \rvert })^{k} = (1_{G})^{k} = 1_{G}.
$$

$$(\implies)$$: Suponga que $$g^{n} = 1_{G}$$. Por minimalidad, $$\lvert g \rvert \leq n$$. Por algoritmo de la división, existen $$q,r \in \mathbb{N}$$ tales que $$n = q \lvert g \rvert + r$$ y $$0 \leq r < \lvert g \rvert$$. Entonces,

$$
1_{G} = g^{n} =g^{q \lvert g \rvert} \ast g^{r} = 1_{G} \ast g^{r} = g^{r},
$$

de donde concluimos que $$r = 0$$ por minimalidad de $$\lvert g \rvert$$, por tanto $$\lvert g \rvert \mid n$$.

Para el caso general $$n \in \mathbb{Z}$$, basta ver que $$g^{n} = 1_{G} \iff g^{-n} = 1_{G}$$ y además $$\lvert  g \rvert \mid n \iff \lvert g \rvert \mid -n$$.

### Definición (Grupo cíclico)

Sea $$G$$ un grupo. $$G$$ es cíclico si existe $$g \in G$$ tal que $$G = \langle g \rangle$$.

### Ejemplo (Grupos cíclicos)

1. $$(\mathbb{Z}, +) = \langle 1 \rangle = \langle -1 \rangle$$. Tenemos que $$\lvert \mathbb{Z} \rvert = \infty, \lvert 1 \rvert = \infty, \lvert 2 \rvert = \infty$$.
2. Considere $$\mathbb{Z}_{5}$$ con la multiplicación de clases de equivalencia (congruencia módulo 5) definida anteriormente. Definimos

    $$
    U(5) = \{ [x] \in \mathbb{Z}_{5}: \exists [y] \in \mathbb{Z}_{5}([x] \cdot [y]=[1]) \} = \mathbb{Z}^{\ast}_{5}
    $$

¿$$U(5)$$ es un grupo cíclico? Sí, por ejemplo, $$\lvert [2] \rvert = 4$$. De la misma manera, su inverso $$[3]$$ también funciona para generar a $$U(5)$$. Pero $$[4]$$ no. Así, $$\langle [2] \rangle, \langle [3] \rangle$$.

### Definición (Unidades de $$\mathbb{Z}_{m}$$)

Considere $$\mathbb{Z}_{m}$$. Defina

$$
U(m) = \{ [x] \in \mathbb{Z}_{m}: \exists [y] \in \mathbb{Z}_{m}([x] \cdot [y] = [1]) \}.
$$

Decimos que $$[a]$$ es una unidad de $$\mathbb{Z}_{m}$$ si $$a \in U(m)$$.

### Ejercicio (Caracterización de unidades)

Muestre que $$[a] \in U(m) \iff \operatorname{MCD}(a,m) = 1$$.

### Teorema (Generador de $$\mathbb{Z}_m$$)

Sea $$m \in \mathbb{N}^{\ast}$$. Considere $$(\mathbb{Z}_{m}, +)$$. Sea $$[a] \in \mathbb{Z}_{m}$$. Sea $$[a] \in \mathbb{Z}_{m}$$. Entonces

$$
\langle [a] \rangle = \mathbb{Z}_{m} \iff \operatorname{MCD}(a,m) = 1.
$$

***Prueba:*** ($$\impliedby$$): Suponga que $$\operatorname{MCD}(a,m)=1$$. Por el ejercicio anterior, existe $$[a]^{-1} \in \mathbb{Z}_{m}$$ tal que $$[a] \cdot [a] ^{-1} = [1]$$. Sea $$[b] \in \mathbb{Z}_{m}$$. Probaremos que $$[b] \in \langle [a] \rangle$$. Sea $$k \in \mathbb{Z}$$ tal que $$[k]:=[b] \cdot [a^{-1}]$$. Así.

$$
\begin{aligned}
[k]= [b] \cdot [a]^{-1} \implies [k] \cdot [a] = [b] \implies [a] + \dots + [a] = [b],
\end{aligned}
$$

de donde concluimos que $$b \in \langle[a]\rangle$$, y por tanto $$\langle [a] \rangle = \mathbb{Z}_{m}$$.
La otra dirección se deja como ejercicio.

### Nota (Cardinalidad de grupos cíclicos)

Si $$G$$ es cíclico, entonces $$G$$ es numerable ($$\lvert G \rvert \leq \lvert \mathbb{N} \rvert$$). Por ser cíclico, existe $$g \in G$$ tal que $$G = \langle g \rangle = \{ g^{n}:n \in \mathbb{Z} \}$$. Considere la función $$\Phi: \mathbb{Z} \to G$$ tal que $$n \mapsto g^{n}$$. Como $$g$$ es cíclico, esta función es sobreyectiva. Así, $$\lvert G \rvert \leq \lvert \mathbb{Z} \rvert$$. Esto implica que cualquier grupo construido a partir de conjuntos no numerables, como $$(\mathbb{R}, +)$$, no puede ser cíclico.

### Proposición (Grupos cíclicos y orden)

Sea $$G$$ un grupo cíclico con $$g \in G$$ tal que $$G = \langle g \rangle$$. Entonces:

1. Si $$\lvert g \rvert = \infty$$, entonces $$g^{i}=g^{j} \iff i=j$$.
2. Si $$\lvert g \rvert=n \in \mathbb{N}$$, entonces $$\langle g \rangle = \{ e,g,\dots, g^{n-1}\}$$. En este caso $$g^{i} = g^{j} \iff n \mid i-j$$. Esto implica que $$\lvert G \rvert = \lvert g \rvert$$.

***Prueba:*** Para (1), suponga que $$\lvert g \rvert=\infty$$. Luego para todo $$n \in \mathbb{N}$$, $$g^{n} \neq e$$. Suponga que existen $$i,j$$ distintos (con $$i<j$$ sin pérdida de generalidad) tales que $$g^{i} = g^{j}$$. Como $$j-i>0$$, tenemos que $$e = g^{i} \ast g^{-i} =g^{j-i}$$, una contradicción pues $$g$$ tiene orden infinito.
Para (2), sabemos que $$\langle g \rangle = \{ g^{n}: n \in \mathbb{Z} \}$$, por lo que $$\{ e,g,\dots, g^{n-1}\} \subseteq \langle g \rangle$$. Ahora, sea $$h \in \langle g \rangle$$. Entonces, existe $$k \in \mathbb{Z}$$ tal que $$h = g^{k}$$. Por algoritmo de la división, existen $$q,r \in \mathbb{Z}$$ con $$0\leq r\leq n-1$$ tales que $$k=nq+r$$. Así, $$h=g^{nq+r} = (g^{n})^{q} \ast g^{r}  = g^{r} \in \{ e,g,\dots, g^{n-1}\}$$. Concluimos que $$\langle  g \rangle = \{ e,g,\dots, g^{n-1}\}$$.
Ahora, dados $$i,j \in \mathbb{Z}$$, suponga que $$g^{i} = g^{j} \implies g^{i-j} = e$$, luego $$\lvert g \rvert \Big\lvert i-j$$. Por último, basta mostrar que si $$0 \leq i<j<n$$ entonces $$g^{i} \neq g^{j}$$. Note que $$0<j-i<n$$, por lo que si $$g^{i} = g^{j}$$, entonces $$g^{j-i} = e$$, lo que contradice la minimalidad del orden $$n$$.

## Subgrupos de Grupos Cíclicos

### Lema (Divisibilidad y subgrupo generado)

Sea $$G$$ un grupo cíclico y $$g \in G$$ tal que $$G = \langle g \rangle$$. Si $$k \mid \ell$$, entonces $$\langle g^{\ell} \rangle \subseteq \langle g^{k} \rangle$$.

***Prueba:*** Sea $$x \in \langle g^{\ell} \rangle$$. Existe $$r \in \mathbb{Z}$$ tal que $$x=(g^{\ell})^{r}$$. Además, como $$k \mid \ell$$, existe $$t \in \mathbb{Z}$$ tal que $$tk = \ell$$. Así, $$x = (g^{tk})^{r} = (g^{k})^{tr} \in \langle g^{k} \rangle$$.

### Ejercicio (Orden de potencia)

Si $$g \in G$$ con $$\lvert g \rvert = rs$$, con $$r,s \in \mathbb{N}$$, entonces $$\lvert g^{r} \rvert = s$$.

### Proposición (Ordenes de subgrupos de grupos cíclicos)

Sea $$G$$ grupo y $$g \in G$$ tal que $$\lvert g \rvert = n$$. Dado $$k \in \mathbb{N}$$, entonces

1. $$\langle g^{k} \rangle = \langle g^{\operatorname{mcd}(n,k)} \rangle$$
2. Si $$c \mid n$$, entonces $$\lvert g^{c} \rvert  = \frac{n}{c}$$.

En particular, $$\lvert g^{k} \rvert = \frac{n}{\operatorname{mcd}(n,k)}$$.

***Prueba:*** Para (1), Sea $$d=\operatorname{mcd}(n,k)$$. Es claro que $$d \mid k \implies \langle g^{k} \rangle \subseteq \langle g^{d} \rangle$$. Por otro lado, por lema de Bezout, existen $$r,t \in \mathbb{Z}$$ tales que $$d = rn + tk$$. Luego, $$g^{d} = g^{rn} \ast g^{tk} = (g^{k})^{t},$$ por lo que $$g^{d} \in \langle g^{k} \rangle$$ y por tanto $$\langle g^{d} \rangle \subseteq \langle g^{k} \rangle$$. Concluimos que $$\langle g^{d} \rangle = \langle g^{k} \rangle$$.

Ahora, para (2), como $$c \mid n$$, existe $$m \in \mathbb{Z}$$ tal que $$mc = n \implies m = \frac{n}{c} \in \mathbb{Z}$$. Usando el ejercicio anterior, tenemos que $$\lvert g \rvert = \frac{n}{c} \cdot c$$ y por tanto $$\lvert g^{c} \rvert = \frac{n}{c}$$. Para el resultado particular, tome $$c=d$$ en (2) y use la propiedad (1).

### Corolario (orden de elementos en grupos cíclicos)

Sea $$G$$ cíclico tal que $$\lvert G \rvert = n$$ y $$h \in G$$. Entonces, $$\lvert h \rvert \Big\lvert n$$.

***Prueba:*** Sea $$g \in G$$ tal que $$\langle g \rangle = G$$. Como $$h \in G$$, existe $$k \in \{ 0,\dots,n-1 \}$$ tal que $$h = g^{k}$$. Así, $$\lvert h \rvert = \lvert g^{k} \rvert = \frac{n}{\operatorname{mcd}(n,k)} \implies \lvert h \rvert \operatorname{mcd}(n,k) = n$$, de donde se sigue la divisibilidad.

### Teorema (Igualdad de subgrupos)

Sea $$G$$ un grupo y $$g \in G$$ tal que $$\lvert g \rvert = n$$. Las siguientes son equivalentes:

1. $$\operatorname{mcd}(k,n) = \operatorname{mcd}(\ell, n)$$
2. $$\langle g^{k} \rangle = \langle g^{\ell} \rangle$$.
3. $$\lvert g^{k} \rvert = \lvert g^{\ell} \rvert$$.

***Prueba:*** $$(2) \implies (3)$$ es trivial. Para $$(1) \implies (2)$$, asuma que $$\operatorname{mcd}(k,n) = \operatorname{mcd}(\ell, n)$$. Note que

$$
\langle g^{k} \rangle = \langle g^{\operatorname{mcd}(n,k)} \rangle = \langle g^{\operatorname{mcd}(n,\ell)} \rangle = \langle g^{\ell} \rangle.
$$

Finalmente, para $$(3) \implies (1)$$, usando la proposición anterior, note que

$$
\lvert g^{k} \rvert = \lvert g^{\ell} \rvert \implies \frac{n}{\operatorname{mcd}(n,k)} = \frac{n}{\operatorname{mcd}(n, \ell)} \implies \operatorname{mcd}(n,k) = \operatorname{mcd}(n, \ell).
$$

### Corolario (Elemento generador de un grupo cíclico)

Sea $$G = \langle g \rangle$$ con $$\lvert g \rvert=n$$. Sea $$k \in \mathbb{Z}$$. Entonces $$G = \langle g^{k} \rangle \iff \operatorname{mcd}(n,k) = 1$$.

***Prueba:*** Por el teorema anterior $$\langle g^{k} \rangle = \langle g^{1} \rangle \iff \operatorname{mcd}(n,k)=\operatorname{mcd}(n,1)  = 1$$.

### Teorema (Subgrupo de grupo cíclico es cíclico)

Sea $$G$$ un grupo cíclico y $$H \leq G$$. Entonces $$H$$ es cíclico.

***Prueba:*** Sea $$g \in G$$ tal que $$G = \langle g \rangle$$. Si $$H$$ es el subgrupo trivial, claramente es cíclico. Suponga que $$H$$ es no trivial. Sea $$e \neq h \in H$$. Como $$h \in H \subseteq G = \langle g \rangle$$, existe $$0 \neq k \in \mathbb{Z}$$ tal que $$h = g^{k}$$. Defina $$A = \{ n \in \mathbb{N}^{\ast} : g^{n} \in H\}$$. Note que $$A \neq \emptyset$$, pues si $$k \geq 0$$, $$k \in A$$, y en caso contrario $$-k \in A$$ (por ser $$H$$ un grupo, $$h^{-1} \in H$$). Luego, aplicando el principio del buen orden, $$A$$ tiene un elemento minimal $$\ell$$. Probaremos que $$H = \langle g^{\ell} \rangle$$. Por un lado, como $$\ell \in A$$, $$g^{\ell}\in H$$ y por tanto $$\langle g^{\ell} \rangle \subseteq H$$. Ahora, tome $$t \in H$$. Existe $$i \in \mathbb{Z}$$ tal que $$t = g^{i}$$. Suponiendo que $$i \neq 0$$, por algoritmo de la división, existen $$q,r \in \mathbb{Z}$$ con $$0\leq r<\ell$$ tales que $$i = q\ell+r \implies r = i-q\ell$$. Así, $$g^{r} = g^{i} \ast g^{-q \ell} \in H$$. Si $$r\neq0$$, tenemos que $$r \in A$$, lo que contradice la minimalidad de $$\ell$$. Concluya que $$r=0$$. Así, $$t = g^{i} = (g^{\ell})^{q}$$, de donde tenemos que $$t \in \langle g^{\ell} \rangle$$, Concluimos que $$H = \langle g^{\ell} \rangle$$.

### Nota (Hallazgo del generador)

Por la prueba, sabemos como encontrar un generador de $$H$$ a partir de un generador de $$G$$,

### Teorema (Lagrange para grupos cíclicos)

Sea $$G$$ un grupo cíclico tal que $$\lvert G \rvert = n$$ y $$H \leq G$$. Entonces, $$\lvert H \rvert \Big\lvert n$$.

***Prueba:*** Sea $$g \in G$$ tal que $$\langle g \rangle=G$$ y $$H\leq G$$. Luego, $$H$$ es cíclico y existe $$k \in \mathbb{N}$$ tal que $$H = \langle g^{k} \rangle$$. Sea $$d = \operatorname{mcd}(n,k)$$. Entonces,

$$
\lvert H \rvert  = \lvert \langle g^{k} \rangle  \rvert = \lvert g^{k} \rvert = \frac{n}{d}  \implies d \lvert H \rvert = n,
$$

de donde se sigue la divisibilidad.

### Teorema (Unicidad de ordenes en subgrupos)

Sea $$G$$ un grupo cíclico con $$\lvert G \rvert = n$$ y sea $$k \in \mathbb{N}$$ tal que $$k \mid n$$. Entonces existe un único subgrupo $$H$$ de $$G$$ con $$\lvert H \rvert = k$$. Además, si $$G = \langle g \rangle$$ entonces $$H = \langle g^{n/k} \rangle$$

***Prueba:*** Sea $$\ell = \frac{n}{k} \in \mathbb{N}$$ (pues $$k \mid n$$). Sea $$H = \langle g^{\ell} \rangle$$. Entonces, $$\lvert H \rvert = \lvert \langle g^{\ell} \rangle  \rvert = \frac{n}{\operatorname{mcd}(n, \ell)}$$. Ahora, como $$n = k\ell$$ entonces $$\operatorname{mcd}(n, \ell) = \operatorname{mcd}(k\ell, \ell) = \ell \operatorname{mcd}(k,1) = \ell$$. Así, $$\lvert H \rvert = \frac{n}{\ell} = k$$. La unicidad queda como ejercicio.
{% endraw %}
