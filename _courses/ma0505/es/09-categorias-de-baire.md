---
layout: chapter
course: ma0505
chapter: 9
title: "Categorías de Baire"
slug: 09-categorias-de-baire
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/09-categorias-de-baire/
---

{% raw %}
## Conjuntos de primera y segunda categoría

### Definición (Conjunto denso en ninguna parte)

Dado un espacio métrico $$(X, d)$$, $$A \subseteq X$$ es *denso en ninguna parte* si $$(\overline{A})^{c}$$ es denso en $$X$$. Equivalentemente, $$(\overline{A})^{\circ} = \emptyset$$.

### Nota (Caracterización por interior de la clausura)

$$A$$ es denso en ninguna parte si y solo si para todo $$x \in X$$ y $$r > 0$$,

$$
(\overline{A})^{c} \cap B(x, r) \neq \emptyset.
$$

### Definición (Primera y segunda categoría (magro))

1. Un conjunto $$A \subseteq X$$ es de *primera categoría* (o *magro*) si es unión numerable de conjuntos densos en ninguna parte.
2. Un conjunto es de *segunda categoría* si no es de primera categoría.

## Los teoremas de Baire

### Teorema (Baire (intersección numerable de abiertos densos))

Sea $$(X, d)$$ completo. Si $$\{G_{n}\}_{n=1}^{\infty}$$ es una sucesión de conjuntos abiertos y densos en $$X$$, entonces $$\bigcap_{n=1}^{\infty} G_{n}$$ es denso en $$X$$.

***Prueba:*** Sea $$A \subseteq X$$ un abierto no vacío. Como $$G_{1}$$ es denso, existe $$x_{1} \in A \cap G_{1}$$, y como $$A \cap G_{1}$$ es abierto, existe $$r_{1} > 0$$ con $$B(x_{1}, r_{1}) \subseteq A \cap G_{1}$$. Tome $$B_{1} = B(x_{1}, r_{1}/2)$$, así $$\overline{B}_{1} \subseteq B(x_{1}, r_{1}) \subseteq A \cap G_{1}$$.

Aplicando el mismo argumento a $$B_{1}$$ y $$G_{2}$$, existen $$x_{2} \in G_{2}$$ y $$0 < r_{2} < r_{1}/2$$ tales que $$B(x_{2}, r_{2}) \subseteq B_{1} \cap G_{2} \subseteq A \cap G_{1} \cap G_{2}$$ y, definiendo $$B_{2} = B(x_{2}, r_{2}/2)$$, $$\overline{B}_{2} \subseteq B_{1} \cap G_{2}$$.

Iterando se obtiene una sucesión $$\{x_{n}\}$$ con $$x_{n} \in G_{n}$$ y $$r_{n} < r_{n-1}/2 \leq r_{1}/2^{n-1}$$ tal que

$$
B(x_{n}, r_{n}) \subseteq B_{n-1} \cap G_{n} \subseteq A \cap \bigcap_{i=1}^{n} G_{i}, \quad \overline{B}_{n} \subseteq B_{n-1} \cap G_{n}.
$$

Si $$n \geq m$$ entonces $$B_{n} \subseteq B_{m}$$ y $$x_{n}, x_{m} \in B_{m}$$, por lo que $$d(x_{n}, x_{m}) < 2 r_{m} < r_{1}/2^{m-2}$$. Así $$\{x_{n}\}$$ es de Cauchy. Por completitud existe $$x = \lim_{n} x_{n}$$, y como $$\{x_{n}\}_{n=m}^{\infty} \subseteq B_{m}$$, $$x \in \overline{B}_{m} \subseteq A \cap \bigcap_{i=1}^{m} G_{i}$$ para todo $$m \geq 1$$, así $$x \in A \cap \bigcap_{i=1}^{\infty} G_{i}$$. Concluimos que $$\bigcap_{i=1}^{\infty} G_{i}$$ es denso.

### Teorema (Categorías de Baire)

Sea $$(X, d)$$ un espacio métrico completo. Si $$G \subseteq X$$ es un abierto no vacío, entonces $$G$$ es de segunda categoría.

***Prueba:*** Suponga, por contradicción, que $$G$$ es de primera categoría. Existen $$A_{n}$$ densos en ninguna parte con $$G = \bigcup_{n=1}^{\infty} A_{n}$$. Sea $$G_{n} = (\overline{A}_{n})^{c}$$; cada $$G_{n}$$ es abierto y denso (por la definición de denso en ninguna parte). Por el teorema de Baire,

$$
\bigcap_{n=1}^{\infty} G_{n} \;=\; \bigcap_{n=1}^{\infty} (\overline{A}_{n})^{c} \;=\; \Big(\bigcup_{n=1}^{\infty} \overline{A}_{n}\Big)^{c}
$$

es denso en $$X$$. Por otro lado, como $$A_{n} \subseteq \overline{A}_{n}$$ para todo $$n$$,

$$
G \;=\; \bigcup_{n=1}^{\infty} A_{n} \;\subseteq\; \bigcup_{n=1}^{\infty} \overline{A}_{n},
$$

de donde

$$
G \cap \Big(\bigcup_{n=1}^{\infty} \overline{A}_{n}\Big)^{c} \;=\; G \cap \bigcap_{n=1}^{\infty} G_{n} \;=\; \emptyset.
$$

Pero $$G$$ es un abierto no vacío, así $$G$$ debe intersecar a todo conjunto denso. Esto contradice que $$\bigcap_{n=1}^{\infty} G_{n}$$ sea denso, concluyendo el resultado.
{% endraw %}
