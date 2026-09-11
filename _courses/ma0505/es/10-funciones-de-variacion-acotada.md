---
layout: chapter
course: ma0505
chapter: 10
title: "Funciones de variación acotada"
slug: 10-funciones-de-variacion-acotada
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/10-funciones-de-variacion-acotada/
---

{% raw %}
## Motivación: longitud de curvas y masa de un alambre

Dos problemas geométricos muestran la necesidad de ampliar la clase de funciones tratables con la integral de Riemann. Considérese una curva continua $$\gamma : [a,b] \to \mathbb{R}^{2}$$, $$\gamma(t) = (\gamma_{1}(t), \gamma_{2}(t))$$. Dada una partición $$a = t_{0} < t_{1} < \dots < t_{n} = b$$, la poligonal de vértices $$\gamma(t_{i})$$ aproxima la curva, y su longitud es

$$
\sum_{i=0}^{n-1} \|\gamma(t_{i+1}) - \gamma(t_{i})\|.
$$

![Aproximación poligonal de una curva](/assets/img/courses/ma0505/variacion-acotada-poligonal.svg)

Si $$\gamma_{1}, \gamma_{2}$$ son diferenciables con derivada Riemann-integrable, el teorema del valor medio sugiere que la longitud es $$\int_{a}^{b} \|\gamma'(t)\|\,dt$$; pero en general no es claro siquiera que el conjunto de longitudes poligonales sea acotado. Un fenómeno análogo aparece al calcular la masa de un alambre de densidad $$\rho$$, que se aproxima por sumas $$\sum_{i} \rho(t_{i})\, A\, \|\gamma(t_{i+1}) - \gamma(t_{i})\|$$. En ambos casos la cantidad relevante es el supremo de sumas de incrementos $$\sum |f(t_{i+1}) - f(t_{i})|$$ sobre todas las particiones; las funciones para las que ese supremo es finito son el objeto de esta sección.

## Definición y primeros ejemplos

### Definición (Función de variación acotada y suma de incrementos)

Sea $$f : [a,b] \to \mathbb{R}$$. Para una partición $$\Gamma = \{ a = t_{0} < t_{1} < \dots < t_{n} = b\}$$ se define la *suma de incrementos*

$$
S(f, \Gamma) = \sum_{i=0}^{n-1} |f(t_{i+1}) - f(t_{i})|.
$$

Decimos que $$f$$ es de *variación acotada* si existe $$M > 0$$ tal que $$S(f, \Gamma) \leq M$$ para toda partición $$\Gamma$$; equivalentemente, si

$$
\sup_{\Gamma} S(f, \Gamma) < \infty.
$$

### Ejemplo (Toda función monótona es de variación acotada)

Si $$f$$ es creciente, los incrementos $$f(t_{i+1}) - f(t_{i})$$ son no negativos y la suma telescopia:

$$
S(f, \Gamma) = \sum_{i=0}^{n-1} \big(f(t_{i+1}) - f(t_{i})\big) = f(b) - f(a).
$$

Análogamente, si $$f$$ es decreciente, $$S(f, \Gamma) = f(a) - f(b)$$ para toda $$\Gamma$$. En ambos casos $$S(f, \Gamma)$$ no depende de $$\Gamma$$, de modo que $$f$$ es de variación acotada.

### Ejemplo (La indicadora de los irracionales no es de variación acotada)

Sea $$\varphi : [0,1] \to \mathbb{R}$$ con $$\varphi(x) = 0$$ si $$x \in \mathbb{Q}$$ y $$\varphi(x) = 1$$ si $$x \notin \mathbb{Q}$$. Dado $$n$$, escoja una partición $$\{x_{k}\}_{k=0}^{2n}$$ con $$x_{0} = 0$$, $$x_{2n} = 1$$, $$x_{2k} \in \mathbb{Q}$$ y $$x_{2k+1} \notin \mathbb{Q}$$. Cada incremento $$|\varphi(x_{k+1}) - \varphi(x_{k})|$$ vale $$1$$, de modo que

$$
S(\varphi, \Gamma) = \sum_{k=0}^{2n-1} |\varphi(x_{k+1}) - \varphi(x_{k})| = 2n.
$$

Como $$n$$ es arbitrario, $$\sup_{\Gamma} S(\varphi, \Gamma) = \infty$$ y $$\varphi$$ no es de variación acotada.

## La variación total

### Definición (Variación total)

Si $$f : [a,b] \to \mathbb{R}$$ es de variación acotada, su *variación total* sobre $$[a,b]$$ es

$$
\operatorname{Var}(f, [a,b]) = \sup_{\Gamma} S(f, \Gamma).
$$

### Proposición (Monotonía de la variación sobre subintervalos)

Sea $$f : [a,b] \to \mathbb{R}$$ de variación acotada y $$[a_{1}, b_{1}] \subseteq [a,b]$$. Entonces la restricción de $$f$$ a $$[a_{1}, b_{1}]$$ es de variación acotada y

$$
\operatorname{Var}(f, [a_{1}, b_{1}]) \leq \operatorname{Var}(f, [a,b]).
$$

***Prueba:*** Sea $$\Gamma_{1}$$ una partición de $$[a_{1}, b_{1}]$$ y considere la partición $$\Gamma = \Gamma_{1} \cup \{a, b\}$$ de $$[a,b]$$. Al añadir los extremos sólo se agregan sumandos no negativos, de modo que

$$
S(f, \Gamma_{1}) \leq S(f, \Gamma_{1}) + |f(a_{1}) - f(a)| + |f(b) - f(b_{1})| = S(f, \Gamma) \leq \operatorname{Var}(f, [a,b]).
$$

Tomando supremo sobre $$\Gamma_{1}$$ se obtiene $$\operatorname{Var}(f, [a_{1}, b_{1}]) \leq \operatorname{Var}(f, [a,b]) < \infty$$.

### Proposición (Las funciones de variación acotada son acotadas)

Si $$f : [a,b] \to \mathbb{R}$$ es de variación acotada, entonces para todo $$x \in [a,b]$$

$$
2|f(x)| \leq \operatorname{Var}(f, [a,b]) + |f(a)| + |f(b)|.
$$

En particular $$f$$ es acotada.

***Prueba:*** Para $$x \in (a,b)$$, la partición $$\{a, x, b\}$$ da

$$
|f(x) - f(a)| + |f(b) - f(x)| \leq \operatorname{Var}(f, [a,b]).
$$

Por la desigualdad triangular inversa, $$|f(x)| - |f(a)| \leq |f(x) - f(a)|$$ y $$|f(x)| - |f(b)| \leq |f(b) - f(x)|$$. Sumando,

$$
2|f(x)| - |f(a)| - |f(b)| \leq \operatorname{Var}(f, [a,b]),
$$

que es la desigualdad buscada (trivial en $$x = a, b$$). Luego $$|f(x)| \leq \tfrac{1}{2}\big(\operatorname{Var}(f,[a,b]) + |f(a)| + |f(b)|\big)$$ para todo $$x$$.

### Lema (Propiedades algebraicas de las funciones de variación acotada)

Sean $$f, g : [a,b] \to \mathbb{R}$$ de variación acotada. Entonces:

1. $$cf + g$$ es de variación acotada para todo $$c \in \mathbb{R}$$;
2. $$fg$$ es de variación acotada;
3. si existe $$\varepsilon > 0$$ con $$|g(x)| \geq \varepsilon$$ para todo $$x \in [a,b]$$, entonces $$1/g$$ es de variación acotada;
4. $$f$$ y $$g$$ son acotadas.

***Prueba:*** Ejercicio.

### Lema (Aditividad de la variación sobre subintervalos)

Sea $$f : [a,b] \to \mathbb{R}$$ de variación acotada y $$a < c < b$$. Entonces

$$
\operatorname{Var}(f, [a,b]) = \operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b]).
$$

***Prueba:*** *($$\leq$$).* Sea $$\Gamma = \{a = x_{0} < \dots < x_{n} = b\}$$ y sea $$\Gamma' = \Gamma \cup \{c\}$$, con $$x_{m_{0}} \leq c < x_{m_{0}+1}$$. Refinar añadiendo $$c$$ no disminuye la suma de incrementos:

$$
S(f, \Gamma) \leq S(f, \Gamma') = S(f, \Gamma_{1}) + S(f, \Gamma_{2}),
$$

donde $$\Gamma_{1} = (\Gamma' \cap [a,c]) \cup \{c\}$$ y $$\Gamma_{2} = \{c\} \cup (\Gamma' \cap [c,b])$$ son particiones de $$[a,c]$$ y $$[c,b]$$ respectivamente. Luego $$S(f, \Gamma) \leq \operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b])$$, y tomando supremo sobre $$\Gamma$$,

$$
\operatorname{Var}(f, [a,b]) \leq \operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b]).
$$

*($$\geq$$).* Si $$\Gamma_{1}$$ y $$\Gamma_{2}$$ son particiones de $$[a,c]$$ y $$[c,b]$$, entonces $$\Gamma = \Gamma_{1} \cup \Gamma_{2}$$ es una partición de $$[a,b]$$ y $$S(f, \Gamma_{1}) + S(f, \Gamma_{2}) = S(f, \Gamma) \leq \operatorname{Var}(f, [a,b])$$. Tomando supremo primero en $$\Gamma_{1}$$ y luego en $$\Gamma_{2}$$,

$$
\operatorname{Var}(f, [a,c]) + \operatorname{Var}(f, [c,b]) \leq \operatorname{Var}(f, [a,b]).
$$

## La descomposición de Jordan

### Notación (Parte positiva y negativa; variaciones positiva y negativa)

Para $$x \in \mathbb{R}$$ se define $$x^{+} = \max\{x, 0\}$$ y $$x^{-} = \max\{-x, 0\}$$; ambas son no negativas y

$$
x^{+} + x^{-} = |x|, \qquad x^{+} - x^{-} = x.
$$

Dada $$f : [a,b] \to \mathbb{R}$$ y una partición $$\Gamma = \{a = t_{0} < \dots < t_{n} = b\}$$, se definen

$$
P(f, \Gamma) = \sum_{i=0}^{n-1} \big(f(t_{i+1}) - f(t_{i})\big)^{+}, \qquad
N(f, \Gamma) = \sum_{i=0}^{n-1} \big(f(t_{i+1}) - f(t_{i})\big)^{-},
$$

y las *variaciones positiva y negativa* $$P(f, [a,b]) = \sup_{\Gamma} P(f, \Gamma)$$, $$N(f, [a,b]) = \sup_{\Gamma} N(f, \Gamma)$$.

### Lema (Relación entre variación total y variaciones positiva y negativa)

Sea $$f : [a,b] \to \mathbb{R}$$ de variación acotada. Entonces

$$
P(f, [a,b]) - N(f, [a,b]) = f(b) - f(a), \qquad P(f, [a,b]) + N(f, [a,b]) = \operatorname{Var}(f, [a,b]).
$$

Equivalentemente,

$$
P(f, [a,b]) = \tfrac{1}{2}\big(\operatorname{Var}(f, [a,b]) + f(b) - f(a)\big), \quad
N(f, [a,b]) = \tfrac{1}{2}\big(\operatorname{Var}(f, [a,b]) - f(b) + f(a)\big).
$$

***Prueba:*** Para cada partición $$\Gamma$$, usando $$x^{+} + x^{-} = |x|$$ y $$x^{+} - x^{-} = x$$ sobre cada incremento,

$$
P(f, \Gamma) + N(f, \Gamma) = S(f, \Gamma), \qquad
P(f, \Gamma) - N(f, \Gamma) = \sum_{i=0}^{n-1}\big(f(t_{i+1}) - f(t_{i})\big) = f(b) - f(a).
$$

De la segunda identidad, $$f(a) + P(f, \Gamma) = f(b) + N(f, \Gamma)$$; como el lado izquierdo y el derecho difieren en la constante $$f(b) - f(a)$$, tomar supremo en $$\Gamma$$ da $$f(a) + P(f, [a,b]) = f(b) + N(f, [a,b])$$, esto es, $$P(f, [a,b]) - N(f, [a,b]) = f(b) - f(a)$$. Además, de $$P(f,\Gamma) - N(f,\Gamma) = f(b) - f(a)$$ se obtiene $$S(f, \Gamma) = 2P(f, \Gamma) - (f(b) - f(a))$$; tomando supremo,

$$
\operatorname{Var}(f, [a,b]) = 2P(f, [a,b]) - (f(b) - f(a)),
$$

y combinando con $$P - N = f(b) - f(a)$$ resultan $$P + N = \operatorname{Var}(f, [a,b])$$ y las fórmulas cerradas para $$P$$ y $$N$$.

### Teorema (Caracterización de Jordan de la variación acotada)

Una función $$f : [a,b] \to \mathbb{R}$$ es de variación acotada si y sólo si $$f$$ es diferencia de dos funciones crecientes. Las funciones pueden tomarse, además, no negativas.

***Prueba:*** *($$\Rightarrow$$).* Defina $$P(x) = P(f, [a,x])$$ y $$N(x) = N(f, [a,x])$$ (con $$P(a) = N(a) = 0$$). Por el lema anterior aplicado a $$[a,x]$$,

$$
f(x) - f(a) = P(x) - N(x), \qquad \text{es decir} \qquad f(x) = \big(f(a) + P(x)\big) - N(x).
$$

Por la monotonía de la variación sobre subintervalos, $$P$$ y $$N$$ son crecientes y no negativas. Eligiendo una constante $$c \geq \max\{0, -f(a)\}$$, las funciones $$g = c + f(a) + P$$ y $$h = c + N$$ son crecientes, no negativas y $$f = g - h$$.

*($$\Leftarrow$$).* Si $$f = g - h$$ con $$g, h$$ crecientes, entonces $$g$$ y $$h$$ son de variación acotada (toda función monótona lo es) y, por el lema de propiedades algebraicas, $$f = g - h$$ también lo es.

## Discontinuidades y refinamiento de particiones

### Teorema (Las funciones de variación acotada tienen discontinuidades a lo sumo contables)

Sea $$f : [a,b] \to \mathbb{R}$$ de variación acotada. Entonces $$f$$ tiene a lo sumo un número contable de discontinuidades, y cada una es de salto o removible (esto es, existen los límites laterales $$f(x^{+})$$ y $$f(x^{-})$$ en todo punto).

***Prueba:*** Por la caracterización de Jordan, $$f = f_{1} - f_{2}$$ con $$f_{1}, f_{2}$$ crecientes; basta probar el enunciado para una función creciente $$g$$, pues la unión de dos conjuntos contables es contable y los límites laterales de $$g$$ existen por monotonía. Para $$k \geq 1$$ sea

$$
D_{k} = \big\{ x \in [a,b] : g(x^{+}) - g(x^{-}) \geq \tfrac{1}{k}\big\}.
$$

Si $$x_{0} < x_{1} < \dots < x_{m}$$ son puntos de $$D_{k}$$, se pueden intercalar $$y_{i}, z_{i}$$ con $$y_{i} < x_{i} < z_{i} = y_{i+1}$$, de modo que los saltos en los $$x_{i}$$ quedan dominados por incrementos disjuntos de $$g$$:

$$
\frac{m+1}{k} \leq \sum_{i=0}^{m} \big(g(z_{i}) - g(y_{i})\big) \leq g(b) - g(a).
$$

Por tanto $$D_{k}$$ es finito, con a lo sumo $$k\,(g(b) - g(a))$$ elementos. El conjunto de discontinuidades de $$g$$ es $$\bigcup_{k \geq 1} D_{k}$$, unión contable de conjuntos finitos, luego contable.

### Teorema (Aproximación de la variación total por particiones finas)

Sea $$f : [a,b] \to \mathbb{R}$$ continua y de variación acotada, y sea $$V = \operatorname{Var}(f, [a,b])$$. Para todo $$M < V$$ existe $$\delta > 0$$ tal que

$$
M < S(f, \Gamma) \leq V \qquad \text{para toda partición } \Gamma \text{ con } |\Gamma| < \delta,
$$

donde $$|\Gamma|$$ denota la norma (mayor longitud de subintervalo) de $$\Gamma$$.

***Prueba:*** La cota $$S(f, \Gamma) \leq V$$ es la definición de $$V$$. Fije $$\mu > 0$$ con $$M + \mu < V$$ y una partición $$\Gamma_{1} = \{a = \tilde{x}_{0} < \dots < \tilde{x}_{k} = b\}$$ tal que $$M + \mu < S(f, \Gamma_{1})$$. Como $$f$$ es uniformemente continua, existe $$\delta_{1} > 0$$ con

$$
|x - y| < \delta_{1} \implies |f(x) - f(y)| < \frac{\mu}{2(k+1)}.
$$

Sea $$\gamma = \min_{0 \leq j \leq k-1} |\tilde{x}_{j+1} - \tilde{x}_{j}|$$ y tome cualquier $$\Gamma$$ con $$|\Gamma| < \min\{\delta_{1}, \gamma\}$$. Entonces cada subintervalo de $$\Gamma$$ contiene a lo sumo un punto de $$\Gamma_{1}$$. Sea $$\Gamma_{2} = \Gamma \cup \Gamma_{1}$$; al pasar de $$\Gamma$$ a $$\Gamma_{2}$$ se insertan a lo sumo $$k+1$$ puntos, y cada inserción de un punto $$\tilde{x}$$ en un subintervalo $$[x_{j-1}, x_{j}]$$ reemplaza $$|f(x_{j}) - f(x_{j-1})|$$ por $$|f(x_{j}) - f(\tilde{x})| + |f(\tilde{x}) - f(x_{j-1})|$$, aumentando la suma en a lo sumo $$2\cdot \frac{\mu}{2(k+1)}$$. Por tanto

$$
S(f, \Gamma_{2}) \leq S(f, \Gamma) + (k+1)\cdot \frac{2\mu}{2(k+1)} = S(f, \Gamma) + \mu.
$$

Como $$\Gamma_{2}$$ refina a $$\Gamma_{1}$$, $$S(f, \Gamma_{1}) \leq S(f, \Gamma_{2})$$, de donde

$$
M < S(f, \Gamma_{1}) - \mu \leq S(f, \Gamma_{2}) - \mu \leq S(f, \Gamma).
$$

### Corolario (Variación total y derivada)

Sea $$f : [a,b] \to \mathbb{R}$$ con $$f'$$ continua en $$[a,b]$$. Entonces

$$
\operatorname{Var}(f, [a,b]) = \int_{a}^{b} |f'(x)|\,dx, \qquad
P(f, [a,b]) = \int_{a}^{b} \big(f'(x)\big)^{+} dx, \qquad
N(f, [a,b]) = \int_{a}^{b} \big(f'(x)\big)^{-} dx.
$$

***Prueba:*** Ejercicio.
{% endraw %}
