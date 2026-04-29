# Diferenciación

#Mate #MA0450
Fecha: 2025-09-08
Prerrequisitos: [[Topología en Rn]], [[Funciones de varias variables]]. Ver también: [[Integración en Rn]], [[Cálculo vectorial]].
Conecta con: [[Transformaciones lineales]] (MA0360, el diferencial es una T.L.), [[Series de funciones]] (MA0350, Taylor en una variable).

## Derivadas parciales

### Definición (Derivada parcial)
Sea $f:D \subseteq \mathbb{R}^n \to \mathbb{R}$ con $D$ vecindario de $a$. Para $j \in \{ 1,\dots,n \}$, se define la derivada parcial de $f$ en $a = (a_{1},\dots,a_{n})$ con respecto a la entrada $j$ como 
$$
D_{j}f(a) = \lim_{ h \to 0} \frac{f(a_{1},\dots,a_{j-1}, a_{j}+h, a_{j+1},\dots,a_{n}) - f(a)}{h}.
$$

#### Nota:
1. Si $y=f(x)$, entonces $f'(a) = \lim_{ h \to 0 } \frac{f(a+h)-f(a)}{h}$.
2. Escribimos $D_{j}f(a) = \frac{\partial f}{\partial x_{j}}(a) = f_{x_{j}}(a)$.
3. Las variables $x_{i} \neq x_{j}$ para todo $i$ se toman como constantes.
4. Si defino $g(x_{j}) = f(a_{1},\dots,a_{j-1}, x_{j}, a_{j+1},\dots, a_{n})$, entonces $D_{j}f(a) = g'(a_{j})$.

#### Ejemplo 
Si $f(x,y,z) = e^{xy^{2}} + \sin(xyz)$ entonces $D_{1}f(x,y,z) = e^{xy^{2}}y^{2} + \cos(xyz) \cdot yz$.

### Definición (Derivadas parciales de orden superior)
Dada $f$ tal que $D_{j} f(a)$ existen para todo $j \in \{ 1,\dots n \}$, se definen $D_{ij}f(a) = D_{i} (D_{j} f(a))$.
Escribimos $D_{ij} f(a) = \frac{\partial}{\partial  x_i}(\frac{\partial f}{\partial  x_{j}})(a) = f_{x_{j}x_{i}}(a)$.

#### Nota:
La notación se puede extender, p.e., $\frac{\partial^{4} f}{\partial x_{1} \partial x_{2} \partial x_{4} \partial x_{3}}(a)$.

### Teorema (Schwarz)
Sea $f:D \subseteq \mathbb{R}^n \to \mathbb{R}$, con $a \in D$. Suponga que $f$ es continua en $B_{r}(a)$ y que $D_{1}f$, $D_{2} f$ y $D_{21} f$ existen y son continuas en $a$. Entonces, $D_{21} f(a)$ existe y $D_{21}f(a) = D_{12}f(a)$.

***Prueba:*** Para $n = 2$, sera $a = (x_{0},y_{0})$. Existen $h,k > 0$ tales que 
$$
\underbrace{ [x_{0}-h,x_{0}+h] }_{I } \times \underbrace{ [y_{0}-k,y_{0}+k] }_{ J } \subseteq B_{r}(x_{0},y_{0}) \subseteq D.
$$
Defina $\phi(x) = f(x, y_{0}+k) - f(x,y_{0})$. Por hipótesis $\phi$ es continua y derivable en $I$. Por teorema del valor medio, existe $c \in (x_{0}, x_{0}+h)$ tal que $\phi(x_{0}+h) - \phi(x_{0}) = \phi'(c) \cdot h$. Entonces, 
$$
\phi(x_{0}+h) - \phi(x_{0}) = h(D_{1}f(c, y_{0}+k) - D_{1}f(c,y_{0})).
$$
Defina $\psi(y) = D_{1}f(x,y)$ con $y \in [y_{0},y_{0}+k]$. Por teorema del valor medio, existe $d \in (y_{0},y_{0}+k)$ tal que $\psi(y_{0}+k) - \psi(y_{0}) = \psi'(d) \cdot k$. Luego 
$$
\begin{aligned}
& D_{1} f(c,y_{0}+k) - D_{1} f(c,y_{0}) = D_{21} f(c,d) \cdot k \\
\implies & \phi(x_{0}+h) - \phi(x_{0}) = D_{21} f(c,d) \cdot k \cdot h \\
\implies & \frac{f(x_{0}+h,y_{0}+k) - f(x_{0}+h,y_{0})}{k} - \frac{f(x_{0},y_{0}+k)-f(x_{0},y_{0})}{k} = h \cdot D_{21} f(c, d) \\

\end{aligned} 
$$
Tomando límite cuando $k \to 0$ y dividiendo entre $h$:
$$
\frac{D_{2}f(x_{0}+h,y_{0}) - D_{2}f(x_{0},y_{0})}{h} = D_{21} f(c,y_{0}) \quad \text{pues }d \in (y_{0},y_{0}+k.
$$
Tomando límite cuando $h \to 0$ 
$$
D_{1}(D_{2}f) (x_{0}, y_{0}) = D_{12} f (x_{0},y_{0}) = D_{21} f(x_{0},y_{0}),
$$
de donde concluimos el resultado.

#### Nota
Para $f:\mathbb{R}^{2} \to \mathbb{R}$, $D_{121} f(a,b) = D_{112} f(a,b) = D_{211} f(a,b)$.  Si $f \in \mathbb{R}^{n} \to \mathbb{R}$, el resultado se mantiene y la intuición de la prueba es la misma, pero la prueba es más tediosa.

### Teorema (Teorema del valor medio)
Cf. [[Integral de Riemann]] (MA0350, TVM en una variable). Sea $f: B_{\delta}(a) \subseteq \mathbb{R}^n \to \mathbb{R}$. Suponga que $f$ es continua y que para todo $j \in \{ 1,\dots,n \},$ $D_{j}(f)$ existe y es continua. Entonces, para todo $x \in B_{\delta}(a)$, existen $\xi_{1}, \dots \xi_{n} \in B_{\delta}(a)$ tales que, si $x = (x_{1},\dots, x_{n})$ y $a = (a_{1}, \dots, a_{n})$, entonces
$$
f(x) - f(a)= \sum_{j=1}^{n} D_{j} f(\xi_{j}) (x_{j} - a_{j}).
$$
***Prueba:*** Para $n=2$, note que 
$$
f(x) - f(a) = f(x_{1},x_{2}) - f(a_{1}, x_{2}) + f(a_{1},x_{2}) - f(a_{1},a_{2}).
$$
Sean $g(t) = f(t,x_{2})$ y $h(t) = f(a_{1},t)$. Entonces, 
$$
\begin{aligned}
\implies f(x)-f(a) &= g(x_{1}) - g(a_{1}) + h(x_{2}) - h(a_{2}) \\
&\underset{TVM}{=} g'(t_{1}) (x_{1}-a_{1}) + h'(t_{2})(x_{2}-a_{2}) \\
&= D_{1}f(\underbrace{ t_{1},x_{2} }_{ \xi_{1} })(x_{1}-a_{1}) + D_{2} f(\underbrace{ a_{1}, t_{2} }_{ \xi_{2} })(x_{2}-a_{2}),
\end{aligned}
$$
con $t_{i}$ entre $x_{i}$ y $a_{i}$. El razonamiento es análogo para $n>2$.

#### Ejemplo 
Considere 
$$
f(x,y) = \begin{cases}
\frac{xy}{x^{2}+y^{2}} \quad \text{si }(x,y) \neq  (0,0) \\
0  \quad  \quad  \quad \text{si }(x,y) = (0,0)
\end{cases}.
$$
Note que 
1. $f$ no es continua en $(0,0)$.
2. $\frac{\partial f}{\partial x} (0,0) = \lim_{ h \to 0 } \frac{f(h,0)-f(0,0)}{h} = \lim_{ h \to 0 } \frac{\frac{0 \cdot h}{h^{2}+0^{2}} - 0}{h} = 0$.
3. Ahora, si $(a,b) \neq (0,0)$, entonces 
$$
\frac{\partial f}{\partial x}(a,b) = \frac{(x^{2}+y^{2})y - xy \cdot 2x}{(x^{2}+y^{2})^{2}} \biggr\rvert_{(x,y)=(a,b)} = \frac{b(b^{2}-a^{2})}{(a^{2}+b^{2})^{2}}.
$$
Así, 
$$
\frac{\partial f(x,y)}{\partial x} = \begin{cases}
\frac{y(x^{2}-y^{2})}{(x^{2}+y^{2})^{2}} \quad \text{si }(x,y) \neq (0,0) \\
0  \quad  \quad  \quad \text{si }(x,y) = (0,0)
\end{cases}
$$
Podemos probar que esta función es continua en $(0,0)$, lo que nos dice que en varias dimensiones, derivabilidad no implica continuidad. Note que la derivada no es continua en $(0,0)$.


### Teorema (Derivabilidad y continuidad)
Sea $f:D\subseteq \mathbb{R}^n \to \mathbb{R}$ tal que $\frac{\partial f}{\partial x_{i}}(x)$ existen y son continuas en $D$ (abierto) para todo $i \in \{ 1,\dots,n \}$. Entonces $f$ es continua en $D$.

***Prueba:*** Sean $a \in D, \varepsilon>0$. Entonces, existe $r>0$ tal que $B:=\bar{B}_{r}(a) \subseteq D$. Como $B$ es compacto y las $\frac{\partial f}{\partial x_{i}}(x)$ son continuas, existen $M_{i} > 0$ para todo $i \in \{ 1,\dots,n \}$ tales que $\left\lvert   \frac{\partial f}{\partial x_{j}} (x) \right\rvert \leq M_{j}$ para todo $x \in B$. Sea $M = \max \{ M_{1}, \dots, M_{n} \}>0$. Tome $\delta < \min \left\{  \frac{\varepsilon}{Mn},1  \right\}$.  Suponga que $\lVert x-a \rVert<\delta$. Así $\lvert x_{j}-a_{j} \rvert < \delta$ para todo $j$. Entonces, por el teorema del valor medio, $f(x)-f(a) = \sum_{j=1}^{n} \frac{\partial f}{\partial x_{j}}(\xi_{j})(x_{j}-a_{j})$, con $\xi_{1}, \xi_{2},\dots,\xi_{n} \in B$. Entonces 
$$
\begin{aligned}
\lvert f(x)-f(a) \rvert &\leq \sum_{j=1}^{n} \left\lvert \frac{\partial f}{\partial x_{j}}(\xi_{j}) \right\rvert \lvert x_{j}-a_{j} \rvert \\
&\leq \sum_{j=1}^{n} M\delta = nM\delta < \varepsilon 
\end{aligned}
$$

### Teorema (Extremos absolutos y derivadas)
Dada $f:D \subseteq \mathbb{R}^n \to \mathbb{R}$, suponga que $f$ alcanza un extremo relativo en $c \in D^{\circ}$. Si $\frac{\partial f}{\partial x_{j}}(c)$ existe, $\frac{\partial f}{\partial x_{j}}(c) = 0$.

***Prueba:*** Defina $g(x) = f(c_{1},c_{2},\dots,c_{j-1},x,c_{j+1},\dots,c_{n})$ con $c = (c_{1},\dots,c_{n})$. Entonces $g'(c) = \frac{\partial f}{\partial x_{j}}(c)$. Sabemos que $g$ tiene extremo relativo en $c$, entonces $g'(c) = \frac{\partial f}{\partial x_{j}}(c) = 0$.

#### Nota 
Sea $f:\mathbb{R} \to \mathbb{R}$. Si $f'(a) = \lim_{ x \to a } \frac{f(x)-f(a)}{x-a} = \frac{\lim_{ h \to 0 }f(a+h)-f(a)}{h}$. Esta es la noción de derivabilidad, pero ¿es esta noción igual a diferenciabilidad?

## Diferenciabilidad

#### Nota
En una dimensión, $f'(a)$ existe si y solo si $\lim_{ h \to 0 } \frac{f(a+h)-f(a)-f'(a)h}{h} = 0$.

### Definición (Diferenciabilidad)
Dada $f:D \subseteq \mathbb{R}^n\to \mathbb{R}^{m}$, con $D$ vecindario de $a$. Se dice que $f$ es diferenciable en $a$ si existe una [[Transformaciones lineales|transformación lineal]] $T:\mathbb{R}^n\to \mathbb{R}^{m}$ tal que 
$$
\lim_{ \vec{h} \to 0 } \frac{\lVert f(a+\vec{h}) - f(a) - T(\vec{h}) \rVert_{m}}{\lVert \vec{h} \rVert_{n}}  = 0
$$
#### Notas
1. $\frac{\partial f}{\partial x_{j}}(c) = \lim_{ h \to 0 } \frac{f(c+h e_{j})-f(c)}{h}$, donde $e_{j}$ es el $j$-ésimo vector canónico.
2. Si la función es diferenciable en $a$, escribimos $D_{f}(a)=T$
3. Evaluar $D_{f}$ se escribe $D_{f}(a)(x) = T(x)$.

#### Ejemplo 
Considere $f:\mathbb{R}^n\to \mathbb{R}^{m}$, con $f(x) = c \in \mathbb{R}^{m}$. Si $T(x) = 0$, entonces $D_{f}(a) = 0$, pues 
$$
\lim_{ h \to 0} \frac{\lVert c-c-0 \rVert }{\lVert h \rVert }  = 0
$$

#### Ejemplo 
Si $f:\mathbb{R}\to \mathbb{R}$ es derivable en $a$, entonces $D_{f}(a)(h) = f'(a) h$. El diferencial puede usarse para hacer aproximaciones, por ejemplo, de Taylor: $f(a+h) \approx f(a) + hf'(a)$.

#### Ejemplo 
Considere $f:\mathbb{R}^{2}\to \mathbb{R}$ con $f(x,y) = x^{2}+3y$ ¿$D_{f}(a,b)$? 
Sea $(h,k)$ el incremento del límite. Note que 
$$
\begin{aligned}
&  \lim_{ (h,k) \to (0,0) } \frac{\lvert (a+h)^{2}+3(b+k) - a^{2}-3b-T(h,k) \rvert }{\lVert (h,k)\rVert } \\
&= \lim_{ (h,k) \to (0,0) } \frac{\lvert 2ah+h^{2}+3k-T(h,k) \rvert }{ \sqrt{h^{2}+k^{2}}}=L
\end{aligned}
$$
Tome $T(h,k) = 2ah + 3k$. Claramente $T$ es lineal y además, si $(h,k) \longrightarrow (0,0)$ entonces $T(h,k)\longrightarrow 0$. Así, 
$$
L=\lim_{ (h,k) \to (0,0)} \frac{h^{2}}{\sqrt{ h^{2}+k^{2} }} = 0 
$$
pues 
$$
0 \leq  \frac{h^{2}}{\sqrt{ h^{2}+k^{2} }} \leq \frac{h^{2}}{\sqrt{ h^{2} }} = h \underset{(h,k) \rightarrow (0,0)}{\longrightarrow} (0,0),
$$
por lo tanto $D_{f}(a,b)(h,k) = 2ah+3k =\begin{pmatrix}2a & 3\end{pmatrix} \begin{pmatrix}h \\ k\end{pmatrix}$.

 ### Teorema (Unicidad del diferencial)
Si $f$ es diferenciable en $a$, su diferencial es único.
***Prueba:*** Suponga que existen $T, S: \mathbb{R}^n \to \mathbb{R}^{m}$ lineales tales que cumplen definición. Entonces se cumple que 
$$
\begin{aligned}
\frac{\lVert T(h)-S(h) \rVert }{\lVert h \rVert } \leq  \frac{\lVert T(h) - f(a+h) + f(a) \rVert }{\lVert h \rVert } + \frac{\lVert f(a+h) - f(a) - S(h)  \rVert }{\lVert h \rVert } \underset{h \rightarrow 0}{\longrightarrow} 0. 
\end{aligned}
$$
Ocupo $T(x) =  S(x) \quad \forall x \in \mathbb{R}^n$. Luego, si $x \in \mathbb{R}^n\setminus \{ 0 \}$, $t \in \mathbb{R}$, tome $h = tx$. Así,
$$
0 = \lim_{ t \to 0 } \frac{\lVert T(tx) - S(tx) \rVert }{\lVert tx \rVert } = \lim_{ t \to 0 } \frac{\lVert T(x) - S(x) \rVert }{\lVert x \rVert } = \frac{\lVert T(x) - S(x) \rVert }{\lVert x \rVert },
$$
por lo que $T(x) = S(x)$ para todo $x \in \mathbb{R}^n\setminus \{ 0 \}$ (la igualdad en cero se cumple trivialmente por ser transformaciones lineales), y por tanto $S = T$.


### Teorema (Diferenciabilidad implica continuidad)
Si $f$ es diferenciable en $a$, entonces es continua en $a$. Entonces, $f$ es continua en $a$.
***Prueba:*** Sea $\varepsilon>0$. Por diferenciabilidad existe $\delta_{1}>0$ tal que si $\lVert h \rVert < \delta_{1}$ entonces 
$$
\frac{\lVert f(a+h) - f(a) - D_{f}(a)(h) \rVert }{h} < \varepsilon. \ \tag{1}
$$
Como $D_{f}(a)$ es lineal, entonces es continua. Existe $\delta_{2}>0$ tal que 
$$\lVert x-a \rVert<\delta_{2} \implies \lVert D_{f}(a)(x) - D_{f}(a)(a) \rVert < \frac{\varepsilon}{2}. $$
Tome $\delta = \min \left\{  \delta_{1}, \delta_{2}, \frac{1}{2}  \right\}$. Suponga que $\lVert x-a \rVert < \delta$. Entonces 
$$
\begin{aligned}
\lVert f(x)-f(a) \rVert &\leq \lVert f(x) - f(a) - D_{f}(a)(x-a) \rVert + \lVert D_{f}(a)(x-a) \rVert  \\
&\leq \varepsilon \lVert x-a \rVert + \frac{\varepsilon}{2} \quad  \quad  \text{tomando } h =x-a \text{ en (1)}\\
&< \varepsilon \delta + \frac{\varepsilon}{2} \leq \varepsilon.
\end{aligned}
$$
Concluimos que $f$ es continua en $a$. 

### Definición (Derivada direccional)
Dado $f:\mathbb{R}^n\to \mathbb{R}$, $\vec{u} \in \mathbb{R}^n$, $\lVert \vec{u} \rVert = 1$, se define la derivada direccional en $\vec{u}$ como 
$$
D_{\vec{u}}f(a) = \lim_{ h \to 0 } \frac{f(a+h \vec{u}) - f(a)}{h}.
$$

#### Nota
Si $\vec{u} = e_{j}$, entonces $D_{\vec{u}}f(a) = \frac{\partial f(a)}{\partial x_{j}}$, pues $a+h \vec{u} = a+h e_{j}$. 

### Teorema (Diferenciabilidad y derivada direccional)
Sea $f:D \subseteq \mathbb{R}^n\to \mathbb{R}$, $a \in D$ abierto. Si $f$ es diferenciable en $a$, entonces $D_{\vec{u}}f(a)$ existe para todo $\vec{u} \in \mathbb{R}^n$, y $D_{\vec{u}}f(a) = D_{f}(a)(u)$.
***Prueba:*** Note que 
$$
\begin{aligned}
D_{\vec{u}}f(a) &= \lim_{ h \to 0 }\underbrace{  \frac{f(a+h \vec{u}) - f(a)-D_{f}(a)(hu)}{h} }_{ \longrightarrow 0 } + \frac{D_{f}(a)(\cancel{ h }u)}{\cancel{ h }} \\
&= D_{f}(a)(u),
\end{aligned}
$$
de donde se concluye el resultado. 

#### Corolario
Bajo la misma hipótesis, $\frac{\partial f}{\partial x_{1}}, \dots, \frac{\partial f}{\partial x_{xn}}$ existen y $D_{f}(a)(y) = \sum_{i=1}^{n} \frac{\partial f(a)}{\partial x_{i}} y_{i}$ con $y = (y_{1}, \dots, y_{n})$.
***Prueba:*** La existencia de las derivadas parciales existen por el teorema anterior, tomando $u$ como cada uno de los vectores canónicos. Además, 
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
\implies D_{f}(a) = \nabla f(a).
$$

#### Ejemplo 
Considere $f:\mathbb{R}^{3} \to \mathbb{R}$ tal que $f(x,y,z)= x^{2}++yz$. Entonces 
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
Si $a = (1,-1,0)$, entonces $\nabla f(a) =\begin{bmatrix}2 & 0 & -1\end{bmatrix}^{T}$ y entonces 
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

### Teorema (Diferenciabilidad por entradas de funciones)
Sea $f:\mathbb{R}^n \to \mathbb{R}^{m}$, $f =\begin{pmatrix}f_{1} \\ \vdots \\ f_{m}\end{pmatrix}$, $f_{j}:\mathbb{R}^n\to \mathbb{R}$. Entonces $f$ es diferenciable en $a$ si y solo si $f_{j}$ es diferenciable en $a$ para todo $j \in \{ 1,\dots ,n \}$. Además, 
$$
D_{f}(a) = \begin{bmatrix}
D_{f_{1}}(a) \\
\vdots \\
D_{f_{n}}(a)
\end{bmatrix}.
$$
***Prueba:*** ($\impliedby$): Sabemos que para todo $x \in \mathbb{R}^{n}$ y para todo $j \in \{ 1,\dots,n \}$, $\lvert x_{j} \rvert \leq \lVert x \rVert \leq \sum_{j=1}^{n} \lvert x_{j} \rvert$. Así, tenemos que 
$$
\begin{aligned}
0 \leq  \frac{\lvert f_{j}(a+h) - f_{j}(a) - T_{j}(h) \rvert }{\lVert h \rVert } &\leq \frac{\lVert f(a+h) -f(a) - T(h) \rVert }{\lVert h \rVert } \\
&\leq \sum_{j=1}^{m} \frac{\lvert f_{j}(a+h) -f_{j}(a) - T_{j}(h)\rvert}{\lVert h \rVert }.
\end{aligned}
$$
$(\implies)$: Si $f$ es diferenciable en $a$, entonces $f_{j}$ es diferenciable en $a$ (por la desigualdad anterior), y entonces $D_{f_{j}}(a) = T_{j}$.

### Definición (Matriz jacobiana)
Sea $f$ diferenciable en $a$. Como $D_{f}(a):\mathbb{R}^n \to \mathbb{R}^{m}$, considere $J_{f}(a)$ (matriz jacobiana de $f$ en $a$) como la matriz asociada a $D_{f}(a)$ en bases canónicas.

#### Corolario
Si $f:\mathbb{R}^n\to \mathbb{R}^{m}$, $f = \begin{pmatrix}f_{1} & \dots & f_{m}\end{pmatrix}^{T}$ es diferenciable en $a$ entonces $\frac{ \partial f_{i}(a) }{ \partial x_{j} }$ existen para todos $j \in \{ 1,\dots n \}$, $i \in \{ 1,\dots,m \}$. Además, $[J_{f}(a)]_{ij} =  \frac{ \partial f_{i}(a) }{ \partial x_{j} }$. Esto es 
$$
J_{f}(a) = \begin{bmatrix}
\frac{ \partial f_{1}(a) }{ \partial x_{1} } & \frac{ \partial f_{1}(a) }{ \partial x_{2} } & \dots & \frac{ \partial f_{1}(a) }{ \partial x_{n} } \\
\frac{ \partial f_{2}(a) }{ \partial x_{1} } & \frac{ \partial f_{2}(a) }{ \partial x_{2} }  & \dots  & \frac{ \partial f_{2}(a) }{ \partial x_{n} } \\
\vdots & \vdots & \ddots & \vdots \\
\frac{ \partial f_{m}(a) }{ \partial x_{1} } & \frac{ \partial f_{m}(a) }{ \partial x_{2} } & \dots & \frac{ \partial f_{m}(a) }{ \partial x_{n} }
\end{bmatrix}_{m \times n}
$$

#### Ejemplo
Considere $f(x,y,z) = \begin{pmatrix}x^{2}\sin y - z \\ e^{xy} + zx\end{pmatrix}$. Entonces, 
$$
J_{f}(x,y,z) = \begin{bmatrix}
2x\sin y & x^{2}\cos y & -1 \\
y e^{xy}+z & xe^{xy} & x
\end{bmatrix}.
$$
Si $(a,b,c) = (1,0,\pi)$, 
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
Sea $f:A\subseteq \mathbb{R}^n \to \mathbb{R}$. Suponga que $f$ es continuamente derivable en $a$; esto es, $f$ y sus derivadas de primer orden son continuas en $a$. Entonces, $f$ es diferenciable en $a$ y $J_{f}(a) = \nabla f(a)$.

***Prueba:*** Sea $\varepsilon>0$. Por continuidad, existen $\delta_{1},\dots,\delta_{n}$ tales que para todo $1\leq j\leq n$ si $\lVert x-a \rVert <\delta_{j}$, entonces $\left\lVert  \frac{ \partial f }{ \partial x_{j} }(x) - \frac{ \partial f }{ \partial x_{j} }(a)  \right\rVert < \frac{\varepsilon}{n}$. Sea $T:\mathbb{R}^n\to \mathbb{R}$ una transformación lineal con $T(x_{1},\dots,x_{n}) = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(a) \cdot x_{i}$ . Tome $\delta = \min\{ \delta_{1},\dots,\delta_{n} \}$ y sea $h = (h_{1},\dots, h_{n}) \in B_{\delta}(a)$. Por Teorema del Valor Medio, existen $\xi_{1}, \dots, \xi_{n} \in B_{\delta}(a)$ tales que  
$$
f(a+h)-f(a) = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(\xi_{i}) \cdot h_{i}.
$$

Así, haciendo uso de esta expresión en la definición de diferenciabilidad: 
$$
\begin{aligned}
\frac{\lvert f(a+h) - f(a) \rvert }{\lVert h \rVert } &= \frac{1}{\lVert h \rVert } \left\lvert  \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(\xi_{i}) \cdot h_{i} \right\rvert \\
&<  \sum_{i=1}^{n} \frac{\varepsilon}{n} \underbrace{ \frac{\lvert h_{i} \rvert }{\lVert h \rVert } }_{ \leq 1 } < \varepsilon,
\end{aligned}
$$
de donde concluimos que $D_{f}(a) = T$.

### Teorema (Jacobiano y gradientes en funciones hacia $\mathbb{R}^{m}$)
Sea $f:A \subseteq \mathbb{R}^n \to a \in A$. Suponga que $f$ es continuamente derivable en $a$. Entonces $f$ es diferenciable en $a$ y $J_{f}(a) = [\nabla f_{1}(a), \nabla f_{2}(a),\dots, \nabla f_{n}(a)]$,

***Prueba:*** Por hipótesis, para todos $1 \leq i \leq n$, $1 \leq j \leq m$, $D_{i} f_{j}(x)$ existen y son continuos en $a$. Por el teorema anterior, $f_{j}$ es diferenciable en $a$, $J_{f_{j}}(a) = \nabla f_{j}(a)$. Luego, como $f_{j}$ es diferenciable en f para todo $j$, concluimos que $f = (f_{1},\dots,f_{n})$ es diferenciable en $a$. Finalmente, $J_{f}(a) = [\nabla f_{1}(a), \nabla f_{2}(a),\dots, \nabla f_{n}(a)]'$.

### Definición (Clases de funciones)
Se dice que $f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$ es de clase $C^{k}$ ($f \in C^{k}(D)$) si sus derivadas de $k$-ésimo orden existen y son continuas. Similarmente, decimos que $f \in C^{\infty}(D)$ si para todo $k \in \mathbb{N}$, $f \in C^{k}(D)$. Si $f:D\to B$, escribimos la definición como $f \in C^{k}(D,B)$.

### Teorema (Gradiente cero)
Sea $f \in C^{1}(D, \mathbb{R}^{m})$ con $D \subseteq \mathbb{R}^{m}$ abierto y conexo. Si $\nabla f(x) = 0$ para todo $x \in D$, $f$ es constante en $D$.

***Prueba:***  Basta probarlo para $m =1$. Sea $a \in D$. Como $D$ es abierto, entonces existe $\delta > 0$ tal que $B_{\delta}(a) \subseteq D$. Sea $x \in B_{\delta}(a)$. Además, por TVM, existen $\xi_{1},\dots,\xi_{n} \in B_{\delta}(a)$ tales que $f(x)-f(a) = \sum_{j=1}^{n} \underbrace{ \frac{ \partial f }{ \partial x_{j} }(a) }_{ =0 } \cdot (x_{j}-a_{j}) = 0$. Luego, $f(x) = f(a)$ para todo $a \in B_{\delta}(a)$.
Ahora, sea $A = \{ x \in D:f(x) = f(a) \}$. Note que $A \neq \emptyset$ pues $a \in A$. Veamos que $A$ es abierto. Dado $y \in A$, existe $\delta_{y} > 0$ $f(y) = f(x)$ para todo $y \in B_{\delta_{y}}(y)$.. Luego, note que el conjunto $B=\{ x \in D: f(x)\neq f(a) \} = f^{-1}[(-\infty,a) \cup(a, \infty)]$ es abierto, por ser imagen de una función continua en un conjunto abierto. 
Como $D = A \cup B$, $A \cap B \neq \emptyset$, pero $D$ es conexo. Luego, como $A \neq \emptyset$, se sigue que $B = \emptyset$. Luego, $A = D$, y por tanto $f$ es constante en $D$.

## Reglas de derivación
### Teorema (Reglas de derivación)
Dadas $f,g:D\subseteq \mathbb{R} \to \mathbb{R}^{m}$ diferenciables en $a$:
1. $D_{f\pm g}(a) = D_{f}(a) \pm D_{g}(a)$,
2. $D_{fg}(a) = D_{f}(a) \cdot g(a) + f(a) D_{g}(a)$,
3. Si $g:D\to \mathbb{R}$, 
$$
D_{\frac{f}{g}}(a) = \frac{D_{f}(a)g(a)-f(a)D_{g}(a)}{[g(a)]^{2}}.
$$
***Prueba:*** Ejercicio

### Teorema (Regla de la cadena)
Sea $D \subseteq \mathbb{R}^n$, con $D$ vecindario de $a$. Suponga que $f:D \to \mathbb{R}^{m}$ es diferenciable en $a$. Sea $E \subseteq \mathbb{R}^{m}$ vecindario de $f(a)$ y $G:E \to \mathbb{R}^{p}$ diferenciable en $f(a)$. Entonces, $g \circ f:D \subseteq \mathbb{R}^n\to \mathbb{R}^{p}$ es diferenciable en $a$ y además $D_{g \circ f}(a) = D_{g}(f(a)) \cdot D_{f}(a)$, esto es, $J_{g \circ f} = J_{g}(f(a)) \cdot J_{f}(a)$.

***Prueba:*** Sabemos lo siguiente:
1. Por diferenciabilidad de $g$ en $f(a)$, dado $\varepsilon>0$, existe $\delta_{1} > 0$ tal que si $\lVert h_{1} \rVert<\delta_{1}$, entonces 
$$
\lVert g(f(a)+h) - g(f(a)) - S(h_{1}) \rVert < \varepsilon \lVert h_{1} \rVert  \quad \text{con }S = D_{g}(f(a)).
$$
2. Por continuidad de $f$ en $a$, existe $\delta>0$ tal que si $\lvert h \rvert<\delta$, entonces $\lVert f(a+h) - f(a) \rVert < \delta_{1}$.T
3. Por diferenciabilidad de $f$, existe $\delta_{2}>0$ tal que si $\lVert h \rVert < \delta_2$ entonces $\lVert f(a+h)-f(a)-T(h) \rVert < \varepsilon \lVert  h \rVert$ con $T=D_{f(a)}$.
4. Por linealidad de $T$, existe $M>0$ tal que $\lVert T(x) \rVert < M \lVert x \rVert$ para todo $x$.

Hay que probar que $D_{g \circ f}(a) = S$. Note que 
$$
\begin{aligned}
\lim_{ h \to 0 } &\frac{\lVert (g \circ f)(a+h) - (g \circ f)(a) - S T (h) \rVert }{\lVert h \rVert } \\
\leq &\lim_{ h \to 0 } \underbrace{ \frac{\lVert g(f(a+h)) - g(f(a)) - S_{0}(f(a+h)-f(a))\rVert }{\lVert h \rVert } }_{ A } \\ + &\lim_{ h \to 0 }\underbrace{ \frac{\lVert S(f(a+h)-f(a)) - S(T(h))\rVert }{\lVert h \rVert } }_{ B }.
\end{aligned}
$$
Note que $B = \left\lVert  S\left( \frac{f(a+h)-f(a) - T(h)}{\lVert  h \rVert} \right)  \right\rVert\underset{h \rightarrow 0}{\longrightarrow} 0$, pues $S$ es continua y el argumento tiende a cero por diferenciabilidad de $f$.
Para $A$, tome $h_{1} = f(a+h)-f(a)$ en la condición (1). Entonces, para $h < \tilde{\delta} < \min \{ \delta, \delta_{1},\delta_{2} \}$, tenemos que 
$$
\begin{aligned}
\frac{\lVert (g(f(a+h))-g(f(a)) - S(f(a+h)-f(a))  \rVert}{\lVert h \rVert } &<  \frac{\varepsilon \lVert f(a+h) - f(a) \rVert}{\lVert h \rVert } \\
&\leq \frac{\varepsilon \lVert f(a+h) - f(a) - T(h) \rVert + \varepsilon \lVert T(h) \rVert}{\lVert h \rVert } \\
& \leq  \frac{\varepsilon^{2} \lVert h \rVert + M \varepsilon \lVert h \rVert}{\lVert h \rVert } = \varepsilon^{2} + M \varepsilon,
\end{aligned}
$$
de donde concluimos que $A \underset{h \rightarrow 0}{\longrightarrow} 0$, de donde concluimos el resultado.

### Teorema (Regla de la cadena y derivadas parciales)
Sea $g=(g_{1},\dots,g_{m}):\mathbb{R}^n\to \mathbb{R}^{m}$ de clase $C^{1}$ en $a$ y $f:\mathbb{R}^{m}\to \mathbb{R}^{p}$ de clase $C^{1}$ rn $g(a)$. Entonces $h = f \circ g:\mathbb{R}^n\to \mathbb{R}^{p}$ es $C^{1}$ en $a$. Además, para $i \in \{ 1,\dots,n \}$, $j \in \{ 1,\dots,p \}$ 
$$
\frac{ \partial h_{j} }{ \partial x_{i} }(a) = \sum_{k=1}^{n} \frac{ \partial f_{j} }{ \partial x_{k} } (g(a)) \cdot \frac{ \partial g_{k} }{ \partial x_{i} } (a).
$$
***Prueba:*** Sabemos que $g$ es diferenciable en $a$ y $f$ es diferenciable en $g(a)$. Así, por el teorema anterior, $h$ es diferenciable en $a$ y $J_{h}(a) =J_{f}(g(a)) J_{g}(a)$. Luego, 
$$
\begin{aligned}
\frac{ \partial h_{j} }{ \partial x_{i} }(a) = (J_{h}(a))_{ji} &= (J_{f}(g(a))J_{g}(a))_{ji}\\
&= \sum_{k=1}^{n} (J_{f}(g(a)))_{jk}(J_{g}(a))_{ki} \\
&= \sum_{k=1}^{n} \frac{ \partial f_{j} }{ \partial x_{k} } (g(a)) \cdot \frac{ \partial g_{k} }{ \partial x_{i} } (a).
\end{aligned}
$$

#### Ejemplo 
Sea $f>\mathbb{R}^{2} \to \mathbb{R}$ de clase $C^{1}$ y $g:\mathbb{R}^{2}\to \mathbb{R}^{2}$ dada por $g(r, \theta) = (r\cos \theta, r \sin \theta)$. En este caso, $h = f \circ g:\mathbb{R}^{2}\to \mathbb{R}$ es $h(r, \theta) = f(g_{1}, g_{2})$, con $g_{1} = r \cos \theta$ y $g_{2} = r \cos \theta$.

Matricialmente 
$$
\begin{aligned}
\begin{bmatrix}
\frac{ \partial h }{ \partial r } \frac{ \partial h }{ \partial \theta }  \\
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
El diagrama de árbol para $f$ y $f_{x}$ es el siguiente:
![[Arbol 1.svg#invert_B]]
La segunda derivada respecto a $r$ viene dada por 
$$
\begin{aligned}
\frac{ \partial^{2} h }{ \partial r^{2} } &= \frac{ \partial }{ \partial r }\left( \frac{ \partial f }{ \partial x } \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial y } \frac{ \partial g_{2} }{ \partial r }  \right)  \\
&= \frac{ \partial  }{ \partial r }\left( \frac{ \partial f }{ \partial x }  \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial x } \frac{ \partial^{2} g_{1} }{ \partial r^{2} } + \frac{ \partial  }{ \partial r }\left( \frac{ \partial f }{ \partial y }  \right) \frac{ \partial g_{2} }{ \partial r } + \frac{ \partial f }{ \partial y } \frac{ \partial^{2} g_{2} }{ \partial r^{2} } \\

&= \left( f_{xx} \frac{ \partial g_{1} }{ \partial r } + f_{xy} \frac{ \partial g_{2} }{ \partial r }   \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial x } \underbrace{ \frac{ \partial^{2} g_{1} }{ \partial r^{2} } }_{ 0 } \\
&  \quad + \left( f_{yx} \frac{ \partial g_{1} }{ \partial r } 
+ f_{yy} \frac{ \partial g_{2} }{ \partial r }   \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial y } \underbrace{ \frac{ \partial^{2} g_{2} }{ \partial r^{2} } }_{ 0 } \\
&=f_{xx} \cos^{2} \theta + 2f_{xy} \sin \theta \cos \theta + f_{yy} \sin^{2} \theta \\
&=D_{11}f(r \cos \theta, r\sin \theta) \cos ^{2} \theta+ 2 D_{12} f(r \cos \theta, r \sin \theta) \sin \theta \cos \theta \\
&  \quad+ D_{22} f(r \cos \theta, r \sin \theta) \sin ^{2} \theta
\end{aligned}
$$

#### Ejemplo 
Sean $f:\mathbb{R}^{3}\to \mathbb{R}$, $g,h: \mathbb{R}^{2}\to \mathbb{R}$, $w:\mathbb{R}^{3}\to \mathbb{R}$ con 
$$
w(x,y,z) = f(g(x,z),h(g(x,z),y),z) = f(u,v,z)
$$
con $u=g(x,z)$, $v=h(r,y)$ y $r = g(x,z)$. Si $h = f \circ g \implies J_{h}(a) = J_{f}(g(a)) \cdot J_{g}(a)$.
![[Arbol 2.svg#invert_B]]
Calculando las derivadas parciales de orden 1: 
$$
\begin{aligned}
\frac{ \partial w }{ \partial y } &= \frac{ \partial f }{ \partial v} \cdot \frac{ \partial h }{ \partial y }  \\
\frac{ \partial w }{ \partial x } &= \frac{ \partial f }{ \partial u } \cdot \frac{ \partial g }{ \partial x } +  \frac{ \partial f }{ \partial v } \cdot \frac{ \partial h }{ \partial r } \cdot \frac{ \partial g }{ \partial x } \\
\frac{ \partial w }{ \partial z } &= \frac{ \partial f }{ \partial u } \cdot \frac{ \partial g }{ \partial z }  + \frac{ \partial f }{ \partial v } \cdot \frac{ \partial h }{ \partial r } \cdot \frac{ \partial g }{ \partial z }.
\end{aligned}
$$

## Desarrollos de Taylor
Generalización de [[Series de funciones#Series de Taylor|Taylor en una variable]] (MA0350). Sea $f \in C^{n+1}(V)$, $V$ vecindario de $a$. Entonces, el desarrollo de Taylor de $f$ viene dado por: 
$$
f(x)  = f(a) + f'(a)(x-a) + \dots \frac{f^{(n)}(a)}{n!}(x-a)^{n} + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n}
$$
con $\xi$ entre $x$ y $a$. ¿Se puede generalizar esto a funciones de varias variables? 

### Teorema (Taylor)
Sea $f:D \to \mathbb{R}$, $f \in C^{d+1}(D)$, $D \subseteq \mathbb{R}^n$, $D$ abierto y conexo. Para $a \in D$, existe $\delta>0$ tal que para todo $x \in B_{\delta}(a)$ se tiene que 
$$
\begin{aligned}
f(x) &= f(a) + \sum_{j=1}^{n} D_{j} f(a) \cdot (x_{j}-a_{j}) + \frac{1}{2!} \sum_{j_{1}=1}^{n} \sum_{j_{2}=1}^{n} D_{j_{1},j_{2}} f(a) (x_{j_{1}} - a_{j_{1}})(x_{j_{2}} - a_{j_{2}}) \\
&+ \frac{1}{3!} \sum_{j_{1},j_{2},j_{3}=1}^{n} D_{j_{1},j_{2}, j_{3}} f(a) (x_{j_{1}} - a_{j_{1}})(x_{j_{2}} - a_{j_{2}})(x_{j_{3}} - a_{j_{3}}) + \dots \\
&+ \frac{1}{d!} \sum_{j_{1},\dots,j_{d} = 1} D_{{j_{1},\dots,j_{d}}}f(a)(x_{j_{1}}-a_{j_{1}})\dots(x_{j_{d}}-a_{j_{d}}) + \\
&+ \frac{1}{(d+1)!} \sum_{j_{1},\dots,j_{d+1} = 1} D_{{j_{1},\dots,j_{d},j_{d+1}}}f(\xi)(x_{j_{1}}-a_{j_{1}})\dots(x_{j_{d}}-a_{j_{d}})(x_{j_{d+1}}-a_{j_{d+1}}),
\end{aligned}
$$
con $\xi$ en el segmento que une $a$ y $x$.
#### Nota
Defina el Hessiano de $f$ en $a$ como la matriz de segundas derivadas, i.e., 
$$
H_{f}(a) = \begin{pmatrix}
D_{11}f(a) & D_{12}f(a) & \dots & D_{1n}f(a) \\
D_{21}f(a) & D_{22}f(a) & \dots & D_{2n}f(a) \\
\vdots & \vdots & \ddots & \vdots \\
D_{n1}f(a) & D_{n_{2}}f(a) & \dots & D_{nn}f(a) 
\end{pmatrix}_{n \times n}.
$$
Esta matriz es simétrica si $f \in C^{2}(D)$. El término de orden 2 del teorema de Taylor puede ser escrito convenientemente como 
$$
(x-a)^{T}_{} H_{f}(a) (x-a).
$$

***Prueba:*** Sea $a \in D$. Tome $B_{\delta}(a) \subseteq D$. Para $x \in B_{\delta}(a)$, defina $g:[0,1] \to \mathbb{R}$ con $g(t) = f(\underbrace{ a+t(x-a) }_{ \in \mathbb{R}^n }) \in \mathbb{R}$. Intuitivamente, esta función genera cualquier punto en el segmento entre $a$ y $x$. Note que $g \in C^{d+1}$, luego aplica el teorema de Taylor en una variable, por tanto 
$$
g(1) = g(0) + g'(0)t + \frac{g''(0)}{2!}t^{2}+\dots + \frac{g^{(d)}(0)}{d!}t^{d} + \frac{g^{(d+1)}(0)}{(d+1)!}t^{d+1}.$$
Note ahora que, $g(1) = f(x), g(0) = f(a)$. Sea $v_{i} = a_{i}+t(x_{i} - a_{i})$. Desarrollando para las derivadas con regla de la cadena
$$
\begin{aligned}
g(t) &= f(a+t(x-a)) = f\big(a_{1}+t(x_{1}-a_{1}), \dots, a_{n}+t(x_{n}-a_{n})\big)\\
\implies g'(t) &= \frac{ \partial f }{ \partial v_{1} } \cdot \frac{ \partial v_{1} }{ \partial t } + \frac{ \partial f }{ \partial v_{2} } \cdot \frac{ \partial v_{2} }{ \partial t } + \dots + \frac{ \partial f }{ \partial v_{n} } \cdot \frac{ \partial v_{n} }{ \partial t }  \\
&= \sum_{j=1}^{n} D_{1}f(v_{1}) (x_{j}-a_{j}) = \sum_{j=1}^{n} D_{1}f(a) (x_{j}-a_{j}).
\end{aligned}
$$
Podemos proceder de manera análoga, e inductivamente para términos de orden superior.
Finalmente, para el resto tome $\xi= a + \lambda(x-a)$.

## Máximos y mínimos
Recordemos:
1. Si $c \in D^{0}$ es extremo relativo, $\nabla f(c) = 0$.
2. $f:K \subseteq \mathbb{R}^n \to \mathbb{R}$, $K$ compacto. $f$ tiene máximo y mínimo absolutos.

### Definición (Punto crítico)
Dada $f:D \subseteq \mathbb{R}^n \to \mathbb{R}$, decimos que $c$ es un punto crítico si $f$ no es diferenciable en $c$ o si $\nabla f(c) = 0$. 
#### Nota
Recuerde que ser un punto crítico no implica ser extremo relativo. Por ejemplo, $f:\mathbb{R} \to \mathbb{R}$ con $f(x)=x^{3}$ tiene un punto crítico en $0$ pero no es extremo relativo. También, $f:\mathbb{R}^{2} \to \mathbb{R}$ con $f(x,y) = x^{2}-y^{2}$.  Se puede verificar que $\nabla f(0,0) = 0$ pero $(0,0)$ es un punto silla. Tenemos que $f(x,0) =x^{2}\geq 0 = f(0,0)$ y $f(0,y) = -y^{2} \leq 0 = f(0,0)$.

### Definición (Máximos, mínimos y puntos silla)
Dada $f:A \subseteq \mathbb{R}^n \to \mathbb{R}$, con $A$ abierto y $x_{0} \in A$:
1. $f(x_{0})$ es máximo (<font color="#fbd5b5">mínimo</font>) local en $A$ si existe $\rho>0$ tal que $f(x) \leq f(x_{0})$ <font color="#fbd5b5">(</font>$f(x_{0}) \leq f(x)$<font color="#fbd5b5">)</font>
2. El punto crítico es global si la desigualdad se cumple para todo $x \in A$.
3. $f(x_{0})$ es punto silla si $\nabla f(x_{0})$ y para todo $r>0$ con $B_{r(x)} \subseteq A$ existen $x_{1}, x_{2} \in B_{r}(x)$ tales que $f(x_{1}) < f(x_{0}) < f(x_{2})$.

### Definición (Matrices def. y semidef. positiva y negativa)
Sea $A \in \mathbb{R}^{n \times n}$ una matriz simétrica. Decimos que $A$ es:
1. definida positiva si para todo $0 \neq x \in \mathbb{R}^n$$, x^{T}Ax > 0$;
2. semidefinida positiva si para todo $0 \neq x \in \mathbb{R}^n$$, x^{T}Ax \geq 0$;
3. definida negativa si para todo $0 \neq x \in \mathbb{R}^n$$, x^{T}Ax < 0$;
4. semidefinida positiva si para todo $0 \neq x \in \mathbb{R}^n$$, x^{T}Ax \leq 0$;
5. indefinida si existen $0 \neq x_{1},x_{2} \in \mathbb{R}^n$ tales que $x_{1}^{T}Ax_{1}>0$ y $x_{2}^{T} A x_{2} < 0$.

### Teorema (Criterio del Hessiano)
Dada $f:D \subseteq \mathbb{R}^n\to \mathbb{R}$, $f \in C^{2}(D)$, defina la matriz hessiana como 
$$
H_{f} = \begin{bmatrix}
D_{11}f & \dots &  D_{1n}f  \\
\vdots & \ddots & \vdots \\
D_{n_{1}}f & \dots & D_{nn}g
\end{bmatrix}.
$$
Si $\nabla f(c) = 0$ ($c$ es punto crítico), entonces
1. hay mínimo relativo en $c$ si $H_{f}(c)$ es definida positiva;
2. hay máximo relativo en $c$ si $H_{f}(c)$ es definida negativa;
3. hay punto silla relativo en $c$ si $H_{f}(c)$ es indefinida;
4. en otro caso, el criterio no decide.

***Prueba:*** Por teorema de Taylor, para $x \in B_{\delta}(c)$ con $\delta>0$:
$$
\begin{aligned}
f(x) &= f(c) + \nabla f(c) (x-c) + \frac{1}{2} (x-c)^{T} H_{f}(\xi) (x-c)\\
f(x) - f(c) &= \frac{1}{2} (x-c)^{T} H_{f}(\xi) (x-c).
\end{aligned}
$$
Como $f \in C^{2}(D)$, por continuidad, si $(x-c)^{T} H_{f}(c)(x-c)>0$, entonces existe $\alpha > 0$ tal que $(x-c)^{T} H_{f}(\xi) (x-c) > 0$ si $\lVert x-c \rVert < \alpha$, pues $\xi$ está en el segmento que une $c$ y $x$. Concluimos que $f(x) - f(c) > 0$ para todo $x \in B_{\alpha}(c)$, de donde concluimos que $f(c)$ es un mínimo relativo. (los otros casos son análogos).

### Teorema (Caracterización de matrices def. y semidef. positivas y negativas)
Las siguientes son equivalentes
1. $A$ es definida positiva <font color="#fbd5b5">(negativa)</font>
2. Los valores propios de $A$ son todos positivos<font color="#fbd5b5"> (negativos)</font>
3. Los determinantes de los menores principales son todos positivos <font color="#fbd5b5">(alternan -,+,-,+,...)</font>.
Además, las siguientes son equivalentes sobre matrices indefinidas
4. $A$ es indefinida.
5. $A$ tiene valores propios negativos y positivos.
 
#### Ejemplo 
Considere $f(x,y) = x^{3}-3xy^{2}+y^{2}$. Primero, encontramos los puntos críticos.

Note que $\nabla f(x,y) = (3x^{2}-3y^{2}, -6xy+2y) = (0,0)$
$$
\implies \begin{cases}
x ^{2} = y^{2}  \\
-3xy+y=0
\end{cases}.
$$
Tenemos $(0,0), \left( \frac{1}{3}, \frac{1}{3} \right), \left( \frac{1}{3}, -\frac{1}{3} \right)$ como puntos críticos. El hessiano de $f$ es 
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
\end{bmatrix} \implies \Delta_{1} = 2 > 0, \ \Delta_{2} = -4 <0  \quad \text{(indefinda)}.
\end{aligned}
$$
Para el punto $(0,0)$, usamos la definición de semidefinida positiva (pues los determinantes de los menores son todos cero y el criterio en esta forma no decide). Note que $(x,y)H_{f}(0,0) (x,y)^{T} = 2y^{2} \geq 0$, por lo que $f(x,y) - f(0,0) \geq 0$ cerca de $(0,0)$ y por tanto $(0,0)$ es mínimo local.

**Ver más ejemplos en las notas de clase**

## Diferenciación de inversas y función implícita

#### Ejemplo 
Si $f:\mathbb{R}\to \mathbb{R}$ es invertible, sabemos que para $g=f^{-1}$, $g(f(x))= x$. Por regla de la cadena, $g'(f(x)) f'(x) = 1$ y así $g'(y)=\frac{1}{f'(f^{-1}(y))}$, donde $y = f^{-1}(x)$ y $f'(x) \neq 0$.

#### Ejemplo 
Para calcular $g'$ para $g(x)=\arcsin x \in \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$. Sabemos que $\sin(g(x)) = 1$ y entonces $\cos(g(x)) g'(x) = 1$. Así 
$$
g'(x) = \frac{1}{\cos(g(x))} = \frac{1}{\sqrt{ 1 - \sin^{2}(g(x)) }} = \frac{1}{\sqrt{ 1-x^{2} }}.
$$
Basta saber que $(\sin x)' = \cos x \neq 0$ para todo $x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$ para saber que es localmente invertible.

### Teorema (Función inversa)
Sea $f:A \subseteq \mathbb{R}^n \to \mathbb{R}^n$,  $f \in C_{1}(A)$ con $A$ abierto. Sea $a \in A$ con $\det J_{f}(a) \neq 0$. Entonces:
1. existen $V,W  \subseteq\mathbb{R}^n$ abiertos tales que $a \in V$, $f(a) \in W$ $f:V\to W$ es invertible con $f^{-1}:W\to V$ diferenciable.
2. $J_{f^{-1}}(y)= [J_{f}(f^{-1}(y))]^{-1}$ para todo $y \in W$.

***Prueba:*** Video complementario

**Ver ejemplos en las notas de clase**

### Teorema (Función implícita)
Sea $f:\mathbb{R}^n \times \mathbb{R}^{m} \to \mathbb{R}^{m}$ de clase $C_{1}$ en un abierto que contiene a $(a,b)$, con $a \in \mathbb{R}^n$, $b \in \mathbb{R}^{m}$, $f(a,b)=0$. Sea $M \in \mathbb{R}^{m \times m}$ con $M_{ij} = D_{n+j}f_{i}$, $1\leq i,j\leq m$. Si $\det M(a,b) \neq 0$, existen $A \subseteq \mathbb{R}^n$, $B \subseteq \mathbb{R}^{m}$ con $a \in A$, $b \in B$ tales que 
$$
\forall x \in A  \quad \exists ! y \in B  \quad (f(x,y)=0).
$$
Esto es, existe $g :A\to B$ con $f(x, g(x)) = 0$. Además, $g$ es diferenciable en $A$ y $J_{g}(x) = -[M(x,y)]^{-1}[D_{j}f_{i}]_{1\leq i\leq m, \hspace{1mm} 1\leq j\leq n}$.

***Idea de la prueba:*** 
Podemos escribir el jacobiano de $f$ como
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
Sea $h:\mathbb{R}^n \to \mathbb{R}^{n+m}$ con $h(x) = (x,g(x))$, tenemos que $J_{h} = \begin{bmatrix}I_{n\times n} \\ J_{g}\end{bmatrix}$. Como $f \circ h = 0$,  tenemos que 
$$
0 = \begin{bmatrix}
N & M
\end{bmatrix} \begin{bmatrix}
I \\
J_{g}
\end{bmatrix} = N+MJ_{g} \implies J_{g} = -M^{-1}N.
$$
#### Ejemplo 
Considere la región definida por $x^{2}+y^{2} = 1$. Localmente, se puede definir una función alrededor de cualquier punto excepto $(-1,0)$ y $(1,0)$, en donde ya no es función pues tenemos dos imágenes para una misma preimagen. Podemos derivar implícitamente respecto a $y$, pensando $y = y(x)$ como una función de $x$.

#### Caso particular 
Para $n=m=1$,  tenemos $f:\mathbb{R} \times \mathbb{R} \to \mathbb{R}$, entonces $N = \frac{ \partial f }{ \partial x }$ y $M = \frac{ \partial f }{ \partial y }$. Si $\det\left( \frac{ \partial f }{ \partial y } \right) \neq 0$, $\frac{dy}{dx} = -\frac{\frac{ \partial f }{ \partial x }}{\frac{ \partial f }{ \partial y }}$.

#### Ejemplo
Considere $f(x,y) = \ln x+2\ln y+xy-1$, $(a,b)=(1,1)$. Tome $(a,b)=(1,1)$.Note que $f(1,1) = 0$ y que $M = \frac{2}{y} + x \implies M(1,1) = 3 \neq 0$.  Por teorema de la función implícita, existen $A,B$ subconjuntos abiertos de $\mathbb{R}$, con $1 \in A$, $1 \in B$ tal que $f(x,g(x)) = 0$.

**Ver más ejemplos en las notas de clase**

## Consideraciones finales

### Derivada direccional y gradiente

Dado $u \in \mathbb{R}^n$ con $\lVert u \rVert_{2} = 1$, $f:\mathbb{R}^n\to \mathbb{R}$, entonces 
$$
\begin{aligned}
\lvert D_{u} f(x_{0}) \rvert &= \lvert \nabla f(x_{0}) \cdot u \rvert \\
&= \lVert \nabla f(x_{0}) \rVert \cdot \lVert u \rVert \lvert \cos \theta \rvert = \lVert \nabla f(x_{0}) \rVert \cdot \lvert \cos \theta \rvert  \\
&\leq  \lVert \nabla f(x_{0}) \rVert,
\end{aligned}
$$
donde $\theta$ es el ángulo entre $\nabla f(x_{0})$ y $u$. Si $u, \nabla f(x_{0})$ son paralelos, se cumple la igualdad, pues $\theta = 0 \implies \cos \theta = 1$.

Si tomo $u = \frac{\nabla f(x_{0})}{\lVert \nabla f(x_{0} \rVert}$, $D_{u} f(x_{0})$ es máximo, i.e., $\nabla f(x_{0})$ es la dirección de mayor cambio vertical en $x_{0}$.

### Diferenciales de orden superior.

Dados $f:A \subseteq \mathbb{R}^n \to \mathbb{R}$, definimos $D_{f}(x_{0}):\mathbb{R}^n\to \mathbb{R}^{m}$. Así, $D_{f}(x_{0})(h) \in \mathbb{R} \in R$. Es posible escribir $D_{f}: A \to \mathcal{L}(\mathbb{R}^n, \mathbb{R}^{m})$. Vimos que $D_{f}(x)$ tiene como matriz asociada a $J_{f}(x)$. Así, 
$$
D_{f}(x_{0}) (h) = J_{f}(x_{0}) h = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} } (x_{0}) h_{i}.
$$
Tiene sentido definir $D(D_{f}(x_{0}))$ si $f \in C^{2}(A)$.

Si $x = (x_{1},\dots,x_{n})$, es usual definir proyecciones $dx_{i}:\mathbb{R}^n\to \mathbb{R}$ que $dx_{i}(x) = x_{i}$. Así, $D_{f}(x_{0}) = \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}$. Evaluando, $D_{f}(x_{0})(h) = \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}(h)$. Así 
$$
\begin{aligned}
\implies D(D_{f}(x_{0})) &= \sum_{j=1}^{n} \frac{ \partial }{ \partial x_{j} }(D_{f}(x_{0})) dx_{j} \\
&= \sum_{j=1}^{n} \frac{ \partial }{ \partial x_{j} } \left( \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}(h) \right) dx_{j} \\
&= \sum_{i,j=1}^{n} \frac{ \partial^{2} f }{ \partial x_{j} \partial x_{i} }  dx_{i} dx_{j}, \quad \text{con } dx_{i} dx_{j}: \mathbb{R}^n \times \mathbb{R}^n \\
\implies D_{f}^{2}(x_{0})(u,v) &= \sum_{i,j=1}^{n} \frac{ \partial^{2} f }{ \partial x_{j} \partial x_{i} }(x_{0}) u_{i} v_{j} \quad= u^{T} H v.
\end{aligned}
$$

### Definición (Diferencial de orden superior)
Sea $B_{2}(\mathbb{R}^n,\mathbb{R}) = \{ f:D\to \mathbb{R} \text{ bilineales}\}$, con $D = \{ (x,x): x \in \mathbb{R}^n \}$. Se define $D^{2}f:A \subseteq \mathbb{R}^n \to B_{2}(\mathbb{R}^n, \mathbb{R})$ por
$$
(D^{2}f(x_{0}))(x) = x^{T} H_{f}(x_{0}) x = \sum_{i,j=1}^{n} x_{i} x_{j} \frac{ \partial f }{ \partial x_{i} \partial x_{j} }.
$$
Análogamente, $D^{3}f:A \subseteq \mathbb{R}^n \to B_{3}(\mathbb{R}^{m}, \mathbb{R})$ dado por 
$$
(D^{2}f(x_{0}))(x) = \sum_{i,j,k=1}^{n} x_{i} x_{j} x_{k} f_{x_{k}x_{j}x_{i}}(x_{0}), 
$$
donde $B_{3}$ es el conjunto de las funciones trilineales restrictas $(x,x,x)$ con $x \in \mathbb{R}^n$.

#### Nota 
Taylor se puede rescribir como 
$$
f(x) = f(x_{0}) + \sum_{k=1}^{p} \frac{1}{k!} (D^{k}_{f}(x_{0}))(x-x_{0}) + \frac{1}{(p+1)!}(D^{p+1}_{f}(\xi))(x-x_{0}).
$$
**Ver  ejemplos en las notas**
