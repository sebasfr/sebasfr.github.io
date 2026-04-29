---
layout: chapter
course: ma0450
chapter: 4
title: "Integración en Rn"
slug: 04-integracion-en-rn
toc:
  sidebar: right
lang: es
---

{% raw %}
La noción general de la integral de Riemann en una variable es aproximar el área bajo el gráfico mediante el cálculo de áreas rectangulares entre particiones. ¿Cómo podemos trasladar esta idea a funciones de varias variables?

## Introducción
Sea $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, con $$f$$ acotada y $$D$$ acotado. Si $$f: D \subseteq \mathbb{R}^{2} \to \mathbb{R}$$, con $$f(x,y)>0$$, buscamos que $$\int \int_{D} f(x,y) dx dy$$ represente el volumen bajo $$f$$.

### Definición (Caja en $$\mathbb{R}^{n}$$)
Definimos una caja como $$C:[a_{1},b_{1}] \times [a_{2},b_{2}] \times...\times[a_{n}, b_{n}] \subseteq \mathbb{R}^n$$.
1. El volumen de $$C$$ viene dado por $$V(C) = \prod_{i=1}^{n} (b_{i}-a_{i})$$.
2. Las caras de la caja vienen dadas por los conjuntos de la forma 


$$
[a_{1},b_{1}] \times \dots \times [a_{i-1}, b_{i-1}] \times \{ a_{i} \} \times [a_{i+1}, b_{i+1}] \times \dots \times [a_{n}, b_{n}]
$$




$$
[a_{1},b_{1}] \times \dots \times [a_{i-1}, b_{i-1}] \times \{ b_{i} \} \times [a_{i+1}, b_{i+1}] \times \dots \times [a_{n}, b_{n}]
$$


para $$i \in \{ 1,\dots,n \}$$.
3. $$D \subseteq \mathbb{R}^n$$ tiene volumen cero si para todo $$\varepsilon>0$$ existe una colección finita de cajas$$\{ C_{i} \}_{i=1}^{k}$$ tales que $$D \subseteq \bigcup_{i=1}^{k} C_{i}$$ y $$\sum_{i=1}^{k} V(C_{i}) < \varepsilon$$.
La idea es primero definir $$\int_{C} f(x)$$ sobre cajas.

#### Ejemplo 
Para $$n=2$$, sea $$f:[a_{1}, b_{1}]\to \mathbb{R}$$ continua. Defina $$G_{f} = \{ (x, f(x)): x \in [a_{1}, b_{1}] \}\subseteq R_{2}$$. Probaremos que $$G_{f}$$ tiene volumen cero. Sea $$\varepsilon>0$$. Como $$f$$ es continua en $$G_{f}$$ y $$G_{f}$$ es compacto, $$f$$ es uniformemente continua. Luego, existe $$\delta>0$$ tal que para todos $$x,y \in D$$, si $$\lVert x-y \rVert<\delta \implies \lvert f(x) - f(y) \rvert < \frac{\varepsilon}{b-a}$$. Particione el intervalo $$[a_{1},b_{1}]$$ en $$m \in \mathbb{N}$$ intervalos iguales ($$a=x_{0}<x_{1}< \dots < x_{m} = b$$), de manera que $$\frac{b-a}{m} < \delta$$. Explícitamente, definimos $$x_{i} = a + i \frac{b-a}{m}$$ para $$i \in \{ 0,\dots,m \}$$. Es posible cubrir $$G_{f}$$ por cajas de la forma $$C_{i} = [x_{i-1}, x_{i}] \times J_{i}$$, con $$J_{i} = \left( \underset{x \in [x_{i-1}, x_{i}] }{\min f(x)}, \underset{x \in [x_{i-1}, x_{i}] }{\min f(x)}+ \frac{\varepsilon}{b-a} \right)$$. Así, $$G_{f} \subseteq \bigcup_{i=1}^{m} C_{i}$$ y 


$$
V(C_{i}) = \frac{b-a}{m} \frac{\varepsilon}{b-a} = \frac{\varepsilon}{m} \implies  \sum_{i=1}^{m} V(C_{i}) = m \frac{\varepsilon}{m} = \varepsilon. 
$$


![Cajas](/assets/img/courses/ma0450/Cajas.svg)

#### Ejercicio 
Para $$f:D =[a_{1}, b_{1}] \times [a_{2}, b_{2}] \to \mathbb{R}$$, defina $$G_{f} = \{ (x,y,f(x,y)):(x,y) \in D \} \subseteq \mathbb{R}^{3}$$. Mostrar que $$V(G_{f}) = 0$$.

### Definición (Partición de una caja)
Dada una caja $$C$$, una partición de $$C$$ es una colección finita de subcajas $$\{ C_{i} \}_{i=1}^{m}$$ obtenida a partir de particiones $$P_{i}$$ de $$[a_{i},b_{i}]$$. Es decir, si $$C= \prod_{i=1}^{n} [a_{i}, b_{i}]$$, tomamos para cada $$i$$ una partición $$P_{i} = \{ a_{i} = x_{0}^{i} < \dots < x_{\ell_{i}}^{i} = b_{i}\}$$, definiendo las subcajas $$\prod_{i=1}^{n} [x_{m_{i}}^{i}, x_{m_{i}+1}^{i}]$$.

### Definición (Refinamiento)
Dada $$C$$ una caja, $$P, Q$$ particiones de $$C$$. Decimos que $$P$$ es un refinamiento de $$Q$$ ($$P$$ es más fina que $$Q$$) y escribimos $$P \leq Q$$ si cada subcaja de $$Q$$ es la unión finita de subcajas de $$P$$.

#### Nota
Dadas $$P = \{ C_{1},\dots,C_{m} \}$$, $$Q=\{ D_{1},\dots, D_{n} \}$$, aún si no existe relación de refinamiento entre ellas, se puede construir un refinamiento $$R = \{ C_{i} \cap D_{j}, 1\leq i\leq m, 1\leq j\leq n \}$$, con $$R\leq P$$ y $$R \leq Q$$.

### Definición (Conjunto de Jordan)
Sea $$K \subseteq \mathbb{R}^n$$. Decimos que $$K$$ es un conjunto de Jordan si $$K$$ es acotado y $$V(\partial K) = 0$$. 

#### Ejemplo 
Toda caja es de Jordan. 

#### Ejemplo 
Dada una caja $$C \subseteq \mathbb{R}^n$$, $$f,g: C \to \mathbb{R}$$ continuas, 


$$
K = \{ (x, x_{n+1}) \in \mathbb{R}^{n+1}: f(x) \leq x_{n+1} \leq  g(x) \}
$$


es de Jordan. Nos interesa porque es el volumen entre dos funciones.

![Conjunto Jordan](/assets/img/courses/ma0450/Conjunto%20Jordan.svg)
### Definición (Volumen respecto a una partición)
Sean $$K \subseteq \mathbb{R}^n$$ de Jordan, $$K \subseteq C$$, $$C$$ caja. Dada $$P = \{ C_{1}, \dots, C_{m} \}$$ partición de $$C_{1}$$ se define el volumen $$K$$ cono respecto a $$P$$ como


$$
v(K,P) = \sum_{C_{j}\cap \bar{K}\neq \emptyset} v(C_{j}).
$$


Se toma $$v(\emptyset, P) = 0$$.
![volumen respecto a caja](/assets/img/courses/ma0450/volumen%20respecto%20a%20caja.svg)
#### Ejercicio

Para cualesquiera particiones $$P$$ y $$Q$$ con $$Q$$ más fina que $$P$$, dado un conjunto $$K$$ de Jordan, se cumple que 


$$
v(K,Q) \leq V(K,P).
$$



### Definición (Volumen de un conjunto)
Dado $$K$$ un conjunto de Jordan y $$C$$ una caja, el volumen de $$K$$ es 


$$
v(K) = \inf \{ v(K,P): \quad P \text{ patición de } C\}.
$$


Si $$K$$ es una caja, el volumen coincide con la definición de volumen de una caja.

### Lema (Independencia del volumen)
El volumen de $$K$$ es el mismo independientemente de la caja que se escoja.

***Prueba:***  Sean $$C,D$$ cajas que contienen a $$K$$. Basta considerar el caso en que $$K \subseteq C \subseteq D$$, (pues $$C \cap D$$ es una caja). Defina 


$$
\begin{aligned}
v_{C}(K) &= \inf \{ v(K,P): \quad P \text{ patición de } C\},\\
v_{D}(K) &=\inf \{ v(K,P): \quad P \text{ patición de } D\}.
\end{aligned}
$$


Como $$C \subseteq D$$, toda partición de $$C$$ se puede completar a una partición de $$D$$. Así, 


$$
v_{D}(K) \leq  v_{C}(K).
$$


Tome $$P = \{ C_{1}, \dots, C_{m} \}$$ partición de $$D$$. Al intersecar las cajas en $$P$$ con $$C$$, se obtiene un refinamiento $$Q = \{ D_{1}, \dots, D_{\ell} \}$$ de $$P$$. Sean $$Q_{C}$$ las subcajas que intersecan a $$C$$. Luego, 


$$
\begin{aligned}
v(K,P) &= {\sum_{C_{j} \in P, \, C_{j} \cap \bar{K} \neq \emptyset}} v(C_{j}) \quad  \geq  \quad \sum_{D_{j} \in Q, \, D_{j} \cap \bar{K} \neq  \emptyset} v(D_{j})\\
&= v(K, Q) = v(K, Q_{c}) \geq  v_{c}(K).
\end{aligned}
$$


Al tomar $$\inf$$ sobre $$P$$, tenemos que $$v_{D}(K) \geq v_{C}(K)$$. Así, se concluye que $$v_{D}(K) = v_{C}(K)$$.

#### Ejemplo 
Dada $$f:[a,b]\to \mathbb{R}^{+}$$ continua. Sean $$B=\{ (x,y)\in \mathbb{R}^{2}, a\leq x\leq b, 0\leq y\leq f(x)\}$$. Veamos que $$\int_{a}^{b} f(x) \, dx = v(B)$$.

***Prueba:*** Sea $$M>0$$ tal que $$B \subseteq [a,b] \times [0,M]$$. Sea $$\varepsilon>0$$. Como $$f$$ es uniformemente continua, tome $$\delta>0$$ tal que 


$$
\forall x,y \in [a,b], \lvert x-y \rvert < \delta \implies \lvert f(x) - f(y) \rvert < \varepsilon.
$$


Tome $$m > \frac{b-a}{\delta}$$ y considere la partición $$P_{x} = \{ a=x_{0} < x_{1} < \dots < x_{m} = b\}$$.= con $$x_{i+1} - x_{i} < \delta$$ . Luego, el gráfico de $$f$$ está cubierto por cajas $$C_{i} = [x_{i-1},x_{i}] \times J_{i}$$ con $$\lvert J_{i} \rvert < \varepsilon$$ para $$i \in \{ 1,\dots,m \}$$. Además, $$J_{i} \subseteq [0, M+\varepsilon]$$. Tome 


$$
Q = \{ \underbrace{ D_{1},\dots,D_{r} }_{ \text{cubrir gráfico} }, \underbrace{ E_{1},\dots, E_{p} }_{ \text{debajo del gráfico} }, \underbrace{ F_{1},\dots,F_{n} }_{ \text{encima del gráfico} } \}.
$$


Así 


$$
\begin{aligned}
\sum_{k=1}^{p} v(E_{k}) \leq  \int_{a}^{b} f(x) \, dx &\leq \sum_{k=1}^{p} v(E_{k})+ \sum_{k=1}^{r} v(D_{k}) = v(B,Q) = \sum_{C_{i} \cap \bar{K} \neq \emptyset} v(C_{i}) \\
\implies v(B,Q) - \int_{a}^{b} f(x) \, dx & \leq v(B,Q) - \sum_{k=1}^{p} v(D_{k}) = \sum_{k=1}^{r} v(D_{k}) \\
&= \sum_{i=1}^{m} v(C_{i}) = \sum_{i=1}^{m} (x_{i}-x_{i-1})\lvert J_{i} \rvert \\
&= \sum_{i=1}^{m} \frac{b-a}{m} \lvert J_{i} \rvert < \sum_{i=1}^{m} \frac{b-a}{m} \lvert \varepsilon \rvert   = \varepsilon(b-a).
\end{aligned} 
$$


Así, para todo $$\varepsilon>0$$ existe una partición $$Q$$ de $$[a,b] \times [0, M+\varepsilon]$$ tal que


$$
\int_{a}^{b} f(x) \, dx \leq v(B, Q) \leq \int_{a}^{b} f(x)  \, dx  + \varepsilon(b-a).
$$


Tomando ínfimo sobre $$Q$$, tenemos que $$\int_{a}^{b} f(x) \, dx = v(B)$$.


### Lema (Unión e intersección de conjuntos de Jordan)
Sean $$K_{1}, K_{2}$$ de Jordan en $$\mathbb{R}^n$$. Entonces:
1. $$K_{1} \cup K_{2}$$ y $$K_{1} \cap K_{2}$$ son de Jordan.
2. $$v(K_{1} \cup K_{2}) = v(K_{1}) + v(K_{2}) - v(K_{1} \cap K_{2})$$.

***Prueba:*** Para 1, note que $$K_{1} \cap K_{2}$$ y $$K_{1} \cup K_{2}$$ son acotados. Además, como $$\partial (K_{1} \cup K_{2}) \subseteq \partial K_{1} \cup \partial K_{2}$$ y $$\partial (K_{1} \cap K_{2}) \subseteq \partial K_{1} \cup \partial K_{2}$$, entonces $$K_{1} \cup K_{2}$$, $$K_{1} \cap K_{2}$$ son de Jordan.

### Definición (Suma de Riemann)
Dada $$f: C \subseteq \mathbb{R}^n \to \mathbb{R}$$ con $$C$$ caja. Sea $$P = \{ C_{1},\dots, C_{k} \}$$ una partición de $$C$$. Se define una suma de Riemann de $$f$$ con respecto a $$P$$ como una suma de la forma 


$$
S(f,P, \xi_{1},\dots,\xi_{k}) = \sum_{i=1}^{k} f(\xi_{i}) V(C_{i}), \quad \text{con }\xi_{i} \in C_{i}.
$$


Usualmente escribimos $$S(f,P, \xi_{1},\dots,\xi_{k}) = S(f,P)$$ por conveniencia.

#### Nota
1. Si $$f(\xi_{i}) = \underset{x \in C_{i}}{\sup} f(x)$$, se obtiene una suma superior, y si $$f(\xi_{i}) = \underset{x \in C_{i}}{\inf} f(x)$$.
2. Si $$f$$ es acotada ($$\forall x \in C   (m \leq f(x) \leq M)$$), $$m v(C) \leq S(f, P) \leq Mv(C)$$ para cualquier escogencia de $$\{ \xi_{i} \}_{i=1}^{n}$$.

### Definición (Riemann-integrabilidad)
Decimos que $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ es Riemann-integrable si existe $$I \in \mathbb{R}$$ tal que para todo $$\varepsilon > 0$$ existe $$P_{\varepsilon}$$ una partición de $$C$$ tal que para toda partición $$P = \{ C_{1},\dots,C_{k} \} \leq P_{\varepsilon}$$ cualquier escogencia de $$\{ \xi_{i} \}_{i=1}^{n}$$, se cumple que


$$
\lvert S(f, P, \xi_{1}, \dots, \xi_{k}) - I \rvert < \varepsilon.
$$


Escribimos que $$\int_{C} f = I$$. (Para $$n=2,3$$, podemos escribir integrales dobles, triples).

#### Nota
1. $$I$$ es único, pues si existen $$I_{1}, I_{2}$$ que satisfacen la definición, 


$$
\lvert I_{1} - I_{2} \rvert \leq \lvert I_{1} - S \rvert + \lvert I_{2} - S \rvert < 2\varepsilon
$$


2. $$C = \prod_{i=1}^{n} [a_{i}, b_{i}]$$. Si existe $$i$$ tal que $$(a_{i}=b_{i})$$, entonces $$V(C) = \prod_{i=1}^{n} (b_{i}-a_{i}) = 0$$, de donde concluimos que $$\int_{C} f = 0$$. 

### Teorema (Cauchy)
Sea $$f:C\subseteq \mathbb{R}^n\to \mathbb{R}$$ con $$C$$ caja. Entonces $$f$$ es Riemann-integrable en $$C$$ si y solo si para todo $$\varepsilon>0$$ existe $$P_{\varepsilon}$$ partición de de $$C$$ tal que para todas particiones $$P,Q$$ más finas que $$P_{\varepsilon}$$, se tiene que $$\lvert S(f,P) - S(f,Q) \rvert < \varepsilon$$ para cualquier escogencia de los $$\xi_{i}$$.

***Prueba:*** ($$\implies$$): Suponga que $$f$$ es Riemann-integrable. Entonces 


$$
\lvert S(f,P) - S(f,Q) \rvert \leq \lvert S(f,P)-I \rvert + \lvert S(f,Q) - I \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon. 
$$



($$\impliedby$$) : Suponga la hipótesis. Para $$\varepsilon = 1$$, defina $$Q_{1}  = P_{1}$$. Para $$n \in \mathbb{N}$$, tome $$P_{\frac{1}{n}}$$ como la partición proveniente de la hipótesis para $$\varepsilon = \frac{1}{n}$$ y defina inductivamente $$Q_{n}$$ como un refinamiento de  $$P_{\frac{1}{n}}$$ y $$Q_{n-1}$$. Así, para todo $$n < m$$, 


$$
\lvert S(f,Q_{n}) -S(f,Q_{m}) \rvert < \frac{1}{n}.
$$


Para cada $$n$$, fije $$\{ \xi_{i} \}$$ (nodos "interiores izquierdos"). Sean $$S_{n} = S(f,Q_{n}, \{ \xi_{i} \})$$. Así, la sucesión $$(S_{n})_{n \in \mathbb{N}}$$ es de Cauchy y por tanto converge a un valor $$I \in \mathbb{R}$$. Sea $$\varepsilon>0$$. Tome $$N \in \mathbb{N}$$ tal que $$\frac{1}{N} < \frac{\varepsilon}{3}$$ y tal que $$\lvert S_{n} - I \rvert < \frac{\varepsilon}{3}$$. Sea $$Q_{\varepsilon}$$ la partición de unir $$P_{\varepsilon}$$ y $$Q_{n}$$. Si $$P$$ es más fina que $$Q_{\varepsilon}$$, entonces, 


$$
\begin{aligned}
\lvert S(f,P) - I \rvert &\leq \lvert S(f,P) - S(f, Q_{\varepsilon}) \rvert + \lvert S(f, Q_{\varepsilon}) - S_{n} \rvert  + \lvert S_{n}-I \rvert \\
& \leq \frac{1}{n} + \frac{1}{n} + \frac{\varepsilon}{3} < \varepsilon,
\end{aligned}
$$


pues $$P \geq Q_{\varepsilon} \geq P_{\varepsilon}$$ y $$Q_{n} \geq P_{\varepsilon}$$.

### Lema (Acotación de sumas y particiones)
Sean $$f:C \subseteq \mathbb{R}^n\to \mathbb{R}$$, $$P = \{ C_{1},\dots C_{m} \}$$ partición de $$C$$. Sea $$Q = \{ D_{1},\dots,D_{p} \}$$ partición de $$C$$ más fina que $$P$$. Entonces, 


$$
\lvert S(f, Q, \{ \xi_{j} \}) - S(f, P, \{ \eta_{k} \}) \rvert \leq  \sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) 
$$


para cualquier escogencia de $$\{ \xi_{j} \}, \{ \eta_{k} \}$$ de $$P$$ con 


$$
M_{i} = \sup \{ f(x):x \in C_{i} \}, \quad m_{i} = \inf \{ f(x): x \in C_{i} \}.
$$



***Prueba:***  Como $$Q$$ es más fina que $$P$$, para todo $$i \in \{ 1,\dots, m \}$$, se tiene que 
$$C_{i} = D_{i_{1}} \cup \dots \cup D_{i_{\ell}}$$. Así, $$\xi_{i_{1}}, \dots, \xi_{i_{\ell}} \in C_{i}$$. Para $$\eta_{i} \in C_{i}$$, se tiene que 


$$
\begin{aligned}
\left\lvert  f(\eta_{i}) v(C_{i}) - \sum_{r=1}^{\ell} f(\xi_{i_{r}}) v(D_{i_{r}}) \right\rvert &= \left\lvert  \sum_{r=1}^{\ell} (f(\eta_{i}) - f(\xi_{irr})) v(D_{i_{r}})   \right\rvert \\
& \leq  \sum_{r=1}^{\ell} \lvert f(\eta_{i}) - f(\xi_{i_{r}})\rvert v(D_{i_{r}}) \\
& \leq \lvert M_{i} - m_{i} \rvert \sum_{r=1}^{\ell} v(D_{i_{r}}) \\
&=(M_{i}-m_{i}) v(C_{i}).
\end{aligned}
$$


Así, $$\lvert S(f, Q, \{ \xi_{j} \}) - S(f, P, \{ \eta_{k} \}) \rvert \leq  \sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) < \varepsilon$$.

### Teorema (Riemann)
Dada $$f:C \subseteq \mathbb{R}^n\to \mathbb{R}$$ acotada, con $$C$$ caja, es Riemann integrable si y solo si  para todo $$\varepsilon>0$$ existe $$P_{\varepsilon}$$ partición de $$C$$ tal que si $$P = \{ C_{1},..,C_{m} \}$$ es refinamiento de $$P_{\varepsilon}$$, entonces $$\sum_{i=1}^{m}(M_{i}-m_{i})v(C_{i}) < \varepsilon$$.

***Prueba:*** ($$\implies$$) Sea $$\varepsilon>0$$. Tome $$P_{\varepsilon}$$ una partición con $$\lvert S(f,P, \xi_{1}, \dots, \xi_{k}) \rvert < \varepsilon$$ para toda partición $$P = \{ C_{1}, \dots, C_{m} \}$$ más fina que $$P_{\varepsilon}$$ y toda elección de $$\xi_{i} \in C_{i}$$. Elija $$z_{i}$$, $$y_{i} \in C_{i}$$ tales que $$M_{i} - \varepsilon < f(y_{i})$$ y $$f(z_{i}) < m_{i} + \varepsilon$$. Así, $$M_{i}-m_{i} < f(y_{i}) - f(z_{i}) + 2\varepsilon$$ para todo $$1 \leq i \leq m$$.  Luego, 


$$
\begin{aligned}
\sum_{i=1}^{m} (M_{i}-m_{i}) v(C_{i}) &\leq  \left( \sum_{i=1}^{m} f(y_{i}) v(C_{i}) - I \right) - \left( \sum_{i=1}^{m} f(z_{i}) v(C_{i}) - I \right) + 2\varepsilon v(C_{i}) \\
& < 2\varepsilon + 2\varepsilon v(C) = \varepsilon(1 + 2 v(C)).
\end{aligned}
$$


$$(\impliedby):$$ Sea $$\varepsilon>0$$ y $$P_{\varepsilon} = \{ C_{1},\dots,C_{m} \}$$ como en la hipótesis. Como $$P_{\varepsilon}$$ es un refinamiento de sí misma, entonces,  


$$
\sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) < \varepsilon.
$$


Si $$P,Q$$ son más finas que $$P_{\varepsilon}$$, entonces, por el lema anterior, 


$$
\begin{aligned}
\lvert S(f,P) - S(f,Q) \rvert &\leq  \lvert S(f,P) - S(f, P_{\varepsilon}) \rvert + \lvert S(f,P_{\varepsilon}) - S(f,Q) \rvert \\
&\leq  2 \sum_{i=1}^{m} (M_{i}-m_{i}) v(C_{i}) < 2\varepsilon.
\end{aligned}
$$



### Teorema (Continuidad impica Riemann-integrabilidad)
Si $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ es continua en $$C$$, entonces es Riemann-integrable en $$C$$.

***Prueba:*** Como $$C$$ es compacto, $$f$$ es uniformemente continua. Sea $$\varepsilon>0$$. Existe $$\delta>0$$ tal que para $$x,y \in C$$ con $$\lVert x-y \rVert < \delta$$, se tiene que $$\lvert f(x) - f(y) \rvert < \frac{\varepsilon}{v(C)}$$. Sea $$P_{\varepsilon}$$ partición de $$C$$ tal que para todos $$x,y$$ en cada subcaja se tiene que $$\lVert x-y \rVert<\delta$$. Si $$P = \{ C_{1},\dots,C_{m} \}$$ es más fina que $$P_{\varepsilon}$$, se tiene que $$M_{i}-m_{i} < \frac{\varepsilon}{v(C)}$$ para todo $$1\leq i\leq m$$, y así, $$\sum_{i=1}^{m} (M_{i}-m_{i})v(C_{i}) < \varepsilon v(C)$$.

### Lema (Discontinuidad en conjunto de volumen cero)
Sea $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ acotada en caja $$C$$, continua en $$C \setminus D$$, con $$D \subseteq C$$ un conjunto de volumen cero. Entonces $$f$$ es Riemann-integrable en $$C$$.

***Prueba:*** Sea $$\varepsilon>0$$. Como $$v(D) = 0$$, existen $$C_{1}, \dots, C_{m} \subseteq C$$ con $$D \subseteq \bigcup_{i=1}^{m} C_{i}$$ y $$\sum_{i=1}^{m} v(C_{i}) < \varepsilon$$. Complete $$\{ C_{1},\dots, C_{m} \}$$ a una partición $$\{ C_{1}, \dots, C_{m} \}$$ a una partición $$\{C_{1},\dots,C_{m},\dots,C_{p}\}$$ de $$C$$. Por continuidad, $$f$$ es integrable en $$C_{m+1},\dots,C_{p}$$. Para $$j \in \{ m+1,\dots,p \}$$, por Riemann-integrabilidad, existen $$P_{\varepsilon}^{j}$$ que satisfacen la definición para $$\frac{\varepsilon}{p-m}>0$$.

Sea $$P_{\varepsilon}$$ una partición de $$C$$ tal que las subcajas de $$P_{\varepsilon}$$ que están en $$C_{j} \  (j=m+1,\dots,p)$$ forman una partición más fina que $$P_{\varepsilon}^{j}$$. Sin pérdida de generalidad, tome $$P_{\varepsilon}$$ tal que $$C_{j} \, (j=m+1,\dots,p)$$ es una unión finita de cajas de $$P_{\varepsilon}$$. 

Dada una partición $$Q = \{ D_{1},\dots,D_{q} \}$$ más fina que $$P_{\varepsilon}$$, suponga que existe $$r \in \mathbb{N}$$ tal que $$Q_{D} = \{D_{1},\dots,D_{r}\} \subseteq \{ C_{1},\dots, C_{m} \}$$ y $$Q_{C} = \{ D_{r+1},\dots,D_{q} \} \subseteq \{ C_{m+1},\dots,C_{p} \}$$. Así,


$$
\begin{aligned}
\left\lvert S(f,Q, \xi_{1},\dots,\xi_{q})  - \sum_{j=m+1}^{p} \int_{C_{j}} f \,\right\rvert &\leq \lvert S(f,Q_{D}, \xi_{1},\dots,\xi_{r}) \rvert + \left\lvert S(f,Q_{C}, \xi_{r+1},\dots,\xi_{q})  - \sum_{j=m+1}^{p} \int_{C_{j}} f \right\rvert \\ 
&\leq \sum_{j=1}^{r} \lvert f(\xi_{j}) \rvert v(D_{j}) + \sum_{j=m+1}^{p} \left\lvert  S(f,C_{j}) - \int_{C_{j}}f \right\rvert \\
&\leq M \varepsilon + (p-m) \frac{\varepsilon}{p-m}.
\end{aligned}
$$


### Definición (Riemann-integrabilidad en conjuntos de Jordan)
Sea $$f:K \subseteq \mathbb{R}^n\to \mathbb{R}$$ con $$K$$ de Jordan. Sea $$C$$ una caja con $$C \supseteq K$$. Definimos la extensión por cero de $$f$$ en $$C$$ como 


$$
f^{C}(x) = \begin{cases}
f(x), \quad \text{si } x \in K \\ 
0, \quad \text{si } x \not\in K. \\
\end{cases}
$$


Se dice que $$f$$ es Riemann-integrable en $$K$$ si $$f^{C}$$ es Riemann-integrable en $$C$$. Se escribe $$\int_{K} f = \int_{T} f^{c}$$.

#### Nota
La definición es independiente de $$C$$, pues $$\int_{C_{1}} f^{C_{1}} = \int_{C_{2}} f^{C_{2}}$$ para cajas $$C_{1} \supseteq K$$, $$C_{2} \supseteq K$$.

***Prueba:*** Dado $$\varepsilon>0$$, tome $$P_{\varepsilon}, Q_{\varepsilon}$$ particiones cde $$C_{1}$$ y $$C_{2}$$ que cumplen la definición de Riemann integrabilidad para $$f^{C_{1}}$$ y $$f^{C_{2}}$$ respectivamente. Sin pérdida de generalidad, suponga que cada subcaja de $$Q_{\varepsilon}$$ es una subcaja de $$P_{\varepsilon}$$. Así, 


$$
\begin{aligned}
\left\lvert  \int_{C_{1}} f^{C_{1}} - \int_{C_{2}} f^{C_{2}}   \right\rvert &\leq \left\lvert  S(f^{C_{1}}, P\varepsilon) - \int_{C_{1}} f^{C_{1}} \right\rvert + \left\lvert  S(f^{C_{1}}, P\varepsilon) - \int_{C_{2}} f^{C_{2}} \right\rvert \\
&< \varepsilon + \left\lvert  S(f^{C_{1}}, P\varepsilon) - \int_{C_{2}} f^{C_{2}} \right\rvert < 2\varepsilon.
\end{aligned}
$$



### Definición (Función característica)
Sea $$A \subseteq \mathbb{R}^n$$. Se obtiene la función característica de $$A$$ como $$1_{A}: \mathbb{R}^n\to \{ 0,1 \}$$ con


$$
1_{A}(x) = \begin{cases}
1, \quad \text{si }x \in A,\\
0, \quad \text{si }x \not\in A.
\end{cases}
$$


#### Nota
$$1_{A \cup B} = 1_{A} + 1_{B} - 1_{A \cap B}$$. Se puede probar por casos.
### Lema (Volumen como integral) 
Sea $$K \subseteq \mathbb{R}^n$$ de Jordan. Entonces, $$\int_{K} 1 = v(K)$$.

***Prueba:*** Sea $$C$$ una caja con $$K \subseteq C$$ y co$$1_{C}$$ la extensión por cero a $$C$$. Note que $$1_{C}$$ es Riemann integrable pues $$v(\partial K) = 0$$. Queremos probar que 


$$
\int_{C} 1_{C} = \inf \{ v(K, P): P \text{ partición de }C \}.
$$


Sea $$\varepsilon>0$$. Como $$v(\partial K) = 0$$, existen $$C_{1},\dots, C_{m}$$ con $$\partial K \subseteq \bigcup_{i=1}^{m} C_{i}$$ tales que $$\sum_{i=1}^{m}v(C_{i}) < \varepsilon$$. De la definición de ínfimo, tome $$Q_{\varepsilon}$$ una partición de $$C$$ tal que 


$$
v(K) \leq v(K, Q_{\varepsilon}) < v(K) + \varepsilon.
$$


Sea $$P_{\varepsilon}$$ partición de $$C$$ que satisface la definición de ser Riemann integrable para $$1_{C}$$. Sin pérdida de generalidad, $$Q_{\varepsilon}=P_{\varepsilon}$$ y $$C_{i}$$ son subcajas de  $$P_{\varepsilon} = \{ C_{1},\dots,C_{m}, C_{m+1},\dots, C_{p} \}$$, con $$\{ C_{m+1},\dots, C_{n} \} \subseteq K^{\circ}$$ para $$n < p$$. Así, 


$$
\begin{aligned}
\left\lvert  \int_{K} 1 - v(K)   \right\rvert  &\leq \left\lvert  \int_{K}1-v(K, P_{\varepsilon})  \right\rvert + \lvert  v(K, P_{\varepsilon}) - v(K) \rvert \\
&< \left\lvert  \int_{K} 1 - \sum_{i=1}^{n} v(C_{i})  \right\rvert + \varepsilon\\
&= \left\lvert  \int_{C} 1_{C} - \sum_{i=1}^{n} v(C_{i})  \right\rvert + \varepsilon < 2\varepsilon, 
\end{aligned}
$$


pues $$\sum_{i=1}^{n} v(C_{i})$$ es una suma de Riemann para $$1_{C}$$ sobre $$P_{\varepsilon}$$.

### Lema (Igualdad de funciones excepto en un conjunto de volumen cero)

Sean $$f,g: C \subseteq \mathbb{R}^n \to \mathbb{R}$$ funciones definidas en la caja $$C$$ tales que $$f$$ es Riemann integrable y $$g$$ es acotada en $$C$$. Si $$g(x) = f(x)$$ para todo $$x \in C \setminus D$$, donde $$D \subseteq C$$ es de volumen cero, entonces $$g$$ es integrable en $$C$$ y $$\int_{C}f = \int_{C} g$$.

***Prueba:*** Pendiente
#### Corolario 
Si $$f:K\subseteq \mathbb{R}^n \to \mathbb{R}$$ es acotada y $$v(K)=0$$, entonces $$f$$ es Riemann integrable en $$K$$ y $$\int_{K} f = 0$$.

***Prueba:*** Si $$C$$ es una caja con $$K \subseteq C$$, entonces $$f_{C}(x) = 1_{K}(x) = 0$$ para todo $$x \in C \setminus K$$. Luego, aplicando el lema,


$$
\int_{K} f = \int_{C} f_{C} = \int_{C} 1_{K} = \int_{K} 1 = v(K) = 0.
$$



## Propiedades de la integral de Riemann

### Teorema (Linealidad)
Sean $$f,g:K \subseteq \mathbb{R}^n \to \mathbb{R}$$, con $$K$$ de Jordan, y $$f,g$$ Riemann-integrables. Entonces, dado $$c \in \mathbb{R}$$, $$f+cg$$ es Riemann-integrable y 


$$
\int_{K} f+cg = \int_{K} f + c \int_{K} g.
$$


***Prueba:*** Sin pérdida de generalidad, suponga que $$K$$ es una caja. Dado $$\varepsilon > 0$$, tome $$P_{\varepsilon}, Q_{\varepsilon}$$ que satisfacen la definición de Riemann-integrabilidad para $$f$$ y $$g$$ respectivamente. Sin pérdida de generalidad, suponga que $$P_{\varepsilon} = Q_{\varepsilon}$$. Luego, para $$P \leq P\varepsilon$$


$$
\begin{aligned}
S(f+cg, P) &= \sum_{i=1}^{m} (f+cg)(\xi_{i}) v(C_{i}) \\
&=S(f,P) + cS()g,P \\
\end{aligned}
$$


Así,


$$
\begin{aligned}
\left\lvert  S(f+cg),P - \int_{K}f -c \int_{K} g\right\rvert & \leq \left\lvert  S(f,P) - \int_{K} f \right\rvert + \lvert c \rvert \left\lvert  S(g,P) - \int_{K} g  \right\rvert  \\
& <\varepsilon + \lvert c \rvert \varepsilon = \varepsilon(1 + \lvert c \rvert ).
\end{aligned}
$$


### Teorema (Separabilidad en conjuntos)
Sean $$A,B$$ de Jordan en $$\mathbb{R}^n$$, $$f:A \cup B \to \mathbb{R}$$ tal que $$f \mid_{A}$$ y $$f \mid_{B}$$ son R.I. en $$A$$ y $$B$$ respectivamente. Entonces
1. $$f$$ es R.I. en $$A \cup B$$.
2. $$\int_{A \cup B} f = \int_{A} f + \int_{B}f - \int_{A \cap B} f$$. 

***Prueba:*** Se puede verificar que $$A \cap B$$ es de Jordan y que $$f$$ es Riemman integrable en $$A \cap B$$ (pues $$A \cap B \subseteq A$$). Luego,


$$
\begin{aligned}
\int_{A} f + \int_{B} f - \int_{A \cap B} f &= \int_{A \cup B} 1_{A} f + \int_{A \cup B} 1_{B} f - \int_{A \cup B} 1_{A \cap B} f \\
&= \int_{A \cup B} 1_{A}f + 1_{B} f - 1_{A \cap B} f \\
&= \int_{A \cup B} 1_{A \cup B} f = \int_{A \cup B} f.
\end{aligned}
$$



### Teorema (Construcción de funciones Riemann-integrables)
Sean $$f,g: K \subseteq \mathbb{R}^n \to \mathbb{R}$$, con $$K$$ de Jordan. Suponga que ambas son Riemann-integrables en $$K$$. Entonces
1. $$\lvert f \rvert$$ es Riemann-integrable en $$K$$
2. Para todo $$n \in \mathbb{N}$$, $$f^{n}$$ es Riemann-integrable en $$K$$.
3. Si existe $$\varepsilon>0$$ tal que para todo $$x \in K$$, $$f(x)\geq \varepsilon$$, entonces $$\frac{1}{f}$$ es Riemann-integrable en $$K$$.
4. $$fg$$ es Riemann-integrable en $$K$$. (Truco: $$fg = \frac{(f+g)^{2}-f^{2}-g^{2}}{2}$$).

### Teorema (Composición y Riemann-Integrabilidad)
Sea $$f:K \subseteq \mathbb{R}^n\to \mathbb{R}$$ Riemann-integrable en $$K$$ y $$g:[c,d]\to \mathbb{R}$$ continua con $$f(K) \subseteq [c,d]$$. Entonces, $$g \circ f$$ es Riemann-integrable en $$K$$.

## Integrales iteradas

Nos centraremos ahora en calcular $$\int_{K} f$$ para regiones $$K$$ generales.
### Lema (Continuidad de integral interior)
Si $$f:[a,b] \times [c,d] \to \mathbb{R}$$ es continua, entonces $$F:[c,d]\to \mathbb{R}$$ dada por 


$$
F(y) = \int_{a}^{b} f(x,y) \, dx 
$$


es continua.

***Prueba:*** Sea $$\varepsilon>0$$. Por continuidad uniforme, existe $$\delta>0$$ tal que para todo $$x \in [a,b]$$ y para todos $$y,y_{0} \in [c,d]$$, si $$\lvert y-y_{0} \rvert<\delta$$ entonces $$\lvert f(x,y)-f(x,y_{0}) \rvert < \varepsilon$$. Entonces, 


$$
\begin{aligned}
\lvert F(y)-F(y_{0}) \rvert &= \left\lvert  \int_{a}^{b} f(x,y) \, dx    - \int_{a}^{b} f(x,y_{0}) \, dx \right\rvert\\
& \leq  \int_{a}^{b} \lvert f(x,y) - f(x,y_{0}) \rvert  \, dx = \varepsilon(b-a),
\end{aligned}
$$


de donde concluimos continuidad de $$F$$.

#### Nota
$$G(x) = \int_{c}^{d} f(x,y) \, dy$$ es continua por el mismo argumento.

### Teorema (Fubini)
Sea $$f:\underbrace{ [a,b] \times [c,d] }_{ C } \to \mathbb{R}$$, con $$f$$ continua. Entonces 


$$
\int_{C} f = \int_{a}^{b} \left( \underbrace{ \int_{c}^{d} f(x,y)  \, dy }_{ G(x) }  \right) \, dx = \int_{c}^{d} \left( \underbrace{ \int_{a}^{b} f(x,y)  \, dx  }_{ F(y) } \right) \, dy.
$$


***Prueba:*** Sabemos que las 3 integrales existen porque $$f$$ es continua. Además, como $$f$$ es uniformemente continua en $$[a,b] \times [c , d]$$, dado $$\varepsilon>0$$ existe $$\delta>0$$ tal que $$\lvert f(x_{1},y_{1}) - f(x_{2},y_{2})\rvert < \varepsilon$$ siempre que $$\lVert (x_{1}-x_{2},y_{1}-y_{2}) \rVert < \delta$$. Particione $$[a,b]$$ en $$\{ a=x_{0}<x_{1}< \dots < x_{m} = b \}$$ y $$[c,d]$$ en $$\{ c = y_{0} < y_{1} < \dots < y_{n} = d \}$$ tal que $$\lvert x_{i+1} - x_{i} \rvert < \frac{\delta}{\sqrt{ 2 }}$$ y $$\lvert y_{j+1}-y_{j} \rvert < \frac{\delta}{\sqrt{ 2 }}$$ para todos $$i,j$$. 
Como $$f$$ es Riemann integrable en $$C$$, sin pérdida de generalidad suponga que $$P_{\varepsilon}$$ coincide con las particiones generadas para $$[a,b]$$ y $$[c,d]$$. Se tiene que 


$$
\begin{aligned}
I_{2}:=\int_{a}^{b} \left( \int_{c}^{d} f(x,y) \, dy  \right)  \, dx &= \int_{a}^{b} \left( \sum_{j=1}^{n} \int_{y_{j-1}}^{y_{j}} f(x,y) \, dy  \right) \, dx  \\
&= \underbrace{ \int_{a}^{b} \left(  \sum_{j=1}^{n} f(x,t_{j}) \cdot (y_{j}-y_{j-1}) \right) \, dx }_{ \text{por TVM para integrales con } t_{j} \in [y_{j-1}, y_{j}] } \\
&= \sum_{j=1}^{n} (y_{j}-y_{j-1}) \int_{a}^{b} f(x,t_{j}) \, dx \\
&\underset{\text{TVM}}{=} \sum_{j=1}^{n} (y_{j} - y_{j-1}) \sum_{i=1}^{m} \int_{x_{i-1}}^{x_{i}} f(x,t_{j})  \, dx \\
&= \sum_{j=1}^{n} \sum_{i=1}^{m} (y_{j}-y_{j-1}) (x_{i}- x_{i-1}) f(s_{i}, t_{j}) \\ &= S(f, P_{\varepsilon}, \{ (s_{i},t_{j}) \}).
\end{aligned}
$$


De manera análoga, existen $$p_{i} \in [x_{i-1}, x_{i}]$$ y $$q_{j} \in [y_{j-1}, y_{j}]$$ tales que 


$$
I_{3}:= \int_{c}^{d} \left( \int_{a}^{b} f(x,y) \, dx  \right)  \, dy = S(f, P_{\varepsilon}, \{ (p_{i}, q_{j}) \}).
$$


Así, 


$$
\begin{aligned}
\lvert I_{2}-I_{3} \rvert & \leq  \sum_{i=1}^{m} \sum_{j=1}^{n} (y_{j} - y_{j-1})(x_{i}-x_{i-1}) \lvert f(s_{i},t_{j}) - f(p_{i}, q_{j}) \rvert \\
& < \varepsilon(b-a)(d-c)
\end{aligned}
$$


pues $$\lVert (s_{i},t_{j}) - (p_{i}, q_{i}) \rVert = \sqrt{ (s_{i}-p_{i})^{2} +(t_{j}-q_{j})^{2}} \leq \sqrt{ \frac{\delta^{2}}{2} + \frac{\delta^{2}}{2} } = \delta$$. De esta manera, $$I_{2} = I_{3}$$.
Finalmente, 


$$
\left\lvert  \int_{C} f  - I_{2}\right\rvert = \left\lvert  \int_{C} f - S(f,P_{\varepsilon}, \{ (s_{i},t_{j}) \})  \right\rvert  < \varepsilon
$$


por definición de Riemann integrabilidad.
#### Nota (Integrales triples)
Si $$f:[a,b]\times[c,d] \times[e,f]\to \mathbb{R}$$ continua, podemos generalizar Fubini para cualquier orden de integración, y el desarrollo de la prueba es análogo. Lo mismo para cualquier reordenamiento de funciones de $$\mathbb{R}^n$$ a $$\mathbb{R}$$.

### Teorema (Fubini con discontinuidades)
Sea $$f:[a,b] \times [c,d] \to \mathbb{R}$$ una función Riemann integrable tal que para todo $$y \in [c,d]$$, la función $$f(\cdot,y):[a,b] \to \mathbb{R}$$ posee una cantidad finita de discontinuidades. Entonces, 


$$
F:[c,d]\to \mathbb{R}, \quad F(y) = \int_{a}^{b} f(x,y) \, dy
$$


es integrable y 


$$
\int_{[a,b] \times [c,d]} f = \int_{c}^{d} \left( \int_{a}^{b} f(x,y) \, dx  \right) \, dy.
$$



***Prueba:*** Se tiene que $$F(y)$$ está bien definida, pues por por hipótesis $$f(\cdot,y)$$ tiene una cantidad finita de discontinuidades.  Dado $$\varepsilon>0$$, tome $$P_{\varepsilon}$$ de la definición de Riemann integrabilidad. Sean $$\{ x_{0},\dots, x_{n} \}, \{ y_{0},\dots,y_{m} \}$$ particiones de $$[a,b]$$ y $$[c,d]$$, respectivamente, generadas por $$P_{\varepsilon}$$. Se tiene 


$$
\begin{aligned}
S(F, \{ y_{j} \}, \{ \xi_{j} \}) &= \sum_{j=1}^{m} F(\xi_{j})(y_{j}-y_{j-1}) \\
&= \sum_{j=1}^{m} \int_{a}^{b} f(x, \xi_{j})(y_{j}-y_{j-1}) \, dx 
\end{aligned}
$$


para cualquier selección de $$\{ \xi_{1},\dots,\xi_{m} \}$$ con $$x_{j-1} < \xi_{j} < x_{j}$$. Como $$f(\cdot, \xi_{j})$$ es Riemann integrable en $$[a,b]$$, existe una suma de Riemann $$S(f(\cdot, \xi_{j}))$$ sobre una partición $$Q$$ de $$[a,b]$$ más fina que $$\{ x_{j} \}_{j=0}^{n}$$ tal que 


$$
\left\lvert  \int_{a}^{b} f(x, \xi_{j}) \,dx - S(f(\cdot, \xi_{j}))  \right\rvert < \varepsilon.
$$


Note que la partición generada por $$Q$$ y $$\{ y_{0},\dots, y_{m} \}$$ de $$[a,b] \times [c,d]$$ es más fina que $$P_{\varepsilon}$$ y 


$$
\sum_{j=1}^{m} S(f(\cdot, \xi_{i}))(y_{j}-y_{j-1})
$$


es una suma de Riemann para $$f$$ sobre esa partición. Así 


$$
\begin{aligned}
\left\lvert  \int_{C} f - S(F, \{ y_{j} \}, \{ \xi_{j} \} )  \right\rvert &\leq \left\lvert  \int_{C} f - \sum_{j=1}^{m}  S(f(\cdot, \xi_{i}))(y_{j}-y_{j-1})  \right\rvert \\  &\quad + \left\lvert  \sum_{j=1}^{m}  S(f(\cdot, \xi_{i}))(y_{j}-y_{j-1}) - \sum_{j=1}^{m} \int_{a}^{b} f(x, \xi_{j})(i_{j}-y_{j-1}) \, dx  \right\rvert \\
& <\varepsilon + \sum_{j=1}^{m} \left\lvert  S(f(\cdot, \xi_{i})) - \int_{a}^{b} f(x, \xi_{j})  \, dx   \right\rvert (y_{j}-y_{j-1}) \\
& < \varepsilon(1+d-c),
\end{aligned} 
$$


de donde concluimos que $$F$$ es Riemann integrable en $$[c,d]$$ y $$\int_{C} = \int_{c}^{d} F(y) \, dy$$.
### Lema (área entre gráficos)

Sean $$\phi, \psi:[a,b]\to \mathbb{R}$$ continuas, con $$\phi(x) \leq \psi(x)$$ para todo $$x \in [a,b]$$. Defina 


$$
A = \{ (x,y): a\leq x\leq b, \phi(x) \leq  y \leq  \psi(x) \}.
$$


Si $$f:A\to \mathbb{R}$$ es continua, entonces $$\int_{A} f = \int_{a}^{b}\left( \int_{\phi(x)}^{\psi(x)}f(x,y)  \, dy \right)  \, dx$$.

***Prueba:*** Sabemos que $$A$$ es de Jordan y $$f$$ es continua. Por tanto, $$f$$ es Riemann integrable en $$A$$. Por definición de $$\int_{A} f$$, ocupo una caja $$C \supseteq A$$. Defina 


$$
f^{C}(x) = \begin{cases}
f(x),  \quad x \in A \\
0, \quad x \in C \setminus A
\end{cases} 
$$


Así, $$\int_{A} f = \int_{C} f^{C} = \int_{c}^{d} \int_{e}^{\text{f}} f^{C}(x,y)  \, dy  \, dx = \int_{a}^{b} \int_{e}^{f}  f^{C}(x,y)\, dy  \, dx$$. Desarrollando: 


$$
\begin{aligned}
\int_{a}^{b} \int_{e}^{\text{f}}  f^{C}(x,y)\, dy  \, dx &= \int_{a}^{b} \left( \underbrace{ \int_{e}^{\phi(x)} f^{C}  \, dy }_{ 0 } + \int_{\phi(x)}^{\psi(x)} f^{C} \, dy + \underbrace{ \int_{\phi(x)}^{\text{f}} f^{c}  \, dy }_{ 0 }  \right) \, dx  \\
&= \int_{a}^{b} \int_{\phi(x)}^{\psi(x)} f(x,y)  \, dy   \, dx.
\end{aligned}
$$



#### Ejemplo 
Calcule el volumen de la región limitada por $$x^{2}+y^{2}\leq 9$$, $$y^{2}-x^{2} \leq 1$$. 
Desarrollando algebraicamente


$$
y^{2}-x^{2} = 1 \implies y = \pm \sqrt{ 1+x^{2} }.
$$


Note que en esta relación, $$\lvert y \rvert\geq1$$ y $$y=x$$ para todo $$(x,y) \in A$$. Encontremos las intersecciones entre ambas relaciones: 


$$
\begin{aligned}
x^{2}+y^{2}&=9\\
y^{2}-x^{2}&=1\\
\implies 2y^{2} &= 10,
\end{aligned}
$$


de donde obtenemos que $$y = \pm \sqrt{ 5 }, x = \pm 2$$. Ocupo 


$$
v(A) = \int_{A} 1  = \int_{?} \int_{?} \, dy \, dx = \int_{?} \int_{?}\, dx \, dy.
$$


Para calcular los límites de integración, es útil ayudarse con los dibujos. Calculemos primero integrando primero sobre $$y$$ y luego sobre $$x$$ ("tipo 1").



$$
\begin{aligned}
v(A) &= \underbrace{ \int_{-3}^{-2} \int_{-\sqrt{ 9-x^{2} }}^{\sqrt{ 9-x^{2} }} 1 \, dy  \, dx  }_{ I_{1} }+ \int_{-2}^{2} \int_{-\sqrt{ 1+x^{2} }}^{\sqrt{ 1+x^{2} }} 1 \, dy \, dx + \int_{2}^{3} \int_{-\sqrt{ 9-x^{2} }}^{\sqrt{ 9-x^{2} }}  \, dy   \, dx \\
&=
\end{aligned}
$$


Si integramos primero sobre $$x$$ y luego sobre $$y$$ ("tipo 2") 


$$
\begin{aligned}
v(A) &= \int_{-1}^{1} \int_{-\sqrt{ 9-y^{2} }}^{\sqrt{ 9-y^{2} }} 1 \, dx  \, dy +\int_{1}^{\sqrt{ 5 }} \int_{-\sqrt{ 9-y^{2} }}^{-\sqrt{ y^{2}-1 }}  1\, dx   \, dy + \int_{1}^{\sqrt{ 5 }} \int_{\sqrt{ 9-y^{2} }}^{\sqrt{ y^{2}-1 }}  \, 1 dx   \, dy \\
&  \quad + \int_{-1}^{\sqrt{ -5 }} \int_{-\sqrt{ 9-y^{2} }}^{-\sqrt{ y^{2}-1 }}  \, 1 dx   \, dy  + \int_{-1}^{\sqrt{ -5 }} \int_{\sqrt{ 9-y^{2} }}^{\sqrt{ y^{2}-1 }}  \, 1 dx   \, dy 
\end{aligned}
$$



### Teorema (Integración con finitud de discontinuidades)
Sea $$f:[a,b] \times [c,d] \to \mathbb{R}$$ tal que para todo $$y \in [c,d]$$, la función $$f(\cdot, y):[a,b] \to \mathbb{R}$$ tiene una cantidad finita de discontinuidades. Entonces:
1. $$F:[c,d] \to \mathbb{R}$$, $$F(y) = \int_{a}^{b} f(x,y) \, dx$$ es R.I.
2. $$\int_{[a,b]\times[c,d]}f = \int_{c}^{d} F(y) dy = \int_{c}^{d} \left( \int_{a}^{b} f(x,y) \, dx \right) \, dy$$. 

#### Idea
En 2 dimensiones, $$\int_{K} f = \int_{a}^{b} \int_{\psi(X)}^{\phi(x)} f \, dy \, dx$$

#### Ejemplo 
Calcule el volumen de una esfera de radio $$r$$: 


$$
K = \{ (x,y,z):x^{2}+y^{2}+z^{2} \leq  r \}.
$$


Tenemos que el volumen de la esfera viene dado por 


$$
\int_{-r}^{r} \int_{-\sqrt{ r^{2}-x^{2} }}^{\sqrt{ r^{2}-x^{2} }} \int_{-\sqrt{ r^{2}-x^{2}-y^{2}}}^{\sqrt{ r^{2}-x^{2}-y^{2}}} 1 \, dx   \, dy  \, dx 
$$



#### Ejemplo 
Calcule el volumen en el primer octante limitado por el plano $$2x+3y+z=6$$.
Tenemos que 


$$
V = \int_{0}^{2} \int_{0}^{(6-3y)/2} \int_{0}^{6-2x-3y}  \, dz  \, dx  \, dy = \int_{0}^{6} \int_{0}^{(6-z)/3} \int_{0}^{(6-z-3y)/2}  \, dx  \, dy  \, dz.
$$


 Para el primer orden, analizamos primero sobre el plano $$xy$$, y para el segundo sobre el plano $$yz$$.
#### Ejemplo 
Calcule $$\int \int \int_{K} f \,dz \,dy \,dx$$, con $$K$$ en el primer octante limitado por 


$$
\begin{aligned}
P_{1}&: x=0 \\
P_{2}&: y=0 \\
P_{3}&: z=0 \\
\pi_{1}&: 2x+4y+3z = 36 \\
\pi_{2}&: x+y+z = 11 \\
\pi_{3}&: 2x+3z = 24.
\end{aligned}
$$



## Cambio de variable

En una dimensión, tenemos que si $$f$$ es continua y $$g:[a,b]\to \mathbb{R}$$ es una función derivable con primera derivada continua, entonces


$$
\int_{g(a)}^{g(b)}  f(x) \, dx  = \int_{a}^{b} f(g(t)) g'(t) \, dt.
$$


Además, esto se puede relajar a $$f$$ integrable en $$g([a,b])$$ y $$g$$ monótona en $$[a,b]$$, en cuyo caso se usa $$\lvert g'(t) \rvert$$ en la integral

### Teorema (Cambio de variable)
Generalización de Integral de Riemann (MA0350, sustitución en una variable). Usa Determinantes (MA0360). Sea $$A \subseteq \mathbb{R}^n$$ un conjunto abierto, $$g:A\to \mathbb{R}^n$$ inyectiva y continuamente diferenciable en $$A$$ con $$\det J_{g}(x) \neq 0$$ para todo $$x \in A$$. Si $$K$$ es de Jordan, $$\bar{K} \subseteq A$$, entonces 


$$
\int_{g(K)} f = \int_{K} (f \circ g) \lvert \det J_{g} \rvert. \ \tag{*} 
$$



### Lema (Imagen de una caja bajo $$g$$ es de Jordan)
1. Si $$K \subseteq A$$ es de Jordan entonces $$g(K)$$ es de Jordan
2. Si $$v(K) = 0$$ entonces $$v(g(K)) = 0$$

### Lema (Volumen bajo transformaciones) 
Sea $$C \subseteq \mathbb{R}^n$$ una caja, $$g:C\to \mathbb{R}^n$$ lineal e inyectiva. Entonces, 


$$
v(g(C)) = \int_{g(C)} 1 = \int_{C} \lvert \det J_{g} \rvert 
$$



### Lema  (Composición de cambios de variable)
Si $$(*)$$ es válido para $$g:A\to \mathbb{R}^n$$, $$h:B\to \mathbb{R}^n$$ con $$g(A) \subseteq B$$, entonces es válido para $$h \circ g: A \to \mathbb{R}^n$$.

### Lema 
Si $$(*)$$ es válido para $$f \equiv 1$$, entonces es válido para cualquier función.


#### Ejemplos de cambios de variable
1.  Coordenadas elípticas: Para elipses de la forma 


$$
\left( \frac{x}{a} \right)^{2} + \left( \frac{y}{b} \right)^{2} = 1,
$$


hacer el cambio de variable $$x = a r \cos \theta, y = br \sin \theta$$, con $$r \in [0,1]$$ y $$\theta \in [0,2\pi]$$, entonces $$\lvert \det J_{g} \rvert = abr \neq 0$$ para todo $$r \neq 0$$.
{% endraw %}
