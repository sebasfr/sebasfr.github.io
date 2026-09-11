---
layout: chapter
course: ma0561
chapter: 6
title: "Traslación y conjugación"
slug: 06-traslacion-y-conjugacion
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/06-traslacion-y-conjugacion/
---

{% raw %}
## Traslación y conjugación

### Definición (Traslación)

Sea $$(G, \ast)$$ un grupo y sea $$a \in G$$. La traslación izquierda (dercha) de $$a$$ es $$T_{a}:G\to G$$ tal que $$x \mapsto a \ast x$$ ($$x \mapsto x \ast a$$).

### Nota (Traslación es biyectiva)

1. $$T_{a}$$ es inyectiva pues $$T_{a}(x)=T_{a}(y) \iff a \ast x = a \ast y \iff x = y$$.
2. $$T_{a}$$ es sobreyectiva, pues si $$y \in G$$, $$T_{a}(a^{-1} \ast y) = y$$.

Luego, $$T_{a}$$ es biyectiva. Concluya que $$T_{a} \in S_{G} = \{ \sigma:G\to G \text{ biyectiva}\}$$.

### Teorema (Traslaciones de $$G$$ son un monomorfismo)

Sea $$f:G\to S_{G}$$ tal que $$f(a) = T_{a}$$. Entonces $$f$$ es un monomorfismo.

***Prueba:*** Probaremos primero que $$f$$ es un homomorfismo, i.e., que $$f(a \ast b) = T_{a \ast b} = T_{a} \ast T_{b}$$. Sea $$x \in G$$. Tenemos que

$$
\begin{aligned}
(T_{a} \circ T_{b})(x) = T_{a}(T_{b}(x)) &= T_{a} (b \ast x)\\
&= a \ast (b \ast x) \\
&=(a \ast b) \ast x \\
&= T_{a \ast b} (x)
\end{aligned},
$$

de donde tenemos que $$f$$ es un homomorfismo. Probaremos que $$f$$ es inyectiva. Sea $$a \in \operatorname{Ker}(f)$$. Sea $$a \in  G$$ tal que $$f(a) = T_{a} = \mathrm{id}_{G}$$. Luego,

$$
\forall x \in G  \quad(T_{a}(x)= x) \implies \forall x \in G  \quad(a \ast x = x) \implies a = 1_{G}.
$$

Así, $$\operatorname{Ker}(f) = \{ \mathrm{id_{G}} \}$$. Concluimos que $$f$$ es un monomorfismo.

### Definición (Conjugación)

Sea $$G$$ un grupo y $$a \in G$$. Defina la conjugación por $$a$$ $$C_{a}: G\to G$$ tal que $$x \mapsto a \ast x \ast a^{-1}$$.

### Teorema (Conjugación en el automorfismo)

Sea $$G$$ un grupo y $$a \in G$$. Entonces $$C_{a} \in \mathrm{Aut}(G)$$.

***Prueba:*** Note que $$C_{a}(x \ast y) = C_{a}(x) \ast C_{a}(y)$$ (ejercicio), por lo que $$C_{a}$$ es homomorfismo. Para probar que es inyectiva, tome $$x \in \operatorname{Ker}(C_{a})$$. Luego

$$
C_{a}(x) = 1_{G} \implies a \ast x \ast a ^{-1} = 1_{G} \implies x = 1_{G}
$$

Para probar que es sobreyectiva, sea $$x \in G$$. Note que $$C_{a}(a^{-1} \ast x \ast a) = x$$, de donde concluimos sobreyectividad.

### Teorema (Conjugaciones de $$G$$ son un homomorfismo)

Sea $$f:G\to \mathrm{Aut}(G) \leq S_{G}$$ tal que $$f(a) = C_{a}$$. Entonces $$f$$ es un homomorfismo.

***Prueba:*** Sea $$x \in G$$. Entonces

$$
\begin{aligned}
(C_{a} \circ C_{b})(x) &= C_{a} (C_{b}(x))\\
&=C_{a} ( b \ast x \ast b^{-1})\\
&=a \ast ( b \ast x \ast b^{-1}) \ast a ^{-1} \\
&=(a \ast b) \ast x \ast (a \ast b) ^{-1} \\
&=C_{a \ast b}(x).
\end{aligned}
$$
{% endraw %}
