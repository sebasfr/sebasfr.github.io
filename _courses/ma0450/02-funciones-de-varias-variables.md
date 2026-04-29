---
layout: chapter
course: ma0450
chapter: 2
title: "Funciones de varias variables"
slug: 02-funciones-de-varias-variables
toc:
  sidebar: right
lang: es
fecha: 2025-08-25
---

{% raw %}
## Recordatorio (Definición de función)
Dados dos conjuntos $$A, B$$, una relación $$f: A \to B$$ se llama función si 


$$
\forall x \in A  \quad \exists! y \in B  \quad(y \in f(x)).
$$


Consideraremos las funciones $$f: D\subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, tal que 


$$
x = \begin{pmatrix}
x_{1} \\
\vdots \\
x_{n}
\end{pmatrix} \to y = f(x) = \begin{pmatrix}
y_{1} \\
\vdots \\
y_{m}
\end{pmatrix}.
$$



#### Ejemplos 
1. $$f:\mathbb{R}^{2} \to \mathbb{R}$$ con $$f(x,y) = 1+xy$$.
2. $$f:\mathbb{R}^{2} \to \mathbb{R}^{3}$$ con $$f(x,y) = (e^{x}, \sin(y), y^{2}+1)$$.
3. $$f:\mathbb{R^{2}} \to \mathbb{R}$$ con $$f(x,y) = x^{2}+y^{2}$$
## Continuidad

### Definición (Vecindario)
Dado $$x \in \mathbb{R}^n$$, un conjunto $$V$$ se llama vecindario de $$x$$ si existe $$U$$ abierto tal que $$x \in U \subseteq V$$. Llamamos vecindario perforado a $$V\setminus \{ x \}$$.

### Definición (Función continua)
Sea $$f : D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ con $$D$$ vecindario de $$a \in D$$. Se dice que $$f$$ es continua en $$a$$ si 


$$
\begin{aligned}
&\forall \varepsilon>0  \quad \exists \delta>0  \quad \Big(\lVert x-a \rVert < \delta \implies \lVert f(x) - f(a) \rVert < \varepsilon \Big) \\
\iff &\forall \varepsilon>0  \quad \exists \delta>0  \quad \Big(x \in B_{\delta}(a) \implies f(x) \in B_{\varepsilon} (f(a)) \Big) \\
\iff &\forall \varepsilon>0  \quad \exists \delta>0  \quad \Big( f(B_{\delta}(a)) \subseteq B_{\varepsilon} (f(a))\Big).
\end{aligned}
$$


#### Nota
Dado un conjunto $$A$$, $$f(A) = \{ y: \exists x  \quad (y = f(x)) \} = \{ f(x): x \in D \}$$.

### Definición (Continuidad en un conjunto)
$$f:D \subseteq \mathbb{R}^{n} \to \mathbb{R}^{m}$$ continua en $$D$$ si es continua en todo punto de $$D$$.

#### Ejemplo 
Considere $$f:\mathbb{R}^{2}\to \mathbb{R}$$ con $$f(x,y) = x^{2}+y^{2}$$. $$f$$ es continua en $$\mathbb{R}^{2}$$.
***Prueba:*** Sean $$(a,b) \in \mathbb{R}^{2}$$ y $$\varepsilon>0$$. Tome $$\delta = \min \left\{  1, \frac{\varepsilon}{1+2 \lvert  a \rvert}, \frac{\varepsilon}{1+2 \lvert  b \rvert} \right\}$$. Suponga que $$\lVert (x,y) - (a,b) \rVert < \delta$$. Esto implica que $$\lvert x-a \rvert < \delta$$ y que $$\lvert y-b \rvert < \delta$$, pues en general $$\lvert x_{j} \rvert \leq \lVert x \rVert_{\infty} \leq \lVert x \rVert_{2}$$. Así, 


$$
\begin{aligned}
\lVert f(x,y) - f(a,b) \rVert &\leq \lvert x-a \rvert \lvert x+a \rvert + \lvert y-b \rvert \lvert y+b \rvert \\
&< \delta (1+2 \lvert a \rvert ) + \delta(1+2 \lvert b \rvert ) \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\end{aligned}
$$



### Teorema (Continuidad por puntos)
Sea $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, con $$D$$ vecindario de $$a$$. Entonces, $$f = (f_{1},\dots,f_{m})$$ es continua en $$a$$ si y solo si $$f_{j}:D \to \mathbb{R}$$ son continuas en $$a$$ para todo $$j \in \{ 1,\dots,m \}$$.
***Prueba:*** La idea es similar a la utilizada en el ejemplo anterior, observando que 


$$
\lvert f_{j}(x) - f_{j}(a) \rvert \leq \lVert f_{j}(x) - f_{j}(a) \rVert \leq  \sum_{j=1}^{m} \lvert f(x) - f(a) \rvert.
$$



### Teorema (Criterio secuencial de continuidad)
Cf. convergencia de sucesiones (MA0350). Sea $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ una función, con $$D$$ vecindario de $$a$$. Entonces, $$f$$ es continua en $$a$$ si y solo si para toda sucesión $$(x_{k})_{k \in \mathbb{N}} \subseteq D$$, con $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$, se tiene que $$f(x_{k}) \underset{k \rightarrow \infty}{\longrightarrow} f(a)$$.
***Prueba:*** ($$\implies$$): Suponga que $$f$$ es continua en $$a$$ y sea $$(x_{k})_{k \in \mathbb{N}}$$ una sucesión en $$D$$ tal que $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow}a$$. Hay que mostrar que $$f(x_{k}) \underset{k \rightarrow \infty}{\longrightarrow} f(a)$$. Dado $$\varepsilon>0$$ note que: 
1. como $$f$$ es continua en $$a$$, existe $$\delta >0$$ tal que si $$\lVert x-a \rVert < \delta$$ entonces $$\lVert f(x)-f(a) \rVert < \varepsilon$$;
2. como $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$, existe $$N \in \mathbb{N}$$ tal que para todo $$k \geq N$$, $$\lVert x_{k}-a \rVert < \delta$$.
Luego, para $$k \geq N$$, por (2), entonces $$\lVert f(x_{k}) - f(a) \rVert < \varepsilon$$, de donde concluimos que $$f(x_{k}) \underset{k  \rightarrow \infty}{\longrightarrow} f(a)$$.
($$\impliedby$$): Suponga por contradicción que $$f$$ no es continua en $$x=a$$, i.e., existe $$\varepsilon>0$$ tal que para todo $$\delta>0$$, se cumple que $$\lVert x-a \rVert <\delta$$ y $$\lVert f(x)-f(a) \rVert \geq \varepsilon$$. Probaremos que existe una sucesión $$(x_{k})_{k \in \mathbb{N}}$$ con $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ tal que  $$k \geq 1$$, tome $$\delta_{k} = \frac{1}{k}$$. Entonces existe $$x_{k}$$ tal que $$\lVert x_{k}-a \rVert < \frac{1}{k}$$ y $$\lVert f(x_{k}) - f(a) \rVert \geq \varepsilon$$, por lo que $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ y $$f(x_{k}) \underset{k \rightarrow \infty}{\cancel{ \longrightarrow }} f(a)$$, una contradicción, pues asumimos que toda sucesión satisface la convergencia de sus imágenes.

#### Corolario
Si existen sucesiones $$(x_{k})_{k \in \mathbb{N}}$$ y $$(y_{k})_{k \in \mathbb{N}}$$ con $$x_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ y $$y_{k} \underset{k \rightarrow \infty}{\longrightarrow} a$$ tales que $$f(x_{k}) \underset{k \rightarrow \infty}{\longrightarrow} L_{1}$$, $$f(y_{k}) \underset{k \rightarrow \infty}{\longrightarrow} L_{2}$$ y $$L_{1} \neq L_{2}$$, entonces $$f$$ no es continua. 

#### Ejemplo 
Considere $$f:\mathbb{R}^{2} \to \mathbb{R}$$ con 


$$
f(x,y) = \begin{cases}
\frac{x^{2}y}{x^{4}+y^{2}}, \quad  \text{si }(x,y) \neq  (0,0) \\ \\
0, \quad \text{si }(x,y) = (0,0)
\end{cases}.
$$


¿Es continua en $$(0,0)$$? Considere la sucesión $$\left( \frac{1}{k}, \frac{1}{k^{2}} \right) \underset{k \rightarrow \infty}{\longrightarrow} (0,0)$$. Note que $$f\left( \frac{1}{n}, \frac{1}{n^{2}} \right) = \frac{\frac{1}{n^{2}} \cdot \frac{1}{n^{2}}}{\frac{1}{n^{4}} + \frac{1}{n^{4}}} = \frac{1}{2}$$. Por lo tanto, $$f$$ no es continua en $$(0,0)$$. En general, si evaluamos $$f$$ en $$\left( \frac{k}{n}, \frac{k}{n^{2}} \right)$$, obtenemos puntos de convergencia diferentes cuando $$n \longrightarrow \infty$$.

### Teorema (Caracterización por abiertos de continuidad)
Sea $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ con $$D$$ abierto. Entonces, $$f$$ es continua en $$D$$ si y solo si para todo $$B \subseteq \mathbb{R}^{m}$$ abierto, se tiene que $$f^{-1}(B)$$ es abierto.

#### Nota
Recuerde que $$f(A) : \{ f(x) : x \in A \}$$ y que $$f^{-1}(A) = \{ x \in D: f(x) \in A \}$$.

***Prueba:*** $$(\implies):$$ Suponga que $$f$$ es continua en $$D$$. Sea $$B \subseteq \mathbb{R}^{m}$$ abierto. Hay que mostrar que $$f^{-1}(B)$$ es abierto. Sea $$x \in f^{-1}(B)$$. Entonces, $$f(x) \in B$$ y $$B$$ es abierto, por lo que existe $$\varepsilon > 0$$ tal que $$B_{\varepsilon}(f(x)) \subseteq B$$. Como $$f$$ es continua, existe $$\delta > 0$$ tal que 


$$
f(B_{\delta}(x)) \subseteq B_{\varepsilon}(f(x)) \subseteq B \implies B_{\delta}(x) \subseteq f^{-1}(B),
$$


donde en la última implicación utilizamos el hecho de que si $$A \subseteq B$$ entonces $$f ^{-1}(A) \subseteq f^{-1}(B)$$. Concluimos que $$f^{-1}(B)$$ es abierto.
($$\impliedby$$): Sea $$\varepsilon>0$$. Sabemos que $$B = B_{\varepsilon}(f(x))$$ es abierto. Por hipótesis, $$f^{-1}(B)$$ es abierto. Note que $$x \in f^{-1}(B)$$. Luego, existe $$\delta>0$$ tal que $$B_{\delta}(x) \subseteq f^{-1}(B)$$, por lo que $$f(B_{\delta}(x)) \subseteq f(f^{-1}(B)) \subseteq B$$, pues para todo conjunto $$A$$, $$f(f^{-1}(A)) \subseteq A$$ Por lo tanto, $$f$$ es continua en $$x$$ para todo $$x \in D$$.

#### Ejemplo 
Sea $$f:\mathbb{R}^n\to \mathbb{R}$$ continua. Como $$(c,+\infty)$$ es abierto, entonces $$f^{-1}((c,+\infty))$$ es abierto. Entonces, $$\{ x \in \mathbb{R}^n: f(x)>c \}$$ es abierto. Similarmente, $$\{ x:a<f(x)<b \}, \{ x:f(x)<d \}$$ son abiertos. Además, $$\{ x: f(x) \leq c \}$$, $$\{ x:f(x)\geq d \}$$, $$\{ x:a\leq f(x)\leq b \}$$, $$\{ x:f(x)=c \}$$ son cerrados.

### Definición (Abierto relativo)
Sea $$D \subseteq E$$. Se dice que $$O \subseteq D$$ es abierto relativo a $$D$$ (o abierto en $$D$$) si existe un conjunto abierto $$U \subseteq E$$ tal que $$O = U \cap D$$.

#### Ejemplo 
En $$E = \mathbb{R}$$, tome $$D = [0,+\infty)$$. Entonces, como $$U = (-1,1)$$ es abierto en $$\mathbb{R}$$, $$O_{1} = [0,1)$$ y $$O_{2} = (0,1)$$ son ambos abiertos relativos a $$D$$.

### Teorema (Continuidad y abiertos relativos)
Sea $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, donde $$A$$ es un vecindario de $$D$$ ($$D \subseteq U \subseteq A$$ con $$U$$ abierto). Entonces, $$f$$ es continua en $$D$$ si y solo si para todo $$B \subseteq \mathbb{R}^{m}$$ abierto, se tiene que $$f^{-1}(B)$$ es abierto relativo a $$D$$.

***Prueba:*** Ejercicio

### Teorema (Operaciones y continuidad)
Sea $$D \subseteq \mathbb{R}^n$$ vecindario de $$a$$ y $$f,g: D \to \mathbb{R}^{m}$$ continuas. Entonces:
1. Para todo $$c \in \mathbb{R}$$, $$cf$$ es continua en $$a$$,
2. $$f \pm g$$ es continua en $$a$$,
3. $$f \cdot g = \sum_{i=1}^{n} f_{i} g_{i}$$ es continua en $$a$$
4. Si $$f(a) \neq \bar{0}$$, existe $$U$$ abierto alrededor de $$a$$ tal que $$f(x) \neq \bar{0}$$ para todo $$x \in U$$.
5. Si $$g:\mathbb{R}^n \to \mathbb{R}$$, $$g(a) \neq 0$$, entonces $$(\frac{f_{1}}{g}, \dots, \frac{f_{m}}{g})$$ es continua en $$a$$.
6. 
***Prueba:*** Ejercicio, se puede desarrollar con sucesiones.

### Teorema (Composición y continuidad)
Sea $$D \subseteq \mathbb{R}^n$$ vecindario de $$a$$, $$f:D \to E \subseteq \mathbb{R}^{m}$$ continua en $$a$$, y $$g:E \to \mathbb{R}^{p}$$ continua en $$f(a)$$ con $$E$$ vecindario de $$f(a)$$. Entonces, $$g \circ f: D \to \mathbb{R}^{p}$$ es continua en $$a$$.

***Prueba:*** Ejercicio, se puede desarrollar con sucesiones.

### Teorema (Continuidad y compacidad)
Sea $$f:K \subseteq \mathbb{R}^{n} \to \mathbb{R}^{m}$$ continua y $$K$$ compacto. Entonces $$f(k)$$ es compacto
***Prueba:*** Sea $$\{ U_{\alpha} \}_{\alpha \in I}$$ un cubrimiento por abiertos de $$f(K)$$. Así, $$f(K) \subseteq \bigcup_{\alpha \in I} U_{\alpha}$$. Como para todo $$\alpha \in I$$, $$U_{\alpha}$$ es abierto, entonces $$V_{\alpha} = f^{-1}(U_{\alpha})$$ es abierto. Así, $$K \subseteq \bigcup_{\alpha \in I} V_{\alpha}$$.
Como $$K$$ es compacto, y $$\{ V_{\alpha} \}_{\alpha \in I}$$ es un cubrimiento por abiertos, existen $$V_{\alpha_{1}}, \dots, V_{\alpha_{m}}$$ tal que $$K \subseteq \bigcup_{j=1}^{m} V_{\alpha_{j}}$$. Entonces, $$f(K) \subseteq f\left( \bigcup_{i=1}^{m} V_{\alpha_{i}} \right) = \bigcup_{i=1}^{m} f(V_{\alpha_{i}}) = \bigcup_{i=1}^{m} U_{\alpha}$$, por lo que $$f(K)$$ es compacto.

#### Corolario
Bajo la mismas hipótesis, $$f$$ es acotada en $$K$$.

### Teorema (Compacidad y valores extremos)
Sean $$f:K \subseteq \mathbb{R}^n\to \mathbb{R}$$, y $$\emptyset \neq K$$ compacto. Entonces, $$f$$ alcanza un máximo y un mínimo en $$K$$, i.e., existen $$x_{m}, x_{M}$$ tales que para todo $$x \in K$$, $$f(x_{m}) \leq f(x) \leq f(x_{M})$$.

***Prueba:*** Sabemos que $$A = \{ f(x): x \in K \}$$ es acotado y que $$A \subseteq \mathbb{R}$$. Sea $$\beta = \sup A$$. Suponga que no existe $$x_{M} \in K$$ tal que $$f(x_{M}) = \beta$$, esto es, para todo $$x \in K$$, $$f(x) < \beta$$. Defina $$g:K \to \mathbb{R}$$ continua tal que $$g(x) := \frac{1}{\beta-f(x)}$$. existe $$M>0$$ tal que $$g(x) \leq M$$, de modo que $$f(x) \leq \beta - \frac{1}{M}$$. Así. $$\beta-\frac{1}{M}$$ es una cota superior de $$A$$, lo que contradice el hecho de que $$\beta$$ es el supremo. Concluimos que existe tal $$x_{M}$$. La existencia de $$x_{m}$$ se prueba de forma análoga.

### Teorema (Valor intermedio generalizado)
Sea $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}$$ continua, con $$C$$ conexo. Sean $$a,b \in C$$ con $$f(a)$$ y $$f(b)$$. Entonces, si $$u \in \mathbb{R}$$ con $$f(a) < u <f(b)$$, existe $$c \in C$$ tal que $$f(c) = u$$.

***Prueba:***  Sea $$u \in (f(a),f(b))$$. Suponga que para todo $$x \in C$$, se tiene $$f(x) \neq u$$. Sean $$A = \{ x \in C: f(x) < u \}$$ y $$B \in \{ x \in C: f(x)>u \}$$. Note que:
1. $$A \cap B  = \emptyset$$,
2. $$A \cup B = \emptyset$$,
3. $$A$$ y $$B$$ son abiertos, pues son imágenes inversas de conjuntos abiertos
4. $$C \cap A \neq \emptyset$$ pues $$a \in C$$ y $$a \in A$$. De la misma manera, $$C \cap B \neq \emptyset$$.
Estas observaciones contradicen la conexidad de $$C$$, de donde concluimos que existe $$c \in C$$ que cumple que $$f(c) = u$$.

### Teorema (Continuidad y conexidad)
Sea $$f:C \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ continua con $$C$$ conexo. Entonces, $$f(c)$$ es conexo.

***Prueba:***  Suponga por contradicción que $$f(C)$$ no es conexo. Luego, existen $$A$$ y $$B$$ abiertos disjuntos, con $$f(C) \subseteq A \cup B$$, $$f(C) \cap A \neq \emptyset$$, y $$f(C) \cap B \neq \emptyset$$. Sabemos que:
1. $$f^{-1}(A)$$ y $$f^{-1}(B)$$ son abiertos por continuidad.
2. $$f^{-1}(A) \cap f^{-1}(B) = \emptyset$$ (se puede probar por contradicción).
3. Como $$f(C) \subseteq A \cup B$$, entonces 


$$
C \subseteq f^{-1}(f(C)) \subseteq f^{-1}(A \cup B) = f^{-1}(A) \cup f^{-1}(B).
$$


4. Como $$f(C) \cap A \neq \emptyset$$, existe $$y$$ tal que $$y \in A$$ y $$y \in f(C)$$, i.e., $$y = f(x)$$ con $$x \in C$$. Luego, $$x \in C \cap f^{-1}(A)$$, por lo que $$C \cap f^{-1}(A) \neq 0$$. Similarmente, podemos probar que $$C \cap f ^{-1}(B) \neq \emptyset$$.
Estas observaciones contradicen la conexidad de $$f(C)$$, de donde concluimos que $$C$$ es conexo. 

### Definición (Continuidad uniforme)
Sea $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$.  $$f$$ es uniformemente continua si para todo $$\varepsilon>0$$ existe $$\delta > 0$$ tal que para todos $$x,y \in D$$ con $$\lVert x-y \rVert < \delta$$, entonces $$\lVert f(x) - f(y) \rVert < \varepsilon$$.

### Teorema (Continuidad uniforme en compacidad)
Si $$f$$ es continua en $$K$$ compacto, entonces $$f$$ es uniformemente continua en $$K$$.

***Prueba:*** Sea $$\varepsilon>0$$. Para $$a \in K$$, existe $$\delta_{a} > 0$$ tal que si $$x \in B_{\delta_{a}}(a)$$ entonces $$\lVert f(x) - f(a) \rVert < \frac{\varepsilon}{2}$$ (por continuidad en $$a$$). Además, $$K \subseteq \bigcup_{a \in K} B_{\frac{\delta_{a}}{2}}(a) = B$$ es un cubrimiento de abiertos. Como $$K$$ es compacto, existen $$a_{1}, \dots, a_{N} \in K$$ tal que $$K \subseteq \bigcup_{j=1}^{N} B_{\frac{\delta_{a_{j}}}{2}}(a_{j})$$. Tome $$\delta = \min\left\{ \frac{\delta_{a_{1}}}{2}, \dots, \frac{\delta_{a_{N}}}{2} \right\}$$. Si $$x,y \in K$$, con $$\lVert x-y \rVert<\delta$$.
Existe $$i \in \{ 1,\dots,N \}$$ tal que si $$x \in B_{\frac{\delta_{a_{i}}}{2}}(a_{i}) \subseteq B_{\delta_{a_{i}}}(a_{i})$$, por lo que $$\lVert f(x)-f(a_{i}) \rVert < \frac{\varepsilon}{2}$$
Además, note que 


$$
\begin{aligned}
\lVert y-a_{i} \rVert & \leq \lVert y-x \rVert + \lVert x-a_{i} \rVert \\
& < \delta + \frac{\delta_{a_{i}}}{2} \leq \frac{\delta_{a_{i}}}{2} + \frac{\delta_{a_{i}}}{2} = \delta_{a_{i}},
\end{aligned}
$$


por lo que $$y \in B_{\delta_{a_{i}}}(a_{i})$$, de donde obtenemos que $$\lVert f(y) - f(a_{i}) \rVert < \frac{\varepsilon}{2}$$.
Así, 


$$
\begin{aligned}
\lVert f(x) - f(y) \rVert & \leq  \lVert f(x) - f(a_{i}) \rVert +  \lVert f(a_{i}) - f(y) \rVert \\
& < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\end{aligned}
$$



## Límites

### Definición (Límite de una función)
Sea $$f:V \setminus \{ a \} \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$, con $$V$$ vecindario de $$a$$. Se dice que $$\lim_{ x \to a } f(x) = L$$ si 


$$
\forall \varepsilon > 0  \quad \exists \delta>0  \quad \forall x \in V \setminus \{ a \} (0 < \lVert x-a \rVert < \delta \implies \lVert f(x) - L \rVert < \varepsilon).
$$



### Teorema (Continuidad y límites)
$$f:A \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ es continua en un punto $$a$$ si y solo si $$\lim_{ x \to a } f(x) = f(a)$$.

***Prueba:*** Se sigue directamente de las definiciones.

### Teorema (Criterio secuencial del límite)
Sea $$f:V \setminus \{ a \} \to \mathbb{R}^{m}$$. Las siguientes son equivalentes: 
1. $$\lim_{ x \to a } f(x) = L$$
2. Para toda sucesión $$(x_{n})_{n \in \mathbb{N}} \subseteq V \setminus \{ a \}$$ con $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} a$$, se tiene que $$f(x_{n}) \underset{n \rightarrow \infty}{\longrightarrow} L$$.

***Prueba:*** Igual a la de continuidad.

### Nota (Operaciones algebraicas sobre límites)
Los resultados sobre $$+,-,\cdot$$ se mantienen para límites.

#### Ejemplo 
Considere $$f(x,y) = (x^{2} + y^{2}) \sin\left( \frac{1}{x^{2}+y^{2}} \right)$$. Calcule $$\lim_{ (x,y) \to (0,0) } f(x,y)$$.
Conjeturamos que el valor del límite es cero. Dado $$\varepsilon>0$$, tome $$\delta = \sqrt{ \varepsilon }$$. Suponga que $$\lVert (x,y) \rVert < \delta$$. Entonces, 


$$
\left\lvert  (x^{2}+y^{2})\underbrace{ \sin\left( \frac{1}{x^{2}+y^{2}} \right) }_{ \leq 1 }  \right\rvert \leq \lVert (x,y) \rVert^{2} < \delta^{2} = \varepsilon. 
$$



#### Ejemplo 
Considere $$f:\mathbb{R}^{2} \to \mathbb{R}$$ tal que 


$$
f(x,y) = \begin{cases}
\frac{x^{3}+y^{3}}{x+y}, \quad  \text{si }x\neq  y \\
x  \quad  \quad  \quad \text{si }x = -y
\end{cases}.
$$


Determine los puntos donde el límite no existe.
Conjeturamos que el límite no existe en los puntos $$(-a,a)$$.
1. Sea $$(x_{n},y_{n}) = \left( a+\frac{1}{n}, -\left( a+\frac{1}{n} \right) \right) \underset{n \rightarrow \infty}{\longrightarrow} (a,-a)$$. Entonces, $$f(x_{n},y_{n}) = a+\frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} a$$.
2. Sea $$(\hat{x}_{n}, \hat{y}_{n}) = \left( a+\frac{1}{n}, -a+\frac{1}{n} \right) \underset{n \rightarrow \infty}{\longrightarrow} (a,-a)$$. Entonces $$f(\hat{x}_{n}, \hat{y}_{n}) = \left( a+\frac{1}{n} \right)^{2} - \left( a + \frac{1}{n} \right)\left( -a+\frac{1}{n} \right) + \left( -a+\frac{1}{n} \right)^{2} \underset{n \rightarrow \infty}{\longrightarrow} 3a^{2}$$.
Note que $$3a^{2} = a$$ si y solo si $$a = 0$$ o $$a = \frac{1}{3}$$, por lo que es necesario probar que el límite existe en estos puntos. También, es necesario probar que el límite existe en los puntos, $$(a,b)$$ con $$a \neq -b$$ (ejercicio).
{% endraw %}
