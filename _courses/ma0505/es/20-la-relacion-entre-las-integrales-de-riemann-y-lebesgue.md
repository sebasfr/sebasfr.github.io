---
layout: chapter
course: ma0505
chapter: 20
title: "La relación entre las integrales de Riemann y Lebesgue"
slug: 20-la-relacion-entre-las-integrales-de-riemann-y-lebesgue
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/20-la-relacion-entre-las-integrales-de-riemann-y-lebesgue/
---

{% raw %}
## Particiones y funciones escalonadas

### Notación (Particiones y funciones escalonadas asociadas)

Sea $$f : [a,b] \to \mathbb{R}$$ acotada por $$M$$, es decir $$|f(x)| \leq M$$ en $$[a,b]$$, y sea

$$
\Gamma_{k} = \{ a = x_{0}^{k} < x_{1}^{k} < \dots < x_{n_{k}}^{k} = b \}
$$

una sucesión de particiones de $$[a,b]$$ tales que $$\Gamma_{k} \subseteq \Gamma_{k+1}$$ (cada una refina a la anterior) y cuya malla $$|\Gamma_{k}| = \max_{i} (x_{i}^{k} - x_{i-1}^{k})$$ tiende a cero. Escribiendo $$x_{i} = x_{i}^{k}$$ y $$n = n_{k}$$ para aligerar la notación, consideremos:

1. si $$m_{i} = \inf_{[x_{i-1},x_{i}]} f(x)$$, la *escalonada inferior*

    $$
    \ell_{k}(x) = \sum_{i=1}^{n-1} m_{i} \mathbf{1}_{[x_{i-1},x_{i})} + m_{n} \mathbf{1}_{[x_{n-1},x_{n}]};
    $$
2. si $$M_{i} = \sup_{[x_{i-1},x_{i}]} f(x)$$, la *escalonada superior*

    $$
    u_{k}(x) = \sum_{i=1}^{n-1} M_{i} \mathbf{1}_{[x_{i-1},x_{i})} + M_{n} \mathbf{1}_{[x_{n-1},x_{n}]}.
    $$

Las integrales de estas funciones simples son las sumas de Darboux:

$$
\int_{[a,b]} \ell_{k}(x) \, dx = \sum_{i=1}^{n} m_{i} (x_{i} - x_{i-1}), \qquad \int_{[a,b]} u_{k}(x) \, dx = \sum_{i=1}^{n} M_{i} (x_{i} - x_{i-1}).
$$

### Nota (Monotonía de las escalonadas bajo refinamiento)

Note que

$$
\ell_{k}(x) \leq f(x) \leq u_{k}(x) \quad \text{para todo } x \in [a,b].
$$

Recordemos que si $$\Gamma_{k} \subseteq \Gamma_{k+1}$$, entonces

1. $$\ell_{k} \leq \ell_{k+1}$$;
2. $$u_{k} \geq u_{k+1}$$.

Como $$|f(x)| \leq M$$ para $$x \in [a,b]$$, entonces $$|\ell_{k}| \leq M$$ y $$|u_{k}| \leq M$$ en $$[a,b]$$. Por monotonía y acotación, existen los límites puntuales

$$
\ell = \lim_{k \to \infty} \ell_{k}, \qquad u = \lim_{k \to \infty} u_{k},
$$

que son medibles por ser límites de medibles, y satisfacen $$\ell(x) \leq f(x) \leq u(x)$$ para todo $$x \in [a,b]$$.

### Proposición (Las sumas de Darboux convergen a las integrales de $$\ell$$ y $$u$$)

Con la notación anterior,

$$
\lim_{k \to \infty} \int_{[a,b]} \ell_{k}(x) \, dx = \int_{[a,b]} \ell(x) \, dx, \qquad \lim_{k \to \infty} \int_{[a,b]} u_{k}(x) \, dx = \int_{[a,b]} u(x) \, dx.
$$

Es decir, estas integrales son el límite de las sumas inferiores y superiores de Darboux. Además,

$$
\int_{[a,b]} u(x) \, dx = \int_{[a,b]} \ell(x) \, dx \iff \int_{[a,b]} \big( u(x) - \ell(x) \big) \, dx = 0 \iff u = \ell \ \text{c.p.d.}
$$

***Prueba:*** Las funciones $$\ell_{k} + M$$ y $$u_{k} + M$$ son medibles, no negativas, convergen puntualmente a $$\ell + M$$ y $$u + M$$ respectivamente, y están dominadas por la constante $$2M$$, que es integrable en $$[a,b]$$ pues $$m([a,b]) = b - a < \infty$$. El teorema de convergencia dominada implica entonces que

$$
\lim_{k \to \infty} \int_{[a,b]} (\ell_{k} + M) \, dx = \int_{[a,b]} (\ell + M) \, dx,
$$

y restando la constante $$M(b-a)$$ de ambos lados (linealidad) se obtiene la afirmación para $$\ell_{k}$$; el argumento para $$u_{k}$$ es idéntico.

Para las equivalencias: como $$u - \ell \geq 0$$ y ambas son integrables (están acotadas por $$M$$ en un dominio de medida finita), la linealidad da

$$
\int_{[a,b]} u \, dx - \int_{[a,b]} \ell \, dx = \int_{[a,b]} (u - \ell) \, dx,
$$

así que la primera equivalencia es inmediata. La segunda es el corolario de la desigualdad de Markov: una función no negativa tiene integral nula si y solo si es nula c.p.d.

### Nota (Si las sumas coinciden, la integral de Riemann es la de Lebesgue)

Concluimos que, si las sumas inferiores y superiores de Darboux convergen al mismo valor, entonces

$$
u = \ell = f \quad \text{c.p.d.}
$$

(pues $$\ell \leq f \leq u$$), la función $$f$$ es medible por coincidir c.p.d. con la función medible $$\ell$$, y por lo tanto

$$
\lim_{k \to \infty} \sum_{i=1}^{n} m_{i} (x_{i} - x_{i-1}) = \lim_{k \to \infty} \sum_{i=1}^{n} M_{i} (x_{i} - x_{i-1}) = \int_{[a,b]} f(x) \, dx,
$$

donde la integral es la de Lebesgue. Es decir, cuando $$f$$ es Riemann integrable, su integral de Riemann coincide con su integral de Lebesgue.

## La caracterización de Lebesgue de la integrabilidad de Riemann

### Teorema (Criterio de Lebesgue: Riemann integrable equivale a continua c.p.d.)

Sea $$f : [a,b] \to \mathbb{R}$$ acotada. Entonces son equivalentes:

1. $$f$$ es Riemann integrable;
2. $$f$$ es continua c.p.d. en $$[a,b]$$.

En tal caso, las integrales de Riemann y de Lebesgue de $$f$$ sobre $$[a,b]$$ coinciden.

***Prueba:*** Fijamos una sucesión de particiones $$\Gamma_{k}$$ con $$\Gamma_{k} \subseteq \Gamma_{k+1}$$ y $$\lim_{k \to \infty} |\Gamma_{k}| = 0$$, y usamos la notación de la subsección anterior.

*(i) implica (ii).* Comenzamos asumiendo que $$f$$ es Riemann integrable; entonces las sumas inferiores y superiores convergen ambas a la integral de Riemann, y por la proposición anterior $$u = \ell = f$$ c.p.d. Sea

$$
Z = \{ \ell \neq f \} \cup \{ \ell \neq u \} \cup \{ f \neq u \} \cup \bigcup_{k=1}^{\infty} \Gamma_{k}.
$$

Entonces $$m(Z) = 0$$, pues es unión numerable de conjuntos nulos: los tres primeros por lo anterior, y cada $$\Gamma_{k}$$ por ser finito. Si $$x \notin Z$$, entonces

$$
u(x) = \ell(x) = f(x), \qquad x \notin \Gamma_{k} \ \text{para todo } k \geq 1.
$$

Afirmamos que $$f$$ es continua en cada $$x \notin Z$$. Supongamos que $$f$$ no es continua en $$x$$. Entonces existe un $$\varepsilon > 0$$ tal que para todo $$\delta > 0$$ existe $$x_{\delta}$$ con

$$
|x_{\delta} - x| < \delta \qquad \text{y} \qquad |f(x) - f(x_{\delta})| > \varepsilon.
$$

Dado $$k$$, como $$x \notin \Gamma_{k}$$, existen nodos consecutivos $$x_{i-1}^{k}, x_{i}^{k}$$ tales que $$x \in (x_{i-1}^{k}, x_{i}^{k})$$, que es abierto. Tomemos $$\delta > 0$$ tal que

$$
(x - \delta, x + \delta) \subseteq (x_{i-1}^{k}, x_{i}^{k}).
$$

Entonces $$x_{\delta} \in (x_{i-1}^{k}, x_{i}^{k})$$ y, como ambos puntos pertenecen al mismo subintervalo de la partición,

$$
\varepsilon < |f(x) - f(x_{\delta})| \leq M_{i} - m_{i} = u_{k}(x) - \ell_{k}(x).
$$

Como esto vale para todo $$k$$, haciendo $$k \to \infty$$ obtenemos

$$
u(x) - \ell(x) \geq \varepsilon > 0,
$$

lo que contradice $$u(x) = \ell(x)$$. Concluimos que $$f$$ es continua en todo punto fuera del conjunto nulo $$Z$$, es decir, $$f$$ es continua c.p.d.

*(ii) implica (i).* Asumamos ahora que

$$
Z = \{ x \in [a,b] :\ f\ \text{es discontinua en } x \}
$$

es de medida cero. Sean $$x \notin Z \cup \{a, b\}$$ y $$\varepsilon > 0$$. Por continuidad de $$f$$ en $$x$$, existe $$\delta > 0$$ tal que

$$
|x - y| < \delta \implies |f(x) - f(y)| < \frac{\varepsilon}{2}.
$$

Tome ahora $$k_{0}$$ tal que

$$
|\Gamma_{k}| < \frac{\delta}{2} \quad \text{si } k \geq k_{0}.
$$

Para $$k \geq k_{0}$$, sea $$i$$ tal que $$x \in [x_{i-1}, x_{i})$$. Entonces todo punto $$y$$ del subintervalo cerrado $$[x_{i-1}, x_{i}]$$ satisface $$|y - x| \leq x_{i} - x_{i-1} \leq |\Gamma_{k}| < \delta$$, es decir,

$$
[x_{i-1}, x_{i}] \subseteq (x - \delta, x + \delta).
$$

Por lo tanto,

$$
f(x) - \frac{\varepsilon}{2} \leq f(y) \leq f(x) + \frac{\varepsilon}{2} \quad \text{para } y \in [x_{i-1}, x_{i}],
$$

y tomando ínfimo y supremo sobre ese subintervalo,

$$
f(x) - \frac{\varepsilon}{2} \leq m_{i} \leq M_{i} \leq f(x) + \frac{\varepsilon}{2}.
$$

Es decir, para $$k \geq k_{0}$$,

$$
|u_{k}(x) - f(x)| \leq \frac{\varepsilon}{2} < \varepsilon, \qquad |\ell_{k}(x) - f(x)| \leq \frac{\varepsilon}{2} < \varepsilon.
$$

Lo anterior nos dice que

$$
\lim_{k \to \infty} \ell_{k}(x) = f(x), \qquad \lim_{k \to \infty} u_{k}(x) = f(x)
$$

para todo $$x$$ fuera del conjunto nulo $$Z \cup \{a,b\}$$, es decir, $$\ell = u = f$$ c.p.d.; en particular $$f$$ es medible. Por el teorema de convergencia dominada (aplicado como en la proposición anterior, con dominación por la constante $$M$$ en el dominio de medida finita $$[a,b]$$), se cumple que

$$
\lim_{k \to \infty} \int_{[a,b]} \ell_{k}(x) \, dx = \int_{[a,b]} f(x) \, dx, \qquad \lim_{k \to \infty} \int_{[a,b]} u_{k}(x) \, dx = \int_{[a,b]} f(x) \, dx.
$$

Es decir, las sumas inferiores y superiores de Darboux convergen ambas al mismo valor; en particular, dado $$\varepsilon > 0$$ existe una partición cuya suma superior y suma inferior difieren en menos de $$\varepsilon$$, y por el criterio de Darboux $$f$$ es Riemann integrable. En conclusión, $$f$$ es Riemann integrable y las integrales de Riemann y Lebesgue concuerdan.
{% endraw %}
