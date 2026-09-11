---
layout: chapter
course: ma0561
chapter: 15
title: "Anillos"
slug: 15-anillos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/15-anillos/
---

{% raw %}
## La definición de anillo y primeras propiedades

### Definición (Anillo y anillo conmutativo)

Un *anillo* es un conjunto $$R$$ junto con dos operaciones binarias $$+, \cdot$$ tales que:

1. $$(R, +)$$ es un grupo abeliano;
2. la operación $$\cdot$$ es asociativa y tiene un elemento neutro;
3. si $$a, b, c \in R$$, entonces $$a \cdot (b + c) = a \cdot b + a \cdot c$$ y $$(a + b) \cdot c = a \cdot c + b \cdot c$$.

Si además $$(R, +, \cdot)$$ cumple que para todos $$a, b \in R$$, $$a \cdot b = b \cdot a$$, entonces $$R$$ es un *anillo conmutativo*.

### Nota (No se supone que $$1 \neq 0$$)

Si $$0$$ es el neutro de $$+$$ y $$1$$ es el neutro de $$\cdot$$, no estamos suponiendo que $$1 \neq 0$$.

### Proposición (Reglas aritméticas básicas en un anillo)

Sea $$(R, +, \cdot)$$ un anillo. Entonces:

1. para todo $$a \in R$$, $$a \cdot 0 = 0 \cdot a = 0$$;
2. para todos $$a, b \in R$$, $$(-a) \cdot b = -(a \cdot b) = a \cdot (-b)$$;
3. para todos $$a, b \in R$$, $$(-a) \cdot (-b) = a \cdot b$$;
4. el neutro de $$\cdot$$ es único y $$(-1) \cdot a = -a$$.

***Prueba:*** Ejercicio.

### Nota (El anillo trivial)

Si $$0 = 1$$, entonces

$$
a = a \cdot 1 = a \cdot 0 = 0
$$

para todo $$a \in R$$, de donde $$R = \{0\}$$ y el anillo es el anillo trivial de un solo elemento.

### Ejemplo (Primeros ejemplos de anillos)

Los siguientes son ejemplos básicos:

1. $$(\mathbb{Z}, +, \cdot)$$ es un anillo conmutativo.
2. Sean $$n > 1$$ y $$R$$ un anillo. Entonces $$M_{n}(R)$$ es un anillo con las operaciones $$+, \cdot$$ de matrices. No es un anillo conmutativo.
3. $$(\mathbb{R}, +, \cdot)$$, $$(\mathbb{Q}, +, \cdot)$$ y $$(\mathbb{C}, +, \cdot)$$ son anillos conmutativos.

## Cuerpos y subanillos

### Definición (Cuerpo)

Un *cuerpo* $$(F, +, \cdot)$$ es un anillo conmutativo tal que $$1 \neq 0$$ y para todo $$a \in F$$,

$$
a \neq 0 \implies \exists b \in F\ (a \cdot b = 1).
$$

### Ejercicio (Los anillos numéricos usuales son cuerpos)

Muestre que $$(\mathbb{R}, +, \cdot)$$, $$(\mathbb{Q}, +, \cdot)$$ y $$(\mathbb{C}, +, \cdot)$$ son cuerpos.

### Definición (Subanillo)

Sea $$(R, +, \cdot)$$ un anillo y $$S \subseteq R$$. Decimos que $$S$$ es un *subanillo* de $$R$$ si $$(S, +\mid_{S \times S}, \cdot\mid_{S \times S})$$ es un anillo.

### Nota (Criterio de subanillo)

$$S \subseteq R$$ es un subanillo si y solo si $$1 \in S$$ y para todos $$a, b \in S$$ se cumple que $$a - b \in S$$ y $$a \cdot b \in S$$. (Ejercicio.)

## Unidades, divisores de cero y dominios enteros

### Definición (Unidades y el grupo de unidades)

Sea $$(R, +, \cdot)$$ un anillo. Un elemento $$a \in R$$ es una *unidad* si existe $$b \in R$$ tal que

$$
a \cdot b = 1 = b \cdot a.
$$

Si $$a$$ es unidad, entonces $$b$$ es único; en este caso escribimos $$b = a^{-1}$$. Definimos además el conjunto

$$
U_{R} = \{ a \in R :\ a \text{ es unidad} \}.
$$

A veces se escribe $$U_{R} = R^{\times}$$.

### Nota (Las unidades forman un grupo)

$$(U_{R}, \cdot)$$ es un grupo.

### Nota (Las unidades de un cuerpo)

Si $$(F, +, \cdot)$$ es un cuerpo, entonces $$U_{F} = F \setminus \{0\}$$.

### Definición (Divisores de cero, anillos de división y dominios enteros)

Sea $$(R, +, \cdot)$$ un anillo.

1. $$a \in R$$ es un *divisor de cero* si $$a \neq 0$$ y existe $$b \in R$$ tal que $$b \neq 0$$ y $$a \cdot b = 0$$ o $$b \cdot a = 0$$.
2. Un anillo sin divisores de cero se llama un *anillo de división*.
3. Un anillo conmutativo sin divisores de cero se llama un *dominio entero*.

### Nota (Las unidades no son divisores de cero)

Todo cuerpo es un dominio entero. Más en general, si $$a \in R$$ es una unidad, entonces $$a$$ no es divisor de cero.

### Lema (Los subanillos de un cuerpo son dominios enteros)

Sea $$(F, +, \cdot)$$ un cuerpo y $$R \subseteq F$$ un subanillo. Entonces $$R$$ es un dominio entero.

***Prueba:*** Primero, $$R$$ es conmutativo, pues la operación $$\cdot$$ de $$R$$ es la restricción de la de $$F$$, que es conmutativa. Ahora, suponga que existe $$a \in R$$ divisor de cero. Entonces $$a \neq 0$$ y existe $$b \in R$$ con $$b \neq 0$$ tal que $$a \cdot b = 0$$ o $$b \cdot a = 0$$. Como $$R \subseteq F$$, tenemos que $$a, b \in F$$, y entonces $$a$$ es un divisor de cero en $$F$$. Pero $$F$$ es un cuerpo y por lo tanto un dominio entero, así que $$F$$ no posee divisores de cero, una contradicción. Concluimos que $$R$$ no tiene divisores de cero, es decir, $$R$$ es un dominio entero.

### Proposición (Ley de cancelación)

Sea $$(R, +, \cdot)$$ un anillo y $$a \in R$$ tal que $$a \neq 0$$ y $$a$$ no es divisor de cero. Si $$a \cdot x = a \cdot y$$, entonces $$x = y$$.

***Prueba:*** Suponga que $$ax = ay$$. Entonces, restando y usando la distributividad,

$$
ax = ay \implies ax - ay = 0 \implies a(x - y) = 0.
$$

Si fuese $$x - y \neq 0$$, la igualdad $$a(x - y) = 0$$ exhibiría a $$a$$ como divisor de cero, pues $$a \neq 0$$. Como $$a$$ no es un divisor de cero, necesariamente $$x - y = 0$$, es decir, $$x = y$$.

### Lema (Todo dominio entero finito es un cuerpo)

Sea $$R \neq \{0\}$$ un dominio entero finito. Entonces $$R$$ es un cuerpo.

***Prueba:*** Note primero que, como $$R \neq \{0\}$$, tenemos que $$1 \neq 0$$. Sea $$a \in R$$ con $$a \neq 0$$, y considere la función $$\mu : R \to R$$ dada por $$\mu(x) = a \cdot x$$. Note que $$\mu$$ es inyectiva: si $$\mu(x) = \mu(y)$$, entonces $$a \cdot x = a \cdot y$$, y como $$a \neq 0$$ no es divisor de cero (pues $$R$$ es dominio entero), la ley de cancelación implica que $$x = y$$. Más aún, como $$R$$ es finito y $$\mu : R \to R$$ es inyectiva, $$\mu$$ es sobreyectiva. En particular, existe $$b \in R$$ tal que

$$
\mu(b) = a \cdot b = 1.
$$

Note que $$b \neq 0$$, pues si $$b = 0$$ tendríamos $$1 = a \cdot 0 = 0$$, y sabemos que $$0 \neq 1$$ en $$R$$. Concluimos que $$a$$ es invertible y, como $$a \neq 0$$ era arbitrario y $$R$$ es conmutativo con $$1 \neq 0$$, $$R$$ es un cuerpo.

### Ejemplo (Los enteros y los enteros módulo $$n$$)

Los siguientes ejemplos serán recurrentes:

1. $$(\mathbb{Z}, +, \cdot)$$ es un anillo, $$\mathbb{Z}^{\times} = \{1, -1\}$$ y $$\mathbb{Z}$$ es un dominio entero.
2. $$(\mathbb{Z}_{n}, +, \cdot)$$, con $$n > 1$$, es un anillo. Es un cuerpo si y solo si $$n$$ es primo, y

    $$
    \mathbb{Z}_{n}^{\times} = \{ [k] \in \mathbb{Z}_{n} :\ \operatorname{mcd}(k, n) = 1 \ \text{y}\ 0 \leq k \leq n - 1 \}.
    $$

    Si $$[x] \in \mathbb{Z}_{n}$$, hay exactamente dos posibilidades: $$[x] \in \mathbb{Z}_{n}^{\times}$$ o $$[x]$$ es divisor de cero (ejercicio).

### Ejemplo (El anillo de endomorfismos de un grupo abeliano)

Sea $$G$$ un grupo abeliano y sea

$$
\operatorname{End}(G) := \{ f : G \to G\ \text{homomorfismo} \}.
$$

Defina $$+, \cdot$$ en $$\operatorname{End}(G)$$ así: si $$f, g \in \operatorname{End}(G)$$, entonces $$f + g : G \to G$$ es tal que $$(f + g)(x) = f(x) + g(x)$$, y $$f \cdot g : G \to G$$ es tal que $$(f \cdot g)(x) = f(g(x))$$. **Ejercicio:** $$\operatorname{End}(G)$$ es un anillo no conmutativo.

### Ejemplo (El anillo de funciones con valores en un anillo)

Sea $$R \neq \{0\}$$ un anillo y $$X$$ un conjunto no vacío. Defina

$$
\mathcal{F}(X, R) := \{ f : X \to R\ \text{funciones} \},
$$

con las operaciones $$+, \cdot$$ dadas puntualmente: si $$f, g \in \mathcal{F}(X, R)$$, entonces

$$
f + g : X \to R, \quad x \mapsto f(x) +_{R} g(x), \qquad f \cdot g : X \to R, \quad x \mapsto f(x) \cdot_{R} g(x).
$$

**Ejercicio:** $$\mathcal{F}(X, R)$$ es un anillo, y es conmutativo si y solo si $$R$$ es conmutativo.

### Ejemplo (Los enteros gaussianos)

Sea $$\mathbb{Z}[i] := \{ a + bi :\ a, b \in \mathbb{Z} \} \subseteq \mathbb{C}$$. Este conjunto es llamado el de los *enteros gaussianos*. Como $$\mathbb{Z}[i]$$ es un subanillo del cuerpo $$\mathbb{C}$$, podemos ver que es un dominio entero.
{% endraw %}
