---
layout: chapter
course: ma0505
chapter: 15
title: "Los teoremas de Egorov y Lusin"
slug: 15-los-teoremas-de-egorov-y-lusin
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/15-los-teoremas-de-egorov-y-lusin/
---

{% raw %}
## El teorema de Egorov

A lo largo de esta sección, $$m$$ denota la medida de Lebesgue en $$\mathbb{R}^{d}$$, $$m_{e}$$ la medida exterior, y “c.p.d.” abrevia *casi por doquier*.

### Nota (La convergencia puntual no implica convergencia uniforme)

Recordemos que existen sucesiones $$f_{k} : E \to \mathbb{R}$$ continuas tales que

$$
\lim_{k \to \infty} f_{k} = f
$$

puntualmente en $$E$$, pero tales que $$f_{k}$$ no converge uniformemente a $$f$$ en compactos. El teorema de Egorov muestra que, para funciones medibles sobre un conjunto de medida finita, la convergencia puntual c.p.d. sí es uniforme fuera de un conjunto de medida arbitrariamente pequeña.

### Ejemplo (La hipótesis de medida finita es esencial en Egorov)

Sean $$E = \mathbb{R}^{d}$$ y

$$
f_{k}(x) = \mathbf{1}_{B(0,k)}(x).
$$

Entonces $$\lim_{k \to \infty} f_{k} = 1$$ puntualmente en $$\mathbb{R}^{d}$$. Sea $$F$$ cerrado y no acotado; entonces para todo $$k \in \mathbb{N}$$ existe $$x \in F$$ tal que

$$
|1 - f_{k}(x)| = 1,
$$

pues $$F$$ posee puntos fuera de $$B(0,k)$$. Es decir, la convergencia no puede ser uniforme en $$F$$. Note además que, si $$F$$ es cerrado y $$m(\mathbb{R}^{d} \setminus F) < \infty$$, entonces $$F$$ no es acotado. Por lo tanto, la conclusión del teorema de Egorov falla para esta sucesión: ningún cerrado que deje afuera medida finita admite convergencia uniforme.

### Lema (Lema técnico previo al teorema de Egorov)

Sean $$E \subseteq \mathbb{R}^{d}$$ medible con $$m(E) < \infty$$ y $$\{f_{k}\}_{k=1}^{\infty}$$ funciones medibles en $$E$$ tales que

$$
\lim_{k \to \infty} f_{k} = f \quad \text{c.p.d. en } E, \qquad |f(x)| \neq \infty \ \text{c.p.d. en } E.
$$

Entonces, dados $$\varepsilon > 0$$ y $$\eta > 0$$, existen $$F \subseteq E$$ cerrado y $$k_{0} = k_{0}(\varepsilon, \eta) \geq 0$$ tales que

$$
m(E \setminus F) < \eta
$$

y

$$
|f_{k}(x) - f(x)| < \varepsilon \quad \text{para todo } x \in F \text{ y } k \geq k_{0}.
$$

***Prueba:*** Defina

$$
\tilde{E} = \{ x \in E :\ \lim_{k \to \infty} f_{k}(x) = f(x),\ |f(x)| < \infty \}.
$$

Por hipótesis, $$m(E \setminus \tilde{E}) = 0$$. Para $$\varepsilon > 0$$ y $$\eta > 0$$ fijos, definamos

$$
E_{m} = \{ x \in \tilde{E} :\ k \geq m \implies |f(x) - f_{k}(x)| < \varepsilon \}.
$$

Entonces cada $$E_{m}$$ es medible, pues

$$
E_{m} = \tilde{E} \cap \bigcap_{k \geq m} \{ x \in E :\ |f(x) - f_{k}(x)| < \varepsilon \}
$$

es una intersección numerable de conjuntos medibles, y además $$E_{m} \subseteq E_{m+1}$$, ya que la condición se exige sobre menos índices $$k$$ al crecer $$m$$. Se cumple que $$\bigcup_{m=1}^{\infty} E_{m} = \tilde{E}$$ (ejercicio; véase el ejercicio siguiente).

Por la continuidad desde abajo de la medida, tenemos que

$$
m(\tilde{E}) = \lim_{m \to \infty} m(E_{m}).
$$

Como $$m(\tilde{E}) \leq m(E) < \infty$$, podemos restar y obtenemos

$$
\lim_{m \to \infty} m(\tilde{E} \setminus E_{m}) = \lim_{m \to \infty} \big( m(\tilde{E}) - m(E_{m}) \big) = 0.
$$

Además $$E \setminus E_{m} = (E \setminus \tilde{E}) \cup (\tilde{E} \setminus E_{m})$$ y $$m(E \setminus \tilde{E}) = 0$$, entonces $$m(E \setminus E_{m}) = m(\tilde{E} \setminus E_{m}) \to 0$$. Sea entonces $$k_{0}$$ tal que

$$
m(E \setminus E_{k_{0}}) < \frac{\eta}{2}.
$$

Note que si $$x \in E_{k_{0}}$$, entonces, por definición de $$E_{k_{0}}$$,

$$
|f(x) - f_{k}(x)| < \varepsilon \quad \text{para } k \geq k_{0}.
$$

Finalmente, como $$E_{k_{0}}$$ es medible, por regularidad interna existe $$F$$ cerrado con $$F \subseteq E_{k_{0}}$$ que satisface

$$
m(E_{k_{0}} \setminus F) < \frac{\eta}{2}.
$$

Entonces

$$
m(E \setminus F) \leq m(E \setminus E_{k_{0}}) + m(E_{k_{0}} \setminus F) < \eta,
$$

y si $$x \in F \subseteq E_{k_{0}}$$ y $$k \geq k_{0}$$, tenemos que $$|f_{k}(x) - f(x)| < \varepsilon$$.

### Ejercicio (La unión de los $$E_{m}$$ recupera $$\tilde{E}$$)

Con la notación de la prueba anterior, muestre que $$\bigcup_{m=1}^{\infty} E_{m} = \tilde{E}$$.

### Teorema (Egorov: la convergencia c.p.d. es casi uniforme en medida finita)

Sean $$E \subseteq \mathbb{R}^{d}$$ medible, con $$m(E) < \infty$$, y $$\{f_{k}\}_{k=1}^{\infty}$$ funciones medibles en $$E$$. Asuma que

$$
\lim_{k \to \infty} f_{k} = f
$$

c.p.d. en $$E$$ y que $$|f(x)| \neq \infty$$ c.p.d. en $$E$$. Entonces, dado $$\varepsilon > 0$$, existe $$F_{\varepsilon} \subseteq E$$ cerrado tal que:

1. $$m(E \setminus F_{\varepsilon}) < \varepsilon$$.
2. $$f_{k}$$ converge a $$f$$ uniformemente en $$F_{\varepsilon}$$.

***Prueba:*** Sea $$\varepsilon > 0$$. Aplicando el lema anterior con $$\varepsilon_{m} = \tfrac{1}{m}$$ y $$\eta_{m} = \tfrac{\varepsilon}{2^{m}}$$ para cada $$m \geq 1$$, existen $$F_{m} \subseteq E$$ cerrados y enteros $$\kappa_{m}^{\varepsilon}$$ tales que

$$
m(E \setminus F_{m}) < \frac{\varepsilon}{2^{m}}
$$

y

$$
|f(x) - f_{k}(x)| < \frac{1}{m} \quad \text{para todo } k \geq \kappa_{m}^{\varepsilon} \text{ y } x \in F_{m}.
$$

Sea

$$
F_{\varepsilon} = \bigcap_{m=1}^{\infty} F_{m}.
$$

Entonces $$F_{\varepsilon}$$ es cerrado, por ser intersección de cerrados, y

$$
m(E \setminus F_{\varepsilon}) = m\left( E \cap \bigcup_{m=1}^{\infty} F_{m}^{c} \right) \leq \sum_{m=1}^{\infty} m(E \setminus F_{m}) < \sum_{m=1}^{\infty} \frac{\varepsilon}{2^{m}} = \varepsilon.
$$

Veamos que la convergencia es uniforme en $$F_{\varepsilon}$$. Dado $$\delta > 0$$, tome $$m \geq 1$$ con $$\tfrac{1}{m} < \delta$$. Si $$x \in F_{\varepsilon} \subseteq F_{m}$$ y $$k \geq \kappa_{m}^{\varepsilon}$$, entonces

$$
|f(x) - f_{k}(x)| < \frac{1}{m} < \delta.
$$

Como $$\kappa_{m}^{\varepsilon}$$ no depende de $$x$$, concluimos que $$f_{k} \to f$$ uniformemente en $$F_{\varepsilon}$$.

## El teorema de Lusin

### Definición (Propiedad $$C$$ de una función)

Una función $$f : E \to \mathbb{R}$$ tiene la *propiedad $$C$$* en $$E$$ si dado $$\varepsilon > 0$$, existe un $$F \subseteq E$$ cerrado tal que

1. $$m(E \setminus F) < \varepsilon$$;
2. $$f$$ es continua relativa a $$F$$, es decir, $$f : F \to \mathbb{R}$$ es continua.

### Nota (Caracterización secuencial de la continuidad relativa)

La segunda condición de la definición anterior es equivalente a que si $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ con

$$
\lim_{n \to \infty} x_{n} = x \in F,
$$

entonces

$$
\lim_{n \to \infty} f(x_{n}) = f(x).
$$

### Lema (Las funciones simples medibles tienen la propiedad $$C$$)

Sea $$\phi$$ una función simple y medible en $$E$$. Entonces $$\phi$$ tiene la propiedad $$C$$.

***Prueba:*** Escribamos

$$
\phi(x) = \sum_{\ell=1}^{m} b_{\ell} \mathbf{1}_{B_{\ell}}(x)
$$

con los $$B_{\ell} \subseteq E$$ medibles, $$B_{i} \cap B_{j} = \emptyset$$ y $$b_{i} \neq b_{j}$$ si $$i \neq j$$, y $$E = \bigcup_{\ell=1}^{m} B_{\ell}$$.

Dado $$\varepsilon > 0$$, por regularidad interna tome, para cada $$1 \leq \ell \leq m$$, un cerrado $$F_{\ell} \subseteq B_{\ell}$$ tal que

$$
m(B_{\ell} \setminus F_{\ell}) < \frac{\varepsilon}{m}.
$$

Entonces

$$
F = \bigcup_{\ell=1}^{m} F_{\ell}
$$

es cerrado, por ser unión finita de cerrados. Además, como los $$B_{\ell}$$ cubren $$E$$, tenemos que $$E \setminus F \subseteq \bigcup_{\ell=1}^{m} (B_{\ell} \setminus F_{\ell})$$, y por lo tanto

$$
m(E \setminus F) \leq \sum_{\ell=1}^{m} m(B_{\ell} \setminus F_{\ell}) < m \cdot \frac{\varepsilon}{m} = \varepsilon.
$$

Falta ver que $$\phi$$ es continua relativa a $$F$$. Tome $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ tal que

$$
\lim_{n \to \infty} x_{n} = y \in F.
$$

Entonces existe $$\ell_{0}$$ tal que $$y \in F_{\ell_{0}}$$. Afirmamos que, dado $$\ell \neq \ell_{0}$$, el conjunto

$$
\{x_{n}\}_{n=1}^{\infty} \cap F_{\ell}
$$

es finito. En caso contrario, existe una subsucesión

$$
\{x_{n_{k}}\}_{k=1}^{\infty} \subseteq F_{\ell} \quad \text{con} \quad \lim_{k \to \infty} x_{n_{k}} = y.
$$

Como $$F_{\ell}$$ es cerrado, esto implica que $$y \in F_{\ell}$$; pero $$F_{\ell} \cap F_{\ell_{0}} \subseteq B_{\ell} \cap B_{\ell_{0}} = \emptyset$$, lo que nos lleva a una contradicción.

Por lo tanto, como los $$x_{n}$$ están repartidos entre los $$F_{\ell}$$ y solo finitos caen fuera de $$F_{\ell_{0}}$$, existe $$k_{0}$$ tal que $$x_{n} \in F_{\ell_{0}}$$ para $$n \geq k_{0}$$. Entonces

$$
\phi(x_{n}) = b_{\ell_{0}} = \phi(y) \quad \text{para } n \geq k_{0},
$$

es decir,

$$
\lim_{n \to \infty} \phi(x_{n}) = \phi(y).
$$

### Teorema (Lusin: medibilidad equivale a la propiedad $$C$$)

Sea $$f : E \to \mathbb{R}$$ con $$E$$ medible. Entonces $$f$$ es medible si y solo si $$f$$ tiene la propiedad $$C$$ en $$E$$.

***Prueba:*** *Medible implica propiedad $$C$$, caso $$m(E) < \infty$$.* Sea $$f : E \to \mathbb{R}$$ medible; entonces existe $$\{f_{k}\}_{k=1}^{\infty}$$ una sucesión de funciones simples y medibles tales que

$$
\lim_{k \to \infty} f_{k}(x) = f(x)
$$

c.p.d. en $$E$$. Sea $$\varepsilon > 0$$. Por el lema anterior, para cada $$k \geq 1$$ existe $$F_{k} \subseteq E$$ cerrado que satisface

$$
m(E \setminus F_{k}) < \frac{\varepsilon}{2^{k+1}},
$$

y tal que $$f_{k}$$ es continua relativa a $$F_{k}$$. Como $$m(E) < \infty$$, por el teorema de Egorov existe $$F_{0} \subseteq E$$ cerrado tal que

$$
m(E \setminus F_{0}) < \frac{\varepsilon}{2} \qquad \text{y} \qquad \lim_{k \to \infty} f_{k} = f \ \text{uniformemente en } F_{0}.
$$

Si tomamos

$$
F = F_{0} \cap \bigcap_{k=1}^{\infty} F_{k},
$$

entonces $$F$$ es cerrado, y como

$$
E \setminus F = (E \setminus F_{0}) \cup \bigcup_{k=1}^{\infty} (E \setminus F_{k}),
$$

tenemos que

$$
m(E \setminus F) \leq m(E \setminus F_{0}) + \sum_{k=1}^{\infty} m(E \setminus F_{k}) < \frac{\varepsilon}{2} + \sum_{k=1}^{\infty} \frac{\varepsilon}{2^{k+1}} = \varepsilon.
$$

Cada $$f_{k}$$ es continua relativa a $$F_{k} \supseteq F$$, y por lo tanto continua relativa a $$F$$. Como

$$
\lim_{k \to \infty} f_{k} = f
$$

uniformemente en $$F$$, y el límite uniforme de funciones continuas es continuo, tenemos que $$f$$ es continua relativa a $$F$$.

*Medible implica propiedad $$C$$, caso $$m(E) = \infty$$.* Llamemos

$$
E_{k} = E \cap \{ x \in \mathbb{R}^{d} :\ k-1 \leq |x| < k \}, \quad k \geq 1.
$$

Los $$E_{k}$$ son medibles, disjuntos dos a dos, cubren $$E$$ y $$m(E_{k}) \leq m(B(0,k)) < \infty$$. Por el caso anterior, para cada $$k$$ existe $$F_{k} \subseteq E_{k}$$ cerrado tal que $$f$$ es continua relativa a $$F_{k}$$ y

$$
m(E_{k} \setminus F_{k}) \leq \frac{\varepsilon}{2^{k}}.
$$

Tome

$$
F = \bigcup_{k=1}^{\infty} F_{k}.
$$

Como $$E \setminus F \subseteq \bigcup_{k=1}^{\infty} (E_{k} \setminus F_{k})$$, tenemos que $$m(E \setminus F) \leq \sum_{k=1}^{\infty} \varepsilon/2^{k} = \varepsilon$$.

Veamos que $$F$$ es cerrado. Sea $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ con $$\lim_{n \to \infty} x_{n} = y \in \mathbb{R}^{d}$$. Como la sucesión converge, es acotada: existe $$k_{0}$$ tal que

$$
n \geq k_{0} \implies |x_{n}| \leq |y| + 1.
$$

Sea $$M$$ un entero con $$M \geq |y| + 2$$. Si $$x_{n} \in F_{k} \subseteq E_{k}$$ con $$n \geq k_{0}$$, entonces $$k - 1 \leq |x_{n}| \leq |y| + 1$$, es decir $$k \leq |y| + 2 \leq M$$. Por lo tanto

$$
x_{n} \in \bigcup_{k=1}^{M} F_{k} \quad \text{para } n \geq k_{0},
$$

que es una unión finita de cerrados y por ende un cerrado. Entonces $$y \in \bigcup_{k=1}^{M} F_{k} \subseteq F$$, y $$F$$ es cerrado.

Veamos que $$f$$ es continua relativa a $$F$$. Sea $$\{x_{n}\}_{n=1}^{\infty} \subseteq F$$ con $$\lim_{n \to \infty} x_{n} = y \in F$$. Por lo anterior, existe $$k_{0}$$ tal que $$x_{n} \in \bigcup_{k=1}^{M} F_{k}$$ para $$n \geq k_{0}$$. Como los $$F_{k}$$ son cerrados y disjuntos dos a dos, por el argumento de la prueba del lema anterior existen $$k_{1}$$ y $$\ell_{1}$$ tales que

$$
n \geq k_{1} \implies x_{n} \in F_{\ell_{1}},
$$

con $$y \in F_{\ell_{1}}$$. Como $$f$$ es continua relativa a $$F_{\ell_{1}}$$, concluimos que $$\lim_{n \to \infty} f(x_{n}) = f(y)$$.

*Propiedad $$C$$ implica medible.* Si $$f$$ posee la propiedad $$C$$, entonces para cada $$k \geq 1$$ existe $$F_{k} \subseteq E$$ cerrado que satisface:

1. $$m(E \setminus F_{k}) < \frac{1}{k}$$;
2. $$f$$ es continua relativa a $$F_{k}$$.

Sea

$$
H = \bigcup_{k=1}^{\infty} F_{k},
$$

entonces $$H \subseteq E$$ y $$m(E \setminus H) = 0$$ (ejercicio; véase el ejercicio siguiente). Escribamos $$Z = E \setminus H$$. Finalmente, para cada $$a \in \mathbb{R}$$,

$$
\begin{aligned}
\{ x \in E :\ f(x) > a \} &= \{ x \in H :\ f(x) > a \} \cup \{ x \in Z :\ f(x) > a \} \\
&= \bigcup_{k=1}^{\infty} \{ x \in F_{k} :\ f(x) > a \} \cup \{ x \in Z :\ f(x) > a \}.
\end{aligned}
$$

Cada $$\{ x \in F_{k} :\ f(x) > a \}$$ es medible: como $$f$$ es continua relativa a $$F_{k}$$, este conjunto es abierto relativo a $$F_{k}$$, es decir, de la forma $$F_{k} \cap G$$ con $$G$$ abierto de $$\mathbb{R}^{d}$$, que es medible. Por otra parte, $$\{ x \in Z :\ f(x) > a \} \subseteq Z$$ tiene medida exterior cero y es por lo tanto medible. Entonces $$\{ f > a \}$$ es medible para todo $$a \in \mathbb{R}$$, es decir, $$f$$ es medible.

### Ejercicio (El complemento de la unión de los $$F_{k}$$ es nulo)

Con la notación de la prueba anterior, muestre que si $$H = \bigcup_{k=1}^{\infty} F_{k}$$ con $$m(E \setminus F_{k}) < \tfrac{1}{k}$$ para todo $$k \geq 1$$, entonces $$m(E \setminus H) = 0$$.
{% endraw %}
