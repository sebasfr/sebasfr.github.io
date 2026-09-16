---
layout: chapter
course: ma0450
chapter: 3
title: "Diferenciación"
slug: 03-diferenciacion
toc:
  sidebar: right
lang: es
fecha: 2025-09-08
permalink: /notes/ma0450/es/03-diferenciacion/
redirect_from:
  - /notes/ma0450/03-diferenciacion/
---

{% raw %}
## Derivadas parciales

### Definición (Derivada parcial)
Sea $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$ con $$D$$ vecindario de $$a$$. Para $$j \in \{ 1,\dots,n \}$$, se define la derivada parcial de $$f$$ en $$a = (a_{1},\dots,a_{n})$$ con respecto a la entrada $$j$$ como 


$$
D_{j}f(a) = \lim_{ h \to 0} \frac{f(a_{1},\dots,a_{j-1}, a_{j}+h, a_{j+1},\dots,a_{n}) - f(a)}{h}.
$$



#### Nota:
1. Si $$y=f(x)$$, entonces $$f'(a) = \lim_{ h \to 0 } \frac{f(a+h)-f(a)}{h}$$.
2. Escribimos $$D_{j}f(a) = \frac{\partial f}{\partial x_{j}}(a) = f_{x_{j}}(a)$$.
3. Las variables $$x_{i} \neq x_{j}$$ para todo $$i$$ se toman como constantes.
4. Si defino $$g(x_{j}) = f(a_{1},\dots,a_{j-1}, x_{j}, a_{j+1},\dots, a_{n})$$, entonces $$D_{j}f(a) = g'(a_{j})$$.
5. Geométricamente, para $$n=2$$, $$D_{1}f(a,b)$$ es la pendiente en $$x = a$$ de la curva que resulta de cortar la gráfica $$z = f(x,y)$$ con el plano $$y = b$$. La derivada parcial solo "ve" a $$f$$ a lo largo de esa recta.

![La derivada parcial como pendiente de la curva de corte con el plano y = b](/assets/img/courses/ma0450/derivada-parcial-corte.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[x={(1cm,0cm)}, y={(0.5cm,0.4cm)}, z={(0cm,1cm)}, scale=1.3]
  % superficie z = f(x,y) como malla
  \foreach \yy in {0,0.5,...,2}
    \draw[gray!60, domain=0:3, samples=30] plot (\x, \yy, {1.6 - 0.15*(\x-1.5)^2 + 0.2*\yy});
  \foreach \xx in {0,0.5,...,3}
    \draw[gray!60, domain=0:2, samples=20] plot (\xx, \x, {1.6 - 0.15*(\xx-1.5)^2 + 0.2*\x});
  % plano y = b
  \fill[orange, opacity=0.12] (0,1,0) -- (3,1,0) -- (3,1,2.4) -- (0,1,2.4) -- cycle;
  \node[orange] at (0.4,1,2.3) {$y=b$};
  % curva de corte g(x) = f(x,b)
  \draw[orange, thick, domain=0:3, samples=40] plot (\x, 1, {1.8 - 0.15*(\x-1.5)^2});
  % punto y tangente en x = a = 2.4 (pendiente -0.27)
  \fill[orange] (2.4,1,1.6785) circle (1.5pt);
  \draw[orange, very thick] (1.6,1,1.8945) -- (3.2,1,1.4625);
  \node[orange, right] at (3.2,1,1.5) {pendiente $D_1 f(a,b)$};
  \draw[dashed] (2.4,1,0) -- (2.4,1,1.6785);
  \fill (2.4,1,0) circle (1.2pt) node[below] {$(a,b)$};
  \draw[->] (0,0,0) -- (3.5,0,0) node[right] {$x$};
  \draw[->] (0,0,0) -- (0,2.5,0) node[above] {$y$};
  \draw[->] (0,0,0) -- (0,0,2.6) node[above] {$z$};
\end{tikzpicture}
-->

#### Ejemplo 
Si $$f(x,y,z) = e^{xy^{2}} + \sin(xyz)$$ entonces $$D_{1}f(x,y,z) = e^{xy^{2}}y^{2} + \cos(xyz) \cdot yz$$.

### Definición (Derivadas parciales de orden superior)
Dada $$f$$ tal que $$D_{j} f(a)$$ existen para todo $$j \in \{ 1,\dots n \}$$, se definen $$D_{ij}f(a) = D_{i} (D_{j} f(a))$$.
Escribimos $$D_{ij} f(a) = \frac{\partial}{\partial  x_i}(\frac{\partial f}{\partial  x_{j}})(a) = f_{x_{j}x_{i}}(a)$$.

#### Nota:
La notación se puede extender, p.e., $$\frac{\partial^{4} f}{\partial x_{1} \partial x_{2} \partial x_{4} \partial x_{3}}(a)$$.

### Teorema (Schwarz)
Sea $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, con $$a \in D$$. Suponga que $$f$$ es continua en $$B_{r}(a) \subseteq D$$, que $$D_{1}f$$, $$D_{2} f$$ y $$D_{21} f = D_{2}(D_{1}f)$$ existen en $$B_{r}(a)$$, y que $$D_{21} f$$ es continua en $$a$$. Entonces, $$D_{12} f(a) = D_{1}(D_{2}f)(a)$$ existe y $$D_{12}f(a) = D_{21}f(a)$$.

***Prueba:*** Para $$n = 2$$, sea $$a = (x_{0},y_{0})$$ y sea $$\varepsilon>0$$. Por continuidad de $$D_{21}f$$ en $$a$$, existe $$\delta>0$$ tal que $$[x_{0}-\delta,x_{0}+\delta] \times [y_{0}-\delta,y_{0}+\delta] \subseteq B_{r}(a)$$ y $$\lvert D_{21}f(x,y) - D_{21}f(a) \rvert < \varepsilon$$ siempre que $$\lvert x-x_{0} \rvert<\delta$$ y $$\lvert y-y_{0} \rvert < \delta$$. Fije $$0<h,k<\delta$$ y considere la *segunda diferencia* de $$f$$ sobre el rectángulo de vértices $$(x_{0},y_{0})$$, $$(x_{0}+h,y_{0})$$, $$(x_{0},y_{0}+k)$$ y $$(x_{0}+h,y_{0}+k)$$:


$$
\Delta(h,k) = f(x_{0}+h,y_{0}+k) - f(x_{0}+h,y_{0}) - f(x_{0},y_{0}+k) + f(x_{0},y_{0}).
$$


![El rectángulo de la segunda diferencia en la prueba de Schwarz](/assets/img/courses/ma0450/schwarz-rectangulo.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[scale=2.2]
  \draw[thick] (0,0) rectangle (2,1.4);
  \fill (0,0) circle (1.2pt) node[below left] {$(x_0,y_0)$};
  \fill (2,0) circle (1.2pt) node[below right] {$(x_0+h,y_0)$};
  \fill (0,1.4) circle (1.2pt) node[above left] {$(x_0,y_0+k)$};
  \fill (2,1.4) circle (1.2pt) node[above right] {$(x_0+h,y_0+k)$};
  \draw[orange, thick, ->] (0.15,0.7) -- (1.85,0.7) node[midway, above] {$\phi$: TVM en $x$};
  \draw[orange, thick, ->] (1.1,0.12) -- (1.1,1.28) node[midway, right] {$\psi$: TVM en $y$};
  \fill[orange] (1.1,0.7) circle (1.4pt) node[above right] {$(c,d)$};
  \node at (1,-0.45) {$\Delta(h,k) = hk \, D_{21}f(c,d)$};
\end{tikzpicture}
-->

Defina $$\phi(x) = f(x, y_{0}+k) - f(x,y_{0})$$, de modo que $$\Delta(h,k) = \phi(x_{0}+h) - \phi(x_{0})$$. Como $$D_{1}f$$ existe, $$\phi$$ es derivable en $$[x_{0},x_{0}+h]$$ y, por el teorema del valor medio, existe $$c \in (x_{0}, x_{0}+h)$$ tal que


$$
\Delta(h,k) = \phi'(c) \cdot h = h\,(D_{1}f(c, y_{0}+k) - D_{1}f(c,y_{0})).
$$


Defina ahora $$\psi(y) = D_{1}f(c,y)$$ con $$y \in [y_{0},y_{0}+k]$$. Como $$D_{21}f = D_{2}(D_{1}f)$$ existe, $$\psi$$ es derivable y, de nuevo por el teorema del valor medio, existe $$d \in (y_{0},y_{0}+k)$$ tal que $$\psi(y_{0}+k) - \psi(y_{0}) = \psi'(d) \cdot k = D_{21} f(c,d) \cdot k$$. Luego


$$
\frac{\Delta(h,k)}{hk} = D_{21} f(c,d), \qquad (c,d) \in (x_{0},x_{0}+h)\times(y_{0},y_{0}+k),
$$


y por la elección de $$\delta$$,


$$
\left\lvert \frac{\Delta(h,k)}{hk} - D_{21}f(a) \right\rvert < \varepsilon \quad \text{para todo } 0<h,k<\delta. \tag{1}
$$


El punto clave es que la cota (1) es *uniforme*: no depende de dónde cayeron $$c$$ y $$d$$ (que sí dependen de $$h$$ y $$k$$). Fijemos $$h$$ y hagamos $$k \to 0$$. Como $$D_{2}f$$ existe en $$(x_{0}+h,y_{0})$$ y en $$(x_{0},y_{0})$$,


$$
\lim_{ k \to 0 } \frac{\Delta(h,k)}{hk} = \frac{1}{h}\left( \lim_{ k \to 0 } \frac{f(x_{0}+h,y_{0}+k) - f(x_{0}+h,y_{0})}{k} - \lim_{ k \to 0 }\frac{f(x_{0},y_{0}+k)-f(x_{0},y_{0})}{k} \right) = \frac{D_{2}f(x_{0}+h,y_{0}) - D_{2}f(x_{0},y_{0})}{h},
$$


y pasando al límite en (1) obtenemos $$\left\lvert \frac{D_{2}f(x_{0}+h,y_{0}) - D_{2}f(x_{0},y_{0})}{h} - D_{21}f(a) \right\rvert \leq \varepsilon$$ para todo $$0<h<\delta$$ (el caso $$h<0$$ o $$k<0$$ es idéntico). Como $$\varepsilon$$ era arbitrario, esto dice exactamente que el límite cuando $$h \to 0$$ del cociente incremental de $$D_{2}f$$ existe y vale $$D_{21}f(a)$$; es decir,


$$
D_{1}(D_{2}f) (x_{0}, y_{0}) = D_{12} f (x_{0},y_{0}) = D_{21} f(x_{0},y_{0}),
$$


de donde concluimos el resultado.

#### Nota
Para $$f:\mathbb{R}^{2} \to \mathbb{R}$$ de clase $$C^{3}$$, $$D_{121} f(a,b) = D_{112} f(a,b) = D_{211} f(a,b)$$: basta aplicar el teorema repetidamente. Si $$f:\mathbb{R}^{n} \to \mathbb{R}$$, el resultado se mantiene para cada par de índices $$i \neq j$$ (las otras variables quedan fijas, así que es el caso $$n=2$$) y la intuición de la prueba es la misma. En particular, si $$f \in C^{2}(D)$$ entonces $$D_{ij}f = D_{ji}f$$ en $$D$$ para todo $$i,j$$: el orden de derivación no importa.

#### Ejemplo (sin continuidad de la parcial cruzada, el orden sí importa)
Sea


$$
f(x,y) = \begin{cases}
\frac{xy(x^{2}-y^{2})}{x^{2}+y^{2}} \quad \text{si }(x,y) \neq (0,0) \\
0  \quad  \quad  \quad \text{si }(x,y) = (0,0)
\end{cases}.
$$


Para $$(x,y) \neq (0,0)$$, derivando el cociente $$\frac{x^{3}y - xy^{3}}{x^{2}+y^{2}}$$,


$$
D_{1}f(x,y) = \frac{y(x^{4}+4x^{2}y^{2}-y^{4})}{(x^{2}+y^{2})^{2}}, \qquad D_{2}f(x,y) = \frac{x(x^{4}-4x^{2}y^{2}-y^{4})}{(x^{2}+y^{2})^{2}},
$$


y como $$f$$ se anula sobre los ejes, $$D_{1}f(0,0) = D_{2}f(0,0) = 0$$. Evaluando sobre los ejes: $$D_{1}f(0,y) = \frac{-y^{5}}{y^{4}} = -y$$ y $$D_{2}f(x,0) = \frac{x^{5}}{x^{4}} = x$$. Por lo tanto


$$
D_{21}f(0,0) = \lim_{ k \to 0 } \frac{D_{1}f(0,k) - D_{1}f(0,0)}{k} = \lim_{ k \to 0 } \frac{-k}{k} = -1, \qquad D_{12}f(0,0) = \lim_{ h \to 0 } \frac{D_{2}f(h,0) - D_{2}f(0,0)}{h} = \lim_{ h \to 0 } \frac{h}{h} = 1.
$$


Las dos parciales cruzadas existen en el origen y **son distintas**. La hipótesis que falla es la continuidad de $$D_{21}f$$ en $$(0,0)$$: de hecho $$D_{21}f$$ toma en todo vecindario del origen valores tan distintos como $$-1$$ y $$1$$.

### Teorema (Teorema del valor medio)
Cf. Integral de Riemann (MA0350, TVM en una variable). Sea $$f: B_{\delta}(a) \subseteq \mathbb{R}^n \to \mathbb{R}$$. Suponga que $$f$$ es continua y que para todo $$j \in \{ 1,\dots,n \},$$ $$D_{j}(f)$$ existe y es continua. Entonces, para todo $$x \in B_{\delta}(a)$$, existen $$\xi_{1}, \dots \xi_{n} \in B_{\delta}(a)$$ tales que, si $$x = (x_{1},\dots, x_{n})$$ y $$a = (a_{1}, \dots, a_{n})$$, entonces


$$
f(x) - f(a)= \sum_{j=1}^{n} D_{j} f(\xi_{j}) (x_{j} - a_{j}).
$$


***Prueba:*** Para $$n=2$$, note que 


$$
f(x) - f(a) = f(x_{1},x_{2}) - f(a_{1}, x_{2}) + f(a_{1},x_{2}) - f(a_{1},a_{2}).
$$


Sean $$g(t) = f(t,x_{2})$$ y $$h(t) = f(a_{1},t)$$. Entonces, 


$$
\begin{aligned}
\implies f(x)-f(a) &= g(x_{1}) - g(a_{1}) + h(x_{2}) - h(a_{2}) \\
&\underset{TVM}{=} g'(t_{1}) (x_{1}-a_{1}) + h'(t_{2})(x_{2}-a_{2}) \\
&= D_{1}f(\underbrace{ t_{1},x_{2} }_{ \xi_{1} })(x_{1}-a_{1}) + D_{2} f(\underbrace{ a_{1}, t_{2} }_{ \xi_{2} })(x_{2}-a_{2}),
\end{aligned}
$$


con $$t_{i}$$ entre $$x_{i}$$ y $$a_{i}$$. Los puntos $$\xi_{1} = (t_{1},x_{2})$$ y $$\xi_{2} = (a_{1},t_{2})$$ están en la bola porque $$\lVert \xi_{1}-a \rVert^{2} = (t_{1}-a_{1})^{2} + (x_{2}-a_{2})^{2} \leq \lVert x-a \rVert^{2}$$, y análogamente para $$\xi_{2}$$. El razonamiento es análogo para $$n>2$$: se pasa de $$a$$ a $$x$$ cambiando una coordenada a la vez.

![El camino en escalera de la prueba del teorema del valor medio](/assets/img/courses/ma0450/tvm-camino.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[scale=1.6]
  \draw[dashed] (0,0) circle (1.9);
  \fill (0,0) circle (1.2pt) node[below left] {$a=(a_1,a_2)$};
  \fill (1.3,0.9) circle (1.2pt) node[above right] {$x=(x_1,x_2)$};
  \draw[orange, thick, ->] (0,0) -- (0,0.9) node[midway, left] {$h(t)=f(a_1,t)$};
  \draw[orange, thick, ->] (0,0.9) -- (1.3,0.9) node[midway, above] {$g(t)=f(t,x_2)$};
  \fill (0,0.9) circle (1.2pt) node[above left] {$(a_1,x_2)$};
  \fill[orange] (0,0.45) circle (1.3pt) node[right] {$\xi_2$};
  \fill[orange] (0.7,0.9) circle (1.3pt) node[below] {$\xi_1$};
  \node at (-1.3,-1.5) {$B_\delta(a)$};
\end{tikzpicture}
-->

#### Nota
El teorema es para funciones *escalares*. Para $$f:\mathbb{R}^n \to \mathbb{R}^{m}$$ con $$m>1$$ se aplica componente a componente, pero los puntos intermedios $$\xi$$ cambian de una componente a otra, y en general no hay un único $$\xi$$ que sirva para todas. Por ejemplo, $$\gamma(t) = (\cos t, \sin t)$$ cumple $$\gamma(2\pi) - \gamma(0) = (0,0)$$, pero $$\gamma'(t) = (-\sin t, \cos t) \neq (0,0)$$ para todo $$t$$, así que no existe $$\xi$$ con $$\gamma(2\pi)-\gamma(0) = \gamma'(\xi)\cdot 2\pi$$. Lo que sí sobrevive es la *desigualdad* del valor medio: si $$f \in C^{1}$$ en un abierto convexo que contiene a $$a$$ y $$x$$, entonces $$\lVert f(x) - f(a) \rVert \leq \sup_{\xi} \lVert J_{f}(\xi) \rVert \, \lVert x-a \rVert$$, con el supremo sobre el segmento.

#### Ejemplo 
Considere 


$$
f(x,y) = \begin{cases}
\frac{xy}{x^{2}+y^{2}} \quad \text{si }(x,y) \neq  (0,0) \\
0  \quad  \quad  \quad \text{si }(x,y) = (0,0)
\end{cases}.
$$


Note que 
1. $$f$$ no es continua en $$(0,0)$$: sobre la recta $$y = x$$ se tiene $$f(x,x) = \frac{x^{2}}{2x^{2}} = \frac{1}{2}$$ para todo $$x \neq 0$$, mientras que $$f(0,0) = 0$$.
2. $$\frac{\partial f}{\partial x} (0,0) = \lim_{ h \to 0 } \frac{f(h,0)-f(0,0)}{h} = \lim_{ h \to 0 } \frac{\frac{0 \cdot h}{h^{2}+0^{2}} - 0}{h} = 0$$.
3. Ahora, si $$(a,b) \neq (0,0)$$, entonces 


$$
\frac{\partial f}{\partial x}(a,b) = \frac{(x^{2}+y^{2})y - xy \cdot 2x}{(x^{2}+y^{2})^{2}} \biggr\rvert_{(x,y)=(a,b)} = \frac{b(b^{2}-a^{2})}{(a^{2}+b^{2})^{2}}.
$$


Así, 


$$
\frac{\partial f(x,y)}{\partial x} = \begin{cases}
\frac{y(y^{2}-x^{2})}{(x^{2}+y^{2})^{2}} \quad \text{si }(x,y) \neq (0,0) \\
0  \quad  \quad  \quad \text{si }(x,y) = (0,0)
\end{cases}
$$


y por simetría $$\frac{\partial f}{\partial y}(x,y) = \frac{x(x^{2}-y^{2})}{(x^{2}+y^{2})^{2}}$$ fuera del origen, con $$\frac{\partial f}{\partial y}(0,0) = 0$$. Así, **ambas derivadas parciales existen en todo $$\mathbb{R}^{2}$$** y sin embargo $$f$$ no es continua en $$(0,0)$$: en varias variables, la existencia de las derivadas parciales no implica continuidad. Note también que $$\frac{\partial f}{\partial x}$$ no es continua en $$(0,0)$$; ni siquiera es acotada, pues $$\frac{\partial f}{\partial x}(0,y) = \frac{y^{3}}{y^{4}} = \frac{1}{y} \to \infty$$ cuando $$y \to 0^{+}$$. Esto es consistente con el teorema siguiente: la continuidad de las parciales es justamente lo que falta.


### Teorema (Derivabilidad y continuidad)
Sea $$f:D\subseteq \mathbb{R}^n \to \mathbb{R}$$ tal que $$\frac{\partial f}{\partial x_{i}}(x)$$ existen y son continuas en $$D$$ (abierto) para todo $$i \in \{ 1,\dots,n \}$$. Entonces $$f$$ es continua en $$D$$.

***Prueba:*** Sean $$a \in D, \varepsilon>0$$. Entonces, existe $$r>0$$ tal que $$B:=\bar{B}_{r}(a) \subseteq D$$. Como $$B$$ es compacto y las $$\frac{\partial f}{\partial x_{i}}(x)$$ son continuas, existen $$M_{i} > 0$$ para todo $$i \in \{ 1,\dots,n \}$$ tales que $$\left\lvert   \frac{\partial f}{\partial x_{j}} (x) \right\rvert \leq M_{j}$$ para todo $$x \in B$$. Sea $$M = \max \{ M_{1}, \dots, M_{n} \}>0$$. Tome $$\delta < \min \left\{  \frac{\varepsilon}{Mn},r  \right\}$$.  Suponga que $$\lVert x-a \rVert<\delta$$, de modo que $$x \in B$$ y $$\lvert x_{j}-a_{j} \rvert < \delta$$ para todo $$j$$. Entonces, por el teorema del valor medio, $$f(x)-f(a) = \sum_{j=1}^{n} \frac{\partial f}{\partial x_{j}}(\xi_{j})(x_{j}-a_{j})$$, con $$\xi_{1}, \xi_{2},\dots,\xi_{n} \in B$$. Entonces 


$$
\begin{aligned}
\lvert f(x)-f(a) \rvert &\leq \sum_{j=1}^{n} \left\lvert \frac{\partial f}{\partial x_{j}}(\xi_{j}) \right\rvert \lvert x_{j}-a_{j} \rvert \\
&\leq \sum_{j=1}^{n} M\delta = nM\delta < \varepsilon 
\end{aligned}
$$



### Teorema (Extremos relativos y derivadas parciales)
Dada $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, suponga que $$f$$ alcanza un extremo relativo en $$c \in D^{\circ}$$. Si $$\frac{\partial f}{\partial x_{j}}(c)$$ existe, $$\frac{\partial f}{\partial x_{j}}(c) = 0$$.

***Prueba:*** Defina $$g(x) = f(c_{1},c_{2},\dots,c_{j-1},x,c_{j+1},\dots,c_{n})$$ con $$c = (c_{1},\dots,c_{n})$$, definida en un intervalo abierto alrededor de $$c_{j}$$ (pues $$c$$ es interior). Entonces $$g'(c_{j}) = \frac{\partial f}{\partial x_{j}}(c)$$. Como $$g$$ tiene extremo relativo en $$c_{j}$$, por el resultado de una variable $$g'(c_{j}) = \frac{\partial f}{\partial x_{j}}(c) = 0$$.

#### Nota 
Sea $$f:\mathbb{R} \to \mathbb{R}$$. Su derivada es $$f'(a) = \lim_{ x \to a } \frac{f(x)-f(a)}{x-a} = \lim_{ h \to 0 }\frac{f(a+h)-f(a)}{h}$$. Esta es la noción de derivabilidad; el ejemplo anterior muestra que tener derivadas parciales es una condición demasiado débil en varias variables (ni siquiera da continuidad). ¿Cuál es la noción correcta de diferenciabilidad?

## Diferenciabilidad

#### Nota
En una dimensión, $$f'(a)$$ existe si y solo si $$\lim_{ h \to 0 } \frac{f(a+h)-f(a)-f'(a)h}{h} = 0$$.

### Definición (Diferenciabilidad)
Dada $$f:D \subseteq \mathbb{R}^n\to \mathbb{R}^{m}$$, con $$D$$ vecindario de $$a$$. Se dice que $$f$$ es diferenciable en $$a$$ si existe una transformación lineal $$T:\mathbb{R}^n\to \mathbb{R}^{m}$$ tal que 


$$
\lim_{ \vec{h} \to 0 } \frac{\lVert f(a+\vec{h}) - f(a) - T(\vec{h}) \rVert_{m}}{\lVert \vec{h} \rVert_{n}}  = 0
$$


#### Notas
1. $$\frac{\partial f}{\partial x_{j}}(c) = \lim_{ h \to 0 } \frac{f(c+h e_{j})-f(c)}{h}$$, donde $$e_{j}$$ es el $$j$$-ésimo vector canónico.
2. Si la función es diferenciable en $$a$$, escribimos $$D_{f}(a)=T$$
3. Evaluar $$D_{f}$$ se escribe $$D_{f}(a)(x) = T(x)$$.
4. Para $$m = 1$$, la definición dice que $$f(a+h) = f(a) + T(h) + r(h)$$ con $$\frac{r(h)}{\lVert h \rVert} \to 0$$: la gráfica de la función afín $$x \mapsto f(a) + T(x-a)$$ es el **plano tangente** a la gráfica de $$f$$ en $$(a,f(a))$$, y el error de aproximar $$f$$ por ese plano es pequeño *incluso comparado con* $$\lVert h \rVert$$. Esa es la diferencia con tener solo derivadas parciales: las parciales controlan el error a lo largo de $$n$$ rectas; la diferenciabilidad lo controla en todas las direcciones a la vez.

![Diferenciabilidad: el plano tangente aproxima la gráfica con un error pequeño comparado con la norma del incremento](/assets/img/courses/ma0450/plano-tangente.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[x={(1cm,0cm)}, y={(0.5cm,0.4cm)}, z={(0cm,1cm)}, scale=1.3]
  % gráfica z = f(x,y) (paraboloide suave) como malla
  \foreach \yy in {0,0.5,...,2}
    \draw[gray!60, domain=0:3, samples=30] plot (\x, \yy, {2.2 - 0.18*(\x-1.6)^2 - 0.18*(\yy-1)^2});
  \foreach \xx in {0,0.5,...,3}
    \draw[gray!60, domain=0:2, samples=20] plot (\xx, \x, {2.2 - 0.18*(\xx-1.6)^2 - 0.18*(\x-1)^2});
  % plano tangente en (a,b) = (2.3,0.6): z = z0 + fx (x-a) + fy (y-b), fx=-0.252, fy=0.144
  \fill[orange, opacity=0.15] (1.3,-0.2,{2.1266+0.252-0.1152}) -- (3.3,-0.2,{2.1266-0.252-0.1152}) -- (3.3,1.4,{2.1266-0.252+0.1152}) -- (1.3,1.4,{2.1266+0.252+0.1152}) -- cycle;
  \draw[orange, thick] (1.3,-0.2,{2.1266+0.252-0.1152}) -- (3.3,-0.2,{2.1266-0.252-0.1152}) -- (3.3,1.4,{2.1266-0.252+0.1152}) -- (1.3,1.4,{2.1266+0.252+0.1152}) -- cycle;
  \fill[orange] (2.3,0.6,2.1266) circle (1.5pt) node[above right] {$(a,f(a))$};
  \draw[dashed] (2.3,0.6,0) -- (2.3,0.6,2.1266);
  \fill (2.3,0.6,0) circle (1.2pt) node[below] {$a$};
  % incremento h y error
  \fill (2.9,1.2,0) circle (1.2pt) node[below right] {$a+h$};
  \draw[->, thick] (2.3,0.6,0) -- (2.9,1.2,0) node[midway, below] {$h$};
  \draw[dashed] (2.9,1.2,0) -- (2.9,1.2,{2.1266-0.252*0.6+0.144*0.6});
  \draw[very thick] (2.9,1.2,{2.1266-0.252*0.6+0.144*0.6}) -- (2.9,1.2,{2.2-0.18*1.69-0.18*0.04}) node[midway, right] {$r(h) = o(\|h\|)$};
  \node[orange] at (1.0,1.5,2.5) {$z = f(a) + D_f(a)(x-a)$};
  \draw[->] (0,0,0) -- (3.6,0,0) node[right] {$x$};
  \draw[->] (0,0,0) -- (0,2.4,0) node[above] {$y$};
  \draw[->] (0,0,0) -- (0,0,2.8) node[above] {$z$};
\end{tikzpicture}
-->

#### Ejemplo 
Considere $$f:\mathbb{R}^n\to \mathbb{R}^{m}$$, con $$f(x) = c \in \mathbb{R}^{m}$$. Si $$T(x) = 0$$, entonces $$D_{f}(a) = 0$$, pues 


$$
\lim_{ h \to 0} \frac{\lVert c-c-0 \rVert }{\lVert h \rVert }  = 0
$$



#### Ejemplo 
Si $$f:\mathbb{R}\to \mathbb{R}$$ es derivable en $$a$$, entonces $$D_{f}(a)(h) = f'(a) h$$. El diferencial puede usarse para hacer aproximaciones, por ejemplo, de Taylor: $$f(a+h) \approx f(a) + hf'(a)$$.

#### Ejemplo 
Considere $$f:\mathbb{R}^{2}\to \mathbb{R}$$ con $$f(x,y) = x^{2}+3y$$ ¿$$D_{f}(a,b)$$? 
Sea $$(h,k)$$ el incremento del límite. Note que 


$$
\begin{aligned}
&  \lim_{ (h,k) \to (0,0) } \frac{\lvert (a+h)^{2}+3(b+k) - a^{2}-3b-T(h,k) \rvert }{\lVert (h,k)\rVert } \\
&= \lim_{ (h,k) \to (0,0) } \frac{\lvert 2ah+h^{2}+3k-T(h,k) \rvert }{ \sqrt{h^{2}+k^{2}}}=L
\end{aligned}
$$


Tome $$T(h,k) = 2ah + 3k$$. Claramente $$T$$ es lineal y además, si $$(h,k) \longrightarrow (0,0)$$ entonces $$T(h,k)\longrightarrow 0$$. Así, 


$$
L=\lim_{ (h,k) \to (0,0)} \frac{h^{2}}{\sqrt{ h^{2}+k^{2} }} = 0 
$$


pues 


$$
0 \leq  \frac{h^{2}}{\sqrt{ h^{2}+k^{2} }} \leq \frac{h^{2}}{\sqrt{ h^{2} }} = \lvert h \rvert \underset{(h,k) \rightarrow (0,0)}{\longrightarrow} 0,
$$


por lo tanto $$D_{f}(a,b)(h,k) = 2ah+3k =\begin{pmatrix}2a & 3\end{pmatrix} \begin{pmatrix}h \\ k\end{pmatrix}$$.

#### Ejemplo
Sea $$f(x,y) = xy$$. En $$(a,b)$$, $$f(a+h,b+k) - f(a,b) = (a+h)(b+k) - ab = bh + ak + hk$$. El candidato lineal es la parte de grado 1 en el incremento, $$T(h,k) = bh + ak$$, y el resto es $$hk$$. Como $$\lvert hk \rvert \leq \frac{h^{2}+k^{2}}{2}$$,


$$
\frac{\lvert hk \rvert}{\sqrt{ h^{2}+k^{2} }} \leq \frac{\sqrt{ h^{2}+k^{2} }}{2} \underset{(h,k) \rightarrow (0,0)}{\longrightarrow} 0,
$$


así que $$f$$ es diferenciable en $$(a,b)$$ con $$D_{f}(a,b)(h,k) = bh + ak$$ (en concordancia con $$\nabla f(a,b) = (b,a)$$, como veremos). Receta para polinomios: expandir $$f(a+h)$$, quedarse con la parte lineal en $$h$$, y comprobar que lo que sobra dividido entre $$\lVert h \rVert$$ tiende a cero.

 ### Teorema (Unicidad del diferencial)
Si $$f$$ es diferenciable en $$a$$, su diferencial es único.

***Prueba:*** Suponga que existen $$T, S: \mathbb{R}^n \to \mathbb{R}^{m}$$ lineales tales que cumplen definición. Entonces se cumple que 


$$
\begin{aligned}
\frac{\lVert T(h)-S(h) \rVert }{\lVert h \rVert } \leq  \frac{\lVert T(h) - f(a+h) + f(a) \rVert }{\lVert h \rVert } + \frac{\lVert f(a+h) - f(a) - S(h)  \rVert }{\lVert h \rVert } \underset{h \rightarrow 0}{\longrightarrow} 0. 
\end{aligned}
$$


Ocupo $$T(x) =  S(x) \quad \forall x \in \mathbb{R}^n$$. Luego, si $$x \in \mathbb{R}^n\setminus \{ 0 \}$$, $$t \in \mathbb{R}$$, tome $$h = tx$$. Así,


$$
0 = \lim_{ t \to 0 } \frac{\lVert T(tx) - S(tx) \rVert }{\lVert tx \rVert } = \lim_{ t \to 0 } \frac{\lVert T(x) - S(x) \rVert }{\lVert x \rVert } = \frac{\lVert T(x) - S(x) \rVert }{\lVert x \rVert },
$$


por lo que $$T(x) = S(x)$$ para todo $$x \in \mathbb{R}^n\setminus \{ 0 \}$$ (la igualdad en cero se cumple trivialmente por ser transformaciones lineales), y por tanto $$S = T$$.


### Teorema (Diferenciabilidad implica continuidad)
Si $$f$$ es diferenciable en $$a$$, entonces $$f$$ es continua en $$a$$.

***Prueba:*** Sea $$\varepsilon>0$$. Por diferenciabilidad existe $$\delta_{1}>0$$ tal que si $$\lVert h \rVert < \delta_{1}$$ entonces 


$$
\frac{\lVert f(a+h) - f(a) - D_{f}(a)(h) \rVert }{\lVert h \rVert} < \varepsilon. \ \tag{1}
$$


Como $$D_{f}(a)$$ es lineal, entonces es continua. Existe $$\delta_{2}>0$$ tal que 
$$\lVert x-a \rVert<\delta_{2} \implies \lVert D_{f}(a)(x) - D_{f}(a)(a) \rVert < \frac{\varepsilon}{2}. $$
Tome $$\delta = \min \left\{  \delta_{1}, \delta_{2}, \frac{1}{2}  \right\}$$. Suponga que $$\lVert x-a \rVert < \delta$$. Entonces 


$$
\begin{aligned}
\lVert f(x)-f(a) \rVert &\leq \lVert f(x) - f(a) - D_{f}(a)(x-a) \rVert + \lVert D_{f}(a)(x-a) \rVert  \\
&\leq \varepsilon \lVert x-a \rVert + \frac{\varepsilon}{2} \quad  \quad  \text{tomando } h =x-a \text{ en (1)}\\
&< \varepsilon \delta + \frac{\varepsilon}{2} \leq \varepsilon.
\end{aligned}
$$


Concluimos que $$f$$ es continua en $$a$$. 

### Definición (Derivada direccional)
Dado $$f:\mathbb{R}^n\to \mathbb{R}$$, $$\vec{u} \in \mathbb{R}^n$$, $$\lVert \vec{u} \rVert = 1$$, se define la derivada direccional en $$\vec{u}$$ como 


$$
D_{\vec{u}}f(a) = \lim_{ h \to 0 } \frac{f(a+h \vec{u}) - f(a)}{h}.
$$



#### Nota
Si $$\vec{u} = e_{j}$$, entonces $$D_{\vec{u}}f(a) = \frac{\partial f(a)}{\partial x_{j}}$$, pues $$a+h \vec{u} = a+h e_{j}$$. 
La derivada direccional mide la tasa de cambio de $$f$$ al salir de $$a$$ sobre la recta $$\{ a + h\vec{u} : h \in \mathbb{R} \}$$: es la derivada en $$h = 0$$ de la función de una variable $$\varphi(h) = f(a+h\vec{u})$$. Se pide $$\lVert \vec{u} \rVert = 1$$ para que $$h$$ mida la distancia recorrida; si no, la misma definición da $$D_{\lambda \vec{u}}f(a) = \lambda D_{\vec{u}}f(a)$$.

![La derivada direccional: la función restringida a la recta por a en dirección u](/assets/img/courses/ma0450/derivada-direccional.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[>=stealth]
  % panel izquierdo: dominio en R^2
  \begin{scope}
    \draw[->] (-0.3,0) -- (3.2,0) node[right] {$x_1$};
    \draw[->] (0,-0.3) -- (0,2.6) node[above] {$x_2$};
    \draw[gray, dashed] (-0.2,0.65) -- (3.1,2.3);
    \fill (1.2,1.35) circle (1.3pt) node[below right] {$a$};
    \draw[orange, very thick, ->] (1.2,1.35) -- ++(0.8,0.4) node[above left] {$\vec u$};
    \fill[orange] (2.0,1.75) circle (1.2pt) node[below right] {$a+h\vec u$};
    \node[gray] at (2.9,2.55) {$\{a+h\vec u\}$};
  \end{scope}
  % panel derecho: la función de una variable h -> f(a + h u)
  \begin{scope}[xshift=5cm]
    \draw[->] (-1.6,0) -- (1.9,0) node[right] {$h$};
    \draw[->] (0,-0.3) -- (0,2.6) node[above] {$\varphi(h)=f(a+h\vec u)$};
    \draw[orange, thick, domain=-1.4:1.7, samples=40] plot (\x, {1.3 + 0.5*\x - 0.15*\x*\x});
    \fill (0,1.3) circle (1.3pt) node[left] {$f(a)$};
    \draw[very thick] (-1.0,0.8) -- (1.0,1.8) node[right] {pendiente $D_{\vec u} f(a)$};
  \end{scope}
\end{tikzpicture}
-->

### Teorema (Diferenciabilidad y derivada direccional)
Sea $$f:D \subseteq \mathbb{R}^n\to \mathbb{R}$$, $$a \in D$$ abierto. Si $$f$$ es diferenciable en $$a$$, entonces $$D_{\vec{u}}f(a)$$ existe para todo $$\vec{u} \in \mathbb{R}^n$$ unitario, y $$D_{\vec{u}}f(a) = D_{f}(a)(u)$$.

***Prueba:*** Note que 


$$
\begin{aligned}
D_{\vec{u}}f(a) &= \lim_{ h \to 0 }\underbrace{  \frac{f(a+h \vec{u}) - f(a)-D_{f}(a)(hu)}{h} }_{ \longrightarrow 0 } + \frac{D_{f}(a)(\cancel{ h }u)}{\cancel{ h }} \\
&= D_{f}(a)(u),
\end{aligned}
$$


de donde se concluye el resultado. 

#### Corolario
Bajo la misma hipótesis, $$\frac{\partial f}{\partial x_{1}}, \dots, \frac{\partial f}{\partial x_{n}}$$ existen y $$D_{f}(a)(y) = \sum_{i=1}^{n} \frac{\partial f(a)}{\partial x_{i}} y_{i}$$ con $$y = (y_{1}, \dots, y_{n})$$.

***Prueba:*** La existencia de las derivadas parciales existen por el teorema anterior, tomando $$u$$ como cada uno de los vectores canónicos. Además, 


$$
\begin{aligned}
D_{f}(a)(y) &= D_{f}(a)\left( \sum_{i=1}^{n} e_{i} y_{i} \right) \\
&= \sum_{i=1}^{n} y_{i} D_{f}(a)(e_{i}) \\
&= \sum_{i=1}^{n} y_{i} \frac{\partial f(a)}{\partial x_{i}}.
\end{aligned}
$$



#### Nota
En notación de vectores, 


$$
D_{f}(a)(y) = \underbrace{ \begin{pmatrix}
\frac{ \partial f(a) }{ \partial x_{1}}  \\
\vdots \\
\frac{ \partial f(a) }{ \partial x_{n} } 
\end{pmatrix} }_{ \text{gradiente de } f \text{ en } a \text{: }\nabla f(a)} \cdot  \quad
\begin{pmatrix}
y_{1} \\
\vdots \\
y_{n}
\end{pmatrix}
\implies D_{f}(a)(y) = \nabla f(a) \cdot y.
$$



#### Ejemplo 
Considere $$f:\mathbb{R}^{3} \to \mathbb{R}$$ tal que $$f(x,y,z)= x^{2}+yz$$. Entonces 


$$
\nabla f (x,y,z) = \begin{bmatrix}
\frac{ \partial f }{ \partial x }(x,y,z)  \\
\frac{ \partial f }{ \partial y }(x,y,z)  \\
\frac{ \partial f }{ \partial z }(x,y,z) 
\end{bmatrix} = \begin{bmatrix}
2x \\
z \\
y
\end{bmatrix}.
$$


Si $$a = (1,-1,0)$$, entonces $$\nabla f(a) =\begin{bmatrix}2 & 0 & -1\end{bmatrix}^{T}$$ y entonces 


$$
D_{f}(a)(x,y,z) = \begin{bmatrix}
2 \\
0 \\
-1
\end{bmatrix} \cdot
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} = 2x-z.
$$



#### Ejemplo (continua y con parciales, pero no diferenciable)
Sea $$f(x,y) = \sqrt{ \lvert xy \rvert }$$. Es continua en $$\mathbb{R}^{2}$$ y se anula sobre los ejes, así que $$D_{1}f(0,0) = \lim_{ h \to 0 }\frac{f(h,0)-f(0,0)}{h} = 0$$ y $$D_{2}f(0,0) = 0$$. Si $$f$$ fuera diferenciable en $$(0,0)$$, por el corolario tendríamos $$D_{f}(0,0) = 0$$ y toda derivada direccional sería cero. Pero para $$\vec{u} = \left( \frac{1}{\sqrt{ 2 }}, \frac{1}{\sqrt{ 2 }} \right)$$,


$$
\frac{f(h\vec{u}) - f(0,0)}{h} = \frac{\sqrt{ h^{2}/2 }}{h} = \frac{\lvert h \rvert}{\sqrt{ 2 }\,h},
$$


que vale $$\frac{1}{\sqrt{ 2 }}$$ para $$h>0$$ y $$-\frac{1}{\sqrt{ 2 }}$$ para $$h<0$$: el límite no existe. Luego $$f$$ no es diferenciable en $$(0,0)$$ (ni siquiera tiene derivada direccional en esa dirección). **Tener parciales no implica ser diferenciable**, ni aun siendo continua.

#### Ejemplo (todas las derivadas direccionales existen, pero no es diferenciable)
Sea


$$
f(x,y) = \begin{cases}
\frac{x^{2}y}{x^{2}+y^{2}} \quad \text{si }(x,y) \neq (0,0) \\
0  \quad  \quad  \quad \text{si }(x,y) = (0,0)
\end{cases}.
$$


Es continua en el origen, pues $$\lvert f(x,y) \rvert \leq \frac{x^{2}\lvert y \rvert}{x^{2}+y^{2}} \leq \lvert y \rvert$$. Para $$\vec{u} = (u_{1},u_{2})$$ unitario, como $$f$$ es homogénea de grado 1 (es decir, $$f(hx,hy) = h f(x,y)$$),


$$
D_{\vec{u}}f(0,0) = \lim_{ h \to 0 } \frac{f(hu_{1},hu_{2})}{h} = \lim_{ h \to 0 } \frac{h\,f(u_{1},u_{2})}{h} = f(u_{1},u_{2}) = u_{1}^{2}u_{2}.
$$


Así *todas* las derivadas direccionales existen en $$(0,0)$$; en particular $$D_{1}f(0,0) = D_{2}f(0,0) = 0$$. Pero si $$f$$ fuera diferenciable, el teorema daría $$D_{\vec{u}}f(0,0) = \nabla f(0,0) \cdot \vec{u} = 0$$ para todo $$\vec{u}$$, mientras que $$u_{1}^{2}u_{2} \neq 0$$ en general (p. ej. $$\vec{u} = \frac{(1,1)}{\sqrt{ 2 }}$$ da $$\frac{1}{2\sqrt{ 2 }}$$). La obstrucción es que $$\vec{u} \mapsto D_{\vec{u}}f(0,0)$$ **no es lineal** en $$\vec{u}$$, mientras que para una función diferenciable siempre lo es ($$= D_{f}(a)(\vec{u})$$).

#### Nota (resumen de implicaciones en un punto $$a$$)


$$
f \in C^{1} \text{ cerca de } a \implies f \text{ diferenciable en } a \implies \begin{cases} f \text{ continua en } a, \\ \text{todas las } D_{\vec{u}}f(a) \text{ existen y } \vec{u} \mapsto D_{\vec{u}}f(a) \text{ es lineal} \end{cases} \implies \text{las parciales existen en } a,
$$


y ninguna de las flechas se revierte: los ejemplos de esta sección y de la siguiente son los contraejemplos (la primera implicación se prueba más abajo).

### Teorema (Diferenciabilidad por entradas de funciones)
Sea $$f:\mathbb{R}^n \to \mathbb{R}^{m}$$, $$f =\begin{pmatrix}f_{1} \\ \vdots \\ f_{m}\end{pmatrix}$$, $$f_{j}:\mathbb{R}^n\to \mathbb{R}$$. Entonces $$f$$ es diferenciable en $$a$$ si y solo si $$f_{j}$$ es diferenciable en $$a$$ para todo $$j \in \{ 1,\dots ,m \}$$. Además, 


$$
D_{f}(a) = \begin{bmatrix}
D_{f_{1}}(a) \\
\vdots \\
D_{f_{m}}(a)
\end{bmatrix}.
$$


***Prueba:*** Sabemos que para todo $$x \in \mathbb{R}^{m}$$ y para todo $$j \in \{ 1,\dots,m \}$$, $$\lvert x_{j} \rvert \leq \lVert x \rVert \leq \sum_{j=1}^{m} \lvert x_{j} \rvert$$. Si $$T = (T_{1},\dots,T_{m})$$ es lineal (cada $$T_{j}:\mathbb{R}^n\to \mathbb{R}$$ lineal), aplicando esto a $$x = f(a+h)-f(a)-T(h)$$ tenemos que 


$$
\begin{aligned}
0 \leq  \frac{\lvert f_{j}(a+h) - f_{j}(a) - T_{j}(h) \rvert }{\lVert h \rVert } &\leq \frac{\lVert f(a+h) -f(a) - T(h) \rVert }{\lVert h \rVert } \\
&\leq \sum_{j=1}^{m} \frac{\lvert f_{j}(a+h) -f_{j}(a) - T_{j}(h)\rvert}{\lVert h \rVert }.
\end{aligned}
$$


($$\implies$$): Si $$f$$ es diferenciable en $$a$$ con $$D_{f}(a) = T$$, el término del medio tiende a cero, y por la desigualdad de la izquierda también lo hace cada cociente $$\frac{\lvert f_{j}(a+h) - f_{j}(a) - T_{j}(h) \rvert }{\lVert h \rVert }$$; así $$f_{j}$$ es diferenciable en $$a$$ con $$D_{f_{j}}(a) = T_{j}$$.

($$\impliedby$$): Si cada $$f_{j}$$ es diferenciable en $$a$$, tome $$T_{j} = D_{f_{j}}(a)$$ y $$T = (T_{1},\dots,T_{m})$$. Cada sumando de la derecha tiende a cero, luego el término del medio también, y $$f$$ es diferenciable en $$a$$ con $$D_{f}(a) = T$$.

### Definición (Matriz jacobiana)
Sea $$f$$ diferenciable en $$a$$. Como $$D_{f}(a):\mathbb{R}^n \to \mathbb{R}^{m}$$, considere $$J_{f}(a)$$ (matriz jacobiana de $$f$$ en $$a$$) como la matriz asociada a $$D_{f}(a)$$ en bases canónicas.

#### Corolario
Si $$f:\mathbb{R}^n\to \mathbb{R}^{m}$$, $$f = \begin{pmatrix}f_{1} & \dots & f_{m}\end{pmatrix}^{T}$$ es diferenciable en $$a$$ entonces $$\frac{ \partial f_{i}(a) }{ \partial x_{j} }$$ existen para todos $$j \in \{ 1,\dots n \}$$, $$i \in \{ 1,\dots,m \}$$. Además, $$[J_{f}(a)]_{ij} =  \frac{ \partial f_{i}(a) }{ \partial x_{j} }$$. Esto es 


$$
J_{f}(a) = \begin{bmatrix}
\frac{ \partial f_{1}(a) }{ \partial x_{1} } & \frac{ \partial f_{1}(a) }{ \partial x_{2} } & \dots & \frac{ \partial f_{1}(a) }{ \partial x_{n} } \\
\frac{ \partial f_{2}(a) }{ \partial x_{1} } & \frac{ \partial f_{2}(a) }{ \partial x_{2} }  & \dots  & \frac{ \partial f_{2}(a) }{ \partial x_{n} } \\
\vdots & \vdots & \ddots & \vdots \\
\frac{ \partial f_{m}(a) }{ \partial x_{1} } & \frac{ \partial f_{m}(a) }{ \partial x_{2} } & \dots & \frac{ \partial f_{m}(a) }{ \partial x_{n} }
\end{bmatrix}_{m \times n}
$$



#### Ejemplo
Considere $$f(x,y,z) = \begin{pmatrix}x^{2}\sin y - z \\ e^{xy} + zx\end{pmatrix}$$. Entonces, 


$$
J_{f}(x,y,z) = \begin{bmatrix}
2x\sin y & x^{2}\cos y & -1 \\
y e^{xy}+z & xe^{xy} & x
\end{bmatrix}.
$$


Si $$(a,b,c) = (1,0,\pi)$$, 


$$
\begin{aligned}
\implies J_{f}(a,b,c) &= \begin{bmatrix} 
0 & 1 & -1 \\
\pi & 1 & 1 
\end{bmatrix} \\
\implies D_{f}(a,b,c)(x,y,z) &= \begin{bmatrix}
0 & 1 & -1 \\
\pi & 1 & 1 
\end{bmatrix} \begin{bmatrix} 
x \\ 
y \\ 
z 
\end{bmatrix} = \begin{bmatrix} 
y-z \\
\pi x+y+z
\end{bmatrix}.
\end{aligned}
$$



### Teorema (Jacobiano y gradiente)
Sea $$f:A\subseteq \mathbb{R}^n \to \mathbb{R}$$ con $$A$$ abierto. Suponga que $$f$$ es continuamente derivable en $$a$$; esto es, las derivadas parciales de primer orden de $$f$$ existen en un vecindario de $$a$$ y son continuas en $$a$$. Entonces, $$f$$ es diferenciable en $$a$$ y $$J_{f}(a) = \nabla f(a)^{T}$$.

***Prueba:*** Sea $$\varepsilon>0$$. Por continuidad, existen $$\delta_{1},\dots,\delta_{n}$$ tales que para todo $$1\leq j\leq n$$ si $$\lVert x-a \rVert <\delta_{j}$$, entonces $$\left\lVert  \frac{ \partial f }{ \partial x_{j} }(x) - \frac{ \partial f }{ \partial x_{j} }(a)  \right\rVert < \frac{\varepsilon}{n}$$. Sea $$T:\mathbb{R}^n\to \mathbb{R}$$ una transformación lineal con $$T(x_{1},\dots,x_{n}) = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(a) \cdot x_{i}$$ . Tome $$\delta = \min\{ \delta_{1},\dots,\delta_{n} \}$$ (achicándolo si hace falta para que las parciales existan en $$B_{\delta}(a)$$) y sea $$h = (h_{1},\dots, h_{n})$$ con $$0<\lVert h \rVert < \delta$$. Por el teorema del valor medio, existen $$\xi_{1}, \dots, \xi_{n} \in B_{\delta}(a)$$ tales que  


$$
f(a+h)-f(a) = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(\xi_{i}) \cdot h_{i}.
$$



Así, haciendo uso de esta expresión en la definición de diferenciabilidad, y como $$\lVert \xi_{i} - a \rVert < \delta$$: 


$$
\begin{aligned}
\frac{\lvert f(a+h) - f(a) - T(h) \rvert }{\lVert h \rVert } &= \frac{1}{\lVert h \rVert } \left\lvert  \sum_{i=1}^{n} \left( \frac{ \partial f }{ \partial x_{i} }(\xi_{i}) - \frac{ \partial f }{ \partial x_{i} }(a) \right) h_{i} \right\rvert \\
&\leq  \sum_{i=1}^{n} \left\lvert \frac{ \partial f }{ \partial x_{i} }(\xi_{i}) - \frac{ \partial f }{ \partial x_{i} }(a) \right\rvert \underbrace{ \frac{\lvert h_{i} \rvert }{\lVert h \rVert } }_{ \leq 1 } < \sum_{i=1}^{n} \frac{\varepsilon}{n} = \varepsilon,
\end{aligned}
$$


de donde concluimos que $$D_{f}(a) = T$$.

### Teorema (Jacobiano y gradientes en funciones hacia $$\mathbb{R}^{m}$$)
Sea $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ con $$A$$ abierto y $$a \in A$$. Suponga que $$f$$ es continuamente derivable en $$a$$. Entonces $$f$$ es diferenciable en $$a$$ y $$J_{f}(a) = [\nabla f_{1}(a), \nabla f_{2}(a),\dots, \nabla f_{m}(a)]^{T}$$; es decir, la fila $$j$$ de $$J_{f}(a)$$ es $$\nabla f_{j}(a)^{T}$$.

***Prueba:*** Por hipótesis, para todos $$1 \leq i \leq n$$, $$1 \leq j \leq m$$, $$D_{i} f_{j}(x)$$ existen cerca de $$a$$ y son continuos en $$a$$. Por el teorema anterior, $$f_{j}$$ es diferenciable en $$a$$ con $$J_{f_{j}}(a) = \nabla f_{j}(a)^{T}$$. Luego, como $$f_{j}$$ es diferenciable en $$a$$ para todo $$j$$, por el teorema de diferenciabilidad por entradas $$f = (f_{1},\dots,f_{m})$$ es diferenciable en $$a$$ y $$J_{f}(a)$$ tiene por filas los $$J_{f_{j}}(a)$$.

### Definición (Clases de funciones)
Se dice que $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ ($$D$$ abierto) es de clase $$C^{k}$$ ($$f \in C^{k}(D)$$) si todas sus derivadas parciales de orden menor o igual que $$k$$ existen y son continuas en $$D$$. Por el teorema anterior, $$f \in C^{1}(D)$$ implica que $$f$$ es diferenciable en todo punto de $$D$$; el recíproco es falso (ver el ejemplo más abajo). Similarmente, decimos que $$f \in C^{\infty}(D)$$ si para todo $$k \in \mathbb{N}$$, $$f \in C^{k}(D)$$. Si $$f:D\to B$$, escribimos la definición como $$f \in C^{k}(D,B)$$.

#### Ejemplo (diferenciable pero no $$C^{1}$$)
Sea $$f(x,y) = (x^{2}+y^{2})\sin\left( \frac{1}{\sqrt{ x^{2}+y^{2} }} \right)$$ para $$(x,y) \neq (0,0)$$ y $$f(0,0) = 0$$. Con $$T = 0$$,


$$
\frac{\lvert f(h,k) - f(0,0) - 0 \rvert}{\sqrt{ h^{2}+k^{2} }} = \sqrt{ h^{2}+k^{2} }\,\left\lvert \sin\left( \frac{1}{\sqrt{ h^{2}+k^{2} }} \right) \right\rvert \leq \sqrt{ h^{2}+k^{2} } \underset{(h,k) \rightarrow (0,0)}{\longrightarrow} 0,
$$


así que $$f$$ es diferenciable en $$(0,0)$$ con $$D_{f}(0,0) = 0$$. Sin embargo, para $$(x,y) \neq (0,0)$$, escribiendo $$\rho = \sqrt{ x^{2}+y^{2} }$$ y usando $$\frac{ \partial \rho }{ \partial x } = \frac{x}{\rho}$$,


$$
D_{1}f(x,y) = 2x\sin\left( \frac{1}{\rho} \right) - \frac{x}{\rho}\cos\left( \frac{1}{\rho} \right),
$$


y sobre el eje $$x$$ ($$y = 0$$, $$x>0$$) esto es $$2x\sin\left( \frac{1}{x} \right) - \cos\left( \frac{1}{x} \right)$$, que no tiene límite cuando $$x \to 0^{+}$$. Luego $$D_{1}f$$ no es continua en $$(0,0)$$ y $$f \notin C^{1}$$ en ningún vecindario del origen: **diferenciable no implica $$C^{1}$$**.

### Teorema (Gradiente cero)
Sea $$f \in C^{1}(D, \mathbb{R}^{m})$$ con $$D \subseteq \mathbb{R}^{n}$$ abierto y conexo. Si $$J_{f}(x) = 0$$ para todo $$x \in D$$ (para $$m=1$$: $$\nabla f(x) = 0$$), entonces $$f$$ es constante en $$D$$.

***Prueba:***  Basta probarlo para $$m =1$$ (se aplica a cada componente). Sea $$a \in D$$. Como $$D$$ es abierto, existe $$\delta > 0$$ tal que $$B_{\delta}(a) \subseteq D$$. Sea $$x \in B_{\delta}(a)$$. Por el TVM, existen $$\xi_{1},\dots,\xi_{n} \in B_{\delta}(a)$$ tales que $$f(x)-f(a) = \sum_{j=1}^{n} \underbrace{ \frac{ \partial f }{ \partial x_{j} }(\xi_{j}) }_{ =0 } \cdot (x_{j}-a_{j}) = 0$$. Luego, $$f(x) = f(a)$$ para todo $$x \in B_{\delta}(a)$$: **$$f$$ es localmente constante**.

Ahora, sea $$A = \{ x \in D:f(x) = f(a) \}$$. Note que $$A \neq \emptyset$$ pues $$a \in A$$. Veamos que $$A$$ es abierto: dado $$y \in A$$, por lo anterior (aplicado en $$y$$) existe $$\delta_{y} > 0$$ tal que $$f(x) = f(y) = f(a)$$ para todo $$x \in B_{\delta_{y}}(y)$$, es decir, $$B_{\delta_{y}}(y) \subseteq A$$. Por otro lado, el conjunto $$B=\{ x \in D: f(x)\neq f(a) \} = f^{-1}[(-\infty,f(a)) \cup(f(a), \infty)]$$ es abierto, por ser preimagen de un abierto bajo una función continua definida en el abierto $$D$$.
Como $$D = A \cup B$$ con $$A \cap B = \emptyset$$, $$A$$ y $$B$$ abiertos, y $$D$$ es conexo, uno de los dos es vacío. Como $$A \neq \emptyset$$, se sigue que $$B = \emptyset$$. Luego, $$A = D$$, y por tanto $$f$$ es constante en $$D$$.

#### Nota
La conexidad es esencial. Si $$D = (-\infty,0) \cup (0,\infty) \subseteq \mathbb{R}$$ y $$f(x) = \operatorname{sgn}(x)$$, entonces $$f'(x) = 0$$ en todo $$D$$ pero $$f$$ no es constante: es localmente constante, con un valor distinto en cada componente conexa.

## Reglas de derivación
### Teorema (Reglas de derivación)
Sea $$D \subseteq \mathbb{R}^n$$ vecindario de $$a$$. Dadas $$f:D \to \mathbb{R}^{m}$$ y $$g:D\to \mathbb{R}$$ diferenciables en $$a$$, y $$\lambda \in \mathbb{R}$$:
1. Si $$g:D\to \mathbb{R}^{m}$$, $$D_{f\pm g}(a) = D_{f}(a) \pm D_{g}(a)$$ y $$D_{\lambda f}(a) = \lambda D_{f}(a)$$,
2. $$D_{gf}(a)(h) = g(a)\, D_{f}(a)(h) + D_{g}(a)(h)\, f(a)$$ (producto de un escalar por un vector; para $$m=1$$ es la regla del producto usual),
3. Si $$g(a) \neq 0$$,


$$
D_{\frac{f}{g}}(a)(h) = \frac{g(a)\,D_{f}(a)(h)-D_{g}(a)(h)\,f(a)}{[g(a)]^{2}}.
$$


***Prueba:*** (1) es inmediato de la definición, pues la suma de transformaciones lineales es lineal y $$\lVert (f+g)(a+h) - (f+g)(a) - (T+S)(h) \rVert \leq \lVert f(a+h)-f(a)-T(h) \rVert + \lVert g(a+h)-g(a)-S(h) \rVert$$.

(2) Sean $$T = D_{f}(a)$$ y $$S = D_{g}(a)$$, y sea $$L(h) = g(a)T(h) + S(h)f(a)$$, que es lineal. Escribimos $$f(a+h) = f(a) + T(h) + r(h)$$ y $$g(a+h) = g(a) + S(h) + \rho(h)$$, con $$\frac{\lVert r(h) \rVert}{\lVert h \rVert} \to 0$$ y $$\frac{\lvert \rho(h) \rvert}{\lVert h \rVert} \to 0$$. Multiplicando,


$$
(gf)(a+h) - (gf)(a) - L(h) = \underbrace{ S(h)T(h) + S(h)r(h) + \rho(h)T(h) + \rho(h) r(h) }_{ E(h) } + g(a)r(h) + \rho(h) f(a).
$$


Los dos últimos términos, divididos entre $$\lVert h \rVert$$, tienden a cero. Para $$E(h)$$, use que $$T$$ y $$S$$ son lineales, luego $$\lVert T(h) \rVert \leq M\lVert h \rVert$$ y $$\lvert S(h) \rvert \leq M \lVert h \rVert$$ para algún $$M>0$$; así


$$
\frac{\lVert E(h) \rVert}{\lVert h \rVert} \leq M^{2}\lVert h \rVert + M\lVert r(h) \rVert + M \lvert \rho(h) \rvert + \lvert \rho(h) \rvert \frac{\lVert r(h) \rVert}{\lVert h \rVert} \underset{h \rightarrow 0}{\longrightarrow} 0,
$$


pues $$r(h) \to 0$$ y $$\rho(h) \to 0$$ (cada sumando es un producto de una cantidad acotada por una que tiende a cero). Por lo tanto $$D_{gf}(a) = L$$.

(3) Por continuidad, $$g \neq 0$$ cerca de $$a$$. Basta ver que $$\frac{1}{g}$$ es diferenciable en $$a$$ con $$D_{1/g}(a)(h) = -\frac{D_{g}(a)(h)}{g(a)^{2}}$$ y aplicar (2) a $$\frac{1}{g}\cdot f$$. En efecto,


$$
\frac{1}{g(a+h)} - \frac{1}{g(a)} + \frac{S(h)}{g(a)^{2}} = \frac{g(a) - g(a+h)}{g(a)g(a+h)} + \frac{S(h)}{g(a)^{2}} = \frac{-S(h)-\rho(h)}{g(a)g(a+h)} + \frac{S(h)}{g(a)^{2}} = \frac{S(h)\,(g(a+h)-g(a))}{g(a)^{2}g(a+h)} - \frac{\rho(h)}{g(a)g(a+h)},
$$


y ambos términos, divididos entre $$\lVert h \rVert$$, tienden a cero (el primero porque $$\frac{\lvert S(h) \rvert}{\lVert h \rVert} \leq M$$ y $$g(a+h)-g(a) \to 0$$ por continuidad; el segundo por definición de $$\rho$$).

### Teorema (Regla de la cadena)
Sea $$D \subseteq \mathbb{R}^n$$, con $$D$$ vecindario de $$a$$. Suponga que $$f:D \to \mathbb{R}^{m}$$ es diferenciable en $$a$$. Sea $$E \subseteq \mathbb{R}^{m}$$ vecindario de $$f(a)$$ con $$f(D) \subseteq E$$, y $$g:E \to \mathbb{R}^{p}$$ diferenciable en $$f(a)$$. Entonces, $$g \circ f:D \subseteq \mathbb{R}^n\to \mathbb{R}^{p}$$ es diferenciable en $$a$$ y además $$D_{g \circ f}(a) = D_{g}(f(a)) \circ D_{f}(a)$$, esto es, $$J_{g \circ f}(a) = J_{g}(f(a)) \cdot J_{f}(a)$$ (producto de matrices $$p \times m$$ por $$m \times n$$).

![La regla de la cadena como composición de aproximaciones lineales](/assets/img/courses/ma0450/regla-de-la-cadena.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[node distance=3.2cm, >=stealth]
  \node (A) {$\mathbb{R}^n$};
  \node (B) [right of=A] {$\mathbb{R}^m$};
  \node (C) [right of=B] {$\mathbb{R}^p$};
  \draw[->, thick] (A) -- node[above] {$f$} node[below] {$J_f(a)$, $m\times n$} (B);
  \draw[->, thick] (B) -- node[above] {$g$} node[below] {$J_g(f(a))$, $p\times m$} (C);
  \draw[->, thick, orange, bend left=35] (A) to node[above] {$g\circ f$, \ $J_g(f(a))\,J_f(a)$, $p\times n$} (C);
  \node[below of=A, node distance=1.2cm] {$a$};
  \node[below of=B, node distance=1.2cm] {$f(a)$};
  \node[below of=C, node distance=1.2cm] {$g(f(a))$};
\end{tikzpicture}
-->

***Prueba:*** Sabemos lo siguiente:
1. Por diferenciabilidad de $$g$$ en $$f(a)$$, dado $$\varepsilon>0$$, existe $$\delta_{1} > 0$$ tal que si $$\lVert h_{1} \rVert<\delta_{1}$$, entonces 


$$
\lVert g(f(a)+h_{1}) - g(f(a)) - S(h_{1}) \rVert \leq \varepsilon \lVert h_{1} \rVert  \quad \text{con }S = D_{g}(f(a))
$$


(con $$\leq$$ para que la desigualdad valga también cuando $$h_{1} = 0$$).
2. Por continuidad de $$f$$ en $$a$$, existe $$\delta>0$$ tal que si $$\lVert h \rVert<\delta$$, entonces $$\lVert f(a+h) - f(a) \rVert < \delta_{1}$$.
3. Por diferenciabilidad de $$f$$, existe $$\delta_{2}>0$$ tal que si $$\lVert h \rVert < \delta_2$$ entonces $$\lVert f(a+h)-f(a)-T(h) \rVert < \varepsilon \lVert  h \rVert$$ con $$T=D_{f}(a)$$.
4. Por linealidad de $$T$$, existe $$M>0$$ tal que $$\lVert T(x) \rVert \leq M \lVert x \rVert$$ para todo $$x$$.

Hay que probar que $$D_{g \circ f}(a) = S \circ T$$. Note que 


$$
\begin{aligned}
\lim_{ h \to 0 } &\frac{\lVert (g \circ f)(a+h) - (g \circ f)(a) - S T (h) \rVert }{\lVert h \rVert } \\
\leq &\lim_{ h \to 0 } \underbrace{ \frac{\lVert g(f(a+h)) - g(f(a)) - S(f(a+h)-f(a))\rVert }{\lVert h \rVert } }_{ A } \\ + &\lim_{ h \to 0 }\underbrace{ \frac{\lVert S(f(a+h)-f(a)) - S(T(h))\rVert }{\lVert h \rVert } }_{ B }.
\end{aligned}
$$


Note que $$B = \left\lVert  S\left( \frac{f(a+h)-f(a) - T(h)}{\lVert  h \rVert} \right)  \right\rVert\underset{h \rightarrow 0}{\longrightarrow} 0$$, pues $$S$$ es continua y el argumento tiende a cero por diferenciabilidad de $$f$$.
Para $$A$$, tome $$h_{1} = f(a+h)-f(a)$$ en la condición (1), lo cual es válido por (2). Entonces, para $$0<\lVert h \rVert < \tilde{\delta} := \min \{ \delta, \delta_{2} \}$$, tenemos que 


$$
\begin{aligned}
\frac{\lVert (g(f(a+h))-g(f(a)) - S(f(a+h)-f(a))  \rVert}{\lVert h \rVert } &\leq  \frac{\varepsilon \lVert f(a+h) - f(a) \rVert}{\lVert h \rVert } \\
&\leq \frac{\varepsilon \lVert f(a+h) - f(a) - T(h) \rVert + \varepsilon \lVert T(h) \rVert}{\lVert h \rVert } \\
& \leq  \frac{\varepsilon^{2} \lVert h \rVert + M \varepsilon \lVert h \rVert}{\lVert h \rVert } = \varepsilon^{2} + M \varepsilon,
\end{aligned}
$$


y como $$\varepsilon$$ es arbitrario, $$A \underset{h \rightarrow 0}{\longrightarrow} 0$$, de donde concluimos el resultado.

### Teorema (Regla de la cadena y derivadas parciales)
Sea $$g=(g_{1},\dots,g_{m}):\mathbb{R}^n\to \mathbb{R}^{m}$$ de clase $$C^{1}$$ en $$a$$ y $$f:\mathbb{R}^{m}\to \mathbb{R}^{p}$$ de clase $$C^{1}$$ en $$g(a)$$. Entonces $$h = f \circ g:\mathbb{R}^n\to \mathbb{R}^{p}$$ es $$C^{1}$$ en $$a$$. Además, para $$i \in \{ 1,\dots,n \}$$, $$j \in \{ 1,\dots,p \}$$ 


$$
\frac{ \partial h_{j} }{ \partial x_{i} }(a) = \sum_{k=1}^{m} \frac{ \partial f_{j} }{ \partial y_{k} } (g(a)) \cdot \frac{ \partial g_{k} }{ \partial x_{i} } (a),
$$


donde $$y_{1},\dots,y_{m}$$ denotan las variables de $$f$$. (La suma corre sobre la dimensión intermedia $$m$$: cada variable $$y_{k}$$ de $$f$$ es una ruta por la que $$x_{i}$$ influye en $$h_{j}$$.)


***Prueba:*** Sabemos que $$g$$ es diferenciable en $$a$$ y $$f$$ es diferenciable en $$g(a)$$. Así, por el teorema anterior, $$h$$ es diferenciable en $$a$$ y $$J_{h}(a) =J_{f}(g(a)) J_{g}(a)$$. Luego, 


$$
\begin{aligned}
\frac{ \partial h_{j} }{ \partial x_{i} }(a) = (J_{h}(a))_{ji} &= (J_{f}(g(a))J_{g}(a))_{ji}\\
&= \sum_{k=1}^{m} (J_{f}(g(a)))_{jk}(J_{g}(a))_{ki} \\
&= \sum_{k=1}^{m} \frac{ \partial f_{j} }{ \partial y_{k} } (g(a)) \cdot \frac{ \partial g_{k} }{ \partial x_{i} } (a).
\end{aligned}
$$



#### Ejemplo 
Sea $$f:\mathbb{R}^{2} \to \mathbb{R}$$ de clase $$C^{2}$$ y $$g:\mathbb{R}^{2}\to \mathbb{R}^{2}$$ dada por $$g(r, \theta) = (r\cos \theta, r \sin \theta)$$ (coordenadas polares). En este caso, $$h = f \circ g:\mathbb{R}^{2}\to \mathbb{R}$$ es $$h(r, \theta) = f(g_{1}, g_{2})$$, con $$g_{1} = r \cos \theta$$ y $$g_{2} = r \sin \theta$$.

Matricialmente 


$$
\begin{aligned}
\begin{bmatrix}
\frac{ \partial h }{ \partial r } & \frac{ \partial h }{ \partial \theta }  \\
\end{bmatrix} \biggr\rvert_{(r, \theta)}  &= \begin{bmatrix} 
\frac{ \partial f }{ \partial x }  & \frac{ \partial f }{ \partial y }   \\
\end{bmatrix} \biggr\rvert_{(g_{1},g_{2})}  
\begin{bmatrix}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta \\
\end{bmatrix} \\
&= \begin{bmatrix}
\cos \theta \frac{ \partial f }{ \partial x } + \sin \theta \frac{ \partial f }{ \partial y } & -r \sin \theta \frac{ \partial f }{ \partial x } + r \cos \theta \frac{ \partial f }{ \partial y }.
\end{bmatrix}
\end{aligned}
$$


Otra forma de escribirlo es


$$
D_{1} h(r, \theta) = \cos \theta \cdot D_{1} f(r \cos \theta, r \sin \theta) + \sin \theta \cdot D_{2}f(r \cos \theta, r \sin \theta).
$$


El diagrama de árbol para $$f$$ y $$f_{x}$$ es el siguiente:
![Arbol 1](/assets/img/courses/ma0450/Arbol%201.svg)
La segunda derivada respecto a $$r$$ viene dada por 


$$
\begin{aligned}
\frac{ \partial^{2} h }{ \partial r^{2} } &= \frac{ \partial }{ \partial r }\left( \frac{ \partial f }{ \partial x } \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial y } \frac{ \partial g_{2} }{ \partial r }  \right)  \\
&= \frac{ \partial  }{ \partial r }\left( \frac{ \partial f }{ \partial x }  \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial x } \frac{ \partial^{2} g_{1} }{ \partial r^{2} } + \frac{ \partial  }{ \partial r }\left( \frac{ \partial f }{ \partial y }  \right) \frac{ \partial g_{2} }{ \partial r } + \frac{ \partial f }{ \partial y } \frac{ \partial^{2} g_{2} }{ \partial r^{2} } \\
&= \left( f_{xx} \frac{ \partial g_{1} }{ \partial r } + f_{xy} \frac{ \partial g_{2} }{ \partial r }   \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial x } \underbrace{ \frac{ \partial^{2} g_{1} }{ \partial r^{2} } }_{ 0 } \\
&  \quad + \left( f_{yx} \frac{ \partial g_{1} }{ \partial r } 
+ f_{yy} \frac{ \partial g_{2} }{ \partial r }   \right) \frac{ \partial g_{2} }{ \partial r } + \frac{ \partial f }{ \partial y } \underbrace{ \frac{ \partial^{2} g_{2} }{ \partial r^{2} } }_{ 0 } \\
&=f_{xx} \cos^{2} \theta + 2f_{xy} \sin \theta \cos \theta + f_{yy} \sin^{2} \theta \quad (\text{usando } f_{xy} = f_{yx} \text{ por Schwarz}) \\
&=D_{11}f(r \cos \theta, r\sin \theta) \cos ^{2} \theta+ 2 D_{12} f(r \cos \theta, r \sin \theta) \sin \theta \cos \theta \\
&  \quad+ D_{22} f(r \cos \theta, r \sin \theta) \sin ^{2} \theta
\end{aligned}
$$



#### Ejemplo 
Sean $$f:\mathbb{R}^{3}\to \mathbb{R}$$, $$g,h: \mathbb{R}^{2}\to \mathbb{R}$$, $$w:\mathbb{R}^{3}\to \mathbb{R}$$ con 


$$
w(x,y,z) = f(g(x,z),h(g(x,z),y),z) = f(u,v,z)
$$


con $$u=g(x,z)$$, $$v=h(r,y)$$ y $$r = g(x,z)$$. El diagrama de árbol registra todas las rutas por las que cada variable independiente llega a $$w$$:
![Arbol 2](/assets/img/courses/ma0450/Arbol%202.svg)
Calculando las derivadas parciales de orden 1 (una ruta por sumando; note que $$z$$ llega a $$w$$ por tres rutas, una de ellas *directa* como tercera variable de $$f$$): 


$$
\begin{aligned}
\frac{ \partial w }{ \partial y } &= \frac{ \partial f }{ \partial v} \cdot \frac{ \partial h }{ \partial y }  \\
\frac{ \partial w }{ \partial x } &= \frac{ \partial f }{ \partial u } \cdot \frac{ \partial g }{ \partial x } +  \frac{ \partial f }{ \partial v } \cdot \frac{ \partial h }{ \partial r } \cdot \frac{ \partial g }{ \partial x } \\
\frac{ \partial w }{ \partial z } &= \frac{ \partial f }{ \partial u } \cdot \frac{ \partial g }{ \partial z }  + \frac{ \partial f }{ \partial v } \cdot \frac{ \partial h }{ \partial r } \cdot \frac{ \partial g }{ \partial z } + \frac{ \partial f }{ \partial z }.
\end{aligned}
$$



#### Ejemplo (derivada a lo largo de una curva)
El caso $$n = 1$$ es especialmente útil: si $$\gamma:\mathbb{R} \to \mathbb{R}^{m}$$ es derivable y $$f:\mathbb{R}^{m}\to \mathbb{R}$$ es diferenciable, entonces $$J_{\gamma}(t) = \gamma'(t)$$ (columna) y $$J_{f} = \nabla f^{T}$$ (fila), así que


$$
\frac{d}{dt} f(\gamma(t)) = J_{f}(\gamma(t)) \, J_{\gamma}(t) = \nabla f(\gamma(t)) \cdot \gamma'(t).
$$


Por ejemplo, si la temperatura en el plano es $$f(x,y) = x^{2}y$$ y una partícula sigue la trayectoria $$\gamma(t) = (\cos t, \sin t)$$, la temperatura que siente varía a razón de


$$
\frac{d}{dt}f(\gamma(t)) = (2\cos t \sin t, \cos^{2} t) \cdot (-\sin t, \cos t) = -2\cos t\sin^{2} t + \cos^{3} t,
$$


lo que en $$t = 0$$ da $$1$$; y en efecto $$f(\gamma(t)) = \cos^{2}t \sin t$$, cuya derivada en $$0$$ es $$1$$. Una consecuencia general: si $$\gamma$$ se mueve dentro de una curva de nivel de $$f$$ (es decir, $$f \circ \gamma$$ es constante), entonces $$\nabla f(\gamma(t)) \cdot \gamma'(t) = 0$$: el gradiente es normal a las curvas de nivel.

#### Ejemplo (la regla de la cadena necesita diferenciabilidad, no solo parciales)
Sea $$f(x,y) = \frac{x^{2}y}{x^{2}+y^{2}}$$ (con $$f(0,0) = 0$$), que vimos que tiene $$D_{1}f(0,0) = D_{2}f(0,0) = 0$$ pero no es diferenciable en el origen, y sea $$\gamma(t) = (t,t)$$. Entonces $$f(\gamma(t)) = \frac{t^{3}}{2t^{2}} = \frac{t}{2}$$, así que $$\frac{d}{dt}f(\gamma(t))\big\rvert_{t=0} = \frac{1}{2}$$. Pero la "fórmula" $$\nabla f(0,0) \cdot \gamma'(0) = (0,0)\cdot(1,1) = 0$$ da otra cosa. No hay contradicción: la regla de la cadena exige que $$f$$ sea diferenciable en $$\gamma(0)$$, y aquí no lo es. Tener parciales no basta.

## Desarrollos de Taylor
Generalización de Taylor en una variable (MA0350). Sea $$f \in C^{n+1}(V)$$, $$V$$ vecindario de $$a$$. Entonces, el desarrollo de Taylor de $$f$$ viene dado por: 


$$
f(x)  = f(a) + f'(a)(x-a) + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^{n} + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$


con $$\xi$$ entre $$x$$ y $$a$$. ¿Se puede generalizar esto a funciones de varias variables? 

### Teorema (Taylor)
Sea $$f:D \to \mathbb{R}$$, $$f \in C^{d+1}(D)$$, $$D \subseteq \mathbb{R}^n$$ abierto. Para $$a \in D$$, existe $$\delta>0$$ tal que para todo $$x \in B_{\delta}(a)$$ se tiene que 


$$
\begin{aligned}
f(x) &= f(a) + \sum_{j=1}^{n} D_{j} f(a) \cdot (x_{j}-a_{j}) + \frac{1}{2!} \sum_{j_{1}=1}^{n} \sum_{j_{2}=1}^{n} D_{j_{1},j_{2}} f(a) (x_{j_{1}} - a_{j_{1}})(x_{j_{2}} - a_{j_{2}}) \\
&+ \frac{1}{3!} \sum_{j_{1},j_{2},j_{3}=1}^{n} D_{j_{1},j_{2}, j_{3}} f(a) (x_{j_{1}} - a_{j_{1}})(x_{j_{2}} - a_{j_{2}})(x_{j_{3}} - a_{j_{3}}) + \dots \\
&+ \frac{1}{d!} \sum_{j_{1},\dots,j_{d} = 1}^{n} D_{{j_{1},\dots,j_{d}}}f(a)(x_{j_{1}}-a_{j_{1}})\dots(x_{j_{d}}-a_{j_{d}}) + \\
&+ \frac{1}{(d+1)!} \sum_{j_{1},\dots,j_{d+1} = 1}^{n} D_{{j_{1},\dots,j_{d},j_{d+1}}}f(\xi)(x_{j_{1}}-a_{j_{1}})\dots(x_{j_{d}}-a_{j_{d}})(x_{j_{d+1}}-a_{j_{d+1}}),
\end{aligned}
$$


con $$\xi$$ en el segmento que une $$a$$ y $$x$$.
#### Nota
Defina el Hessiano de $$f$$ en $$a$$ como la matriz de segundas derivadas, i.e., 


$$
H_{f}(a) = \begin{pmatrix}
D_{11}f(a) & D_{12}f(a) & \dots & D_{1n}f(a) \\
D_{21}f(a) & D_{22}f(a) & \dots & D_{2n}f(a) \\
\vdots & \vdots & \ddots & \vdots \\
D_{n1}f(a) & D_{n2}f(a) & \dots & D_{nn}f(a) 
\end{pmatrix}_{n \times n}.
$$


Esta matriz es simétrica si $$f \in C^{2}(D)$$ (teorema de Schwarz). El término de orden 2 del teorema de Taylor puede ser escrito convenientemente como 


$$
\frac{1}{2}(x-a)^{T} H_{f}(a) (x-a),
$$


y el de orden 1 como $$\nabla f(a)^{T}(x-a) = \nabla f(a) \cdot (x-a)$$.



***Prueba:*** Sea $$a \in D$$. Tome $$B_{\delta}(a) \subseteq D$$. Para $$x \in B_{\delta}(a)$$, defina $$g:[0,1] \to \mathbb{R}$$ con $$g(t) = f(\underbrace{ a+t(x-a) }_{ \in \mathbb{R}^n }) \in \mathbb{R}$$. Intuitivamente, esta función recorre el segmento entre $$a$$ y $$x$$, que está contenido en la bola (la bola es convexa).

![El segmento a + t(x - a) dentro de la bola, parametrizado por g](/assets/img/courses/ma0450/taylor-segmento.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[scale=1.6]
  \draw[dashed] (0,0) circle (1.9);
  \fill (0,0) circle (1.2pt) node[below left] {$a = g(0)$};
  \fill (1.4,0.8) circle (1.2pt) node[above right] {$x = g(1)$};
  \draw[orange, thick] (0,0) -- (1.4,0.8);
  \fill[orange] (0.7,0.4) circle (1.3pt) node[below right] {$a+t(x-a)$};
  \fill[orange] (0.98,0.56) circle (1.3pt) node[above left] {$\xi$};
  \node at (-1.2,-1.5) {$B_\delta(a)$};
  \draw[->] (-2.6,0) -- (-2.6,1.2) node[above] {$g(t) = f(a+t(x-a))$};
\end{tikzpicture}
-->

Por la regla de la cadena, $$g \in C^{d+1}[0,1]$$, luego aplica el teorema de Taylor en una variable con $$t=1$$ alrededor de $$t=0$$: existe $$\lambda \in (0,1)$$ tal que


$$
g(1) = g(0) + g'(0) + \frac{g''(0)}{2!}+\dots + \frac{g^{(d)}(0)}{d!} + \frac{g^{(d+1)}(\lambda)}{(d+1)!}.
$$


Note ahora que $$g(1) = f(x)$$ y $$g(0) = f(a)$$. Sea $$v(t) = a+t(x-a)$$, con componentes $$v_{i}(t) = a_{i}+t(x_{i} - a_{i})$$ y $$v_{i}'(t) = x_{i}-a_{i}$$. Desarrollando las derivadas con la regla de la cadena


$$
\begin{aligned}
g(t) &= f(v(t)) = f\big(a_{1}+t(x_{1}-a_{1}), \dots, a_{n}+t(x_{n}-a_{n})\big)\\
\implies g'(t) &= \sum_{j=1}^{n} D_{j}f(v(t)) \cdot v_{j}'(t) = \sum_{j=1}^{n} D_{j}f(a+t(x-a)) (x_{j}-a_{j}), \\
\implies g''(t) &= \sum_{j_{1}=1}^{n} \sum_{j_{2}=1}^{n} D_{j_{1}j_{2}}f(a+t(x-a)) (x_{j_{1}}-a_{j_{1}})(x_{j_{2}}-a_{j_{2}}),
\end{aligned}
$$


donde la segunda línea sale de derivar cada $$D_{j_{2}}f(v(t))$$ otra vez con la regla de la cadena. Inductivamente, $$g^{(k)}(t) = \sum_{j_{1},\dots,j_{k}=1}^{n} D_{j_{1}\dots j_{k}}f(a+t(x-a))\prod_{i=1}^{k}(x_{j_{i}}-a_{j_{i}})$$. Evaluando en $$t=0$$ se obtienen los términos del desarrollo, y para el resto $$\xi = a + \lambda(x-a)$$, que está en el segmento entre $$a$$ y $$x$$.

#### Ejemplo
Calculemos el desarrollo de Taylor de orden 3 de $$f(x,y) = e^{x}\sin y$$ alrededor de $$a = (0,0)$$. Las derivadas necesarias son


$$
\begin{aligned}
f &= e^{x}\sin y, & f_{x} &= e^{x}\sin y, & f_{y} &= e^{x}\cos y, \\
f_{xx} &= e^{x}\sin y, & f_{xy} &= e^{x}\cos y, & f_{yy} &= -e^{x}\sin y, \\
f_{xxx} &= e^{x}\sin y, & f_{xxy} &= e^{x}\cos y, & f_{xyy} &= -e^{x}\sin y, & f_{yyy} &= -e^{x}\cos y,
\end{aligned}
$$


que en $$(0,0)$$ valen $$f = 0$$, $$f_{x} = 0$$, $$f_{y} = 1$$, $$f_{xx} = 0$$, $$f_{xy} = 1$$, $$f_{yy} = 0$$, $$f_{xxx} = 0$$, $$f_{xxy} = 1$$, $$f_{xyy} = 0$$, $$f_{yyy} = -1$$. En la suma de orden $$k$$ del teorema cada derivada mixta aparece tantas veces como ordenamientos tenga su multiíndice: $$f_{xy}$$ aparece $$2$$ veces ($$xy$$, $$yx$$) y $$f_{xxy}$$ aparece $$3$$ veces ($$xxy$$, $$xyx$$, $$yxx$$). Así,


$$
\begin{aligned}
f(x,y) &= \underbrace{ 0 }_{ f(a) } + \underbrace{ 0\cdot x + 1 \cdot y }_{ \text{orden }1 } + \frac{1}{2!}\underbrace{ (0 \cdot x^{2} + 2 \cdot 1 \cdot xy + 0 \cdot y^{2}) }_{ \text{orden }2 } + \frac{1}{3!}\underbrace{ (0 \cdot x^{3} + 3\cdot 1 \cdot x^{2}y + 3 \cdot 0 \cdot xy^{2} + (-1) y^{3}) }_{ \text{orden }3 } + R_{3} \\
&= y + xy + \frac{x^{2}y}{2} - \frac{y^{3}}{6} + R_{3}(x,y),
\end{aligned}
$$


con $$R_{3}(x,y) = \frac{1}{4!}\sum_{j_{1},\dots,j_{4}=1}^{2} D_{j_{1}j_{2}j_{3}j_{4}}f(\xi)\, x_{j_{1}}x_{j_{2}}x_{j_{3}}x_{j_{4}}$$ para algún $$\xi$$ en el segmento de $$(0,0)$$ a $$(x,y)$$. Como todas las derivadas de orden 4 son de la forma $$\pm e^{\xi_{1}}\sin\xi_{2}$$ o $$\pm e^{\xi_{1}}\cos\xi_{2}$$ y $$\lvert \xi_{1} \rvert \leq \lvert x \rvert$$, se tiene $$\lvert R_{3}(x,y) \rvert \leq \frac{e^{\lvert x \rvert}}{24}(\lvert x \rvert + \lvert y \rvert)^{4}$$. Comprobación: multiplicando las series $$e^{x} = 1 + x + \frac{x^{2}}{2} + \dots$$ y $$\sin y = y - \frac{y^{3}}{6} + \dots$$ se obtiene $$y + xy + \frac{x^{2}y}{2} - \frac{y^{3}}{6} + \dots$$, que coincide.

## Máximos y mínimos
Recordemos:
1. Si $$c \in D^{0}$$ es extremo relativo, $$\nabla f(c) = 0$$.
2. $$f:K \subseteq \mathbb{R}^n \to \mathbb{R}$$, $$K$$ compacto. $$f$$ tiene máximo y mínimo absolutos.

### Definición (Punto crítico)
Dada $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, decimos que $$c$$ es un punto crítico si $$f$$ no es diferenciable en $$c$$ o si $$\nabla f(c) = 0$$. 
#### Nota
Recuerde que ser un punto crítico no implica ser extremo relativo. Por ejemplo, $$f:\mathbb{R} \to \mathbb{R}$$ con $$f(x)=x^{3}$$ tiene un punto crítico en $$0$$ pero no es extremo relativo. También, $$f:\mathbb{R}^{2} \to \mathbb{R}$$ con $$f(x,y) = x^{2}-y^{2}$$.  Se puede verificar que $$\nabla f(0,0) = 0$$ pero $$(0,0)$$ es un punto silla. Tenemos que $$f(x,0) =x^{2}\geq 0 = f(0,0)$$ y $$f(0,y) = -y^{2} \leq 0 = f(0,0)$$.

### Definición (Máximos, mínimos y puntos silla)
Dada $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}$$, con $$A$$ abierto y $$x_{0} \in A$$:
1. $$f(x_{0})$$ es máximo (resp. mínimo) local en $$A$$ si existe $$\rho>0$$ tal que $$f(x) \leq f(x_{0})$$ (resp. $$f(x_{0}) \leq f(x)$$) para todo $$x \in B_{\rho}(x_{0})$$.
2. El extremo es global (o absoluto) si la desigualdad se cumple para todo $$x \in A$$.
3. $$x_{0}$$ es punto silla si $$\nabla f(x_{0}) = 0$$ y para todo $$r>0$$ con $$B_{r}(x_{0}) \subseteq A$$ existen $$x_{1}, x_{2} \in B_{r}(x_{0})$$ tales que $$f(x_{1}) < f(x_{0}) < f(x_{2})$$.

### Definición (Matrices def. y semidef. positiva y negativa)
Sea $$A \in \mathbb{R}^{n \times n}$$ una matriz simétrica. Decimos que $$A$$ es:
1. definida positiva si para todo $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax > 0$$;
2. semidefinida positiva si para todo $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax \geq 0$$;
3. definida negativa si para todo $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax < 0$$;
4. semidefinida negativa si para todo $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax \leq 0$$;
5. indefinida si existen $$0 \neq x_{1},x_{2} \in \mathbb{R}^n$$ tales que $$x_{1}^{T}Ax_{1}>0$$ y $$x_{2}^{T} A x_{2} < 0$$.

### Teorema (Criterio del Hessiano)
Dada $$f:D \subseteq \mathbb{R}^n\to \mathbb{R}$$, $$f \in C^{2}(D)$$, defina la matriz hessiana como 


$$
H_{f} = \begin{bmatrix}
D_{11}f & \dots &  D_{1n}f  \\
\vdots & \ddots & \vdots \\
D_{n1}f & \dots & D_{nn}f
\end{bmatrix}.
$$


Si $$\nabla f(c) = 0$$ ($$c$$ es punto crítico), entonces
1. hay mínimo relativo en $$c$$ si $$H_{f}(c)$$ es definida positiva;
2. hay máximo relativo en $$c$$ si $$H_{f}(c)$$ es definida negativa;
3. hay punto silla relativo en $$c$$ si $$H_{f}(c)$$ es indefinida;
4. en otro caso, el criterio no decide.

***Prueba:*** Probamos el caso 1; el caso 2 se obtiene aplicándolo a $$-f$$. Sea $$B_{\delta}(c) \subseteq D$$. Por el teorema de Taylor con $$d=1$$ y $$\nabla f(c) = 0$$, para cada $$x \in B_{\delta}(c)$$ existe $$\xi$$ en el segmento entre $$c$$ y $$x$$ tal que


$$
\begin{aligned}
f(x) &= f(c) + \nabla f(c) \cdot (x-c) + \frac{1}{2} (x-c)^{T} H_{f}(\xi) (x-c)\\
\implies f(x) - f(c) &= \frac{1}{2} (x-c)^{T} H_{f}(\xi) (x-c).
\end{aligned}
$$


El problema es que $$H_{f}$$ está evaluada en $$\xi$$, no en $$c$$; la continuidad de las segundas derivadas es lo que permite pasar de una a otra. Como $$H_{f}(c)$$ es definida positiva y la esfera unitaria $$S = \{ u \in \mathbb{R}^n : \lVert u \rVert = 1 \}$$ es compacta, la función continua $$u \mapsto u^{T}H_{f}(c)u$$ alcanza en $$S$$ un mínimo $$m > 0$$. Por continuidad de las $$D_{ij}f$$ en $$c$$, existe $$0<\alpha\leq\delta$$ tal que $$\lvert D_{ij}f(\xi) - D_{ij}f(c) \rvert < \frac{m}{2n^{2}}$$ para todo $$i,j$$ si $$\lVert \xi - c \rVert < \alpha$$. Entonces, para $$u \in S$$ y tal $$\xi$$,


$$
\lvert u^{T} H_{f}(\xi) u - u^{T} H_{f}(c) u \rvert \leq \sum_{i,j=1}^{n} \lvert D_{ij}f(\xi) - D_{ij}f(c) \rvert \, \lvert u_{i} \rvert \lvert u_{j} \rvert < n^{2} \cdot \frac{m}{2n^{2}} = \frac{m}{2},
$$


de modo que $$u^{T}H_{f}(\xi)u > m - \frac{m}{2} = \frac{m}{2} > 0$$. Si $$0<\lVert x-c \rVert < \alpha$$, entonces $$\xi \in B_{\alpha}(c)$$ y, escribiendo $$x - c = \lVert x-c \rVert u$$ con $$u \in S$$,


$$
f(x) - f(c) = \frac{\lVert x-c \rVert^{2}}{2} \, u^{T} H_{f}(\xi) u > \frac{m}{4}\lVert x-c \rVert^{2} > 0.
$$


Concluimos que $$f(c)$$ es un mínimo relativo (estricto). Para el caso 3, si $$H_{f}(c)$$ es indefinida, tome $$u_{1},u_{2} \in S$$ con $$u_{1}^{T}H_{f}(c)u_{1} > 0 > u_{2}^{T}H_{f}(c)u_{2}$$; el mismo argumento de continuidad, aplicado a lo largo de cada dirección, muestra que $$f(c+tu_{1}) > f(c)$$ y $$f(c+tu_{2}) < f(c)$$ para $$t>0$$ pequeño, así que $$c$$ es punto silla.

![Curvas de nivel cerca de un punto crítico: mínimo, silla y caso degenerado](/assets/img/courses/ma0450/hessiano-curvas-de-nivel.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[scale=0.9]
  % definida positiva: elipses
  \begin{scope}
    \foreach \r in {0.4,0.8,1.2} \draw (0,0) ellipse ({1.3*\r} and {0.8*\r});
    \fill[orange] (0,0) circle (1.5pt);
    \node at (0,-1.6) {$H_f(c)$ def. positiva: mínimo};
  \end{scope}
  % indefinida: hipérbolas
  \begin{scope}[xshift=4.2cm]
    \foreach \k in {0.3,0.7,1.1} {
      \draw[domain=-1.3:1.3, samples=40] plot (\x, {sqrt(\x*\x + \k*\k)*0.9 - 0.9*\k + \k*0.9}) ;
      \draw[domain=-1.3:1.3, samples=40] plot (\x, {-(sqrt(\x*\x + \k*\k)*0.9 - 0.9*\k + \k*0.9)}) ;
    }
    \fill[orange] (0,0) circle (1.5pt);
    \node at (0,-1.6) {$H_f(c)$ indefinida: silla};
  \end{scope}
  % degenerada: rectas paralelas (f = y^2)
  \begin{scope}[xshift=8.4cm]
    \foreach \y in {-1.1,-0.7,-0.35,0.35,0.7,1.1} \draw (-1.3,\y) -- (1.3,\y);
    \fill[orange] (0,0) circle (1.5pt);
    \node at (0,-1.6) {semidefinida: no decide};
  \end{scope}
\end{tikzpicture}
-->

### Teorema (Caracterización de matrices def. y semidef. positivas y negativas)
Sea $$A$$ simétrica. Las siguientes son equivalentes:
1. $$A$$ es definida positiva (resp. negativa);
2. los valores propios de $$A$$ son todos positivos (resp. negativos);
3. los determinantes de los menores principales *dominantes* $$\Delta_{k} = \det(A_{1..k,1..k})$$, $$k=1,\dots,n$$, son todos positivos (resp. alternan en signo empezando en negativo: $$(-1)^{k}\Delta_{k} > 0$$).

Además, las siguientes son equivalentes:
4. $$A$$ es indefinida;
5. $$A$$ tiene valores propios negativos y positivos.

Para $$n=2$$ el criterio es especialmente cómodo: con $$\Delta_{2} = \det A$$, si $$\Delta_{2}<0$$ la matriz es indefinida (los valores propios tienen signos opuestos, pues su producto es $$\det A$$); si $$\Delta_{2}>0$$ es definida, con el signo de $$\Delta_{1} = a_{11}$$; y si $$\Delta_{2} = 0$$ es semidefinida y el criterio del hessiano no decide. Cuidado: el criterio (3) **no** se extiende a las semidefinidas cambiando $$>$$ por $$\geq$$ (por ejemplo $$\begin{bmatrix} 0 & 0 \\ 0 & -1 \end{bmatrix}$$ tiene $$\Delta_{1} = \Delta_{2} = 0$$ y no es semidefinida positiva); para ellas hay que revisar *todos* los menores principales, o usar los valores propios.
 
#### Ejemplo 
Considere $$f(x,y) = x^{3}-3xy^{2}+y^{2}$$. Primero, encontramos los puntos críticos.

Note que $$\nabla f(x,y) = (3x^{2}-3y^{2}, -6xy+2y) = (0,0)$$


$$
\implies \begin{cases}
x ^{2} = y^{2}  \\
-3xy+y=0
\end{cases}.
$$


Tenemos $$(0,0), \left( \frac{1}{3}, \frac{1}{3} \right), \left( \frac{1}{3}, -\frac{1}{3} \right)$$ como puntos críticos. El hessiano de $$f$$ es 


$$
H_{f}(x,y) = \begin{bmatrix}
6x & -6y \\
-6y & -6x+2
\end{bmatrix}.
$$


Finalmente, calculamos los determinantes de los menores para cada caso: 


$$
\begin{aligned}
H_{f}\left( \frac{1}{3}, \frac{1}{3} \right) &= \begin{bmatrix}
2 & -2 \\
-2 & 0
\end{bmatrix} \implies \Delta_{1} = 2 > 0, \ \Delta_{2} = -4 < 0  \quad \text{(indefinida)}, \\
H_{f}\left( \frac{1}{3}, \frac{-1}{3} \right) &= \begin{bmatrix}
2 & 2 \\
2 & 0
\end{bmatrix} \implies \Delta_{1} = 2 > 0, \ \Delta_{2} = -4 <0  \quad \text{(indefinida)}.
\end{aligned}
$$


Así, ambos puntos son puntos silla. Para el punto $$(0,0)$$ tenemos $$H_{f}(0,0) = \begin{bmatrix} 0 & 0 \\ 0 & 2 \end{bmatrix}$$, así que $$\Delta_{1} = \Delta_{2} = 0$$ y $$(x,y)H_{f}(0,0) (x,y)^{T} = 2y^{2} \geq 0$$: la matriz es semidefinida positiva pero no definida positiva, y el criterio **no decide**. Es tentador concluir que hay un mínimo, pero es falso: sobre el eje $$x$$, $$f(x,0) = x^{3}$$, que es positivo para $$x>0$$ y negativo para $$x<0$$, mientras que $$f(0,0) = 0$$. Toda bola alrededor de $$(0,0)$$ contiene puntos con $$f>0$$ y puntos con $$f<0$$, así que $$(0,0)$$ es un punto silla, no un extremo. Moraleja: semidefinida no basta; cuando el criterio no decide, hay que mirar la función directamente.

#### Ejemplo (cuando el criterio no decide, todo puede pasar)
Las funciones $$f_{1}(x,y) = x^{4}+y^{4}$$, $$f_{2}(x,y) = x^{4}-y^{4}$$ y $$f_{3}(x,y) = x^{3}+y^{2}$$ tienen todas a $$(0,0)$$ como punto crítico; la hessiana ahí es la matriz nula para las dos primeras y $$\begin{bmatrix} 0 & 0 \\ 0 & 2 \end{bmatrix}$$ (semidefinida positiva) para la tercera, así que el criterio no decide en ninguno de los tres casos. Sin embargo, $$(0,0)$$ es un mínimo estricto de $$f_{1}$$, un punto silla de $$f_{2}$$ (pues $$f_{2}(x,0) = x^{4} > 0 > -y^{4} = f_{2}(0,y)$$) y un punto silla de $$f_{3}$$ (pues $$f_{3}(x,0) = x^{3}$$ cambia de signo). En estos casos hay que analizar $$f$$ directamente, típicamente restringiéndola a rectas o curvas que pasen por el punto crítico.

#### Ejemplo (tres variables)
Sea $$f(x,y,z) = x^{2}+y^{2}+z^{2}-xy-yz$$. Entonces $$\nabla f = (2x - y,\ 2y - x - z,\ 2z - y)$$, que se anula solo en el origen (el sistema es lineal y su matriz tiene determinante $$4 \neq 0$$), y


$$
H_{f} = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}, \qquad \Delta_{1} = 2, \quad \Delta_{2} = \det\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} = 3, \quad \Delta_{3} = \det H_{f} = 4.
$$


Todos positivos, así que $$H_{f}$$ es definida positiva y $$(0,0,0)$$ es un mínimo relativo; de hecho es absoluto, pues $$f(x) = \frac{1}{2}x^{T}H_{f}x > 0 = f(0)$$ para todo $$x \neq 0$$.

#### Ejemplo (extremos absolutos en un compacto)
Sea $$f(x,y) = x^{2}+2y^{2}-x$$ sobre el disco cerrado $$K = \{ (x,y) : x^{2}+y^{2} \leq 1 \}$$. Como $$K$$ es compacto y $$f$$ es continua, existen máximo y mínimo absolutos, y cada uno se alcanza o bien en un punto crítico del interior o bien en la frontera.

*Interior:* $$\nabla f = (2x-1, 4y) = (0,0) \iff (x,y) = \left( \frac{1}{2},0 \right)$$, que está en el interior de $$K$$, con $$f\left( \frac{1}{2},0 \right) = -\frac{1}{4}$$.

*Frontera:* parametrizamos $$x^{2}+y^{2} = 1$$ con $$(\cos t, \sin t)$$ y estudiamos $$\varphi(t) = f(\cos t,\sin t) = \cos^{2}t + 2\sin^{2}t - \cos t = 2 - \cos^{2}t - \cos t$$. Con $$c = \cos t \in [-1,1]$$, la función $$2 - c^{2} - c$$ tiene derivada $$-2c-1$$, que se anula en $$c = -\frac{1}{2}$$, donde vale $$\frac{9}{4}$$; en los extremos, $$c = 1$$ da $$0$$ y $$c = -1$$ da $$2$$.

*Comparando:* el mínimo absoluto es $$-\frac{1}{4}$$, en $$\left( \frac{1}{2},0 \right)$$, y el máximo absoluto es $$\frac{9}{4}$$, alcanzado en los dos puntos de la frontera con $$\cos t = -\frac{1}{2}$$: $$\left( -\frac{1}{2}, \pm\frac{\sqrt{ 3 }}{2} \right)$$. Note que en la frontera no se usa $$\nabla f$$ (esos puntos no son críticos de $$f$$): el problema en la frontera es un problema de una variable.

## Diferenciación de inversas y función implícita

#### Ejemplo 
Si $$f:\mathbb{R}\to \mathbb{R}$$ es invertible y derivable, con inversa $$g=f^{-1}$$ derivable, sabemos que $$g(f(x))= x$$. Por regla de la cadena, $$g'(f(x)) f'(x) = 1$$ y así $$g'(y)=\frac{1}{f'(f^{-1}(y))}$$, donde $$y = f(x)$$ y $$f'(x) \neq 0$$. Note que el argumento *supone* que $$g$$ es derivable; el teorema de la función inversa es justamente lo que garantiza eso (y la existencia local de $$g$$) a partir de $$f'(x) \neq 0$$.

#### Ejemplo 
Para calcular $$g'$$ para $$g(x)=\arcsin x \in \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$$. Sabemos que $$\sin(g(x)) = x$$ y entonces $$\cos(g(x)) g'(x) = 1$$. Así 


$$
g'(x) = \frac{1}{\cos(g(x))} = \frac{1}{\sqrt{ 1 - \sin^{2}(g(x)) }} = \frac{1}{\sqrt{ 1-x^{2} }}.
$$


Basta saber que $$(\sin x)' = \cos x \neq 0$$ para todo $$x \in (-\frac{\pi}{2}, \frac{\pi}{2})$$ para saber que $$\sin$$ es localmente invertible ahí, con inversa derivable (para $$x = \pm 1$$, extremos del dominio de $$\arcsin$$, la derivada explota: $$\cos(\pm\frac{\pi}{2}) = 0$$).

### Teorema (Función inversa)
Sea $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}^n$$,  $$f \in C^{1}(A)$$ con $$A$$ abierto. Sea $$a \in A$$ con $$\det J_{f}(a) \neq 0$$. Entonces:
1. existen $$V,W  \subseteq\mathbb{R}^n$$ abiertos tales que $$a \in V$$, $$f(a) \in W$$ y $$f:V\to W$$ es biyectiva, con $$f^{-1}:W\to V$$ de clase $$C^{1}$$;
2. $$J_{f^{-1}}(y)= [J_{f}(f^{-1}(y))]^{-1}$$ para todo $$y \in W$$.

![El teorema de la función inversa: f restringida a V es una biyección sobre W](/assets/img/courses/ma0450/funcion-inversa-vecindarios.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[>=stealth]
  \draw[thick, rounded corners=12pt] (-3.4,-1.6) rectangle (-0.4,1.6);
  \node at (-2.9,1.3) {$A$};
  \draw[orange, thick] (-1.9,0) ellipse (0.9 and 0.7);
  \node[orange] at (-1.9,-1.05) {$V$};
  \fill (-1.9,0) circle (1.3pt) node[above] {$a$};
  \draw[thick, rounded corners=12pt] (0.4,-1.6) rectangle (3.4,1.6);
  \node at (2.9,1.3) {$\mathbb{R}^n$};
  \draw[orange, thick, rotate around={20:(1.9,0)}] (1.9,0) ellipse (1.0 and 0.6);
  \node[orange] at (1.9,-1.05) {$W = f(V)$};
  \fill (1.9,0) circle (1.3pt) node[above] {$f(a)$};
  \draw[->, thick, bend left=25] (-1.2,0.5) to node[above] {$f$ (biyectiva)} (1.2,0.5);
  \draw[->, thick, bend left=25] (1.2,-0.5) to node[below] {$f^{-1}$, $J_{f^{-1}} = J_f^{-1}$} (-1.2,-0.5);
\end{tikzpicture}
-->

***Idea de la prueba:*** (En clase se remitió a un video complementario; esta es la estructura del argumento.)
1. *Fórmula para la derivada.* Si ya sabemos que $$f^{-1}$$ existe en $$W$$ y es diferenciable, la regla de la cadena aplicada a $$f^{-1} \circ f = \mathrm{id}_{V}$$ da $$J_{f^{-1}}(f(x)) \cdot J_{f}(x) = I$$, que es (2). Lo difícil es (1) y la diferenciabilidad de la inversa.
2. *Reducción.* Componiendo con la transformación lineal invertible $$J_{f}(a)^{-1}$$ (que no afecta ninguna conclusión), se puede suponer $$J_{f}(a) = I$$. Por continuidad de las parciales, existe una bola cerrada $$\bar B = \bar B_{r}(a)$$ en la que $$\lVert J_{f}(x) - I \rVert < \frac{1}{2}$$ y $$\det J_{f}(x) \neq 0$$.
3. *Inyectividad.* Sea $$\varphi(x) = x - f(x)$$, de modo que $$J_{\varphi} = I - J_{f}$$ tiene norma menor que $$\frac{1}{2}$$ en $$\bar B$$. Por el teorema del valor medio aplicado a cada componente, $$\lVert \varphi(x) - \varphi(x') \rVert \leq \frac{1}{2}\lVert x-x' \rVert$$ para $$x,x' \in \bar B$$, y entonces


$$
\lVert f(x) - f(x') \rVert \geq \lVert x-x' \rVert - \lVert \varphi(x)-\varphi(x') \rVert \geq \tfrac{1}{2}\lVert x-x' \rVert.
$$


   Así $$f$$ es inyectiva en $$\bar B$$ y su inversa (donde exista) es Lipschitz, en particular continua.
4. *La imagen es abierta.* Sea $$V = B_{r}(a)$$ y $$W = f(V)$$. Dado $$y_{0} = f(x_{0})$$ con $$x_{0} \in V$$, tome $$\rho>0$$ con $$\bar B_{\rho}(x_{0}) \subseteq V$$ y sea $$y$$ con $$\lVert y - y_{0} \rVert < \frac{\rho}{4}$$. La función $$x \mapsto \lVert f(x) - y \rVert^{2}$$ es continua en el compacto $$\bar B_{\rho}(x_{0})$$ y alcanza su mínimo. Sobre la esfera $$\lVert x - x_{0} \rVert = \rho$$, por el paso 3, $$\lVert f(x) - y \rVert \geq \lVert f(x) - y_{0} \rVert - \lVert y - y_{0} \rVert \geq \frac{\rho}{2} - \frac{\rho}{4} > \lVert f(x_{0}) - y \rVert$$, así que el mínimo no está en la frontera. En un mínimo interior el gradiente se anula: $$2 J_{f}(x)^{T}(f(x)-y) = 0$$, y como $$J_{f}(x)$$ es invertible, $$f(x) = y$$. Luego $$B_{\rho/4}(y_{0}) \subseteq W$$: $$W$$ es abierto, y $$f:V \to W$$ es biyectiva por el paso 3.
5. *Diferenciabilidad de la inversa.* Sea $$y = f(x)$$, $$y+k = f(x+h)$$ con $$T = J_{f}(x)$$. Entonces $$k = T h + r(h)$$ con $$\lVert r(h) \rVert / \lVert h \rVert \to 0$$, y


$$
f^{-1}(y+k) - f^{-1}(y) - T^{-1}k = h - T^{-1}(Th + r(h)) = -T^{-1} r(h).
$$


   Como $$\lVert h \rVert \leq 2\lVert k \rVert$$ por el paso 3, $$\frac{\lVert T^{-1}r(h) \rVert}{\lVert k \rVert} \leq 2\lVert T^{-1} \rVert \frac{\lVert r(h) \rVert}{\lVert h \rVert} \to 0$$ cuando $$k \to 0$$ (lo que fuerza $$h \to 0$$). Por tanto $$f^{-1}$$ es diferenciable en $$y$$ con $$D_{f^{-1}}(y) = J_{f}(x)^{-1}$$, y como $$y \mapsto J_{f}(f^{-1}(y))^{-1}$$ es continua (entradas de la inversa son cocientes de polinomios en las entradas, con denominador el determinante), $$f^{-1} \in C^{1}(W)$$.

#### Nota
1. El teorema es *local*: $$f$$ puede no ser inyectiva globalmente aunque $$\det J_{f} \neq 0$$ en todas partes (ver el segundo ejemplo).
2. La condición $$\det J_{f}(a) \neq 0$$ es suficiente pero no necesaria para que exista una inversa: $$f(x) = x^{3}$$ es una biyección de $$\mathbb{R}$$ con $$f'(0) = 0$$; lo que se pierde es la *diferenciabilidad* de la inversa en $$0$$ ($$\sqrt[3]{y}$$ no es derivable en $$0$$).
3. Si $$f \in C^{k}$$, entonces $$f^{-1} \in C^{k}$$ (se itera el argumento de continuidad del paso 5).

#### Ejemplo (coordenadas polares)
Sea $$f(r,\theta) = (r\cos\theta, r\sin\theta)$$, de clase $$C^{\infty}$$ en $$\mathbb{R}^{2}$$. Entonces


$$
J_{f}(r,\theta) = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix}, \qquad \det J_{f}(r,\theta) = r\cos^{2}\theta + r\sin^{2}\theta = r.
$$


Así, en todo punto con $$r \neq 0$$ el teorema da una inversa local $$C^{1}$$ (una determinación local de $$(x,y) \mapsto (\sqrt{x^{2}+y^{2}}, \theta)$$), con


$$
J_{f^{-1}}(x,y) = [J_{f}(r,\theta)]^{-1} = \frac{1}{r}\begin{bmatrix} r\cos\theta & r\sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} = \begin{bmatrix} \frac{x}{\sqrt{ x^{2}+y^{2} }} & \frac{y}{\sqrt{ x^{2}+y^{2} }} \\ -\frac{y}{x^{2}+y^{2}} & \frac{x}{x^{2}+y^{2}} \end{bmatrix},
$$


lo cual coincide con derivar directamente $$r = \sqrt{x^{2}+y^{2}}$$ y $$\theta = \arctan(y/x)$$. En $$r = 0$$ el teorema no aplica, y en efecto $$f$$ no es inyectiva en ningún vecindario del eje $$r=0$$ (todo $$(0,\theta)$$ va a dar al origen).

#### Ejemplo (local pero no global)
Sea $$f(x,y) = (e^{x}\cos y, e^{x}\sin y)$$. Entonces


$$
J_{f}(x,y) = \begin{bmatrix} e^{x}\cos y & -e^{x}\sin y \\ e^{x}\sin y & e^{x}\cos y \end{bmatrix}, \qquad \det J_{f}(x,y) = e^{2x} > 0
$$


en todo $$\mathbb{R}^{2}$$, así que $$f$$ es localmente invertible en *todo* punto. Sin embargo, $$f(x,y+2\pi) = f(x,y)$$: $$f$$ no es inyectiva en $$\mathbb{R}^{2}$$ y no tiene inversa global. (Es la exponencial compleja $$z \mapsto e^{z}$$ vista en $$\mathbb{R}^{2}$$; las inversas locales son las ramas del logaritmo.)

#### Ejemplo (cálculo de una derivada de la inversa sin conocer la inversa)
Sea $$f(x,y) = (x+y, xy)$$ y $$a = (2,1)$$, con $$f(a) = (3,2)$$. Como $$J_{f}(x,y) = \begin{bmatrix} 1 & 1 \\ y & x \end{bmatrix}$$ y $$\det J_{f}(2,1) = 2-1 = 1 \neq 0$$, existe una inversa local $$g = f^{-1}$$ cerca de $$(3,2)$$ con $$g(3,2) = (2,1)$$, y


$$
J_{g}(3,2) = [J_{f}(2,1)]^{-1} = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}^{-1} = \begin{bmatrix} 2 & -1 \\ -1 & 1 \end{bmatrix}.
$$


Esto dice, por ejemplo, que si la suma $$s = x+y$$ sube en $$\Delta s$$ y el producto $$p = xy$$ queda fijo, entonces $$x$$ sube aproximadamente $$2\Delta s$$ y $$y$$ baja aproximadamente $$\Delta s$$. Note que sobre la recta $$x = y$$ el determinante se anula: ahí $$f$$ no es localmente inyectiva, pues $$f(x,y) = f(y,x)$$ y los puntos $$(x,y)$$ y $$(y,x)$$ se acercan al acercarse a la diagonal.

### Teorema (Función implícita)
Sea $$f:\mathbb{R}^n \times \mathbb{R}^{m} \to \mathbb{R}^{m}$$ de clase $$C^{1}$$ en un abierto que contiene a $$(a,b)$$, con $$a \in \mathbb{R}^n$$, $$b \in \mathbb{R}^{m}$$, $$f(a,b)=0$$. Sea $$M \in \mathbb{R}^{m \times m}$$ con $$M_{ij} = D_{n+j}f_{i}$$, $$1\leq i,j\leq m$$. Si $$\det M(a,b) \neq 0$$, existen $$A \subseteq \mathbb{R}^n$$, $$B \subseteq \mathbb{R}^{m}$$ con $$a \in A$$, $$b \in B$$ tales que 


$$
\forall x \in A  \quad \exists ! y \in B  \quad (f(x,y)=0).
$$


Esto es, existe una única $$g :A\to B$$ con $$f(x, g(x)) = 0$$ para todo $$x \in A$$ (y $$g(a) = b$$). Además, $$g$$ es de clase $$C^{1}$$ en $$A$$ y $$J_{g}(x) = -[M(x,g(x))]^{-1} N(x,g(x))$$, donde $$N = [D_{j}f_{i}]_{1\leq i\leq m, \hspace{1mm} 1\leq j\leq n}$$ es el bloque de $$J_{f}$$ correspondiente a las variables $$x$$.

***Idea de la prueba:*** 
Podemos escribir el jacobiano de $$f$$ como


$$
\begin{aligned}
J_{f} &= \begin{bmatrix} N & M \\
\end{bmatrix}_{m \times (n+m)}, \\ \\
\text{con }N &= \begin{bmatrix} 
D_{1}f_{1} & \dots & D_{n}f_{1} \\
\vdots & \ddots & \vdots \\ 
D_{1}f_{m} & \dots & D_{n}f_{m} \\
\end{bmatrix}_{m \times n} \text{y }
M = \begin{bmatrix} 
D_{n+1}f_{1}  & \dots & D_{n+m} f_{1} \\ 
\vdots & \ddots & \vdots \\
D_{n+1}f_{m} & \dots & D_{n+m}f_{m}
\end{bmatrix}_{m \times m}.
\end{aligned}
$$


Sea $$h:\mathbb{R}^n \to \mathbb{R}^{n+m}$$ con $$h(x) = (x,g(x))$$, tenemos que $$J_{h} = \begin{bmatrix}I_{n\times n} \\ J_{g}\end{bmatrix}$$. Como $$f \circ h = 0$$,  tenemos que 


$$
0 = \begin{bmatrix}
N & M
\end{bmatrix} \begin{bmatrix}
I \\
J_{g}
\end{bmatrix} = N+MJ_{g} \implies J_{g} = -M^{-1}N.
$$


#### Ejemplo 
Considere la circunferencia $$x^{2}+y^{2} = 1$$, es decir, el conjunto de ceros de $$f(x,y) = x^{2}+y^{2}-1$$. Aquí $$n = m = 1$$ y $$M = \frac{ \partial f }{ \partial y } = 2y$$, que es distinto de cero salvo en $$(-1,0)$$ y $$(1,0)$$. Alrededor de cualquier otro punto $$(a,b)$$ de la circunferencia, el teorema garantiza un intervalo $$A$$ alrededor de $$a$$ y una única función $$y = g(x)$$ con $$g(a) = b$$ y $$x^{2}+g(x)^{2} = 1$$; concretamente $$g(x) = \sqrt{ 1-x^{2} }$$ si $$b>0$$ y $$g(x) = -\sqrt{ 1-x^{2} }$$ si $$b<0$$. En $$(\pm 1, 0)$$ no hay tal función: todo intervalo alrededor de $$x = 1$$ contiene puntos $$x>1$$ sin preimagen y puntos $$x<1$$ con dos ($$\pm\sqrt{ 1-x^{2} }$$); geométricamente, la tangente es vertical. Derivando implícitamente respecto a $$x$$, pensando $$y = y(x)$$: $$2x + 2y\,y' = 0$$, luego $$y' = -\frac{x}{y} = -\frac{f_{x}}{f_{y}}$$, que es la fórmula del teorema.

![La circunferencia como gráfico local y = g(x), salvo en los puntos de tangente vertical](/assets/img/courses/ma0450/funcion-implicita-circulo.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[scale=1.7]
  \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
  \draw[->] (0,-1.4) -- (0,1.4) node[above] {$y$};
  \draw[thick] (0,0) circle (1);
  % ventana A x B alrededor de (a,b)
  \draw[orange, dashed] (0.2,0.55) rectangle (0.9,1.15);
  \draw[orange, very thick, domain=0.2:0.9, samples=40] plot (\x, {sqrt(1-\x*\x)});
  \fill[orange] (0.6,0.8) circle (1.3pt) node[above right] {$(a,b)$};
  \draw[orange, thick] (0.2,-0.08) -- (0.9,-0.08) node[midway, below] {$A$};
  \draw[orange, thick] (-0.08,0.55) -- (-0.08,1.15) node[midway, left] {$B$};
  \node[orange] at (1.35,1.0) {$y=g(x)$};
  % puntos malos
  \fill (1,0) circle (1.3pt) node[below right] {$(1,0)$};
  \fill (-1,0) circle (1.3pt) node[below left] {$(-1,0)$};
  \draw[dashed] (1,-0.5) -- (1,0.5);
  \draw[dashed] (-1,-0.5) -- (-1,0.5);
  \node at (0,-1.7) {$f_y = 2y = 0$ en $(\pm1,0)$: tangente vertical, no hay $g$};
\end{tikzpicture}
-->

#### Caso particular 
Para $$n=m=1$$,  tenemos $$f:\mathbb{R} \times \mathbb{R} \to \mathbb{R}$$, entonces $$N = \frac{ \partial f }{ \partial x }$$ y $$M = \frac{ \partial f }{ \partial y }$$. Si $$\det\left( \frac{ \partial f }{ \partial y } \right) \neq 0$$, $$\frac{dy}{dx} = -\frac{\frac{ \partial f }{ \partial x }}{\frac{ \partial f }{ \partial y }}$$.

#### Ejemplo
Considere $$f(x,y) = \ln x+2\ln y+xy-1$$ en $$x,y>0$$ y $$(a,b)=(1,1)$$. Note que $$f(1,1) = 0 + 0 + 1 - 1 = 0$$ y que $$M = \frac{ \partial f }{ \partial y } = \frac{2}{y} + x \implies M(1,1) = 3 \neq 0$$.  Por el teorema de la función implícita, existen $$A,B$$ subconjuntos abiertos de $$\mathbb{R}$$, con $$1 \in A$$, $$1 \in B$$, y una única $$g:A \to B$$ de clase $$C^{1}$$ con $$g(1) = 1$$ y $$f(x,g(x)) = 0$$. Aunque no podemos despejar $$g$$ explícitamente, sí podemos derivarla:


$$
g'(1) = -\frac{f_{x}(1,1)}{f_{y}(1,1)} = -\frac{\frac{1}{x}+y}{\frac{2}{y}+x}\Bigg\rvert_{(1,1)} = -\frac{2}{3}.
$$


Así, cerca de $$x = 1$$, $$g(x) \approx 1 - \frac{2}{3}(x-1)$$.

#### Ejemplo (una superficie como gráfico local)
Sea $$F(x,y,z) = xz + yz^{2} + z^{3} - 1$$ y $$(a,b) = ((0,0), 1)$$, con $$n = 2$$, $$m = 1$$. Se tiene $$F(0,0,1) = 0$$ y $$M = F_{z} = x + 2yz + 3z^{2}$$, con $$M(0,0,1) = 3 \neq 0$$. Luego cerca de $$(0,0)$$ la superficie $$F = 0$$ es el gráfico de una función $$z = g(x,y)$$ de clase $$C^{1}$$ con $$g(0,0) = 1$$, y


$$
J_{g}(0,0) = -M^{-1}N = -\frac{1}{F_{z}}\begin{bmatrix} F_{x} & F_{y} \end{bmatrix}\Bigg\rvert_{(0,0,1)} = -\frac{1}{3}\begin{bmatrix} z & z^{2} \end{bmatrix}\Bigg\rvert_{(0,0,1)} = \begin{bmatrix} -\frac{1}{3} & -\frac{1}{3} \end{bmatrix}.
$$


El plano tangente a la superficie en $$(0,0,1)$$ es entonces $$z = 1 - \frac{x}{3} - \frac{y}{3}$$. Note que es el mismo plano que da $$\nabla F(0,0,1) \cdot (x,y,z-1) = 0$$, pues $$\nabla F(0,0,1) = (1,1,3)$$.

#### Ejemplo (dos ecuaciones, $$m = 2$$)
Considere el sistema


$$
\begin{cases}
F_{1}(x,y,z) = x^{2}+y^{2}+z^{2}-3 = 0 \\
F_{2}(x,y,z) = xy - z = 0
\end{cases}
$$


cerca del punto $$(1,1,1)$$, que lo satisface. ¿Podemos despejar $$(y,z)$$ en función de $$x$$? Aquí $$n = 1$$, $$m = 2$$, y el bloque de las variables dependientes es


$$
M = \frac{ \partial (F_{1},F_{2}) }{ \partial (y,z) } = \begin{bmatrix} 2y & 2z \\ x & -1 \end{bmatrix}, \qquad M(1,1,1) = \begin{bmatrix} 2 & 2 \\ 1 & -1 \end{bmatrix}, \qquad \det M(1,1,1) = -4 \neq 0.
$$


Por el teorema, existe $$g(x) = (y(x), z(x))$$ de clase $$C^{1}$$ cerca de $$x = 1$$ con $$g(1) = (1,1)$$, y con $$N = \frac{ \partial (F_{1},F_{2}) }{ \partial x } = \begin{bmatrix} 2x \\ y \end{bmatrix}$$,


$$
J_{g}(1) = \begin{bmatrix} y'(1) \\ z'(1) \end{bmatrix} = -M^{-1}N = -\frac{1}{-4}\begin{bmatrix} -1 & -2 \\ -1 & 2 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \frac{1}{4}\begin{bmatrix} -4 \\ 0 \end{bmatrix} = \begin{bmatrix} -1 \\ 0 \end{bmatrix}.
$$


Comprobación por derivación implícita: derivando ambas ecuaciones respecto a $$x$$ en $$(1,1,1)$$ se obtiene $$2 + 2y' + 2z' = 0$$ y $$1 + y' - z' = 0$$, cuya solución es $$y' = -1$$, $$z' = 0$$. Geométricamente, la curva intersección de la esfera con la silla $$z = xy$$ pasa por $$(1,1,1)$$ con vector tangente $$(1,-1,0)$$.

#### Nota
Si $$\det M(a,b) = 0$$ el teorema no dice nada, y puede pasar cualquier cosa: para $$f(x,y) = y^{2} - x^{2}$$ en $$(0,0)$$ no hay ninguna función $$y = g(x)$$ única (hay dos: $$\pm x$$), mientras que para $$f(x,y) = y^{3} - x$$ en $$(0,0)$$ sí hay una única, $$g(x) = \sqrt[3]{x}$$, pero no es derivable en $$0$$.

## Consideraciones finales

### Derivada direccional y gradiente

Dado $$u \in \mathbb{R}^n$$ con $$\lVert u \rVert_{2} = 1$$ y $$f:\mathbb{R}^n\to \mathbb{R}$$ diferenciable en $$x_{0}$$, entonces $$D_{u}f(x_{0}) = \nabla f(x_{0}) \cdot u$$ y, por Cauchy-Schwarz, 


$$
\begin{aligned}
\lvert D_{u} f(x_{0}) \rvert &= \lvert \nabla f(x_{0}) \cdot u \rvert \\
&= \lVert \nabla f(x_{0}) \rVert \cdot \lVert u \rVert \lvert \cos \theta \rvert = \lVert \nabla f(x_{0}) \rVert \cdot \lvert \cos \theta \rvert  \\
&\leq  \lVert \nabla f(x_{0}) \rVert,
\end{aligned}
$$


donde $$\theta$$ es el ángulo entre $$\nabla f(x_{0})$$ y $$u$$. Si $$u, \nabla f(x_{0})$$ son paralelos, se cumple la igualdad, pues $$\theta = 0 \implies \cos \theta = 1$$.

Si $$\nabla f(x_{0}) \neq 0$$ y tomo $$u = \frac{\nabla f(x_{0})}{\lVert \nabla f(x_{0}) \rVert}$$, entonces $$D_{u} f(x_{0}) = \lVert \nabla f(x_{0}) \rVert$$ es el valor máximo posible: $$\nabla f(x_{0})$$ apunta en la dirección de mayor crecimiento de $$f$$ en $$x_{0}$$, y $$-\nabla f(x_{0})$$ en la de mayor decrecimiento. En las direcciones perpendiculares al gradiente ($$\theta = \pi/2$$) la derivada direccional es cero: son las direcciones tangentes a la *curva de nivel* $$\{ f = f(x_{0}) \}$$, así que el gradiente es normal a las curvas de nivel.

![El gradiente es normal a la curva de nivel y apunta hacia donde f crece más rápido](/assets/img/courses/ma0450/gradiente-curvas-de-nivel.svg)

<!-- TikZ source of the figure above
\begin{tikzpicture}[scale=1.5, >=stealth]
  % curvas de nivel (elipses concéntricas)
  \foreach \r in {0.7,1.1,1.5,1.9} \draw[gray] (0,0) ellipse ({1.2*\r} and {0.75*\r});
  \node[gray] at (2.0,-1.6) {$f = c_1 < c_2 < c_3 < c_4$};
  % punto x0 sobre la elipse r=1.1
  \coordinate (P) at ({1.2*1.1*cos(50)}, {0.75*1.1*sin(50)});
  \fill (P) circle (1.3pt) node[below left] {$x_0$};
  % gradiente: normal exterior a la elipse en P
  \draw[orange, very thick, ->] (P) -- ++(0.55,0.95) node[above] {$\nabla f(x_0)$};
  % dirección tangente: derivada direccional cero
  \draw[thick, ->] (P) -- ++(0.95,-0.55) node[right] {$u$, $D_u f = 0$};
  % una dirección genérica con ángulo theta
  \draw[thick, dashed, ->] (P) -- ++(1.05,0.35) node[right] {$u$, $D_u f = \|\nabla f\|\cos\theta$};
  \draw (P) ++(0.35,0.55) arc (58:20:0.6);
  \node at ($(P)+(0.62,0.5)$) {$\theta$};
\end{tikzpicture}
-->

#### Ejemplo
Sea $$f(x,y) = x^{2}y$$ y $$x_{0} = (1,2)$$. Entonces $$\nabla f(x,y) = (2xy, x^{2})$$ y $$\nabla f(1,2) = (4,1)$$. En la dirección $$u = \left( \frac{3}{5}, \frac{4}{5} \right)$$,


$$
D_{u}f(1,2) = \nabla f(1,2) \cdot u = \frac{12}{5} + \frac{4}{5} = \frac{16}{5},
$$


mientras que la máxima tasa de crecimiento en $$(1,2)$$ es $$\lVert \nabla f(1,2) \rVert = \sqrt{ 17 }$$, alcanzada en la dirección $$\frac{(4,1)}{\sqrt{ 17 }}$$, y en la dirección $$\frac{(1,-4)}{\sqrt{ 17 }}$$, tangente a la curva de nivel $$x^{2}y = 2$$, la derivada direccional es cero.

### Diferenciales de orden superior.

Dada $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}$$ diferenciable, en cada punto tenemos $$D_{f}(x_{0}):\mathbb{R}^n\to \mathbb{R}$$ lineal, con $$D_{f}(x_{0})(h) \in \mathbb{R}$$. Es posible entonces ver la derivada como una función $$D_{f}: A \to \mathcal{L}(\mathbb{R}^n, \mathbb{R})$$ que a cada punto le asigna una transformación lineal. Vimos que $$D_{f}(x)$$ tiene como matriz asociada a $$J_{f}(x)$$. Así, 


$$
D_{f}(x_{0}) (h) = J_{f}(x_{0}) h = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} } (x_{0}) h_{i}.
$$


Tiene sentido definir $$D(D_{f}(x_{0}))$$ si $$f \in C^{2}(A)$$.

Si $$x = (x_{1},\dots,x_{n})$$, es usual definir proyecciones $$dx_{i}:\mathbb{R}^n\to \mathbb{R}$$ que $$dx_{i}(x) = x_{i}$$. Así, $$D_{f}(x_{0}) = \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}$$. Evaluando, $$D_{f}(x_{0})(h) = \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}(h)$$. Así 


$$
\begin{aligned}
\implies D(D_{f}(x_{0})) &= \sum_{j=1}^{n} \frac{ \partial }{ \partial x_{j} }(D_{f}(x_{0})) dx_{j} \\
&= \sum_{j=1}^{n} \frac{ \partial }{ \partial x_{j} } \left( \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}(h) \right) dx_{j} \\
&= \sum_{i,j=1}^{n} \frac{ \partial^{2} f }{ \partial x_{j} \partial x_{i} }  dx_{i} dx_{j}, \quad \text{con } dx_{i} dx_{j}: \mathbb{R}^n \times \mathbb{R}^n \\
\implies D_{f}^{2}(x_{0})(u,v) &= \sum_{i,j=1}^{n} \frac{ \partial^{2} f }{ \partial x_{j} \partial x_{i} }(x_{0}) u_{i} v_{j} \quad= u^{T} H v.
\end{aligned}
$$



### Definición (Diferencial de orden superior)
Sea $$B_{2}(\mathbb{R}^n,\mathbb{R}) = \{ f:D\to \mathbb{R} \text{ bilineales}\}$$, con $$D = \{ (x,x): x \in \mathbb{R}^n \}$$. Se define $$D^{2}f:A \subseteq \mathbb{R}^n \to B_{2}(\mathbb{R}^n, \mathbb{R})$$ por


$$
(D^{2}f(x_{0}))(x) = x^{T} H_{f}(x_{0}) x = \sum_{i,j=1}^{n} x_{i} x_{j} \frac{ \partial^{2} f }{ \partial x_{i} \partial x_{j} }(x_{0}).
$$


Análogamente, $$D^{3}f:A \subseteq \mathbb{R}^n \to B_{3}(\mathbb{R}^{n}, \mathbb{R})$$ dado por 


$$
(D^{3}f(x_{0}))(x) = \sum_{i,j,k=1}^{n} x_{i} x_{j} x_{k} f_{x_{k}x_{j}x_{i}}(x_{0}), 
$$


donde $$B_{3}$$ es el conjunto de las funciones trilineales restrictas $$(x,x,x)$$ con $$x \in \mathbb{R}^n$$.

#### Nota 
Taylor se puede rescribir como 


$$
f(x) = f(x_{0}) + \sum_{k=1}^{p} \frac{1}{k!} (D^{k}f(x_{0}))(x-x_{0}) + \frac{1}{(p+1)!}(D^{p+1}f(\xi))(x-x_{0}).
$$


#### Ejemplo
Sea $$f(x,y) = x^{2}y$$ y $$x_{0} = (1,2)$$. Entonces $$\nabla f(1,2) = (4,1)$$ y $$H_{f}(x,y) = \begin{bmatrix} 2y & 2x \\ 2x & 0 \end{bmatrix}$$, así que $$H_{f}(1,2) = \begin{bmatrix} 4 & 2 \\ 2 & 0 \end{bmatrix}$$. Para $$h = (h_{1},h_{2})$$,


$$
D^{1}f(1,2)(h) = 4h_{1} + h_{2}, \qquad D^{2}f(1,2)(h) = h^{T}H_{f}(1,2)h = 4h_{1}^{2} + 4h_{1}h_{2}, \qquad D^{3}f(1,2)(h) = 3 f_{xxy}\, h_{1}^{2}h_{2} = 6h_{1}^{2}h_{2},
$$


pues la única tercera derivada no nula es $$f_{xxy} = f_{xyx} = f_{yxx} = 2$$ (tres ordenamientos del mismo índice) y las de orden 4 en adelante son cero. Como el resto de orden 4 se anula, Taylor es exacto:


$$
f(1+h_{1},2+h_{2}) = 2 + (4h_{1}+h_{2}) + \frac{1}{2}(4h_{1}^{2}+4h_{1}h_{2}) + \frac{1}{6}\cdot 6h_{1}^{2}h_{2} = 2 + 4h_{1} + h_{2} + 2h_{1}^{2} + 2h_{1}h_{2} + h_{1}^{2}h_{2},
$$


que en efecto es la expansión de $$(1+h_{1})^{2}(2+h_{2})$$.
{% endraw %}
