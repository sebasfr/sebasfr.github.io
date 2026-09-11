---
layout: chapter
course: ma0561
chapter: 21
title: "Homomorfismos de anillos"
slug: 21-homomorfismos-de-anillos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/21-homomorfismos-de-anillos/
---

{% raw %}
## Definiciones y primeros ejemplos

### Definición (Homomorfismo de anillos)

Sean $$R, S$$ anillos. Entonces $$\varphi : R \to S$$ es un *homomorfismo de anillos* si:

1. $$\varphi(a +_{R} b) = \varphi(a) +_{S} \varphi(b)$$ para todos $$a, b \in R$$;
2. $$\varphi(a \cdot_{R} b) = \varphi(a) \cdot_{S} \varphi(b)$$ para todos $$a, b \in R$$;
3. $$\varphi(1_{R}) = 1_{S}$$.

### Nota (Los homomorfismos preservan el cero)

La definición implica que $$\varphi(0_{R}) = 0_{S}$$, pues

$$
\varphi(0_{R}) = \varphi(0_{R} + 0_{R}) = \varphi(0_{R}) +_{S} \varphi(0_{R}) \implies 0_{S} = \varphi(0_{R}),
$$

cancelando $$\varphi(0_{R})$$ en el grupo $$(S, +)$$.

### Definición (Monomorfismos, isomorfismos y automorfismos)

Sea $$\varphi : R \to S$$ un homomorfismo de anillos.

- Si $$\varphi$$ es inyectiva, entonces $$\varphi$$ es un *monomorfismo*.
- Si $$\varphi$$ es biyectiva, entonces $$\varphi$$ es un *isomorfismo*.
- Si $$\varphi$$ es biyectiva y $$R = S$$, entonces $$\varphi$$ es un *automorfismo*.

Si $$R$$ y $$S$$ son anillos tales que existe un isomorfismo $$\varphi : R \to S$$, decimos que $$R$$ y $$S$$ son *isomorfos* y escribimos $$R \cong S$$.

### Ejemplo ($$\mathbb{R}[x]/(x^{2}+1)$$ es isomorfo a $$\mathbb{C}$$)

Ya vimos que $$\mathbb{R}[x]/(x^{2} + 1) = \{ [a + b x] :\ a, b \in \mathbb{R} \}$$ (el argumento de forma normal es el mismo que para $$\mathbb{Z}[x]/(x^{2})$$). La función

$$
\varphi : \mathbb{C} \longrightarrow \mathbb{R}[x]/(x^{2} + 1), \qquad a + i b \longmapsto [a + b x],
$$

es un isomorfismo (ejercicio). En particular, $$\mathbb{R}[x]/(x^{2}+1) \cong \mathbb{C}$$.

### Lema (Los homomorfismos preservan unidades)

Sean $$R, S$$ anillos y $$\varphi : R \to S$$ un homomorfismo. Si $$a \in R^{\times}$$, entonces $$\varphi(a) \in S^{\times}$$ y $$\varphi(a^{-1}) = (\varphi(a))^{-1}$$.

***Prueba:*** Sea $$a \in R^{\times}$$ con inverso $$a^{-1} \in R$$, de modo que $$a \cdot a^{-1} = 1_{R} = a^{-1} \cdot a$$. Aplicando $$\varphi$$,

$$
\varphi(a \cdot a^{-1}) = \varphi(1_{R}) \implies \varphi(a) \cdot_{S} \varphi(a^{-1}) = 1_{S} = \varphi(a^{-1}) \cdot_{S} \varphi(a),
$$

donde la segunda igualdad se obtiene aplicando $$\varphi$$ a $$a^{-1} \cdot a = 1_{R}$$. Entonces $$\varphi(a^{-1})$$ es un inverso multiplicativo de $$\varphi(a)$$, es decir, $$\varphi(a^{-1}) = (\varphi(a))^{-1}$$ y $$\varphi(a) \in S^{\times}$$.

### Ejemplo (La inclusión de un subanillo y la reducción módulo $$n$$)

Dos ejemplos básicos de homomorfismos:

1. Sea $$S$$ un subanillo de $$R$$. La función $$\varphi : S \to R$$ tal que $$x \mapsto x$$ es un monomorfismo.
2. La función $$\varphi : \mathbb{Z} \to \mathbb{Z}_{n}$$ tal que $$x \mapsto [x]$$ es un homomorfismo.

## Núcleo e imagen

### Definición (Núcleo e imagen de un homomorfismo)

Sean $$R, S$$ anillos y $$\varphi : R \to S$$ un homomorfismo.

1. $$\operatorname{Ker}(\varphi) = \{ x \in R :\ \varphi(x) = 0_{S} \} \subseteq R$$;
2. $$\operatorname{Im}(\varphi) = \{ \varphi(x) :\ x \in R \} = \varphi(R) \subseteq S$$.

### Nota (El núcleo es un ideal y detecta la inyectividad)

$$\operatorname{Ker}(\varphi)$$ es un $$R$$-ideal. Además, $$\operatorname{Ker}(\varphi) = \{0_{R}\}$$ si y solo si $$\varphi$$ es inyectiva.

### Nota (Composición de homomorfismos)

La composición de homomorfismos es un homomorfismo, y el inverso de un isomorfismo es un isomorfismo. Además,

$$
\varphi_{1} \circ (\varphi_{2} \circ \varphi_{3}) = (\varphi_{1} \circ \varphi_{2}) \circ \varphi_{3}.
$$

### Ejemplo (La reducción de coeficientes módulo $$n$$ y su núcleo)

Sea $$r_{n} : \mathbb{Z}[x] \longrightarrow \mathbb{Z}_{n}[x]$$ tal que

$$
r_{n}(a_{0} + a_{1} x + \dots + a_{m} x^{m}) = [a_{0}] + [a_{1}] x + \dots + [a_{m}] x^{m}.
$$

La función $$r_{n}$$ es un homomorfismo (ejercicio) y es sobreyectiva. Además, $$\operatorname{Ker}(r_{n}) = (n\mathbb{Z})[x]$$, pues

$$
\begin{aligned}
a_{0} + a_{1} x + \dots + a_{m} x^{m} \in \operatorname{Ker}(r_{n})
&\iff [a_{i}] = [0] \quad \forall i \in \{0, 1, \dots, m\} \\
&\iff n \mid a_{i} \quad \forall i \in \{0, 1, \dots, m\}.
\end{aligned}
$$

### Ejemplo (El homomorfismo de evaluación y su núcleo)

Sea $$a \in \mathbb{R}$$ y sea $$\varphi_{a} : \mathbb{R}[x] \to \mathbb{R}$$ tal que $$\varphi_{a}(p(x)) = p(a)$$. Entonces $$\varphi_{a}$$ es un homomorfismo (ejercicio). Su núcleo es

$$
\begin{aligned}
\operatorname{Ker}(\varphi_{a}) &= \{ p(x) \in \mathbb{R}[x] :\ p(a) = 0 \} \\
&= \{ p(x) \in \mathbb{R}[x] :\ \exists q(x) \in \mathbb{R}[x]\ \big( p(x) = (x - a) \cdot q(x) \big) \} \\
&= \{ (x - a) \cdot q(x) :\ q(x) \in \mathbb{R}[x] \} \\
&= (x - a) \cdot \mathbb{R}[x] \neq \{ 0_{\mathbb{R}[x]} \},
\end{aligned}
$$

donde la segunda igualdad es el teorema de factorización de la raíz.

### Lema (Propiedades invariantes bajo isomorfismos)

Sean $$R, S$$ anillos y $$\varphi : R \to S$$ un isomorfismo. Entonces:

1. $$R$$ es conmutativo $$\iff$$ $$S$$ es conmutativo;
2. $$x \in R^{\times} \iff \varphi(x) \in S^{\times}$$;
3. $$R$$ es un cuerpo $$\iff$$ $$S$$ es un cuerpo;
4. $$x \in R$$ es divisor de cero $$\iff$$ $$\varphi(x) \in S$$ es divisor de cero.

***Prueba:*** Ejercicio.

### Ejemplo ($$\mathbb{R} \times \mathbb{R}$$ no es isomorfo a $$\mathbb{C}$$ como anillo)

Sea $$\varphi : \mathbb{R} \times \mathbb{R} \to \mathbb{C}$$ tal que $$(a, b) \mapsto a + i b$$. Es un isomorfismo de grupos abelianos, pero no de anillos, pues $$\mathbb{C}$$ es un dominio entero y $$\mathbb{R} \times \mathbb{R}$$ no lo es (tiene divisores de cero).

### Ejemplo ($$\mathbb{Q}(i)$$ no es isomorfo a $$\mathbb{Q}$$)

Sea $$\mathbb{Q}(i) = \{ a + i b :\ a, b \in \mathbb{Q} \}$$. Entonces $$\mathbb{Q}(i)$$ es un cuerpo y $$\mathbb{Q}(i) \not\cong \mathbb{Q}$$. En efecto, existe $$\alpha \in \mathbb{Q}(i)$$ tal que $$\alpha^{2} = -1$$ (a saber, $$\alpha = i$$), es decir, tal que $$\alpha^{2} + 1 = 0$$. Si $$f : \mathbb{Q}(i) \to \mathbb{Q}$$ fuese un isomorfismo, tendríamos que

$$
f(\alpha^{2} + 1) = f(0) = 0 \implies (f(\alpha))^{2} + f(1) = 0 \implies (f(\alpha))^{2} + 1 = 0.
$$

Esto implicaría que en $$\mathbb{Q}$$ la ecuación $$x^{2} + 1 = 0$$ tiene solución, lo cual es imposible, pues $$x^{2} \geq 0$$ para todo $$x \in \mathbb{Q}$$. Concluimos que no existe tal isomorfismo.

### Ejemplo (El único automorfismo de $$\mathbb{Z}$$ es la identidad)

$$\operatorname{Aut}(\mathbb{Z}) = \{\mathrm{id}_{\mathbb{Z}}\}$$. En efecto, sea $$f \in \operatorname{Aut}(\mathbb{Z})$$. Entonces

$$
\begin{aligned}
f(0) &= 0, \\
f(1) &= 1, \\
f(2) &= f(1) + f(1) = 2, \\
&\ \,\vdots \\
f(n) &= n \quad \text{si } n \in \mathbb{N},
\end{aligned}
$$

donde cada paso usa la aditividad: $$f(n + 1) = f(n) + f(1)$$. En general, $$f(-n) = -f(n) = -n$$ si $$n > 0$$, pues los homomorfismos preservan inversos aditivos. Concluimos que $$f = \mathrm{id}_{\mathbb{Z}}$$.

### Ejemplo (La conjugación es un automorfismo de matrices)

Sea $$U \in GL_{n}(\mathbb{R})$$. La función $$\varphi : M_{n \times n}(\mathbb{R}) \longrightarrow M_{n \times n}(\mathbb{R})$$ dada por $$A \longmapsto U \cdot A \cdot U^{-1}$$ es un automorfismo.

## Extensión y contracción de ideales

### Lema (La imagen inversa de un ideal es un ideal)

Sean $$R, S$$ anillos, $$\varphi : R \to S$$ un homomorfismo y $$J \subseteq S$$ un $$S$$-ideal. Entonces $$\varphi^{-1}(J)$$ es un $$R$$-ideal.

***Prueba:*** Ejercicio.

### Nota (La imagen directa de un ideal no es necesariamente un ideal)

Si $$I \subseteq R$$ es un $$R$$-ideal, no necesariamente $$\varphi(I)$$ es un ideal de $$S$$. ¿Por qué?

### Definición (Extensión y contracción de ideales)

Sea $$\varphi : R \to S$$ un homomorfismo de anillos.

1. Sea $$I$$ un $$R$$-ideal. Defina la *extensión* de $$I$$, denotada $$I^{e}$$, como el ideal más pequeño de $$S$$ que contiene a $$\varphi(I)$$.
2. Si $$J \subseteq S$$ es un $$S$$-ideal, la *contracción* de $$J$$, denotada $$J^{c}$$, es $$\varphi^{-1}(J)$$.

### Proposición (Contracciones y extensiones iteradas)

Sea $$\varphi : R \to S$$ un homomorfismo de anillos, $$I \subseteq R$$ un $$R$$-ideal y $$J \subseteq S$$ un $$S$$-ideal. Entonces:

1. $$I \subseteq (I^{e})^{c}$$ y $$J \supseteq (J^{c})^{e}$$;
2. $$I^{e} = I^{ece}$$;
3. $$J^{c} = J^{cec}$$.

***Prueba:*** Usaremos dos monotonías. Si $$I_{1} \subseteq I_{2}$$ son $$R$$-ideales, entonces $$I_{1}^{e} \subseteq I_{2}^{e}$$: en efecto, $$\varphi(I_{1}) \subseteq \varphi(I_{2}) \subseteq I_{2}^{e}$$, y como $$I_{1}^{e}$$ es el ideal más pequeño que contiene a $$\varphi(I_{1})$$, tenemos que $$I_{1}^{e} \subseteq I_{2}^{e}$$. Si $$J_{1} \subseteq J_{2}$$ son $$S$$-ideales, entonces $$J_{1}^{c} = \varphi^{-1}(J_{1}) \subseteq \varphi^{-1}(J_{2}) = J_{2}^{c}$$, directamente.

Para (a): si $$x \in I$$, entonces $$\varphi(x) \in \varphi(I) \subseteq I^{e}$$, así que $$x \in \varphi^{-1}(I^{e}) = (I^{e})^{c}$$; es decir, $$I \subseteq I^{ec}$$. Por otra parte, $$\varphi(J^{c}) = \varphi(\varphi^{-1}(J)) \subseteq J$$, y como $$J$$ es un ideal que contiene a $$\varphi(J^{c})$$, el ideal más pequeño con esa propiedad satisface $$(J^{c})^{e} \subseteq J$$.

Para (b): aplicando la primera parte de (a) al ideal $$I$$ y luego la monotonía de la extensión, $$I \subseteq I^{ec}$$ implica $$I^{e} \subseteq I^{ece}$$. Y aplicando la segunda parte de (a) con $$J = I^{e}$$, obtenemos $$I^{ece} = (I^{ec})^{e} = ((I^{e})^{c})^{e} \subseteq I^{e}$$. Ambas contenciones dan $$I^{e} = I^{ece}$$.

Para (c): aplicando la primera parte de (a) con $$I = J^{c}$$, obtenemos $$J^{c} \subseteq (J^{c})^{ec} = J^{cec}$$. Y aplicando la monotonía de la contracción a $$(J^{c})^{e} \subseteq J$$, obtenemos $$J^{cec} = ((J^{c})^{e})^{c} \subseteq J^{c}$$. Ambas contenciones dan $$J^{c} = J^{cec}$$.

### Ejemplo (Una extensión que crece: $$n\mathbb{Z}$$ dentro de $$\mathbb{Q}$$)

Sea $$\varphi : \mathbb{Z} \to \mathbb{Q}$$ tal que $$n \mapsto n$$, y sea $$n \neq 0, 1$$. Entonces $$\varphi(n) = n \in \mathbb{Q}^{\times}$$, y como el único ideal de $$\mathbb{Q}$$ que contiene una unidad es todo $$\mathbb{Q}$$, tenemos que

$$
\langle \varphi((n)) \rangle = \mathbb{Q} \implies (n\mathbb{Z})^{e} = \mathbb{Q} \implies ((n\mathbb{Z})^{e})^{c} = \mathbb{Q}^{c} = \varphi^{-1}(\mathbb{Q}) = \mathbb{Z}.
$$

Es decir, $$I = n\mathbb{Z} \subsetneq I^{ec} = \mathbb{Z}$$: la contracción de la extensión puede ser estrictamente mayor que el ideal original.

## Los teoremas de isomorfismo

### Teorema (Primer teorema del isomorfismo)

Sean $$R, S$$ anillos y $$f : R \to S$$ un homomorfismo de anillos. Sea $$F : R/\operatorname{Ker}(f) \to \operatorname{Im}(f)$$ tal que $$[a] \longmapsto f(a)$$. Entonces $$F$$ es un isomorfismo y, en particular,

$$
R/\operatorname{Ker}(f) \cong \operatorname{Im}(f).
$$

***Prueba:*** *$$F$$ está bien definida.* Si $$[a] = [b]$$, entonces $$a - b \in \operatorname{Ker}(f)$$, de modo que

$$
f(a - b) = 0 \implies f(a) = f(b) \implies F([a]) = F([b]).
$$

*$$F$$ es un homomorfismo.* Usando que $$f$$ lo es,

$$
\begin{aligned}
F([a] + [b]) &= F([a + b]) = f(a + b) = f(a) + f(b) = F([a]) + F([b]), \\
F([a] \cdot [b]) &= F([a \cdot b]) = f(a \cdot b) = f(a) \cdot f(b) = F([a]) \cdot F([b]), \\
F([1]) &= f(1) = 1.
\end{aligned}
$$

*$$F$$ es sobreyectiva.* Todo elemento de $$\operatorname{Im}(f)$$ es de la forma $$f(a) = F([a])$$ para algún $$a \in R$$.

*$$F$$ es inyectiva.* Calculamos el núcleo:

$$
F([a]) = 0_{S} \implies f(a) = 0_{S} \implies a \in \operatorname{Ker}(f) \implies [a] = [0],
$$

es decir, $$\operatorname{Ker}(F) = \{ 0_{R/\operatorname{Ker}(f)} \} = \{ [0] \}$$, y por lo tanto $$F$$ es inyectiva. Concluimos que $$F$$ es un isomorfismo.

### Ejemplo (El cociente de un producto por un factor)

Sean $$R, S$$ anillos y $$\pi : R \times S \to S$$ tal que $$(x, s) \mapsto s$$, que es un homomorfismo sobreyectivo. Su núcleo es

$$
\operatorname{Ker}(\pi) = R \times \{0\},
$$

pues $$\pi(x, s) = 0_{S}$$ si y solo si $$s = 0_{S}$$. Entonces, por el primer teorema del isomorfismo,

$$
(R \times S)/(R \times \{0\}) \cong S.
$$

### Ejemplo (El cociente de un producto por un producto de ideales)

Sean $$R, S$$ anillos, $$I$$ un $$R$$-ideal y $$J$$ un $$S$$-ideal. Entonces

$$
(R \times S)/(I \times J) \cong R/I \times S/J,
$$

usando el homomorfismo $$\varphi : R \times S \to R/I \times S/J$$ tal que $$(r, s) \mapsto (r + I, s + J)$$ (ejercicio).

### Teorema (Segundo teorema del isomorfismo)

Sea $$R$$ un anillo, $$S \leq R$$ un subanillo e $$I$$ un $$R$$-ideal. Entonces:

1. $$S \cap I$$ es un $$S$$-ideal;
2. $$S + I$$ es un subanillo de $$R$$;
3. $$I$$ es un $$(S + I)$$-ideal;
4. $$S/(S \cap I) \cong (S + I)/I$$.

***Prueba:*** Para (1): $$0 \in S \cap I$$, y $$S \cap I$$ es cerrado bajo sumas por serlo $$S$$ e $$I$$. Para la absorción, sean $$s \in S$$ y $$x \in S \cap I$$; entonces $$s x \in S$$, por ser $$S$$ cerrado bajo productos, y $$s x \in I$$, por la absorción de $$I$$ en $$R$$ (note que $$s \in S \subseteq R$$); es decir, $$s x \in S \cap I$$, y análogamente $$x s \in S \cap I$$.

Para (2): usamos el criterio de subanillo. Primero, $$1 = 1 + 0 \in S + I$$. Si $$s + x, s' + x' \in S + I$$, entonces

$$
(s + x) - (s' + x') = (s - s') + (x - x') \in S + I,
$$

y para el producto,

$$
(s + x)(s' + x') = s s' + (s x' + x s' + x x'),
$$

donde $$s s' \in S$$ y los tres términos del paréntesis están en $$I$$ por absorción; entonces el producto está en $$S + I$$.

Para (3): $$I \subseteq S + I$$ (pues $$x = 0 + x$$), $$I$$ es no vacío y cerrado bajo sumas, y la absorción por elementos de $$S + I \subseteq R$$ es un caso particular de la absorción de $$I$$ en $$R$$.

Para (4): considere $$\varphi : S \to (S + I)/I$$ dada por $$\varphi(s) = s + I$$, la restricción a $$S$$ de la proyección canónica. Es un homomorfismo, pues las operaciones de $$(S+I)/I$$ se calculan con representantes. Es sobreyectiva: toda clase de $$(S + I)/I$$ es de la forma $$(s + x) + I$$ con $$s \in S$$, $$x \in I$$, y $$(s + x) + I = s + I = \varphi(s)$$, pues $$x \in I$$. Su núcleo es

$$
\operatorname{Ker}(\varphi) = \{ s \in S :\ s + I = I \} = \{ s \in S :\ s \in I \} = S \cap I.
$$

Por el primer teorema del isomorfismo, $$S/(S \cap I) \cong \operatorname{Im}(\varphi) = (S + I)/I$$.

### Teorema (Tercer teorema del isomorfismo)

Sea $$R$$ un anillo y sean $$I \subseteq J \subseteq R$$ ideales. Entonces

$$
(R/I)\big/(J/I) \cong R/J.
$$

***Prueba:*** Considere $$f : R/I \to R/J$$ dada por $$f([x]_{I}) = [x]_{J}$$. Está bien definida: si $$[x]_{I} = [y]_{I}$$, entonces $$x - y \in I \subseteq J$$, de modo que $$[x]_{J} = [y]_{J}$$. Es un homomorfismo, pues las operaciones en ambos cocientes se calculan con representantes:

$$
f([x]_{I} + [y]_{I}) = f([x + y]_{I}) = [x + y]_{J} = [x]_{J} + [y]_{J},
$$

y análogamente para el producto; además $$f([1]_{I}) = [1]_{J}$$. Es sobreyectiva: toda clase $$[x]_{J}$$ es $$f([x]_{I})$$. Su núcleo es

$$
\operatorname{Ker}(f) = \{ [x]_{I} :\ [x]_{J} = [0]_{J} \} = \{ [x]_{I} :\ x \in J \} = J/I.
$$

Por el primer teorema del isomorfismo,

$$
(R/I)\big/(J/I) = (R/I)\big/\operatorname{Ker}(f) \cong \operatorname{Im}(f) = R/J.
$$
{% endraw %}
