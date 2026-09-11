---
layout: chapter
course: ma0561
chapter: 19
title: "Productos de anillos"
slug: 19-productos-de-anillos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/19-productos-de-anillos/
---

{% raw %}
## El producto directo y sus propiedades

### Definición (El producto de dos anillos)

Sean $$R_{1}, R_{2}$$ anillos, con estructuras $$(R_{1}, +_{R_{1}}, \cdot_{R_{1}}, 0_{R_{1}}, 1_{R_{1}})$$ y $$(R_{2}, +_{R_{2}}, \cdot_{R_{2}}, 0_{R_{2}}, 1_{R_{2}})$$. Defina

$$
R_{1} \times R_{2} := \{ (x_{1}, x_{2}) :\ x_{1} \in R_{1},\ x_{2} \in R_{2} \},
$$

con las operaciones componente a componente:

$$
(x_{1}, x_{2}) + (y_{1}, y_{2}) = (x_{1} +_{R_{1}} y_{1},\ x_{2} +_{R_{2}} y_{2}), \qquad (x_{1}, x_{2}) \cdot (y_{1}, y_{2}) = (x_{1} y_{1},\ x_{2} y_{2}).
$$

El cero en $$R_{1} \times R_{2}$$ es $$\vec{0} = (0_{R_{1}}, 0_{R_{2}})$$ y el uno es $$\vec{1} = (1_{R_{1}}, 1_{R_{2}})$$. Entonces $$(R_{1} \times R_{2}, +, \cdot, \vec{0}, \vec{1})$$ es un anillo.

### Definición (El producto directo de una familia de anillos)

En general, si $$\{R_{i}\}_{i \in I}$$ es un conjunto de anillos, podemos construir el anillo

$$
\prod_{i \in I} R_{i}
$$

de forma análoga, con las operaciones definidas componente a componente.

### Ejemplo ($$\mathbb{R}^{2}$$ tiene divisores de cero)

$$\mathbb{R}^{2} = \mathbb{R} \times \mathbb{R}$$ es un anillo, y

$$
\underbrace{(1, 0)}_{\neq (0,0)} \cdot \underbrace{(0, 1)}_{\neq (0,0)} = (0, 0).
$$

Entonces, a pesar de que $$\mathbb{R}$$ no tiene divisores de cero, $$\mathbb{R}^{2}$$ sí tiene.

### Nota (Las unidades del producto)

Sea $$\{R_{i} :\ i \in I\}$$ un conjunto de anillos y $$R = \prod_{i \in I} R_{i}$$. Al considerar las unidades $$R^{\times}$$, tenemos que

$$
R^{\times} = \prod_{i \in I} R_{i}^{\times}.
$$

### Teorema (Subanillos e ideales de un producto)

Sea $$\{R_{i} :\ i \in I\}$$ un conjunto de anillos y $$R = \prod_{i \in I} R_{i}$$. Entonces:

1. si para cada $$i \in I$$, $$S_{i}$$ es un subanillo de $$R_{i}$$, entonces $$\prod_{i \in I} S_{i}$$ es un subanillo de $$R$$;
2. si para cada $$i \in I$$, $$A_{i} \subseteq R_{i}$$ es un $$R_{i}$$-ideal, entonces $$\prod_{i \in I} A_{i}$$ es un $$R$$-ideal;
3. si $$K$$ es un ideal de $$R \times S$$, entonces existen $$I$$ un $$R$$-ideal y $$J$$ un $$S$$-ideal tales que $$K = I \times J$$.

***Prueba:*** Para (1): usamos el criterio de subanillo. Como $$1_{R_{i}} \in S_{i}$$ para cada $$i$$, tenemos que $$\vec{1} = (1_{R_{i}})_{i} \in \prod_{i} S_{i}$$; y si $$a = (a_{i})_{i}$$ y $$b = (b_{i})_{i}$$ están en $$\prod_{i} S_{i}$$, entonces $$a - b = (a_{i} - b_{i})_{i}$$ y $$a b = (a_{i} b_{i})_{i}$$ tienen todas sus componentes en los $$S_{i}$$, por ser cada $$S_{i}$$ subanillo.

Para (2): $$\prod_{i} A_{i} \neq \emptyset$$ pues contiene a $$\vec{0}$$; es cerrado bajo sumas componente a componente; y si $$r = (r_{i})_{i} \in R$$ y $$x = (x_{i})_{i} \in \prod_{i} A_{i}$$, entonces $$r x = (r_{i} x_{i})_{i}$$ tiene cada componente en $$A_{i}$$ por la absorción de cada $$A_{i}$$.

Para (3): sea $$K$$ un ideal de $$R \times S$$. Si $$(r, s) \in K$$, la absorción con $$(1, 0)$$ y $$(0, 1)$$ da

$$
(r, 0) = (1, 0) \cdot (r, s) \in K, \qquad (0, s) = (0, 1) \cdot (r, s) \in K.
$$

Defina

$$
I = \{ r \in R :\ (r, 0) \in K \}, \qquad J = \{ s \in S :\ (0, s) \in K \}.
$$

Entonces $$I$$ es un $$R$$-ideal: $$0 \in I$$; si $$r, r' \in I$$, entonces $$(r + r', 0) = (r, 0) + (r', 0) \in K$$; y si $$a \in R$$, entonces $$(a r, 0) = (a, 0) \cdot (r, 0) \in K$$ por la absorción de $$K$$. Análogamente $$J$$ es un $$S$$-ideal. Veamos que $$K = I \times J$$. “$$\subseteq$$”: si $$(r, s) \in K$$, por lo anterior $$(r, 0), (0, s) \in K$$, es decir, $$r \in I$$ y $$s \in J$$. “$$\supseteq$$”: si $$r \in I$$ y $$s \in J$$, entonces

$$
(r, s) = (r, 0) + (0, s) \in K,
$$

por la cerradura de $$K$$ bajo sumas.
{% endraw %}
