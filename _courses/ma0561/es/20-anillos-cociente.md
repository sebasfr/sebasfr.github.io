---
layout: chapter
course: ma0561
chapter: 20
title: "Anillos cociente"
slug: 20-anillos-cociente
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/20-anillos-cociente/
---

{% raw %}
## La congruencia módulo un ideal y el cociente

### Definición (La relación de congruencia módulo un ideal)

Sea $$R$$ un anillo e $$I$$ un $$R$$-ideal. Para $$a, b \in R$$, definamos la relación $$\sim_{I}$$ tal que

$$
a \sim_{I} b \iff a - b \in I.
$$

### Lema (La congruencia módulo un ideal es de equivalencia)

La relación $$\sim_{I}$$ es una relación de equivalencia en $$R$$.

***Prueba:*** Verificamos las tres propiedades:

1. *Reflexividad:* $$a \sim_{I} a$$, pues $$a - a = 0 \in I$$.
2. *Simetría:* si $$a \sim_{I} b$$, entonces $$a - b \in I$$; como $$I$$ es cerrado bajo inversos aditivos, $$b - a = -(a - b) \in I$$, es decir, $$b \sim_{I} a$$.
3. *Transitividad:* si $$a \sim_{I} b$$ y $$b \sim_{I} c$$, entonces $$a - b \in I$$ y $$b - c \in I$$. Como $$I$$ es cerrado bajo sumas,

    $$
    a - c = (a - b) + (b - c) \in I,
    $$

    es decir, $$a \sim_{I} c$$.

### Nota (Las clases de equivalencia son clases laterales)

Sea $$R/I = \{ [a]_{I} :\ a \in R \}$$ el conjunto de clases de equivalencia de $$\sim_{I}$$. Entonces

$$
\begin{aligned}
[a]_{I} &= \{ b \in R :\ a \sim_{I} b \} = \{ b \in R :\ a - b \in I \} \\
&= \{ b \in R :\ \exists x \in I\ (x = a - b) \} = \{ b \in R :\ \exists x \in I\ (b = a - x) \} \\
&= \{ a - x :\ x \in I \} = a + I,
\end{aligned}
$$

donde la última igualdad usa que $$I$$ es cerrado bajo inversos aditivos, de modo que $$\{-x : x \in I\} = I$$. **Notación:** $$[a]_{I} = a + I$$.

### Definición (Las operaciones del anillo cociente)

Definimos $$\tilde{+}$$ en $$R/I$$ tal que

$$
(a + I)\ \tilde{+}\ (b + I) = (a + b) + I.
$$

El ideal $$I$$ es el “$$0$$” en $$R/I$$ (es decir, $$[0]_{I}$$). Definimos $$\tilde{\cdot}$$ en $$R/I$$ tal que

$$
(a + I)\ \tilde{\cdot}\ (b + I) = (a \cdot b) + I.
$$

La clase $$1_{R} + I$$ es el “$$1$$” en $$R/I$$.

### Teorema (El cociente es un anillo)

$$R/I$$ es un anillo con estas operaciones. Se llama el *anillo cociente* de $$R$$ por $$I$$.

***Prueba:*** La parte delicada es verificar que $$\tilde{+}$$ y $$\tilde{\cdot}$$ están bien definidas, es decir, que no dependen de los representantes. Suponga que $$a + I = a' + I$$ y $$b + I = b' + I$$, o sea, $$a - a' \in I$$ y $$b - b' \in I$$. Para la suma,

$$
(a + b) - (a' + b') = (a - a') + (b - b') \in I,
$$

de modo que $$(a + b) + I = (a' + b') + I$$. Para el producto, sumamos y restamos $$a' b$$:

$$
a b - a' b' = (a - a') b + a' (b - b'),
$$

y aquí $$(a - a') b \in I$$ por la absorción por la derecha y $$a' (b - b') \in I$$ por la absorción por la izquierda; entonces $$a b - a' b' \in I$$, es decir, $$(a b) + I = (a' b') + I$$. Aquí se usa de manera esencial que $$I$$ es un ideal bilátero.

Los axiomas de anillo se heredan de $$R$$ operando con representantes; por ejemplo,

$$
\big( (a + I)\, \tilde{\cdot}\, (b + I) \big)\, \tilde{\cdot}\, (c + I) = (a b) c + I = a (b c) + I = (a + I)\, \tilde{\cdot}\, \big( (b + I)\, \tilde{\cdot}\, (c + I) \big),
$$

y de igual forma la asociatividad y conmutatividad de $$\tilde{+}$$, la distributividad, los neutros $$I = 0 + I$$ y $$1 + I$$, y el inverso aditivo $$(-a) + I$$.

### Definición (La proyección canónica)

Si $$R$$ es un anillo e $$I$$ es un $$R$$-ideal, sea $$\pi_{I} : R \to R/I$$ tal que $$a \mapsto a + I$$, la *proyección canónica* de $$R$$ en $$R/I$$.

### Proposición (Propiedades de la proyección canónica)

La proyección canónica $$\pi_{I}$$ es sobreyectiva y $$\operatorname{Ker}(\pi_{I}) = I$$.

***Prueba:*** La sobreyectividad es inmediata: toda clase $$a + I \in R/I$$ es $$\pi_{I}(a)$$. Para el núcleo, tenemos las dos contenciones:

$$
\text{si } x \in I \implies \pi_{I}(x) = x + I = I = [0]_{I} \implies x \in \operatorname{Ker}(\pi_{I}),
$$

pues $$x - 0 = x \in I$$; y recíprocamente,

$$
\text{si } x \in \operatorname{Ker}(\pi_{I}) \implies \pi_{I}(x) = x + I = I \implies x \in I,
$$

pues $$x = x - 0 \in I$$. Concluimos que $$\operatorname{Ker}(\pi_{I}) = I$$.

## Ejemplos de cocientes

### Ejemplo (Los enteros módulo $$n$$ como cociente)

$$\mathbb{Z}/(n) = \mathbb{Z}_{n}$$.

### Ejemplo (El cociente $$\mathbb{Z}[x]/(x^{2})$$)

Si $$p(x) + (x^{2}) \in \mathbb{Z}[x]/(x^{2})$$, entonces existen únicos $$a, b \in \mathbb{Z}$$ tales que

$$
[p(x)]_{(x^{2})} = [a + b x]_{(x^{2})}.
$$

Para la existencia, escriba $$p(x) = a + b x + x^{2} q(x)$$ con $$q(x) \in \mathbb{Z}[x]$$; entonces $$p(x) - (a + bx) = x^{2} q(x) \in (x^{2})$$. Probemos ahora la unicidad. Sean $$a_{0}, a_{1}, b_{0}, b_{1} \in \mathbb{Z}$$ tales que

$$
[a_{0} + a_{1} x]_{(x^{2})} = [b_{0} + b_{1} x]_{(x^{2})}.
$$

Entonces

$$
(a_{0} - b_{0}) + (a_{1} - b_{1}) x \in (x^{2}).
$$

Pero todo elemento no nulo de $$(x^{2}) = x^{2} \cdot \mathbb{Z}[x]$$ tiene grado al menos $$2$$, es decir, sus coeficientes de grados $$0$$ y $$1$$ son nulos; entonces $$a_{0} = b_{0}$$ y $$a_{1} = b_{1}$$. Concluimos que

$$
\mathbb{Z}[x]/(x^{2}) = \{ [a + b x]_{(x^{2})} :\ a, b \in \mathbb{Z} \}.
$$

Note además que

$$
[3x]_{(x^{2})} \cdot [5x]_{(x^{2})} = [15 x^{2}]_{(x^{2})} = [0]_{(x^{2})},
$$

de modo que $$\mathbb{Z}[x]/(x^{2})$$ tiene divisores de cero.

### Ejercicio (Divisores de cero y unidades de $$\mathbb{Z}[x]/(x^{2})$$)

Muestre que los divisores de cero de $$\mathbb{Z}[x]/(x^{2})$$ son $$\{ [b x] :\ b \neq 0 \}$$ y que las unidades son $$\{ [\pm 1 + b x] :\ b \in \mathbb{Z} \}$$.

### Ejemplo (Un cociente de los enteros gaussianos)

Sea $$\mathbb{Z}[i] = \{ a + b i :\ a, b \in \mathbb{Z} \}$$. Entonces $$\mathbb{Z}[i]/(1 + i) = \{ [0], [1] \}$$ (ejercicio).

### Ejemplo (El cociente $$\mathbb{R}[x]/(x^{2} + 1)$$)

Sea $$R = \mathbb{R}[x]/(x^{2} + 1)$$ y $$\alpha = [x]$$. Entonces

$$
\alpha^{2} = [x^{2}] = [-1],
$$

pues $$x^{2} - (-1) = x^{2} + 1 \in (x^{2} + 1)$$. Es decir, en $$R$$ hay solución a la ecuación “$$t^{2} + 1 = 0$$”. Veremos que $$R \cong \mathbb{C}$$.

## El teorema de correspondencia

### Definición (Cociente de un subconjunto)

Sea $$R$$ un anillo, $$I$$ un $$R$$-ideal y $$S \subseteq R$$ (solo un subconjunto). Definimos

$$
S/I := \{ s + I :\ s \in S \} \subseteq R/I.
$$

### Teorema (Correspondencia entre ideales y subanillos del cociente)

La aplicación $$S \mapsto S/I$$ induce biyecciones que preservan la inclusión entre los siguientes conjuntos:

1. $$\{ J :\ J \text{ ideal de } R \text{ tal que } J \supseteq I \} \to \{ \text{ideales de } R/I \}$$;
2. $$\{ \text{subanillos de } R \text{ que contienen a } I \} \to \{ \text{subanillos de } R/I \}$$.

En ambos casos la función inversa es $$A \mapsto \{ r \in R :\ r + I \in A \}$$.

***Prueba:*** Probamos el caso de ideales; el de subanillos es idéntico, usando el criterio de subanillo en lugar de la definición de ideal. Escriba $$\Phi(J) = J/I$$ y $$\Psi(A) = \{ r \in R :\ r + I \in A \}$$.

*$$\Phi$$ llega a donde debe.* Si $$J \supseteq I$$ es un ideal de $$R$$, entonces $$J/I$$ es un ideal de $$R/I$$: es no vacío; es cerrado bajo sumas, pues $$(j + I) + (j' + I) = (j + j') + I$$ con $$j + j' \in J$$; y absorbe productos, pues $$(r + I)(j + I) = r j + I$$ con $$r j \in J$$ por la absorción de $$J$$ en $$R$$.

*$$\Psi$$ llega a donde debe.* Si $$A$$ es un ideal de $$R/I$$, entonces $$\Psi(A)$$ es un ideal de $$R$$: si $$r, r' \in \Psi(A)$$, entonces $$(r + r') + I = (r + I) + (r' + I) \in A$$, así que $$r + r' \in \Psi(A)$$; y si $$s \in R$$, entonces $$(s r) + I = (s + I)(r + I) \in A$$ por la absorción de $$A$$. Además $$I \subseteq \Psi(A)$$: si $$x \in I$$, entonces $$x + I = I = [0] \in A$$, pues todo ideal contiene al cero.

*Son mutuamente inversas.* Primero, $$\Psi(\Phi(J)) = \{ r :\ r + I \in J/I \} = J$$: la contención “$$\supseteq$$” es clara, y si $$r + I = j + I$$ para algún $$j \in J$$, entonces $$r - j \in I \subseteq J$$, de donde $$r = j + (r - j) \in J$$. Segundo, $$\Phi(\Psi(A)) = \{ r + I :\ r + I \in A \} = A$$, pues todo elemento de $$A$$ es una clase $$r + I$$ para algún $$r \in R$$.

*Preservan la inclusión.* Si $$J \subseteq J'$$, entonces $$J/I \subseteq J'/I$$ directamente; y si $$A \subseteq A'$$, entonces $$\Psi(A) \subseteq \Psi(A')$$ directamente. (En el caso de subanillos, $$\Psi(B) \supseteq I$$ vale porque $$[0] \in B$$, y la cuenta de inversas usa $$I \subseteq S$$ de la misma manera.)
{% endraw %}
