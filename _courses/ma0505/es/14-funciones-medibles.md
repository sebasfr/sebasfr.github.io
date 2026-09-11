---
layout: chapter
course: ma0505
chapter: 14
title: "Funciones medibles"
slug: 14-funciones-medibles
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/14-funciones-medibles/
---

{% raw %}
## Definición y equivalencias

### Definición (Función medible)

Sea $$f : E \to \overline{\mathbb{R}} = \mathbb{R} \cup \{\pm\infty\}$$. Decimos que $$f$$ es *medible* si para todo $$a \in \mathbb{R}$$

$$
\{f > a\} := \{x \in E : f(x) > a\} \in \mathcal{M}.
$$

Como $$E = \bigcup_{k=1}^{\infty}\{f > -k\} \cup \{f = -\infty\}$$, si $$f$$ es medible entonces $$E$$ es medible si y sólo si $$\{f = -\infty\}$$ es medible. En lo que sigue se supone que $$E$$ es medible.

### Ejemplo (Funciones continuas e indicadoras)

1. Si $$f : \mathbb{R}^{d} \to \mathbb{R}$$ es continua, $$\{f > a\} = f^{-1}((a, \infty))$$ es abierto, luego medible; toda función continua es medible.
2. Si $$f = \mathbf{1}_{A}$$ con $$A$$ medible, entonces $$\{f > a\}$$ vale $$E$$ si $$a < 0$$, $$A$$ si $$0 \leq a < 1$$ y $$\emptyset$$ si $$a \geq 1$$; en todos los casos es medible.

### Teorema (Condiciones equivalentes de medibilidad)

Sea $$f : E \to \overline{\mathbb{R}}$$ con $$E$$ medible. Las siguientes condiciones, para todo $$a \in \mathbb{R}$$, son equivalentes:

$$
\text{(i) } \{f > a\} \in \mathcal{M}, \quad \text{(ii) } \{f < a\} \in \mathcal{M}, \quad \text{(iii) } \{f \leq a\} \in \mathcal{M}, \quad \text{(iv) } \{f \geq a\} \in \mathcal{M}.
$$

***Prueba:*** $$\{f \leq a\} = \{f > a\}^{c}$$ y $$\{f < a\} = \{f \geq a\}^{c}$$, de modo que (i)$$\Leftrightarrow$$(iii) y (ii)$$\Leftrightarrow$$(iv) por cerradura bajo complementos. Además

$$
\{f \geq a\} = \bigcap_{n=1}^{\infty}\Big\{f > a - \tfrac{1}{n}\Big\}, \qquad \{f > a\} = \bigcup_{n=1}^{\infty}\Big\{f \geq a + \tfrac{1}{n}\Big\},
$$

lo que muestra (i)$$\Rightarrow$$(iv) y (iv)$$\Rightarrow$$(i) por cerradura bajo intersecciones y uniones numerables. Las cuatro condiciones son, pues, equivalentes.

### Nota (Otros conjuntos medibles asociados a $$f$$)

Si $$f : E \to \overline{\mathbb{R}}$$ es medible, son medibles

$$
\{f > -\infty\} = \bigcup_{k}\{f > -k\}, \quad \{f < \infty\} = \bigcup_{k}\{f \leq k\}, \quad \{f = \infty\}, \quad \{a \leq f \leq b\}, \quad \{a \leq f < b\},
$$

por ser intersecciones y uniones numerables de los conjuntos $$\{f > a\}$$, $$\{f \leq a\}$$, etc.

### Definición (Función Borel medible)

$$f : E \to \mathbb{R}$$ es *Borel medible* si $$E \in \mathcal{B}$$ y $$\{f > a\} \in \mathcal{B}$$ para todo $$a \in \mathbb{R}$$.

### Teorema (Medibilidad por preimágenes de abiertos)

Sea $$f : E \to \mathbb{R}$$. Entonces $$f$$ es medible si y sólo si $$f^{-1}(G)$$ es medible para todo abierto $$G \subseteq \mathbb{R}$$.

***Prueba:*** Si las preimágenes de abiertos son medibles, tomando $$G = (a, \infty)$$ se obtiene $$\{f > a\} = f^{-1}(G)$$ medible, luego $$f$$ es medible. Recíprocamente, sea $$f$$ medible y $$G \subseteq \mathbb{R}$$ abierto; escriba $$G = \bigcup_{k}(a_{k}, b_{k})$$. Como

$$
f^{-1}\big((a_{k}, b_{k})\big) = \{a_{k} < f\} \cap \{f < b_{k}\}
$$

es medible, $$f^{-1}(G) = \bigcup_{k} f^{-1}\big((a_{k}, b_{k})\big)$$ es unión numerable de medibles, luego medible.

## Composición, igualdad casi por doquier y operaciones

### Lema (Composición de una medible con una continua)

Sea $$f : E \to \mathbb{R}$$ medible y $$\phi : \mathbb{R} \to \mathbb{R}$$ continua. Entonces $$\phi \circ f$$ es medible.

***Prueba:*** Sea $$G \subseteq \mathbb{R}$$ abierto. Entonces $$(\phi \circ f)^{-1}(G) = f^{-1}\big(\phi^{-1}(G)\big)$$. Como $$\phi$$ es continua, $$\phi^{-1}(G)$$ es abierto, y como $$f$$ es medible, $$f^{-1}\big(\phi^{-1}(G)\big)$$ es medible. Por el teorema anterior, $$\phi \circ f$$ es medible.

### Nota (Consecuencias inmediatas)

Si $$f$$ es medible, entonces $$|f|$$, $$|f|^{p}$$ ($$p > 0$$), $$e^{cf}$$ ($$c \in \mathbb{R}$$) y las partes positiva y negativa

$$
f^{+} = \max\{f, 0\}, \qquad f^{-} = \max\{-f, 0\}
$$

son medibles. (Aquí $$f^{+}, f^{-} \geq 0$$, $$f = f^{+} - f^{-}$$ y $$|f| = f^{+} + f^{-}$$, en concordancia con la notación de partes positiva y negativa de un número real.)

### Definición (Casi por doquier)

Una propiedad se cumple *casi por doquier* (c.p.d.) si se cumple salvo en un conjunto de medida cero.

### Lema (La igualdad casi por doquier preserva la medibilidad)

Sean $$f, g : E \to \mathbb{R}$$ con $$f$$ medible y $$g = f$$ casi por doquier. Entonces $$g$$ es medible.

***Prueba:*** Sea $$a \in \mathbb{R}$$. Descomponiendo según donde $$f$$ y $$g$$ coinciden,

$$
\{g > a\} = \big(\{g > a\} \cap \{f = g\}\big) \cup \big(\{g > a\} \cap \{f \neq g\}\big).
$$

El primer conjunto es $$\{f > a\} \cap \{f = g\}$$, medible (intersección de medibles, salvo el conjunto $$\{f \neq g\}$$ de medida cero que es medible). El segundo está contenido en $$\{f \neq g\}$$, de medida cero, luego medible. Por tanto $$\{g > a\}$$ es unión de medibles y $$g$$ es medible.

### Lema (Composición con una continua para funciones finitas c.p.d.)

Sea $$f : E \to \overline{\mathbb{R}}$$ medible con $$m(\{f = \infty\}) = m(\{f = -\infty\}) = 0$$. Entonces $$\phi \circ f$$ es medible para toda $$\phi : \mathbb{R} \to \mathbb{R}$$ continua.

***Prueba:*** Sea $$F = \{x \in E : f(x) \in \mathbb{R}\}$$ y defina $$f_{1} = f$$ en $$F$$ y $$f_{1} = 0$$ en $$E \setminus F$$. Como $$E \setminus F = \{f = \infty\} \cup \{f = -\infty\}$$ tiene medida cero, $$f_{1}$$ es medible y $$f_{1} = f$$ casi por doquier. Por el lema de composición, $$\phi \circ f_{1}$$ es medible, y como $$\phi \circ f_{1} = \phi \circ f$$ c.p.d., el lema anterior da que $$\phi \circ f$$ es medible.

### Lema (El conjunto donde una medible supera a otra es medible)

Sean $$f, g : E \to \mathbb{R}$$ medibles. Entonces $$\{f > g\}$$ es medible.

***Prueba:*** Sea $$\{q_{n}\}_{n=1}^{\infty}$$ una enumeración de $$\mathbb{Q}$$. Como $$f(x) > g(x)$$ si y sólo si existe un racional estrictamente entre $$g(x)$$ y $$f(x)$$,

$$
\{f > g\} = \bigcup_{n=1}^{\infty}\big(\{f > q_{n}\} \cap \{q_{n} > g\}\big),
$$

unión numerable de intersecciones de medibles, luego medible.

### Lema (Estructura de espacio vectorial de las funciones medibles)

Sean $$f, g : E \to \mathbb{R}$$ medibles. Entonces:

1. $$f + \lambda$$ y $$\lambda f$$ son medibles para todo $$\lambda \in \mathbb{R}$$;
2. $$f + g$$ es medible.

***Prueba:*** El inciso (i) queda como ejercicio (directo desde la definición: $$\{f + \lambda > a\} = \{f > a - \lambda\}$$ y, para $$\lambda > 0$$, $$\{\lambda f > a\} = \{f > a/\lambda\}$$, etc.). Para (ii), $$g$$ y $$\lambda - g$$ son medibles por (i), y por el lema anterior aplicado a $$f$$ y $$\lambda - g$$,

$$
\{f + g > \lambda\} = \{f > \lambda - g\}
$$

es medible para todo $$\lambda \in \mathbb{R}$$, luego $$f + g$$ es medible.

### Ejercicio (El caso de valores infinitos en la suma)

El lema anterior sigue valiendo para $$f, g : E \to \overline{\mathbb{R}}$$ siempre que $$f + g$$ esté bien definida (es decir, evitando la indeterminación $$\infty - \infty$$). Pruebe esta variante.

### Corolario (Producto y cociente de funciones medibles)

Sean $$f, g : E \to \overline{\mathbb{R}}$$ medibles. Entonces $$fg$$ es medible (con la convención $$0 \cdot (\pm\infty) = 0$$, de modo que el producto siempre está definido), y $$f/g$$ es medible si $$g \neq 0$$.

***Prueba:*** Sea $$F = \{f \in \mathbb{R}\} \cap \{g \in \mathbb{R}\}$$. Para $$a \geq 0$$,

$$
\{fg > a\} = \big(\{fg > a\} \cap F\big) \cup \big(\{f = \infty\} \cap \{g > 0\}\big) \cup \big(\{g = \infty\} \cap \{f > 0\}\big) \cup \big(\{f = -\infty\} \cap \{g < 0\}\big) \cup \big(\{g = -\infty\} \cap \{f < 0\}\big),
$$

y todos los conjuntos del lado derecho son medibles salvo, a priori, el primero. En $$F$$ vale la identidad de polarización

$$
fg = \tfrac{1}{4}\big((f + g)^{2} - (f - g)^{2}\big);
$$

como $$f + g$$ y $$f - g$$ son medibles (lema anterior) y el cuadrado es composición con la continua $$t \mapsto t^{2}$$, $$fg$$ es medible en $$F$$, de modo que $$\{fg > a\} \cap F$$ es medible. El tratamiento de $$a < 0$$ y del cociente $$f/g$$ (componiendo con $$t \mapsto 1/t$$ donde $$g \neq 0$$) queda como ejercicio.

## Sucesiones de funciones medibles y funciones simples

### Teorema (Sup, inf, límite superior e inferior de funciones medibles)

Sea $$\{f_{k}\}_{k=1}^{\infty}$$ una sucesión de funciones medibles $$E \to \overline{\mathbb{R}}$$. Entonces $$\sup_{k} f_{k}$$, $$\inf_{k} f_{k}$$, $$\limsup_{k} f_{k}$$ y $$\liminf_{k} f_{k}$$ son medibles.

***Prueba:*** Para todo $$a \in \mathbb{R}$$,

$$
\Big\{\sup_{k \geq 1} f_{k} > a\Big\} = \bigcup_{k=1}^{\infty}\{f_{k} > a\}
$$

es medible, luego $$\sup_{k} f_{k}$$ es medible. Las restantes se reducen a esta:

$$
\inf_{k} f_{k} = -\sup_{k}(-f_{k}), \qquad \limsup_{k} f_{k} = \inf_{k \geq 1}\sup_{\ell \geq k} f_{\ell}, \qquad \liminf_{k} f_{k} = \sup_{k \geq 1}\inf_{\ell \geq k} f_{\ell}.
$$

### Definición (Función simple)

Una función $$\phi$$ es *simple* si existen conjuntos medibles $$A_{1}, \dots, A_{m}$$ y reales $$a_{1}, \dots, a_{m}$$ con

$$
\phi = \sum_{k=1}^{m} a_{k}\, \mathbf{1}_{A_{k}}.
$$

### Ejercicio (Forma canónica de una función simple)

Pruebe que toda función simple $$\phi$$ admite una representación $$\phi = \sum_{k=1}^{\ell} b_{k}\, \mathbf{1}_{B_{k}}$$ con $$B_{1}, \dots, B_{\ell}$$ medibles disjuntos dos a dos y $$b_{1}, \dots, b_{\ell}$$ distintos dos a dos.

### Nota (Aproximación diádica de una función no negativa)

Sea $$f : E \to [0, \infty]$$. Para $$k \in \mathbb{N}$$ defina

$$
f_{k} = k\,\mathbf{1}_{B_{k}} + \sum_{j=1}^{k 2^{k}} \frac{j-1}{2^{k}}\,\mathbf{1}_{A_{k}^{j}}, \qquad B_{k} = f^{-1}\big([k, \infty]\big), \quad A_{k}^{j} = f^{-1}\Big(\Big[\tfrac{j-1}{2^{k}}, \tfrac{j}{2^{k}}\Big)\Big),
$$

es decir, $$f_{k}(x) = \tfrac{j-1}{2^{k}}$$ si $$\tfrac{j-1}{2^{k}} \leq f(x) < \tfrac{j}{2^{k}}$$ y $$f_{k}(x) = k$$ si $$f(x) \geq k$$. Si $$0 \leq f(x) < k$$, entonces $$0 \leq f(x) - f_{k}(x) < \tfrac{1}{2^{k}}$$, de modo que $$f_{k}(x) \to f(x)$$ cuando $$f(x) < \infty$$; y si $$f(x) = \infty$$, $$f_{k}(x) = k \to \infty$$. Además $$f_{k} \leq f_{k+1}$$: al pasar de $$k$$ a $$k+1$$ cada intervalo diádico se parte en dos, y el valor de $$f_{k+1}$$ es igual o una unidad diádica mayor que el de $$f_{k}$$. Si $$f$$ es medible, los $$A_{k}^{j}$$ y $$B_{k}$$ son medibles y cada $$f_{k}$$ es simple y medible.

### Teorema (Aproximación por funciones simples)

Sea $$f : E \to \overline{\mathbb{R}}$$. Entonces existe una sucesión de funciones simples $$\psi_{k}$$ con $$\psi_{k} \to f$$ puntualmente. Si $$f \geq 0$$, la sucesión puede tomarse creciente; si $$f$$ es medible, los $$\psi_{k}$$ pueden tomarse medibles.

***Prueba:*** Para $$f \geq 0$$ la sucesión diádica $$\psi_{k} = f_{k}$$ de la nota anterior es simple, creciente y converge puntualmente a $$f$$ (y medible si $$f$$ lo es). Para $$f$$ de signo arbitrario se aplica lo anterior a $$f^{+}$$ y $$f^{-}$$ y se toma $$\psi_{k} = (f^{+})_{k} - (f^{-})_{k}$$; los detalles de este caso quedan como ejercicio.
{% endraw %}
