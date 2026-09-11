---
layout: chapter
course: ma0561
chapter: 11
title: "Acciones de grupo"
slug: 11-acciones-de-grupo
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/11-acciones-de-grupo/
---

{% raw %}
## Definiciones y propiedades elementales

### Definición (Acción de Grupos)

Sea $$(G, \cdot)$$ un grupo y sea $$X$$ un conjunto. Decimos que $$G$$ actúa sobre $$X$$ (o que $$X$$ es un $$G$$-conjunto) si existe una función $$\alpha: G \times X \to X$$ tal que

1. $$\forall g,h \in G  \quad\forall x \in X  \quad \Big( \alpha\big(g, \alpha(h,x)\big) = \alpha(g \cdot h, x)\Big)$$,
2. $$\forall x \in X  \quad\Big( \alpha(1_{G}, x) = x \Big)$$.

### Notación (Acción de un elemento)

Si $$G$$ actúa sobre $$X$$, dado $$g \in G$$, denotamos $$\alpha_{g}:X \to X$$ tal que $$x \mapsto \alpha(g,x)$$. Si conocemos la acción específica, es común escribir $$g \cdot x$$.

### Nota (Propiedades inmediatas)

1. Para todos $$g,h \in G$$ y para todo $$x \in X$$, tenemos que $$\alpha_{g}(\alpha_{h}(x)) = \alpha_{g \cdot h}(x)$$.
2. $$\alpha_{1_{G}} = \mathrm{id}_{X}$$

### Ejemplos (Acciones usuales)

1. Sea $$n \in \mathbb{N}$$. Considere $$G = S_{n}$$ y $$X = \{ 1,\dots,n \}$$. Defina $$\alpha: S_{n} \times X \to X$$ tal que $$(\sigma, i) \mapsto \sigma(i)$$. Note que si $$\gamma,\sigma \in S_{n}$$, dado $$i \in X$$,

    $$
    \alpha_{\sigma}(\alpha_{\gamma}(i)) = \alpha_{\sigma}(\gamma(i)) = (\sigma \circ \gamma)(i) = \alpha_{\sigma \circ \gamma} (i).
    $$

Además, $$\alpha_{\mathrm{id}}(i) = \mathrm{id}(i) = i$$. Por tanto, $$\alpha$$ es una acción de grupos y $$S_{n}$$ actúa sobre $$X$$.

1. Sean $$G = (\mathbb{Z}, +)$$ y $$X = \mathbb{R}$$. Defina $$\tau: G \times X \to X$$ tal que $$(n,x) \mapsto x+ n$$. Note que dados $$m,n \in \mathbb{Z}$$ y $$x \in \mathbb{R}$$,

    $$
    \tau_{n}(\tau_{m(x)}) = \tau_{n}(x+m) = (x+m)+n = x + (m+n) = \tau_{m+n}(x).
    $$

Además, $$\tau_{0}(x) = x+0 = x$$. Por tanto, $$\mathbb{Z}$$ actúa sobre $$\mathbb{R}$$.

1. Sean $$G = \mathrm{GL}_{n}(\mathbb{R})$$ y $$X = \mathbb{R}^{n}$$. Defina $$\alpha: G \times X \to X$$ tal que $$(A,v) \mapsto A v$$. Mostrar que $$\alpha$$ es una acción de grupos queda como ejercicio.

1. Dado un grupo $$G$$, defina $$\mu:G \times G \to G$$ tal que $$(g,h) \mapsto g \cdot h$$. Es fácil ver que $$\mu$$ es una acción de grupo. Así, $$G$$ actúa sobre sí mismo.

### Lema (Acción es biyectiva sobre $$X$$)

Sea $$G$$ un grupo y $$X$$ un conjunto. Suponga que $$\alpha:G \times X \to X$$ es una acción de grupos. Entonces, si $$g \in G$$, $$\alpha_{g}: X \to X$$ tal que $$x \mapsto \alpha(g,x)$$ es una biyección, i.e., $$\alpha_{g} \in S_{x}$$.

***Prueba:*** Considere $$\alpha_{g^{-1}}:X \to X$$ tal que $$x \mapsto \alpha(g^{-1}, x)$$. Note que

$$
(\alpha_{g} \circ \alpha_{g^{-1}})(x) = \alpha_{g \circ g ^{-1}}(x) = \alpha_{1_{G}}(x) = x.
$$

De la misma forma, $$(\alpha_{g^{-1}} \circ \alpha_{g}) = \mathrm{id}_{X}$$, por lo que concluimos que la función es biyectiva.

### Teorema (Acciones y homomorfismos están en biyección)

Sea $$G$$ un grupo y $$X$$ un conjunto. Defina

$$
\begin{aligned}
\Omega:&= \{ \alpha: G \times X  \to X: \alpha \text{ es una acción de } G \text{ en }X\},\\
\Sigma:&= \{ \phi: G \to S_{X} : \phi \text{ es homomorfismo de grupos} \}.
\end{aligned}
$$

Entonces, $$\Omega$$ y $$\Sigma$$ están en biyección

***Prueba:*** Defina $$\Phi: \Omega \to \Sigma$$ de la siguiente manera. Dada una acción $$\alpha: G \times X \to X$$, defina $$\phi:G \to S_{X}$$ tal que $$\phi(g) = \alpha_{g}$$ donde $$\alpha_{g}:X \to X$$ es tal que $$x \mapsto\alpha(g,x)$$. Es fácil ver que $$\phi$$ es un homomorfismo y que $$\alpha_{g} \in S_{X}$$. Tome $$\Phi(\alpha) = \phi$$.
Ahora, defina $$\Psi: \Sigma \to \Omega$$ de la siguiente manera. Dado $$\phi:G\to S_{X}$$ homomorfismo, sea $$\alpha:G \times X \to X$$ tal que $$(g,x) \mapsto \phi(g)(x) \in X$$. Note que $$\alpha$$ es una acción, pues si $$g,h \in G$$y $$x \in X$$, tenemos que

$$
\begin{aligned}
\alpha(g \cdot h,x) = \phi(gh) (x) &= (\phi(g) \circ \phi(h))(x) \\
&= \phi(g) \big(\phi(h)(x)\big) \\
&=\phi(g) (\alpha(h, x)) \\
&=\alpha(g, \alpha(h,x)),
\end{aligned}
$$

y además, dado $$x \in X$$, $$\alpha(1_{G}, x) = \phi(1_{G})(x) = \mathrm{id}_{X}(x) = x$$. Tome $$\Psi(\phi) = \alpha$$. Verificar que $$\Phi \circ \Psi = \mathrm{id}_{\Sigma}$$ y que $$\Psi \circ \Phi = \mathrm{id}_{\Omega}$$ queda como ejercicio.

### Teorema (Cayley)

Dado $$G$$ un grupo, $$G$$ es isomorfo a un subgrupo de $$S_{G}$$.

***Prueba:*** Considere $$\mu_{g}:G \to G$$ tal que $$h \mapsto g\cdot h$$. Sea $$\phi: G \to S_{G}$$ tal que $$g \mapsto \mu_{g}$$. Ya vimos que $$\phi$$ es un homomorfismo. Veamos que $$\phi$$ es inyectivo:

$$
g \in \operatorname{Ker}(\phi) \iff \phi(g) = \mu_{g}= \mathrm{id}_{G} \iff g \cdot x = x  \quad \forall x \in G \iff g =1_{G},
$$

por lo que $$\operatorname{Ker}(\phi) = \{ 1_{G} \}$$. Ahora, usando el primer teorema del isomorfismo, obtenemos que

$$
G / \operatorname{Ker}(\phi) = G/\{ 1_{G} \} = G\cong \operatorname{Im}(\phi) \leq  S_{G},
$$

de donde concluimos el resultado.
{% endraw %}
