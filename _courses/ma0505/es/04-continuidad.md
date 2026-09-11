---
layout: chapter
course: ma0505
chapter: 4
title: "Continuidad"
slug: 04-continuidad
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/04-continuidad/
---

{% raw %}
## Definiciones y ejemplos

### Definición (Límite de una función entre espacios métricos)

Sean $$(X, d), (Y, \rho)$$ espacios métricos, $$f : X \to Y$$, $$a \in X$$ y $$\ell \in Y$$. Decimos que $$\lim_{z \to a} f(z) = \ell$$ si para todo $$\varepsilon > 0$$ existe $$\delta > 0$$ tal que

$$
0 < d(z, a) < \delta \implies \rho(f(z), \ell) < \varepsilon.
$$

Note que para definir el límite no es necesario que $$f$$ esté definida en $$a$$.

### Definición (Función continua)

La función $$f : X \to Y$$ es *continua* en $$a \in X$$ si $$\lim_{z \to a} f(z) = f(a)$$. Es decir, para todo $$\varepsilon > 0$$ existe $$\delta > 0$$ tal que

$$
d(z, a) < \delta \implies \rho(f(z), f(a)) < \varepsilon,
$$

o equivalentemente, $$f(B_{X}(a, \delta)) \subseteq B_{Y}(f(a), \varepsilon)$$. Decimos simplemente que $$f$$ es *continua* si lo es en todo punto de $$X$$.

### Definición (Función Lipschitz)

$$f : X \to Y$$ es *$$\lambda$$-Lipschitz* si para todos $$x, y \in X$$,

$$
\rho(f(x), f(y)) \leq \lambda\, d(x, y).
$$

Se dice simplemente que $$f$$ es *Lipschitz* si existe $$\lambda \geq 0$$ con tal propiedad.

### Ejemplo (La distancia a un punto es $$1$$-Lipschitz)

Sea $$(X, d)$$ un espacio métrico y $$a \in X$$. La función $$f(x) = d(x, a)$$ es $$1$$-Lipschitz, ya que de la desigualdad triangular

$$
|d(x, a) - d(y, a)| \leq d(x, y),
$$

es decir $$|f(x) - f(y)| \leq d(x, y)$$. En particular $$f$$ es continua.

## Caracterizaciones topológicas de la continuidad

### Lema (Continuidad y preimágenes de abiertos)

Si $$f : X \to Y$$ es continua y $$G \subseteq Y$$ es abierto, entonces $$f^{-1}(G)$$ es abierto en $$X$$.

***Prueba:*** Sea $$x_{0} \in f^{-1}(G)$$ y $$y_{0} = f(x_{0}) \in G$$. Como $$G$$ es abierto, existe $$\varepsilon > 0$$ con $$B_{Y}(y_{0}, \varepsilon) \subseteq G$$. Por continuidad de $$f$$ en $$x_{0}$$, existe $$\delta > 0$$ tal que $$f(B_{X}(x_{0}, \delta)) \subseteq B_{Y}(y_{0}, \varepsilon) \subseteq G$$, es decir $$B_{X}(x_{0}, \delta) \subseteq f^{-1}(G)$$.

### Teorema (Caracterizaciones de la continuidad)

Sea $$f : X \to Y$$. Son equivalentes:

1. $$f$$ es continua;
2. $$f^{-1}(G)$$ es abierto en $$X$$ para todo abierto $$G \subseteq Y$$;
3. $$f^{-1}(F)$$ es cerrado en $$X$$ para todo cerrado $$F \subseteq Y$$;
4. $$f(\overline{B}) \subseteq \overline{f(B)}$$ para todo $$B \subseteq X$$ (clausura en $$X$$ a la izquierda, en $$Y$$ a la derecha).

***Prueba:*** $$(1) \implies (2)$$: Demostrado en el lema anterior.

$$(2) \implies (1)$$: Dado $$\varepsilon > 0$$ y $$a \in X$$, $$B_{Y}(f(a), \varepsilon)$$ es abierto, por lo que $$f^{-1}(B_{Y}(f(a), \varepsilon))$$ es abierto. Como $$a \in f^{-1}(B_{Y}(f(a), \varepsilon))$$, existe $$\delta > 0$$ con $$B_{X}(a, \delta) \subseteq f^{-1}(B_{Y}(f(a), \varepsilon))$$, i.e. $$f(B_{X}(a, \delta)) \subseteq B_{Y}(f(a), \varepsilon)$$.

$$(2) \iff (3)$$: Si $$F \subseteq Y$$ es cerrado, entonces $$Y \setminus F$$ es abierto y $$f^{-1}(Y \setminus F) = X \setminus f^{-1}(F)$$. Por tanto $$f^{-1}(F)$$ es cerrado si y solo si $$f^{-1}(Y\setminus F)$$ es abierto.

$$(3) \iff (4)$$: $$f(\overline{B}) \subseteq \overline{f(B)}$$ para todo $$B$$ equivale a $$\overline{B} \subseteq f^{-1}(\overline{f(B)})$$ para todo $$B$$. Tomando $$B = f^{-1}(F)$$ con $$F$$ cerrado, se obtiene $$\overline{f^{-1}(F)} \subseteq f^{-1}(F)$$, esto es $$f^{-1}(F)$$ cerrado, y recíprocamente.

### Teorema (Caracterización por sucesiones)

Sea $$f : X \to Y$$ y $$a \in X$$. Entonces $$f$$ es continua en $$a$$ si y solo si para toda sucesión $$\{ x_{n}\}_{n \in \mathbb{N}} \subseteq X$$ con $$x_{n} \to a$$ se cumple $$f(x_{n}) \to f(a)$$.

***Prueba:*** $$(\implies)$$: Si $$x_{n} \to a$$ y $$\varepsilon > 0$$, por continuidad existe $$\delta > 0$$ con $$d(x, a) < \delta \implies \rho(f(x), f(a)) < \varepsilon$$. Tome $$n_{0}$$ tal que $$n \geq n_{0}$$ implique $$d(x_{n}, a) < \delta$$; entonces $$\rho(f(x_{n}), f(a)) < \varepsilon$$, esto es $$f(x_{n}) \to f(a)$$.

$$(\impliedby)$$: Si $$f$$ no fuese continua en $$a$$, existiría $$\varepsilon > 0$$ tal que para todo $$\delta > 0$$ existe $$x_{\delta} \in X$$ con $$d(x_{\delta}, a) < \delta$$ y $$\rho(f(x_{\delta}), f(a)) \geq \varepsilon$$. Tomando $$\delta = 1/n$$ se obtiene $$x_{n}$$ con $$d(x_{n}, a) < 1/n$$ y $$\rho(f(x_{n}), f(a)) \geq \varepsilon$$. Así $$x_{n} \to a$$ pero $$f(x_{n}) \not\to f(a)$$, contradicción.

## Homeomorfismos e isometrías

### Definición (Homeomorfismo)

Sea $$f : X \to Y$$. Decimos que $$f$$ es un *homeomorfismo* si $$f$$ es continua, biyectiva y $$f^{-1}$$ es continua. En tal caso, $$X$$ y $$Y$$ se dicen *homeomorfos*.

### Nota (Los homeomorfismos envían abiertos en abiertos)

Si $$f : X \to Y$$ es un homeomorfismo y $$A \subseteq X$$ es abierto, entonces $$f(A) = (f^{-1})^{-1}(A)$$ es abierto en $$Y$$.

### Ejercicio (Homeomorfismos preservan el interior)

Si $$f : X \to Y$$ es un homeomorfismo y $$A \subseteq X$$, entonces $$f(A^{\circ}) = (f(A))^{\circ}$$.

### Definición (Isometría)

Sea $$\phi : (X, d_X) \to (Y, d_Y)$$. Decimos que $$\phi$$ es una *isometría* si $$\phi$$ es sobreyectiva y preserva la métrica, es decir, si para todos $$x,y \in X$$,

$$
d_Y(\phi(x), \phi(y)) = d_X(x,y).
$$

### Nota (Toda isometría es biyectiva)

Si $$\phi : (X, d_X) \to (Y, d_Y)$$ es una isometría, entonces $$\phi$$ es inyectiva, pues si $$\phi(x) = \phi(y)$$ entonces $$d_Y(\phi(x),\phi(y))=d_X(x,y) = 0$$, de donde tenemos que $$x=y$$.
{% endraw %}
