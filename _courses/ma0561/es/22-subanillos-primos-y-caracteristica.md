---
layout: chapter
course: ma0561
chapter: 22
title: "Subanillos primos y característica"
slug: 22-subanillos-primos-y-caracteristica
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/22-subanillos-primos-y-caracteristica/
---

{% raw %}
## El subanillo primo y el cuerpo primo

### Definición (Cuerpo primo)

Sea $$F$$ un cuerpo. Definimos el *cuerpo primo* de $$F$$ como la intersección de todos los subcuerpos de $$F$$.

### Definición (Subanillo primo)

Sea $$R$$ un anillo. El *subanillo primo* (o *anillo primo*) de $$R$$ es la intersección de todos los subanillos de $$R$$; es decir, el subanillo más pequeño de $$R$$.

### Nota (El anillo primo de un cuerpo vive en su cuerpo primo)

Si $$(F, +, \cdot)$$ es un cuerpo, entonces es un anillo; como todo subcuerpo de $$F$$ es en particular un subanillo, el anillo primo de $$F$$ es un subanillo del cuerpo primo de $$F$$.

### Ejemplo (Subanillos primos conocidos)

Los siguientes ejemplos ilustran la definición:

1. $$\mathbb{Z}$$ es el subanillo primo de $$\mathbb{Z}$$, y $$\mathbb{Z}_{n}$$ es el subanillo primo de $$\mathbb{Z}_{n}$$.
2. Sea $$R$$ un anillo y considere $$M_{n \times n}(R)$$. Entonces $$\{ z \cdot I_{n} :\ z \in \mathbb{Z} \}$$ es el anillo primo de $$M_{n \times n}(R)$$.
3. Si $$R_{1} \subseteq R_{2}$$ son anillos (respectivamente, cuerpos), entonces $$R_{1}$$ y $$R_{2}$$ tienen el mismo anillo primo (respectivamente, cuerpo primo).

### Nota (La cadena de anillos numéricos)

Note que $$\mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R} \subseteq \mathbb{C} \subseteq \mathbb{H}$$ (como anillos):

- todos tienen el mismo anillo primo, $$\mathbb{Z}$$;
- $$\mathbb{Q}$$ es el cuerpo primo de $$\mathbb{Q}$$, $$\mathbb{R}$$ y $$\mathbb{C}$$.

## La característica

### Definición (Característica de un anillo)

Si $$R$$ es un anillo y $$R_{0}$$ es su anillo primo, definimos

$$
\operatorname{char}(R) =
\begin{cases}
|R_{0}| & \text{si } R_{0} \text{ es finito}, \\
0 & \text{si no}.
\end{cases}
$$

### Teorema (El subanillo primo es $$\mathbb{Z}$$ o $$\mathbb{Z}_{n}$$)

Sea $$R$$ un anillo.

1. El subanillo primo $$R_{0}$$ de $$R$$ es isomorfo a $$\mathbb{Z}$$ o a $$\mathbb{Z}_{n}$$, y en tal caso

    $$
    \operatorname{char}(R) =
    \begin{cases}
    n & \text{si } R_{0} \cong \mathbb{Z}_{n}, \\
    0 & \text{si } R_{0} \cong \mathbb{Z}.
    \end{cases}
    $$
2. Si $$D$$ es un dominio entero, entonces $$\operatorname{char}(D)$$ es $$0$$ o un número primo $$p$$.

***Prueba:*** *Parte 1.* Sea $$R_{0}$$ el anillo primo de $$R$$ y sea $$f_{R} : \mathbb{Z} \longrightarrow R$$ tal que $$n \longmapsto n \cdot 1_{R}$$, que es un homomorfismo de anillos (de hecho, el único; véase el ejercicio sobre homomorfismos desde $$\mathbb{Z}$$). Afirmamos que $$\operatorname{Im}(f_{R}) = R_{0}$$: por una parte, $$\operatorname{Im}(f_{R})$$ es un subanillo de $$R$$; por otra, todo subanillo $$S$$ de $$R$$ contiene a $$1_{R}$$ y es cerrado bajo sumas y restas, así que contiene a $$n \cdot 1_{R}$$ para todo $$n \in \mathbb{Z}$$, es decir, $$\operatorname{Im}(f_{R}) \subseteq S$$. Entonces $$\operatorname{Im}(f_{R})$$ es el subanillo más pequeño de $$R$$, o sea, $$\operatorname{Im}(f_{R}) = R_{0}$$. Por el primer teorema del isomorfismo,

$$
R_{0} = \operatorname{Im}(f_{R}) \cong \mathbb{Z}/\operatorname{Ker}(f_{R}).
$$

Note que $$\operatorname{Ker}(f_{R})$$ es un ideal de $$\mathbb{Z}$$, y como $$\mathbb{Z}$$ es un DIP, tenemos que $$\operatorname{Ker}(f_{R}) = (n)$$ con $$n \in \mathbb{N}$$. Si $$n = 0$$, entonces $$\operatorname{Ker}(f_{R}) = \{0\}$$, de modo que $$R_{0} \cong \mathbb{Z}$$, que es infinito, y $$\operatorname{char}(R) = 0$$. Si $$n \neq 0$$, entonces $$R_{0} \cong \mathbb{Z}/(n) \cong \mathbb{Z}_{n}$$, que tiene $$n$$ elementos, y $$\operatorname{char}(R) = n$$.

*Parte 2.* Fue probada en la tarea; queda como ejercicio.

## El homomorfismo de Frobenius y el pequeño teorema de Fermat

### Teorema (Frobenius: elevar a la $$p$$ es un homomorfismo)

Sea $$R$$ un anillo conmutativo tal que $$\operatorname{char}(R) = p > 0$$ con $$p$$ primo. Entonces $$\varphi : R \to R$$ tal que $$x \mapsto x^{p}$$ es un homomorfismo. En particular,

$$
(x + y)^{p} = x^{p} + y^{p} \quad \text{para todos } x, y \in R.
$$

***Prueba:*** Note primero que $$\varphi(1) = 1^{p} = 1$$, y que, como $$R$$ es conmutativo,

$$
\varphi(x \cdot y) = (x y)^{p} = x^{p} y^{p} = \varphi(x) \cdot \varphi(y).
$$

Falta probar que $$\varphi(x + y) = \varphi(x) + \varphi(y)$$, es decir, que $$(x + y)^{p} = x^{p} + y^{p}$$.

Sean $$a, b \in R$$. Por el teorema del binomio de Newton, válido en anillos conmutativos,

$$
(a + b)^{p} = \sum_{i=0}^{p} \binom{p}{i} a^{i} b^{p-i},
$$

donde $$\binom{p}{i} a^{i} b^{p-i}$$ denota el múltiplo entero correspondiente. Afirmamos que si $$0 < i < p$$, entonces $$\binom{p}{i}$$ es múltiplo de $$p$$: de la identidad

$$
i!\,(p - i)!\, \binom{p}{i} = p!
$$

vemos que $$p$$ divide al lado derecho; pero $$p$$ es primo y no divide a $$i!$$ ni a $$(p-i)!$$, pues todos sus factores son menores que $$p$$; entonces $$p \mid \binom{p}{i}$$. Ahora, como $$\operatorname{char}(R) = p$$, tenemos que $$p \cdot 1_{R} = 0$$, y si $$\binom{p}{i} = p \cdot t$$ con $$t \in \mathbb{Z}$$, entonces

$$
\binom{p}{i} \cdot a^{i} b^{p-i} = \big( \binom{p}{i} \cdot 1_{R} \big)\, a^{i} b^{p-i} = \big( t \cdot (p \cdot 1_{R}) \big)\, a^{i} b^{p-i} = 0.
$$

Es decir, en la suma binomial solo sobreviven los términos $$i = 0$$ e $$i = p$$, de modo que $$(a + b)^{p} = a^{p} + b^{p}$$.

### Nota (Frobenius en cuerpos finitos y sus iteradas)

Tres observaciones sobre el homomorfismo anterior:

1. $$\varphi$$ es llamado el *homomorfismo de Frobenius*.
2. Si $$R$$ es un cuerpo finito, entonces $$\operatorname{Ker}(\varphi) = \{0\}$$ (el núcleo es un ideal propio de un cuerpo), de modo que $$\varphi$$ es inyectiva. Como $$R$$ es finito, $$\varphi$$ es también sobreyectiva, y entonces $$\varphi$$ es un automorfismo.
3. $$\varphi^{n} : R \to R$$, $$x \mapsto x^{p^{n}}$$, es un homomorfismo para todo $$n \in \mathbb{N}$$, por ser composición de homomorfismos. En particular,

    $$
    (a + b)^{p^{n}} = a^{p^{n}} + b^{p^{n}} \quad \text{para todos } a, b \in R,\ n \in \mathbb{N}.
    $$

### Teorema (Pequeño teorema de Fermat)

Sea $$p$$ primo. Entonces $$n^{p} \equiv n \pmod{p}$$ para todo $$n > 0$$.

***Prueba:*** Procedemos por inducción sobre $$n$$. El caso base $$n = 1$$ es trivial, pues $$1^{p} = 1$$. Ahora, suponga como hipótesis inductiva que $$n^{p} \equiv n \pmod{p}$$ para algún $$n \in \mathbb{N}$$. El anillo $$\mathbb{Z}_{p}$$ es su propio anillo primo, así que $$\operatorname{char}(\mathbb{Z}_{p}) = p$$. Usando el homomorfismo de Frobenius en $$\mathbb{Z}_{p}$$ y la hipótesis inductiva, tenemos que

$$
(n + 1)^{p} = n^{p} + 1^{p} = n + 1 \pmod{p},
$$

lo que prueba el paso inductivo. Concluya el resultado.
{% endraw %}
