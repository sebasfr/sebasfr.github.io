---
layout: chapter
course: ma0561
chapter: 12
title: "Órbitas y estabilizadores"
slug: 12-orbitas-y-estabilizadores
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/12-orbitas-y-estabilizadores/
---

{% raw %}
## Órbitas y estabilizadores

Sea $$G$$ un grupo y $$X$$ un conjunto. Sea $$\alpha$$ una acción de $$G$$ sobre $$X$$. Defina la relación $$\sim$$ en $$X$$ tal que $$x \sim y \iff \exists g \in G \Big(\alpha_{g}(x) = y\Big)$$. Es fácil ver que $$\sim$$ es una relación de equivalencia.

### Definición (Órbita)

Sea $$G$$ un grupo y $$X$$ un conjunto tal que $$G$$ actúa sobre $$X$$ por la acción $$\alpha$$. Dada la relación de equivalencia $$\sim$$ arriba definida, definimos la órbita de $$x \in X$$ como

$$
\mathcal{O}_{x} := \{ y \in X:y \sim x \} = \{ y \in X: \exists g \in G \big( \alpha_{g}(x) = y \big) \}.
$$

Como $$\sim$$ es una relación de equivalencia, las órbitas forman una partición de $$X$$, i.e., $$X = \dot\bigcup_{x \in X} \mathcal{O}_{x}$$.

### Definición (Acción transitiva)

Sea $$G$$ un grupo y $$X$$ un conjunto tal que $$G$$ actúa sobre $$X$$. Si existe $$x \in X$$ tal que $$\mathcal{O}_{x} =X$$ decimos que la acción es transitiva. Equivalentemente, la acción es transitiva si para todos $$x,y \in X$$ existe $$g \in G$$ tal que $$x = \alpha_{g}(y)$$.

### Definición (Estabilizador)

Sea $$G$$ un grupo y $$X$$ un conjunto tal que $$G$$ actúa sobre $$X$$ por la acción $$\alpha$$. Dado $$x \in X$$, definimos el estabilizador de $$x$$ por $$G_{x}:= \{ g \in G:\alpha_{g}(x)=x \}$$.

### Lema (Estabilizador es un subgrupo)

***Prueba:*** $$G_{x} \neq \emptyset$$ pues $$1_{G} \in G_{x}$$ por definición. Ahora, sean $$g,h \in G_{x}$$. Note que $$\alpha_{h^{-1}}(x) = (\alpha_{h})^{-1}(x) = x$$. Finalmente, tenemos que

$$
\alpha_{gh^{-1}}(x) = \alpha_{g}(\alpha_{h^{-1}}(x)) = x,
$$

por lo que $$g \cdot h^{-1} \in G_{x}$$, de donde concluimos que $$G_{x} \leq G$$.

### Ejemplos (Órbitas y estabilizadores)

1. Sea $$n\geq2$$. Considere la acción de $$S_{n}$$ sobre $$X = \{ 1,\dots,n \}$$ tal que $$\alpha_{\sigma}(i) = \sigma(i)$$. En este caso hay una única órbita. Sean $$i,j \in X$$ y considere $$\tau = \begin{pmatrix}i & j\end{pmatrix}$$. Note que $$\alpha_{\tau}(i) = j$$, por lo que $$i \sim j$$, i.e., todo par de elementos de $$X$$ se relacionan. Por tanto la acción es transitiva. Ahora, note que si $$1 \leq i\leq n$$, $$G_{i} = \{ \sigma \in S_{n}: \sigma(i) = i \} \cong S_{n-1}$$.

1. Considere $$G = (\mathbb{Z}, + )$$ y $$X=\mathbb{R}$$ bajo la acción $$\tau(n,x) = x+n$$. Note que si $$x,y \in \mathbb{R}$$,

    $$
    x \sim y \iff \exists n \in \mathbb{Z} \Big(\tau_{n}(x) = y\Big) \iff \exists n \in \mathbb{Z} \Big(y=x+n\Big) \iff x-y \in \mathbb{Z},
    $$

de donde tenemos que $$x$$ y $$y$$ tienen la misma parte decimal. Hay una cantidad no numerable de órdenes. Es evidente ver que para todo $$x \in \mathbb{R}$$, $$G_{x} = \{ 0 \}$$.

1. Considere $$G = \mathbb{S}^{1} =\{ e^{i\theta}:\theta \in [0, 2\pi) \}$$ y $$X = \mathbb{C}$$. Defina la acción $$\rho_{\theta}(z) = z e^{i \theta}$$ (ver que esto es una acción es un ejercicio). Sea $$z \in \mathbb{C}$$. Entonces,

    $$
    \mathcal{O}_{z} = \{ \rho_{\theta}(z): \theta \in [0, 2\pi) \} = \{ ze^{i \theta}: \theta \in [0,2\pi) \} = \{ w \in \mathbb{C}: \lvert w \rvert  = \lvert z \rvert  \}.
    $$

Ahora, veamos qué pasa con el estabilizador. Si $$z = 0$$, tenemos que

$$
G_{0} = \{ \theta \in \mathbb{S}^{1}: \rho_{\theta}(0) = 0 \} = \{ g \in \mathbb{S}^{1}: 0 e^{i \theta} = 0 \} = \mathbb{S}^{1}.
$$

Por otro lado, si $$z \neq 0$$,

$$
\rho_{\theta}(z) = z \iff z e^{i \theta} = z \iff \theta = 0 \iff e^{i \theta } = 1,
$$

lo que implica que $$G_{Z} = \{ 1 \}$$.

1. Sea $$G$$ un grupo y $$H \leq G$$. Considere $$G / H = \{ gH : g \in G\}$$. Defina una acción de $$G$$ en $$G / H$$ tal que $$\mu:G \times G / H\to G /H$$ tal que $$\mu_{g}(hH) = (g \cdot h) H$$. Queda como ejercicio ver que $$\mu$$ es una acción transitiva. Ahora, note que

    $$
    g \in G_{xH} \iff (g \cdot x) H = xH \iff x ^{-1} \cdot g \cdot x \in H \iff g \in x H x ^{-1},
    $$

de modo que $$G_{xH} = xH x ^{-1}$$.

1. Sea $$G = \mathrm{GL}(n,\mathbb{R})$$ y $$X = \mathbb{R}^n$$. Defina la acción $$\alpha_{A}(v)=Av$$. Note que

    $$
    \mathcal{O}_{0} = \{ v \in \mathbb{R}: \exists A \in G (Av = w) \} = \{ 0 \}.
    $$

Por tanto, esta acción no es transitiva.

1. Sea $$G$$ un grupo. Defina $$\mu:G\to G$$ tal que $$\mu_{g}(h) = gh$$. Sean $$h,g \in G$$. Note que $$\mu_{gh^{-1}}(h) = (gh^{-1})h=g$$, de modo que $$h \sim g$$. Por tanto, la acción es transitiva.

1. Sea $$G$$ un grupo y considere la acción de $$G$$ en $$G$$ como la conjugación $$\mu_{g}(h) = ghg^{-1}$$. Sea $$x \in G$$. Tenemos que

    $$
    x^G := O_{x} = \{ y \in G: \exists g \in G (g xg^{-1} = y) \} = \{ gxg^{-1}:g \in G \}.
    $$

Por otro lado, $$G_{x}:= \{ g \in G: gxg^{-1} = x \} = C_{G}(x)$$ (el centralizador).

### Teorema (Órbita y cociente del estabilizador)

Sea $$G$$ un grupo y $$X$$ un conjunto tal que $$G$$ actúa sobre $$X$$. Sea $$x \in X$$. Entonces $$\lvert \mathcal{O}_{x} \rvert = [G:G_{x}]$$.

***Prueba:*** Vamos a construir una biyección $$\Phi:\mathcal{O}_{x} \to G / G_{x}$$. Sea $$y \in \mathcal{O}_{x}$$. Entonces existe $$g \in G$$ tal que $$\alpha_{g}(x) = y$$. Defina $$\Phi(y) = g \cdot G_{x}$$. $$\Phi$$ está bien definida, pues si $$g,h$$ son tales que $$\alpha_{g}(x) = \alpha_{h}(x)$$, entonces

$$
\alpha_{h^{-1}g}(x) = \alpha_{h^{-1}}(\alpha_{g}(x)) = \alpha_{h^{-1}}(\alpha_{h}(x)) = \alpha_{1_{G}}(x) = x,
$$

de modo que $$h^{-1}g \in G_{x}$$ y por tanto $$g \cdot G_{x} = h \cdot G_{x}$$. $$\Phi$$ es inyectiva pues si $$y,z \in \mathcal{O}_{x}$$ tal que $$\Phi(y) = \Phi(z)$$, existen $$g,h \in G$$ tales que $$\alpha_{g}(x) = y$$ y $$\alpha_{h}(x) = z$$. Así, tenemos que

$$
g G_{x} = h G_{x} \implies h^{-1} g \in G_{x} \implies \alpha_{h^{-1}g}(x)=x.
$$

Así, $$\alpha_{h^{-1}}(\alpha_{g}(x)) = \alpha_{h}^{-1}(\alpha_{g}(x)) = x \implies \alpha_{g}(x)=\alpha_{h}(x)$$. Finalmente $$\Phi$$ es sobreyectiva, pues si $$g \cdot G_{x} \in G / G_{x}$$, tome $$y = \alpha_{g}(x)$$. Note que $$\Phi(y) = g \cdot G_{x}$$. Así, $$\Phi$$ es una biyección y por tanto los conjuntos dados poseen la misma cardinalidad.

### Corolario (La órbita divide al orden del grupo)

Sea $$G$$ un grupo finito y $$X$$ un conjunto tal que $$G$$ actúa sobre $$X$$. Entonces para todo $$x \in X$$, $$\lvert \mathcal{O}_{x} \rvert \Big\lvert \lvert G \rvert$$.

***Prueba:*** Tenemos que $$\lvert \mathcal{O}_{x} \rvert = [G:G_{x}] =\frac{ \lvert G \rvert}{\lvert G_{x} \rvert}$$, de donde concluimos el resultado

### Corolario (Tamaño de la clase de conjugación)

Sea $$G$$ un grupo finito y $$x \in G$$, Entonces $$\lvert x^{G} \rvert = [G:C_{G}(x)]$$.

### Teorema (Cauchy)

Sea $$G$$ un grupo finito y $$p$$ un primo tal que $$p \Big\lvert \lvert G \rvert$$. Entonces existe $$g \in G$$ tal que $$\lvert g \rvert = p$$.

***Prueba:*** [**Prueba 1, para grupos abelianos.**]
Suponga que $$G$$ es abeliano. Procedemos por inducción fuerte sobre $$\lvert G \rvert=n$$. El caso base ($$n=1$$) es trivialmente cierto por vacuidad. Suponga como hipótesis inductiva que el resultado es cierto para todo grupo $$H$$ tal que $$\lvert H \rvert < n$$. Sea $$a \in G$$ con $$a \neq 1_{G}$$ y $$k = \lvert  a \rvert$$. Considere los siguientes casos:
**Caso 1:** Suponga que $$p \mid k$$. Entonces, existe $$\ell \in \mathbb{N}$$ tal que $$p \ell = k$$. Luego $$\lvert a^{\ell} \rvert = p$$.
**Caso 2:** Suponga que $$p \not\mid k$$. Sea $$H = \langle a \rangle$$. Como $$G$$ es abeliano, $$H \triangleleft G$$, por lo que $$G/H$$ es un grupo y $$\lvert H \rvert = k$$. Note que

$$
\lvert G / H \rvert = \frac{\lvert G \rvert }{\lvert H \rvert } = \frac{n}{k} < n.
$$

Como $$p \mid n$$ y $$p \not\mid k$$, $$p \mid \frac{n}{k}$$. Por la hipótesis inductiva, existe $$sH \in G /H$$ tal que $$\lvert sH \rvert = p$$. Sea $$m = \lvert s \rvert$$. Note que $$(sH)^{m} = s^{m}H = H$$, por lo que $$p \mid m$$. Finalmente, aplique el caso 1 sobre $$s$$. Concluimos el resultado

***Prueba:*** [**Prueba 2, general.**]
Sea $$x \in G$$. Recuerde que $$x^{G} = \{ g x g^{-1}: g \in G \}$$ y que $$\lvert x^{G} \rvert = [G:C_{G}(x)]$$. Procedemos por inducción fuerte sobre $$\lvert G \rvert=n$$. Considere los siguientes casos:
**Caso 1:** Si $$x \in Z(G)$$, entonces $$x^{G}=\{ x \} \implies G = C_{G}(x)$$.
**Caso 2:** Si $$x \not\in Z(G)$$, entonces $$\lvert x^{G} \rvert > 1$$. Entonces $$C_{G}(x) < G \implies \lvert C_{G}(x) \rvert < \lvert G \rvert$$. Si $$p \Big\lvert \lvert C_{G}(x) \rvert$$, por la hipótesis inductiva, existe $$g \in C_{G}(x) \subseteq G$$ tal que $$\lvert g \rvert=p$$, de donde concluimos el resultado. Si $$p \not\Big\lvert \lvert C_{G}(x) \rvert$$, tenemos que

$$
[G:C_{G}(x)] = \frac{\lvert G \rvert }{\lvert C_{G}(x) \rvert } \implies [G:C_{G}(x)] \cdot \lvert C_{G}(x) \rvert = \lvert G \rvert \implies p \mid [G:C_{G}(x)].
$$

Sean $$x_{1},\dots,x_{k}$$ las clases de conjugación diferentes que se obtienen mediante la relación de ser conjugación y que no estén en $$Z(G)$$. Entonces,

$$
G = Z(G) \dot{\cup} \bigcup_{i=1}^{k} x_{i}^{G} \implies \lvert G \rvert = \lvert Z(G) \rvert + \sum_{i=1}^{k} \lvert x_{i}^{G} \rvert \implies \lvert G \rvert - \sum_{i=1}^{k} \lvert x_{i}^{G} \rvert = \lvert Z(G) \rvert,
$$

de donde concluimos que $$p \Big\lvert \lvert Z(G) \rvert$$. Así, $$Z(G)$$ es subgrupo propio de $$G$$, y concluimos el resultado al aplicar la hipótesis inductiva sobre $$Z(G)$$.

### Nota (La hipótesis de primalidad es necesaria)

El teorema es falso si $$p$$ no es primo. Note que $$8 \mid 120 \implies 8 \Big\lvert \lvert S_{5} \rvert$$. Pero hemos visto que no hay subgrupos de orden 8 en $$S_{5}$$.

### Definición ($$p$$-grupo)

Sea $$p$$ primo. Un grupo $$G$$ es un $$p$$-grupo si existe $$k \in \mathbb{N}$$ tal que $$\lvert G \rvert=p^{k}$$.

### Ejercicio (Centro de un $$p$$-grupo)

Si $$G$$ es un $$p$$-grupo, $$Z(G) \neq \{ 1_{G} \}$$.

### Corolario (Grupos de orden $$p^{2}$$)

Si $$p$$ es primo y $$\lvert G \rvert = p^{2}$$, entonces $$G$$ es abeliano.

***Prueba:*** Suponga que $$G$$ no es abeliano. Entonces $$Z(G)$$ es un subgrupo propio de $$G$$. Por Lagrange, $$\lvert Z(G) \rvert \in \{ 1,p \}$$. Por el ejercicio anterior, $$\lvert Z(G) \rvert = p$$. Sabemos que $$Z(G) \triangleleft G$$. Así, $$\lvert G / Z(G) \rvert = \frac{\lvert G \rvert}{\lvert Z(G) \rvert} = p$$, de donde concluimos que $$G / Z(G)$$ es cíclico y por tanto $$G$$ es abeliano.

### Teorema (Subgrupos de un grupo abeliano finito)

Sea $$G$$ un grupo abeliano finito. Entonces $$G$$ tiene un subgrupo de orden $$d$$ para todo $$d$$ tal que $$d \Big\lvert \lvert G \rvert$$.

***Prueba:*** Sea $$n = \lvert G \rvert$$. Proceda por inducción fuerte sobre $$d$$, con $$d \mid n$$. El caso base es trivial, pues si $$H = \{ 1_{G} \}\implies \lvert H \rvert=1$$. Sea $$d>1$$. Suponga como hipótesis inductiva que para todo $$e < d$$ y para todo $$\tilde{G}$$ grupo con $$e \Big\lvert \lvert \tilde{G} \rvert$$ existe $$\tilde{H} < \tilde{G}$$ tal que $$\lvert \tilde{H} \rvert = e$$. Como $$d \mid n$$, existe $$k \in \mathbb{N}$$ tal que $$kd=n$$. Como $$d>1$$, existe $$p$$ primo tal que $$p \mid d$$, i.e., existe $$\ell \in \mathbb{N}$$ tal que $$\ell p = d$$. Por Teorema de Cauchy, existe $$g \in G$$ tal que $$\lvert g \rvert=p$$. Sea $$H = \langle g \rangle$$. Note que $$H$$ es cíclico, y por tanto abeliano y normal. Luego, $$G / H$$ es grupo. Así,

$$
\lvert G / H \rvert = \frac{\lvert G \rvert }{\lvert H \rvert } = \frac{n}{p} = \frac{kd}{p} = \frac{k \ell p}{p} = k \ell.
$$

Así, $$\ell \Big\lvert \lvert G / H \rvert$$ y $$\lvert G/H \rvert < n$$. Como $$\ell < d$$, por la hipótesis inductiva, existe $$S^{\ast} < G / H$$ tal que $$\lvert S^{\ast} \rvert = \ell$$. Por teorema de correspondencia, existe $$S < G$$ tal que $$H \leq S \leq G$$ y $$S^{\ast} = S/H$$. Concluimos notando que

$$
\ell = \lvert S^{\ast} \rvert = \frac{\lvert S \rvert}{\lvert H \rvert } = \frac{\lvert S \rvert}{p} \implies \lvert S \rvert = \ell p =d,
$$

de donde se sigue el resultado.

### Teorema (Subgrupos de un $$p$$-grupo)

Sea $$G$$ un $$p-grupo$$ tal que $$\lvert G \rvert = p^{e}$$. Entonces para todo $$k \leq e$$, existe $$H \leq G$$ tal que $$\lvert H \rvert = p^{k}$$.

***Prueba:*** Procedemos por inducción sobre $$e$$. Para $$e=0$$, tenemos que $$G=\{ 1_{G} \}.$$ Tome $$H = G$$. Sea $$e > 0$$ y sea $$k \leq e$$. Suponga como hipótesis inductiva que el resultado es cierto para $$f<e$$. Como $$\lvert G \rvert = p^{e}$$ y $$e>0$$, entonces $$Z(G)$$ es no trivial. Considere los siguientes casos.

- Si $$G = Z(G)$$, entonces $$G$$ es abeliano. Por el teorema anterior, concluimos el resultado.
- Ahora, si $$G \neq Z(G)$$, existe $$c < e$$ tal que $$\lvert Z(G) \rvert = p^{c}$$ con $$c<e$$. Si $$k \leq c$$, entonces por hipótesis inductiva sobre $$Z(G)$$, existe $$H \triangleleft Z(G)$$ tal que $$\lvert H \rvert=p^{k}$$. Por otro lado, si $$k>c$$, sabemos que $$G / Z(G)$$ es un grupo (pues $$Z(G) \triangleleft G$$). Ahora, note que

    $$
    \lvert G / Z(G) \rvert = \frac{\lvert G \rvert }{\lvert Z(G) \rvert } = p^{e-c}.
    $$

Aplicando hipótesis inductiva sobre $$G / Z(G)$$, existe $$S^{\ast} \leq G/Z(G)$$ tal que $$\lvert S^{\ast} \rvert = p^{k-c}$$. Por teorema de correspondencia, existe $$S \leq G$$ tal que $$Z(G) \leq S \leq G$$ y $$S^{\ast} = S / Z(G)$$. Así,

$$
\lvert S^{\ast} \rvert \cdot \lvert Z(G) \rvert = \lvert S \rvert \implies p^{k-c} \cdot p^{c} = \lvert S \rvert,
$$

de donde concluimos el resultado.
{% endraw %}
