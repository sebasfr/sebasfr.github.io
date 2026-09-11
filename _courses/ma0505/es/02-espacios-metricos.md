---
layout: chapter
course: ma0505
chapter: 2
title: "Espacios métricos"
slug: 02-espacios-metricos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/02-espacios-metricos/
---

{% raw %}
## Normas, distancias y métricas

### Definición (Norma)

Una *norma* en $$\mathbb{R}^{d}$$ es una función $$\|\cdot\| : \mathbb{R}^{d} \to [0, +\infty)$$ que satisface:

1. $$\|x\| \geq 0$$ para todo $$x \in \mathbb{R}^{d}$$, con $$\|x\| = 0$$ si y solo si $$x = 0$$;
2. $$\|\lambda x\| = |\lambda|\,\|x\|$$ para todo $$\lambda \in \mathbb{R}$$ y $$x \in \mathbb{R}^{d}$$;
3. $$\|x + y\| \leq \|x\| + \|y\|$$ para todos $$x, y \in \mathbb{R}^{d}$$.

### Nota (Distancia inducida por una norma en $$\mathbb{R}^{d}$$)

Una norma induce una *distancia* (o métrica) $$d : \mathbb{R}^{d} \times \mathbb{R}^{d} \to [0, +\infty)$$ mediante $$d(x,y) = \|x - y\|$$, la cual cumple:

1. $$d(x,y) = d(y,x)$$;
2. $$d(x,y) = 0 \iff x = y$$;
3. $$d(x,z) = \|x-z\| = \|x-y+y-z\| \leq \|x-y\| + \|y-z\| = d(x,y) + d(y,z)$$.

### Definición (Espacio métrico)

Sea $$E$$ un conjunto. Una *métrica* es una función $$d : E \times E \to [0, +\infty)$$ que satisface:

1. $$d(x,y) = d(y,x)$$;
2. $$d(x,y) = 0$$ si y solo si $$x = y$$;
3. $$d(x,y) \leq d(x,z) + d(z,y)$$ *(desigualdad triangular)*.

El par $$(E, d)$$ se llama *espacio métrico*.

### Ejemplo (La métrica usual en $$\mathbb{R}^{d}$$)

En $$\mathbb{R}^{d}$$ con la norma euclídea, $$d(x,y) = \|x - y\|$$ es métrica; la desigualdad triangular es la usual del módulo.

## Topología métrica: bolas, abiertos y cerrados

### Definición (Bola abierta en un espacio métrico)

Sea $$(E, d)$$ un espacio métrico. Para $$x_{0} \in E$$ y $$r > 0$$ se define

$$
B(x_{0}, r) = \{ y \in E : d(x_{0}, y) < r \}.
$$

### Definición (Conjunto abierto en un espacio métrico)

$$D \subseteq E$$ es un *conjunto abierto* si para todo $$x_{0} \in D$$ existe $$r > 0$$ tal que $$B(x_{0}, r) \subseteq D$$. En particular $$\emptyset$$ y $$E$$ son abiertos.

### Lema (Las bolas son abiertos)

Para todos $$x_{0} \in E$$ y $$r > 0$$, $$B(x_{0}, r)$$ es un conjunto abierto.

***Prueba:*** Sea $$x_{1} \in B(x_{0}, r)$$. Mostraremos que si $$0 < r_{1} < r - d(x_{0}, x_{1})$$, entonces $$B(x_{1}, r_{1}) \subseteq B(x_{0}, r)$$. En efecto, si $$y \in B(x_{1}, r_{1})$$, entonces

$$
d(x_{0}, y) \leq d(x_{0}, x_{1}) + d(x_{1}, y) < d(x_{0}, x_{1}) + r_{1} < d(x_{0}, x_{1}) + r - d(x_{0}, x_{1}) = r,
$$

de donde $$y \in B(x_{0}, r)$$.

### Lema (Intersección finita de abiertos es abierto)

Si $$G_{1}, G_{2}, \dots, G_{m}$$ son abiertos en $$(E, d)$$, entonces $$\bigcap_{i=1}^{m} G_{i}$$ es abierto.

***Prueba:*** Basta probarlo para $$m = 2$$ y aplicar inducción. Sea $$x_{0} \in G_{1} \cap G_{2}$$. Existen $$r_{1}, r_{2} > 0$$ tales que $$B(x_{0}, r_{1}) \subseteq G_{1}$$ y $$B(x_{0}, r_{2}) \subseteq G_{2}$$. Tomando $$r = \min(r_{1}, r_{2})$$,

$$
B(x_{0}, r) \subseteq B(x_{0}, r_{1}) \cap B(x_{0}, r_{2}) \subseteq G_{1} \cap G_{2}.
$$

### Lema (Unión arbitraria de abiertos es abierto)

Si $$\{ G_{\lambda} \}_{\lambda \in \Lambda}$$ es una colección cualquiera de abiertos en $$(E, d)$$, entonces $$\bigcup_{\lambda \in \Lambda} G_{\lambda}$$ es abierto.

***Prueba:*** Si $$x_{0} \in \bigcup_{\lambda \in \Lambda} G_{\lambda}$$, entonces existe $$\lambda_{0}$$ con $$x_{0} \in G_{\lambda_{0}}$$. Como $$G_{\lambda_{0}}$$ es abierto, existe $$r > 0$$ tal que $$B(x_{0}, r) \subseteq G_{\lambda_{0}} \subseteq \bigcup_{\lambda \in \Lambda} G_{\lambda}$$.

### Definición (Conjunto cerrado)

$$F \subseteq E$$ es *cerrado* si $$E \setminus F$$ es abierto.

### Nota (Propiedades básicas de los cerrados)

1. Si $$\{ F_{\lambda} \}_{\lambda \in \Lambda}$$ es una familia de cerrados, $$\bigcap_{\lambda \in \Lambda} F_{\lambda}$$ es cerrado, pues

    $$
    E \setminus \bigcap_{\lambda \in \Lambda} F_{\lambda} = \bigcup_{\lambda \in \Lambda} (E \setminus F_{\lambda})
    $$

    es unión de abiertos.
2. Si $$F_{1}, \dots, F_{m}$$ son cerrados, entonces $$\bigcup_{i=1}^{m} F_{i}$$ es cerrado.

### Ejemplo (Las propiedades de cerrados/abiertos no se preservan al pasar a colecciones arbitrarias)

1. $$\bigcap_{n=1}^{\infty} \left( a - \tfrac{1}{n}, a + \tfrac{1}{n}\right) = \{ a\}$$ no es abierto. Es decir, la intersección numerable de abiertos no es necesariamente abierta.
2. $$\left( a, b \right) = \bigcup_{n=1}^{\infty} \left[a + \tfrac{1}{n}, b - \tfrac{1}{n}\right]$$ no es cerrado. Es decir, la unión numerable de cerrados no es necesariamente cerrada.
{% endraw %}
