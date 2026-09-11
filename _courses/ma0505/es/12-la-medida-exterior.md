---
layout: chapter
course: ma0505
chapter: 12
title: "La medida exterior"
slug: 12-la-medida-exterior
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/12-la-medida-exterior/
---

{% raw %}
## Motivación: medir longitudes y áreas

La longitud de un segmento $$[a,b)$$ es $$b - a$$; la de una unión finita de intervalos disjuntos $$[a_{i}, b_{i})$$ es $$\sum_{i} (b_{i} - a_{i})$$.

![La medida elemental de un intervalo](/assets/img/courses/ma0505/medida-elemental-intervalo.svg)

Un punto tiene longitud cero, pues $$\{a\} \subseteq [a, a + \varepsilon)$$ da $$\ell(\{a\}) \leq \varepsilon$$ para todo $$\varepsilon > 0$$. En consecuencia, toda unión finita de puntos tiene longitud cero. Pero, ¿cuál es la “longitud” de $$\mathbb{Q} \cap [0,1]$$? Si se enumeran $$\mathbb{Q} \cap [0,1] = \{q_{n}\}_{n=1}^{\infty}$$, cada $$\bigcup_{i=1}^{n}\{q_{i}\}$$ tiene longitud $$0$$; formalmente, $$\mathbf{1}_{\mathbb{Q} \cap [0,1]} = \lim_{n} \mathbf{1}_{\bigcup_{i=1}^{n}\{q_{i}\}}$$, y si pudiera intercambiarse límite e integral se obtendría “$$\int_{0}^{1} \mathbf{1}_{\mathbb{Q} \cap [0,1]} = 0$$”. El problema es que $$\mathbf{1}_{\mathbb{Q} \cap [0,1]}$$ no es Riemann integrable. La *medida exterior* captura esta idea de tamaño sin depender de la integral de Riemann.

## La medida elemental y la medida exterior en R

### Definición (Familia de intervalos y medida elemental)

Sea

$$
S = \{[a,b] : a < b\} \cup \{(-\infty, b] : b \in \mathbb{R}\} \cup \{[a, \infty) : a \in \mathbb{R}\} \cup \{\emptyset\}.
$$

Se define $$m : S \to [0, \infty]$$ por $$m([a,b]) = b - a$$ (si $$a < b$$), $$m((-\infty, b]) = m([a, \infty)) = \infty$$ y $$m(\emptyset) = 0$$. Sobre uniones finitas de intervalos con interiores disjuntos se extiende aditivamente: si los $$\mathring{I_{i}}$$ son disjuntos dos a dos e $$I_{i} = [a_{i}, b_{i}]$$, entonces $$m\big(\bigcup_{i=1}^{k} I_{i}\big) = \sum_{i=1}^{k}(b_{i} - a_{i})$$.

### Ejercicio (Monotonía de la medida elemental sobre cubrimientos)

Pruebe que si $$\bigcup_{k=1}^{n} I_{k} \subseteq \bigcup_{\ell=1}^{m} J_{\ell}$$ con los interiores $$\mathring{I_{k}}$$ disjuntos dos a dos, entonces

$$
\sum_{k=1}^{n} m(I_{k}) \leq \sum_{\ell=1}^{m} m(J_{\ell}).
$$

### Definición (Medida exterior)

Dado $$E \subseteq \mathbb{R}$$, su *medida exterior* es

$$
m_{e}(E) = \inf\left\{ \sum_{k=1}^{\infty} m(I_{k}) : E \subseteq \bigcup_{k=1}^{\infty} I_{k},\ I_{k} \in S \right\}.
$$

De la definición se sigue inmediatamente la *monotonía*: si $$E_{1} \subseteq E_{2}$$, entonces $$m_{e}(E_{1}) \leq m_{e}(E_{2})$$.

### Lema (Medida exterior de un intervalo)

Para $$a < b$$, $$m_{e}([a,b]) = b - a$$.

***Prueba:*** Como $$[a,b] \in S$$ se cubre a sí mismo, $$m_{e}([a,b]) \leq b - a$$. Para la cota inferior, sea $$\{I_{k}\} \subseteq S$$ con $$[a,b] \subseteq \bigcup_{k} I_{k}$$ y fije $$\varepsilon > 0$$. Si algún $$I_{k}$$ es no acotado (de la forma $$(-\infty, b]$$ o $$[a, \infty)$$), entonces $$\sum_{k} m(I_{k}) = \infty \geq b - a$$ y ese cubrimiento no restringe el ínfimo; podemos pues suponer cada $$I_{k} = [a_{k}, b_{k}]$$ finito. Para cada $$k$$ elija un intervalo abierto $$I_{k}^{\ast} \supseteq I_{k}$$ con $$m(\overline{I_{k}^{\ast}}) \leq (1 + \varepsilon)\, m(I_{k})$$. Entonces $$[a,b] \subseteq \bigcup_{k} I_{k}^{\ast}$$ y, por compacidad de $$[a,b]$$, existe $$k_{0}$$ con $$[a,b] \subseteq \bigcup_{k=1}^{k_{0}} I_{k}^{\ast} \subseteq \bigcup_{k=1}^{k_{0}} \overline{I_{k}^{\ast}}$$. Como un intervalo cubierto por finitos intervalos tiene longitud a lo sumo la suma de las longitudes,

$$
b - a \leq \sum_{k=1}^{k_{0}} m(\overline{I_{k}^{\ast}}) \leq (1 + \varepsilon)\sum_{k=1}^{k_{0}} m(I_{k}) \leq (1 + \varepsilon)\sum_{k=1}^{\infty} m(I_{k}).
$$

Por tanto $$\frac{b - a}{1 + \varepsilon} \leq \sum_{k} m(I_{k})$$; tomando ínfimo sobre los cubrimientos, $$\frac{b - a}{1 + \varepsilon} \leq m_{e}([a,b])$$, y haciendo $$\varepsilon \to 0$$, $$b - a \leq m_{e}([a,b])$$.

### Lema (Subaditividad numerable de la medida exterior)

Sean $$E_{k} \subseteq \mathbb{R}$$ para $$k \geq 1$$. Entonces

$$
m_{e}\left(\bigcup_{k=1}^{\infty} E_{k}\right) \leq \sum_{k=1}^{\infty} m_{e}(E_{k}).
$$

***Prueba:*** Si algún $$m_{e}(E_{k}) = \infty$$ la desigualdad es trivial, así que suponemos $$m_{e}(E_{k}) < \infty$$ para todo $$k$$. Sea $$\varepsilon > 0$$. Por definición de medida exterior, para cada $$k$$ existen $$\{I_{i}^{k}\}_{i=1}^{\infty} \subseteq S$$ con $$E_{k} \subseteq \bigcup_{i} I_{i}^{k}$$ y

$$
\sum_{i=1}^{\infty} m(I_{i}^{k}) \leq m_{e}(E_{k}) + \frac{\varepsilon}{2^{k}}.
$$

La familia numerable $$\{I_{i}^{k}\}_{i,k}$$ cubre $$\bigcup_{k} E_{k}$$, luego

$$
m_{e}\left(\bigcup_{k} E_{k}\right) \leq \sum_{k=1}^{\infty}\sum_{i=1}^{\infty} m(I_{i}^{k}) \leq \sum_{k=1}^{\infty}\left( m_{e}(E_{k}) + \frac{\varepsilon}{2^{k}}\right) = \sum_{k=1}^{\infty} m_{e}(E_{k}) + \varepsilon.
$$

Como $$\varepsilon > 0$$ es arbitrario, se concluye.

## La medida exterior en Rd

### Definición (Medida exterior en $$\mathbb{R}^{d}$$)

Sea $$S_{d} = \{[a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}] : a_{k} \leq b_{k}\} \cup \{\emptyset\}$$ y $$m\big([a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}]\big) = \prod_{k=1}^{d}(b_{k} - a_{k})$$. Para $$E \subseteq \mathbb{R}^{d}$$,

$$
m_{e}(E) = \inf\left\{ \sum_{k=1}^{\infty} m(I_{k}) : E \subseteq \bigcup_{k=1}^{\infty} I_{k},\ I_{k} \in S_{d} \right\}.
$$

### Lema (Medida exterior de una caja)

Sea $$I = [a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}]$$. Entonces $$m_{e}(I) = \prod_{k=1}^{d}(b_{k} - a_{k})$$.

***Prueba:*** La cota $$m_{e}(I) \leq \prod_{k}(b_{k} - a_{k})$$ es inmediata pues $$I \in S_{d}$$. La cota inferior repite el argumento del caso unidimensional: dado un cubrimiento $$\{I_{k}\} \subseteq S_{d}$$ de $$I$$ y $$\varepsilon > 0$$, se dilatan los $$I_{k}$$ a cajas abiertas $$I_{k}^{\ast} \supseteq I_{k}$$ con $$m(\overline{I_{k}^{\ast}}) \leq (1 + \varepsilon) m(I_{k})$$; por compacidad de $$I$$ basta un subcubrimiento finito, y la aditividad finita del volumen sobre cajas (con interiores disjuntos, tras subdividir) da $$\prod_{k}(b_{k} - a_{k}) \leq (1 + \varepsilon)\sum_{k} m(I_{k})$$. Se concluye haciendo $$\varepsilon \to 0$$.

### Lema (Subaditividad numerable en $$\mathbb{R}^{d}$$)

Sean $$E_{i} \subseteq \mathbb{R}^{d}$$ para $$i \geq 1$$. Entonces $$m_{e}\big(\bigcup_{i} E_{i}\big) \leq \sum_{i} m_{e}(E_{i})$$.

***Prueba:*** La demostración del caso unidimensional no usa la dimensión: cubriendo cada $$E_{i}$$ por cajas de $$S_{d}$$ con suma de volúmenes menor que $$m_{e}(E_{i}) + \varepsilon/2^{i}$$ y reuniendo los cubrimientos, se obtiene $$m_{e}\big(\bigcup_{i} E_{i}\big) \leq \sum_{i} m_{e}(E_{i}) + \varepsilon$$ para todo $$\varepsilon > 0$$.

### Ejemplo (Conjuntos de medida exterior cero)

1. Si $$m_{e}(E_{i}) = 0$$ para todo $$i \geq 1$$, por subaditividad $$m_{e}\big(\bigcup_{i} E_{i}\big) \leq \sum_{i} m_{e}(E_{i}) = 0$$.
2. Para $$x = (x_{1}, \dots, x_{d})$$, $$\{x\} \subseteq [x_{1}, x_{1} + \varepsilon] \times \dots \times [x_{d}, x_{d} + \varepsilon]$$ da $$m_{e}(\{x\}) \leq \varepsilon^{d}$$, luego $$m_{e}(\{x\}) = 0$$. Por (a), todo conjunto numerable tiene medida exterior cero; en particular $$m_{e}(\mathbb{Q}^{d}) = 0$$.

## Aproximación por abiertos y conjuntos G-delta

### Lema (Aproximación de la medida exterior por abiertos)

Sean $$E \subseteq \mathbb{R}^{d}$$ y $$\varepsilon > 0$$. Entonces existe un abierto $$G \subseteq \mathbb{R}^{d}$$ con $$E \subseteq G$$ y

$$
m_{e}(E) \leq m_{e}(G) \leq m_{e}(E) + \varepsilon.
$$

***Prueba:*** La cota $$m_{e}(E) \leq m_{e}(G)$$ es la monotonía. Suponga $$m_{e}(E) < \infty$$ (si no, $$G = \mathbb{R}^{d}$$ sirve). Tome $$\{I_{i}\}_{i=1}^{\infty} \subseteq S_{d}$$ con $$E \subseteq \bigcup_{i} I_{i}$$ y $$\sum_{i} m(I_{i}) \leq m_{e}(E) + \varepsilon/2$$. Para cada $$i$$ elija una caja $$I_{i}^{\ast}$$ con $$I_{i} \subseteq \mathring{I_{i}^{\ast}}$$ y $$m(I_{i}^{\ast}) \leq m(I_{i}) + \varepsilon/2^{i+1}$$. Entonces $$G = \bigcup_{i} \mathring{I_{i}^{\ast}}$$ es abierto, $$E \subseteq G$$ y, por subaditividad,

$$
m_{e}(G) \leq \sum_{i=1}^{\infty} m_{e}(\mathring{I_{i}^{\ast}}) \leq \sum_{i=1}^{\infty} m(I_{i}^{\ast}) \leq \sum_{i=1}^{\infty}\left(m(I_{i}) + \frac{\varepsilon}{2^{i+1}}\right) \leq m_{e}(E) + \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = m_{e}(E) + \varepsilon.
$$

### Definición (Conjunto $$G_{\delta}$$)

Un conjunto $$H \subseteq \mathbb{R}^{d}$$ es de tipo *$$G_{\delta}$$* si es intersección numerable de abiertos: $$H = \bigcap_{k=1}^{\infty} G_{k}$$ con cada $$G_{k}$$ abierto.

### Lema (Envoltura $$G_{\delta}$$ de igual medida exterior)

Para todo $$E \subseteq \mathbb{R}^{d}$$ existe un conjunto $$G_{\delta}$$, $$H \supseteq E$$, con $$m_{e}(E) = m_{e}(H)$$.

***Prueba:*** Por el lema anterior, para cada $$k \geq 1$$ existe un abierto $$G_{k} \supseteq E$$ con $$m_{e}(E) \leq m_{e}(G_{k}) \leq m_{e}(E) + \tfrac{1}{k}$$. Sea $$H = \bigcap_{k} G_{k}$$, conjunto $$G_{\delta}$$ con $$E \subseteq H$$. Por monotonía, $$m_{e}(H) \leq m_{e}(G_{k}) \leq m_{e}(E) + \tfrac{1}{k}$$ para todo $$k$$, luego $$m_{e}(H) \leq m_{e}(E)$$; la desigualdad opuesta es la monotonía $$m_{e}(E) \leq m_{e}(H)$$.

## Conjuntos Lebesgue medibles

### Definición (Conjunto Lebesgue medible)

$$E \subseteq \mathbb{R}^{d}$$ es *Lebesgue medible* si para todo $$\varepsilon > 0$$ existe un abierto $$G \supseteq E$$ con $$m_{e}(G \setminus E) < \varepsilon$$. Si $$E$$ es medible se define su *medida de Lebesgue* como $$m(E) = m_{e}(E)$$.

### Ejemplo (Intervalos y conjuntos de medida exterior cero son medibles)

Si $$E = [a,b]$$, tomando $$G = (a - \tfrac{\varepsilon}{2}, b + \tfrac{\varepsilon}{2})$$ se tiene $$m_{e}(G \setminus E) = m_{e}\big((a - \tfrac{\varepsilon}{2}, a) \cup (b, b + \tfrac{\varepsilon}{2})\big) \leq \varepsilon$$; análogamente $$[a,b)$$, $$(a,b]$$ y $$(a,b)$$ son medibles, con $$m([a,b]) = b - a$$. Si $$m_{e}(E) = 0$$, por aproximación existe un abierto $$G \supseteq E$$ con $$m_{e}(G) < \varepsilon$$, y entonces $$m_{e}(G \setminus E) \leq m_{e}(G) < \varepsilon$$; por tanto todo conjunto de medida exterior cero es medible.

### Teorema (Unión numerable de conjuntos medibles es medible)

Sea $$\{E_{i}\}_{i=1}^{\infty}$$ una familia de conjuntos medibles. Entonces $$E = \bigcup_{i=1}^{\infty} E_{i}$$ es medible.

***Prueba:*** Sea $$\varepsilon > 0$$. Para cada $$i$$ existe un abierto $$G_{i} \supseteq E_{i}$$ con $$m_{e}(G_{i} \setminus E_{i}) < \varepsilon/2^{i}$$. Entonces $$G = \bigcup_{i} G_{i}$$ es abierto, $$E \subseteq G$$ y

$$
G \setminus E = \Big(\bigcup_{i} G_{i}\Big) \setminus E \subseteq \bigcup_{i} (G_{i} \setminus E_{i}),
$$

pues si $$x \in G_{i}$$ pero $$x \notin E$$ entonces $$x \notin E_{i}$$. Por subaditividad y monotonía,

$$
m_{e}(G \setminus E) \leq \sum_{i=1}^{\infty} m_{e}(G_{i} \setminus E_{i}) < \sum_{i=1}^{\infty}\frac{\varepsilon}{2^{i}} = \varepsilon.
$$

### Ejercicio (Aditividad de la medida exterior sobre cajas con interiores disjuntos)

Sea $$I_{j} = I_{1}^{j} \times \dots \times I_{d}^{j}$$ con cada $$I_{i}^{j}$$ un intervalo finito y $$\mathring{I_{i}} \cap \mathring{I_{j}} = \emptyset$$ para $$i \neq j$$. Pruebe que

$$
m_{e}\left(\bigcup_{j=1}^{m} I_{j}\right) = \sum_{j=1}^{m} m_{e}(I_{j}).
$$

### Lema (Aditividad para conjuntos a distancia positiva)

Si $$E_{1}, E_{2} \subseteq \mathbb{R}^{d}$$ satisfacen $$d(E_{1}, E_{2}) > 0$$, entonces

$$
m_{e}(E_{1} \cup E_{2}) = m_{e}(E_{1}) + m_{e}(E_{2}).
$$

***Prueba:*** La desigualdad $$\leq$$ es la subaditividad. Para $$\geq$$, sea $$\varepsilon > 0$$ y $$\{I_{k}\} \subseteq S_{d}$$ con $$E_{1} \cup E_{2} \subseteq \bigcup_{k} I_{k}$$ y $$\sum_{k} m(I_{k}) \leq m_{e}(E_{1} \cup E_{2}) + \varepsilon$$. Subdividiendo cada caja si es necesario (lo que no altera la suma de volúmenes, por la aditividad finita del volumen sobre cajas con interiores disjuntos, cf. el ejercicio anterior), puede suponerse $$\operatorname{diam}(I_{k}) < \tfrac{1}{2} d(E_{1}, E_{2})$$. Entonces ninguna caja corta a la vez a $$E_{1}$$ y a $$E_{2}$$: si $$I_{k} \cap E_{1} \neq \emptyset$$, entonces $$I_{k} \cap E_{2} = \emptyset$$. Separando el cubrimiento en las cajas $$\{J_{\ell}\}$$ que cortan a $$E_{1}$$ y las $$\{\widetilde{J}_{\ell}\}$$ que cortan a $$E_{2}$$,

$$
m_{e}(E_{1}) + m_{e}(E_{2}) \leq \sum_{\ell} m(J_{\ell}) + \sum_{\ell} m(\widetilde{J}_{\ell}) \leq \sum_{k} m(I_{k}) \leq m_{e}(E_{1} \cup E_{2}) + \varepsilon.
$$

Como $$\varepsilon$$ es arbitrario, $$m_{e}(E_{1}) + m_{e}(E_{2}) \leq m_{e}(E_{1} \cup E_{2})$$.
{% endraw %}
