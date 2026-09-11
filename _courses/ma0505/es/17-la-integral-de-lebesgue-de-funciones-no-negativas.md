---
layout: chapter
course: ma0505
chapter: 17
title: "La integral de Lebesgue de funciones no negativas"
slug: 17-la-integral-de-lebesgue-de-funciones-no-negativas
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/17-la-integral-de-lebesgue-de-funciones-no-negativas/
---

{% raw %}
## La región bajo el gráfico

### Definición (Región bajo el gráfico y gráfico de una función)

Sea $$f : E \to \overline{\mathbb{R}}$$ medible con $$E \subseteq \mathbb{R}^{d}$$ medible y $$f \geq 0$$. Definimos la *región bajo el gráfico* de $$f$$ sobre $$E$$ como

$$
R(f,E) = \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq f(x) \},
$$

y el *gráfico* de $$f$$ sobre $$E$$ como

$$
\Gamma(f,E) = \{ (x, f(x)) :\ x \in E \}.
$$

Surge la pregunta: ¿es $$R(f,E)$$ medible?

### Ejemplo (La región bajo un múltiplo de una indicadora)

Analicemos el caso

$$
f(x) = a \mathbf{1}_{A}(x)
$$

con $$A \subseteq E$$ medible y $$a > 0$$. Entonces ocurre que

$$
\begin{aligned}
R(f,E) &= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq f(x) \} \\
&= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in A,\ 0 \leq y \leq a \} \cup \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E \setminus A,\ y = 0 \} \\
&= \big( A \times [0,a] \big) \cup \big( (E \setminus A) \times \{0\} \big).
\end{aligned}
$$

Es decir, la medibilidad de $$R(f,E)$$ en este caso se reduce a la medibilidad de productos de la forma $$A \times [0,a]$$.

### Lema (Medida del producto de un medible por un intervalo)

Sea $$A \subseteq \mathbb{R}^{d}$$ medible y $$a \geq 0$$. Entonces $$A \times [0,a] \subseteq \mathbb{R}^{d+1}$$ es medible y su medida es

$$
m(A \times [0,a]) = a\, m(A),
$$

con la convención $$0 \cdot \infty = 0$$.

***Prueba:*** *Caso de una caja.* Si $$A = [a_{1},b_{1}] \times \dots \times [a_{d},b_{d}]$$, entonces $$A \times [0,a]$$ es una caja de $$\mathbb{R}^{d+1}$$ y el resultado se sigue de la fórmula para el volumen de cajas. Verificar los detalles queda como ejercicio para la persona lectora.

*Caso de un abierto con $$m(A) < \infty$$.* Si $$A$$ es abierto, entonces existen cajas $$I_{k}$$ en $$d$$ dimensiones tales que

$$
A = \bigcup_{k=1}^{\infty} I_{k} \quad \text{con } I_{j}^{\circ} \cap I_{k}^{\circ} = \emptyset \text{ si } j \neq k.
$$

Entonces

$$
A \times [0,a] = \bigcup_{k=1}^{\infty} I_{k} \times [0,a]
$$

es un conjunto medible, por ser unión numerable de cajas. Como

$$
(I_{k} \times [0,a])^{\circ} \cap (I_{j} \times [0,a])^{\circ} = \emptyset, \quad k \neq j,
$$

y la medida de una unión numerable de cajas con interiores disjuntos dos a dos es la suma de sus medidas, tenemos que

$$
m(A \times [0,a]) = \sum_{i=1}^{\infty} m(I_{i} \times [0,a]) = a \sum_{i=1}^{\infty} m(I_{i}) = a\, m(A).
$$

*Caso de un $$G_{\delta}$$ con $$m(A) < \infty$$.* Sea ahora

$$
A = \bigcap_{j=1}^{\infty} G_{j}
$$

un $$G_{\delta}$$ con cada $$G_{i}$$ abierto y $$G_{i+1} \subseteq G_{i}$$. Podemos asumir la monotonía porque, reemplazando $$G_{j}$$ por $$G_{1} \cap \dots \cap G_{j}$$, que sigue siendo abierto, la intersección total no cambia. Además, como $$m(A) < \infty$$, por regularidad exterior existe un abierto $$G \supseteq A$$ con $$m(G) < \infty$$; intersecando cada $$G_{j}$$ con $$G$$ podemos suponer también que $$m(G_{1}) < \infty$$. Luego

$$
A \times [0,a] = \bigcap_{j=1}^{\infty} G_{j} \times [0,a],
$$

con $$G_{i+1} \times [0,a] \subseteq G_{i} \times [0,a]$$ medibles y de medida finita, pues $$m(G_{i} \times [0,a]) = a\, m(G_{i}) \leq a\, m(G_{1}) < \infty$$ por el caso anterior. Entonces, por continuidad desde arriba de la medida,

$$
m(A \times [0,a]) = \lim_{i \to \infty} m(G_{i} \times [0,a]) = \lim_{i \to \infty} a\, m(G_{i}) = a\, m(A).
$$

*Caso medible general con $$m(A) < \infty$$.* En el caso de que $$A$$ sea medible con medida finita, podemos escribir

$$
A = H \setminus Z
$$

con $$H$$ un conjunto $$G_{\delta}$$ tal que $$A \subseteq H$$, $$m(H) = m(A)$$, y $$Z = H \setminus A$$ de medida cero. Entonces, por el paso anterior, $$H \times [0,a]$$ es medible y

$$
m(H \times [0,a]) = a\, m(H).
$$

Se deja de ejercicio probar que

$$
m_{e}(Z \times [0,a]) = 0.
$$

Entonces $$Z \times [0,a]$$ es medible con medida cero,

$$
A \times [0,a] = (H \times [0,a]) \setminus (Z \times [0,a])
$$

es medible, y

$$
m(A \times [0,a]) = m(H \times [0,a]) = a\, m(H) = a\, m(A).
$$

*Caso $$m(A) = \infty$$.* Finalmente, si $$m(A) = \infty$$, llamemos

$$
A_{k} = A \cap B(0,k).
$$

De esta manera

$$
A = \bigcup_{k=1}^{\infty} A_{k},
$$

con $$A_{k} \subseteq A_{k+1}$$ medibles y acotados, en particular de medida finita. Por los argumentos anteriores,

$$
A_{k} \times [0,a] \subseteq A_{k+1} \times [0,a]
$$

son conjuntos medibles tales que

$$
m(A_{k} \times [0,a]) = a\, m(A_{k}).
$$

Entonces $$A \times [0,a] = \bigcup_{k=1}^{\infty} A_{k} \times [0,a]$$ es medible y, por continuidad desde abajo,

$$
m(A \times [0,a]) = \lim_{k \to \infty} m(A_{k} \times [0,a]) = \lim_{k \to \infty} a\, m(A_{k}) = a\, m(A).
$$

### Ejercicio (El producto de un nulo por un intervalo es nulo)

Sea $$Z \subseteq \mathbb{R}^{d}$$ con $$m(Z) = 0$$ y $$a \geq 0$$. Muestre que $$m_{e}(Z \times [0,a]) = 0$$.

## El gráfico de una función medible

### Lema (El gráfico de una función medible tiene medida cero)

Sea $$f : E \to \mathbb{R}$$ medible, con $$E$$ medible. Entonces $$m_{e}(\Gamma(f,E)) = 0$$.

***Prueba:*** Asumamos primero que $$E$$ tiene medida finita. Sea $$\varepsilon > 0$$ y, para cada $$k \in \mathbb{Z}$$,

$$
E_{k} = \{ x \in E :\ k \varepsilon \leq f(x) < (k+1) \varepsilon \}.
$$

Los $$E_{k}$$ son medibles, disjuntos dos a dos, y

$$
E = \bigcup_{k \in \mathbb{Z}} E_{k}.
$$

Note que

$$
\Gamma(f, E_{k}) = \{ (x, f(x)) :\ x \in E_{k} \} \subseteq E_{k} \times [k\varepsilon, (k+1)\varepsilon).
$$

Por el lema anterior y la invariancia de la medida exterior bajo traslaciones, tenemos que

$$
m_{e}(\Gamma(f,E_{k})) \leq m_{e}\big( E_{k} \times [k\varepsilon,(k+1)\varepsilon) \big) \leq \varepsilon\, m(E_{k}).
$$

Por lo tanto, por subaditividad numerable de la medida exterior, vale que

$$
m_{e}(\Gamma(f,E)) = m_{e}\left( \bigcup_{k \in \mathbb{Z}} \Gamma(f,E_{k}) \right) \leq \sum_{k \in \mathbb{Z}} m_{e}(\Gamma(f,E_{k})) \leq \sum_{k \in \mathbb{Z}} \varepsilon\, m(E_{k}) = \varepsilon\, m(E),
$$

donde la última igualdad usa que los $$E_{k}$$ son disjuntos dos a dos. Como $$\varepsilon > 0$$ es arbitrario y $$m(E) < \infty$$, concluimos que $$m_{e}(\Gamma(f,E)) = 0$$.

Terminar la prueba en el caso $$m(E) = \infty$$ queda como ejercicio (véase el ejercicio siguiente).

### Ejercicio (El caso de medida infinita del lema del gráfico)

Termine la prueba del lema anterior: muestre que si $$m(E) = \infty$$, entonces también $$m_{e}(\Gamma(f,E)) = 0$$.

### Lema (La región bajo una función simple no negativa es medible)

Sea $$\phi : E \to \mathbb{R}$$ simple, medible y no negativa, digamos

$$
\phi(x) = \sum_{i=1}^{m} a_{i} \mathbf{1}_{A_{i}},
$$

con $$a_{i} \neq a_{j}$$ y $$A_{i} \cap A_{j} = \emptyset$$ para $$i \neq j$$, y $$E = \bigcup_{i=1}^{m} A_{i}$$. Entonces $$R(\phi,E)$$ es medible.

***Prueba:*** Tenemos que

$$
R(\phi,E) = \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq \phi(x) \} = \bigcup_{j=1}^{m} \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in A_{j},\ 0 \leq y \leq a_{j} \},
$$

es decir, $$R(\phi,E) = \bigcup_{j=1}^{m} A_{j} \times [0,a_{j}]$$, que es una unión finita de conjuntos medibles por el lema del producto, y por lo tanto es un conjunto medible.

### Teorema (La región bajo el gráfico de una función medible no negativa es medible)

Sea $$f : E \to \mathbb{R}$$ medible con $$f \geq 0$$ y $$E$$ medible. Entonces $$R(f,E) \subseteq \mathbb{R}^{d+1}$$ es un conjunto medible.

***Prueba:*** Como $$f \geq 0$$ es medible, existe una sucesión creciente de funciones simples, medibles y no negativas $$\{\phi_{k}\}_{k=1}^{\infty}$$ que satisface

$$
\lim_{k \to \infty} \phi_{k}(x) = f(x)
$$

en $$E$$. Luego, si $$0 \leq y < f(x)$$, como $$\phi_{k}(x) \to f(x) > y$$, existe $$\phi_{k}$$ tal que

$$
0 \leq y \leq \phi_{k}(x).
$$

Entonces, separando los puntos con $$y < f(x)$$ de aquellos con $$y = f(x)$$,

$$
R(f,E) = \{ (x,y) :\ x \in E,\ 0 \leq y < f(x) \} \cup \{ (x,y) :\ x \in E,\ f(x) = y \},
$$

y por lo anterior obtenemos

$$
R(f,E) = \bigcup_{k=1}^{\infty} R(\phi_{k},E) \cup \{ (x,y) :\ x \in E,\ f(x) = y,\ y \geq 0 \},
$$

pues cada $$R(\phi_{k},E) \subseteq R(f,E)$$ al ser $$\phi_{k} \leq f$$. Ahora, cada $$R(\phi_{k},E)$$ es medible por el lema anterior, y el segundo conjunto está contenido en $$\Gamma(f,E)$$, que tiene medida exterior cero y es por lo tanto medible. Concluimos que $$R(f,E)$$ es medible, por ser unión numerable de medibles.

## La definición de la integral

### Definición (Integral de Lebesgue de una función medible no negativa)

Dada $$f : E \to \mathbb{R}$$ medible tal que $$f \geq 0$$, definimos su *integral de Lebesgue* como

$$
\int_{E} f \, dx = m(R(f,E)).
$$

### Proposición (La integral de una función simple no negativa)

Sea $$\phi = \sum_{i=1}^{m} a_{i} \mathbf{1}_{A_{i}}$$ simple, medible y no negativa, con los $$A_{i} \subseteq E$$ medibles y disjuntos dos a dos. Entonces

$$
\int_{E} \phi(x) \, dx = \sum_{i=1}^{m} a_{i}\, m(A_{i}).
$$

***Prueba:*** Podemos asumir que $$a_{i} \neq 0$$ para $$1 \leq i \leq m$$, pues los términos con $$a_{i} = 0$$ no aportan a ninguno de los dos lados. Entonces

$$
\begin{aligned}
\int_{E} \phi(x)\, dx &= m\big( R(\phi,E) \big) \\
&= m\big( \{ \phi = 0 \} \times \{0\} \big) + m\left( \bigcup_{i=1}^{m} \{ (x,y) :\ x \in A_{i},\ 0 \leq y \leq a_{i} \} \right) \\
&= 0 + \sum_{i=1}^{m} a_{i}\, m(A_{i}),
\end{aligned}
$$

donde usamos que $$\{\phi = 0\} \times \{0\}$$ tiene medida cero, que los conjuntos $$A_{i} \times [0,a_{i}]$$ son disjuntos dos a dos porque los $$A_{i}$$ lo son, y la fórmula $$m(A_{i} \times [0,a_{i}]) = a_{i}\, m(A_{i})$$.

### Teorema (Monotonía de la integral respecto al integrando y al dominio)

Sean $$f, g : E \to [0,\infty)$$ medibles.

1. Si $$0 \leq g \leq f$$, entonces

    $$
    \int_{E} g(x) \, dx \leq \int_{E} f(x) \, dx.
    $$
2. Si $$E_{1} \subseteq E_{2} \subseteq E$$ son medibles, entonces

    $$
    \int_{E_{1}} f(x) \, dx \leq \int_{E_{2}} f(x) \, dx.
    $$

***Prueba:*** Dado que $$0 \leq g \leq f$$, tenemos que

$$
\{ (x,y) :\ x \in E,\ 0 \leq y \leq g(x) \} \subseteq \{ (x,y) :\ x \in E,\ 0 \leq y \leq f(x) \},
$$

luego $$R(g,E) \subseteq R(f,E)$$, y la parte (i) se sigue de la monotonía de la medida.

Para la segunda parte vamos primero a probar que

$$
\int_{E_{1}} f(x) \, dx = \int_{E} \mathbf{1}_{E_{1}} f(x) \, dx
$$

para $$E_{1} \subseteq E$$ medible. Note que

$$
\{ (x,y) :\ x \in E,\ 0 \leq y \leq \mathbf{1}_{E_{1}}(x) f(x) \} = \big( (E \setminus E_{1}) \times \{0\} \big) \cup \{ (x,y) :\ x \in E_{1},\ 0 \leq y \leq f(x) \},
$$

y como $$(E \setminus E_{1}) \times \{0\}$$ tiene medida cero, entonces

$$
m\big( R(\mathbf{1}_{E_{1}} f, E) \big) = m\big( R(f,E_{1}) \big).
$$

Ahora, si $$E_{1} \subseteq E_{2}$$ son medibles, entonces

$$
\mathbf{1}_{E_{1}} f \leq \mathbf{1}_{E_{2}} f,
$$

y por la parte (i) obtenemos

$$
\int_{E} \mathbf{1}_{E_{1}} f(x) \, dx \leq \int_{E} \mathbf{1}_{E_{2}} f(x) \, dx.
$$

Concluimos que

$$
\int_{E_{1}} f(x) \, dx \leq \int_{E_{2}} f(x) \, dx.
$$
{% endraw %}
