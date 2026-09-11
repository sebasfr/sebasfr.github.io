---
layout: chapter
course: ma0505
chapter: 7
title: "El Teorema de Arzelà-Ascoli"
slug: 07-el-teorema-de-arzela-ascoli
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/07-el-teorema-de-arzela-ascoli/
---

{% raw %}
## El espacio C(K,R)

### Definición (Espacio de funciones continuas sobre un compacto)

Sea $$(X, d)$$ un espacio métrico y $$K \subseteq X$$ compacto. Se define

$$
\mathcal{C}(K, \mathbb{R}) = \{ f : K \to \mathbb{R} \;:\; f \text{ continua}\}
$$

y, para $$f, g \in \mathcal{C}(K, \mathbb{R})$$,

$$
d_{\infty}(f, g) = \sup_{x \in K} |f(x) - g(x)|.
$$

$$(\mathcal{C}(K, \mathbb{R}), d_{\infty})$$ es un espacio métrico cuya convergencia coincide con la convergencia uniforme.

## Equicontinuidad

### Definición (Familia equicontinua)

Sea $$\{f_{\alpha}\}_{\alpha \in \Omega}$$ una familia de funciones $$f_{\alpha} : X \to Y$$ con $$(X, d), (Y, \rho)$$ espacios métricos. Decimos que $$\{f_{\alpha}\}_{\alpha \in \Omega}$$ es *equicontinua* en $$x_{0} \in X$$ si para todo $$\varepsilon > 0$$ existe $$\delta > 0$$ tal que

$$
d(x_{0}, y) < \delta \implies \rho(f_{\alpha}(y), f_{\alpha}(x_{0})) < \varepsilon \quad \text{para todo } \alpha \in \Omega.
$$

La familia es *equicontinua* si lo es en todo punto de $$X$$.

### Lema (Compactos en $$\mathcal{C}(K, \mathbb{R})$$ son equicontinuos)

Sea $$C \subseteq \mathcal{C}(K, \mathbb{R})$$ compacto. Entonces $$C$$ es equicontinuo: dados $$\varepsilon > 0$$ y $$x_{0} \in K$$, existe $$\delta > 0$$ tal que para todo $$f \in C$$ y todo $$y \in K$$ con $$d(x_{0}, y) < \delta$$ se cumple $$|f(y) - f(x_{0})| < \varepsilon$$.

***Prueba:*** Por contradicción: si fallase, existirían $$\varepsilon > 0$$ y $$x_{0} \in K$$ tales que para todo $$n \in \mathbb{N}$$ existen $$y_{n}, k_{n}$$ con $$d(x_{0}, y_{n}) < 1/n$$ y $$|f_{k_{n}}(x_{0}) - f_{k_{n}}(y_{n})| \geq \varepsilon$$, donde $$\{f_{k_{n}}\} \subseteq C$$. Por compacidad existe una subsucesión $$\{f_{k_{n_{l}}}\}_{l \geq 1}$$ que converge uniformemente a una función continua $$f : K \to \mathbb{R}$$. Para simplificar la notación, escribamos $$\tilde{f}_{l} := f_{k_{n_{l}}}$$ y $$\tilde{y}_{l} := y_{n_{l}}$$. Entonces $$\tilde{y}_{l} \to x_{0}$$ y $$|\tilde{f}_{l}(x_{0}) - \tilde{f}_{l}(\tilde{y}_{l})| \geq \varepsilon$$.

Como $$\tilde{y}_{l} \to x_{0}$$ y $$f$$ es continua, existe $$l_{0}$$ tal que $$|f(\tilde{y}_{l}) - f(x_{0})| < \varepsilon/3$$ para $$l \geq l_{0}$$. Entonces, para $$l$$ grande,

$$
|\tilde{f}_{l}(\tilde{y}_{l}) - \tilde{f}_{l}(x_{0})| \leq d_{\infty}(\tilde{f}_{l}, f) + |f(\tilde{y}_{l}) - f(x_{0})| + d_{\infty}(\tilde{f}_{l}, f) < \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} = \varepsilon,
$$

contradiciendo que $$|f_{m_{l}}(y_{l}) - f_{m_{l}}(x_{0})| \geq \varepsilon$$.

### Lema (Equicontinuidad y convergencia puntual a un continuo dan convergencia uniforme)

Sea $$\{f_{n}\}_{n=1}^{\infty}$$ una familia equicontinua de funciones $$f_{n} : X \to Y$$ y $$K \subseteq X$$ compacto tal que $$\lim_{n \to \infty} f_{n}(x) = f_{0}(x)$$ para todo $$x \in K$$, con $$f_{0}$$ continua en $$K$$. Entonces $$\{f_{n}\}$$ converge uniformemente a $$f_{0}$$ en $$K$$.

***Prueba:*** Sea $$\varepsilon > 0$$. Por equicontinuidad, para cada $$x \in K$$ existe $$\delta_{x} > 0$$ tal que $$y \in B(x, \delta_{x})$$ implica $$\rho(f_{n}(x), f_{n}(y)) < \varepsilon/3$$ para todo $$n \geq 0$$. Como $$K$$ es compacto, existen $$x_{1}, \dots, x_{m}$$ con $$K \subseteq \bigcup_{i=1}^{m} B(x_{i}, \delta_{x_{i}})$$. Tome $$n_{0}$$ tal que $$\rho(f_{n}(x_{i}), f_{0}(x_{i})) < \varepsilon/3$$ para todo $$1 \leq i \leq m$$ y todo $$n \geq n_{0}$$.

Para $$y \in K$$, existe $$i$$ con $$y \in B(x_{i}, \delta_{x_{i}})$$, así

$$
\rho(f_{n}(y), f_{0}(y)) \leq \rho(f_{n}(y), f_{n}(x_{i})) + \rho(f_{n}(x_{i}), f_{0}(x_{i})) + \rho(f_{0}(x_{i}), f_{0}(y)) < \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} + \tfrac{\varepsilon}{3} = \varepsilon
$$

para $$n \geq n_{0}$$.

### Lema (Convergencia en denso para familia equicontinua produce continuidad)

Sean $$D \subseteq X$$ denso y $$\{f_{n}\}_{n=1}^{\infty}$$ una sucesión equicontinua de funciones $$f_{n} : X \to Y$$. Suponga que $$\{f_{n}(x)\}_{n=1}^{\infty}$$ converge para todo $$x \in D$$ y que para cada $$x \in X$$ el conjunto $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ es completo (en particular esto se cumple si $$Y$$ es completo, o si $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ es compacto). Entonces $$\{f_{n}(x)\}$$ converge para todo $$x \in X$$ y su límite es continuo.

***Prueba:*** *Convergencia.* Sea $$x \in X$$ y $$\varepsilon > 0$$. Por equicontinuidad existe $$\delta > 0$$ con

$$
d(x, y) < \delta \implies \rho(f_{n}(x), f_{n}(y)) < \varepsilon/3 \quad \text{para todo } n \geq 1.
$$

Por densidad existe $$y \in B(x, \delta) \cap D$$ y, como $$\{f_{n}(y)\}$$ converge, existe $$n_{0}$$ con $$\rho(f_{n}(y), f_{m}(y)) < \varepsilon/3$$ para $$n, m \geq n_{0}$$. Entonces

$$
\rho(f_{n}(x), f_{m}(x)) \leq \rho(f_{n}(x), f_{n}(y)) + \rho(f_{n}(y), f_{m}(y)) + \rho(f_{m}(y), f_{m}(x)) < \varepsilon,
$$

así $$\{f_{n}(x)\}$$ es de Cauchy. Como $$\{f_{n}(x)\} \subseteq \overline{\{f_{n}(x)\}}$$ y este último es completo por hipótesis, $$\{f_{n}(x)\}$$ converge en $$\overline{\{f_{n}(x)\}} \subseteq Y$$.

*Continuidad del límite.* Definamos $$f(x) = \lim_{n} f_{n}(x)$$. Para $$d(x, y) < \delta$$,

$$
\rho(f(x), f(y)) = \lim_{n \to \infty} \rho(f_{n}(x), f_{n}(y)) \leq \tfrac{\varepsilon}{3},
$$

así $$f$$ es continua en $$x$$.

### Nota (Hipótesis suficientes sobre el codominio)

La hipótesis “$$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ completo” del lema anterior se satisface, por ejemplo, cuando $$Y$$ es completo (todo cerrado de un completo es completo) o cuando $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ es compacto (por compacto $$\Rightarrow$$ completo). El segundo caso es el que se usa en el Teorema de Arzelà-Ascoli más adelante.

### Lema (Convergencia puntual en compacto bajo equicontinuidad implica uniforme)

Sea $$\{f_{n}\}_{n=1}^{\infty}$$ una familia equicontinua, $$f_{n} : X \to Y$$, y $$K \subseteq X$$ compacto. Si $$\lim_{n \to \infty} f_{n}(x) = f_{0}(x)$$ existe en $$Y$$ para todo $$x \in K$$, entonces $$f_{0}$$ es continua y $$f_{n}$$ converge uniformemente a $$f_{0}$$ en $$K$$.

***Prueba:*** *Continuidad de $$f_{0}$$.* Sea $$x \in K$$ y $$\varepsilon > 0$$. Por equicontinuidad existe $$\delta > 0$$ tal que para todo $$n \geq 1$$, $$d(x, y) < \delta$$ implica $$\rho(f_{n}(x), f_{n}(y)) < \varepsilon/3$$. Pasando al límite $$n \to \infty$$,

$$
\rho(f_{0}(x), f_{0}(y)) = \lim_{n \to \infty} \rho(f_{n}(x), f_{n}(y)) \leq \tfrac{\varepsilon}{3} < \varepsilon
$$

para $$d(x, y) < \delta$$, lo que prueba la continuidad de $$f_{0}$$ sin requerir hipótesis adicional sobre $$Y$$.

*Convergencia uniforme.* Aplicando el primer lema de equicontinuidad (*Equicontinuidad y convergencia puntual a un continuo dan convergencia uniforme*) con el límite continuo $$f_{0}$$ recién obtenido, $$f_{n} \to f_{0}$$ uniformemente en $$K$$.

## El teorema

### Teorema (Arzelà-Ascoli)

Sean $$X$$ separable y $$\{f_{n}\}_{n=1}^{\infty}$$ una familia equicontinua de funciones $$f_{n} : X \to Y$$. Suponga que $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$ es compacto para todo $$x \in X$$. Entonces existe una subsucesión de $$\{f_{n}\}$$ que converge puntualmente a una función continua $$f : X \to Y$$. Además, la convergencia es uniforme en cada compacto $$K \subseteq X$$.

***Prueba:*** Sea $$D = \{x_{n}\}_{n=1}^{\infty} \subseteq X$$ denso (existe por separabilidad). Como $$\overline{\{f_{n}(x_{1})\}_{n=1}^{\infty}}$$ es compacto, existe una subsucesión $$\{f_{n_{k}}^{1}\}_{k}$$ tal que $$\{f_{n_{k}}^{1}(x_{1})\}$$ converge. Análogamente $$\overline{\{f_{n_{k}}^{1}(x_{2})\}_{k}}$$ es compacto (es un cerrado contenido en el compacto $$\overline{\{f_{n}(x_{2})\}_{n=1}^{\infty}}$$, luego compacto), de modo que existe una subsucesión $$\{f_{n_{k}}^{2}\}$$ de $$\{f_{n_{k}}^{1}\}$$ tal que $$\{f_{n_{k}}^{2}(x_{2})\}$$ converge.

Iterando, dado $$\{f_{n_{k}}^{m}\}$$ con $$\{f_{n_{k}}^{m}(x_{j})\}$$ convergente para $$1 \leq j \leq m$$, extraemos $$\{f_{n_{k}}^{m+1}\}$$ subsucesión de $$\{f_{n_{k}}^{m}\}$$ tal que $$\{f_{n_{k}}^{m+1}(x_{m+1})\}$$ converge. Por construcción, $$\{f_{n_{k}}^{m}(x_{j})\}$$ converge para $$1 \leq j \leq m$$.

Tomamos la subsucesión *diagonal* $$\{f_{n_{m}}^{m}\}_{m=1}^{\infty}$$. Para $$j \leq m$$, $$\{f_{n_{m}}^{m}(x_{j})\}_{m \geq j}$$ es una subsucesión de $$\{f_{n_{k}}^{j}\}$$ y por tanto converge. Así $$\{f_{n_{m}}^{m}\}$$ converge puntualmente sobre $$D$$ y es equicontinua. Además, para cada $$x \in X$$, $$\overline{\{f_{n_{m}}^{m}(x)\}_{m=1}^{\infty}}$$ es un cerrado contenido en el compacto $$\overline{\{f_{n}(x)\}_{n=1}^{\infty}}$$, luego compacto y en particular completo. Por el lema previo (aplicado con esta condición de completitud sobre las clausuras de los valores), $$\{f_{n_{m}}^{m}\}$$ converge en todo $$X$$ a una función continua $$f$$, y la convergencia es uniforme en compactos.
{% endraw %}
