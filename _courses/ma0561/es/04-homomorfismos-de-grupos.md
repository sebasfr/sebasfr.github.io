---
layout: chapter
course: ma0561
chapter: 4
title: "Homomorfismos de grupos"
slug: 04-homomorfismos-de-grupos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/04-homomorfismos-de-grupos/
---

{% raw %}
## Definiciones elementales

### Definición (Homomorfismo de grupos)

Sean $$(G,\ast_{G}), (H,\ast_{H})$$ grupos. Un homomorfismo de grupos entre $$G$$ y $$H$$ es una función $$f:G\to H$$ tal que

$$
\forall a,b, \in G  \quad \Big( f(a \ast_{G} b) = f(a) \ast_{h} f(b)\Big).
$$

### Ejemplos (Homomorfismos básicos)

1. Sea $$G$$ un grupo y $$f:G\to G$$ tal que $$f(x) = 1_{G}$$ para todo $$x \in G$$. Note que

    $$
    f(x \ast y) = 1_{G} = 1_{G} \ast 1_{G} = f(x) \ast f(g)
    $$
2. Considere $$f:(\mathbb{R},+) \to (\mathbb{R}^{\ast}, \cdot)$$ tal que $$f(x) = e^{x}$$. Note que

    $$
    f(x+y) = e^{x+y} = e^{x}
     \cdot e^{y} = f(x) \cdot f(y).
    $$

### Proposición (Propiedades de los homomorfismos)

Sean $$(G,\ast_{G}), (H,\ast_{H})$$ grupos y $$f:G\to H$$ un homomorfismo. Entonces:

1. $$f(1_{G}) = 1_{H}$$,
2. $$\forall g \in G  \quad \Big( f(g^{-1}) = \big(f(g)\big)^{-1}\Big)$$,
3. $$\forall n \in \mathbb{Z} \quad \Big(f(g^{n}) = \big(f(g)\big)^{n}\Big)$$
4. Si $$g \in G$$ y $$\lvert g \rvert = n$$, entonces $$\lvert f(g) \rvert \Big\lvert n$$.

***Prueba:*** Para (1), note que

$$
f(1_{G}) = f(1_{G} \ast_{G} 1_{G}) = f(1_{G}) \ast_{H} f(1_{G}),
$$

de donde concluimos que $$f(1_{G}) = 1_{H}$$.
Para (2), note que

$$
g \ast_{G} g^{-1} = 1_{G} \implies f(g) \ast_{H} f(g^{-1}) = 1_{H} \implies f(g^{-1}) = \big(f(g)\big)^{-1}.
$$

Para (3), en el caso $$n\geq 0$$, procedemos por inducción. El caso base $$n=0$$ se probó en (1). Suponga como hipótesis inductiva que $$f(g^{n})=\big(f(g)\big)^{n}$$ para algún $$n \in \mathbb{N}$$. Note que

$$
\begin{aligned}
f(g^{n+1}) = f(g^{n} \ast_{G} g) &=f(g^{n}) \ast_{H} f(g)\\
&=\big(f(g)\big)^{n} \ast_{H} f(g) \\
&= \big(f(g)\big)^{n+1}.
\end{aligned}
$$

Ahora, para $$n<0$$, note que $$-n > 0$$. Así, $$g^{n} = (g^{-n})^{-1}$$. Así,

$$
f(g^{n}) = f\big((g^{-n})^{-1}\big) = \big(f(g^{-n})\big)^{-1} = \Big(\big(f(g)\big)^{-n}\Big)^{-1} = \big(f(g)\big)^{n}.
$$

Finalmente, para (4), como $$\lvert g \rvert = n$$,

$$
g^{n} = 1_{G} \implies f(g^{n}) = \big(f(g)\big)^{n} = 1_{H},
$$

de donde deducimos que $$\lvert f(g) \rvert \Big\lvert n$$.

### Ejemplo (Proyección y homomorfismos a $$\mathbb{Z}$$)

1. Considere $$f:(\mathbb{Z}, +)\to(\mathbb{Z}_{n}, +)$$ tal que $$x \mapsto [x]$$. Note que

    $$
    f(x+y) = [x+y] = [x] + [y] = f(x) + f(y),
    $$

de donde concluimos que $$f$$ es un homomorfismo.

1. ¿Existe un homomorfismo no trivial $$f:\mathbb{Z}_{n} \to \mathbb{Z}$$? Si existiera, note que $$\lvert [1] \rvert = n$$ y entonces $$\lvert f[1] \rvert \Big\lvert n$$, una contradicción, pues el orden de los elementos en $$\mathbb{Z}$$ es infinito (salvo el cero).

### Proposición (Composición de homomorfismos)

Sean $$G,H,K$$ grupos y $$f:G\to H$$, $$g:H\to K$$ homomorfismos. Entonces $$g \circ f:G \to K$$ es un homomorfismo.

***Prueba:*** Ejercicio

### Definición (Kernel e Imagen de un homomorfismo)

Sean $$G,H$$ grupos y $$f:G\to H$$ homomorfismo. Defina

$$
\begin{aligned}
\operatorname{Ker}(f) &= \{ x \in G: f(x) = 1_{H} \} \subseteq G \\
\operatorname{Im}(f) &= \{ f(x):x \in G \} \subseteq H.
\end{aligned}
$$

### Teorema (Kernel e Imagen son subgrupos)

Sean $$G,H$$ grupos y $$f:G\to H$$ homomorfismo. Entonces,

1. $$\operatorname{Ker}(f) \leq G$$
2. $$\operatorname{Im}(f) \leq H$$

***Prueba:*** Para (1), note que $$1_{G} \in \operatorname{Ker}(f)$$, por lo que $$\operatorname{Ker}(f) \neq \emptyset$$. Sean $$x,y \in \operatorname{Ker}(f)$$.

$$
f(x \ast_{G} y^{-1}) = f(x) \ast_{H} f(y^{-1}) =1_{H} \implies x \ast_{G} y \in \operatorname{Ker}(f).
$$

Para (2), note que $$f(1_{G}) = 1_{H} \in \operatorname{Im}(f)$$, por lo que $$\operatorname{Im}(f) \neq \emptyset$$. Sean $$a,b \in \operatorname{Im}(f)$$. Luego, existen $$x,y \in G$$ tales que $$f(x) = a$$ y $$f(y) = b$$. Por propiedades de homomorfismos, $$b^{-1} = f(y^{-1})$$. Así,

$$
f(x \ast_{G} y^{-1}) = f(x) \ast_{H} \big(f(y)\big)^{-1} = a \ast_{H} b^{-1} \in \operatorname{Im}(f).
$$

### Ejemplo (Proyección $$\mathbb{Z} \to \mathbb{Z}_n$$)

Sea $$\pi:\mathbb{Z} \to \mathbb{Z}_{n}$$ tal que $$x \mapsto [x]$$. Tenemos que

$$
\begin{aligned}
\operatorname{Im}(\pi) &= \{ \pi(x):x \in \mathbb{Z} \} \\
&=\{ [x]: x \in \mathbb{Z} \} \\
&=\mathbb{Z}_{n},\\
\operatorname{Ker}(\pi) &=\{ x:\pi(x) = [0] \} \\
&=\{ x: [x] = 0 \} \\
&=n \cdot \mathbb{Z}.
\end{aligned}
$$

### Definición (Monomorfismos, epimorfismos e isomorfismos)

Sea $$f:G\to H$$ un homomorfismo de grupos:

1. si $$f$$ es inyectivo, decimos que $$f$$ es un monomorfismo,
2. si $$f$$ es sobreyectivo, decimos que $$f$$ es un epimorfismo,
3. si $$f$$ es biyectivo, decimos que $$f$$ es un isomorfismo.

### Teorema (Existencia del isomorfismo inverso)

Si $$f:G\to H$$ es un isomorfismo, entonces $$f^{-1}:H\to G$$ (como función) es un isomorfismo.

***Prueba:*** Ejercicio.

### Teorema (Monomorfismos y kernel)

Sea $$f:G\to H$$ homomorfismo. Entonces,

$$
f \text{ es monomorfismo} \iff \operatorname{Ker}(f) = \{ 1_{G} \}
$$

***Prueba:*** ejercicio. Notar que $$f(x)=f(y) \implies f(x \ast y^{-1}) = 1_{H}$$.

### Teorema (Imagen inversa y homomorfismos)

Sea $$f:G\to H$$ un homomorfismo y sea $$H'\leq H$$. Entonces $$f^{-1}(H') \leq G$$

***Prueba:*** Note que $$1_{G} \in f^{-1}(H')$$ pues $$f(1_{G}) = 1_{H} \in H \implies f^{-1}(H') \neq \emptyset$$. Sean $$x,y \in f^{-1}(H')$$. Hay que mostrar que $$x \ast_{G} y^{-1} \in f^{-1}(H')$$. Como $$f(x) \in H', f(y) \in H'$$, entonces $$\big(f(y)\big)^{-1} = f(y^{-1}) \in H'$$. Entonces $$f(x \ast_{G} y^{-1}) = f(x)\ast_{H} f(y^{-1}) \in H'$$.

### Definición (Automorfismo y grupo de automorfismos)

Sea $$G$$ un grupo. Un automorfismo de $$G$$ es un isomorfismo de $$G$$ en $$G$$. Defina $$\mathrm{Aut} \hspace{2pt}(G) = \{ f:G\to G \text{ isomorfismo}\}$$ como el conjuto de automorfismos de $$G$$.
Note que $$\mathrm{Aut} \hspace{2pt}(G) \subseteq S_{G} = \{ \phi: G\to G \text{ biyectiva}\}$$.

### Teorema (Subgrupo de automorfismos)

$$\mathrm{Aut} \hspace{2pt}(G) \leq S_{g}$$.

***Prueba:*** Ejercicio

### Definición (Grupos isomorfos)

Decimos que dos grupos $$G$$ y $$H$$ son isomorfos si existe un isomorfismo $$f:G\to H$$. Escribimos $$G \cong H$$.

### Ejemplo (Isomorfismo $$\mathbb{Z}_4 \cong G$$)

Considere $$G = (\{ 1,i,-1,-i \}, \ast)$$.

$$Z_{4} \cong G$$ bajo el isomorfismo

$$
\begin{aligned}
0  &\mapsto 1 \\
1 &\mapsto i \\
2 &\mapsto -1 \\
3 &\mapsto -i
\end{aligned}
$$

### Nota (Ser isomorfo es relación de equivalencia)

Note que la relación $$G \cong H$$ es reflexiva, transitiva y simétrica (es fácil probarlo). Luego es una relación de equivalencia.

### Teorema (Isomorfismos de grupos cíclicos)

Si $$G = \langle g \rangle$$, entonces:

1. Si $$\lvert g \rvert = \infty \implies G \cong \mathbb{Z}$$.
2. Si $$\lvert g \rvert = n \implies G \cong \mathbb{Z}_{n}$$.
{% endraw %}
