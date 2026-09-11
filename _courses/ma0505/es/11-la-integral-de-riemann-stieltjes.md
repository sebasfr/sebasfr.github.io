---
layout: chapter
course: ma0505
chapter: 11
title: "La integral de Riemann–Stieltjes"
slug: 11-la-integral-de-riemann-stieltjes
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/11-la-integral-de-riemann-stieltjes/
---

{% raw %}
## Sumas y definición de la integral

### Definición (Suma de Riemann–Stieltjes)

Sean $$f, \phi : [a,b] \to \mathbb{R}$$ con $$f$$ acotada. Dada una partición $$\Gamma = \{a = x_{0} < x_{1} < \dots < x_{n} = b\}$$ y puntos intermedios $$\xi_{i} \in [x_{i-1}, x_{i}]$$ para $$1 \leq i \leq n$$, la *suma de Riemann–Stieltjes* de $$f$$ respecto de $$\phi$$ es

$$
R(f, \Gamma, \phi) = \sum_{i=1}^{n} f(\xi_{i})\,\big[\phi(x_{i}) - \phi(x_{i-1})\big].
$$

### Definición (Integral de Riemann–Stieltjes)

Decimos que $$f$$ es *Riemann–Stieltjes integrable* respecto de $$\phi$$ en $$[a,b]$$ si existe $$I \in \mathbb{R}$$ tal que para todo $$\varepsilon > 0$$ existe $$\delta > 0$$ con

$$
|\Gamma| < \delta \implies |R(f, \Gamma, \phi) - I| < \varepsilon
$$

para cualquier elección de puntos intermedios $$\xi_{1}, \dots, \xi_{n}$$, donde $$|\Gamma| = \max_{i}(x_{i} - x_{i-1})$$. En tal caso se escribe $$I = \int_{a}^{b} f \, d\phi$$.

### Ejercicio (Criterio de Cauchy para la integrabilidad de Riemann–Stieltjes)

Pruebe que $$f$$ es Riemann–Stieltjes integrable respecto de $$\phi$$ si y sólo si para todo $$\varepsilon > 0$$ existe $$\delta > 0$$ tal que

$$
|\Gamma| < \delta \ \text{ y }\ |\Gamma'| < \delta \implies |R(f, \Gamma, \phi) - R(f, \Gamma', \phi)| < \varepsilon
$$

para cualesquiera elecciones de puntos intermedios.

### Lema (Una discontinuidad común impide la integrabilidad)

Sean $$\phi : [a,b] \to \mathbb{R}$$ y $$f : [a,b] \to \mathbb{R}$$ acotada. Si existe $$z_{0} \in (a,b)$$ donde tanto $$f$$ como $$\phi$$ son discontinuas, entonces $$f$$ no es Riemann–Stieltjes integrable respecto de $$\phi$$.

***Prueba:*** Se muestra que falla el criterio de Cauchy. Como $$f$$ y $$\phi$$ son discontinuas en $$z_{0}$$, existe $$\varepsilon > 0$$ tal que, para todo $$\delta > 0$$, hay un punto $$w_{\delta}$$ con $$0 < |w_{\delta} - z_{0}| < \delta$$ y $$|\phi(w_{\delta}) - \phi(z_{0})| \geq \sqrt{\varepsilon}$$, y un punto $$\xi_{\delta}$$ con $$|\xi_{\delta} - z_{0}| < |w_{\delta} - z_{0}|$$ y $$|f(\xi_{\delta}) - f(z_{0})| \geq \sqrt{\varepsilon}$$; en particular $$\xi_{\delta}$$ queda estrictamente entre $$z_{0}$$ y $$w_{\delta}$$. Tome una partición $$\Gamma$$ con $$|\Gamma| < \delta$$ que tenga a $$z_{0}$$ y a $$w_{\delta}$$ como nodos consecutivos $$x_{i_{0}-1} = z_{0}$$, $$x_{i_{0}} = w_{\delta}$$, de modo que $$\xi_{\delta} \in (x_{i_{0}-1}, x_{i_{0}})$$. Construya dos sumas de Riemann–Stieltjes con la misma $$\Gamma$$ y los mismos puntos intermedios salvo en el subintervalo $$[x_{i_{0}-1}, x_{i_{0}}]$$, donde una toma $$\xi_{i_{0}} = \xi_{\delta}$$ y la otra $$\xi_{i_{0}} = z_{0}$$. Entonces

$$
|R(f, \Gamma, \phi) - R'(f, \Gamma, \phi)| = |f(\xi_{\delta}) - f(z_{0})|\,|\phi(x_{i_{0}}) - \phi(x_{i_{0}-1})| = |f(\xi_{\delta}) - f(z_{0})|\,|\phi(w_{\delta}) - \phi(z_{0})| \geq \sqrt{\varepsilon}\cdot\sqrt{\varepsilon} = \varepsilon.
$$

Así, para todo $$\delta > 0$$ hay sumas con norma menor que $$\delta$$ que difieren en al menos $$\varepsilon$$, y el criterio de Cauchy falla. El caso en que los testigos $$w_{\delta}$$ (de $$\phi$$) y $$\xi_{\delta}$$ (de $$f$$) no pueden tomarse del mismo lado de $$z_{0}$$ se trata de forma análoga y queda como ejercicio.

## Sumas superiores e inferiores

### Definición (Sumas inferior y superior de Darboux–Stieltjes)

Sea $$f : [a,b] \to \mathbb{R}$$ acotada y $$\Gamma = \{a = x_{0} < \dots < x_{n} = b\}$$. Para $$1 \leq i \leq n$$ sean

$$
m_{i} = \inf_{x_{i-1} \leq \xi \leq x_{i}} f(\xi), \qquad M_{i} = \sup_{x_{i-1} \leq \xi \leq x_{i}} f(\xi).
$$

Las *sumas inferior y superior* respecto de $$\phi$$ son

$$
L(f, \Gamma, \phi) = \sum_{i=1}^{n} m_{i}\,\big[\phi(x_{i}) - \phi(x_{i-1})\big], \qquad
U(f, \Gamma, \phi) = \sum_{i=1}^{n} M_{i}\,\big[\phi(x_{i}) - \phi(x_{i-1})\big].
$$

### Nota (Encaje de las sumas y caso de Riemann)

Si $$\phi$$ es creciente, entonces $$\phi(x_{i}) - \phi(x_{i-1}) \geq 0$$ y para toda elección de puntos intermedios

$$
L(f, \Gamma, \phi) \leq R(f, \Gamma, \phi) \leq U(f, \Gamma, \phi).
$$

Si $$\phi(x) = x$$ se recuperan las sumas y la integral de Riemann usuales.

### Lema (Propiedades de monotonía de las sumas de Darboux–Stieltjes)

Sea $$f : [a,b] \to \mathbb{R}$$ acotada y $$\phi : [a,b] \to \mathbb{R}$$ creciente.

1. Si $$\Gamma_{1} \subseteq \Gamma_{2}$$ (refinamiento), entonces $$L(f, \Gamma_{1}, \phi) \leq L(f, \Gamma_{2}, \phi)$$ y $$U(f, \Gamma_{2}, \phi) \leq U(f, \Gamma_{1}, \phi)$$.
2. Para cualesquiera particiones $$\Gamma_{1}, \Gamma_{2}$$, $$\ L(f, \Gamma_{1}, \phi) \leq U(f, \Gamma_{2}, \phi)$$.

***Prueba:*** *(1).* Basta insertar un punto $$y$$ en un subintervalo $$[x_{i-1}, x_{i}]$$ de $$\Gamma_{1}$$. Como

$$
\sup_{[x_{i-1}, y]} f, \ \sup_{[y, x_{i}]} f \ \leq\ \sup_{[x_{i-1}, x_{i}]} f,
$$

y $$\phi(y) - \phi(x_{i-1}) \geq 0$$, $$\phi(x_{i}) - \phi(y) \geq 0$$ con suma $$\phi(x_{i}) - \phi(x_{i-1})$$, se obtiene

$$
\big(\textstyle\sup_{[x_{i-1}, y]} f\big)\big(\phi(y) - \phi(x_{i-1})\big) + \big(\textstyle\sup_{[y, x_{i}]} f\big)\big(\phi(x_{i}) - \phi(y)\big) \leq \big(\textstyle\sup_{[x_{i-1}, x_{i}]} f\big)\big(\phi(x_{i}) - \phi(x_{i-1})\big),
$$

es decir, el refinamiento sólo puede disminuir $$U$$. Iterando sobre los puntos añadidos, $$U(f, \Gamma_{2}, \phi) \leq U(f, \Gamma_{1}, \phi)$$. El argumento para $$L$$ (con ínfimos) es simétrico y da $$L(f, \Gamma_{1}, \phi) \leq L(f, \Gamma_{2}, \phi)$$.

*(2).* Sea $$\Gamma = \Gamma_{1} \cup \Gamma_{2}$$, refinamiento común. Por (1) y la nota anterior,

$$
L(f, \Gamma_{1}, \phi) \leq L(f, \Gamma, \phi) \leq U(f, \Gamma, \phi) \leq U(f, \Gamma_{2}, \phi).
$$

## Existencia de la integral

### Nota (Reducción al integrador creciente)

A partir de la definición se verifica que si $$\int_{a}^{b} f\,d\phi_{1}$$ y $$\int_{a}^{b} f\,d\phi_{2}$$ existen y $$\phi = \phi_{1} - \phi_{2}$$, entonces $$\int_{a}^{b} f\,d\phi$$ existe y

$$
\int_{a}^{b} f\,d\phi = \int_{a}^{b} f\,d\phi_{1} - \int_{a}^{b} f\,d\phi_{2}.
$$

Como toda función de variación acotada es diferencia de dos funciones crecientes (caracterización de Jordan), el estudio de la integrabilidad respecto de un integrador de variación acotada se reduce al caso en que $$\phi$$ es creciente.

### Teorema (Existencia de la integral para integrando continuo e integrador de variación acotada)

Sea $$f : [a,b] \to \mathbb{R}$$ continua y $$\phi : [a,b] \to \mathbb{R}$$ de variación acotada. Entonces $$\int_{a}^{b} f\,d\phi$$ existe y

$$
\left| \int_{a}^{b} f\,d\phi \right| \leq \Big(\sup_{[a,b]} |f|\Big)\,\operatorname{Var}(\phi, [a,b]).
$$

***Prueba:*** Por la nota anterior basta probar la existencia cuando $$\phi$$ es creciente; si $$\phi$$ es constante toda suma es nula y la integral vale $$0$$, así que suponemos $$\phi(b) > \phi(a)$$. Sea $$\varepsilon > 0$$. Como $$f$$ es uniformemente continua, existe $$\delta_{1} > 0$$ tal que

$$
|x - y| < \delta_{1} \implies |f(x) - f(y)| < \frac{\varepsilon}{2\big(\phi(b) - \phi(a)\big)}.
$$

*Las sumas superior e inferior se aproximan.* Si $$|\Gamma| < \delta_{1}$$, por continuidad existen $$\xi_{i}, \eta_{i} \in [x_{i-1}, x_{i}]$$ con $$f(\xi_{i}) = M_{i}$$, $$f(\eta_{i}) = m_{i}$$; como $$|\xi_{i} - \eta_{i}| \leq |\Gamma| < \delta_{1}$$,

$$
U(f, \Gamma, \phi) - L(f, \Gamma, \phi) = \sum_{i=1}^{n} (M_{i} - m_{i})\big(\phi(x_{i}) - \phi(x_{i-1})\big) \leq \frac{\varepsilon}{2(\phi(b) - \phi(a))}\big(\phi(b) - \phi(a)\big) = \frac{\varepsilon}{2}.
$$

*Estabilidad de $$U$$.* Si $$|\Gamma| < \delta_{1}$$ y $$|\Gamma'| < \delta_{1}$$, usando $$U - L \leq \varepsilon/2$$ y $$L(f, \cdot, \phi) \leq U(f, \cdot, \phi)$$ entre particiones distintas,

$$
U(f, \Gamma, \phi) \leq L(f, \Gamma, \phi) + \tfrac{\varepsilon}{2} \leq U(f, \Gamma', \phi) + \tfrac{\varepsilon}{2},
$$

y simétricamente, de modo que $$|U(f, \Gamma, \phi) - U(f, \Gamma', \phi)| \leq \varepsilon/2$$.

*Construcción del límite.* Tome particiones $$\{\Gamma_{k}\}_{k=1}^{\infty}$$ con $$|\Gamma_{k}| \to 0$$ y sea $$\Gamma_{k}' = \bigcup_{j=1}^{k} \Gamma_{j}$$, de modo que $$\Gamma_{k}' \subseteq \Gamma_{k+1}'$$ y $$\Gamma_{k} \subseteq \Gamma_{k}'$$. Por la monotonía (1), $$\{U(f, \Gamma_{k}', \phi)\}_{k}$$ es decreciente y acotada inferiormente (por cualquier suma inferior), así que

$$
U := \inf_{k \geq 1} U(f, \Gamma_{k}', \phi) = \lim_{k \to \infty} U(f, \Gamma_{k}', \phi)
$$

existe. Dado $$\varepsilon$$, sea $$k_{0}$$ con $$0 \leq U(f, \Gamma_{k}', \phi) - U < \varepsilon/2$$ para $$k \geq k_{0}$$, y $$k_{1}$$ con $$|\Gamma_{k}| < \delta_{1}$$ para $$k \geq k_{1}$$. Como $$\Gamma_{k} \subseteq \Gamma_{k}'$$ y ambas tienen norma $$< \delta_{1}$$, la estabilidad de $$U$$ da $$|U(f, \Gamma_{k}, \phi) - U(f, \Gamma_{k}', \phi)| \leq \varepsilon/2$$, luego para $$k \geq \max\{k_{0}, k_{1}\}$$,

$$
|U(f, \Gamma_{k}, \phi) - U| \leq |U(f, \Gamma_{k}, \phi) - U(f, \Gamma_{k}', \phi)| + |U(f, \Gamma_{k}', \phi) - U| < \varepsilon.
$$

*Independencia de la sucesión.* Si $$\{\widetilde{\Gamma}_{k}\}$$ es otra sucesión con $$|\widetilde{\Gamma}_{k}| \to 0$$, para $$k$$ grande ambas normas son $$< \delta_{1}$$ y la estabilidad de $$U$$ da $$|U(f, \Gamma_{k}, \phi) - U(f, \widetilde{\Gamma}_{k}, \phi)| \leq \varepsilon/2$$; luego $$U(f, \widetilde{\Gamma}_{k}, \phi) \to U$$ también. Así, $$U(f, \Gamma, \phi) \to U$$ cuando $$|\Gamma| \to 0$$.

*Conclusión.* Ya se mostró que $$U(f, \Gamma, \phi) \to U$$ cuando $$|\Gamma| \to 0$$. Además, para $$|\Gamma| < \delta_{1}$$ se tiene $$L(f, \Gamma, \phi) \geq U(f, \Gamma, \phi) - \tfrac{\varepsilon}{2}$$, de modo que también $$L(f, \Gamma, \phi) \to U$$. El encaje $$L(f, \Gamma, \phi) \leq R(f, \Gamma, \phi) \leq U(f, \Gamma, \phi)$$ da entonces $$R(f, \Gamma, \phi) \to U$$ cuando $$|\Gamma| \to 0$$. Por tanto $$\int_{a}^{b} f\,d\phi = U$$ existe. Finalmente, para $$\phi$$ de variación acotada y cualquier $$\Gamma$$,

$$
|R(f, \Gamma, \phi)| \leq \Big(\sup_{[a,b]}|f|\Big)\sum_{i=1}^{n}|\phi(x_{i}) - \phi(x_{i-1})| \leq \Big(\sup_{[a,b]}|f|\Big)\operatorname{Var}(\phi, [a,b]),
$$

y pasando al límite se obtiene la cota anunciada.

## Propiedades: linealidad, valor medio e integración por partes

### Teorema (Linealidad de la integral de Riemann–Stieltjes)

Sean $$f_{1}, f_{2} : [a,b] \to \mathbb{R}$$ Riemann–Stieltjes integrables respecto de $$\phi_{1}, \phi_{2} : [a,b] \to \mathbb{R}$$, $$c \in \mathbb{R}$$ y $$a < c' < b$$. Entonces:

1. $$\displaystyle \int_{a}^{b}(c f_{1} + f_{2})\,d\phi_{1} = c\int_{a}^{b} f_{1}\,d\phi_{1} + \int_{a}^{b} f_{2}\,d\phi_{1}$$;
2. $$\displaystyle \int_{a}^{b} f_{1}\,d(c\phi_{1}) = c\int_{a}^{b} f_{1}\,d\phi_{1}$$;
3. $$\displaystyle \int_{a}^{b} f_{1}\,d(\phi_{1} + \phi_{2}) = \int_{a}^{b} f_{1}\,d\phi_{1} + \int_{a}^{b} f_{1}\,d\phi_{2}$$;
4. $$\displaystyle \int_{a}^{b} f_{1}\,d\phi_{1} = \int_{a}^{c'} f_{1}\,d\phi_{1} + \int_{c'}^{b} f_{1}\,d\phi_{1}$$.

***Prueba:*** Ejercicio.

### Nota (Cotas por el supremo y el ínfimo del integrando)

Si $$\phi$$ es creciente, de $$L(f, \Gamma, \phi) \leq R(f, \Gamma, \phi) \leq U(f, \Gamma, \phi)$$, $$U(f, \Gamma, \phi) \leq (\phi(b) - \phi(a))\sup_{[a,b]} f$$ y $$L(f, \Gamma, \phi) \geq (\phi(b) - \phi(a))\inf_{[a,b]} f$$ se obtiene, pasando al límite,

$$
\Big(\inf_{[a,b]} f\Big)\big(\phi(b) - \phi(a)\big) \leq \int_{a}^{b} f\,d\phi \leq \Big(\sup_{[a,b]} f\Big)\big(\phi(b) - \phi(a)\big).
$$

### Lema (Teorema del valor medio para la integral de Riemann–Stieltjes)

Sean $$f : [a,b] \to \mathbb{R}$$ continua y $$\phi : [a,b] \to \mathbb{R}$$ creciente, con $$f$$ Riemann–Stieltjes integrable respecto de $$\phi$$. Entonces existe $$\xi \in [a,b]$$ tal que

$$
\int_{a}^{b} f\,d\phi = f(\xi)\big(\phi(b) - \phi(a)\big).
$$

***Prueba:*** Si $$\phi(b) = \phi(a)$$, las cotas de la nota anterior dan $$\int_{a}^{b} f\,d\phi = 0$$ y cualquier $$\xi$$ sirve. Si $$\phi(b) > \phi(a)$$, dividiendo las mismas cotas entre $$\phi(b) - \phi(a)$$,

$$
\inf_{[a,b]} f \ \leq\ \frac{1}{\phi(b) - \phi(a)}\int_{a}^{b} f\,d\phi \ \leq\ \sup_{[a,b]} f.
$$

Como $$f$$ es continua en el compacto $$[a,b]$$, alcanza su ínfimo y su supremo, y por el teorema del valor intermedio toma todo valor entre ellos; en particular existe $$\xi \in [a,b]$$ donde $$f(\xi)$$ iguala el cociente anterior, lo que da la identidad.

### Teorema (Integración por partes)

Si $$\int_{a}^{b} f\,d\phi$$ existe, entonces $$\int_{a}^{b} \phi\,df$$ existe y

$$
\int_{a}^{b} f\,d\phi + \int_{a}^{b} \phi\,df = f(b)\phi(b) - f(a)\phi(a).
$$

***Prueba:*** Sea $$\Gamma = \{a = x_{0} < \dots < x_{n} = b\}$$ con puntos intermedios $$\xi_{i} \in [x_{i-1}, x_{i}]$$. Considere los puntos $$\xi_{0} = a$$, $$\xi_{n+1} = b$$ y la partición $$\Gamma' = \{\xi_{0}, \xi_{1}, \dots, \xi_{n+1}\}$$, que satisface $$x_{i-1} \leq \xi_{i} \leq x_{i} \leq \xi_{i+1}$$, de modo que cada $$x_{i}$$ es un punto intermedio válido de $$\Gamma'$$. Por sumación por partes (Abel),

$$
R(f, \Gamma, \phi) = \sum_{i=1}^{n} f(\xi_{i})\big(\phi(x_{i}) - \phi(x_{i-1})\big) = -\sum_{i=0}^{n} \phi(x_{i})\big(f(\xi_{i+1}) - f(\xi_{i})\big) + f(b)\phi(b) - f(a)\phi(a),
$$

es decir, $$R(f, \Gamma, \phi) = -R(\phi, \Gamma', f) + f(b)\phi(b) - f(a)\phi(a)$$, donde $$R(\phi, \Gamma', f)$$ es una suma de Riemann–Stieltjes de $$\phi$$ respecto de $$f$$ con la partición $$\Gamma'$$ y puntos intermedios $$x_{i}$$. Como $$\xi_{i} \in [x_{i-1}, x_{i}]$$, cada brecha cumple $$\xi_{i+1} - \xi_{i} \leq x_{i+1} - x_{i-1} \leq 2|\Gamma|$$, de modo que $$|\Gamma'| \leq 2|\Gamma| \to 0$$. Como $$\int_{a}^{b} f\,d\phi$$ existe, $$R(f, \Gamma, \phi) \to \int_{a}^{b} f\,d\phi$$ cuando $$|\Gamma| \to 0$$, y la identidad algebraica anterior fuerza $$R(\phi, \Gamma', f) \to f(b)\phi(b) - f(a)\phi(a) - \int_{a}^{b} f\,d\phi$$. Como $$|\Gamma'| \to 0$$ y este límite no depende de la sucesión de particiones elegida, $$\int_{a}^{b} \phi\,df$$ existe e iguala $$f(b)\phi(b) - f(a)\phi(a) - \int_{a}^{b} f\,d\phi$$, que es la identidad buscada.

## Paso al límite bajo el signo integral

### Ejemplo (Una sucesión creciente de funciones Riemann-integrables con límite no integrable)

Sea $$\{r_{n}\}_{n=1}^{\infty}$$ una enumeración de $$\mathbb{Q} \cap [0,1]$$ y

$$
f_{n} : [0,1] \to \mathbb{R}, \qquad f_{n}(x) = \begin{cases} 1, & x \in \{r_{1}, \dots, r_{n}\},\\ 0, & \text{en otro caso.}\end{cases}
$$

Entonces $$f_{n} \leq f_{n+1}$$ y $$f_{n} \to f = \mathbf{1}_{\mathbb{Q} \cap [0,1]}$$ puntualmente. Es un ejercicio comprobar que $$\int_{0}^{1} f_{n}(x)\,dx = 0$$ para todo $$n$$, mientras que $$f$$ no es Riemann integrable. Así, el límite puntual de funciones Riemann-integrables puede no serlo, lo que motiva una noción de integral más flexible.

### Lema (Paso al límite bajo convergencia uniforme)

Sea $$\phi : [a,b] \to \mathbb{R}$$ de variación acotada y $$\{f_{n}\}_{n=1}^{\infty}$$ una sucesión de funciones Riemann–Stieltjes integrables respecto de $$\phi$$. Si $$f_{n} \to f$$ uniformemente en $$[a,b]$$ y $$f$$ es Riemann–Stieltjes integrable respecto de $$\phi$$, entonces

$$
\lim_{n \to \infty} \int_{a}^{b} f_{n}\,d\phi = \int_{a}^{b} f\,d\phi.
$$

***Prueba:*** Para cualquier función $$g$$ Riemann–Stieltjes integrable respecto de $$\phi$$ y toda partición $$\Gamma$$,

$$
|R(g, \Gamma, \phi)| \leq \Big(\sup_{[a,b]}|g|\Big)\sum_{i}|\phi(x_{i}) - \phi(x_{i-1})| \leq \Big(\sup_{[a,b]}|g|\Big)\operatorname{Var}(\phi, [a,b]),
$$

y pasando al límite, $$\big|\int_{a}^{b} g\,d\phi\big| \leq (\sup_{[a,b]}|g|)\operatorname{Var}(\phi, [a,b])$$. Aplicando esto a $$g = f_{n} - f$$ (integrable, por serlo $$f_{n}$$ y $$f$$) y usando la linealidad,

$$
\left| \int_{a}^{b} f_{n}\,d\phi - \int_{a}^{b} f\,d\phi \right| = \left| \int_{a}^{b} (f_{n} - f)\,d\phi \right| \leq \Big(\sup_{[a,b]}|f_{n} - f|\Big)\operatorname{Var}(\phi, [a,b]).
$$

Como $$f_{n} \to f$$ uniformemente, $$\sup_{[a,b]}|f_{n} - f| \to 0$$, y el lado derecho tiende a cero.
{% endraw %}
