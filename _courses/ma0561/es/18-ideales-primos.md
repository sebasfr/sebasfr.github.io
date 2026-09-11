---
layout: chapter
course: ma0561
chapter: 18
title: "Ideales primos"
slug: 18-ideales-primos
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/18-ideales-primos/
---

{% raw %}
## Definición y caracterizaciones

### Definición (Ideal primo)

Sea $$R$$ un anillo y $$I$$ un $$R$$-ideal. Decimos que $$I$$ es *primo* si para todos $$x, y \in R$$, si $$x y \in I$$ entonces $$x \in I$$ o $$y \in I$$.

### Notación (El espectro primo)

Denotamos por $$\operatorname{Spec}(R)$$ al conjunto de los ideales primos de $$R$$.

### Proposición (Caracterización de primalidad con productos de ideales)

Sea $$R$$ un anillo y sea $$I$$ un $$R$$-ideal. Las siguientes son equivalentes:

1. $$I$$ es primo;
2. para todos $$J_{1}, J_{2}$$ ideales de $$R$$: si $$J_{1} J_{2} \subseteq I$$, entonces $$J_{1} \subseteq I$$ o $$J_{2} \subseteq I$$.

***Prueba:*** Ejercicio.

### Proposición (El ideal cero es primo si y solo si el anillo es dominio entero)

Sea $$R$$ un anillo conmutativo con $$R \neq \{0\}$$. Entonces $$R$$ es un dominio entero si y solo si $$\{0\}$$ es primo.

***Prueba:*** “$$\Rightarrow$$”: Sean $$x, y \in R$$ tales que $$x \cdot y \in \{0\}$$, es decir, $$x \cdot y = 0$$. Como $$R$$ es un dominio entero, no posee divisores de cero, y entonces $$x = 0$$ o $$y = 0$$; es decir, $$x \in \{0\}$$ o $$y \in \{0\}$$. Concluimos que $$\{0\}$$ es primo.

“$$\Leftarrow$$”: Procedemos por contrapositiva. Si $$R$$ no es un dominio entero, entonces, al ser $$R$$ conmutativo, la única posibilidad es que posea divisores de cero: existen $$x, y \in R$$ tales que $$x \neq 0$$, $$y \neq 0$$, pero $$x \cdot y = 0$$. Entonces $$x \cdot y \in \{0\}$$, pero $$x \notin \{0\}$$ y $$y \notin \{0\}$$, de modo que $$\{0\}$$ no es primo.

## Maximales, primos y el nilradical

### Proposición (Todo ideal maximal es primo)

Sea $$R$$ un anillo conmutativo con $$R \neq \{0\}$$. Entonces todo ideal maximal es primo. En particular, $$\operatorname{Spec}(R) \neq \emptyset$$.

***Prueba:*** Sea $$\mathfrak{m}$$ un ideal maximal, y sean $$x, y \in R$$ tales que $$x \cdot y \in \mathfrak{m}$$. Suponga, por contradicción, que $$x \notin \mathfrak{m}$$ y $$y \notin \mathfrak{m}$$. Considere

$$
(x) + \mathfrak{m} = \{ r \cdot x + m :\ r \in R,\ m \in \mathfrak{m} \} \subseteq R,
$$

que es un ideal, por ser suma de ideales. Note que $$\mathfrak{m} \subseteq (x) + \mathfrak{m}$$, y la contención es estricta: $$x = 1 \cdot x + 0 \in (x) + \mathfrak{m}$$, pero $$x \notin \mathfrak{m}$$. Es decir, $$\mathfrak{m} \subsetneq (x) + \mathfrak{m}$$, y análogamente $$\mathfrak{m} \subsetneq (y) + \mathfrak{m}$$.

Como $$\mathfrak{m}$$ es maximal y ambos son ideales que contienen propiamente a $$\mathfrak{m}$$, tenemos que

$$
(x) + \mathfrak{m} = R = (y) + \mathfrak{m}.
$$

Como $$1 \in R$$, existen $$m_{1}, m_{2} \in \mathfrak{m}$$ y $$r_{1}, r_{2} \in R$$ tales que

$$
1 = r_{1} x + m_{1}, \qquad 1 = r_{2} y + m_{2}.
$$

Multiplicando ambas igualdades,

$$
1 = (r_{1} x + m_{1})(r_{2} y + m_{2}) = \underbrace{r_{1} r_{2}\, x y}_{\in\, \mathfrak{m}} + \underbrace{r_{1} x\, m_{2}}_{\in\, \mathfrak{m}} + \underbrace{m_{1}\, r_{2} y}_{\in\, \mathfrak{m}} + \underbrace{m_{1} m_{2}}_{\in\, \mathfrak{m}} \in \mathfrak{m},
$$

donde el primer sumando está en $$\mathfrak{m}$$ porque $$x y \in \mathfrak{m}$$ y $$\mathfrak{m}$$ absorbe productos, y los restantes por absorción directa. Entonces $$1 \in \mathfrak{m}$$, de donde $$\mathfrak{m} = R$$, lo cual es una contradicción con la definición de ideal maximal. Concluimos que $$x \in \mathfrak{m}$$ o $$y \in \mathfrak{m}$$, es decir, $$\mathfrak{m}$$ es primo.

Finalmente, por el corolario del teorema de Krull, $$\operatorname{mSpec}(R) \neq \emptyset$$, y como todo maximal es primo, $$\operatorname{Spec}(R) \supseteq \operatorname{mSpec}(R) \neq \emptyset$$.

### Ejemplo (Espectros primos conocidos)

Calculamos $$\operatorname{Spec}$$ en los ejemplos básicos:

1. Sea $$K$$ un cuerpo. Entonces $$\operatorname{mSpec}(K) = \operatorname{Spec}(K) = \{ \{0\} \}$$.
2. Sea $$R = \mathbb{Z}$$. Entonces

    $$
    \operatorname{mSpec}(\mathbb{Z}) = \{ p\mathbb{Z} :\ p \text{ primo} \}, \qquad \operatorname{Spec}(\mathbb{Z}) = \operatorname{mSpec}(\mathbb{Z}) \cup \{ \{0\} \}.
    $$
3. Sea $$R = \mathbb{R}[x]$$. El ideal $$\langle x^{2} - 1 \rangle$$ no es primo:

    $$
    x^{2} - 1 = (x - 1)(x + 1) \in \langle x^{2} - 1 \rangle,
    $$

    pero (ejercicio) $$(x - 1), (x + 1) \notin \langle x^{2} - 1 \rangle$$.

### Teorema (El nilradical es la intersección de los ideales primos)

Sea $$R$$ un anillo conmutativo. Entonces

$$
\bigcap_{I \text{ primo}} I = \operatorname{Nil}(R) = \{ x \in R :\ \exists n \in \mathbb{N}\ (x^{n} = 0) \}.
$$

***Prueba:*** Ejercicio.
{% endraw %}
