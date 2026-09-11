---
layout: chapter
course: ma0561
chapter: 8
title: "Subgrupos normales"
slug: 08-subgrupos-normales
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/08-subgrupos-normales/
---

{% raw %}
## Subgrupos normales

### Definición (Producto de conjuntos)

Sea $$G$$ un grupo y $$S,T \subseteq G$$. Defina $$ST = \{ s \ast t: s \in S, t \in T \}$$.
Note que si $$S = \{ s \}$$ y $$T\leq G$$, entonces $$sT =ST$$, una coclase de $$G$$. Note que si $$S,T,U \subseteq G$$, . Si $$\mathcal{F} = \{ A:A\subseteq G \}$$, entonces $$\cdot$$ está definida en $$\mathcal{F}$$ y es asociativa.

### Definición (Subgrupo normal)

Sea $$H \leq G$$. Decimos que $$H$$ es un subgrupo normal de $$G$$ y escribimos $$H \triangleleft G$$ si $$Hx = xH$$ para todo $$x \in G$$.

### Nota (Propiedades de subgrupos normales)

1. Si $$G$$ es abeliano, todo subgrupo es normal.
2. $$xH = Hx \iff xH x^{-1} = \{ x \ast h \ast x ^{-1}: h \in H \} = H$$.
3. Si $$H \triangleleft G$$, esto no implica que para todos $$x \in G$$ y $$h \in H$$ $$x \ast h = h \ast x$$. Lo que sí es cierto es que si $$h \in H$$, existe $$h' \in H$$ tal que $$x \ast h = h' \ast x$$.
4. Si para todo $$x \in  G$$, $$x H x ^{-1} \subseteq H$$, esto necesariamente implica la igualdad entre ambos conjuntos, y por tanto, que $$H \triangleleft G$$. Suponga que $$xHx ^{-1} \subseteq H$$ para todo $$x \in G$$. Note que, para $$x \in G$$.

    $$
    H = x ^{-1}(\underbrace{  x H x ^{-1} }_{ \in H }) x \subseteq x ^{-1} H x \subseteq H \implies x ^{-1} H x = H.
    $$
5. Para todo grupo $$G$$, $$\{ 1_{G} \} \triangleleft G$$, $$G \triangleleft G$$.

### Proposición (Subgrupos encadenados)

Sean $$K,H,G$$ grupos con $$K\leq H\leq G$$. Si $$K \triangleleft G$$, entonces $$K \triangleleft H$$.

***Prueba:*** El resultado es trivial, pues $$G \subseteq H$$.

### Teorema (Kernel es subgrupo normal)

Sea $$f:G\to G'$$ un homomorfismo de grupos. Entonces, $$\operatorname{Ker}(f) \triangleleft G$$.

***Prueba:*** Sea $$H:= \operatorname{Ker}(f)$$. Sea $$x \in G$$. Hay que mostrar que $$xHx ^{-1} \subseteq H$$. Sea $$h \in H$$. Entonces, $$f(x \ast h \ast x ^{-1}) = f(x) \ast f(h) \ast f(x ^{-1}) = 1_{G'}$$.

### Ejemplo (Subgrupo normal en $$S_3$$)

Sea $$G = S_{3} = \{ (1), \begin{pmatrix}1 & 2\end{pmatrix}, \begin{pmatrix}1 & 3\end{pmatrix}, \begin{pmatrix}2 & 3\end{pmatrix} \begin{pmatrix}1 & 2 & 3\end{pmatrix} \begin{pmatrix}3 & 2 & 1\end{pmatrix} \}$$. Considere, $$H = \langle \begin{pmatrix}1 & 2 & 3\end{pmatrix} \rangle$$. Tenemos que

y así por el resto de ciclos.
{% endraw %}
