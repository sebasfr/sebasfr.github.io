---
layout: chapter
course: ma0561
chapter: 5
title: "Cadenas y sucesiones exactas"
slug: 05-cadenas-y-sucesiones-exactas
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/05-cadenas-y-sucesiones-exactas/
---

{% raw %}
## Cadenas y sucesiones exactas

### Definición (Complejo de cadenas)

Un complejo de cadenas es un conjunto $$\mathcal{S} = (G_{i}, \phi_{i})_{i \in \mathbb{Z}}$$ en donde:

1. Para todo $$i \in \mathbb{Z}$$, $$G_{i}$$ es un grupo,
2. Para todo $$i \in \mathbb{Z}$$, $$\phi_{i}: G_{i} \to G_{i-1}$$ es un homomorfismo de grupos.
3. $$\phi_i \circ \phi_{i+1}: G_{i+1} \to G_{i-1}$$ es tal que $$(\phi_{i} \circ \phi_{i+1})(x) = 1_{G_{i-1}}$$ para todo $$x \in G_{i+1}$$.

$$
\cdots \to G_{3} \overset{\phi_{3}}{\to} G_{2} \overset{\phi_{2}}{\to} G_{1} \overset{\phi_{1}}{\to} G_{0} \overset{\phi_{-1}}{\to} G_{-1} \overset{\phi_{-2}}{\to} \cdots
$$

Note que $$(\phi_{i} \circ \phi_{i+1})(x) = \phi_{i} \big(\phi_{i+1}(x)\big)= 1_{G_{i-1}}$$, luego $$\phi_{i+1}(x) \in \operatorname{Ker}(\phi_{i})$$ para todo $$i \in \mathbb{N}$$. Sea $$Z_{n}(\mathcal{S}) = \operatorname{Ker}(\phi_{n}) \subseteq G_{n}$$. $$B_{n}(\mathcal{S})=\operatorname{Im}(\phi_{n+1}) \subseteq G_{n}$$. Note que

$$
B_{n}(\mathcal{S}) \leq  Z_{n}(\mathcal{S}) \leq  G_{n}
$$

### Definición (Sucesión exacta)

Tome $$\mathcal{S} = (G_{i}, \phi_{i})_{i \in \mathbb{Z}}$$ un complejo de cadenas. Si tenemos que para todo $$i$$ tenemos que $$\operatorname{Im}(\phi_{i+1}) = \operatorname{Ker}(\phi_{i})$$. Decimos que $$\mathcal{S}$$ es una sucesión exacta.

### Definición (Sucesión corta)

Una sucesión es corta si es finita.

### Ejemplo (Sucesión exacta corta)

Considere

$$
0 \rightarrow G_{2} \overset{ f }{\rightarrow} G_{1} \overset{ g }{\rightarrow} G_{0} \rightarrow 0,
$$

donde $$0$$ denota el grupo trivial. Los homomorfismos sin nombre son los triviales.

### Teorema (Exactitud de la sucesión e inyectividad/sobreyectividad)

Sea $$\phi_{0}:G_{0}\to G_{1}$$ homomorfismo:

1. Si $$0 \overset{ f }{\rightarrow} G_{0} \overset{ \phi_{0} }{\rightarrow} G_{1}$$ es exacta, entonces $$\phi_{0}$$ es inyectiva.
2. Si $$G_{0} \overset{ \phi_{0} }{\rightarrow} G_{1} \overset{ f }{\rightarrow} 0$$ es exacta, entonces $$\phi_{0}$$ es sobreyectiva.
3. Si $$0 \overset{  f }{\rightarrow} G_{0} \overset{ \phi_{0} }{\rightarrow} G_{1} \overset{ g }{\rightarrow} 0$$, entonces $$\phi_{0}$$ es un isomorfismo.

***Prueba:*** Para (1), note que $$\operatorname{Ker}(\phi_{0}) = \operatorname{Im}(f) = \{ 1_{G_{0}} \}$$, por lo que $$\phi_{0}$$ es inyectiva. Para (2), note que $$\operatorname{Im}(\phi_{0}) = \operatorname{Ker} f = G_{1}$$. Combinamos ambos resultados para (3).

### Ejemplo (Sucesión exacta $$\mathbb{Z} \to \mathbb{Z}_2$$)

Considere

$$
0 \rightarrow 2\mathbb{Z} \overset{ i }{\rightarrow}  \mathbb{Z} \overset{ \pi }{\rightarrow} \mathbb{Z}_{2} \rightarrow 0,
$$

donde $$i(x) = x$$ y $$\pi(x) = [x]$$ para todo $$x \in \mathbb{Z}$$. Basta mostrar que $$\operatorname{Im}(i) = \operatorname{Ker}(\pi)$$.
{% endraw %}
