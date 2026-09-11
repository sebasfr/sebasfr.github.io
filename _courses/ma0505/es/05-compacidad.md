---
layout: chapter
course: ma0505
chapter: 5
title: "Compacidad"
slug: 05-compacidad
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/05-compacidad/
---

{% raw %}
## Compacidad secuencial

### Definición (Conjunto secuencialmente compacto)

$$C \subseteq X$$ es *secuencialmente compacto* si toda sucesión $$\{ x_{n}\}_{n=1}^{\infty} \subseteq C$$ posee una subsucesión convergente a un punto de $$C$$.

### Lema (Caracterización por intersección de clausuras de colas)

Sea $$(X, d)$$ un espacio métrico y $$C \subseteq X$$. Son equivalentes:

1. $$C$$ es secuencialmente compacto;
2. para toda $$\{ x_{n}\}_{n=1}^{\infty} \subseteq C$$,

    $$
    C \cap \left( \bigcap_{k=1}^{\infty} \overline{ \{ x_{m} : m \geq k\}} \right) \neq \emptyset.
    $$

***Prueba:*** $$(1) \implies (2)$$: Si $$\{ x_{n_{k}}\}_{k=1}^{\infty}$$ es una subsucesión que converge a $$x_{0} \in C$$, dado $$\varepsilon > 0$$ existe $$k_{0}$$ tal que $$k \geq k_{0}$$ implica $$d(x_{n_{k}}, x_{0}) < \varepsilon$$. Como $$n_{k} \geq k$$, se sigue que $$B(x_{0}, \varepsilon) \cap \{ x_{m} : m \geq k\} \neq \emptyset$$ para todo $$k \geq 1$$, así $$x_{0} \in \overline{ \{ x_{m} : m \geq k\}}$$ para todo $$k$$.

$$(2) \implies (1)$$: Sea $$x_{0} \in C \cap \bigcap_{k=1}^{\infty} \overline{ \{ x_{m} : m \geq k\}}$$. Construimos iterativamente una subsucesión convergente a $$x_{0}$$: tomamos $$x_{n_{1}} \in B(x_{0}, 1) \cap \{ x_{m} : m \geq 1\}$$, luego $$x_{n_{2}} \in B(x_{0}, \tfrac{1}{2}) \cap \{ x_{m} : m \geq n_{1} + 1\}$$, y en general $$x_{n_{k+1}} \in B(x_{0}, \tfrac{1}{k}) \cap \{ x_{m} : m \geq n_{k} + 1\}$$. Entonces $$x_{n_{k}} \to x_{0}$$.

### Lema (Secuencialmente compacto implica cerrado y acotado)

Sea $$C \subseteq X$$ secuencialmente compacto. Entonces $$C$$ es cerrado y acotado.

***Prueba:*** *Cerrado:* Sea $$x \in \overline{C}$$. Existe $$\{x_{n}\}_{n=1}^{\infty} \subseteq C$$ con $$x_{n} \to x$$. Por compacidad secuencial existe una subsucesión $$\{x_{n_{k}}\}_{k=1}^{\infty}$$ que converge a un punto de $$C$$. Por unicidad del límite, $$x \in C$$, así $$\overline{C} \subseteq C$$.

*Acotado:* Si $$C$$ no fuese acotado, fijado $$x_{0} \in X$$ podríamos elegir $$x_{n} \in C$$ con $$d(x_{0}, x_{n}) \geq n$$. Toda subsucesión $$\{x_{n_{k}}\}$$ satisfaría $$d(x_{0}, x_{n_{k}}) \to \infty$$ y por tanto no podría ser convergente, contradiciendo la compacidad secuencial.

## Cubrimientos por abiertos y compacidad

### Definición (Recubrimiento por abiertos)

Una colección $$\mathcal{U} = \{ U_{\alpha} : \alpha \in \Lambda\}$$ de abiertos es un *recubrimiento* (o *cubrimiento*) de $$A \subseteq X$$ si

$$
A \subseteq \bigcup_{\alpha \in \Lambda} U_{\alpha}.
$$

### Lema (Lema técnico de cubrimientos para conjuntos secuencialmente compactos (Lebesgue))

Sea $$C \subseteq X$$ secuencialmente compacto y $$\mathcal{U}$$ un recubrimiento por abiertos de $$C$$. Entonces existe $$\varepsilon > 0$$ tal que para todo $$x \in C$$ existe $$U \in \mathcal{U}$$ con $$B(x, \varepsilon) \subseteq U$$.

***Prueba:*** Por contradicción: suponga que para todo $$\varepsilon > 0$$ existe $$x_{\varepsilon} \in C$$ tal que $$B(x_{\varepsilon}, \varepsilon) \not\subseteq U$$ para ningún $$U \in \mathcal{U}$$. En particular, para $$\varepsilon = 1/n$$ existe $$x_{n} \in C$$ con $$B(x_{n}, 1/n) \not\subseteq U_{\alpha}$$ para todo $$\alpha \in \Lambda$$.

Por compacidad secuencial existen $$\{x_{n_{k}}\}_{k=1}^{\infty}$$ y $$x_{0} \in C$$ tales que $$x_{n_{k}} \to x_{0}$$. Como $$\mathcal{U}$$ recubre $$C$$, existe $$U_{\alpha_{0}} \in \mathcal{U}$$ con $$x_{0} \in U_{\alpha_{0}}$$ y $$\varepsilon > 0$$ tal que $$B(x_{0}, \varepsilon) \subseteq U_{\alpha_{0}}$$. Tome $$k_{0}$$ tal que $$k \geq k_{0}$$ implique $$d(x_{n_{k}}, x_{0}) < \varepsilon/2$$ y $$1/n_{k} < \varepsilon/2$$. Entonces, para $$y \in B(x_{n_{k}}, 1/n_{k})$$,

$$
d(y, x_{0}) \leq d(y, x_{n_{k}}) + d(x_{n_{k}}, x_{0}) < \tfrac{1}{n_{k}} + \tfrac{\varepsilon}{2} < \varepsilon,
$$

así $$B(x_{n_{k}}, 1/n_{k}) \subseteq B(x_{0}, \varepsilon) \subseteq U_{\alpha_{0}}$$, lo cual contradice la construcción.

### Definición (Conjunto compacto)

$$C \subseteq X$$ es *compacto* si dado un recubrimiento por abiertos $$\mathcal{U} = \{U_{\alpha} : \alpha \in \Lambda\}$$ de $$C$$, existen $$U_{\alpha_{1}}, \dots, U_{\alpha_{m}} \in \mathcal{U}$$ tales que

$$
C \subseteq \bigcup_{k=1}^{m} U_{\alpha_{k}}.
$$

Es decir, todo recubrimiento por abiertos admite un subrecubrimiento finito.

## Equivalencia entre las dos nociones de compacidad

### Lema (Compacidad secuencial equivale a compacidad)

Para $$C \subseteq X$$ son equivalentes:

1. $$C$$ es secuencialmente compacto;
2. $$C$$ es compacto.

***Prueba:*** $$(1) \implies (2)$$: Sea $$\mathcal{U}$$ recubrimiento por abiertos de $$C$$. Por el lema técnico anterior existe $$\varepsilon > 0$$ tal que para cada $$x \in C$$ alguna bola $$B(x, \varepsilon)$$ está contenida en algún $$U_{\alpha}$$. Tomemos $$x_{1} \in C$$ y $$\alpha_{1}$$ con $$B(x_{1}, \varepsilon) \subseteq U_{\alpha_{1}}$$. Si $$C \subseteq B(x_{1}, \varepsilon)$$ ya tenemos un subrecubrimiento finito; si no, escogemos $$x_{2} \in C \setminus B(x_{1}, \varepsilon)$$ y $$U_{\alpha_{2}}$$ con $$B(x_{2}, \varepsilon) \subseteq U_{\alpha_{2}}$$. Iterando, si en algún paso $$C \subseteq \bigcup_{i=1}^{m} B(x_{i}, \varepsilon) \subseteq \bigcup_{i=1}^{m} U_{\alpha_{i}}$$, hemos terminado. De lo contrario, obtenemos $$\{x_{k}\}_{k=1}^{\infty} \subseteq C$$ con $$d(x_{i}, x_{j}) \geq \varepsilon$$ para $$i \neq j$$. Esta sucesión no admite subsucesión convergente: toda subsucesión convergente sería de Cauchy, luego sus términos estarían eventualmente a distancia $$< \varepsilon$$, contradiciendo $$d(x_{i}, x_{j}) \geq \varepsilon$$. Esto contradice la compacidad secuencial.

$$(2) \implies (1)$$: Sea $$\{x_{m}\}_{m=1}^{\infty} \subseteq C$$ y suponga, por contradicción, que no admite subsucesión convergente en $$C$$. Defina $$U_{n} = X \setminus \overline{\{x_{m} : m \geq n\}}$$. Entonces $$U_{n} \subseteq U_{n+1}$$ y $$X \setminus \bigcup_{n=1}^{\infty} U_{n} = \bigcap_{n=1}^{\infty} \overline{\{x_{m} : m \geq n\}}$$. Como $$\{x_{m}\}$$ no tiene subsucesión convergente en $$C$$, $$C \cap \bigcap_{k=1}^{\infty} \overline{\{x_{m} : m \geq k\}} = \emptyset$$, así $$C \subseteq \bigcup_{n=1}^{\infty} U_{n}$$. Por compacidad existe un subrecubrimiento finito; por monotonía de $$\{U_{n}\}$$, existe $$m_{0}$$ con $$C \subseteq U_{m_{0}}$$. Pero entonces $$\{x_{k} : k \geq m_{0}\} \subseteq C \subseteq X \setminus \overline{\{x_{k} : k \geq m_{0}\}}$$, contradicción.

## Compacidad y funciones continuas

### Lema (La imagen continua de un compacto es compacto)

Sea $$f : X \to Y$$ continua y $$K \subseteq X$$ compacto. Entonces $$f(K)$$ es compacto en $$Y$$.

***Prueba:*** Sea $$\mathcal{U} = \{ U_{\alpha} : \alpha \in \Lambda_{1}\}$$ un cubrimiento por abiertos de $$f(K)$$. Entonces $$K \subseteq f^{-1}\!\left( \bigcup_{\alpha \in \Lambda_{1}} U_{\alpha}\right) = \bigcup_{\alpha \in \Lambda_{1}} f^{-1}(U_{\alpha})$$, y cada $$f^{-1}(U_{\alpha})$$ es abierto en $$X$$. Por compacidad de $$K$$, existen $$\alpha_{1}, \dots, \alpha_{m}$$ tales que

$$
K \subseteq \bigcup_{i=1}^{m} f^{-1}(U_{\alpha_{i}}),
$$

de donde $$f(K) \subseteq \bigcup_{i=1}^{m} U_{\alpha_{i}}$$.

### Teorema (Caracterización por la propiedad de intersección finita)

Sea $$(X, d)$$ un espacio métrico. Son equivalentes:

1. $$X$$ es compacto;
2. si $$\mathcal{F} = \{ F_{\alpha} : \alpha \in \Lambda\}$$ es una familia de cerrados tal que $$\bigcap_{\alpha \in A} F_{\alpha} \neq \emptyset$$ para todo $$A \subseteq \Lambda$$ finito, entonces $$\bigcap_{\alpha \in \Lambda} F_{\alpha} \neq \emptyset$$.

***Prueba:*** Para ambas direcciones se usa que $$\bigcap_{\alpha \in \Lambda} F_{\alpha} = \emptyset$$ si y solo si $$X = \bigcup_{\alpha \in \Lambda} (X \setminus F_{\alpha})$$, esto es, $$\{X \setminus F_{\alpha}\}_{\alpha}$$ es un cubrimiento por abiertos de $$X$$.

Si $$X$$ es compacto y se cumple la propiedad de intersección finita pero $$\bigcap_{\alpha} F_{\alpha} = \emptyset$$, existirían $$\alpha_{1}, \dots, \alpha_{m}$$ con $$X = \bigcup_{i=1}^{m} (X \setminus F_{\alpha_{i}})$$, i.e. $$\bigcap_{i=1}^{m} F_{\alpha_{i}} = \emptyset$$, contradicción.

Recíprocamente, dado un cubrimiento por abiertos $$\{ U_{\alpha}\}$$ sin subrecubrimiento finito, $$\{X \setminus U_{\alpha}\}$$ es una familia de cerrados con la propiedad de intersección finita pero intersección total vacía.

## Compacidad en Rd

### Nota (Las cajas en $$\mathbb{R}^{d}$$ son secuencialmente compactas)

Por el teorema de Bolzano-Weierstrass, $$C = [a_{1}, b_{1}] \times \dots \times [a_{d}, b_{d}]$$ con $$a_{i} \leq b_{i}$$ es secuencialmente compacto. Además todo compacto es cerrado y acotado.

### Teorema (Heine-Borel en $$\mathbb{R}^{d}$$)

Sea $$C \subseteq \mathbb{R}^{d}$$. Entonces $$C$$ es compacto respecto de la norma euclídea si y solo si $$C$$ es cerrado y acotado.

***Prueba:*** $$(\implies)$$: Todo compacto es cerrado y acotado por el lema general.

$$(\impliedby)$$: Sea $$F \subseteq \mathbb{R}^{d}$$ cerrado y acotado. Existe $$n$$ tal que $$F \subseteq C_{n} = [-n, n]^{d}$$. Sea $$\{x_{m}\}_{m=1}^{\infty} \subseteq F$$. Como $$C_{n}$$ es secuencialmente compacto, existe $$\{x_{m_{k}}\}_{k=1}^{\infty}$$ subsucesión que converge a $$x_{0} \in C_{n}$$. Como $$\{x_{m_{k}}\} \subseteq F$$ y $$F$$ es cerrado, $$x_{0} \in F$$. Así $$F$$ es secuencialmente compacto y, por la equivalencia, compacto.

### Teorema (Valores extremos)

Sean $$K \subseteq X$$ compacto y $$f : X \to \mathbb{R}$$ continua. Entonces $$f(K)$$ es compacto y, en particular, $$f$$ alcanza su ínfimo y su supremo en $$K$$.

***Prueba:*** $$f(K)$$ es compacto, luego cerrado y acotado en $$\mathbb{R}$$. Sean $$a = \inf_{x \in K} f(x)$$ y $$b = \sup_{x \in K} f(x)$$. Para cada $$n \in \mathbb{N}^{\ast}$$ existe $$x_{n} \in K$$ con $$a \leq f(x_{n}) \leq a + 1/n$$. Por compacidad de $$K$$, existe una subsucesión $$\{x_{n_{k}}\}$$ que converge a $$y_{0} \in K$$, y por continuidad $$f(x_{n_{k}}) \to f(y_{0})$$; pero $$f(x_{n_{k}}) \to a$$, luego $$f(y_{0}) = a$$. Análogamente, $$b$$ se alcanza.
{% endraw %}
