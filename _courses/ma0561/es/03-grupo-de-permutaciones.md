---
layout: chapter
course: ma0561
chapter: 3
title: "Grupo de permutaciones"
slug: 03-grupo-de-permutaciones
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/03-grupo-de-permutaciones/
---

{% raw %}
## Grupo de permutaciones

Sea $$n \in \mathbb{N}^{\ast}$$. Defina

$$
S_{n} = \{ \sigma: \sigma \text{ es permutación de }\{ 1,\dots,n \} \}.
$$

Si $$X$$ es un conjunto cualquiera, $$\sigma: X \to X$$ biyectiva es una permutación.
$$S_{X} = \{ \sigma : \quad \sigma: X \to X \text{ permutación} \}$$. Es fácil ver que si $$\lvert X \rvert = n$$, $$S_{X} \cong S_{n}$$, pues

$$
\begin{aligned}
X &= \{ x_{1},\dots,x_{n} \}\\
&\cong \{ 1,\dots,n \}
\end{aligned}.
$$

### Teorema (Orden del grupo de permutaciones)

Sea $$n \in \mathbb{N}^{\ast}$$. Entonces $$\lvert S_{n} \rvert = n!$$.

***Prueba:*** Note que

$$
\begin{aligned}
\sigma(1) &\text{ tiene } n \text{ posibilidades}\\
\sigma(2) &\text{ tiene } n-1 \text{ posibilidades} \\
& \qquad \qquad \vdots \\
\sigma(n) &\text{ tiene } 1 \text{ posibilidad}.
\end{aligned}
$$

### Definición (Mover y fijar un elemento)

Sea $$\alpha \in S_{n}$$ y sea $$k \in \{ 1, \dots, n \}$$. Decimos que:

1. "$$\alpha$$ mueve $$k$$" si $$\alpha(k) \neq k$$,
2. "$$\alpha$$ fija $$k$$" si $$\alpha(k) = k$$.

### Notación (Composición de permutaciones)

Considere $$\alpha:\{ 1,2,3\} \to \{ 1,2,3 \}$$ y $$\beta:\{ 1,2,3\} \to \{ 1,2,3 \}$$ tales que

$$
\alpha = \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 3
\end{pmatrix}, \quad
\beta = \begin{pmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{pmatrix}.
$$

Tenemos que

$$
\alpha \circ \beta = \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 3
\end{pmatrix} \circ \begin{pmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{pmatrix} = \begin{pmatrix}
1 & 2 & 3 \\
3 & 1 & 2
\end{pmatrix},
$$

$$
\beta \circ \alpha = \begin{pmatrix}
1 & 2 & 3 \\
3 & 2 & 1
\end{pmatrix} \circ \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 3
\end{pmatrix} = \begin{pmatrix}
1 & 2 & 3 \\
2 & 3 & 1
\end{pmatrix}.
$$

En general, dos permutaciones no tienen por qué conmutar.

### Definición (r-ciclo)

Sea $$n \in \mathbb{N}^\ast$$ y $$r \in \{ 1,\dots,n \}$$. Decimos que $$\alpha \in S_{n}$$ es un $$r$$-ciclo. Si existen, $$i_{1},\dots,i_{r} \in \{ 1,\dots,n \}$$ distintos tales que

$$
\begin{aligned}
\alpha(i_{1}) &= i_{2}\\
\alpha(i_{2}) &= i_{3}\\
\vdots\\
\alpha(i_{r-1}) &= i_{r}\\
\alpha(i_{r}) &= i_{1}.
\end{aligned}
$$

Escribimos, $$\begin{pmatrix}i_{1} & \cdots  & i_{r}\end{pmatrix}$$. Note que si $$\alpha = \begin{pmatrix} i_{1} & \cdots & i_{r}\end{pmatrix}$$ y $$j \not\in \{ i_{1},\dots,i_{r} \}$$, entonces $$\alpha(j) = j$$.

### Ejemplo ($$r$$-ciclo en $$S_4$$)

$$\alpha=\begin{pmatrix}1 & 2 & 3 & 4 \\ 2 & 3 & 1 & 4\end{pmatrix} = \begin{pmatrix}1 & 2 & 3\end{pmatrix} \in S_{4}$$.

### Definición (Permutaciones disjuntas)

Sean $$\alpha,\beta \in S_{n}$$/ Decimos que $$\alpha$$ y $$\beta$$ son disjuntas si todo elemento que es movido por $$\alpha$$ es fijado por $$\beta$$ y todo elemento que mueve $$\beta$$ es fijado por $$\alpha$$. Note que esta definición admite que haya elementos fijados por ambas,

### Definición (Transposición)

Decimos que un $$2$$-ciclo es una transposición.

### Nota (Notación cíclica)

$$
\begin{pmatrix}
1 & 3 & 5
\end{pmatrix} = \begin{pmatrix}
5 & 1 & 3
\end{pmatrix} = \begin{pmatrix}
3 & 5 & 1
\end{pmatrix}
$$

son el mismo ciclo.

### Ejercicio ($$r$$-ciclo y orden)

Muestre que $$\alpha \in S_{n}$$ es un $$r$$-ciclo si y solo si $$\lvert a \rvert = r$$ (i.e., $$\alpha^{r} = \mathrm{id}_{n}$$).

### Nota (Inverso de un ciclo)

Si $$\alpha = \begin{pmatrix}1 & 3 & 5\end{pmatrix} \in S_{5}$$, $$\alpha ^{-1} = \begin{pmatrix}5 & 3 & 1\end{pmatrix}$$.

### Ejemplo (Producto de transposiciones disjuntas)

Considere $$\alpha \in S_{4}$$ con

$$
\alpha = \begin{pmatrix}
1 & 2 & 3 & 4 \\
2 & 1 & 4 & 3
\end{pmatrix} = \underbrace{ \begin{pmatrix}
1 & 2
\end{pmatrix} }_{ \beta_{1} } \underbrace{ \begin{pmatrix}
3 & 4
\end{pmatrix} }_{ \beta_{2} },
$$

donde $$\beta_{1}, \beta_{2} \in S_{1}$$ son $$2$$-ciclos disjuntos.

### Teorema (Conmutatividad de permutaciones disjuntas)

Sean $$\alpha, \beta \in S_{n}$$ disjuntas. Entonces $$\alpha \circ \beta = \beta \circ \alpha$$.

***Prueba:*** Sea $$i \in \{ 1,\dots, n \}$$. Tenemos tres casos posibles.
**Caso 1:** $$\alpha$$ mueve $$i$$. Sea $$j = \alpha(i) \neq i$$. Entonces, $$\beta(i) = i$$. Note además que $$\alpha(j) \neq j$$, pues de lo contrario, $$\alpha(i) = j = \alpha(j)$$ implica por inyectividad de $$\alpha$$ que $$i = j$$, una contradicción. Por tanto, $$\beta(j) = j$$. Así, tenemos que

$$
\begin{aligned}
(\alpha \circ \beta)(i) &= \alpha(\beta(i)) = \alpha(i) = j \\
(\beta \circ \alpha)(i) &= \beta(\alpha(i)) = \beta(j) = j.
\end{aligned}
$$

**Caso 2:** $$\beta$$ mueve $$i$$. Este caso es análogo al anterior.
**Caso 3:** $$\alpha, \beta$$ fijan a $$i$$: Note que $$\alpha(i) = \beta(i) = i$$. Luego

$$
\begin{aligned}
(\alpha \circ \beta)(i) &= \alpha(\beta(i)) = \alpha(i) = i \\
(\beta \circ \alpha)(i) &= \beta(\alpha(i)) = \beta(j) = i.
\end{aligned}
$$

Concluya que permutaciones disjuntas conmutan.

### Teorema (Orbita finita)

Sea $$\alpha \in S_{n}$$, $$i \in \{ 1,\dots,n \}$$ tal que $$\alpha(i) \neq i$$. Defina la sucesión $$\{ i_{k} \}_{k \in \mathbb{N}^{\ast}}$$ de manera que $$i_{1} = i$$, $$i_{2} = \alpha(i_{1}) = \alpha(i), \dots,i_{k+1} = \alpha (i_{k})$$ para todo $$k \in \mathbb{N}^{\ast}$$. Entonces:

1. existe $$k \in \{ 1,\dots,n \}$$ tal que $$i_{k+1} \in \{ i_{1},\dots, i_{k} \}$$;
2. si $$r = \min \{ k \in \mathbb{N}^{\ast} : i_{k+1} \in \{ i_{1},\dots,i_{k} \} \} \implies i_{r+1} = i_{1}.$$

***Prueba:*** Para (1), note que para todo $$k \in \mathbb{N}^{\ast}$$, $$\{ i_{1},\dots,i_{k} \} \subseteq \{ 1,\dots,n \}$$ y $$\{ 1,\dots,n \}$$ es finito, entonces el resultado se sigue directamente.
Para (2), defina $$r$$ como en el enunciado. Tome $$i_{j}:= i_{r+1} \in \{ i_{1},\dots,i_{r} \}$$. Suponga por contradicción que $$j>1 \implies j-1>0$$. Note que $$\alpha^{j-1}(i) = i_{j} = i_{r+1} = \alpha^{r}(i)$$. Aplicando $$\alpha ^{-1}$$ $$j-1$$ veces, tenemos que

$$
i_{1} = i = \alpha^{r+1-j}(i),
$$

pero $$r+1-j < r$$, por lo que esto contradice la minimalidad de $$r$$. Por tanto $$j = 1$$.

### Lema (Igualdad de ciclos)

Sean $$\alpha, \beta \in S_{n}$$ y sea $$i \in \{ 1,\dots,n \}$$. Si $$\alpha, \beta$$ mueven $$i$$ y para todo $$k \in \mathbb{N}$$, $$\alpha^{k}(i) = \beta^{k}(i)$$, entonces $$\alpha = \beta$$.

***Prueba:*** ejercicio.

### Teorema (Factorización en ciclos disjuntos)

Toda permutación en $$S_{n}$$ es producto de ciclos disjuntos. Además, si agregamos los $$1$$-ciclos la descomposición es única módulo el orden.

***Prueba:*** Sea $$\alpha \in S_{n}$$. Proceda por inducción fuerte sobre el número $$k$$ de elementos que mueve $$\alpha$$. Si $$k=0$$, entonces $$\alpha = \mathrm{id}_{n}$$. Entonces, $$\alpha = (1)(2) \cdots (n)$$.
Considere ahora el caso de $$k>0$$. Suponga que el teorema es cierto para $$\{0,1,\dots,k-1\}$$. Sea $$i \in \{ 1,\dots,n \}$$ tal que $$\alpha(i) \neq i$$. Defina $$i_{k} \in \{ 1,\dots,n \}$$ tal que $$i_{1} = i$$ y $$i_{m+1} = \alpha(i_{m}) = \alpha^{m}(i)$$ para $$m \in \mathbb{N}^{\ast}$$. Sea $$r = \min \{ \ell \in \mathbb{N}: i_{\ell+1} \in \{ i_{1},\dots,i_{\ell} \} \} \leq n$$. Por teorema anterior, $$i_{r+1}=i_{1}$$. Sea $$\delta = \begin{pmatrix}i_{1} & \cdots  & i_{r}\end{pmatrix} \in S_{n}$$ un $$r$$=ciclo.
Si $$r = n$$ , $$\delta$$ es un $$n$$-ciclo y $$\delta = \alpha$$. Si $$r<n$$, defina $$A := \{ 1,\dots,n \} \setminus \{ i_{1},\dots,i_{r} \}$$. Note que $$\alpha(A) = A$$, pues todos estos puntos son fijados por $$\alpha$$. Además, $$\delta$$ fija todos los elementos de $$A$$ por construcción. Sea $$\beta \in S_{n}$$ tal que para todo $$x \in A$$, $$\beta(x) = \alpha(x)$$ y para todo $$x \in \{ i_{1},\dots,i_{r} \}$$, $$\beta(x) = x$$. Note que $$\beta$$ y $$\delta$$ son disjuntas. Además, $$\alpha = \beta \circ \delta$$. El número de elementos que $$\beta$$ mueve es menor que $$k$$. Luego, por hipótesis inductiva aplicada a $$\beta$$, $$\beta$$ es producto de ciclos disjuntos, y por tanto $$\alpha = \beta \circ \delta$$ también lo es.

### Proposición (Descomposición en transposiciones)

Sea $$n\geq 2$$. Todo $$\alpha \in S_{n}$$ es producto de transposiciones.

***Prueba:*** Basta mostrarlo si $$\alpha$$ es un ciclo. Sea $$\alpha = \begin{pmatrix}a_{1} & \cdots & a_{n}\end{pmatrix}$$ un ciclo. Proceda por inducción fuerte sobre $$r$$. Para $$r=1$$, note que $$\alpha = (a)$$. Luego, $$\alpha$$ es la identidad de $$S_n$$. Sea $$b \in \{ 1,\dots,n \}$$ tal que $$b\neq a$$ (sabemos que existe porque $$n>2$$). Luego, $$\alpha = \begin{pmatrix} a & b\end{pmatrix} \begin{pmatrix}a & b\end{pmatrix} = \mathrm{id}_{S_{n}}$$. Suponga como hipótesis inductiva que el teorema es cierto para cada $$k$$-ciclo con $$k \leq r-1$$.
Probaremos que $$\alpha = \begin{pmatrix}a_{1} & a_{3} & \cdots  & a_{r-1}\end{pmatrix} \begin{pmatrix}a_{1} & a_{2}\end{pmatrix}$$. Sea $$\beta = \begin{pmatrix}a_{1} & a_{3} & \cdots  & a_{r}\end{pmatrix} \begin{pmatrix}a_{1} & a_{2}\end{pmatrix}$$. Note que

$$
\begin{aligned}
\beta(a_{r}) = a_{1} &= \alpha(a_{r}) \\
\beta(a_{1}) = a_{2} &=\alpha(a_{1})\\
\beta(a_{2}) = a_{3} &= \alpha(a_{2})\\
\beta(a_{k}) = a_{k+1} &= \alpha(a_{k}), \qquad 3\leq k\leq r-1.\\b
\beta(b) = b &= \alpha(b), \qquad b \not\in \{ a_{1},\dots,a_{k} \}.
\end{aligned}
$$

Luego $$\alpha = \beta$$. Aplicamos H.I. en $$\begin{pmatrix}a_{1} & a_{3} & \cdots a_{r}\end{pmatrix}$$.

### Nota (Forma estándar)

$$\alpha = \begin{pmatrix} x_{1} & \cdots & x_{m}\end{pmatrix} = \begin{pmatrix}x_{1} & x_{m}\end{pmatrix} \begin{pmatrix}x_{1} & x_{m-1}\end{pmatrix} \cdots \begin{pmatrix}x_{1} & x_{2}\end{pmatrix}$$.

### Ejemplo (Factorización en transposiciones)

Considere

$$
\begin{aligned}
\alpha &=\begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
6 & 2 & 7 & 9 & 8 & 3 & 1 & 5 & 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 6 & 3 & 7
\end{pmatrix} \begin{pmatrix}
2
\end{pmatrix} \begin{pmatrix}
4 & 9
\end{pmatrix} \begin{pmatrix}
8 & 5
\end{pmatrix} \qquad \text{factorización en ciclos} \\
&= \begin{pmatrix}
1 & 3 & 7
\end{pmatrix} \begin{pmatrix}
1 & 6
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
4 & 9
\end{pmatrix} \begin{pmatrix}
5 & 8
\end{pmatrix} \\
&=\begin{pmatrix}
1 & 7
\end{pmatrix} \begin{pmatrix}
1 & 3
\end{pmatrix} \begin{pmatrix}
1 & 6
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
1 & 2
\end{pmatrix} \begin{pmatrix}
4 & 9
\end{pmatrix} \begin{pmatrix}
5 & 8
\end{pmatrix} \qquad \text{descomposición en transposiciones}.
\end{aligned}
$$

### Definición (Signo)

Sea $$n \in \mathbb{N}$$, $$\alpha \in S_{n}$$. Si $$\alpha = \beta_{1} \cdots \beta_{k}$$ es una factorización completa en ciclos disjuntos. Defina $$\operatorname{sgn}(\sigma) = (-1)^{n-k}$$.

### Teorema (Signo y transposiciones)

Sea $$\alpha \in S_{n}$$ y $$\tau$$ una transposición. Entonces, $$\operatorname{sgn}(\tau\alpha) = -\operatorname{sgn}(\alpha)$$.

***Prueba:*** Ejercicio

### Teorema (Signo separa producto)

Sea $$\alpha, \beta \in S_{n}$$. Entonces $$\operatorname{sgn}(\alpha\beta) = \operatorname{sgn}(\alpha) \operatorname{sgn}(\beta)$$.

***Prueba:*** Ejercicio, inducción sobre el número de transposiciones.

### Definición (Paridad de la permutación)

Decimos que $$\alpha \in S_{n}$$ es par si $$\alpha$$ se puede descomponer como el producto de un número par de transposiciones. En caso contrario $$\alpha$$ es impar.

### Teorema (Paridad y signo)

Sea $$\alpha \in S_{n}$$. $$\alpha$$ es impar si y solo si $$\operatorname{sgn}( \alpha ) = - 1$$.

### Definición (Grupo alternante)

$$A_{n}:= \{ \sigma \in S_{n}: \sigma \text{ es par} \}$$ es un grupo. Además. $$\lvert A_{n} \rvert = \frac{n!}{2}$$.
{% endraw %}
