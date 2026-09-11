---
layout: chapter
course: ma0505
chapter: 3
title: "Propiedades topológicas básicas"
slug: 03-propiedades-topologicas-basicas
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/03-propiedades-topologicas-basicas/
---

{% raw %}
## Interior de un conjunto

### Definición (Punto interior e interior de un conjunto)

Sea $$(E, d)$$ un espacio métrico y $$A \subseteq E$$. Decimos que $$x_{0} \in A$$ es un *punto interior* de $$A$$ si existe $$r > 0$$ con $$B(x_{0}, r) \subseteq A$$. El *interior* de $$A$$, denotado $$A^{\circ}$$, es el conjunto de los puntos interiores de $$A$$.

### Lema ($$A^{\circ}$$ es el mayor abierto contenido en $$A$$)

Sea $$G \subseteq A$$ con $$G$$ abierto. Entonces $$G \subseteq A^{\circ}$$. En particular, $$A^{\circ}$$ es el abierto más grande contenido en $$A$$.

***Prueba:*** Si $$x_{0} \in G$$, como $$G$$ es abierto existe $$r > 0$$ con $$B(x_{0}, r) \subseteq G \subseteq A$$, por lo que $$x_{0} \in A^{\circ}$$. Concluimos que $$G \subseteq A^{\circ}$$.

### Ejercicio ($$A^{\circ}$$ es abierto)

Pruebe que para todo $$A \subseteq E$$, $$A^{\circ}$$ es un conjunto abierto.

### Lema (Interior de la intersección)

Sean $$A_{1}, A_{2} \subseteq E$$. Entonces $$(A_{1} \cap A_{2})^{\circ} = A_{1}^{\circ} \cap A_{2}^{\circ}$$.

***Prueba:*** Como $$A_{1}^{\circ} \cap A_{2}^{\circ}$$ es abierto y está contenido en $$A_{1} \cap A_{2}$$, por el lema previo $$A_{1}^{\circ} \cap A_{2}^{\circ} \subseteq (A_{1} \cap A_{2})^{\circ}$$.

Recíprocamente, si $$x \in (A_{1} \cap A_{2})^{\circ}$$, existe $$r > 0$$ con $$B(x, r) \subseteq A_{1} \cap A_{2}$$. Entonces $$B(x, r) \subseteq A_{1}$$ y $$B(x, r) \subseteq A_{2}$$, lo que implica $$x \in A_{1}^{\circ} \cap A_{2}^{\circ}$$.

### Ejercicio (Monotonía del interior)

Si $$A \subseteq B$$ entonces $$A^{\circ} \subseteq B^{\circ}$$. *Sugerencia:* use el lema $$G \subseteq A^{\circ}$$ siempre que $$G$$ sea abierto y $$G \subseteq A$$.

### Ejercicio (Caracterización de abierto por interior)

Dado $$B \subseteq E$$, $$B$$ es abierto si y solo si $$B = B^{\circ}$$.

## Convergencia de sucesiones y distancia entre conjuntos

### Definición (Convergencia de sucesiones)

Una sucesión $$\{ x_{n} \}_{n=1}^{\infty} \subseteq E$$ *converge* a $$x \in E$$ si para todo $$\varepsilon > 0$$ existe $$n_{0} \in \mathbb{N}$$ tal que $$n \geq n_{0}$$ implica $$d(x_{n}, x) < \varepsilon$$. Se escribe $$x_{n} \to x$$ cuando $$n \to \infty$$.

### Definición (Distancia entre conjuntos)

Dados $$A, B \subseteq E$$, se define

$$
d(A, B) = \inf \{ d(x, y) : (x, y) \in A \times B \}.
$$

En particular, para $$x \in E$$ y $$A \subseteq E$$, $$d(x, A) = \inf\{ d(x,a) : a \in A\}$$.

### Ejercicio (La distancia a un conjunto es $$1$$-Lipschitz)

Para todo $$A \subseteq E$$ y $$x, y \in E$$, $$|d(x, A) - d(y, A)| \leq d(x, y)$$.

## Clausura de un conjunto

### Lema (Caracterización de la clausura por sucesiones y por distancia)

Dados $$x \in E$$ y $$A \subseteq E$$, son equivalentes:

1. $$d(x, A) = 0$$;
2. existe $$\{ x_{n} \}_{n=1}^{\infty} \subseteq A$$ tal que $$x_{n} \to x$$ cuando $$n \to \infty$$.

***Prueba:*** $$(1) \implies (2)$$: Si $$d(x, A) = 0$$, para cada $$n \in \mathbb{N}$$ existe $$x_{n} \in A$$ con $$d(x, x_{n}) < 1/n$$, por lo que $$\{x_{n}\}_{n=1}^{\infty} \subseteq A$$ y $$x_{n} \to x$$.

$$(2) \implies (1)$$: Si $$\{x_{n}\}_{n=1}^{\infty} \subseteq A$$ y $$x_{n} \to x$$, entonces $$d(x, A) \leq d(x, x_{n}) \to 0$$, de donde $$d(x, A) = 0$$.

### Definición (Clausura y puntos de adherencia)

Dado $$A \subseteq E$$, la *clausura* de $$A$$ es

$$
\overline{A} = \{ x \in E : d(x, A) = 0\}.
$$

Sus elementos se llaman *puntos de adherencia* de $$A$$. Inmediatamente $$A \subseteq \overline{A}$$.

### Proposición (Monotonía de la clausura)

Si $$A \subseteq B \subseteq E$$, entonces $$\overline{A} \subseteq \overline{B}$$.

***Prueba:*** Para $$x \in E$$,

$$
\inf_{b \in B} d(x, b) \leq \inf_{a \in A} d(x, a),
$$

i.e. $$d(x, B) \leq d(x, A)$$. Así, $$d(x, A) = 0$$ implica $$d(x, B) = 0$$.

### Ejemplo (Distancia cero entre dos cerrados disjuntos)

Sean $$A = \{ n + \tfrac{1}{n} \}_{n=1}^{\infty}$$ y $$B = \mathbb{Z}$$. Ambos son cerrados (por ejemplo $$\mathbb{R} \setminus B = \bigcup_{n \in \mathbb{Z}} (n, n+1)$$ es abierto). Sin embargo,

$$
d\!\left(n + \tfrac{1}{n}, n\right) = \tfrac{1}{n} \to 0,
$$

de modo que $$d(A, B) = 0$$.

### Lema (Cerrado equivale a igual a su clausura)

Sea $$A \subseteq E$$. Entonces $$A$$ es cerrado si y solo si $$A = \overline{A}$$.

***Prueba:*** $$(\impliedby)$$: Si $$A = \overline{A}$$ y $$x \notin A$$, entonces $$d(x, A) > 0$$. Existe $$r > 0$$ con $$r \leq d(x, A)$$ y entonces $$B(x, r) \cap A = \emptyset$$, i.e. $$B(x, r) \subseteq E \setminus A$$. Así $$E\setminus A$$ es abierto y $$A$$ es cerrado.

$$(\implies)$$: Supongamos $$A$$ cerrado y tomemos $$x \in E \setminus A$$. Como $$E\setminus A$$ es abierto, existe $$r_{1} > 0$$ con $$B(x, r_{1}) \subseteq E \setminus A$$, por lo que $$B(x, r_{1}) \cap A = \emptyset$$ y $$d(x, A) \geq r_{1} > 0$$. Por tanto $$x \notin \overline{A}$$, lo cual prueba $$\overline{A} \subseteq A$$. La inclusión $$A \subseteq \overline{A}$$ es inmediata.

### Proposición (La clausura es un conjunto cerrado)

Para todo $$A \subseteq E$$, $$\overline{A}$$ es cerrado.

***Prueba:*** Sea $$z \notin \overline{A}$$, es decir $$d(z, A) = r > 0$$. Veremos que $$B(z, r/2) \subseteq E \setminus \overline{A}$$. Si $$w \in B(z, r/2)$$ y $$a \in A$$, entonces

$$
r \leq d(z, a) \leq d(z, w) + d(w, a) < \tfrac{r}{2} + d(w, a),
$$

por lo que $$d(w, a) > r/2$$ y, tomando ínfimo, $$d(w, A) \geq r/2 > 0$$, i.e. $$w \notin \overline{A}$$.

### Ejercicio (Propiedades de la clausura sobre uniones e intersecciones)

Para $$A, B \subseteq E$$:

1. $$\overline{A \cup B} = \overline{A} \cup \overline{B}$$;
2. $$\overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$$.

## Acumulación y frontera

### Definición (Punto de acumulación)

Un punto $$x_{0} \in E$$ es un *punto de acumulación* de $$A \subseteq E$$ si para todo $$r > 0$$,

$$
\big(B(x_{0}, r) \setminus \{ x_{0}\}\big) \cap A \neq \emptyset.
$$

Es decir, toda bola centrada en $$x_{0}$$ contiene puntos de $$A$$ distintos de $$x_{0}$$.

### Ejercicio (Caracterización de los puntos de acumulación por sucesiones)

$$x_{0}$$ es punto de acumulación de $$A$$ si y solo si existe una sucesión $$\{ x_{n}\}_{n=1}^{\infty} \subseteq A \setminus \{x_{0}\}$$ tal que $$x_{n} \to x_{0}$$.

### Ejemplo (Punto de acumulación único de $$\{1/n\}$$)

Sea $$A = \{ 1/n : n \geq 1\}$$. Entonces $$\overline{A} = A \cup \{ 0\}$$ y $$0$$ es el único punto de acumulación de $$A$$, pues

$$
B\!\left(\tfrac{1}{n}, \tfrac{1}{(n+1)^{2}}\right) \cap A = \left\{ \tfrac{1}{n}\right\} \quad \text{si } n \geq 1.
$$

### Definición (Punto frontera y frontera de un conjunto)

Dado $$A \subseteq E$$ y $$x \in E$$, decimos que $$x$$ es *punto frontera* de $$A$$ si para todo $$r > 0$$,

$$
B(x, r) \cap A \neq \emptyset \quad\text{y}\quad B(x, r) \cap (E \setminus A) \neq \emptyset.
$$

Equivalentemente, $$d(x, A) = d(x, E \setminus A) = 0$$.

### Notación (Frontera)

La *frontera* de $$A$$ se denota

$$
\partial A = \{\text{puntos frontera de } A\} = \{ x \in E : d(x, A) = d(x, E \setminus A) = 0\} = \overline{A} \cap \overline{E \setminus A}.
$$

Observe que $$\partial A \subseteq \overline{A}$$.

## Vecindarios y densidad

### Definición (Vecindario de un punto)

Dado $$x \in E$$, $$V \subseteq E$$ es un *vecindario* de $$x$$ si existe $$r > 0$$ tal que $$B(x, r) \subseteq V$$.

### Nota (Abiertos como vecindarios)

Si $$V$$ es abierto, $$V$$ es vecindario de cada uno de sus puntos.

### Definición (Vecindario $$r$$ de un conjunto)

Dado $$A \subseteq E$$ y $$r > 0$$, se define

$$
V_{r}(A) = \{ x \in E : d(x, A) < r\}.
$$

En particular $$A \subseteq \overline{A} \subseteq V_{r}(A)$$.

### Ejercicio (Las bolas centradas en $$A$$ están contenidas en $$V_{r}(A)$$)

Sea $$x \notin \overline{A}$$ con $$x \in V_{r}(A)$$. Si $$0 < r_{1} < r - d(x, A)$$, muestre que

$$
B(x, r_{1}) \subseteq V_{r}(A).
$$

### Lema ($$V_{r}(A)$$ es abierto)

Si $$A \subseteq E$$ y $$r > 0$$, entonces $$V_{r}(A)$$ es abierto.

***Prueba:*** Sea $$x \in V_{r}(A)$$ y tome $$a \in A$$ con $$d(x, a) < r$$. Defina $$r_{1} = r - d(x, a) > 0$$. Para $$y \in B(x, r_{1})$$ se tiene

$$
d(y, A) \leq d(y, a) \leq d(y, x) + d(x, a) < r_{1} + d(x, a) = r,
$$

es decir $$y \in V_{r}(A)$$. Así $$B(x, r_{1}) \subseteq V_{r}(A)$$.

### Proposición (La clausura es intersección de vecindarios)

Para todo $$A \subseteq E$$,

$$
\overline{A} = \bigcap_{r > 0} V_{r}(A).
$$

En particular, $$\overline{A}$$ es intersección numerable de abiertos.

***Prueba:*** Si $$x \in \overline{A}$$ entonces $$d(x, A) = 0 < r$$ para todo $$r > 0$$, así $$x \in V_{r}(A)$$. Recíprocamente, si $$x \in \bigcap_{r > 0} V_{r}(A)$$ entonces $$d(x, A) < r$$ para todo $$r > 0$$, por lo que $$d(x, A) = 0$$ y $$x \in \overline{A}$$.

### Definición (Conjunto denso y espacio separable)

$$A \subseteq E$$ es *denso* en $$E$$ si $$\overline{A} = E$$. Un espacio métrico $$(E, d)$$ es *separable* si posee un conjunto denso y numerable.

### Ejemplo ($$\mathbb{R}$$ y $$\mathbb{R}^{d}$$ son separables)

$$(\mathbb{R}, |\cdot|)$$ es separable pues $$\mathbb{Q}$$ es denso en $$\mathbb{R}$$. En general $$(\mathbb{R}^{d}, \|\cdot\|)$$ es separable porque $$\mathbb{Q}^{d}$$ es denso en $$\mathbb{R}^{d}$$.
{% endraw %}
