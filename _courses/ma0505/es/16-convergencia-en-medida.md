---
layout: chapter
course: ma0505
chapter: 16
title: "Convergencia en medida"
slug: 16-convergencia-en-medida
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/16-convergencia-en-medida/
---

{% raw %}
## Definición y relación con la convergencia c.p.d.

### Definición (Convergencia en medida)

Sean $$f, f_{n} : E \to \overline{\mathbb{R}}$$ medibles y finitas casi por doquier. Decimos que $$f_{n}$$ *converge a $$f$$ en medida* si, para todo $$\varepsilon > 0$$,

$$
\lim_{n \to \infty} m\{ |f_{n} - f| > \varepsilon \} = 0.
$$

Denotamos $$f_{n} \xrightarrow{m} f$$.

### Nota (La convergencia en medida es la más débil del curso)

Esta convergencia es la convergencia más débil que veremos en el curso: la convergencia uniforme implica la convergencia puntual, la puntual implica la convergencia c.p.d., y sobre conjuntos de medida finita la convergencia c.p.d. implica la convergencia en medida, como muestra el teorema siguiente. Ninguna de las implicaciones recíprocas vale en general.

### Teorema (En medida finita, la convergencia c.p.d. implica convergencia en medida)

Sean $$f, f_{n} : E \to \overline{\mathbb{R}}$$ medibles y finitas casi por doquier. Si

$$
\lim_{n \to \infty} f_{n} = f
$$

casi por doquier en $$E$$ y $$m(E) < \infty$$, entonces $$f_{n} \xrightarrow{m} f$$ en $$E$$.

***Prueba:*** Sean $$\eta > 0$$ y $$\varepsilon > 0$$; hay que mostrar que existe $$n_{0}$$ tal que

$$
m\{ |f_{n} - f| > \varepsilon \} < \eta
$$

cuando $$n \geq n_{0}$$. Como $$m(E) < \infty$$, por el teorema de Egorov existe $$F \subseteq E$$ cerrado tal que

$$
m(E \setminus F) < \eta
$$

y $$f_{n} \to f$$ uniformemente en $$F$$. Entonces existe $$n_{0}$$ tal que

$$
|f_{n}(x) - f(x)| < \varepsilon \quad \text{para todo } n \geq n_{0} \text{ y } x \in F.
$$

Luego

$$
\{ x \in E :\ |f_{n}(x) - f(x)| > \varepsilon \} \subseteq E \setminus F
$$

cuando $$n \geq n_{0}$$, y por monotonía de la medida,

$$
m\{ x \in E :\ |f_{n}(x) - f(x)| > \varepsilon \} \leq m(E \setminus F) < \eta.
$$

### Ejemplo (La máquina de escribir: convergencia en medida sin convergencia puntual)

Considere la sucesión de indicadoras de intervalos diádicos de $$[0,1]$$:

$$
\begin{gathered}
I_{0} = \mathbf{1}_{[0,1]}, \\
I_{1,1} = \mathbf{1}_{[0,\frac{1}{2}]}, \quad I_{1,2} = \mathbf{1}_{[\frac{1}{2},1]}, \\
I_{2,i} = \mathbf{1}_{[\frac{i-1}{2^{2}},\frac{i}{2^{2}}]}, \quad 1 \leq i \leq 4.
\end{gathered}
$$

En general, $$I_{n,i} = \mathbf{1}_{[\frac{i-1}{2^{n}},\frac{i}{2^{n}}]}$$ con $$1 \leq i \leq 2^{n}$$. Para obtener una sucesión ordenamos los índices lexicográficamente:

$$
(m,i) \leq (n,j) \iff (m < n) \lor \big( (m = n) \land i \leq j \big).
$$

Esta sucesión converge a cero en medida, pues para $$0 < \varepsilon < 1$$ el conjunto $$\{ I_{n,i} > \varepsilon \}$$ es un intervalo de medida $$2^{-n}$$, y $$n \to \infty$$ a lo largo de la sucesión. Sin embargo, no converge en ningún punto: para cada $$x \in [0,1]$$ y cada $$n$$ existe algún $$i$$ con $$x \in [\frac{i-1}{2^{n}},\frac{i}{2^{n}}]$$, de modo que la sucesión toma los valores $$1$$ y $$0$$ infinitas veces en $$x$$.

### Teorema (Toda sucesión convergente en medida tiene una subsucesión convergente c.p.d.)

Sea $$f_{n} \xrightarrow{m} f$$ en $$E$$. Entonces existen índices $$n_{1} < n_{2} < \dots$$ de manera que

$$
f_{n_{j}} \to f
$$

casi por doquier en $$E$$.

***Prueba:*** Dado $$j \geq 1$$, por la convergencia en medida existe $$n_{j}$$ tal que

$$
m\left\{ |f_{n} - f| > \frac{1}{j} \right\} \leq \frac{1}{2^{j}} \quad \text{si } n \geq n_{j}.
$$

Sin pérdida de generalidad podemos suponer $$n_{j} < n_{j+1}$$, escogiendo los índices de manera creciente. Entonces

$$
m\left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\} \leq \frac{1}{2^{j}}.
$$

Tome

$$
H_{m} = \bigcup_{j \geq m} \left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\}.
$$

Entonces $$H_{m+1} \subseteq H_{m}$$ y, por subaditividad numerable,

$$
m(H_{m}) \leq \sum_{j \geq m} m\left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\} \leq \sum_{j \geq m} \frac{1}{2^{j}} = \frac{1}{2^{m-1}}.
$$

Considere

$$
Z = \bigcap_{m \in \mathbb{N}} H_{m}.
$$

Como $$Z \subseteq H_{m}$$ para todo $$m$$, tenemos que $$m(Z) \leq 2^{-(m-1)}$$ para todo $$m$$, y entonces $$Z$$ tiene medida cero. Además, si

$$
x \in E \setminus Z = \bigcup_{m \in \mathbb{N}} (E \setminus H_{m}),
$$

entonces existe $$m_{0}$$ tal que $$x \in E \setminus H_{m_{0}}$$. Como

$$
E \setminus H_{m_{0}} = E \setminus \bigcup_{j \geq m_{0}} \left\{ |f_{n_{j}} - f| > \frac{1}{j} \right\} = \bigcap_{j \geq m_{0}} \left\{ |f_{n_{j}} - f| \leq \frac{1}{j} \right\},
$$

obtenemos que, dado $$x \in E \setminus Z$$, existe $$m_{0}$$ tal que

$$
|f_{n_{j}}(x) - f(x)| \leq \frac{1}{j} \quad \text{para } j \geq m_{0}.
$$

Finalmente, dado $$\varepsilon > 0$$, existe $$j_{0}$$ tal que $$\tfrac{1}{j_{0}} < \varepsilon$$, y entonces

$$
|f_{n_{j}}(x) - f(x)| \leq \frac{1}{j} \leq \frac{1}{j_{0}} < \varepsilon
$$

para $$j \geq \max(j_{0}, m_{0})$$. Es decir, $$f_{n_{j}}(x) \to f(x)$$ para todo $$x$$ fuera del conjunto nulo $$Z$$.

## Sucesiones de Cauchy en medida

### Definición (Sucesión de Cauchy en medida)

Decimos que $$(f_{n})_{n \in \mathbb{N}}$$ es *de Cauchy en medida* si para todos $$\varepsilon, \eta > 0$$ existe $$N \in \mathbb{N}$$ tal que

$$
m\{ |f_{n} - f_{m}| > \varepsilon \} < \eta
$$

para $$n, m \geq N$$.

### Lema (Toda sucesión de Cauchy en medida converge en medida)

Una sucesión de Cauchy en medida es convergente en medida.

***Prueba:*** Ejercicio.
{% endraw %}
