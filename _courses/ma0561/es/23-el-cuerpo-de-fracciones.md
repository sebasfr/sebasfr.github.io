---
layout: chapter
course: ma0561
chapter: 23
title: "El cuerpo de fracciones"
slug: 23-el-cuerpo-de-fracciones
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/23-el-cuerpo-de-fracciones/
---

{% raw %}
## La construcción

### Definición (La relación de proporcionalidad en $$D \times (D \setminus \{0\})$$)

Sea $$D$$ un dominio entero y sea $$S = D \times (D \setminus \{0\})$$. Defina la relación $$\sim$$ en $$S$$ tal que

$$
(a, b) \sim (c, d) \iff a \cdot d = b \cdot c.
$$

Usamos la notación $$\frac{a}{b} := [(a, b)]$$ para la clase de equivalencia de $$(a, b)$$.

### Lema (La relación de proporcionalidad es de equivalencia)

La relación $$\sim$$ es una relación de equivalencia en $$S$$.

***Prueba:*** La reflexividad y la simetría son inmediatas de la conmutatividad de $$D$$: $$a \cdot b = b \cdot a$$ da $$(a,b) \sim (a,b)$$, y si $$a d = b c$$, entonces $$c b = d a$$, es decir, $$(c, d) \sim (a, b)$$.

Para la transitividad usamos que $$D$$ es un dominio entero. Suponga que $$(a, b) \sim (c, d)$$ y $$(c, d) \sim (e, f)$$, es decir, $$a d = b c$$ y $$c f = d e$$. Multiplicando la primera igualdad por $$f$$ y usando la segunda,

$$
a d f = b c f = b d e,
$$

y reordenando con la conmutatividad, $$d (a f) = d (b e)$$, es decir, $$d (a f - b e) = 0$$. Como $$d \neq 0$$ y $$D$$ no tiene divisores de cero, concluimos que $$a f - b e = 0$$, o sea $$a f = b e$$, que es exactamente $$(a, b) \sim (e, f)$$.

### Definición (El cuerpo de fracciones y sus operaciones)

Sea $$F := \left\{ \frac{a}{b} :\ (a, b) \in S \right\}$$. Note que si $$x \in D \setminus \{0\}$$, entonces $$\frac{a}{b} = \frac{a \cdot x}{b \cdot x}$$. Además, podemos definir operaciones en $$F$$ de la siguiente manera:

$$
\frac{a}{b} + \frac{c}{d} = \frac{a d + b c}{b d}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}.
$$

Note que los denominadores $$b d$$ son no nulos porque $$D$$ es un dominio entero, que $$\frac{0}{1}$$ es el neutro de $$+$$ y que $$\frac{1}{1}$$ es el neutro de $$\cdot$$. La buena definición de estas operaciones (su independencia de los representantes) se verifica en la prueba del teorema siguiente.

### Teorema (El cuerpo de fracciones es un cuerpo)

$$(F, +, \cdot, \frac{0}{1}, \frac{1}{1})$$ es un anillo conmutativo y, más interesantemente, en realidad es un cuerpo.

***Prueba:*** *Buena definición de las operaciones.* Suponga que $$\frac{a}{b} = \frac{a'}{b'}$$ y $$\frac{c}{d} = \frac{c'}{d'}$$, es decir, $$a b' = a' b$$ y $$c d' = c' d$$. Para la suma hay que ver que $$\frac{a d + b c}{b d} = \frac{a' d' + b' c'}{b' d'}$$, o sea, que $$(a d + b c) b' d' = (a' d' + b' c') b d$$. Usando la conmutatividad y las dos relaciones,

$$
(a d + b c)\, b' d' = (a b')\, d d' + (c d')\, b b' = (a' b)\, d d' + (c' d)\, b b' = (a' d' + b' c')\, b d.
$$

Para el producto, $$(a c)(b' d') = (a b')(c d') = (a' b)(c' d) = (a' c')(b d)$$, es decir, $$\frac{a c}{b d} = \frac{a' c'}{b' d'}$$.

*$$F$$ es un anillo conmutativo.* Los denominadores $$b d$$ son no nulos, pues $$D$$ es un dominio entero. La asociatividad, la conmutatividad de ambas operaciones y la distributividad se verifican con representantes y se reducen a las propiedades correspondientes de $$D$$; el neutro aditivo es $$\frac{0}{1}$$, el inverso aditivo de $$\frac{a}{b}$$ es $$\frac{-a}{b}$$, y el neutro multiplicativo es $$\frac{1}{1}$$.

*$$F$$ es un cuerpo.* Note primero que $$1 \neq 0$$ en $$D$$ (si $$1 = 0$$, entonces $$D = \{0\}$$ y no habría denominadores disponibles), y entonces $$\frac{1}{1} \neq \frac{0}{1}$$ en $$F$$, pues $$1 \cdot 1 \neq 0 \cdot 1$$. Sea ahora $$\frac{a}{b} \neq \frac{0}{1}$$; esto significa que $$a \cdot 1 \neq b \cdot 0$$, es decir, $$a \neq 0$$. Entonces $$\frac{b}{a} \in F$$ (el denominador $$a$$ es no nulo) y

$$
\frac{a}{b} \cdot \frac{b}{a} = \frac{a b}{b a} = \frac{1}{1},
$$

pues $$(a b) \cdot 1 = (b a) \cdot 1$$. Es decir, todo elemento no nulo de $$F$$ es invertible, y $$F$$ es un cuerpo.

### Nota (Ejemplos de cuerpos de fracciones)

Escribimos $$F = \operatorname{Frac}(D)$$ para el *cuerpo de fracciones* de $$D$$.

- $$\operatorname{Frac}(\mathbb{Z}) \cong \mathbb{Q}$$.
- Si $$D$$ es un cuerpo, entonces $$\operatorname{Frac}(D) \cong D$$.
- Si $$D = \Bbbk[x_{1}, \dots, x_{n}]$$ con $$\Bbbk$$ un cuerpo, entonces

    $$
    \operatorname{Frac}(D) = \Bbbk(x_{1}, \dots, x_{n}) = \left\{ \frac{p(x_{1}, \dots, x_{n})}{q(x_{1}, \dots, x_{n})} :\ q \neq 0 \right\},
    $$

    el cuerpo de funciones racionales en $$n$$ variables.

### Nota (El dominio se sumerge en su cuerpo de fracciones)

Podemos suponer que $$D \subseteq \operatorname{Frac}(D)$$, pues $$i : D \to \operatorname{Frac}(D)$$, $$x \mapsto \frac{x}{1}$$, es un homomorfismo inyectivo, por lo que $$D$$ se “sumerge” en $$\operatorname{Frac}(D)$$; esto es,

$$
D \cong \operatorname{Im}(i) = \left\{ \frac{x}{1} :\ x \in D \right\} \subseteq \operatorname{Frac}(D).
$$

## La propiedad universal

### Teorema (Propiedad universal del cuerpo de fracciones)

Sea $$D$$ un dominio entero, $$K$$ un cuerpo y $$f : D \to K$$ un homomorfismo inyectivo. Entonces existe un único homomorfismo inyectivo $$\tilde{f} : \operatorname{Frac}(D) \to K$$ tal que

$$
\tilde{f}\left( \frac{x}{1} \right) = f(x) \quad \text{para todo } x \in D.
$$

De forma explícita,

$$
\tilde{f}\left( \frac{a}{b} \right) = \frac{f(a)}{f(b)} := f(a) \cdot f(b)^{-1} \quad \text{para todos } a, b \in D,\ b \neq 0.
$$

***Prueba:*** *$$\tilde{f}$$ está bien definida.* Si $$\frac{a}{b} = \frac{c}{d}$$, entonces $$a d = b c$$, y aplicando $$f$$ obtenemos $$f(a) \cdot f(d) = f(b) \cdot f(c)$$. Note que $$f(b) \neq 0$$ y $$f(d) \neq 0$$, pues $$b, d \neq 0$$ y $$f$$ es inyectiva (su núcleo es trivial). Entonces, despejando en el cuerpo $$K$$, tenemos que

$$
\frac{f(a)}{f(b)} = \frac{f(c)}{f(d)} \in K \implies \tilde{f}\left( \frac{a}{b} \right) = \tilde{f}\left( \frac{c}{d} \right).
$$

Probar que $$\tilde{f}$$ es un homomorfismo inyectivo queda como ejercicio.

*Unicidad.* Suponga que $$h : \operatorname{Frac}(D) \to K$$ es un homomorfismo tal que $$h\left( \frac{x}{1} \right) = f(x)$$ para todo $$x \in D$$. Sea $$b \neq 0$$; como $$\frac{b}{1} \cdot \frac{1}{b} = \frac{b}{b} = \frac{1}{1}$$ y los homomorfismos preservan unidades, tenemos que $$h\left( \frac{1}{b} \right) = h\left( \frac{b}{1} \right)^{-1} = f(b)^{-1}$$. Entonces

$$
h\left( \frac{a}{b} \right) = h\left( \frac{a}{1} \cdot \frac{1}{b} \right) = h\left( \frac{a}{1} \right) \cdot h\left( \frac{1}{b} \right) = f(a) \cdot f(b)^{-1} = \frac{f(a)}{f(b)} = \tilde{f}\left( \frac{a}{b} \right),
$$

es decir, $$h = \tilde{f}$$.

### Teorema (El cuerpo primo como cuerpo de fracciones del anillo primo)

Sea $$\Bbbk$$ un cuerpo.

1. Si $$R$$ es el subanillo primo de $$\Bbbk$$ y $$F$$ es el subcuerpo primo de $$\Bbbk$$, entonces $$F \cong \operatorname{Frac}(R)$$.
2. El subcuerpo primo de $$\Bbbk$$ es isomorfo a $$\mathbb{Q}$$ o a $$\mathbb{Z}_{p}$$ (también denotado $$\mathbb{F}_{p}$$), según $$\operatorname{char}(\Bbbk) = 0$$ o $$\operatorname{char}(\Bbbk) = p > 0$$.

***Prueba:*** *Parte 1.* Como todo subcuerpo de $$\Bbbk$$ es en particular un subanillo, el subanillo primo $$R$$ está contenido en el subcuerpo primo $$F$$, y entonces la inclusión $$i : R \to F$$, $$x \mapsto x$$, es un homomorfismo inyectivo de $$R$$ en el cuerpo $$F$$. Además, $$R$$ es un dominio entero, por ser subanillo de un cuerpo. Por la propiedad universal del cuerpo de fracciones, existe un homomorfismo inyectivo $$\tilde{\imath} : \operatorname{Frac}(R) \to F$$ con $$\tilde{\imath}\left(\frac{a}{b}\right) = a b^{-1}$$. Sea

$$
F_{0} = \operatorname{Im}(\tilde{\imath}) = \{ a b^{-1} :\ a, b \in R,\ b \neq 0 \} \subseteq F.
$$

Como $$\tilde{\imath}$$ es un homomorfismo inyectivo desde un cuerpo, $$F_{0} \cong \operatorname{Frac}(R)$$ y $$F_{0}$$ es un subcuerpo de $$\Bbbk$$: es un subanillo (imagen de un homomorfismo), y el inverso de $$a b^{-1} \neq 0$$ es $$b a^{-1} \in F_{0}$$. Por la minimalidad del subcuerpo primo, $$F \subseteq F_{0}$$; y ya vimos que $$F_{0} \subseteq F$$. Concluimos que

$$
F = F_{0} \cong \operatorname{Frac}(R).
$$

*Parte 2.* Por el teorema del subanillo primo, $$R \cong \mathbb{Z}$$ o $$R \cong \mathbb{Z}_{n}$$; y como $$\Bbbk$$ es un cuerpo, en particular un dominio entero, su característica es $$0$$ o un primo $$p$$. Si $$\operatorname{char}(\Bbbk) = 0$$, entonces $$R \cong \mathbb{Z}$$ y, por la parte 1 (un isomorfismo de dominios se extiende a los cuerpos de fracciones vía la propiedad universal),

$$
F \cong \operatorname{Frac}(R) \cong \operatorname{Frac}(\mathbb{Z}) \cong \mathbb{Q}.
$$

Si $$\operatorname{char}(\Bbbk) = p$$ primo, entonces $$R \cong \mathbb{Z}_{p}$$, que ya es un cuerpo (pues $$p$$ es primo), y el cuerpo de fracciones de un cuerpo es él mismo:

$$
F \cong \operatorname{Frac}(\mathbb{Z}_{p}) \cong \mathbb{Z}_{p} = \mathbb{F}_{p}.
$$
{% endraw %}
