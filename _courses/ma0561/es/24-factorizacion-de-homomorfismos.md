---
layout: chapter
course: ma0561
chapter: 24
title: "Factorización de homomorfismos"
slug: 24-factorizacion-de-homomorfismos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/24-factorizacion-de-homomorfismos/
---

{% raw %}
## El teorema de factorización

### Teorema (Factorización de un homomorfismo por un cociente)

Sean $$R, S$$ anillos e $$I$$ un $$R$$-ideal. Sea $$f : R \to S$$ un homomorfismo tal que $$I \subseteq \operatorname{Ker}(f)$$. Entonces existe un único homomorfismo $$\bar{f} : R/I \to S$$ tal que

$$
\bar{f}([x]) = f(x) \quad \text{para todo } x \in R.
$$

Equivalentemente, $$\bar{f} \circ \pi_{I} = f$$, es decir, el siguiente diagrama conmuta:

![La factorización de un homomorfismo a través del cociente](/assets/img/courses/ma0561/factorizacion-de-homomorfismos.svg)

***Prueba:*** *$$\bar{f}$$ está bien definida.* Si $$[x] = [y]$$, entonces

$$
[x] = [y] \iff x - y \in I \subseteq \operatorname{Ker}(f) \implies f(x - y) = f(x) - f(y) = 0_{S} \implies f(x) = f(y),
$$

y por lo tanto $$\bar{f}([x]) = \bar{f}([y])$$.

*$$\bar{f}$$ es un homomorfismo.* Al igual que en el primer teorema del isomorfismo, esto se hereda directamente de $$f$$:

$$
\bar{f}([x] + [y]) = \bar{f}([x + y]) = f(x + y) = f(x) + f(y) = \bar{f}([x]) + \bar{f}([y]),
$$

y análogamente para el producto; además $$\bar{f}([1]) = f(1) = 1_{S}$$.

*Unicidad.* Si $$g : R/I \to S$$ satisface $$g([x]) = f(x)$$ para todo $$x \in R$$, entonces $$g$$ y $$\bar{f}$$ coinciden en todas las clases $$[x]$$, que son todos los elementos de $$R/I$$; entonces $$g = \bar{f}$$.

### Teorema (Biyección entre homomorfismos que anulan $$I$$ y homomorfismos del cociente)

Sean $$R, S$$ anillos e $$I$$ un $$R$$-ideal. La función $$f \mapsto \bar{f}$$ es una biyección

$$
\{ f \in \operatorname{Hom}(R, S) :\ f(I) = \{0\} \} \longrightarrow \operatorname{Hom}(R/I, S).
$$

***Prueba:*** Ejercicio.

### Ejercicio (El único homomorfismo desde $$\mathbb{Z}$$)

Si $$f : \mathbb{Z} \to R$$, con $$R$$ un anillo, es un homomorfismo, entonces $$f(n) = n \cdot 1_{R}$$; en particular, hay un único homomorfismo $$\mathbb{Z} \to R$$.

### Ejemplo (Los homomorfismos de $$\mathbb{Z}_{m}$$ en $$\mathbb{Z}_{n}$$)

Sean $$m, n \in \mathbb{Z}^{+}$$. ¿Cuáles son los elementos de $$\operatorname{Hom}(\mathbb{Z}_{m}, \mathbb{Z}_{n})$$? Por la biyección del teorema anterior, con $$R = \mathbb{Z}$$ e $$I = (m)$$,

$$
|\operatorname{Hom}(\mathbb{Z}/(m), \mathbb{Z}_{n})| = \Big| \underbrace{\{ f : \mathbb{Z} \to \mathbb{Z}_{n}\ \text{homomorfismo} :\ f((m)) = \{[0]_{n}\} \}}_{A} \Big|.
$$

Usando el ejercicio anterior, si $$f \in A$$, entonces $$f(x) = x \cdot [1]_{n} = [x]_{n}$$; es decir, el único candidato es la reducción módulo $$n$$. Este candidato pertenece a $$A$$ si y solo si $$f((m)) = \{[0]_{n}\}$$, y como $$(m)$$ está generado por $$m$$, esto equivale a $$f(m) = [0]_{n}$$. Note que si $$f(m) \neq [0]_{n}$$, entonces $$A = \emptyset$$ y $$|\operatorname{Hom}(\mathbb{Z}_{m}, \mathbb{Z}_{n})| = 0$$. Por otro lado,

$$
f(m) = [0]_{n} \iff m \cdot [1]_{n} = [0]_{n} \iff [m]_{n} = [0]_{n} \iff n \mid m.
$$

En ese caso $$|A| = 1$$, de modo que $$|\operatorname{Hom}(\mathbb{Z}_{m}, \mathbb{Z}_{n})| = 1$$, y el único homomorfismo es

$$
x + (m) \mapsto x + (n), \qquad \text{es decir,} \qquad [x]_{m} \mapsto [x]_{n}.
$$

### Teorema (Extensión de homomorfismos al anillo de polinomios)

Sean $$A, B$$ anillos conmutativos, $$f \in \operatorname{Hom}(A, B)$$ y $$b \in B$$. Entonces existe un único $$\bar{f} \in \operatorname{Hom}(A[x], B)$$ tal que

$$
\bar{f}\left( \sum_{i=0}^{n} a_{i} x^{i} \right) = \sum_{i=0}^{n} f(a_{i})\, b^{i}.
$$

***Prueba:*** Ejercicio.

## Cocientes por ideales primos y maximales

### Teorema (Primo equivale a cociente dominio; maximal equivale a cociente cuerpo)

Sea $$R$$ un anillo conmutativo e $$I$$ un $$R$$-ideal. Entonces:

1. $$I$$ es primo $$\iff$$ $$R/I$$ es un dominio entero;
2. $$I$$ es maximal $$\iff$$ $$R/I$$ es un cuerpo.

***Prueba:*** *(a), “$$\Leftarrow$$”.* Suponga que $$R/I$$ es un dominio entero, y sean $$a, b \in R$$ tales que $$a b \in I$$. Entonces

$$
(a + I)(b + I) = a b + I = I,
$$

es decir, el producto de las clases es el cero de $$R/I$$. Como $$R/I$$ es un dominio entero, no posee divisores de cero, y entonces alguno de los dos factores debe ser cero: $$a + I = I$$ o $$b + I = I$$. Es decir, $$a \in I$$ o $$b \in I$$, de donde concluimos que $$I$$ es primo.

*(a), “$$\Rightarrow$$”.* Suponga que $$I$$ es primo. Note primero que $$R/I$$ es conmutativo, por serlo $$R$$. Sean $$a + I, b + I \in R/I$$ tales que

$$
(a + I)(b + I) = a b + I = I,
$$

es decir, $$a b \in I$$. Por la primalidad de $$I$$, tenemos que $$a \in I$$ o $$b \in I$$; suponiendo sin pérdida de generalidad que $$a \in I$$, obtenemos $$a + I = I$$. Es decir, si un producto de clases es cero, alguno de los factores es cero, de modo que $$R/I$$ no posee divisores de cero y es un dominio entero.

*(b), “$$\Rightarrow$$”.* Suponga que $$I$$ es maximal. Como $$I \neq R$$, tenemos que $$1 \notin I$$, y entonces $$[1] \neq [0]$$ en $$R/I$$. Sea $$x \in R$$ tal que $$[x] \neq [0]$$. Por el teorema de correspondencia, los ideales de $$R/I$$ corresponden a los ideales de $$R$$ que contienen a $$I$$; por la maximalidad de $$I$$, estos son solo $$I$$ y $$R$$, así que los únicos $$R/I$$-ideales son $$I/I = \{[0]\}$$ y $$R/I$$. Considere el ideal $$\langle [x] \rangle$$: como $$[x] \neq [0]$$, tenemos que $$\langle [x] \rangle \neq \{[0]\}$$, y entonces $$\langle [x] \rangle = R/I$$. Como $$[1] \in R/I = \langle [x] \rangle = \{ [y][x] :\ [y] \in R/I \}$$, existe $$[y] \in R/I$$ tal que $$[y][x] = [1]$$, es decir, $$[x]$$ es una unidad. Concluimos que todo elemento no nulo de $$R/I$$ es invertible y, junto con la conmutatividad y $$[1] \neq [0]$$, que $$R/I$$ es un cuerpo.

*(b), “$$\Leftarrow$$”.* Suponga que $$R/I$$ es un cuerpo. Entonces $$[1] \neq [0]$$ en $$R/I$$, es decir, $$1 \notin I$$, de modo que $$I \neq R$$. Sea ahora $$J$$ un ideal tal que $$I \subseteq J$$ y $$J \neq I$$; hay que ver que $$J = R$$. Por el teorema de correspondencia, $$J/I$$ es un ideal de $$R/I$$, y como existe $$x \in J \setminus I$$, tenemos que $$[x] \in J/I$$ con $$[x] \neq [0]$$, es decir, $$J/I \neq \{[0]\}$$. Pero un cuerpo solo posee los dos ideales triviales, así que $$J/I = R/I$$. Como la correspondencia $$J \mapsto J/I$$ es una biyección entre los ideales de $$R$$ que contienen a $$I$$ y los ideales de $$R/I$$, de $$J/I = R/I$$ concluimos que $$J = R$$. Es decir, $$I$$ es maximal.
{% endraw %}
