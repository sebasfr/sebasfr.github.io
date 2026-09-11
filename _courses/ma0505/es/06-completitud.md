---
layout: chapter
course: ma0505
chapter: 6
title: "Completitud"
slug: 06-completitud
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/06-completitud/
---

{% raw %}
## Sucesiones de Cauchy y espacios completos

### Definición (Sucesión de Cauchy)

Una sucesión $$\{x_{n}\}_{n=1}^{\infty}$$ en $$(X, d)$$ es *de Cauchy* si para todo $$\varepsilon > 0$$ existe $$n_{0} \in \mathbb{N}$$ tal que

$$
n, m \geq n_{0} \implies d(x_{n}, x_{m}) < \varepsilon.
$$

A diferencia de la compacidad, este concepto es *intrínseco* al espacio métrico.

### Ejercicio (Recordatorio sobre sucesiones de Cauchy)

1. Toda sucesión convergente es de Cauchy.
2. Toda sucesión de Cauchy es acotada.

### Definición (Espacio métrico completo)

$$(X, d)$$ es *completo* si toda sucesión de Cauchy en $$X$$ es convergente en $$X$$.

### Ejemplo ($$(\mathcal{C}([0,1], \mathbb{R}), d_{\infty})$$ es completo)

Sea $$\mathcal{C} = \{ f : [0,1] \to \mathbb{R} \;:\; f \text{ continua}\}$$ con $$d_{\infty}(f, g) = \sup_{x \in [0,1]} |f(x) - g(x)|$$. Sea $$\{f_{n}\}_{n=1}^{\infty}$$ de Cauchy. Para cada $$x \in [0,1]$$, $$|f_{n}(x) - f_{m}(x)| \leq d_{\infty}(f_{n}, f_{m})$$, por lo que $$\{f_{n}(x)\}_{n=1}^{\infty}$$ es de Cauchy en $$\mathbb{R}$$. Como $$\mathbb{R}$$ es completo, defina $$f(x) = \lim_{n \to \infty} f_{n}(x)$$.

Veamos que $$f \in \mathcal{C}$$. Dado $$\varepsilon > 0$$, fije $$n_{0}$$ con $$d_{\infty}(f_{n}, f_{m}) < \varepsilon/2$$ para $$n, m \geq n_{0}$$. Para $$x \in [0,1]$$, existe $$m_{1} \geq n_{0}$$ con $$|f(x) - f_{m_{1}}(x)| < \varepsilon/2$$, luego para $$n \geq n_{0}$$,

$$
|f(x) - f_{n}(x)| \leq |f(x) - f_{m_{1}}(x)| + d_{\infty}(f_{m_{1}}, f_{n}) < \tfrac{\varepsilon}{2} + \tfrac{\varepsilon}{2} = \varepsilon.
$$

Por tanto $$f_{n} \to f$$ uniformemente y, como límite uniforme de continuas, $$f$$ es continua.

### Nota (Estrategia para demostrar que una sucesión de Cauchy converge)

Como es usual, para probar que una sucesión de Cauchy converge se empieza encontrando un *candidato* para el límite y luego se verifica la convergencia hacia él.

## Completitud y conjuntos cerrados

### Lema (Caracterización de subespacios completos como cerrados)

Sea $$(X, d)$$ un espacio métrico y $$C \subseteq X$$. Entonces:

1. Si $$(C, d)$$ es completo, entonces $$C$$ es cerrado en $$(X, d)$$;
2. Si $$X$$ es completo y $$C$$ es cerrado en $$X$$, entonces $$(C, d)$$ es completo.

***Prueba:*** *(2)*: Sea $$\{x_{n}\}_{n=1}^{\infty} \subseteq C$$ de Cauchy. Como $$X$$ es completo, existe $$x \in X$$ con $$x_{n} \to x$$. Por ser $$C$$ cerrado, $$x \in C$$, así $$\{x_{n}\}$$ converge en $$C$$.

*(1)*: Sea $$x \in \overline{C}$$ y tome $$\{x_{n}\}_{n=1}^{\infty} \subseteq C$$ con $$x_{n} \to x$$ en $$X$$. Como $$\{x_{n}\}$$ es convergente, es de Cauchy en $$C$$. Por completitud de $$C$$, existe $$x' \in C$$ con $$x_{n} \to x'$$. Por unicidad del límite, $$x = x' \in C$$, lo que prueba $$\overline{C} \subseteq C$$.

### Lema (Compacto implica completo)

Si $$(X, d)$$ es compacto, entonces $$(X, d)$$ es completo.

***Prueba:*** Sea $$\{x_{n}\}_{n=1}^{\infty}$$ de Cauchy. Por compacidad existe $$\{x_{n_{k}}\}$$ que converge a $$x \in X$$. Dado $$\varepsilon > 0$$, existen $$n_{0}, k_{0}$$ con $$n, m \geq n_{0} \implies d(x_{n}, x_{m}) < \varepsilon/2$$ y $$k \geq k_{0} \implies d(x, x_{n_{k}}) < \varepsilon/2$$. Para $$n, k \geq \max\{n_{0}, k_{0}\}$$,

$$
d(x_{n}, x) \leq d(x_{n}, x_{n_{k}}) + d(x_{n_{k}}, x) < \tfrac{\varepsilon}{2} + \tfrac{\varepsilon}{2} = \varepsilon.
$$

### Nota (Completitud no implica compacidad)

La implicación recíproca es falsa: $$\mathbb{R}$$ es completo pero no compacto.

## Conjuntos totalmente acotados

### Definición (Espacio totalmente acotado)

$$(X, d)$$ es *totalmente acotado* (o *paracompacto*) si para todo $$\varepsilon > 0$$ existen $$x_{1}, \dots, x_{m} \in X$$ tales que

$$
X = \bigcup_{i=1}^{m} B(x_{i}, \varepsilon).
$$

En particular, todo espacio compacto es totalmente acotado.

### Ejemplo (Acotado pero no totalmente acotado)

Considere $$\rho : \mathbb{N} \times \mathbb{N} \to \{0, 1\}$$ con $$\rho(n, m) = 1$$ si $$n \neq m$$ y $$\rho(n, n) = 0$$. Para cualquier $$n$$, $$\mathbb{N} = B(n, 2)$$, así $$(\mathbb{N}, \rho)$$ es acotado. Sin embargo, $$B(n, 1/2) = \{n\}$$, por lo que no es posible cubrir $$\mathbb{N}$$ con una colección finita de bolas de radio $$1/2$$. Concluimos que $$(\mathbb{N}, \rho)$$ es acotado pero no totalmente acotado.

### Ejercicio (Sucesiones que toman finitos valores admiten subsucesión convergente)

Si el conjunto $$\{ x_{n} : n \in \mathbb{N}\}$$ es finito, entonces existe una subsucesión $$\{x_{n_{k}}\}_{k=1}^{\infty}$$ que converge a un punto de la sucesión.

### Lema (Caracterización de totalmente acotado por subsucesiones de Cauchy)

$$(X, d)$$ es totalmente acotado si y solo si toda sucesión $$\{x_{n}\}_{n=1}^{\infty} \subseteq X$$ posee una subsucesión de Cauchy.

***Prueba:*** $$(\implies)$$: Por el ejercicio anterior, podemos asumir que la sucesión toma infinitos valores distintos. Como $$X$$ es totalmente acotado existen $$y_{1}, \dots, y_{m}$$ con $$X \subseteq \bigcup_{i=1}^{m} B(y_{i}, 1)$$. Alguno de estos $$B(y_{i_{1}}, 1)$$ contiene infinitos puntos de $$\{x_{n}\}$$; sea $$\{x_{n_{k,1}}\}_{k=1}^{\infty}$$ la subsucesión correspondiente.

Iterando, en el paso $$\ell$$ existen $$\tilde{y}_{\ell}$$ y una subsucesión $$\{x_{n_{k,\ell}}\}_{k=1}^{\infty} \subseteq B(\tilde{y}_{\ell}, 1/\ell)$$ extraída de $$\{x_{n_{k,\ell-1}}\}$$. Note que $$d(x_{n_{k,\ell}}, x_{n_{s,\ell}}) < 2/\ell$$ para todos $$k, s$$. Considere la subsucesión diagonal $$\{x_{n_{\ell,\ell}}\}_{\ell=1}^{\infty}$$: si $$\ell \leq s$$, $$d(x_{n_{\ell,\ell}}, x_{n_{s,s}}) \leq 2/\ell$$, lo cual muestra que es de Cauchy.

$$(\impliedby)$$: Si $$X$$ no fuese totalmente acotado, existiría $$\varepsilon > 0$$ tal que ninguna colección finita de bolas de radio $$\varepsilon$$ recubre $$X$$. Construya iterativamente $$x_{0} \in X$$ y, dado $$x_{1}, \dots, x_{n-1}$$, $$x_{n} \in X \setminus \bigcup_{i=1}^{n-1} B(x_{i}, \varepsilon)$$. Entonces $$d(x_{i}, x_{j}) \geq \varepsilon$$ para $$i \neq j$$, sucesión sin subsucesiones de Cauchy.

### Teorema (Compacto $$=$$ completo $$+$$ totalmente acotado)

Un espacio métrico es compacto si y solo si es completo y totalmente acotado.

***Prueba:*** $$(\implies)$$: Todo compacto es completo (probado anteriormente). Para ver que todo compacto es totalmente acotado, dado $$\varepsilon > 0$$ la familia $$\{ B(x, \varepsilon) : x \in X\}$$ es un cubrimiento por abiertos de $$X$$, así por compacidad existen $$x_{1}, \dots, x_{m} \in X$$ con $$X = \bigcup_{i=1}^{m} B(x_{i}, \varepsilon)$$.

$$(\impliedby)$$: Sea $$\{x_{n}\}_{n=1}^{\infty} \subseteq X$$. Por ser totalmente acotado, posee una subsucesión $$\{x_{n_{k}}\}$$ de Cauchy. Por completitud, $$\{x_{n_{k}}\}$$ converge en $$X$$. Así $$X$$ es secuencialmente compacto, equivalentemente compacto.

## Compleción de un espacio métrico

### Teorema (Existencia de la compleción)

Sea $$(X, d)$$ un espacio métrico. Entonces:

1. Existe un espacio métrico completo $$(X^{\sharp}, d^{\sharp})$$ y una función inyectiva $$i : X \to X^{\sharp}$$ que preserva distancias, con $$i(X)$$ denso en $$X^{\sharp}$$.
2. Si $$(X, d)$$ es completo, entonces $$(X^{\sharp}, d^{\sharp})$$ es isométrico a $$(X, d)$$.

***Prueba:*** *Construcción.* Sean $$\{x_{n}\}, \{y_{n}\} \subseteq X$$ de Cauchy. La desigualdad triangular da

$$
|d(x_{m}, y_{m}) - d(x_{n}, y_{n})| \leq d(x_{m}, x_{n}) + d(y_{m}, y_{n}),
$$

luego $$\{d(x_{m}, y_{m})\}_{m=1}^{\infty}$$ es de Cauchy en $$\mathbb{R}$$. Definimos

$$
\tilde{d}(\{x_{n}\}, \{y_{n}\}) = \lim_{m \to \infty} d(x_{m}, y_{m}).
$$

Esta $$\tilde{d}$$ es simétrica y satisface la desigualdad triangular pero puede valer $$0$$ entre dos sucesiones distintas; es una *semimétrica*. Definimos $$\{x_{n}\} \sim \{y_{n}\}$$ cuando $$\tilde{d}(\{x_{n}\}, \{y_{n}\}) = 0$$ y consideramos

$$
X^{\sharp} = \big\{[\{x_{n}\}] \;:\; \{x_{n}\} \subseteq X \text{ de Cauchy}\big\}, \quad d^{\sharp}([\{x_{n}\}], [\{y_{n}\}]) = \tilde{d}(\{x_{n}\}, \{y_{n}\}).
$$

*$$d^{\sharp}$$ está bien definida.* Si $$\{x_{n}\} \sim \{x_{n}'\}$$, entonces $$d(x_{m}, x_{m}') \to 0$$, y dado $$\{y_{n}\}$$ de Cauchy,

$$
d(x_{m}, y_{m}) \leq d(x_{m}, x_{m}') + d(x_{m}', y_{m}),
$$

luego $$\lim_{m} d(x_{m}, y_{m}) \leq \lim_{m} d(x_{m}', y_{m})$$. Recíprocamente, $$d(x_{m}', y_{m}) \leq d(x_{m}', x_{m}) + d(x_{m}, y_{m})$$ implica $$\lim_{m} d(x_{m}', y_{m}) \leq \lim_{m} d(x_{m}, y_{m})$$, de donde se sigue la igualdad y por tanto $$d^{\sharp}$$ no depende de los representantes.

*$$i$$ preserva distancias y $$i(X)$$ es denso.* Para $$x \in X$$ defina $$i(x) = [\{x, x, \dots\}]$$. Entonces $$d^{\sharp}(i(x), i(y)) = \lim_{m} d(x, y) = d(x, y)$$. Dado $$[\{x_{n}\}] \in X^{\sharp}$$ y $$\varepsilon > 0$$, existe $$n_{0}$$ con $$d(x_{n}, x_{n_{0}}) < \frac{\varepsilon}{2}$$ para $$n \geq n_{0}$$, así $$d^{\sharp}([\{x_{n}\}], i(x_{n_{0}})) = \lim_{m} d(x_{m}, x_{n_{0}}) \leq \frac{\varepsilon}{2} < \varepsilon$$.

*$$X^{\sharp}$$ es completo.* Sea $$\{\underline{x}^{m}\}_{m=1}^{\infty} \subseteq X^{\sharp}$$ de Cauchy. Por la densidad de $$i(X)$$ en $$X^{\sharp}$$ recién probada, para cada $$m \in \mathbb{N}$$ existe $$y_{m} \in X$$ con $$d^{\sharp}(\underline{x}^{m}, i(y_{m})) < 1/m$$. Entonces

$$
d(y_{m}, y_{n}) = d^{\sharp}(i(y_{m}), i(y_{n})) \leq \tfrac{1}{m} + d^{\sharp}(\underline{x}^{m}, \underline{x}^{n}) + \tfrac{1}{n},
$$

así $$\{y_{n}\}$$ es de Cauchy en $$X$$. Sea $$\underline{y} = [\{y_{n}\}] \in X^{\sharp}$$. Dado $$\varepsilon > 0$$, escoja $$k_{0}$$ con $$d(y_{n}, y_{j}) < \varepsilon/2$$ para todos $$n, j \geq k_{0}$$. Para $$m \geq k_{0}$$,

$$
d^{\sharp}(i(y_{m}), \underline{y}) = \lim_{j \to \infty} d(y_{m}, y_{j}) \leq \tfrac{\varepsilon}{2},
$$

de donde

$$
d^{\sharp}(\underline{x}^{m}, \underline{y}) \leq d^{\sharp}(\underline{x}^{m}, i(y_{m})) + d^{\sharp}(i(y_{m}), \underline{y}) \leq \tfrac{1}{m} + \tfrac{\varepsilon}{2} < \varepsilon
$$

para $$m$$ suficientemente grande. Concluimos $$\underline{x}^{m} \to \underline{y}$$ en $$X^{\sharp}$$.

*(2)*: Si $$(X, d)$$ es completo, dada $$\{x_{n}\}$$ de Cauchy existe $$x \in X$$ con $$x_{n} \to x$$. Entonces $$d^{\sharp}([\{x_{n}\}], i(x)) = \lim_{m} d(x_{m}, x) = 0$$, así $$i(x) = [\{x_{n}\}]$$ y $$i$$ es sobreyectiva, luego una isometría.

### Definición (Compleción de un espacio)

Decimos que $$X^\ast$$ es complecion de $$X$$ si $$X^\ast$$ es completo y contiene una copia de $$X$$, la cual es densa. Es decir, existe una isometría $$\phi: X \to \phi(X) \subseteq X^\ast$$, con $$\overline{\phi(X)} = X^\ast$$.

### Lema (Propiedad universal de la compleción)

Sea $$(Y, \rho)$$ un espacio métrico completo y $$j : X \to Y$$ una función que preserva distancias con $$j(X)$$ denso en $$Y$$. Entonces existe $$\theta : X^{\sharp} \to Y$$, una isometría tal que $$\theta \circ i = j$$.

***Prueba:*** Ejercicio (extender $$\theta$$ a partir de $$\theta(i(x)) = j(x)$$ usando densidad y completitud).
{% endraw %}
