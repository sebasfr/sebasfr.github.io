---
layout: chapter
course: ma0505
chapter: 13
title: "La medida de Lebesgue"
slug: 13-la-medida-de-lebesgue
toc:
  sidebar: right
lang: es
permalink: /notes/ma0505/es/13-la-medida-de-lebesgue/
---

{% raw %}
## Cerrados, complementos y la sigma-álgebra de los medibles

### Ejercicio (Descomposición de un abierto en cajas casi disjuntas)

Pruebe que todo abierto $$G \subseteq \mathbb{R}^{d}$$ se escribe como $$G = \bigcup_{k=1}^{\infty} I_{k}$$, con $$I_{k} = [a_{1}^{k}, b_{1}^{k}] \times \dots \times [a_{d}^{k}, b_{d}^{k}]$$ cajas cerradas de interiores disjuntos dos a dos.

### Teorema (Todo conjunto cerrado es medible)

Sea $$F \subseteq \mathbb{R}^{d}$$ cerrado. Entonces $$F$$ es medible.

***Prueba:*** *Caso compacto.* Suponga primero $$F$$ compacto, de modo que $$m_{e}(F) < \infty$$. Dado $$\varepsilon > 0$$, por aproximación existe un abierto $$G \supseteq F$$ con $$m_{e}(G) \leq m_{e}(F) + \tfrac{\varepsilon}{2}$$. El abierto $$G \setminus F$$ se descompone como unión numerable de cajas cerradas $$\{I_{k}\}$$ de interiores disjuntos. Para cada $$\ell$$, los compactos disjuntos $$F$$ y $$\bigcup_{k=1}^{\ell} I_{k}$$ están a distancia positiva, luego por aditividad a distancia positiva

$$
m_{e}(F) + m_{e}\Big(\bigcup_{k=1}^{\ell} I_{k}\Big) = m_{e}\Big(F \cup \bigcup_{k=1}^{\ell} I_{k}\Big) \leq m_{e}(G),
$$

de donde $$\sum_{k=1}^{\ell} m_{e}(I_{k}) = m_{e}\big(\bigcup_{k=1}^{\ell} I_{k}\big) \leq m_{e}(G) - m_{e}(F) \leq \tfrac{\varepsilon}{2}$$ para todo $$\ell$$. Por tanto $$\sum_{k=1}^{\infty} m_{e}(I_{k}) \leq \tfrac{\varepsilon}{2}$$ y, por subaditividad, $$m_{e}(G \setminus F) \leq \sum_{k} m_{e}(I_{k}) < \varepsilon$$. Así $$F$$ es medible.

*Caso general.* Si $$F$$ es cerrado cualquiera, $$F = \bigcup_{k=1}^{\infty} F_{k}$$ con $$F_{k} = F \cap \overline{B(0,k)}$$ compacto; cada $$F_{k}$$ es medible y, por ser unión numerable de medibles, $$F$$ es medible.

### Teorema (El complemento de un conjunto medible es medible)

Si $$E \subseteq \mathbb{R}^{d}$$ es medible, entonces $$E^{c}$$ es medible.

***Prueba:*** Para cada $$k \geq 1$$ existe un abierto $$G_{k} \supseteq E$$ con $$m_{e}(G_{k} \setminus E) < \tfrac{1}{k}$$. Cada $$G_{k}^{c}$$ es cerrado, luego medible, y $$H = \bigcup_{k} G_{k}^{c}$$ es medible con

$$
H = \bigcup_{k} G_{k}^{c} = \Big(\bigcap_{k} G_{k}\Big)^{c} \subseteq E^{c}.
$$

Además $$E^{c} \setminus H \subseteq E^{c} \setminus G_{k}^{c} = E^{c} \cap G_{k} = G_{k} \setminus E$$, de modo que $$m_{e}(E^{c} \setminus H) \leq \tfrac{1}{k}$$ para todo $$k$$; luego $$Z = E^{c} \setminus H$$ tiene medida exterior cero (y es medible). Finalmente $$E^{c} = H \cup Z$$ es unión de medibles, luego medible.

### Definición ($$\sigma$$-álgebra)

Sea $$\Omega$$ un conjunto. Una *$$\sigma$$-álgebra* $$\mathcal{F} \subseteq 2^{\Omega}$$ satisface:

1. $$\Omega \in \mathcal{F}$$;
2. si $$E \in \mathcal{F}$$, entonces $$E^{c} \in \mathcal{F}$$;
3. si $$\{F_{k}\}_{k=1}^{\infty} \subseteq \mathcal{F}$$, entonces $$\bigcup_{k} F_{k} \in \mathcal{F}$$.

### Lema (Cerradura de una $$\sigma$$-álgebra bajo intersecciones y diferencias)

Sea $$\mathcal{F}$$ una $$\sigma$$-álgebra y $$\{E_{k}\}_{k=1}^{\infty} \subseteq \mathcal{F}$$. Entonces $$\bigcap_{k} E_{k} \in \mathcal{F}$$, $$E_{1} \setminus E_{2} \in \mathcal{F}$$ y $$\emptyset \in \mathcal{F}$$.

***Prueba:*** Ejercicio.

### Lema (Los conjuntos medibles forman una $$\sigma$$-álgebra)

La familia $$\mathcal{M} = \{E \subseteq \mathbb{R}^{d} : E \text{ medible}\}$$ es una $$\sigma$$-álgebra.

***Prueba:*** $$\mathbb{R}^{d}$$ es abierto, luego medible. La cerradura bajo complemento y bajo unión numerable son los dos teoremas anteriores. Por tanto $$\mathcal{M}$$ satisface las tres condiciones; en particular contiene intersecciones numerables y diferencias $$E_{1} \setminus E_{2} = E_{1} \cap E_{2}^{c}$$ de medibles.

### Definición ($$\sigma$$-álgebra generada)

Dada $$\mathcal{S} \subseteq 2^{\Omega}$$, la *$$\sigma$$-álgebra generada por $$\mathcal{S}$$* es

$$
\sigma(\mathcal{S}) = \bigcap_{\substack{\mathcal{F}\ \sigma\text{-álgebra} \\ \mathcal{S} \subseteq \mathcal{F}}} \mathcal{F},
$$

la menor $$\sigma$$-álgebra que contiene a $$\mathcal{S}$$ (la intersección de $$\sigma$$-álgebras es una $$\sigma$$-álgebra).

## Borelianos y caracterización por cerrados

### Definición ($$\sigma$$-álgebra de Borel)

La *$$\sigma$$-álgebra de Borel* $$\mathcal{B}$$ es la $$\sigma$$-álgebra generada por los abiertos de $$\mathbb{R}^{d}$$. Por ser $$\sigma$$-álgebra, $$\mathcal{B}$$ contiene a los cerrados, a los conjuntos $$G_{\delta}$$ y $$F_{\sigma}$$, y $$\mathcal{B} \subseteq \mathcal{M}$$.

### Lema (Caracterización de la medibilidad por cerrados interiores)

Sea $$E \subseteq \mathbb{R}^{d}$$. Entonces $$E$$ es medible si y sólo si para todo $$\varepsilon > 0$$ existe un cerrado $$F \subseteq E$$ con $$m_{e}(E \setminus F) < \varepsilon$$.

***Prueba:*** $$E$$ es medible si y sólo si $$E^{c}$$ lo es. Dado $$\varepsilon > 0$$, si $$E^{c}$$ es medible existe un abierto $$G \supseteq E^{c}$$ con $$m_{e}(G \setminus E^{c}) < \varepsilon$$. Tome $$F = G^{c}$$, cerrado y $$F \subseteq E$$. Entonces

$$
m_{e}(E \setminus F) = m_{e}(E \cap F^{c}) = m_{e}(E \cap G) = m_{e}(G \setminus E^{c}) < \varepsilon.
$$

Recíprocamente, si existen tales cerrados $$F \subseteq E$$, entonces sus complementos abiertos $$F^{c} \supseteq E^{c}$$ cumplen $$m_{e}(F^{c} \setminus E^{c}) = m_{e}(E \setminus F) < \varepsilon$$, de modo que $$E^{c}$$ es medible y por tanto $$E$$ también.

## sigma-aditividad y continuidad de la medida

### Teorema ($$\sigma$$-aditividad de la medida de Lebesgue)

Sea $$\{E_{k}\}_{k=1}^{\infty}$$ una familia numerable de conjuntos medibles disjuntos dos a dos. Entonces

$$
m\left(\bigcup_{k=1}^{\infty} E_{k}\right) = \sum_{k=1}^{\infty} m(E_{k}).
$$

***Prueba:*** La desigualdad $$\leq$$ es la subaditividad. Para $$\geq$$, suponga primero cada $$E_{k}$$ acotado. Dado $$\varepsilon > 0$$, por la caracterización por cerrados existe un cerrado (y acotado, luego compacto) $$F_{k} \subseteq E_{k}$$ con $$m(E_{k} \setminus F_{k}) < \varepsilon/2^{k}$$. Los $$F_{k}$$ son compactos disjuntos, luego a distancia positiva dos a dos, y por aditividad a distancia positiva (e inducción),

$$
\sum_{i=1}^{m} m(F_{i}) = m\Big(\bigcup_{i=1}^{m} F_{i}\Big) \leq m\Big(\bigcup_{i=1}^{\infty} E_{i}\Big) \qquad \text{para todo } m,
$$

de donde $$\sum_{i=1}^{\infty} m(F_{i}) \leq m\big(\bigcup_{i} E_{i}\big)$$. Como $$m(E_{k}) \leq m(F_{k}) + \varepsilon/2^{k}$$,

$$
\sum_{i=1}^{\infty} m(E_{i}) - \varepsilon \leq \sum_{i=1}^{\infty} m(F_{i}) \leq m\Big(\bigcup_{i} E_{i}\Big),
$$

y haciendo $$\varepsilon \to 0$$ se obtiene $$\sum_{i} m(E_{i}) \leq m\big(\bigcup_{i} E_{i}\big)$$. El caso general (conjuntos no acotados) se reduce a este partiendo cada $$E_{k}$$ en las coronas $$E_{k} \cap (\overline{B(0,n)} \setminus B(0,n-1))$$ y queda como ejercicio.

### Nota (Monotonía y resta de medidas)

Si $$E_{1} \subseteq E_{2}$$ son medibles, entonces $$m(E_{2}) = m(E_{1}) + m(E_{2} \setminus E_{1})$$; en particular $$m(E_{1}) \leq m(E_{2})$$, y si $$m(E_{1}) < \infty$$,

$$
m(E_{2} \setminus E_{1}) = m(E_{2}) - m(E_{1}).
$$

### Teorema (Continuidad de la medida)

Sea $$\{E_{k}\}_{k=1}^{\infty}$$ una sucesión de conjuntos medibles.

1. Si $$E_{i} \subseteq E_{i+1}$$ para todo $$i$$, entonces $$\displaystyle m\Big(\bigcup_{i=1}^{\infty} E_{i}\Big) = \lim_{k \to \infty} m(E_{k})$$.
2. Si $$E_{i+1} \subseteq E_{i}$$ para todo $$i$$ y existe $$i_{0}$$ con $$m(E_{i_{0}}) < \infty$$, entonces $$\displaystyle m\Big(\bigcap_{i=1}^{\infty} E_{i}\Big) = \lim_{i \to \infty} m(E_{i})$$.

***Prueba:*** *(i).* Con $$E_{0} = \emptyset$$, los conjuntos $$E_{i} \setminus E_{i-1}$$ son medibles, disjuntos y $$\bigcup_{i} E_{i} = \bigsqcup_{i} (E_{i} \setminus E_{i-1})$$. Por $$\sigma$$-aditividad y telescopaje,

$$
m\Big(\bigcup_{i} E_{i}\Big) = \sum_{i=1}^{\infty} m(E_{i} \setminus E_{i-1}) = \lim_{n \to \infty}\sum_{i=1}^{n}\big(m(E_{i}) - m(E_{i-1})\big) = \lim_{n \to \infty} m(E_{n}),
$$

donde el telescopaje es válido cuando los $$m(E_{i})$$ son finitos; si algún $$m(E_{n}) = \infty$$, ambos lados valen $$\infty$$ por monotonía.

*(ii).* Descartando los primeros términos se puede suponer $$i_{0} = 1$$, de modo que $$m(E_{i}) \leq m(E_{1}) < \infty$$ para todo $$i$$. Sea $$E = \bigcap_{i} E_{i}$$. Entonces $$E_{1} = E \sqcup \bigsqcup_{i \geq 1}(E_{i} \setminus E_{i+1})$$, así que

$$
m(E_{1}) = m(E) + \sum_{i=1}^{\infty}\big(m(E_{i}) - m(E_{i+1})\big) = m(E) + \lim_{n \to \infty}\big(m(E_{1}) - m(E_{n})\big) = m(E) + m(E_{1}) - \lim_{n} m(E_{n}).
$$

Como $$m(E_{1}) < \infty$$ se cancela, y $$m(E) = \lim_{n} m(E_{n})$$.

### Ejemplo (La finitud es necesaria en la continuidad por arriba)

La hipótesis $$m(E_{i_{0}}) < \infty$$ no puede omitirse: con $$E_{k} = [-k, k]^{c} \subseteq \mathbb{R}$$ se tiene $$E_{k+1} \subseteq E_{k}$$, $$m(E_{k}) = \infty$$ para todo $$k$$, pero $$\bigcap_{k} E_{k} = \emptyset$$, de modo que $$m\big(\bigcap_{k} E_{k}\big) = 0 \neq \infty = \lim_{k} m(E_{k})$$.

### Teorema (Continuidad exterior por abajo para conjuntos arbitrarios)

Si $$E_{k} \subseteq E_{k+1} \subseteq \mathbb{R}^{d}$$ para todo $$k$$ (sin suponerlos medibles), entonces

$$
m_{e}\left(\bigcup_{k=1}^{\infty} E_{k}\right) = \lim_{k \to \infty} m_{e}(E_{k}).
$$

***Prueba:*** Para cada $$k$$ tome un conjunto $$G_{\delta}$$, $$G_{k} \supseteq E_{k}$$, con $$m_{e}(E_{k}) = m(G_{k})$$. Los $$G_{k}$$ no tienen por qué estar encajados, así que se define $$V_{k} = \bigcap_{j=k}^{\infty} G_{j}$$, medible y con $$V_{k} \subseteq V_{k+1}$$. Como $$E_{k} \subseteq E_{k+\ell} \subseteq G_{k+\ell}$$ para todo $$\ell \geq 0$$, resulta $$E_{k} \subseteq \bigcap_{j \geq k} G_{j} = V_{k}$$. Por monotonía, $$m_{e}(E_{k}) \leq m(V_{k}) \leq m(G_{k}) = m_{e}(E_{k})$$, luego $$m(V_{k}) = m_{e}(E_{k})$$. Finalmente, usando $$\bigcup_{k} E_{k} \subseteq \bigcup_{k} V_{k}$$ y la continuidad por abajo (para los medibles $$V_{k}$$),

$$
m_{e}\Big(\bigcup_{k} E_{k}\Big) \leq m\Big(\bigcup_{k} V_{k}\Big) = \lim_{k \to \infty} m(V_{k}) = \lim_{k \to \infty} m_{e}(E_{k}).
$$

La desigualdad opuesta es la monotonía: $$m_{e}(E_{m}) \leq m_{e}\big(\bigcup_{k} E_{k}\big)$$ para todo $$m$$, luego $$\lim_{m} m_{e}(E_{m}) \leq m_{e}\big(\bigcup_{k} E_{k}\big)$$.

## Caracterizaciones de la medibilidad

### Teorema (Caracterización por $$G_{\delta}$$ y $$F_{\sigma}$$ módulo medida cero)

Sea $$E \subseteq \mathbb{R}^{d}$$. Las siguientes condiciones son equivalentes:

1. $$E$$ es medible;
2. $$E = H \setminus Z$$, donde $$H$$ es de tipo $$G_{\delta}$$ y $$m_{e}(Z) = 0$$;
3. $$E = H \cup Z$$, donde $$H$$ es de tipo $$F_{\sigma}$$ y $$m_{e}(Z) = 0$$.

***Prueba:*** $$(ii) \Rightarrow (i)$$ y $$(iii) \Rightarrow (i)$$ son inmediatas, pues los conjuntos $$G_{\delta}$$ y $$F_{\sigma}$$ son medibles y los de medida exterior cero también, y $$\mathcal{M}$$ es cerrada bajo diferencias y uniones. Probamos $$(i) \Rightarrow (ii)$$. Si $$E$$ es medible, para cada $$k$$ existe un abierto $$G_{k} \supseteq E$$ con $$m_{e}(G_{k} \setminus E) < \tfrac{1}{k}$$. Sea $$H = \bigcap_{k} G_{k}$$, de tipo $$G_{\delta}$$ con $$E \subseteq H$$. Entonces $$m_{e}(H \setminus E) \leq m_{e}(G_{k} \setminus E) < \tfrac{1}{k}$$ para todo $$k$$, luego $$m_{e}(H \setminus E) = 0$$ y $$E = H \setminus Z$$ con $$Z = H \setminus E$$. La implicación $$(i) \Rightarrow (iii)$$ es análoga (usando la caracterización por cerrados interiores) y queda como ejercicio.

### Ejercicio (Caracterización por casi-uniones de intervalos)

Sea $$E \subseteq \mathbb{R}^{d}$$ con $$m_{e}(E) < \infty$$. Pruebe que $$E$$ es medible si y sólo si para todo $$\varepsilon > 0$$ existen $$\widetilde{S}, N_{1}, N_{2}$$ tales que $$E = (\widetilde{S} \cup N_{1}) \setminus N_{2}$$, con $$\widetilde{S} = \bigcup_{k} I_{k}$$ ($$I_{k} \in S_{d}$$), $$m_{e}(N_{1}) < \varepsilon$$ y $$m_{e}(N_{2}) < \varepsilon$$.

### Teorema (Criterio de Carathéodory)

$$E \subseteq \mathbb{R}^{d}$$ es medible si y sólo si para todo $$A \subseteq \mathbb{R}^{d}$$

$$
m_{e}(A) = m_{e}(A \cap E) + m_{e}(A \setminus E).
$$

***Prueba:*** *($$\Rightarrow$$).* Sea $$E$$ medible y $$A \subseteq \mathbb{R}^{d}$$. Tome un $$G_{\delta}$$, $$H \supseteq A$$, con $$m_{e}(A) = m(H)$$. Como $$H$$ y $$E$$ son medibles, $$H \cap E$$ y $$H \setminus E$$ son medibles, disjuntos y de unión $$H$$, de modo que $$m(H) = m(H \cap E) + m(H \setminus E)$$. Usando $$A \cap E \subseteq H \cap E$$ y $$A \setminus E \subseteq H \setminus E$$,

$$
m_{e}(A) = m(H) = m(H \cap E) + m(H \setminus E) \geq m_{e}(A \cap E) + m_{e}(A \setminus E).
$$

La desigualdad opuesta es la subaditividad, así que hay igualdad.

*($$\Leftarrow$$).* Suponga que la identidad vale para todo $$A$$. Si $$m_{e}(E) < \infty$$, tome un $$G_{\delta}$$, $$H \supseteq E$$, con $$m(H) = m_{e}(E)$$ y aplique la hipótesis a $$A = H$$: como $$E \subseteq H$$, $$H \cap E = E$$ y

$$
m_{e}(H) = m_{e}(E) + m_{e}(H \setminus E),
$$

de donde $$m_{e}(H \setminus E) = 0$$. Entonces $$H \setminus E$$ es medible y $$E = H \setminus (H \setminus E)$$ es medible. Si $$m_{e}(E) = \infty$$, sea $$E_{k} = E \cap B(0,k)$$ y $$H_{k}$$ un $$G_{\delta}$$ con $$E_{k} \subseteq H_{k}$$, $$m(H_{k}) = m_{e}(E_{k})$$. Aplicando la hipótesis a $$A = H_{k}$$ y usando $$E_{k} \subseteq H_{k} \cap E$$,

$$
m_{e}(H_{k}) = m_{e}(H_{k} \cap E) + m_{e}(H_{k} \setminus E) \geq m_{e}(E_{k}) + m_{e}(H_{k} \setminus E),
$$

y como $$m_{e}(H_{k}) = m_{e}(E_{k})$$, resulta $$m_{e}(H_{k} \setminus E) = 0$$. Con $$H = \bigcup_{k} H_{k}$$ (medible, $$E \subseteq H$$) se tiene $$m_{e}(H \setminus E) \leq \sum_{k} m_{e}(H_{k} \setminus E) = 0$$, luego $$E = H \setminus Z$$ con $$Z = H \setminus E$$ de medida cero, y $$E$$ es medible.

### Corolario (Aditividad respecto de un conjunto medible)

Sea $$E$$ medible con $$E \subseteq A \subseteq \mathbb{R}^{d}$$. Entonces $$m_{e}(A) = m(E) + m_{e}(A \setminus E)$$. Si además $$m(E) < \infty$$, entonces $$m_{e}(A \setminus E) = m_{e}(A) - m(E)$$.

***Prueba:*** Por el criterio de Carathéodory aplicado a $$A$$ y como $$E \subseteq A$$ implica $$A \cap E = E$$,

$$
m_{e}(A) = m_{e}(A \cap E) + m_{e}(A \setminus E) = m(E) + m_{e}(A \setminus E).
$$

Si $$m(E) < \infty$$ se despeja $$m_{e}(A \setminus E) = m_{e}(A) - m(E)$$.

### Teorema (Envoltura $$G_{\delta}$$ que respeta intersecciones con medibles)

Para todo $$E \subseteq \mathbb{R}^{d}$$ existe un conjunto $$G_{\delta}$$, $$H \supseteq E$$, tal que $$m(H \cap M) = m_{e}(E \cap M)$$ para todo conjunto medible $$M$$.

***Prueba:*** *Caso $$m_{e}(E) < \infty$$.* Sea $$H$$ de tipo $$G_{\delta}$$ con $$E \subseteq H$$ y $$m(H) = m_{e}(E)$$. Para $$M$$ medible, por Carathéodory (aplicado a $$H$$ y a $$E$$ respectivamente),

$$
m(H) = m(H \cap M) + m(H \setminus M), \qquad m_{e}(E) = m_{e}(E \cap M) + m_{e}(E \setminus M).
$$

Como $$E \cap M \subseteq H \cap M$$ y $$E \setminus M \subseteq H \setminus M$$ dan $$m_{e}(E \cap M) \leq m(H \cap M)$$ y $$m_{e}(E \setminus M) \leq m(H \setminus M)$$, y $$m(H) = m_{e}(E)$$, las dos descomposiciones suman lo mismo con cada término dominado: forzosamente $$m(H \cap M) = m_{e}(E \cap M)$$.

*Caso general.* Sea $$E_{k} = E \cap B(0,k)$$ y, por el caso anterior, $$G_{k}$$ de tipo $$G_{\delta}$$ con $$E_{k} \subseteq G_{k}$$ y $$m(G_{k} \cap M) = m_{e}(E_{k} \cap M)$$ para todo medible $$M$$. Poniendo $$H_{k} = \bigcap_{j \geq k} G_{j}$$ se obtiene $$E_{k} \subseteq H_{k}$$ y $$m_{e}(E_{k} \cap M) = m_{e}(H_{k} \cap M)$$. Como $$E_{k} \cap M \uparrow E \cap M$$ y $$H_{k} \cap M \uparrow$$, la continuidad por abajo da

$$
m_{e}(E \cap M) = \lim_{k} m_{e}(E_{k} \cap M) = \lim_{k} m_{e}(H_{k} \cap M) = m_{e}\Big(\bigcup_{k} H_{k} \cap M\Big).
$$

El conjunto $$\widetilde{H} = \bigcup_{k} H_{k}$$ es medible; escribiéndolo como $$\widetilde{H} = H \setminus Z$$ con $$H$$ de tipo $$G_{\delta}$$ y $$m_{e}(Z) = 0$$, se concluye $$m_{e}(E \cap M) = m_{e}(\widetilde{H} \cap M) = m(H \cap M)$$.

## El conjunto de Cantor

### Ejemplo (El conjunto de Cantor: cerrado, no numerable y de medida cero)

Sea $$C_{0} = [0,1]$$ y, recursivamente, $$C_{k+1}$$ el resultado de quitar a cada intervalo de $$C_{k}$$ su tercio central abierto; por ejemplo

$$
C_{1} = \Big[0, \tfrac{1}{3}\Big] \cup \Big[\tfrac{2}{3}, 1\Big], \qquad C_{2} = \Big[0, \tfrac{1}{9}\Big] \cup \Big[\tfrac{2}{9}, \tfrac{1}{3}\Big] \cup \Big[\tfrac{2}{3}, \tfrac{7}{9}\Big] \cup \Big[\tfrac{8}{9}, 1\Big].
$$

El *conjunto de Cantor* es $$C = \bigcap_{k=1}^{\infty} C_{k}$$.

![Los primeros pasos de la construcción del conjunto de Cantor](/assets/img/courses/ma0505/conjunto-de-cantor.svg)

Cada $$C_{k}$$ es cerrado, luego $$C$$ es cerrado y medible. Como en cada paso se conserva $$\tfrac{2}{3}$$ de la longitud, $$m(C_{k}) = (\tfrac{2}{3})^{k}$$, y al ser $$C_{k+1} \subseteq C_{k}$$ con $$m(C_{1}) < \infty$$, la continuidad por arriba da

$$
m(C) = \lim_{k \to \infty} m(C_{k}) = \lim_{k \to \infty}\Big(\tfrac{2}{3}\Big)^{k} = 0.
$$

### Ejercicio (Caracterización del conjunto de Cantor en base tres)

Para $$x \in [0,1]$$ con expansión $$x = \sum_{i=1}^{\infty} n_{i}/3^{i}$$, $$n_{i} \in \{0,1,2\}$$ (eligiendo, cuando hay dos expansiones, la que evita el dígito $$1$$ terminal), pruebe que $$x \in C_{k}$$ si y sólo si $$n_{1}, \dots, n_{k} \in \{0, 2\}$$; por tanto $$x \in C$$ si y sólo si $$n_{i} \in \{0,2\}$$ para todo $$i$$.

### Ejemplo (La función de Cantor y la no numerabilidad de $$C$$)

La *función de Cantor* $$\Phi : C \to [0,1]$$, $$\Phi\big(\sum_{i} n_{i}/3^{i}\big) = \sum_{i} \tfrac{n_{i}}{2}\,\tfrac{1}{2^{i}}$$ (con $$n_{i} \in \{0,2\}$$), está bien definida y es sobreyectiva sobre $$[0,1]$$. Como $$[0,1]$$ es no numerable, $$C$$ también lo es. Así, $$C$$ es un conjunto cerrado, no numerable y de medida de Lebesgue cero.

## Un conjunto no medible

### Lema (Lema de Steinhaus: $$E - E$$ contiene un intervalo)

Sea $$E \subseteq \mathbb{R}$$ medible con $$m(E) > 0$$. Entonces el conjunto $$E - E = \{x - y : x, y \in E\}$$ contiene un intervalo abierto centrado en $$0$$.

***Prueba:*** Se puede suponer $$m(E) < \infty$$ (reemplazando $$E$$ por $$E \cap [-R, R]$$ con $$R$$ grande, de medida positiva). Con $$\varepsilon = \tfrac{1}{3}$$, tome un abierto $$G \supseteq E$$ con $$m(G) < (1 + \varepsilon)m(E)$$ y escriba $$G = \bigcup_{k}[a_{k}, b_{k}]$$ con interiores disjuntos. Poniendo $$E_{k} = [a_{k}, b_{k}] \cap E$$ se tiene $$m(E) = \sum_{k} m(E_{k})$$ y

$$
\sum_{k} m([a_{k}, b_{k}]) = m(G) < (1 + \varepsilon)m(E) = (1 + \varepsilon)\sum_{k} m(E_{k}),
$$

luego existe $$k_{0}$$ con $$m(I) \leq (1 + \varepsilon)\, m(\widetilde{E})$$, donde $$I = [a_{k_{0}}, b_{k_{0}}]$$ y $$\widetilde{E} = E_{k_{0}}$$; en particular $$m(I) \leq \tfrac{4}{3} m(\widetilde{E})$$. Afirmamos que si $$|d| < \tfrac{1}{2} m(I)$$ entonces $$(\widetilde{E} - d) \cap \widetilde{E} \neq \emptyset$$. En efecto, si fuera $$(\widetilde{E} - d) \cap \widetilde{E} = \emptyset$$, entonces $$m\big(\widetilde{E} \cup (\widetilde{E} - d)\big) = 2 m(\widetilde{E})$$; pero $$\widetilde{E}$$ y $$\widetilde{E} - d$$ están ambos contenidos en un intervalo de longitud $$m(I) + |d| < \tfrac{3}{2} m(I)$$, así que $$2 m(\widetilde{E}) < \tfrac{3}{2} m(I)$$, esto es $$m(\widetilde{E}) < \tfrac{3}{4} m(I)$$, contradiciendo $$m(I) \leq \tfrac{4}{3}m(\widetilde{E})$$. Por tanto, para $$|d| < \tfrac{1}{2}m(I)$$ existen $$x, y \in \widetilde{E}$$ con $$x - d = y$$, es decir $$d \in \widetilde{E} - \widetilde{E} \subseteq E - E$$. Luego $$\big(-\tfrac{1}{2}m(I), \tfrac{1}{2}m(I)\big) \subseteq E - E$$.

### Nota (Invariancia por traslaciones de la medida exterior)

De la definición, $$m_{e}$$ es invariante por traslaciones: $$m_{e}(E + t) = m_{e}(E)$$ para todo $$t$$, pues trasladar un cubrimiento por cajas produce un cubrimiento por cajas del mismo volumen.

### Ejemplo (El conjunto de Vitali es no medible)

Defina sobre $$\mathbb{R}$$ la relación de equivalencia $$x \sim y \iff x - y \in \mathbb{Q}$$. La clase de $$x$$ es $$\{x + r : r \in \mathbb{Q}\}$$, numerable; por tanto hay una cantidad no numerable de clases. El *conjunto de Vitali* $$E$$ se obtiene escogiendo un representante de cada clase. Entonces $$E$$ es no numerable y $$(E - E) \cap \mathbb{Q} = \{0\}$$, pues dos elementos distintos de $$E$$ no son equivalentes y su diferencia es irracional. Si $$E$$ fuese medible: caso $$m(E) > 0$$ es imposible, porque por el lema de Steinhaus $$E - E$$ contendría un intervalo alrededor de $$0$$ y por ende racionales no nulos, contra $$(E - E) \cap \mathbb{Q} = \{0\}$$; luego $$m(E) = 0$$. Pero $$\mathbb{R} = \bigcup_{r \in \mathbb{Q}}(E + r)$$, y por invariancia por traslaciones y subaditividad

$$
m_{e}(\mathbb{R}) \leq \sum_{r \in \mathbb{Q}} m_{e}(E + r) = \sum_{r \in \mathbb{Q}} m_{e}(E) = 0,
$$

absurdo. Por tanto $$E$$ no es medible.

### Corolario (Todo conjunto de medida exterior positiva contiene un no medible)

Sea $$A \subseteq \mathbb{R}$$ con $$m_{e}(A) > 0$$. Entonces existe $$E \subseteq A$$ no medible.

***Prueba:*** Con $$E$$ el conjunto de Vitali, $$\mathbb{R} = \bigsqcup_{r \in \mathbb{Q}}(E + r)$$, de modo que $$A = \bigcup_{r \in \mathbb{Q}} A_{r}$$ con $$A_{r} = A \cap (E + r)$$. Cada $$A_{r} - A_{r} \subseteq (E + r) - (E + r) = E - E$$, luego $$(A_{r} - A_{r}) \cap \mathbb{Q} = \{0\}$$; por el lema de Steinhaus, si $$A_{r}$$ fuera medible no podría tener medida positiva, así que $$m(A_{r}) = 0$$. Si todos los $$A_{r}$$ fueran medibles, por subaditividad $$m_{e}(A) \leq \sum_{r} m_{e}(A_{r}) = 0$$, contradiciendo $$m_{e}(A) > 0$$. Por tanto algún $$A_{r} \subseteq A$$ es no medible.
{% endraw %}
