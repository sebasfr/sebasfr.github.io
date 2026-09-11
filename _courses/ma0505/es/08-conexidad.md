---
layout: chapter
course: ma0505
chapter: 8
title: "Conexidad"
slug: 08-conexidad
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/08-conexidad/
---

{% raw %}
## Conjuntos disconexos y conexos

### Definición (Espacio disconexo y conexo)

Un espacio $$(X, d)$$ es *disconexo* si existen $$A, B$$ abiertos no vacíos tales que

$$
X = A \cup B, \quad A \cap B = \emptyset.
$$

Un espacio se dice *conexo* si no es disconexo. Equivalentemente, si $$X = A \cup B$$ con $$A, B$$ abiertos disjuntos, entonces $$A = X$$ o $$B = X$$.

### Definición (Disconexidad de un subconjunto)

$$E \subseteq X$$ es *disconexo* si existen $$A, B$$ abiertos en $$(X, d)$$ tales que

$$
E = (A \cap E) \cup (B \cap E), \quad (A \cap B) \cap E = \emptyset, \quad A \cap E \neq \emptyset \neq B \cap E.
$$

Es decir, $$E$$ se descompone en dos abiertos relativos no vacíos y disjuntos.

### Ejercicio (Caracterización de los abiertos en subespacios)

Dado $$E \subseteq X$$, defina $$d_{E} : E \times E \to \mathbb{R}$$ por $$(x, y) \mapsto d(x, y)$$. $$(E, d_{E})$$ es un espacio métrico. Pruebe que $$D \subseteq E$$ es abierto en $$(E, d_{E})$$ si y solo si existe $$O \subseteq X$$ abierto en $$(X, d)$$ tal que $$D = E \cap O$$.

## Conexos en R y propiedades

### Lema (Los intervalos abiertos son conexos)

Para $$a < b$$, el intervalo $$I = (a, b)$$ es conexo.

***Prueba:*** Suponga que $$I = (I \cap A) \cup (I \cap B)$$ con $$A, B$$ abiertos disjuntos y ambos cortes no vacíos. Sean $$s \in I \cap A$$, $$t \in I \cap B$$ con $$s < t$$; entonces $$[s, t] \subseteq I$$. Como $$s \in A$$ existe $$\delta_{1} > 0$$ con $$(s - \delta_{1}, s + \delta_{1}) \subseteq A$$, así $$[s, s + \delta_{1}/2] \subseteq [s, t] \cap A$$.

Defina $$u = \sup\{ x \in [s, t] : [s, x] \subseteq A\}$$. Por construcción $$s < u \leq t$$. Si $$u \in B$$, existe $$\delta_{2} > 0$$ con $$(u - \delta_{2}, u + \delta_{2}) \subseteq B \cap [s,t]$$; pero por propiedades del supremo existe $$w \in [s, t] \cap A$$ con $$u - \delta_{2} < w \leq u$$, lo cual implicaría $$w \in A \cap B$$ (pues $$w \in [s, t] \cap A$$ por la definición del supremo y $$w \in (u - \delta_{2}, u + \delta_{2}) \subseteq B$$), contradiciendo $$A \cap B = \emptyset$$. Si $$u \in A$$, existe $$\delta_{3} > 0$$ con $$[u, u + \delta_{3}] \subseteq [s, t] \cap A$$, lo que contradice la definición del supremo cuando $$u < t$$, o contradice $$t \in B$$ cuando $$u = t$$.

### Lema (Las funciones continuas preservan la conexidad)

Sea $$f : X \to Y$$ continua. Si $$E \subseteq X$$ es conexo, entonces $$f(E)$$ es conexo.

***Prueba:*** Suponga que existen $$B, C \subseteq Y$$ abiertos tales que $$f(E) = (f(E) \cap C) \cup (f(E) \cap B)$$ con ambos cortes no vacíos y disjuntos. Entonces

$$
\emptyset \neq f^{-1}(f(E) \cap C) = E \cap f^{-1}(C), \quad \emptyset \neq f^{-1}(f(E) \cap B) = E \cap f^{-1}(B),
$$

y $$E = (E \cap f^{-1}(C)) \cup (E \cap f^{-1}(B))$$ con $$f^{-1}(C), f^{-1}(B)$$ abiertos disjuntos en $$X$$, contradiciendo que $$E$$ es conexo.

### Corolario ($$\mathbb{R}^{d}$$ es conexo)

$$\mathbb{R}^{d}$$ es conexo para todo $$d \geq 1$$.

***Prueba:*** Suponga $$\mathbb{R}^{d} = A \cup B$$ con $$A, B$$ abiertos no vacíos disjuntos. Tome $$x \in A$$, $$y \in B$$ y $$f : [0, 1] \to \mathbb{R}^{d}$$, $$t \mapsto (1-t)x + ty$$, continua. Como $$[0, 1]$$ es conexo, $$[x, y] = f([0,1])$$ es conexo. Pero $$[x, y] = ([x,y] \cap A) \cup ([x,y] \cap B)$$ con ambos cortes no vacíos, contradicción.

### Lema (Unión de conexos con un punto en común)

Sea $$\{ E_{\alpha} : \alpha \in A\}$$ una familia de conjuntos conexos tal que $$\bigcap_{\alpha \in A} E_{\alpha} \neq \emptyset$$. Entonces $$E = \bigcup_{\alpha \in A} E_{\alpha}$$ es conexo.

***Prueba:*** Sea $$x \in \bigcap_{\alpha \in A} E_{\alpha}$$ y suponga, por contradicción, que existen $$A', B'$$ abiertos con $$E = (A' \cap E) \cup (B' \cap E)$$, $$A' \cap E \neq \emptyset$$, $$B' \cap E \neq \emptyset$$ y $$A' \cap B' \cap E = \emptyset$$. Sin pérdida de generalidad $$x \in B'$$.

Como $$A' \cap E \neq \emptyset$$, tome $$y \in A' \cap E$$; como $$E = \bigcup_{\alpha} E_{\alpha}$$, existe $$\alpha_{0}$$ con $$y \in E_{\alpha_{0}}$$, luego $$A' \cap E_{\alpha_{0}} \neq \emptyset$$. Por otra parte $$x \in E_{\alpha_{0}}$$ (pues $$x$$ está en *cada* $$E_{\alpha}$$) y $$x \in B'$$, así $$B' \cap E_{\alpha_{0}} \neq \emptyset$$.

Veamos que esto descompone $$E_{\alpha_{0}}$$ en dos abiertos relativos no vacíos y disjuntos:

- **Cobertura:** todo $$z \in E_{\alpha_{0}}$$ satisface $$z \in E$$, luego (por la descomposición global) $$z \in A'$$ o $$z \in B'$$. Por tanto

    $$
    E_{\alpha_{0}} \;\subseteq\; (E_{\alpha_{0}} \cap A') \cup (E_{\alpha_{0}} \cap B');
    $$

    la inclusión recíproca es inmediata. Concluimos $$E_{\alpha_{0}} = (E_{\alpha_{0}} \cap A') \cup (E_{\alpha_{0}} \cap B')$$.
- **Disjuntez:** $$(E_{\alpha_{0}} \cap A') \cap (E_{\alpha_{0}} \cap B') = E_{\alpha_{0}} \cap (A' \cap B') \subseteq E \cap (A' \cap B') = \emptyset$$.
- **Ambos no vacíos:** ya probado arriba.

Esto contradice que $$E_{\alpha_{0}}$$ sea conexo.

## Componentes conexas

### Definición (Componente conexa de un punto)

Sea $$(X, d)$$ un espacio métrico y $$x \in X$$. La *componente conexa* de $$x$$ es

$$
C(x) = \bigcup\{ E \subseteq X : E \text{ conexo}, \; x \in E\}.
$$

### Nota (La componente conexa es conexa)

Por el lema de unión de conexos con punto en común, $$C(x)$$ es conexo para todo $$x \in X$$.

### Ejercicio (Las componentes son clases de equivalencia)

Defina la relación $$\mathcal{R}$$ en $$X$$ por $$x \mathcal{R} y \iff \exists\, C \text{ conexo}\,(x, y \in C)$$. Pruebe que $$\mathcal{R}$$ es una relación de equivalencia y que $$[x] = C(x)$$.

## Caracterización de los conexos en R

### Lema (Un conexo de $$\mathbb{R}$$ contiene los segmentos entre sus puntos)

Sea $$E \subseteq \mathbb{R}$$ conexo y $$a, b \in E$$ con $$a \leq b$$. Entonces $$[a, b] \subseteq E$$.

***Prueba:*** Suponga que existe $$x \in [a, b] \setminus E$$. Entonces

$$
E = (E \cap (-\infty, x)) \cup (E \cap (x, \infty)),
$$

descomposición de $$E$$ en dos abiertos relativos no vacíos y disjuntos, contradiciendo que $$E$$ es conexo.

### Teorema (Los conexos de $$\mathbb{R}$$ son los intervalos)

$$E \subseteq \mathbb{R}$$ es conexo si y solo si $$E$$ es un intervalo (acotado o no, abierto, cerrado o semiabierto).

***Prueba:*** $$(\impliedby)$$: Los intervalos abiertos son conexos por un lema previo, y la unión creciente $$\bigcup_{n} (a + 1/n, b - 1/n)$$, $$\bigcup_{n} [a, b - 1/n]$$, etc., con intersección no vacía permite obtener todos los demás tipos por aplicación del lema de unión.

$$(\implies)$$: Si $$E$$ es conexo y acotado, defina $$\alpha = \inf E$$, $$\beta = \sup E$$. Tome $$\{a_{n}\}, \{b_{n}\} \subseteq E$$ con $$a_{n} \downarrow \alpha$$ y $$b_{n} \uparrow \beta$$. Entonces, por el lema anterior, $$[a_{n}, b_{n}] \subseteq E$$, y por tanto $$(\alpha, \beta) = \bigcup_{n} [a_{n}, b_{n}] \subseteq E \subseteq [\alpha, \beta]$$. Así $$E$$ es uno de $$[\alpha, \beta], (\alpha, \beta], [\alpha, \beta), (\alpha, \beta)$$, según si $$\alpha, \beta \in E$$. Si $$E$$ no es acotado superiormente, defina $$\beta = +\infty$$ y tome $$b_{n} \in E$$ con $$b_{n} \to +\infty$$; entonces $$(\alpha, +\infty) = \bigcup_{n} [a_{n}, b_{n}] \subseteq E$$, así $$E \in \{ (\alpha, +\infty),\; [\alpha, +\infty) \}$$. Análogamente para $$E$$ no acotado inferiormente, y el caso $$E = \mathbb{R}$$ se obtiene combinando ambos.

### Ejercicio (Estructura de los abiertos en $$\mathbb{R}$$)

Sea $$G \subseteq \mathbb{R}$$ abierto. Pruebe que existen intervalos abiertos disjuntos $$\{ (a_{i}, b_{i})\}_{i=1}^{\infty}$$ tales que $$G = \bigcup_{i=1}^{\infty} (a_{i}, b_{i})$$.

## Arcoconexidad

### Definición (Conjunto arcoconexo en $$\mathbb{R}^{d}$$)

$$E \subseteq \mathbb{R}^{d}$$ es *arcoconexo* si para todos $$x_{0}, x_{1} \in E$$ existe una curva $$\gamma : [0, 1] \to \mathbb{R}^{d}$$ tal que

1. $$\gamma(0) = x_{0}$$ y $$\gamma(1) = x_{1}$$;
2. $$\gamma(t) \in E$$ para todo $$t \in [0, 1]$$.

### Ejemplo (La curva del seno topológico: conexo no arcoconexo)

Considere

$$
E = \{(0, 0)\} \cup \left\{ (x, y) : 0 < x \leq 1,\; y = \sin\!\left(\tfrac{1}{x}\right) \right\}.
$$

*$$E$$ es conexo.* Sean $$A, B$$ abiertos con $$A \cap E \neq \emptyset \neq B \cap E$$, $$E \subseteq A \cup B$$ y $$A \cap B = \emptyset$$, y supóngase $$(0, 0) \in A$$. Para $$n \in \mathbb{N}$$ con $$n$$ grande, $$x_{n} = (\tfrac{1}{\pi n}, \sin(\pi n)) = (\tfrac{1}{\pi n}, 0) \in A$$ (por convergencia a $$(0,0)$$ y abierto $$A$$). Para cada $$n$$,

$$
E_{n} = \left\{ (x, y) : \tfrac{1}{n\pi} \leq x \leq 1,\; y = \sin\!\left(\tfrac{1}{x}\right)\right\}
$$

es la imagen continua del intervalo $$[\tfrac{1}{\pi n}, 1]$$ y por tanto es conexo. Como $$E_{n} \cap A \neq \emptyset$$, $$E_{n} \cap B = \emptyset$$, así $$E_{n} \subseteq A$$, y tomando uniones $$\{(x, \sin(1/x)) : 0 < x \leq 1\} \subseteq A$$. Concluimos $$E \subseteq A$$, contradiciendo $$B \cap E \neq \emptyset$$.

*$$E$$ no es arcoconexo.* Suponga que existe $$\tilde{\gamma} : [0, 1] \to E$$ continua con $$\tilde{\gamma}(0) = (0, 0)$$ y $$\tilde{\gamma}(1) = (1/(n_{0}\pi), 0)$$. Sea $$t_{0} = \sup\{ t > 0 : \tilde{\gamma}(t) = (0, 0)\}$$. Tomando $$\{t_{n}\}$$ decreciente con $$t_{n} \to t_{0}$$, $$\tilde{\gamma}(t_{n}) \to (0, 0)$$, así $$\tilde{\gamma}_{1}(t_{n}) \to 0$$ y $$\tilde{\gamma}_{2}(t_{n}) = \sin(1/\tilde{\gamma}_{1}(t_{n}))$$ no converge (oscila entre $$-1$$ y $$1$$ a lo largo de los $$t_{n}$$ adecuados), contradiciendo la continuidad de $$\tilde{\gamma}_{2}$$ en $$t_{0}$$.

### Ejercicio (Detalles del contraejemplo de arcoconexidad)

En el ejemplo anterior, pruebe:

1. Si $$x_{n} < x_{n+1}$$ entonces, para $$x_{n} \leq x \leq x_{n+1}$$, $$(x, \sin(1/x)) \in \tilde{\gamma}([0,1])$$.
2. $$B = \{ (x, \sin(1/x)) : 0 < x < 1/(n_{0}\pi)\} \subseteq \tilde{\gamma}([0,1])$$.
3. $$\tilde{\gamma}([t_{0}, 1]) \setminus B = \{ (0, 0)\}$$.
4. $$\tilde{\gamma}$$ no es continua en $$t_{0}$$.

### Lema (En abiertos de $$\mathbb{R}^{d}$$, conexo equivale a arcoconexo)

Sea $$E \subseteq \mathbb{R}^{d}$$ abierto. Entonces $$E$$ es conexo si y solo si $$E$$ es arcoconexo.

***Prueba:*** $$(\impliedby)$$: Por el teorema general, todo arcoconexo es conexo.

$$(\implies)$$: Fije $$x_{0} \in E$$ y considere $$A = \{ x \in E : x \text{ se une a } x_{0} \text{ por una curva en } E\}$$. Como $$E$$ es abierto y unión de curvas con bolas, $$A$$ y $$E \setminus A$$ son ambos abiertos en $$E$$ (alrededor de cualquier $$y \in A$$ una bola en $$E$$ se une a $$y$$ con una recta y por concatenación a $$x_{0}$$). Por conexidad y $$A \neq \emptyset$$, $$A = E$$. (Detalles: *ejercicio*.)
{% endraw %}
