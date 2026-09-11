---
layout: chapter
course: ma0505
chapter: 1
title: "Repaso: normas en Rd y conexidad"
slug: 01-repaso-normas-en-rd-y-conexidad
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/01-repaso-normas-en-rd-y-conexidad/
---

{% raw %}
## Normas en Rd

### Definición (Familia de normas $$p$$ en $$\mathbb{R}^{d}$$)

En $$\mathbb{R}^{d}$$ se consideran las siguientes normas:

1. *Euclídea*: $$\|(x_{1},\dots,x_{d})\| = (x_{1}^{2}+\dots+x_{d}^{2})^{1/2}$$.
2. *Norma del supremo*: $$\|(x_{1},\dots,x_{d})\|_{\infty} = \max\{ |x_{i}| : 1 \leq i \leq d\}$$.
3. *Norma $$p$$* ($$1 \leq p < \infty$$): $$\|(x_{1},\dots,x_{d})\|_{p} = (|x_{1}|^{p}+\dots+|x_{d}|^{p})^{1/p}$$.

El caso $$p = 2$$ coincide con la norma euclídea, esto es,

$$
\|(x_{1},\dots,x_{d})\| = \|(x_{1},\dots,x_{d})\|_{2}.
$$

### Definición (Bola asociada a una norma $$p$$)

Para $$x_{0} \in \mathbb{R}^{d}$$ y $$r > 0$$ se define

$$
B_{p}(x_{0},r) = \{ x \in \mathbb{R}^{d} : \|x - x_{0}\|_{p} < r \}.
$$

Cuando $$p = 2$$ se escribe simplemente $$B(x_{0},r)$$.

### Definición (Conjunto abierto en $$\mathbb{R}^{d}$$)

$$D \subseteq \mathbb{R}^{d}$$ es un *conjunto abierto* si para todo $$x_{0} \in D$$ existe $$r > 0$$ tal que

$$
B(x_{0},r) \subseteq D.
$$

En particular $$\emptyset$$ y $$\mathbb{R}^{d}$$ son abiertos, y toda bola es abierta.

## Equivalencia de normas p en Rd

### Proposición (Cotas entre la norma euclídea y la norma del supremo)

Para todo $$(x_{1},\dots,x_{d}) \in \mathbb{R}^{d}$$,

$$
\|(x_{1},\dots,x_{d})\|_{\infty} \leq \|(x_{1},\dots,x_{d})\| \leq \sqrt{d}\,\|(x_{1},\dots,x_{d})\|_{\infty}.
$$

***Prueba:*** Para $$1 \leq i \leq d$$, $$|x_{i}| \leq \sqrt{x_{1}^{2}+\dots+x_{d}^{2}} = \|(x_{1},\dots,x_{d})\|$$, lo cual da $$\|(x_{1},\dots,x_{d})\|_{\infty} \leq \|(x_{1},\dots,x_{d})\|$$. Recíprocamente,

$$
\|(x_{1},\dots,x_{d})\| = \sqrt{x_{1}^{2}+\dots+x_{d}^{2}} \leq \left(d \max_{1 \leq i \leq d} |x_{i}|^{2}\right)^{1/2} = \sqrt{d}\,\|(x_{1},\dots,x_{d})\|_{\infty}.
$$

### Proposición (Cotas entre la norma $$p$$ y la norma del supremo)

Para todo $$1 \leq p < \infty$$ y todo $$(x_{1},\dots,x_{d}) \in \mathbb{R}^{d}$$,

$$
\|(x_{1},\dots,x_{d})\|_{\infty} \leq \|(x_{1},\dots,x_{d})\|_{p} \leq d^{1/p} \|(x_{1},\dots,x_{d})\|_{\infty}.
$$

En consecuencia $$\|(x_{1},\dots,x_{d})\| \leq \sqrt{d}\,\|(x_{1},\dots,x_{d})\|_{p}$$.

***Prueba:*** Para cada $$1\leq i\leq d$$, $$|x_{i}|^{p}\leq \sum_{j=1}^{d}|x_{j}|^{p}$$, y tomando $$p$$-ésima raíz se obtiene la cota inferior. Para la cota superior,

$$
\sum_{j=1}^{d} |x_{j}|^{p} \leq d \max_{1\leq j\leq d} |x_{j}|^{p},
$$

y al tomar $$p$$-ésima raíz se concluye. La última desigualdad combina ambas con la cota euclídea $$\leq \sqrt{d} \|\cdot\|_{\infty}$$.

### Lema (Las normas $$p$$ definen los mismos abiertos en $$\mathbb{R}^{d}$$)

Las normas $$\|\cdot\|_{p}$$ ($$1\leq p\leq\infty$$) determinan la misma familia de conjuntos abiertos en $$\mathbb{R}^{d}$$.

***Prueba:*** Basta mostrar que dado $$r > 0$$ existe $$r_{p} > 0$$ con $$B_{p}(x,r_{p}) \subseteq B(x,r)$$ y, recíprocamente, existe $$r' > 0$$ con $$B(x,r') \subseteq B_{p}(x,r)$$. Por la proposición anterior, si $$\|x-y\|_{p} < r/\sqrt{d}$$ entonces $$\|x-y\| \leq \sqrt{d}\,\|x-y\|_{p} < r$$, de modo que $$r_{p} = r/\sqrt{d}$$ cumple

$$
B_{p}\!\left(x,\tfrac{r}{\sqrt{d}}\right) \subseteq B(x,r).
$$

Análogamente, $$B(x, r/d^{1/p}) \subseteq B_{p}(x,r)$$. Por tanto cada abierto respecto de una norma lo es respecto de la otra.

## Conexidad y arcoconexidad en Rd

### Definición (Conjunto disconexo y conexo)

$$G \subseteq \mathbb{R}^{d}$$ es *disconexo* si existen $$G_{0}, G_{1}$$ abiertos tales que

$$
G_{0} \cap G \neq \emptyset, \quad G_{1} \cap G \neq \emptyset, \quad G_{0} \cap G_{1} = \emptyset \quad\text{y}\quad G \subseteq G_{0} \cup G_{1}.
$$

Un conjunto se dice *conexo* si no es disconexo.

### Definición (Curva)

Una *curva* es una función continua $$\gamma : [a,b] \to \mathbb{R}^{d}$$.

### Definición (Conjunto arcoconexo)

$$E \subseteq \mathbb{R}^{d}$$ es *arcoconexo* si para todos $$x_{0}, x_{1} \in E$$ existe una curva $$\gamma : [a,b] \to \mathbb{R}^{d}$$ tal que

$$
\gamma(a) = x_{0}, \quad \gamma(b) = x_{1} \quad\text{y}\quad \gamma(t) \in E \text{ para todo } t \in [a,b].
$$

### Nota (Reparametrización al intervalo $$[0,1]$$)

Si $$\gamma : [a,b] \to \mathbb{R}^{d}$$ es continua, entonces $$\gamma_{1} : [0,1] \to \mathbb{R}^{d}$$ dada por $$\gamma_{1}(s) = \gamma((b-a)s + a)$$ es continua. Por tanto, en la definición de arcoconexidad puede suponerse $$a = 0$$ y $$b = 1$$.

### Lema (Un arcoconexo no admite descomposición en abiertos disjuntos)

Sea $$E \subseteq \mathbb{R}^{d}$$ arcoconexo. Entonces no existen $$G_{0}, G_{1}$$ abiertos no vacíos tales que $$E \subseteq G_{0} \cup G_{1}$$ y $$G_{0} \cap G_{1} = \emptyset$$.

***Prueba:*** Supongamos que tales $$G_{0}, G_{1}$$ existen y tomemos $$x_{0} \in G_{0} \cap E$$, $$x_{1} \in G_{1} \cap E$$. Por arcoconexidad existe $$\gamma : [0,1] \to E$$ con $$\gamma(0)=x_{0}$$ y $$\gamma(1)=x_{1}$$. Como $$G_{0}$$ es abierto, existe $$r > 0$$ con $$B(x_{0}, r) \subseteq G_{0}$$. Por continuidad de $$\gamma$$ existe $$\delta > 0$$ tal que $$|t| < \delta$$ implica $$\|\gamma(0) - \gamma(t)\| < r$$, de modo que $$\gamma(t) \in B(x_{0}, r) \subseteq G_{0}$$ para $$0 < t < \delta$$.

Definamos

$$
t_{0} = \sup \{ t > 0 : \gamma(s) \in G_{0},\ 0 \leq s < t \}.
$$

El conjunto está acotado por $$1$$ y contiene a $$\delta/2$$ (pues $$\gamma(s) \in G_{0}$$ para $$0 \leq s < \delta$$ por lo anterior), así que $$\delta/2 \leq t_{0} \leq 1$$. Si $$\gamma(t_{0}) \in G_{0}$$, existe $$r_{1} > 0$$ con $$B(\gamma(t_{0}), r_{1}) \subseteq G_{0}$$ y, por continuidad, existe $$\delta_{1} > 0$$ con $$|t_{0} - s| < \delta_{1} \implies \gamma(s) \in B(\gamma(t_{0}), r_{1}) \subseteq G_{0}$$. Esto contradice la definición de supremo.

Por tanto $$\gamma(t_{0}) \in E \setminus G_{0} \subseteq G_{1}$$. Pero existirían entonces $$r_{2}, \delta_{2} > 0$$ tales que $$|t_{0} - s| < \delta_{2} \implies \gamma(s) \in B(\gamma(t_{0}), r_{2}) \subseteq G_{1}$$. Por definición de supremo existe $$s' \in (t_{0} - \delta_{2}, t_{0})$$ con $$\gamma(s') \in G_{0}$$; pero entonces $$\gamma(s') \in G_{0} \cap G_{1} = \emptyset$$, contradicción.

### Teorema (Relación entre conexidad y arcoconexidad en $$\mathbb{R}^{d}$$)

Sea $$G \subseteq \mathbb{R}^{d}$$. Entonces:

1. Si $$G$$ es arcoconexo, entonces $$G$$ es conexo.
2. Si $$G$$ es abierto y conexo, entonces $$G$$ es arcoconexo.

***Prueba:*** La parte (1) es consecuencia directa del lema anterior. La parte (2) se demuestra fijando $$x_{0} \in G$$ y considerando el conjunto $$A = \{ x \in G : x \text{ se puede unir a } x_{0} \text{ por una curva en } G\}$$; usando que $$G$$ es abierto se prueba que $$A$$ y $$G \setminus A$$ son ambos abiertos, y por conexidad y $$A \neq \emptyset$$ se concluye $$A = G$$.
{% endraw %}
