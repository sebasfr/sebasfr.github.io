---
layout: chapter
course: ma0561
chapter: 16
title: "El anillo de polinomios"
slug: 16-el-anillo-de-polinomios
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/16-el-anillo-de-polinomios/
---

{% raw %}
## La construcción de R[x]

### Definición (Sucesiones eventualmente cero en $$R$$)

Sea $$R$$ un anillo. Definimos el conjunto de sucesiones de $$R$$ como

$$
R^{\mathbb{N}} := \{ (a_{i})_{i \in \mathbb{N}} :\ a_{i} \in R \} = \{ (a_{0}, a_{1}, \dots, a_{n}, \dots) :\ a_{i} \in R \}.
$$

Llamamos $$P \subseteq R^{\mathbb{N}}$$ al subconjunto de sucesiones *eventualmente cero*, esto es,

$$
P := \{ (a_{i})_{i \in \mathbb{N}} :\ \exists N \in \mathbb{N}\ (a_{k} = 0,\ \forall k > N) \}.
$$

### Definición (La suma y los neutros en $$P$$)

Defina la operación $$+$$ en $$P$$ de la siguiente manera:

$$
(a_{i})_{i \in \mathbb{N}} + (b_{i})_{i \in \mathbb{N}} = (a_{i} + b_{i})_{i \in \mathbb{N}}.
$$

Note que esta operación es cerrada en $$P$$. Defina el uno y el cero en $$P$$ como

$$
\begin{aligned}
1 &:= (1, 0, 0, \dots, 0, \dots), \\
0 &:= (0, 0, \dots, 0, \dots).
\end{aligned}
$$

### Definición (Multiplicación escalar en $$P$$)

Si $$c \in R$$ y $$(a_{i})_{i \in \mathbb{N}} \in P$$, defina

$$
c \cdot (a_{i})_{i \in \mathbb{N}} = (c \cdot a_{0},\ c \cdot a_{1},\ \dots) \in P.
$$

### Notación (Las potencias $$x^{k}$$)

Si $$k \in \mathbb{N}$$, defina $$x^{k} := (\delta_{i,k})_{i \in \mathbb{N}}$$, donde $$\delta_{i,k}$$ es la delta de Kronecker. Por ejemplo:

$$
\begin{aligned}
x^{1} &:= (0, 1, 0, \dots), \\
x^{2} &:= (0, 0, 1, \dots), \\
1 &= x^{0} = (1, 0, \dots, 0).
\end{aligned}
$$

### Ejemplo (Un polinomio como sucesión)

$$
5 + 7x + 3x^{2} = 5 \cdot (1, 0, \dots, 0) + 7 \cdot (0, 1, 0, \dots, 0) + 3 \cdot (0, 0, 1, \dots) \in P.
$$

### Definición (El producto de polinomios y el anillo $$R[x]$$)

Sean $$p = (a_{i})_{i \in \mathbb{N}}$$ y $$q = (b_{i})_{i \in \mathbb{N}}$$, con $$p, q \in P$$. Defina $$p \cdot q = (c_{i})_{i \in \mathbb{N}}$$ tal que

$$
c_{k} = \sum_{i=0}^{k} a_{i} \cdot b_{k-i}.
$$

Note que $$p \cdot q \in P$$. Así, $$P$$ es un anillo con estas operaciones y lo denotamos por $$R[x]$$. Este anillo es llamado el *anillo de polinomios* sobre $$R$$.

## El grado de un polinomio

### Definición (Grado de un polinomio y coeficiente principal)

Antes de definir el grado de un polinomio, establecemos algunas convenciones sobre el conjunto $$\mathbb{N} \cup \{-\infty\}$$. En particular:

1. $$\forall n \in \mathbb{N}\ (-\infty < n)$$;
2. $$r + (-\infty) = -\infty$$ para $$r \in \mathbb{N}$$;
3. $$(-\infty) + (-\infty) = -\infty$$.

Sea $$R$$ un anillo y $$p \in R[x]$$. Definimos la función del grado $$\deg : R[x] \to \mathbb{N} \cup \{-\infty\}$$ tal que

$$
\deg(p) =
\begin{cases}
-\infty & \text{si } p = 0, \\
n & \text{si } p = (a_{i})_{i \in \mathbb{N}},\ a_{n} \neq 0\ \text{y } n \text{ es el elemento más grande de } \mathbb{N} \text{ tal que } a_{n} \neq 0.
\end{cases}
$$

Si $$\deg(p) = n$$, decimos que $$a_{n}$$ es el *coeficiente principal* de $$p$$.

### Proposición (Propiedades del grado)

Sea $$R$$ un anillo y sean $$p, q \in R[x]$$. Entonces:

1. $$\deg(p + q) \leq \max\{\deg(p), \deg(q)\}$$;
2. $$\deg(p \cdot q) \leq \deg(p) + \deg(q)$$;
3. si $$p \neq 0$$, $$q \neq 0$$ y los coeficientes principales de $$p$$ y $$q$$ no son divisores de cero, entonces $$\deg(p \cdot q) = \deg(p) + \deg(q)$$.

***Prueba:*** Si $$p = 0$$ o $$q = 0$$, las tres afirmaciones son inmediatas de las convenciones con $$-\infty$$. Suponga entonces que $$p = (a_{i})_{i \in \mathbb{N}}$$ y $$q = (b_{i})_{i \in \mathbb{N}}$$ son no nulos, con $$\deg(p) = n$$ y $$\deg(q) = m$$.

Para (1), si $$k > \max\{n, m\}$$, entonces $$a_{k} = 0$$ y $$b_{k} = 0$$, de modo que el coeficiente $$k$$-ésimo de $$p + q$$ es $$a_{k} + b_{k} = 0$$. Es decir, todo coeficiente de $$p + q$$ por encima de $$\max\{n, m\}$$ se anula, y por lo tanto $$\deg(p + q) \leq \max\{\deg(p), \deg(q)\}$$.

Para (2), escriba $$p \cdot q = (c_{k})_{k \in \mathbb{N}}$$ con $$c_{k} = \sum_{i=0}^{k} a_{i} b_{k-i}$$. Si $$k > n + m$$, entonces en cada sumando $$a_{i} b_{k-i}$$ ocurre una de dos: o bien $$i > n$$, y entonces $$a_{i} = 0$$; o bien $$i \leq n$$, y entonces $$k - i \geq k - n > m$$, de modo que $$b_{k-i} = 0$$. En ambos casos el sumando es cero, así que $$c_{k} = 0$$ para $$k > n + m$$, y concluimos que $$\deg(p \cdot q) \leq \deg(p) + \deg(q)$$.

Para (3), examinamos el coeficiente $$c_{n+m}$$: un sumando $$a_{i} b_{n+m-i}$$ solo puede ser no nulo si $$i \leq n$$ y $$n + m - i \leq m$$, es decir, si $$i \geq n$$; entonces el único sumando posiblemente no nulo es el de $$i = n$$, y $$c_{n+m} = a_{n} b_{m}$$. Como $$a_{n}$$ no es divisor de cero, $$a_{n} \neq 0$$ (es coeficiente principal) y $$b_{m} \neq 0$$, tenemos que $$a_{n} b_{m} \neq 0$$. Entonces $$c_{n+m} \neq 0$$ y, junto con (2), $$\deg(p \cdot q) = n + m$$.

### Definición (El anillo de polinomios en $$n$$ variables)

Sea $$R$$ un anillo conmutativo y $$n \geq 1$$. Definimos el anillo de polinomios con $$n$$ variables como

$$
R[x_{1}, \dots, x_{n}] =
\begin{cases}
R[x_{1}] & \text{si } n = 1, \\
R[x_{1}, \dots, x_{n-1}][x_{n}] & \text{si } n > 1.
\end{cases}
$$

### Nota (Interpretación de los polinomios como funciones)

Si $$p \in R[x]$$, entonces $$p$$ define una función $$\tilde{p} : R \to R$$: si $$p = (a_{i})_{i \in \mathbb{N}} = a_{0} + a_{1} x + \dots + a_{n} x^{n}$$, entonces

$$
\tilde{p} :\ c \mapsto a_{0} + a_{1} c + \dots + a_{n} c^{n}.
$$

**Importante:** no se debe confundir el polinomio con su función asociada.

### Ejemplo (Polinomios distintos con la misma función asociada)

Considere los siguientes polinomios en $$\mathbb{Z}_{3}[x]$$:

$$
\begin{aligned}
p &= x^{2} + 1, \\
q &= x^{3} + x^{2} + 2x + 1.
\end{aligned}
$$

Note que $$p \neq q$$ pero $$\tilde{p} = \tilde{q}$$:

$$
\begin{aligned}
\tilde{p}(0) &= 1 = \tilde{q}(0), \\
\tilde{p}(1) &= 2 = \tilde{q}(1), \\
\tilde{p}(2) &= 2 = \tilde{q}(2).
\end{aligned}
$$

## El algoritmo de la división y las raíces

### Teorema (Algoritmo de la división para anillos conmutativos)

Sea $$R$$ un anillo conmutativo. Sean $$f, g \in R[x]$$ tales que $$g \neq 0$$, y sea $$b$$ el coeficiente principal de $$g$$. Entonces existen $$m \geq 0$$ y $$q, r \in R[x]$$ tales que

$$
b^{m} \cdot f = q \cdot g + r, \quad \text{con } \deg(r) < \deg(g) \ \text{y}\ m \leq \max\{0,\ \deg(f) - \deg(g) + 1\}.
$$

***Prueba:*** Procedemos por inducción fuerte sobre $$\deg(f)$$. Si $$\deg(f) < \deg(g)$$ (en particular, si $$f = 0$$), tome $$m = 0$$, $$q = 0$$ y $$r = f$$; entonces $$b^{0} f = 0 \cdot g + f$$, $$\deg(r) = \deg(f) < \deg(g)$$ y $$m = 0 \leq \max\{0, \deg(f) - \deg(g) + 1\}$$.

Suponga ahora que $$\deg(f) \geq \deg(g)$$, y que el resultado vale para todo polinomio de grado menor que $$\deg(f)$$. Sean $$a$$ el coeficiente principal de $$f$$, $$n = \deg(f)$$ y $$k = \deg(g)$$, de modo que $$n \geq k$$. Defina

$$
h := b \cdot f - a \cdot x^{\,n-k} \cdot g.
$$

Entonces $$\deg(h) < \deg(f)$$: en efecto, tanto $$b \cdot f$$ como $$a \cdot x^{\,n-k} \cdot g$$ tienen grado a lo más $$n$$, y sus coeficientes de grado $$n$$ son $$b \cdot a$$ y $$a \cdot b$$ respectivamente, que coinciden porque $$R$$ es conmutativo; al restar, el término de grado $$n$$ se cancela. Por hipótesis inductiva aplicada a $$h$$, existen $$m_{1} \geq 0$$ y $$q_{1}, r_{1} \in R[x]$$ tales que

$$
b^{m_{1}} \cdot h = q_{1} \cdot g + r_{1}, \qquad \deg(r_{1}) < \deg(g), \qquad m_{1} \leq \max\{0,\ \deg(h) - \deg(g) + 1\}.
$$

Así, sustituyendo la definición de $$h$$, tenemos que

$$
\begin{aligned}
q_{1} \cdot g + r_{1} = b^{m_{1}} \cdot h &= b^{m_{1}} \big( b \cdot f - a \cdot x^{\,n-k} \cdot g \big) \\
&= b^{m_{1} + 1} \cdot f - b^{m_{1}} \cdot a \cdot x^{\,n-k} \cdot g,
\end{aligned}
$$

y despejando obtenemos

$$
b^{m_{1} + 1} \cdot f = \big( q_{1} + b^{m_{1}} \cdot a \cdot x^{\,n-k} \big) \cdot g + r_{1}.
$$

Tomando $$m = m_{1} + 1$$, $$q = q_{1} + b^{m_{1}} \cdot a \cdot x^{\,n-k}$$ y $$r = r_{1}$$, se cumple la identidad con $$\deg(r) < \deg(g)$$. Finalmente, como $$\deg(h) \leq n - 1$$, tenemos que

$$
m = m_{1} + 1 \leq \max\{0,\ (n - 1) - k + 1\} + 1 \leq (n - k) + 1 = \max\{0,\ \deg(f) - \deg(g) + 1\},
$$

donde la última igualdad usa que $$n \geq k$$. Esto completa el paso inductivo y la prueba.

### Definición (Raíz de un polinomio)

Sea $$p(x) \in R[x]$$. Decimos que $$\alpha \in R$$ es una *raíz* de $$p$$ si $$\tilde{p}(\alpha) = 0$$.

### Teorema (Factorización de la raíz de un polinomio)

Sea $$R$$ un anillo conmutativo y $$p(x) \in R[x]$$. Entonces $$\alpha$$ es raíz de $$p(x)$$ si y solo si existe $$t \in R[x]$$ tal que $$p = (x - \alpha) \cdot t$$.

***Prueba:*** Ejercicio.

### Teorema (Algoritmo de la división para cuerpos)

Sea $$F$$ un cuerpo. Sean $$f, g \in F[x]$$ tales que $$g \neq 0$$. Entonces existen únicos $$q, r \in F[x]$$ tales que

$$
f = q \cdot g + r, \quad \text{con } \deg(r) < \deg(g).
$$

***Prueba:*** Para la existencia se aplica el algoritmo de la división para anillos: si $$b$$ es el coeficiente principal de $$g$$, existen $$m \geq 0$$ y $$q_{0}, r_{0} \in F[x]$$ tales que $$b^{m} f = q_{0} g + r_{0}$$ con $$\deg(r_{0}) < \deg(g)$$. Como $$g \neq 0$$, tenemos que $$b \neq 0$$, y entonces $$b$$ es una unidad de $$F$$; en particular $$b^{m}$$ es invertible. Multiplicando por $$b^{-m}$$ obtenemos

$$
f = \big( b^{-m} q_{0} \big) g + b^{-m} r_{0},
$$

y basta tomar $$q = b^{-m} q_{0}$$ y $$r = b^{-m} r_{0}$$. Note que $$\deg(r) = \deg(r_{0}) < \deg(g)$$, pues multiplicar por la constante no nula $$b^{-m}$$ no altera el grado (en un cuerpo no hay divisores de cero). La unicidad queda como ejercicio.

### Teorema (Polinomios sobre un dominio entero)

Sea $$A$$ un dominio entero. Entonces:

1. $$A[x]$$ es un dominio entero y $$(A[x])^{\times} = A^{\times}$$;
2. si $$p \in A[x]$$, $$p \neq 0$$ y $$\deg(p) = n$$, entonces $$p$$ tiene a lo más $$n$$ raíces distintas.

***Prueba:*** *Parte 1.* Suponga que existen $$p, q \in A[x]$$, con $$p \neq 0$$ y $$q \neq 0$$, tales que $$p \cdot q = 0$$. Entonces $$\deg(p \cdot q) = -\infty$$. Pero los coeficientes principales de $$p$$ y $$q$$ son distintos de cero, y en un dominio entero los elementos no nulos no son divisores de cero; entonces, por las propiedades del grado,

$$
\deg(p \cdot q) = \deg(p) + \deg(q) \in \mathbb{N},
$$

una contradicción. Concluimos que $$A[x]$$ es un dominio entero.

Para las unidades, note primero que $$A^{\times} \subseteq (A[x])^{\times}$$, pues la igualdad $$a \cdot a^{-1} = 1$$ en $$A$$ también vale en $$A[x]$$ al identificar las constantes. Recíprocamente, sea $$p \in (A[x])^{\times}$$. Entonces existe $$q \in A[x]$$ tal que $$p \cdot q = 1$$; en particular $$p \neq 0$$ y $$q \neq 0$$. Así,

$$
\deg(p \cdot q) = \underbrace{\deg(p) + \deg(q)}_{\in\, \mathbb{N}} = \deg(1) = 0,
$$

de donde $$\deg(p) = \deg(q) = 0$$, y entonces $$p$$ y $$q$$ son constantes, es decir, $$p, q \in A$$ con $$p \cdot q = 1$$. Concluimos que $$p \in A^{\times}$$, y por lo tanto $$(A[x])^{\times} = A^{\times}$$.

*Parte 2.* Procedemos por inducción sobre $$n = \deg(p)$$. Si $$n = 0$$, entonces $$p = a_{0} \neq 0$$ es constante, así que $$\tilde{p}(\alpha) = a_{0} \neq 0$$ para todo $$\alpha \in A$$, y $$p$$ tiene $$0 \leq 0$$ raíces. Suponga ahora que el resultado vale para polinomios no nulos de grado $$n - 1$$, y sea $$p$$ de grado $$n \geq 1$$. Si $$p$$ no tiene raíces, no hay nada que probar. Si $$\alpha$$ es una raíz de $$p$$, por el teorema de factorización de la raíz existe $$t \in A[x]$$ tal que $$p = (x - \alpha) \cdot t$$; note que $$t \neq 0$$, pues $$p \neq 0$$. Como el coeficiente principal de $$x - \alpha$$ es $$1$$, que no es divisor de cero, las propiedades del grado dan $$n = \deg(p) = 1 + \deg(t)$$, es decir, $$\deg(t) = n - 1$$. Ahora, si $$\beta \neq \alpha$$ es otra raíz de $$p$$, evaluando en $$\beta$$ tenemos que

$$
0 = \tilde{p}(\beta) = (\beta - \alpha) \cdot \tilde{t}(\beta),
$$

donde usamos que la función asociada de un producto es el producto de las funciones asociadas cuando el anillo es conmutativo (verificación directa con la fórmula $$c_{k} = \sum_{i} a_{i} b_{k-i}$$). Como $$\beta - \alpha \neq 0$$ y $$A$$ es un dominio entero, necesariamente $$\tilde{t}(\beta) = 0$$, es decir, toda raíz de $$p$$ distinta de $$\alpha$$ es raíz de $$t$$. Por hipótesis inductiva, $$t$$ tiene a lo más $$n - 1$$ raíces distintas, y entonces $$p$$ tiene a lo más $$1 + (n - 1) = n$$ raíces distintas.
{% endraw %}
