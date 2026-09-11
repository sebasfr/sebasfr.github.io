---
layout: chapter
course: ma0561
chapter: 17
title: "Ideales"
slug: 17-ideales
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/17-ideales/
---

{% raw %}
## Definición y ejemplos

### Definición ($$R$$-ideal por la izquierda, por la derecha y bilátero)

Sea $$R$$ un anillo y $$I \subseteq R$$ con $$I \neq \emptyset$$. Decimos que $$I$$ es un *$$R$$-ideal por la izquierda* (respectivamente, *por la derecha*) si:

1. $$\forall x, y \in I\ (x + y \in I)$$;
2. $$\forall r \in R\ \forall x \in I\ (r \cdot x \in I)$$ (respectivamente, $$x \cdot r \in I$$); esta propiedad se llama *absorción*.

Si $$I$$ es un $$R$$-ideal por la derecha y por la izquierda, decimos que $$I$$ es un *$$R$$-ideal*.

### Nota (Primeras propiedades de los ideales)

Sea $$I$$ un $$R$$-ideal (izquierdo o derecho).

1. $$(I, +)$$ es un grupo. Note que $$0 \in I$$: en efecto, como $$0 \in R$$ y la proposición de reglas aritméticas da $$0 \cdot x = 0$$ para todo $$x \in R$$, la absorción aplicada a cualquier $$x \in I$$ muestra que $$0 = 0 \cdot x \in I$$.
2. Sea $$x \in I$$. Entonces $$(-1) \cdot x = -x \in I$$.
3. Si $$1 \in I$$, entonces $$I = R$$, pues si $$a \in R$$, la absorción da $$a \cdot 1 = a \in I$$.

### Ejemplo (Ideales triviales y los ideales de un cuerpo)

Los primeros ejemplos de ideales:

1. Si $$R$$ es un anillo, $$R$$ y $$\{0\}$$ son ideales; se les llama los *ideales triviales*.
2. Sea $$F$$ un cuerpo y $$I$$ un ideal en $$F$$ tal que $$I \neq \{0\}$$. Sea $$a \in I$$ con $$a \neq 0$$. Entonces

    $$
    a^{-1} \in F \implies a^{-1} \cdot a \in I \implies 1 \in I \implies I = F.
    $$

    Concluimos que un cuerpo solo posee los dos ideales triviales.

### Ejemplo (Ideales en anillos de polinomios)

Sea $$R$$ un anillo conmutativo.

1. Sea $$I \subseteq R[x]$$ tal que

    $$
    I = \{ p \in R[x] :\ \text{el término constante de } p \text{ es cero} \}.
    $$

    Entonces $$I$$ es un ideal.
2. Si $$I$$ es un ideal de $$R$$, defina

    $$
    I[x] = \{ p \in R[x] :\ p(x) \text{ tiene todos sus coeficientes en } I \}.
    $$

    Entonces $$I[x]$$ es un ideal en $$R[x]$$.

### Ejemplo (Ideales en $$\mathbb{Z}$$ y en $$\mathbb{Z}_{n}$$)

Dos familias de ideales en los anillos de enteros:

1. $$n\mathbb{Z}$$ es un ideal de $$\mathbb{Z}$$.
2. Sea $$n > 1$$ y considere $$\mathbb{Z}_{n}$$. Sea $$d \in \mathbb{Z}_{n}$$ tal que $$d \mid n$$. Entonces $$\langle d \rangle$$ (el grupo aditivo generado por $$d$$) es un ideal.

### Ejemplo (Un ideal por la izquierda que no es ideal por la derecha)

Sea $$R = M_{2 \times 2}(\mathbb{R})$$ y defina

$$
I := \left\{ \begin{pmatrix} a & 0 \\ b & 0 \end{pmatrix} :\ a, b \in \mathbb{R} \right\}.
$$

Note que

$$
\begin{aligned}
\begin{pmatrix} x & y \\ z & w \end{pmatrix} \begin{pmatrix} a & 0 \\ b & 0 \end{pmatrix} &= \begin{pmatrix} xa + yb & 0 \\ za + wb & 0 \end{pmatrix} \in I, \\
\begin{pmatrix} a & 0 \\ b & 0 \end{pmatrix} \begin{pmatrix} x & y \\ z & w \end{pmatrix} &= \begin{pmatrix} ax & ay \\ bx & by \end{pmatrix} \notin I \ \text{en general},
\end{aligned}
$$

por lo que $$I$$ es un ideal por la izquierda pero no por la derecha.

### Definición (Elemento nilpotente y el nilradical)

Si $$R$$ es un anillo, $$a \in R$$ es *nilpotente* si existe $$n \in \mathbb{N}$$ tal que $$a^{n} = 0$$. El menor $$n$$ que exista es el *índice de nilpotencia* de $$a$$. Además,

$$
\operatorname{Nil}(R) = \{ x \in R :\ x \text{ es nilpotente} \}
$$

es un ideal, llamado el *nilradical* de $$R$$ (ejercicio).

## Operaciones con ideales y el ideal generado

### Definición (Suma, intersección y producto de ideales)

Sea $$R$$ un anillo conmutativo y sean $$I, J$$ ideales. Defina:

$$
\begin{aligned}
I + J &:= \{ a + b :\ a \in I,\ b \in J \}, \\
I \cap J &:= \{ x :\ x \in I \wedge x \in J \}, \\
I \cdot J &:= \left\{ \sum_{i=1}^{n} a_{i} \cdot b_{i} :\ a_{i} \in I,\ b_{i} \in J,\ n \in \mathbb{N} \right\}.
\end{aligned}
$$

### Teorema (Las operaciones de ideales producen ideales)

$$I + J$$, $$I \cap J$$ e $$I \cdot J$$ son ideales.

***Prueba:*** Ejercicio.

### Corolario (La intersección de ideales es un ideal)

La intersección de cualquier familia de ideales de $$R$$ es un ideal de $$R$$.

***Prueba:*** Sea $$\{I_{\alpha}\}_{\alpha \in \Delta}$$ una familia de ideales y $$I = \bigcap_{\alpha \in \Delta} I_{\alpha}$$. Como $$0 \in I_{\alpha}$$ para todo $$\alpha$$, tenemos que $$0 \in I$$, y en particular $$I \neq \emptyset$$. Si $$x, y \in I$$, entonces $$x, y \in I_{\alpha}$$ para todo $$\alpha$$, y como cada $$I_{\alpha}$$ es cerrado bajo sumas, $$x + y \in I_{\alpha}$$ para todo $$\alpha$$, es decir, $$x + y \in I$$. Finalmente, si $$r \in R$$ y $$x \in I$$, la absorción en cada $$I_{\alpha}$$ da $$r x \in I_{\alpha}$$ para todo $$\alpha$$, de modo que $$r x \in I$$ (y análogamente $$x r \in I$$). Concluimos que $$I$$ es un ideal.

### Definición (Ideal generado, finitamente generado y principal)

Sea $$R$$ un anillo conmutativo y $$U \subseteq R$$.

1. $$(U) := \bigcap_{U \subseteq I,\ I \text{ ideal}} I$$ es el *ideal generado* por $$U$$. Note que $$(U)$$ es un ideal, puesto que la intersección de ideales es un ideal. Si $$U$$ es finito y $$U = \{u_{1}, \dots, u_{n}\}$$, escribimos $$(u_{1}, \dots, u_{n}) = (U)$$.
2. Decimos que un ideal $$I$$ es *finitamente generado* si existe $$U \subseteq R$$ finito tal que $$I = (U)$$.
3. Decimos que $$I$$ es un *ideal principal* si existe $$a \in R$$ tal que $$I = (a)$$. Note que en este caso $$I = (a) = \{ r \cdot a :\ r \in R \}$$ (ejercicio).

### Teorema (Caracterización del ideal generado como combinaciones)

Sea $$R$$ un anillo conmutativo y $$\emptyset \neq U \subseteq R$$. Entonces

$$
(U) = \underbrace{\left\{ \sum_{i=1}^{n} a_{i} u_{i} :\ n \in \mathbb{N},\ a_{i} \in R,\ u_{i} \in U \right\}}_{J}.
$$

***Prueba:*** Veamos primero que $$J$$ es un ideal: la suma de dos combinaciones de la forma $$\sum a_{i} u_{i}$$ es de nuevo una combinación de ese tipo, y si $$r \in R$$, entonces $$r \sum_{i=1}^{n} a_{i} u_{i} = \sum_{i=1}^{n} (r a_{i}) u_{i} \in J$$, lo que da la absorción. Además $$U \subseteq J$$, pues $$u = 1 \cdot u$$ para cada $$u \in U$$. Entonces $$J$$ es uno de los ideales que intersecamos para definir $$(U)$$, y por lo tanto $$(U) \subseteq J$$.

Recíprocamente, sea $$w \in J$$. Entonces existen $$n \in \mathbb{N}$$, $$a_{i} \in R$$ y $$u_{i} \in U$$ tales que $$w = \sum_{i=1}^{n} a_{i} u_{i}$$. Sea $$I$$ un ideal cualquiera tal que $$U \subseteq I$$. Entonces, por absorción, $$a_{i} u_{i} \in I$$ para todo $$i$$, y por cerradura de la suma $$\sum_{i=1}^{n} a_{i} u_{i} \in I$$, de modo que $$w \in I$$. Como $$I$$ es arbitrario, tenemos que

$$
w \in \bigcap_{U \subseteq I,\ I \text{ ideal}} I = (U),
$$

es decir, $$J \subseteq (U)$$. Concluimos la igualdad.

### Ejemplo (Cálculos con ideales generados)

Sea $$R$$ un anillo conmutativo.

1. $$(0) = \{0\}$$ y $$(1) = R$$. Si $$u \in R^{\times}$$, entonces $$(u) = R$$. En general, si $$u_{1}, \dots, u_{n} \in I$$ con $$I$$ ideal, entonces $$(u_{1}, \dots, u_{n}) \subseteq I$$.
2. Si $$R = \mathbb{Z}$$, entonces $$(6, 15) = (3)$$: como $$6 = 3 \cdot 2$$ y $$15 = 3 \cdot 5$$, tenemos que $$6, 15 \in (3)$$ y por lo tanto $$(6, 15) \subseteq (3)$$. Por otra parte, $$3 = 6 \cdot (-2) + 15$$, entonces $$3 \in (6, 15)$$ y por lo tanto $$(3) \subseteq (6, 15)$$.
3. Considere el anillo de polinomios $$R[x]$$. Note que

    $$
    (x) = \{ x \cdot p(x) :\ p(x) \in R[x] \} = \{ r(x) :\ \text{el coeficiente constante de } r(x) \text{ es cero} \}.
    $$

### Definición (Anillo de ideales principales y DIP)

Recogemos dos nociones:

1. Un *anillo de ideales principales* es un anillo en el que todo ideal es principal.
2. Un *dominio de ideales principales* (DIP) es un anillo de ideales principales que es un dominio entero.

### Ejemplo ($$\mathbb{Z}[x]$$ no es un anillo de ideales principales)

Sea $$R = \mathbb{Z}[x]$$. Se puede probar que $$(2, x)$$ no es principal (ejercicio). Entonces $$\mathbb{Z}[x]$$ no es un anillo de ideales principales.

### Teorema ($$\mathbb{Z}$$ es un DIP, y $$K[x]$$ es un DIP si $$K$$ es un cuerpo)

$$\mathbb{Z}$$ es un dominio de ideales principales. Si $$K$$ es un cuerpo, entonces $$K[x]$$ es un dominio de ideales principales.

***Prueba:*** Ya sabemos que $$\mathbb{Z}$$ es un dominio entero. Claramente $$\{0\} = (0)$$ es principal. Sea $$I \neq \{0\}$$ un ideal de $$\mathbb{Z}$$. Entonces existe $$a \in I$$ con $$a \neq 0$$; como $$-a \in I$$, existe al menos un elemento de $$\mathbb{Z}^{+}$$ en $$I$$. Sea $$b \in I$$ el elemento positivo más pequeño de $$I$$. Probaremos que $$I = (b)$$. Claramente $$(b) \subseteq I$$, por absorción. Sea $$a \in I$$. Por el algoritmo de la división en $$\mathbb{Z}$$, existen $$q, r \in \mathbb{Z}$$ tales que

$$
a = q b + r, \quad \text{con } 0 \leq r < b.
$$

Entonces $$a - q b = r \in I$$, pues $$a \in I$$ y $$q b \in I$$. Por la minimalidad de $$b$$, necesariamente $$r = 0$$; entonces $$a = q b$$, de modo que $$a \in (b)$$ y por lo tanto $$I \subseteq (b)$$. Concluimos que $$I = (b)$$.

La prueba de que $$K[x]$$ es un DIP si $$K$$ es un cuerpo queda como ejercicio.

### Definición (Ideales primos relativos)

Sea $$R$$ un anillo conmutativo y sean $$I, J$$ ideales. Decimos que $$I$$ y $$J$$ son *primos relativos* si $$I + J = R$$.

### Proposición (Propiedades de la suma y el producto de ideales)

Sea $$R$$ un anillo conmutativo y sean $$I, J, K$$ ideales. Entonces:

1. $$I + J = J + I$$ y $$I J = J I$$;
2. $$I + (J + K) = (I + J) + K$$ y $$(I J) K = I (J K)$$;
3. $$I (J + K) = I J + I K$$;
4. $$(0) + I = I$$, $$R \cdot I = I$$ y $$I + R = R$$;
5. $$(0) \cdot I = (0)$$;
6. $$I J \subseteq I \cap J$$.

***Prueba:*** Para (1): $$I + J = J + I$$ es inmediato de la conmutatividad de la suma en $$R$$, y $$I J = J I$$ porque cada generador satisface $$a_{i} b_{i} = b_{i} a_{i}$$, al ser $$R$$ conmutativo.

Para (2): ambos lados de $$I + (J + K) = (I + J) + K$$ son $$\{ a + b + c :\ a \in I,\ b \in J,\ c \in K \}$$, por la asociatividad de la suma. Para el producto, note que todo elemento de $$(I J) K$$ es una suma finita $$\sum_{i} w_{i} c_{i}$$ con $$w_{i} \in I J$$ y $$c_{i} \in K$$; escribiendo cada $$w_{i}$$ como suma finita de productos $$a b$$, y distribuyendo, $$(I J) K$$ es exactamente el conjunto de sumas finitas de productos triples $$(a b) c$$ con $$a \in I$$, $$b \in J$$, $$c \in K$$. El mismo argumento describe $$I (J K)$$ como las sumas finitas de productos $$a (b c)$$, y la asociatividad de $$R$$ da la igualdad.

Para (3): “$$\subseteq$$” porque cada generador satisface $$a (b + c) = a b + a c \in I J + I K$$, y las sumas finitas de estos quedan en el ideal $$I J + I K$$. “$$\supseteq$$” porque $$I J \subseteq I (J + K)$$ (todo $$b \in J$$ se escribe $$b = b + 0 \in J + K$$) e $$I K \subseteq I (J + K)$$, y el ideal $$I (J + K)$$ es cerrado bajo sumas.

Para (4): $$(0) + I = I$$ pues $$0 + a = a$$; $$R \cdot I = I$$ pues “$$\subseteq$$” es la absorción y “$$\supseteq$$” se sigue de $$a = 1 \cdot a$$; y $$I + R = R$$ pues todo $$a \in R$$ se escribe $$a = 0 + a$$.

Para (5): cada generador de $$(0) \cdot I$$ es de la forma $$0 \cdot b = 0$$, así que $$(0) \cdot I = \{0\} = (0)$$.

Para (6): cada generador $$a b$$ con $$a \in I$$, $$b \in J$$ pertenece a $$I$$ (absorción de $$I$$, con $$b \in R$$) y a $$J$$ (absorción de $$J$$, con $$a \in R$$); como $$I \cap J$$ es un ideal, las sumas finitas de tales productos quedan en $$I \cap J$$, es decir, $$I J \subseteq I \cap J$$.

## Ideales maximales y el teorema de Krull

### Definición (Ideal maximal y el espectro maximal)

Sea $$R$$ un anillo conmutativo. Un ideal $$\mathfrak{m} \neq R$$ es *maximal* si cada vez que $$J$$ es un ideal tal que $$\mathfrak{m} \subseteq J$$, entonces $$J = R$$ o $$J = \mathfrak{m}$$. Denotamos por $$\operatorname{mSpec}(R)$$ al conjunto de ideales maximales de $$R$$.

### Ejemplo (Espectros maximales conocidos)

Calculamos $$\operatorname{mSpec}$$ en los ejemplos básicos:

1. Si $$R = \{0\}$$, entonces $$\operatorname{mSpec}(R) = \emptyset$$.
2. Si $$K$$ es un cuerpo, entonces $$\operatorname{mSpec}(K) = \{ \{0\} \}$$.
3. Sea $$R = \mathbb{Z}_{4}$$. Los ideales son $$(0)$$, $$(2) = \{0, 2\}$$ y $$(1) = \mathbb{Z}_{4} = (3)$$. Note que $$\operatorname{mSpec}(\mathbb{Z}_{4}) = \{(2)\}$$.
4. En $$\mathbb{Z}$$ todos los ideales son de la forma $$n\mathbb{Z}$$ con $$n \in \mathbb{N}$$. Muestre que $$n\mathbb{Z}$$ es maximal si y solo si $$n$$ es primo.

### Axioma (Lema de Zorn)

Sea $$(X, \leq)$$ un conjunto parcialmente ordenado. Si

1. $$X \neq \emptyset$$, y
2. todo subconjunto totalmente ordenado de $$X$$ posee una cota superior en $$X$$,

entonces $$X$$ posee un elemento maximal.

### Teorema (Krull: todo ideal propio está contenido en un maximal)

Sea $$R \neq \{0\}$$ un anillo conmutativo y sea $$I$$ un ideal propio. Entonces existe $$\mathfrak{m}$$ un ideal maximal tal que $$I \subseteq \mathfrak{m}$$.

***Prueba:*** Sea

$$
\Omega := \{ J :\ J \text{ ideal},\ J \neq R,\ I \subseteq J \},
$$

que es un conjunto parcialmente ordenado por la inclusión. Note que $$\Omega \neq \emptyset$$, pues $$I \in \Omega$$. Para aplicar el lema de Zorn, sea $$(C_{\alpha})_{\alpha \in \Delta}$$ una cadena en $$\Omega$$, que podemos suponer no vacía (la cadena vacía tiene a $$I$$ como cota superior), y sea $$N = \bigcup_{\alpha \in \Delta} C_{\alpha}$$. Probaremos que $$N \in \Omega$$.

Primero, $$N$$ es un ideal. Note que $$N \neq \emptyset$$, pues $$C_{\alpha} \subseteq N$$ para $$\alpha \in \Delta$$ y cada $$C_{\alpha}$$ es no vacío. Sean $$x, y \in N$$. Entonces existen $$\alpha, \beta \in \Delta$$ tales que $$x \in C_{\alpha}$$ y $$y \in C_{\beta}$$. Como $$(C_{\alpha})$$ es una cadena, tenemos que $$C_{\alpha} \subseteq C_{\beta}$$ o $$C_{\beta} \subseteq C_{\alpha}$$; sin pérdida de generalidad, $$C_{\alpha} \subseteq C_{\beta}$$. Entonces $$x, y \in C_{\beta}$$, y como $$C_{\beta}$$ es un ideal, $$x + y \in C_{\beta} \subseteq N$$. De la misma manera, si $$x \in N$$ y $$r \in R$$, entonces $$x \in C_{\alpha}$$ para algún $$\alpha$$, y $$r \cdot x \in C_{\alpha} \subseteq N$$ por absorción.

Segundo, $$N \neq R$$: si $$N = R$$, entonces $$1 \in N$$, de modo que existe $$\alpha$$ tal que $$1 \in C_{\alpha}$$, y por lo tanto $$C_{\alpha} = R$$, lo que contradice que $$C_{\alpha} \in \Omega$$. Finalmente, $$I \subseteq C_{\alpha} \subseteq N$$ para cualquier $$\alpha \in \Delta$$, por lo que $$N \in \Omega$$ y $$N$$ es una cota superior de la cadena $$(C_{\alpha})_{\alpha \in \Delta}$$.

Luego, por el lema de Zorn, existe $$\mathfrak{m}$$ un elemento maximal en $$\Omega$$. Veamos que $$\mathfrak{m}$$ es un ideal maximal de $$R$$: por construcción $$\mathfrak{m} \neq R$$ y $$I \subseteq \mathfrak{m}$$. Si $$J$$ es un ideal tal que $$\mathfrak{m} \subseteq J$$ y $$J \neq R$$, entonces $$I \subseteq \mathfrak{m} \subseteq J$$, así que $$J \in \Omega$$; por la maximalidad de $$\mathfrak{m}$$ en $$\Omega$$, tenemos que $$J = \mathfrak{m}$$. Es decir, todo ideal que contiene a $$\mathfrak{m}$$ es $$R$$ o es $$\mathfrak{m}$$, que es la definición de ideal maximal.

### Corolario (El espectro maximal es no vacío y detecta las no unidades)

Si $$R \neq \{0\}$$ es un anillo conmutativo, entonces $$\operatorname{mSpec}(R) \neq \emptyset$$. Además,

$$
\bigcup_{\mathfrak{m} \in \operatorname{mSpec}(R)} \mathfrak{m} = R \setminus R^{\times}.
$$

***Prueba:*** Como $$R \neq \{0\}$$, el ideal $$(0)$$ es propio, y por el teorema de Krull existe un ideal maximal que lo contiene; entonces $$\operatorname{mSpec}(R) \neq \emptyset$$.

“$$\supseteq$$”: Si $$x \in R \setminus R^{\times}$$, entonces $$(x) \neq R$$: en caso contrario $$1 \in (x)$$, es decir, $$1 = r x$$ para algún $$r \in R$$, y $$x$$ sería una unidad. Por Krull, existe $$\mathfrak{m}$$ maximal tal que $$(x) \subseteq \mathfrak{m}$$. Concluya que $$x \in \bigcup_{\mathfrak{m} \in \operatorname{mSpec}(R)} \mathfrak{m}$$.

“$$\subseteq$$”: Si $$x \in \mathfrak{m}$$ con $$\mathfrak{m}$$ maximal, entonces $$x \notin R^{\times}$$: si $$x$$ fuese una unidad, tendríamos $$1 = x^{-1} x \in \mathfrak{m}$$ por absorción, de donde $$\mathfrak{m} = R$$, lo que contradice $$\mathfrak{m} \neq R$$.

### Definición (Anillo local)

Un anillo conmutativo $$R \neq \{0\}$$ es *local* si posee exactamente un ideal maximal.

### Corolario (Caracterización de los anillos locales)

Si $$R \neq \{0\}$$ es un anillo conmutativo, entonces $$R$$ es local si y solo si $$R \setminus R^{\times}$$ es un ideal.

***Prueba:*** Ejercicio.

### Definición (Radical de Jacobson)

Sea $$R \neq \{0\}$$ un anillo conmutativo. Definimos el *radical de Jacobson* como

$$
\operatorname{Rad}(R) = \bigcap_{\mathfrak{m} \in \operatorname{mSpec}(R)} \mathfrak{m}.
$$

### Ejercicio (Caracterización del radical de Jacobson)

Muestre que $$x \in \operatorname{Rad}(R)$$ si y solo si $$1 - x y \in R^{\times}$$ para cada $$y \in R$$.
{% endraw %}
