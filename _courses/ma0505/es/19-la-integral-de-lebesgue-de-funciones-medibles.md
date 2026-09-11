---
layout: chapter
course: ma0505
chapter: 19
title: "La integral de Lebesgue de funciones medibles"
slug: 19-la-integral-de-lebesgue-de-funciones-medibles
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/19-la-integral-de-lebesgue-de-funciones-medibles/
---

{% raw %}
## La definición y las funciones integrables

### Definición (Parte positiva, parte negativa y la integral general)

Sea $$f : E \to \overline{\mathbb{R}}$$ una función medible. Entonces

$$
f = f^{+} - f^{-}
$$

con

$$
f^{+} = \max(0, f) \qquad \text{y} \qquad f^{-} = \max(0, -f).
$$

Sabemos que $$f^{+}$$ y $$f^{-}$$ son medibles y no negativas, entonces

$$
\int_{E} f^{+} \, dx, \qquad \int_{E} f^{-} \, dx
$$

están bien definidas. Por tanto podemos definir

$$
\int_{E} f \, dx = \int_{E} f^{+} \, dx - \int_{E} f^{-} \, dx
$$

siempre que

$$
\int_{E} f^{+} \, dx < \infty \qquad \text{o} \qquad \int_{E} f^{-} \, dx < \infty.
$$

En tal caso decimos que la integral de $$f$$ sobre $$E$$ *existe* (con valor posiblemente $$\pm\infty$$).

### Definición (Función integrable y el espacio $$L(E)$$)

Decimos que $$f$$ es *integrable*, o bien que $$f \in L(E)$$, si

$$
\int_{E} f^{+} \, dx < \infty \qquad \text{y} \qquad \int_{E} f^{-} \, dx < \infty.
$$

### Nota (Desigualdad triangular integral y finitud c.p.d.)

Como $$|f| = f^{+} + f^{-}$$, para $$f \in L(E)$$ tenemos que

$$
\left| \int_{E} f \, dx \right| \leq \int_{E} f^{+} \, dx + \int_{E} f^{-} \, dx = \int_{E} |f| \, dx,
$$

donde la última igualdad usa la linealidad para funciones no negativas. En particular, $$f \in L(E)$$ si y solo si $$\int_{E} |f| \, dx < \infty$$. Además, si $$\int_{E} |f| \, dx < \infty$$, entonces $$f \in \mathbb{R}$$ c.p.d., por la proposición sobre funciones con integral finita.

## Monotonía y propiedades básicas

### Teorema (Monotonía de la integral general)

Sean $$f : E \to \overline{\mathbb{R}}$$ y $$g : E \to \overline{\mathbb{R}}$$ medibles tales que

$$
\int_{E} f \, dx \qquad \text{y} \qquad \int_{E} g \, dx
$$

existen. Si $$f \leq g$$ c.p.d. en $$E$$, entonces

$$
\int_{E} f \, dx \leq \int_{E} g \, dx.
$$

En particular, si $$f = g$$ c.p.d. en $$E$$, entonces

$$
\int_{E} f \, dx = \int_{E} g \, dx.
$$

***Prueba:*** Note que si $$f \leq g$$ c.p.d., entonces, punto a punto donde vale la desigualdad,

$$
f^{+} = \max\{0, f\} \leq \max\{0, g\} = g^{+}, \qquad g^{-} = \max\{0, -g\} \leq \max\{0, -f\} = f^{-},
$$

es decir, $$f^{+} \leq g^{+}$$ y $$g^{-} \leq f^{-}$$ c.p.d. Luego, por la monotonía c.p.d. de la integral de funciones no negativas,

$$
\int_{E} f^{+} \, dx \leq \int_{E} g^{+} \, dx, \qquad \int_{E} g^{-} \, dx \leq \int_{E} f^{-} \, dx,
$$

y entonces, restando en el sentido extendido (la existencia de ambas integrales garantiza que no aparece la forma $$\infty - \infty$$),

$$
\int_{E} f \, dx = \int_{E} f^{+} \, dx - \int_{E} f^{-} \, dx \leq \int_{E} g^{+} \, dx - \int_{E} g^{-} \, dx = \int_{E} g \, dx.
$$

Si $$f = g$$ c.p.d., las dos desigualdades dan la igualdad.

### Teorema (Restricción del dominio, aditividad numerable y conjuntos nulos)

Sea $$f : E \to \overline{\mathbb{R}}$$ medible tal que $$\int_{E} f \, dx$$ existe.

1. Si $$E_{1} \subseteq E$$ es medible, entonces $$\int_{E_{1}} f \, dx$$ existe.
2. Si $$E = \bigcup_{k=1}^{\infty} E_{k}$$ con los $$E_{k}$$ medibles y disjuntos dos a dos, entonces

    $$
    \int_{E} f \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f \, dx.
    $$
3. Si $$E_{1} \subseteq E$$ con $$m(E_{1}) = 0$$, entonces $$\int_{E_{1}} f \, dx = 0$$.

***Prueba:*** Para (i), note que, por monotonía respecto al dominio para funciones no negativas,

$$
0 \leq \int_{E_{1}} f^{+} \, dx \leq \int_{E} f^{+} \, dx, \qquad 0 \leq \int_{E_{1}} f^{-} \, dx \leq \int_{E} f^{-} \, dx.
$$

Como alguna de las dos integrales sobre $$E$$ es finita, la correspondiente sobre $$E_{1}$$ también lo es, y $$\int_{E_{1}} f \, dx$$ existe.

Para (ii), sabemos, por la aditividad del dominio para funciones no negativas, que

$$
\int_{E} f^{+} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{+} \, dx, \qquad \int_{E} f^{-} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{-} \, dx.
$$

Como

$$
\int_{E} f^{+} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{+} \, dx < \infty \qquad \text{o} \qquad \int_{E} f^{-} \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{-} \, dx < \infty,
$$

al menos una de las dos series converge, y podemos restar término a término sin ambigüedad. Entonces

$$
\int_{E} f \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f^{+} \, dx - \sum_{k=1}^{\infty} \int_{E_{k}} f^{-} \, dx = \sum_{k=1}^{\infty} \left( \int_{E_{k}} f^{+} \, dx - \int_{E_{k}} f^{-} \, dx \right) = \sum_{k=1}^{\infty} \int_{E_{k}} f \, dx.
$$

Finalmente, para (iii), si $$m(E_{1}) = 0$$, el lema de la integral sobre conjuntos nulos aplicado a $$f^{+}$$ y $$f^{-}$$ da

$$
\int_{E_{1}} f \, dx = \int_{E_{1}} f^{+} \, dx - \int_{E_{1}} f^{-} \, dx = 0 - 0 = 0.
$$

## Linealidad y diferencias de funciones

### Teorema (Linealidad de la integral general)

Sean $$f, g : E \to \overline{\mathbb{R}}$$ medibles tales que $$\int_{E} f \, dx$$ existe, y $$c \in \mathbb{R}$$. Entonces

$$
\int_{E} c f \, dx = c \int_{E} f \, dx.
$$

Además, si $$f, g \in L(E)$$, entonces $$f + g \in L(E)$$ y

$$
\int_{E} (f + g) \, dx = \int_{E} f \, dx + \int_{E} g \, dx.
$$

***Prueba:*** *Homogeneidad.* Si $$c \geq 0$$, entonces $$(cf)^{+} = c f^{+}$$ y $$(cf)^{-} = c f^{-}$$, y el resultado se sigue de la homogeneidad para funciones no negativas. Si $$c < 0$$, entonces

$$
(cf)^{+} = -c f^{-}, \qquad (cf)^{-} = -c f^{+},
$$

pues $$cf \geq 0$$ exactamente donde $$f \leq 0$$. Entonces

$$
\int_{E} c f \, dx = \int_{E} (-c) f^{-} \, dx - \int_{E} (-c) f^{+} \, dx = -c \int_{E} f^{-} \, dx + c \int_{E} f^{+} \, dx = c \int_{E} f \, dx.
$$

*Aditividad.* Si $$f, g$$ son integrables, entonces son finitas c.p.d., de modo que $$f + g$$ está definida c.p.d., y como $$|f + g| \leq |f| + |g|$$,

$$
0 \leq \int_{E} |f + g| \, dx \leq \int_{E} |f| \, dx + \int_{E} |g| \, dx < \infty,
$$

usando la monotonía y la linealidad para no negativas; es decir, $$f + g \in L(E)$$. Note que los siguientes conjuntos medibles, disjuntos dos a dos, cubren $$E$$ salvo un conjunto nulo (donde $$f$$ o $$g$$ toman valores infinitos):

$$
\begin{aligned}
&E_{1} = \{ f \geq 0,\ g \geq 0 \}, \\
&E_{2} = \{ f < 0,\ g < 0 \}, \\
&E_{3} = \{ f \geq 0,\ g < 0,\ f + g \geq 0 \}, \\
&E_{4} = \{ f < 0,\ g \geq 0,\ f + g \geq 0 \}, \\
&E_{5} = \{ f \geq 0,\ g < 0,\ f + g < 0 \}, \\
&E_{6} = \{ f < 0,\ g \geq 0,\ f + g < 0 \}.
\end{aligned}
$$

Por la aditividad del dominio, basta probar la aditividad de la integral en cada $$E_{i}$$.

En $$E_{1}$$ las tres funciones $$f, g, f+g$$ son no negativas, así que, por la linealidad para no negativas,

$$
\int_{E_{1}} (f + g) \, dx = \int_{E_{1}} (f^{+} + g^{+}) \, dx = \int_{E_{1}} f^{+} \, dx + \int_{E_{1}} g^{+} \, dx = \int_{E_{1}} f \, dx + \int_{E_{1}} g \, dx,
$$

y también, en $$E_{2}$$, donde las tres son negativas,

$$
\begin{aligned}
\int_{E_{2}} (f + g) \, dx &= \int_{E_{2}} -(f^{-} + g^{-}) \, dx = -\int_{E_{2}} (f^{-} + g^{-}) \, dx \\
&= -\int_{E_{2}} f^{-} \, dx - \int_{E_{2}} g^{-} \, dx = \int_{E_{2}} f \, dx + \int_{E_{2}} g \, dx.
\end{aligned}
$$

En $$E_{3}$$ tenemos $$f = (f + g) + (-g)$$ con $$f + g \geq 0$$ y $$-g > 0$$; de esta manera, por la linealidad para no negativas,

$$
\int_{E_{3}} f \, dx = \int_{E_{3}} \big( (f+g) - g \big) \, dx = \int_{E_{3}} (f + g) \, dx + \int_{E_{3}} (-g) \, dx = \int_{E_{3}} (f + g) \, dx - \int_{E_{3}} g \, dx,
$$

donde el último paso usa la homogeneidad con $$c = -1$$ y que $$g \in L(E_{3})$$. Por lo tanto

$$
\int_{E_{3}} (f + g) \, dx = \int_{E_{3}} f \, dx + \int_{E_{3}} g \, dx.
$$

Además, en $$E_{5}$$ tenemos $$-g = -(f+g) + f$$ con $$-(f+g) > 0$$ y $$f \geq 0$$, entonces

$$
\int_{E_{5}} (-g) \, dx = \int_{E_{5}} \big( -(f+g) + f \big) \, dx = \int_{E_{5}} -(f+g) \, dx + \int_{E_{5}} f \, dx.
$$

Así, multiplicando por $$-1$$ y reordenando, tenemos que

$$
\int_{E_{5}} f \, dx + \int_{E_{5}} g \, dx = \int_{E_{5}} (f + g) \, dx.
$$

Los casos $$E_{4}$$ y $$E_{6}$$ son análogos, intercambiando los papeles de $$f$$ y $$g$$; terminar el resto de la prueba es un ejercicio.

### Nota (Combinaciones lineales y una advertencia sobre la resta)

Sean $$f_{1}, \dots, f_{n} \in L(E)$$ y $$a_{1}, \dots, a_{n} \in \mathbb{R}$$. Entonces, iterando el teorema anterior, $$\sum_{k=1}^{n} a_{k} f_{k} \in L(E)$$ y

$$
\int_{E} \left( \sum_{k=1}^{n} a_{k} f_{k} \right) \, dx = \sum_{k=1}^{n} a_{k} \int_{E} f_{k} \, dx.
$$

Ojo: cuando las integrales no son finitas, en general *no* es cierto que

$$
\int_{E} (f - g) \, dx = \int_{E} f \, dx - \int_{E} g \, dx.
$$

Por ejemplo, considere $$f = \mathbf{1}_{[n,\infty)}$$ y $$g = \mathbf{1}_{[n+1,\infty)}$$: la resta $$f - g = \mathbf{1}_{[n,n+1)}$$ tiene integral $$1$$, pero $$\int f \, dx = \int g \, dx = \infty$$ y la diferencia $$\infty - \infty$$ no está definida.

### Proposición (Resta de una minorante integrable)

Sean $$f$$ y $$\phi$$ medibles en $$E$$ tales que $$\phi \leq f$$ c.p.d. y $$\phi \in L(E)$$. Entonces $$\int_{E} f \, dx$$ y $$\int_{E} (f - \phi) \, dx$$ existen y

$$
\int_{E} (f - \phi) \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx.
$$

***Prueba:*** Como $$\phi \leq f$$ c.p.d., tenemos $$-f \leq -\phi$$ c.p.d. y entonces

$$
f^{-} = \max(0, -f) \leq \max(0, -\phi) = \phi^{-} \quad \text{c.p.d.},
$$

de donde

$$
0 \leq \int_{E} f^{-} \, dx \leq \int_{E} \phi^{-} \, dx < \infty.
$$

Es decir, $$\int_{E} f \, dx$$ existe, con valor en $$(-\infty, \infty]$$, y quedan dos casos según el valor de $$\int_{E} f^{+} \, dx$$.

Si $$\int_{E} f^{+} \, dx < \infty$$, entonces $$f \in L(E)$$, y como también $$-\phi \in L(E)$$, la linealidad da directamente

$$
\int_{E} (f - \phi) \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx.
$$

Ahora, si $$\int_{E} f^{+} \, dx = \infty$$, es decir $$f \notin L(E)$$, afirmamos que $$f - \phi \notin L(E)$$. En efecto, donde ambas son finitas vale $$f = \phi + (f - \phi) \leq \phi^{+} + (f - \phi)$$, y como el lado derecho es no negativo,

$$
f^{+} \leq \phi^{+} + (f - \phi) \quad \text{c.p.d.}
$$

Integrando, por monotonía c.p.d. y linealidad para no negativas,

$$
\infty = \int_{E} f^{+} \, dx \leq \int_{E} \phi^{+} \, dx + \int_{E} (f - \phi) \, dx,
$$

y como $$\int_{E} \phi^{+} \, dx < \infty$$, se sigue que $$\int_{E} (f - \phi) \, dx = \infty$$. Además $$f - \phi \geq 0$$ c.p.d., así que

$$
\int_{E} (f - \phi) \, dx = \int_{E} (f - \phi)^{+} \, dx = \infty.
$$

Concluimos que, en este caso, ambos lados valen $$\infty$$:

$$
\int_{E} (f - \phi) \, dx = \infty = \int_{E} f \, dx - \int_{E} \phi \, dx,
$$

pues $$\int_{E} f \, dx = \infty$$ y $$\int_{E} \phi \, dx \in \mathbb{R}$$.

### Nota (Productos de funciones integrables)

Las condiciones para que $$fg$$ sea integrable son más complejas que para la suma. Por ejemplo, si $$f \in L(E)$$ y $$g$$ es medible con $$|g(x)| \leq M$$ para $$x \in E$$, entonces $$fg \in L(E)$$, pues $$|fg| \leq M |f|$$ y la monotonía da $$\int_{E} |fg| \, dx \leq M \int_{E} |f| \, dx < \infty$$.

## Los teoremas de convergencia

### Teorema (Convergencia monótona con minorante o mayorante integrable)

Sea $$\{f_{k}\}_{k=1}^{\infty}$$ una sucesión de funciones medibles en $$E$$, tales que $$\lim_{k \to \infty} f_{k} = f$$ c.p.d. en $$E$$.

1. Si existe $$\phi \in L(E)$$ tal que $$\phi \leq f_{k} \leq f_{k+1}$$ c.p.d. para todo $$k \geq 1$$, entonces

    $$
    \lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx.
    $$
2. Si existe $$\phi \in L(E)$$ tal que $$f_{k+1} \leq f_{k} \leq \phi$$ c.p.d. para todo $$k \geq 1$$, entonces

    $$
    \lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx.
    $$

***Prueba:*** Solo probaremos el caso creciente; la parte (ii) se deja como ejercicio a la persona lectora. Si se cumple la primera condición, entonces

$$
f_{k} - \phi \geq 0 \qquad \text{y} \qquad f_{k+1} - \phi \geq f_{k} - \phi \quad \text{c.p.d.}
$$

para $$k \geq 1$$, y además $$f_{k} - \phi \to f - \phi$$ c.p.d. Entonces, por el teorema de convergencia monótona para funciones no negativas,

$$
\lim_{k \to \infty} \int_{E} (f_{k} - \phi) \, dx = \int_{E} (f - \phi) \, dx.
$$

Por la proposición de la resta de una minorante integrable, aplicada a cada $$f_{k}$$ y a $$f$$ (con minorante $$\phi$$),

$$
\int_{E} (f_{k} - \phi) \, dx = \int_{E} f_{k} \, dx - \int_{E} \phi \, dx, \qquad \int_{E} (f - \phi) \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx.
$$

Es decir,

$$
\lim_{k \to \infty} \int_{E} f_{k} \, dx - \int_{E} \phi \, dx = \int_{E} f \, dx - \int_{E} \phi \, dx,
$$

y como $$\int_{E} \phi \, dx \in \mathbb{R}$$, podemos cancelar y concluir que $$\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx$$.

### Ejemplo (Integración término a término de series de funciones no negativas)

Sean $$f_{k} : E \to [0,\infty]$$ medibles para $$k \geq 1$$. Entonces, si llamamos

$$
g_{m} = \sum_{k=1}^{m} f_{k},
$$

tenemos que $$0 \leq g_{m} \leq g_{m+1}$$. Luego, por el teorema de convergencia monótona y la linealidad,

$$
\begin{aligned}
\int_{E} \left( \sum_{k=1}^{\infty} f_{k} \right) \, dx &= \int_{E} \lim_{m \to \infty} g_{m}(x) \, dx = \lim_{m \to \infty} \int_{E} g_{m}(x) \, dx \\
&= \lim_{m \to \infty} \int_{E} \sum_{k=1}^{m} f_{k}(x) \, dx = \lim_{m \to \infty} \sum_{k=1}^{m} \int_{E} f_{k}(x) \, dx = \sum_{k=1}^{\infty} \int_{E} f_{k}(x) \, dx.
\end{aligned}
$$

### Ejemplo (Una sucesión que converge a cero con integrales constantes)

Sea $$E = [0,1]$$ y definamos

$$
f_{k}(x) =
\begin{cases}
k & \text{si } 0 \leq x \leq \frac{1}{k}, \\
0 & \text{si } \frac{1}{k} < x \leq 1.
\end{cases}
$$

Entonces

$$
\int_{E} f_{k}(x) \, dx = k \cdot m\left( \left[0, \tfrac{1}{k}\right] \right) = 1 \quad \text{para todo } k,
$$

pero $$\lim_{k \to \infty} f_{k} = 0$$ c.p.d. en $$[0,1]$$: para $$x > 0$$, $$f_{k}(x) = 0$$ apenas $$k > \tfrac{1}{x}$$. Nos preguntamos:

¿Cuándo $$\displaystyle \lim_{k \to \infty} \int_{E} f_{k}(x) \, dx = \int_{E} \lim_{k \to \infty} f_{k}(x) \, dx$$?

Este ejemplo muestra que alguna hipótesis adicional (monotonía, dominación, etc.) es necesaria.

### Teorema (Lema de Fatou)

Sea $$f_{k} : E \to [0,\infty]$$ una sucesión de funciones medibles no negativas. Entonces

$$
\int_{E} \liminf_{k \to \infty} f_{k} \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k} \, dx.
$$

***Prueba:*** Recordemos que

$$
\liminf_{k \to \infty} f_{k} = \sup_{k \geq 1} \inf_{m \geq k} f_{m} = \lim_{k \to \infty} \inf_{m \geq k} f_{m}.
$$

Considere

$$
g_{k} = \inf_{m \geq k} f_{m};
$$

entonces $$\{g_{k}\}$$ es una sucesión creciente de funciones medibles no negativas con $$g_{k} \to \liminf_{k \to \infty} f_{k}$$. Por el teorema de convergencia monótona,

$$
\int_{E} \Big( \liminf_{k \to \infty} f_{k} \Big) \, dx = \lim_{k \to \infty} \int_{E} \inf_{m \geq k} f_{m} \, dx.
$$

Note que

$$
\inf_{m \geq k} f_{m} \leq f_{n} \quad \text{para } n \geq k \geq 1.
$$

Entonces, por monotonía, para $$n \geq k$$,

$$
\int_{E} \inf_{m \geq k} f_{m}(x) \, dx \leq \int_{E} f_{n}(x) \, dx,
$$

y tomando el ínfimo sobre $$n \geq k$$,

$$
\int_{E} \inf_{m \geq k} f_{m}(x) \, dx \leq \inf_{n \geq k} \int_{E} f_{n}(x) \, dx.
$$

Tomando ahora el límite cuando $$k \to \infty$$ en ambos lados,

$$
\lim_{k \to \infty} \int_{E} \inf_{m \geq k} f_{m}(x) \, dx \leq \lim_{k \to \infty} \inf_{n \geq k} \int_{E} f_{n}(x) \, dx = \liminf_{k \to \infty} \int_{E} f_{k}(x) \, dx.
$$

Combinando con la primera identidad, concluimos que

$$
\int_{E} \liminf_{k \to \infty} f_{k} \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k} \, dx.
$$

### Nota (Cota uniforme de integrales y el límite inferior)

Note que si $$f_{k} : E \to [0,\infty]$$ es medible para cada $$k$$ y

$$
\int_{E} f_{k}(x) \, dx \leq M \quad \text{para todo } k,
$$

entonces, por el lema de Fatou,

$$
\int_{E} \liminf_{k \to \infty} f_{k} \, dx \leq M.
$$

### Teorema (Convergencia dominada de Lebesgue para funciones no negativas)

Sea $$\{f_{k}\}_{k=1}^{\infty}$$ una sucesión de funciones medibles no negativas tales que

$$
\lim_{k \to \infty} f_{k} = f
$$

c.p.d. en $$E$$. Si existe $$\phi$$ medible con

$$
0 \leq f_{k} \leq \phi \quad \text{c.p.d. para todo } k \geq 1, \qquad \int_{E} \phi(x) \, dx < \infty,
$$

entonces

$$
\lim_{k \to \infty} \int_{E} f_{k}(x) \, dx = \int_{E} f(x) \, dx.
$$

***Prueba:*** Como $$f = \liminf_{k \to \infty} f_{k}$$ c.p.d., el lema de Fatou y la igualdad c.p.d. de las integrales dan

$$
\int_{E} f(x) \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k} \, dx.
$$

Note además que $$0 \leq f \leq \phi$$ c.p.d., entonces $$f, f_{k} \in L(E)$$, pues sus integrales están dominadas por $$\int_{E} \phi \, dx < \infty$$.

Considere ahora $$h_{k} = \phi - f_{k} \geq 0$$ c.p.d. Por el lema de Fatou aplicado a $$\{h_{k}\}$$,

$$
\int_{E} \liminf_{k \to \infty} (\phi - f_{k}) \, dx \leq \liminf_{k \to \infty} \int_{E} (\phi - f_{k}) \, dx.
$$

Note que, como el límite de $$f_{k}$$ existe c.p.d.,

$$
\liminf_{k \to \infty} (\phi - f_{k}) = \lim_{k \to \infty} (\phi - f_{k}) = \phi - f \quad \text{c.p.d.}
$$

Por otro lado, usando la linealidad (todas las funciones involucradas son integrables), tenemos que

$$
\liminf_{k \to \infty} \int_{E} (\phi - f_{k})(x) \, dx = \liminf_{k \to \infty} \left( \int_{E} \phi(x) \, dx - \int_{E} f_{k}(x) \, dx \right) = \int_{E} \phi(x) \, dx - \limsup_{k \to \infty} \int_{E} f_{k}(x) \, dx.
$$

La última igualdad vale porque $$\liminf_{k}(-a_{k}) = -\limsup_{k} a_{k}$$ para toda sucesión real $$\{a_{k}\}$$, y sumar la constante finita $$\int_{E} \phi \, dx$$ conmuta con el límite inferior. Combinando las tres relaciones anteriores y cancelando $$\int_{E} \phi \, dx \in \mathbb{R}$$, concluimos que

$$
\limsup_{k \to \infty} \int_{E} f_{k}(x) \, dx \leq \int_{E} f(x) \, dx \leq \liminf_{k \to \infty} \int_{E} f_{k}(x) \, dx,
$$

es decir, el límite existe y $$\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx$$.

### Teorema (Convergencia uniforme en dominios de medida finita)

Sea $$f_{k} \in L(E)$$ para $$k \geq 1$$. Si $$\lim_{k \to \infty} f_{k} = f$$ uniformemente en $$E$$ con $$m(E) < \infty$$, entonces $$f \in L(E)$$ y

$$
\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f \, dx.
$$

***Prueba:*** Ejercicio.

### Nota (La hipótesis de medida finita es esencial en la convergencia uniforme)

Note que $$f_{k}(x) = \frac{1}{k}$$ converge a cero uniformemente en $$\mathbb{R}$$, pero

$$
\int_{\mathbb{R}} f_{k} \, dx = \infty
$$

para todo $$k$$, así que la conclusión del teorema anterior falla sin la hipótesis $$m(E) < \infty$$.
{% endraw %}
