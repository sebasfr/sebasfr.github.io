---
layout: chapter
course: ma0505
chapter: 18
title: "Propiedades de la integral de funciones no negativas"
slug: 18-propiedades-de-la-integral-de-funciones-no-negativas
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/18-propiedades-de-la-integral-de-funciones-no-negativas/
---

{% raw %}
## Funciones con valores infinitos

### Definición (Integral de una función medible con valores en $$[0,\infty]$$)

Sea $$f : E \to [0,\infty]$$ medible con $$E$$ medible y $$f \geq 0$$. Tome

$$
E_{1} = \{ x \in E :\ f(x) = \infty \}.
$$

Definimos

$$
\begin{aligned}
R(f,E) &= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E,\ 0 \leq y \leq f(x) \} \\
&= \{ (x,y) \in \mathbb{R}^{d+1} :\ x \in E \setminus E_{1},\ 0 \leq y \leq f(x) \} \cup \big( E_{1} \times [0,\infty) \big),
\end{aligned}
$$

y

$$
\Gamma(f,E) = \{ (x,f(x)) \in \mathbb{R}^{d+1} :\ x \in E \setminus E_{1} \}.
$$

Al igual que se hizo para funciones de valores reales, definimos

$$
\int_{E} f \, dx = m\big( R(f,E) \big).
$$

### Nota (La región sigue siendo medible para valores infinitos)

La teoría desarrollada hasta ahora asegura que $$R(f,E)$$ es medible siempre que $$f$$ y $$E$$ sean medibles: la primera parte de la descomposición es la región bajo la restricción de $$f$$ al medible $$E \setminus E_{1}$$, y

$$
E_{1} \times [0,\infty) = \bigcup_{n=1}^{\infty} E_{1} \times [0,n]
$$

es una unión numerable de conjuntos medibles.

### Proposición (Una función con integral finita es finita c.p.d.)

Sea $$f : E \to [0,\infty]$$ medible tal que

$$
\int_{E} f(x) \, dx < \infty.
$$

Entonces $$m(\{ x \in E : f(x) = \infty \}) = 0$$, es decir, $$f$$ es finita casi por doquier.

***Prueba:*** Sea $$E_{1} = \{ f = \infty \}$$ y, para cada $$n \in \mathbb{N}$$, tome

$$
g(x) = n \mathbf{1}_{E_{1}}(x).
$$

Entonces $$g(x) \leq f(x)$$ para $$x \in E$$, pues en $$E_{1}$$ se tiene $$f = \infty \geq n$$ y fuera de $$E_{1}$$ se tiene $$g = 0 \leq f$$. Luego, por la fórmula para funciones simples y la monotonía de la integral,

$$
n\, m(E_{1}) = \int_{E} g(x)\, dx \leq \int_{E} f(x) \, dx < \infty
$$

para todo $$n \in \mathbb{N}$$, y por lo tanto $$m(E_{1}) = 0$$.

## Descomposición del dominio y el teorema de convergencia monótona

### Proposición (Aditividad de la integral respecto al dominio)

Sea $$f : E \to [0,\infty]$$ medible. En el caso de que $$E = \bigcup_{i=1}^{\infty} E_{i}$$ con los $$E_{i}$$ medibles y $$E_{i} \cap E_{j} = \emptyset$$ si $$i \neq j$$, tenemos que

$$
\int_{E} f(x) \, dx = \sum_{k=1}^{\infty} \int_{E_{k}} f(x) \, dx.
$$

Esta fórmula es válida también para uniones finitas.

***Prueba:*** Como los $$E_{i}$$ son disjuntos dos a dos, tenemos que

$$
R(f,E) = \bigcup_{k=1}^{\infty} R(f,E_{k}),
$$

y los $$R(f,E_{k})$$ son disjuntos dos a dos, pues sus primeras coordenadas viven en conjuntos disjuntos. De esta manera, por aditividad numerable de la medida,

$$
\int_{E} f(x) \, dx = m(R(f,E)) = m\left( \bigcup_{k=1}^{\infty} R(f,E_{k}) \right) = \sum_{k=1}^{\infty} m(R(f,E_{k})) = \sum_{k=1}^{\infty} \int_{E_{k}} f(x) \, dx.
$$

La fórmula para uniones finitas se obtiene tomando $$E_{k} = \emptyset$$ para los índices restantes, pues $$R(f,\emptyset) = \emptyset$$.

### Teorema (Convergencia monótona para funciones no negativas)

Sea $$\{f_{k}\}_{k=1}^{\infty}$$ una sucesión de funciones medibles tales que

$$
0 \leq f_{k}(x) \leq f_{k+1}(x)
$$

para todo $$x \in E$$. Si

$$
\lim_{k \to \infty} f_{k}(x) = f(x)
$$

casi por doquier en $$E$$, entonces

$$
\lim_{k \to \infty} \int_{E} f_{k}(x) \, dx = \int_{E} f(x) \, dx.
$$

***Prueba:*** Sea $$Z \subseteq E$$ el conjunto nulo donde falla la convergencia, y $$\tilde{E} = E \setminus Z$$. Para cualquier función medible no negativa $$g$$ se tiene $$R(g,Z) \subseteq Z \times [0,\infty) = \bigcup_{n} Z \times [0,n]$$, que tiene medida cero; entonces $$\int_{Z} g \, dx = 0$$ y, por la aditividad del dominio, las integrales sobre $$E$$ y sobre $$\tilde{E}$$ coinciden tanto para $$f$$ como para cada $$f_{k}$$. Podemos entonces suponer que $$f_{k}(x) \to f(x)$$ para todo $$x \in E$$.

Con el mismo argumento de aproximación usado para la región bajo el gráfico, tenemos que

$$
R(f,E) = \Gamma(f,E) \cup \bigcup_{k=1}^{\infty} R(f_{k},E):
$$

si $$0 \leq y < f(x)$$, como $$f_{k}(x) \uparrow f(x)$$, existe $$k$$ con $$y \leq f_{k}(x)$$, es decir $$(x,y) \in R(f_{k},E)$$; si $$y = f(x) < \infty$$, entonces $$(x,y) \in \Gamma(f,E)$$; y cada $$R(f_{k},E) \subseteq R(f,E)$$ porque $$f_{k} \leq f$$. Como

$$
R(f_{k},E) \subseteq R(f_{k+1},E)
$$

por la monotonía de la sucesión, y $$m(\Gamma(f,E)) = 0$$, la continuidad desde abajo de la medida nos da

$$
\int_{E} f(x) \, dx = m(R(f,E)) = m\left( \bigcup_{k=1}^{\infty} R(f_{k},E) \right) = \lim_{k \to \infty} m(R(f_{k},E)) = \lim_{k \to \infty} \int_{E} f_{k}(x) \, dx.
$$

## Una fórmula útil

### Notación (Suma inferior asociada a una partición finita del dominio)

Dada $$f : E \to [0,\infty]$$ medible y una partición finita $$E = \bigcup_{i=1}^{N} E_{i}$$ en medibles disjuntos dos a dos, definimos

$$
\sum\big(f, \{E_{i}\}_{i=1}^{N}\big) = \sum_{i=1}^{N} \Big( \inf_{E_{i}} f \Big) \mathbf{1}_{E_{i}} \leq f.
$$

### Teorema (La integral como supremo de sumas inferiores)

Sea $$f : E \to [0,\infty]$$ medible, no negativa. Entonces

$$
\int_{E} f(x) \, dx = \sup \left\{ \int_{E} \sum\big(f, \{E_{i}\}_{i=1}^{N}\big) \, dx :\ E = \bigcup_{i=1}^{N} E_{i} \ \text{partición finita en medibles disjuntos} \right\}.
$$

***Prueba:*** Dados $$E_{1}, \dots, E_{N}$$ medibles disjuntos dos a dos tales que $$E = \bigcup_{i=1}^{N} E_{i}$$, tenemos que

$$
\sum\big(f, \{E_{i}\}_{i=1}^{N}\big) \leq f,
$$

entonces, por monotonía y la fórmula para funciones simples,

$$
\sum_{i=1}^{N} \Big( \inf_{E_{i}} f \Big) m(E_{i}) = \int_{E} \sum\big(f, \{E_{i}\}_{i=1}^{N}\big) \, dx \leq \int_{E} f(x) \, dx.
$$

Es decir, el supremo del enunciado es menor o igual que la integral.

Para la desigualdad recíproca, dados $$k \geq 1$$ y $$1 \leq i \leq k 2^{k}$$, defina

$$
E_{k}^{0} = \{ f \geq k \}, \qquad E_{k}^{i} = \left\{ \frac{i-1}{2^{k}} \leq f(x) < \frac{i}{2^{k}} \right\}.
$$

Entonces

$$
E = \bigcup_{i=0}^{k 2^{k}} E_{k}^{i}
$$

es una partición finita en medibles disjuntos dos a dos. Tome

$$
f_{k}(x) = k \mathbf{1}_{E_{k}^{0}} + \sum_{i=1}^{k 2^{k}} \left( \frac{i-1}{2^{k}} \right) \mathbf{1}_{E_{k}^{i}};
$$

esta es la aproximación diádica estándar, así que sabemos que

$$
f_{k} \leq f_{k+1} \qquad \text{y} \qquad \lim_{k \to \infty} f_{k} = f
$$

puntualmente en $$E$$. Por el teorema de convergencia monótona,

$$
\int_{E} f_{k} \, dx \to \int_{E} f \, dx.
$$

Como en cada pieza de la partición el valor de $$f_{k}$$ es menor o igual que el ínfimo de $$f$$ en ella, tenemos que

$$
f_{k} \leq \sum\big(f, \{E_{k}^{i}\}_{i=0}^{k 2^{k}}\big) \leq f,
$$

e integrando,

$$
\int_{E} f_{k} \, dx \leq \sum_{i=0}^{k 2^{k}} \Big( \inf_{E_{k}^{i}} f \Big) m(E_{k}^{i}) \leq \int_{E} f(x) \, dx.
$$

El término del medio es una de las sumas inferiores del enunciado, y el lado izquierdo converge a $$\int_{E} f \, dx$$; tenemos entonces que

$$
\lim_{k \to \infty} \sum_{i=0}^{k 2^{k}} \Big( \inf_{E_{k}^{i}} f \Big) m(E_{k}^{i}) = \int_{E} f(x) \, dx,
$$

y el supremo del enunciado alcanza a la integral.

### Corolario (La integral como supremo sobre funciones simples)

Sea $$f : E \to [0,\infty]$$ medible. Entonces

$$
\int_{E} f(x) \, dx = \sup \left\{ \int_{E} \phi(x) \, dx :\ \phi\ \text{simple y medible},\ 0 \leq \phi \leq f\ \text{en } E \right\}.
$$

***Prueba:*** Ejercicio.

## Conjuntos nulos, desigualdad de Markov y funciones nulas

### Lema (La integral sobre un conjunto de medida cero es nula)

Sea $$f : E \to [0,\infty]$$ medible. Si $$m(E) = 0$$, entonces

$$
\int_{E} f(x) \, dx = 0.
$$

***Prueba:*** Sean $$f_{k} = \sum_{i=1}^{m} a_{i} \mathbf{1}_{A_{i}}$$, con $$A_{i} \cap A_{j} = \emptyset$$ si $$i \neq j$$, funciones simples no negativas crecientes hacia $$f$$, de modo que, por el teorema de convergencia monótona,

$$
\lim_{k \to \infty} \int_{E} f_{k} \, dx = \int_{E} f(x) \, dx.
$$

Note que

$$
\int_{E} f_{k}(x) \, dx = \sum_{i=1}^{m} a_{i}\, m(A_{i}).
$$

Como $$A_{i} \subseteq E$$, entonces $$m(A_{i}) = 0$$ para $$1 \leq i \leq m$$, y cada $$\int_{E} f_{k} \, dx = 0$$. Concluimos que $$\int_{E} f \, dx = 0$$.

### Teorema (La integral respeta desigualdades c.p.d.)

Sean $$f, g : E \to [0,\infty]$$ medibles tales que $$g(x) \leq f(x)$$ casi por doquier en $$E$$. Entonces vale que

$$
\int_{E} g(x) \, dx \leq \int_{E} f(x) \, dx.
$$

En particular, si $$f = g$$ c.p.d. en $$E$$, entonces

$$
\int_{E} g(x) \, dx = \int_{E} f(x) \, dx.
$$

***Prueba:*** Sea

$$
A = \{ x \in E :\ g(x) \leq f(x) \}.
$$

Entonces $$E = A \cup Z$$ con $$Z = E \setminus A$$ de medida cero y $$A \cap Z = \emptyset$$. Así, por la aditividad del dominio y el lema anterior, tenemos

$$
\int_{E} f(x) \, dx = \int_{A} f(x) \, dx + \int_{Z} f(x) \, dx = \int_{A} f(x) \, dx,
$$

$$
\int_{E} g(x) \, dx = \int_{A} g(x) \, dx + \int_{Z} g(x) \, dx = \int_{A} g(x) \, dx.
$$

Como $$g \leq f$$ puntualmente en $$A$$, la monotonía de la integral da $$\int_{A} g \, dx \leq \int_{A} f \, dx$$, y el resultado se sigue. Si además $$f = g$$ c.p.d., ambas desigualdades valen y se obtiene la igualdad.

### Proposición (Desigualdad de Markov)

Sean $$f : E \to [0,\infty]$$ medible y $$\alpha > 0$$. Entonces

$$
m(\{ f \geq \alpha \}) \leq \frac{1}{\alpha} \int_{E} f(x) \, dx.
$$

***Prueba:*** Como $$f \geq 0$$, tenemos las desigualdades puntuales

$$
\alpha \mathbf{1}_{\{f \geq \alpha\}} \leq f \mathbf{1}_{\{f \geq \alpha\}} \leq f.
$$

Integrando y usando la fórmula para funciones simples, la identidad $$\int_{E} \mathbf{1}_{E_{1}} f \, dx = \int_{E_{1}} f \, dx$$ y la monotonía,

$$
\alpha\, m(\{ f \geq \alpha \}) \leq \int_{\{f \geq \alpha\}} f(x) \, dx \leq \int_{E} f(x) \, dx,
$$

y basta dividir por $$\alpha > 0$$.

### Corolario (Una función no negativa con integral nula es nula c.p.d.)

Sea $$f : E \to [0,\infty]$$ medible tal que $$\int_{E} f(x) \, dx = 0$$. Entonces $$f = 0$$ casi por doquier.

***Prueba:*** Por la desigualdad de Markov, para todo $$\alpha > 0$$ tenemos que

$$
m(\{ f \geq \alpha \}) \leq \frac{1}{\alpha} \int_{E} f(x) \, dx = 0.
$$

Luego

$$
\{ f > 0 \} = \bigcup_{k=1}^{\infty} \left\{ f \geq \frac{1}{k} \right\}
$$

es una unión numerable de conjuntos de medida cero, y por lo tanto es un conjunto de medida cero. Es decir, $$f = 0$$ c.p.d.

## Linealidad

### Teorema (Linealidad de la integral para funciones no negativas)

Sean $$f, g : E \to [0,\infty]$$ medibles y $$c \geq 0$$. Entonces

$$
\int_{E} \big( c f(x) + g(x) \big) \, dx = c \int_{E} f(x) \, dx + \int_{E} g(x) \, dx.
$$

***Prueba:*** *Homogeneidad.* Si $$c = 0$$, con la convención $$0 \cdot \infty = 0$$ tenemos $$cf \equiv 0$$ y ambos lados de la homogeneidad son nulos. Sea entonces $$c > 0$$; vamos a probar que

$$
\int_{E} c f(x) \, dx = c \int_{E} f(x) \, dx.
$$

Sea $$\{f_{k}\}$$ una sucesión de funciones simples no negativas tales que

$$
0 \leq f_{k} \leq f_{k+1} \qquad \text{y} \qquad \lim_{k \to \infty} f_{k} = f.
$$

Si

$$
f_{k} = \sum_{i=1}^{m_{k}} a_{i} \mathbf{1}_{A_{i}},
$$

con los $$A_{i}$$ medibles y disjuntos dos a dos, tenemos que

$$
\lim_{k \to \infty} c f_{k} = \lim_{k \to \infty} \sum_{i=1}^{m_{k}} c a_{i} \mathbf{1}_{A_{i}} = c f(x), \qquad c f_{k} \leq c f_{k+1}.
$$

Entonces, aplicando el teorema de convergencia monótona dos veces y la fórmula para simples,

$$
\int_{E} c f(x) \, dx = \lim_{k \to \infty} \int_{E} c f_{k}(x) \, dx = \lim_{k \to \infty} \sum_{i=1}^{m_{k}} c a_{i}\, m(A_{i}) = c \lim_{k \to \infty} \sum_{i=1}^{m_{k}} a_{i}\, m(A_{i}) = c \int_{E} f(x) \, dx.
$$

*Aditividad.* Falta mostrar la aditividad. Para tal efecto tomemos $$g_{k}$$ una sucesión de funciones simples no negativas tales que

$$
g_{k} \leq g_{k+1}, \qquad \lim_{k \to \infty} g_{k} = g.
$$

Entonces se sigue que

$$
g_{k} + f_{k} \leq g_{k+1} + f_{k+1}, \qquad \lim_{k \to \infty} (g_{k} + f_{k}) = g + f.
$$

Vamos a mostrar primero la aditividad para las simples, es decir, que

$$
\int_{E} \big( g_{k}(x) + f_{k}(x) \big) \, dx = \int_{E} g_{k}(x) \, dx + \int_{E} f_{k}(x) \, dx.
$$

Sea

$$
g_{k} = \sum_{j=1}^{\ell_{k}} b_{j} \mathbf{1}_{B_{j}}, \quad \text{con } E = \bigcup_{j=1}^{\ell_{k}} B_{j} \text{ disjuntos dos a dos},
$$

y recordemos que

$$
f_{k} = \sum_{i=1}^{m_{k}} a_{i} \mathbf{1}_{A_{i}}, \quad \text{con } E = \bigcup_{i=1}^{m_{k}} A_{i} \text{ disjuntos dos a dos}.
$$

Note que, al ser ambas familias particiones de $$E$$,

$$
\mathbf{1}_{A_{i}} = \sum_{j=1}^{\ell_{k}} \mathbf{1}_{B_{j} \cap A_{i}}, \qquad \mathbf{1}_{B_{j}} = \sum_{i=1}^{m_{k}} \mathbf{1}_{B_{j} \cap A_{i}},
$$

entonces

$$
g_{k}(x) + f_{k}(x) = \sum_{j=1}^{\ell_{k}} \sum_{i=1}^{m_{k}} b_{j} \mathbf{1}_{A_{i} \cap B_{j}} + \sum_{i=1}^{m_{k}} \sum_{j=1}^{\ell_{k}} a_{i} \mathbf{1}_{A_{i} \cap B_{j}} = \sum_{j=1}^{\ell_{k}} \sum_{i=1}^{m_{k}} (b_{j} + a_{i}) \mathbf{1}_{A_{i} \cap B_{j}},
$$

que es una función simple sobre la partición común $$\{A_{i} \cap B_{j}\}$$. Ahora, por aditividad finita de la medida,

$$
\sum_{i=1}^{m_{k}} m(A_{i} \cap B_{j}) = m\left( B_{j} \cap \bigcup_{i=1}^{m_{k}} A_{i} \right) = m(B_{j} \cap E) = m(B_{j}),
$$

y de igual forma tenemos

$$
\sum_{j=1}^{\ell_{k}} m(A_{i} \cap B_{j}) = m(A_{i}).
$$

Finalmente,

$$
\begin{aligned}
\int_{E} \big( f_{k}(x) + g_{k}(x) \big) \, dx &= \sum_{j=1}^{\ell_{k}} \sum_{i=1}^{m_{k}} (a_{i} + b_{j})\, m(A_{i} \cap B_{j}) \\
&= \sum_{j=1}^{\ell_{k}} b_{j} \sum_{i=1}^{m_{k}} m(A_{i} \cap B_{j}) + \sum_{i=1}^{m_{k}} a_{i} \sum_{j=1}^{\ell_{k}} m(A_{i} \cap B_{j}) \\
&= \sum_{j=1}^{\ell_{k}} b_{j}\, m(B_{j}) + \sum_{i=1}^{m_{k}} a_{i}\, m(A_{i}) \\
&= \int_{E} g_{k}(x) \, dx + \int_{E} f_{k}(x) \, dx.
\end{aligned}
$$

Como $$\{f_{k} + g_{k}\}$$ es una sucesión creciente de simples que converge a $$f + g$$, el teorema de convergencia monótona aplicado tres veces nos da

$$
\int_{E} (f + g) \, dx = \lim_{k \to \infty} \int_{E} (f_{k} + g_{k}) \, dx = \lim_{k \to \infty} \left( \int_{E} f_{k} \, dx + \int_{E} g_{k} \, dx \right) = \int_{E} f \, dx + \int_{E} g \, dx.
$$

Combinando la homogeneidad con la aditividad, aplicadas a $$cf$$ y $$g$$, se concluye el enunciado.
{% endraw %}
