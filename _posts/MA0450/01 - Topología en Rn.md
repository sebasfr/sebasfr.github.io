# Topología en $\mathbb{R}^{n}$

#Mate #MA0450
Fecha:  2025-08-11
Ver también: [[Funciones de varias variables]], [[Diferenciación]], [[Integración en Rn]], [[Cálculo vectorial]].
Generaliza conceptos de: [[Sucesiones]] (MA0350), [[Subsucesiones]] (MA0350).

## Preliminares
### Definición ($\mathbb{R}^{n}$)
$$
\begin{aligned}
\mathbb{R}^{n} :&= \mathbb{R} \times \mathbb{R} \times \dots \times \mathbb{R} \\
&= \{ (x_{1},x_{2},\dots,x_{n}): x_{i} \in \mathbb{R} \quad  \forall 1 \leq i \leq  n \}
\end{aligned}
$$
Escribimos $\bar{x} = (x_{1},\dots,x_{n}) \in \mathbb{R}^{n}$. Tenemos dos operaciones, de modo que se define un espacio vectorial: 
$$
\begin{aligned}
\bar{x} + \bar{y} &= (x_{1}+y_{1},\dots,x_{n}+y_{n}) \\
\alpha \bar{x} &= (\alpha x_{1}, \dots, \alpha x_{n}).
\end{aligned}
$$

### Definición (Norma)
Dado un espacio vectioral $E$ sobre $\mathbb{R}$, una norma es una operación $\lVert \cdot \rVert: E \to \mathbb{R}$ tal que 
1. $\forall x \in E \quad (\lVert x \rVert \geq 0  \quad \land  \quad \lVert x \rVert = 0 \iff x=0)$.
2.  $\forall x \in E \quad \forall \alpha \in \mathbb{R} \quad  (\lVert \alpha x \rVert = \lvert \alpha \rvert \lVert x \rVert)$.
3. $\forall x,y \in E \quad (\lVert x+y \rVert \leq \lVert x \rVert+ \lVert y \rVert)$.

#### Ejemplo 
En $\mathbb{R}$ el valor absoluto es una norma.

### Definición (Espacio vectorial normado)
Un E.V. con norma $\lVert \cdot \rVert$ se llama E.V. normado y se denota $(E, \lVert \cdot \rVert)$.

### Definición (Producto escalar)
Dado un e.v. $E$ sobre $\mathbb{R}$, un producto escalar es una aplicación $\langle \cdot,\cdot \rangle : E \times E \to \mathbb{R}$ tal que 
1. $\langle x, y \rangle = \langle y, x \rangle$.
2. $\langle x, y_{1}+y_{2} \rangle = \langle x, y_{1}\rangle +  \langle x, y_{2}\rangle$.
3. $\langle x, \lambda y \rangle = \lambda \langle x, y \rangle \quad \forall \lambda \in \mathbb{R}$.
4. $\langle x, x \rangle \geq 0$ y si $x \neq 0$ entonces $\langle x, x \rangle > 0$.

#### Observación 1
$$
\begin{aligned}
\langle x_{1}+x_{2},y \rangle &= \langle y, x_{1}+x_{2} \rangle  \\
&= \langle y, x_{1} \rangle + \langle y,x_{2} \rangle \\
&= \langle x_{1},y \rangle + \langle x_{2},y \rangle.
\end{aligned}
$$

#### Observación 2
$$
\langle 0,0+0 \rangle = \langle 0,0 \rangle + \langle 0,0 \rangle \implies \langle 0,0 \rangle = 0.
$$

#### Ejemplo 
En $\mathbb{R}^{n}$, $\langle x,y \rangle = x \cdot y = \sum_{i=1}^{n} x_{i} y_{i}$ es un producto escalar (ejercicio).

### Lema (Cauchy-Schwartz)
Para todos $x, y \in E$, se tiene que $\langle x,y \rangle^{2} \leq \langle x,x \rangle \cdot \langle y,y \rangle$.

***Prueba:*** Por la propiedad 3 del producto escalar, tenemos que para todo $\lambda \in \mathbb{R}$
$$
\begin{aligned}
0 &\leq \langle x+\lambda y, x + \lambda y \rangle \\
&= \langle x,x \rangle + 2 \lambda \langle x,y \rangle + \lambda^{2} \langle y,y \rangle = f(\lambda).
\end{aligned}
$$
Note que $f(\lambda)$ es cuadrática y su discriminante necesariamente es menor o igual que cero (por la propiedad 4 de l producto escalar). El discriminante viene dado por 
$$
4 \langle x,y \rangle^{2} - 4 \langle x,x \rangle \langle y,y \rangle \leq  0
\iff \langle x,y \rangle^{2} \leq \langle x,x \rangle \langle y,y \rangle. 
$$
 
#### Ejemplo (Norma 2)
Dado un producto escalar $\langle \cdot, \cdot \rangle$,  $\lVert x \rVert = \sqrt{ \langle x,x \rangle }$ es una norma.

***Prueba:*** Probaremos cada propiedad
1. $\lVert x \rVert\geq 0$ y $\lVert x \rVert = 0 \iff \langle x,x \rangle = 0 \iff x=0$. 
2. $\lVert \lambda x \rVert = \sqrt{ \langle \lambda x, \lambda x \rangle } = \sqrt{ \lambda^{2} \langle x, x \rangle } = \lvert \lambda \rvert \lVert x \rVert$.
3. $$
\begin{aligned}
\lVert x+y \rVert^{2} &= \langle x+y, x+y\rangle \\
&= \langle x,x \rangle + 2 \langle x,y \rangle + \langle y,y \rangle  \\
&= \lVert x \rVert^{2}+ 2 \langle x,y \rangle  + \lVert y \rVert^{2} \\
&\leq_{C.S.} \lVert x \rVert^{2}+2 \lVert x \rVert \lVert y \rVert + \lVert y \rVert^{2} \\
&= ( \lVert x \rVert + \lVert y \rVert)^{2}.
\end{aligned}
$$
	Todo producto escalar induce a una norma.

#### Observación
En $\mathbb{R}^{n}$, con $\langle x,y \rangle = \sum_{i=1}^{n} x_{i} y_{i}$, 
$$
\lVert x \rVert = \sqrt{ \langle x,x \rangle  } = \sqrt{ \sum_{i=1}^{n} x_{i}^{2} } = \lVert x \rVert_{2}
$$
![[attachments/norma.svg#invert_B]]
#### Ejemplo 
En $\mathbb{R}^{n}$, dado $x = (x_{1},..., x_{n})$, las siguientes son normas:
1. $\lVert x \rVert_{1} := \sum_{i=1}^{n} \lvert x_{i} \rvert$,
2. $\lVert x \rVert_{\infty} := \underset{1\leq j\leq n}{\max} \lvert x_{j} \rvert$
3.  $\lVert x \rVert_{p} := \left\lvert  \sum_{i=1}^{n} \lvert x_{i}^{p} \rvert  \right\rvert^{1/p}$.
Por convención, en el curso se usará la norma 2 al menos de que se indique lo contrario.
### Definición (Normas equivalentes)
Dadas $\lVert \cdot \rVert_{a}$ y $\lVert \cdot \rVert_{b}$ normas, se dicen equivalentes si existen $\alpha, \beta >0$ tales que para todo $x \in E$, 
$$
\alpha \lVert x \rVert_{a} \leq \lVert x \rVert_{b} \leq  \beta \lVert x \rVert_{a}.
$$

#### Ejemplo 
$$
\begin{aligned}
\lVert x \rVert_{2} &\leq \lVert x\rVert_{1} \leq  \sqrt{ n } \lVert x \rVert_{2} \\
\lVert x \rVert_{\infty} &\leq \lVert x \rVert_{2} \leq  \sqrt{ n } \lVert x \rVert_{\infty} \\
\lVert x \rVert_{\infty} &\leq \lVert x \rVert_{1} \leq  n \lVert x \rVert_{\infty} 
\end{aligned}
$$

#### Ejemplo 
Cada norma define una geometría distinta: 
1. $B_{2} = \{ x \in \mathbb{R}^{2}: \lVert x \rVert_{2} = 1\}$
![[Norma2.svg#invert_B]]
2.  $B_{1} = \{ x \in \mathbb{R}^{2}: \lVert x \rVert_{1} = 1\}$
![[Norma1.svg#invert_B]]
3.  $B_{\infty} = \{ x \in \mathbb{R}^{2}: \lVert x \rVert_{\infty} = 1\}$
![[NormaInf.svg#invert_B]]

#### Ejemplo 
En $E = C([a,b], \mathbb{R})$, $\langle f,g \rangle = \int_{a}^{b} f(x)g(x) \, dx$ es un producto escalar y tiene norma inducida $\lVert f \rVert = \sqrt{ \langle f,f \rangle } = \sqrt{ \int_{a}^{b} \lvert f \rvert^{2} \, dx }$.

### Lema (Ley del paralelogramo)
En un e.v. con producto escalar, la norma inducida satisface 
$$
\lVert x+y \rVert^{2} + \lVert x-y \rVert^{2} = 2 \lVert x \rVert^{2}+2 \lVert y \rVert^{2} \ \tag{*}
$$
***Prueba:*** Ejercicio.

#### Nota
En un e.v. normado, no necesariamente existe un producto escalar asociado a cada norma.

### Lema (Producto escalar a partir de una norma) 
En un e.v. normado, se puede definir $\langle \cdot, \cdot \rangle$ a partir de $\lVert \cdot \rVert$ si y solo si  se cumple la ley del paralelogramo. En este caso, 
$$
\langle x,y \rangle = \frac{1}{4}[ \lVert x+y \rVert^{2} - \lVert x-y \rVert^{2} ].
$$

#### Ejemplo 
$\lVert x \rVert_{\infty}$ en $\mathbb{R}^{n}$ no cumple $(*)$.

### Definición (Distancia)
Una distancia es una función $d(\cdot,\cdot): E \times E \to \mathbb{R}$ tal que 
1. $d(x,y) = 0 \iff x=y$,
2. $d(x,y) = d(y,x)$
3. $d(x,z) \leq d(x,y) + d(y,z)$.

#### Nota
Toda norma induce la distancia $d(x,y) = \lVert x-y \rVert$. En $\mathbb{R}^{n}$, la distancia viene dada por 
$$d(x,y) = \lVert x-y \rVert_{2} = \left( \sum_{i=1}^{n} (x_{i} - y_{i})^{2} \right)^{1/2}.$$

## Abiertos y cerrados (en $\mathbb{R}^{n}$)
 
### Definición (Bola abierta y cerrada)
Dado $a \in \mathbb{R}^{n}, r \in \mathbb{R}$:
1. Se llama bola abierta de centro $a$ y radio $r$ a 
$$
B_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a \rVert < r \}
$$
2. y bola cerrada de centro $a$ y radio $r$ a
$$
\bar{B}_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a \rVert \leq  r \}.
$$
#### Ejemplo 
![[intervalo.svg#invert_B]]
En $\mathbb{R}$ cualquier intervalo $(c,d)$ es una bola abierta, tomando $a = \frac{c+d}{2}, r= \frac{d-c}{2} >0$, pues 
$$
\lvert x-a \rvert < r \iff a-r = c < x < d = a+r.
$$
De manera análoga, todo intervalo $[c,d]$ es una bola cerrada.

#### Ejemplo
1. En $\mathbb{R}^{2}$:
![[bola R2.svg#invert_B]]

2. En $\mathbb{R}^{3}$:
![[bola R3.svg]]
### Definición (punto interior y conjunto abierto)
Dado un conjunto $A \subseteq \mathbb{R}^{n}$,
1. se dice que $a \in A$ es un punto interior de $A$, si existe una bola $B_{\delta}(x)$ con $a \in B_{\delta}(x)$ tal que $B_{\delta}(x) \subseteq A$,
2. se define $A^{0} = \{ a \in A: a \text{ es punto interior} \}$,
3. $A$ es abierto si $A = A^{0}$, i.e., si  
$$
\forall x \in A  \quad \exists \delta>0  \quad(B_{\delta}(x) \subseteq A)
$$
![[conjunto abierto.svg#invert_B]]

#### Ejemplo 
$A = (0,1)$ es abierto en $\mathbb{R}$ pero $A = [0,1)$ no. (dibujar)

### Lema (Bola abierta $\implies$ conjunto abierto)
Toda bola abierta $B_{r}(a)$ es un conjunto abierto.

***Prueba:*** Sea $x \in B_{r}(a)$. Tome $0 < \delta < r - \lVert x-a \rVert$. Sabemos que $\lVert x-a \rVert < r$. 
Veamos que $B_{\delta}(x) \subseteq B_{r}(a)$. Sea $y \in B_{\delta}(x)$, entonces $\lVert x-y \rVert < \delta$. Hay que mostrar que $y \in B_{r}(a)$, i.e.,  $\lVert y-a \rVert < r$. Note que 
$$
\begin{aligned}
\lVert y-a \rVert &\leq \lVert y-x \rVert + \lVert x-a \rVert \\
&< \delta + (r-\delta) = r.
\end{aligned}
$$
![[bola es conjunto abierto.svg#invert_B]]

### Definición (conjunto cerrado)
Un conjunto $F \subseteq \mathbb{R}^{n}$ se llama cerrado si $F^{C}$ es abierto.
 
#### Ejemplo
Note que $\mathbb{R}^{n}$ es abierto, pues si $x \in \mathbb{R}^{n}$, tome $-$ y así $B_{\delta}(x) \subseteq \mathbb{R}^{n}$. $\mathbb{R}^{n}$ es también cerrado, pues $(\mathbb{R}^{n})^{C} = \emptyset$ es abierto por vacuidad. Luego $\mathbb{R}^{n}$ y  $\emptyset$ son ambos abiertos y cerrados (*clopen*).

#### Ejemplo 
$A = [0,1)$ no es abierto pues $0$ no es punto interior. Además no es cerrado, pues su complemento $(-\infty, 0) \cup  [1,\infty)$ no es abierto (considere $x=1$). 

#### Ejemplo 
Una bola cerrada $\bar{B}_{r}(a)$ es un conjunto cerrado.
Recordemos que $\bar{B}_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a \rVert \leq r \}$. Sea $x \in (\bar{B}_{r}(a))^{C}$. Tome $0<\delta< \lVert x-a \rVert-r$ (tiene sentido pues $\lVert x-a \rVert>r$).
Sea $y \in B_{\delta}(x)$. Hay que mostrar que $y \in (\bar{B}_{r}(a))^{C}$ . Como 
$$
\begin{aligned}
\delta + r < \lVert x-a \rVert &\leq \lVert x-y \rVert + \lVert y-a \rVert \\
& < \delta + \lVert y-a \rVert 
\end{aligned}
$$
entonces $r < \lVert y-a \rVert$, de donde se concluye que $y \not\in \bar{B}_{r}(a)$.
![[bola cerrada es cerrado.svg#invert_B]]
### Definición (Punto exterior y punto frontera)
1. Se dice que $x$ es punto exterior de $A$ si es un punto interior de $A^{C}$, es decir, el conjunto de puntos exteriores es $(A^{C})^{0}$.
2. $x$ es punto frontera si 
$$
\forall \delta > 0  \quad(B_{\delta}(x) \cap A \neq  \emptyset  \quad\land  \quad B_{\delta}(x) \cap A^{C} \neq  \emptyset).
$$
Se denota $\partial A = \{ \text{puntos frontera de }A \}$.
![[ext front int.svg#invert_B ]]

#### Ejemplo 
$A = [0,1)$ no es abierto (pues si $x=0$, no existe $\delta>0$ tal que $B_{\delta}(0) \subseteq A$. Note que 
$$
A^{0} = (0,1), \quad \partial A = \{ 0,1 \}, \quad (A^{C})^{0} = (-\infty,0) \cap(1,+\infty).
$$

#### Ejemplo 
Dados $a \in \mathbb{R}^{n}$, $r>0$, $\partial B_{r}(a) = \{ x \in \mathbb{R}^{n}: \lVert x-a = r\rVert \}$.
***Prueba:*** "$\supseteq$" Sea $x \in \mathbb{R}^{n}$ tal que $\lVert x-a \rVert=r$. Veamos que $x \in \partial B_{r}(a)$. Sea $\delta>0$.
1. Encontramos $z \in B_{\delta}(x) \cap (B_{\delta}(a))^{C}$. Tome $\bar{z} = \bar{a} + \left( 1 + \frac{\delta}{2r} \right) (\bar{x}-\bar{a})$. Entonces, 
$$
\lVert z-a \rVert = \left\lVert  \left( 1+\frac{\delta}{2r} \right)(x-a)  \right\rVert = r +\frac{\delta}{2} > r.
$$
Luego, $z \in (B_{r}(a))^{C}$. Además $\lVert z-x \rVert = \frac{\delta}{2} < \delta$, así $z \in B_{\delta}(x)$. Concluimos que  $z \in B_{\delta}(a) \cap (B_{\delta}(a))^{C}$.
![[Frontera bola 1.svg#invert_B]]
2. Queremos $y \in B_{\delta}(x) \cap B_{r}(a)$. Si $r > \frac{\delta}{2}$, tome $\bar{y} = \bar{a} + \left( 1-\frac{\delta}{2r} \right)(\bar{x}-\bar{a})$. Entonces, 
$$
\lVert y-a \rVert = \left\lvert  1-\frac{\delta}{2r}  \right\rvert r = \left\lvert  r-\frac{\delta}{2}  \right\rvert = r-\frac{\delta}{2} < r.
$$
Así $y \in B_{r}(a)$. Además, 
$$
\lVert y-x \rVert = \frac{\delta}{2r} \lVert x-a \rVert = \frac{\delta}{2} < \delta.
$$
Así, $y \in B_{\delta}(x)$. Por tanto, si $r> \frac{\delta}{2}$, $y \in B_{\delta}(x) \cap B_{r}(a)$.
![[Frontera bola 2.svg#invert_B]]
Ahora, si $r< \frac{\delta}{2}$, tome $y = a$. Claramente $y \in B_{r}(a)$. Además 
$$
\lVert y-x \rVert = \lVert a-x \rVert  = r \leq \frac{\delta}{2} < \delta,
$$
por lo que $y \in B_{\delta}(x)$. Concluimos que $y \in B_{\delta}(x) \cap B_{r}(a)$.
![[Frontera bola 3.svg#invert_B]]
"$\subseteq$": Sea $x$ un punto frontera de $B_{r}(a)$.  Si $\lVert x-a \rVert > r$ existe $\delta>0$ tal que $B_{\delta}(x) \cap B_{r}(a) = \emptyset$, una contradicción. Si $\lVert x-a \rVert < r$, existe $\delta > 0$ tal que $B_{\delta}(x) \cap (B_{r}(a))^{C} = \emptyset$, una contradicción. Concluimos que $\lVert x-a \rVert = r$.

### Definición (Clausura)
La clausura (cerradura) de un conjunto $A$ es $\bar{A} = A \cup \partial A$.

### Lema (Complemento de la clausura y puntos interiores del complemento)
$(\bar{A})^{C} = (A^{C})^{0}$  y $\overline{(A^{c})} = (A^{0})^{C}$
***Prueba:*** "$\subseteq$" Sea $x \in (\bar{A})^{C}$. Entonces $x \in (A \cup \partial A)^{C}$, es decir, $x \not\in A$ y $x \not\in \partial A$.  Como $x \not\in \partial A$, por definición tenemos que existe $\delta>0$ tal que $B_{\delta}(x) \cap A = \emptyset$ o $B_{\delta}(x) \cap A^{c} = \emptyset$. Nótese que lo segundo es imposible, pues $x \in A^{c}$ y $x \in B_{\delta}(x)$. Luego, 
$$
\begin{aligned}
&B_{\delta}(x) \cap A = \emptyset \\
&\implies B_{\delta}(x) \subseteq A^{c}\\
&\implies x \text{ es punto interior de } A^{c} \\
&\implies x \in (A^{c})^{0}.
\end{aligned}
$$
"$\supseteq$" Sea $x \in (A^{c})^{0}$. Entonces, $x$ es punto interior de $A^{c}$, luego existe $\delta>0$ tal que $B_{\delta}(x) \subseteq A^{c}$. Así $x \not\in A$ (pues $x \in B_{\delta}(x) \subseteq A^{c}$) y $x \not\in \partial A$ (pues $B_{\delta}(x) \cap A = \emptyset$). Concluimos que $x \in (\bar{A})^{C}$.

![[Cerradura y complemento.svg#invert_B]]

(probar el ii de tarea moral) 
### Teorema (Interiores, clausura y subconjunto)
Sea $A$ un conjunto. Entonces:
1. $A^{\circ}$ es abierto y es el abierto más grande contenido en $A$, esto es 
$$
\forall U  \quad(U \subseteq A  \quad\land  \quad U \text{ abierto} \implies U \subseteq A^{\circ}).
$$
2. $\bar{A}$ es un cerrado y es el cerrado más pequeño que contiene a $A$, i.e., 
$$
\forall F  \quad (F\supseteq A  \quad\land  \quad F \text{ cerrado} \implies \bar{A} \subseteq F).
$$

***Prueba:*** 1. Probaremos primero que $A^{\circ}$ es abierto. Sea $a \in A^{\circ}$. Hay que mostrar que  existe una bola abierta que contenga a $a$ tal que esté contenida en $A^{\circ}$. Como $a \in A^{\circ}$ es un punto interior, existe $\delta>0$ $B_{\delta}(a) \subseteq A$. Como $B_{\delta}(a)$ es abierto, para todo $x \in B_{\delta}(a)$ existe $\eta > 0$ tal que $B_{\eta}(x) \subseteq B_{\delta}(a) \subseteq A$. Así, todo $x \in B_{\delta}(a)$ es punto interior de $A$ (pues está dentro de $B_{\eta}(x)$ y entonces pertenece a $B_{\delta}(a)$). Luego $B_{\delta}(a) \subseteq A^{\circ}$. Concluimos que $A^{\circ}$ es abierto.
Probaremos ahora que $A^{\circ}$ es el abierto más grande contenido en $A$. Sea $U \subseteq A$ tal que $U$ es abierto. Sea $u \in U$. Como $U$ es abierto, existe $\delta>0$ tal que $B_{\delta}(u) \subseteq U \subseteq A$ y entonces $u$ es punto interior de $A$, i.e., $U \in A^{\circ}$.

Para 2., probaremos  primero que $\bar{A}$ es cerrado. Sabemos que $(\bar{A})^{c} = (A^{c})^{\circ}$. Por el punto anterior, $(A^{c})^{\circ} = (\bar{A})^{c}$ es abierto y por tanto $\bar{A}$ es cerrado. 
Probaremos ahora que $\bar{A}$ es el cerrado más grande contenido en $A$. Sea $F \supseteq A$, con $F$ cerrado. Note que $F^{c} \subseteq A^{c}$ y como $F^{c}$ es abierto, tenemos por el resultado probado en 1. que $F^{c} \subseteq (A^{c})^{\circ} = (\bar{A})^{c}$. Luego, $F \supseteq \bar{A}$.

### Teorema (Sobre la unión y la intersección de abiertos)
1. $\emptyset$ y $\mathbb{R}^{n}$ son abiertos (y cerrados).
2. La unión arbitraria de abiertos es abierta.
3. La intersección <u>finita</u> de abiertos es abierto

***Prueba:*** El primer punto ya fue demostrado. 
Para 2, sean $\{ U_{k} \}_{k \in I}$ una colección arbitraria de abiertos. Defina $U = \bigcup_{k \in I} U_{k}$. Sea $x \in U$. Luego, existe $\alpha_{j} \in I$ tal que $x \in U_{\alpha_{j}}$ (como $x$ pertenece a la unión, debe pertenecer a al menos uno de los conjuntos). Como $U_{\alpha_{j}}$ es abierto, existe $\delta>0$ tal que $B_{\delta}(x) \subseteq U_{\alpha_{j}} \subseteq U$, de donde concluimos que $U$ es abierto.

***Hacer dibujo***

Para 3, sean $\{ U_{j} \}_{i=1}^{n}$ abiertos. Sean $U = \bigcap_{j=1}^{n} U_{j}$ . Sea $x \in U$. Así, $x \in U_{j}$ para todo $j \in \{ 1,\dots,n \}$. Como $U_{j}$ es abierto, existe $\delta_{j}>0$ tal que $B_{\delta_{j}}(x) \subseteq U_{j}$ . Tome $\delta = \min \{ \delta_{1},\dots, \delta_{n} \}$. Note que $B_{\delta}(x) \subseteq B_{\delta_{j}}(x) \subseteq U_{j}$ para todo $j$. Luego $B_{\delta}(x) \subseteq U$ y concluimos que $U$ es abierto.

***Hacer dibujo***
#### Ejemplo 
Busquemos $\{U_{j}\}_{j=1}^{\infty}$ abiertos tales que $\bigcap_{j=1}^{\infty} U_{j}$ no es abierto. En $\mathbb{R}$, note que los conjuntos $U_{j} = \left( -\frac{1}{j}, \frac{1}{j} \right)$ son abiertos y que $\bigcap_{j=1}^{\infty} U_{j} = \{ 0 \}$ y $\{ 0 \}$ es cerrado (podemos ver que su complemento $(-\infty,0)  \cup (0,+\infty)$ es abierto pues es la unión de dos abiertos).

***Hacer dibujo***

#### Ejemplo 
¿$\mathbb{N}$ es cerrado en $\mathbb{R}$? Claramente no es abierto (considere una bola de tamaño $\frac{1}{2}$). Note que $\mathbb{N}^{c} = (-\infty, 0) \cap [\bigcup_{k=0}^{\infty} (k,k+1)]$, que es abierto pues es una unión de abiertos. Concluimos que $\mathbb{N}$ es cerrado.

### Teorema (Sobre la unión e intersección de cerrados)
1. La intersección arbitraria de cerrados es cerrada.
2. La unión finita de cerrados es cerrado.

***Prueba:*** Para 1, sea $\{ F_{\alpha} \}_{\alpha \in I}$ una familia de conjuntos cerrados y sea $F = \bigcap_{\alpha \in I} F_{\alpha}$. Entonces $F^{c} = \bigcup_{\alpha \in I} F_{\alpha}^{c}$ es abierto pues $F_{\alpha}^{c}$ es abierto para todo $\alpha \in I$. Concluimos que $F$ es cerrado. Para 2, similarmente, $\left( \bigcup_{j=1}^{n} F_{j} \right)^{c} = \bigcap_{j=1}^{n} F_{j}^{c}$.

#### Ejemplo 
Tome $F_{n} = [\frac{0,1}{n]}$ que son cerrados. Entonces, $\bigcap_{n=1}^{\infty} F_{n} = \{ 0 \}$ es cerrado.

#### Ejemplo 
 $\mathbb{Z}$ es cerrado en $\mathbb{R}$.

### Definición (punto de acumulación y punto aislado) 
1. Un punto $p$ se dice punto de acumulación de $A$ si 
$$
\forall\delta>0  \quad(B_{\delta}(p) \setminus \{ p \} \cap A \neq  \emptyset)
$$
Denotamos $A' = \{ \text{puntos de acumulación de }A \}$.
2.Un punto $p \in A$ se llama aislado si 
$$
\exists \delta>0  \quad (B_{\delta}(p) \setminus \{ p \} \cap A = \emptyset ).
$$

#### Ejemplo 
En $\mathbb{N}$, todos sus puntos son puntos aislados tomando $\delta=\frac{1}{2}$. Luego, para $n \in \mathbb{N}$, $B_{\delta}(n) = \left( n-\frac{1}{2}, n +\frac{1}{2} \right)$ y $B_{\delta}(n) \setminus \{ n \} \cap \mathbb{N} = \emptyset$.

#### Ejemplo 
Para $A=[0,1]$, $A' = [0,1]$.
***Hacer dibujo***

#### Ejemplo 
Para $A = \{ 0 \}$, $A' = \emptyset$.
***Hacer dibujo***

#### Ejemplo 
En $\mathbb{R}^{2}$, considere $A = \left\{  \frac{1}{m}, \frac{1}{n} : m,n \in \mathbb{N}^{*}  \right\}$. Todo punto de $A$ es aislado (ejercicio). Además, $A'= \{ (0,0) \}$. Pues si $(x,y) \neq (0,0)$, no puede ser punto de acumulación, pues siempre existe tal $\delta$. Para $(0,0)$ sí, pues por arquimedianidad siempre existen $m,n$ tales que $\left\lVert  \frac{1}{m}, \frac{1}{n}  \right\rVert < \delta$.
***Hacer dibujo***


### Teorema (Conjunto cerrado y puntos de acumulación)
$F$ es cerrado si y solo si todo punto de acumulación de F pertenece a F.

***Prueba:*** ($\implies$): Suponga que $F$ es cerrado. Sea $a$ un punto de acumulación de $F$ y suponga por contradicción que $a \not\in F$, i.e., $a \in F^{c}$. Note que $F^{c}$ es abierto, i.e., existe $\delta>0$ tal que $B_{\delta}(a) \subseteq F^{c}$. Entonces $B_{\delta}(a) \cap F = \emptyset$, y luego $B_{\delta}(a) \setminus \{ a \} \cap F = \emptyset$, lo que contradice la definición de punto de acumulación. Concluimos entonces que $a \in F$.
($\impliedby$): Suponga que $F$ es un conjunto que contiene todos sus puntos de acumulación. Suponga por contradicción que $F$ <u>no</u> es cerrado. Así $F^{c}$ no es abierto, es decir, existe $a \in F^{c}$ tal que para todo $\delta>0$, $B_{\delta}(a) \not\subseteq F^{c}$, es decir, existen puntos $x \in B_{\delta}(a) \cap F$. Como $a \not\in F$ entonces $(B_{\delta}(a)\setminus \{ a \}) \cap F \neq \emptyset$. Luego, $a$ es punto de acumulación, y entonces $a \in F$ una contradicción pues asumimos que $a \not\in F$.

## Compacidad

### Definición (Cubrimiento de abiertos y conjunto compacto)
1. Una colección de abiertos $\{ U_{\alpha} \}_{\alpha \in I}$ se llama un cubrimiento de abiertos de $A$ si $A \subseteq \bigcup_{\alpha \in I} U_{\alpha}$. 
2. A se llama compacto si para todo cubrimiento abierto $\{ U_{\alpha} \}$ de $A$ existen $\{U_{\alpha_{1}}, U_{\alpha_{2}}, \dots U_{\alpha_{m}}\}$ (subcubrimiento finito) tal que $A \subseteq \bigcup_{j=1}^{n} U_{\alpha_{j}}$.

#### Ejemplo 
En $\mathbb{R}^{n}$, un cubrimiento de $\mathbb{R}^{n}$ es $U_{\alpha} = R_{1}(\alpha)$, $\alpha \in \mathbb{R}^{n}$.

#### Ejemplo 
$\mathbb{R}$ no es compacto. Si $\mathbb{R}$ fuera compacto, como $\mathbb{R} \subseteq \bigcup_{n \in \mathbb{N}}(-n,n)$ es un cubrimiento de abiertos de $\mathbb{R}$, luego, existen $n_{1},\dots,n_{m} \in \mathbb{N}$ tales que 
$$
\mathbb{R} \subseteq \bigcup_{j=1}^{m} (-n_{j}, n_{j}) \subseteq (
-M,M)
$$
con $M = \max \{ n_{1}, \dots, n_{m} \}$, una contradicción.

#### Ejemplo 
$(0,1)$ no es un compacto. Tome $(0,1) \subseteq \bigcup_{n=1}^{\infty} \left( \frac{1}{n}, 1 \right)$. Si fuera compacto, existen $n_{1}, \dots, n_{m} \in N^{\ast}$ tales que 
$$
(0,1) \subseteq \bigcup_{j=1}^{n} \left( \frac{1}{n_{j}},1 \right) = \left( \frac{1}{M}, 1 \right)
$$
con $M = \max \{ n_{1}, \dots, n_{m} \}$, una contradicción.

#### Ejemplo 
$[a,b]$ es compacto. 
***Prueba:***  Sea $\{ U_{\alpha} \}_{\alpha \in J}$ un cubrimiento de abiertos de $[a,b]$, es decir, $[a,b] \subseteq \bigcup_{\alpha \in J} U_{\alpha}$. Por contradicción, suponga que no existe un subcubrimiento finito. Defina $I_{1} = [a,b]$. Considere $\{ [a, \frac{a+b}{2}], [\frac{a+b}{2}, b] \}$ partición de $[a,b]$. Al menos uno de estos subintervalos no tiene un subcubrimiento finito (si ambos lo tuvieran, tendría un subcubrimiento finito para $[a,b]$). Llame a este subintervalo $I_{2} \supseteq I_{1}$. Recursivamente, defina $\{ I_{j} \}_{j=1}^{\infty}$ tales que $I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots$ son cerrados y $I_{j}$ no tiene un subcubrimiento finito para todo $j$. Por el teorema de intervalos encajados, existe $x \in \bigcap_{j=1}^{\infty} \subseteq [a,b] \subseteq \bigcup_{\alpha \in J} U_{\alpha}$.  Luego, existe algún $\alpha \in J$ tal que $x \in U_{\alpha}$. Además, como $U_{\alpha}$ es abierto, existe $\delta>0$ tal que $B_{\delta}(x) \subseteq U_{\alpha}$. Además, note que $\lvert I_{j} \rvert \underset{j \rightarrow \infty}{\longrightarrow} 0$. Así, existe $I_{N} \subseteq B_{\delta}(x) \subseteq U_{\alpha}$, i.e, $I_{N}$ tiene un subcubrimiento finito, una contradicción pues asumimos que los $\{ I_{j} \}_{j=1}^{\infty}$ no tenían. 
***Hacer dibujo***

#### Ejemplo (Conjunto finito es compacto)
Todo conjunto finito $A = \{ x_{1},\dots,x_{n} \}$ es compacto.
***Prueba:*** Sea $\{ U_{\alpha} \}_{\alpha \in I}$ un cubrimiento abierto de $A$, i,.e., $A \subseteq \bigcup_{\alpha \in I} U_{\alpha}$. Para $j \in \{ 1,\dots,n \}$, como $x_{j} \in A \subseteq \bigcup_{\alpha \in I} U_{\alpha}$, entonces existe $\alpha_{j} \in I$ tal que $x_{j} \in U_{\alpha_{j}}$. Tome el subcubrimiento finito $\{ U_{\alpha_{1}}, \dots, U_{\alpha_{n}} \}$. Así, $A \subseteq \bigcup_{j=1}^{n} U_{\alpha_{j}}$.
![[conjunto finito es compacto.svg#invert_B]]

### Lema (Subconjunto cerrado de compacto es compacto) 
Si $K$ es compacto y $F \subseteq K$ con $F$ cerrado. Entonces, $F$ es compacto. 
***Prueba:*** Sea $\{ U_{\alpha} \}_{\alpha \in I}$ abiertos tales que $F \subseteq \bigcup_{\alpha \in I} U_{\alpha}$. Como $K \subseteq F \cup F^{C}$, entonces $\left(\bigcup_{\alpha \in I} U_{\alpha}\right) \cup F^{C}$ es un cubrimiento de abiertos para $K$. Como $K$ es compacto, entonces existe un subcubrimiento finito $\{U_{\alpha_{1}}, \dots, U_{\alpha_{n}}\}$ tal que 
$$
F \subseteq K \subseteq U_{\alpha_{1}} \cup \cdots \cup U_{\alpha_{n}} \cup F^{C},
$$
y como $F \cap F^{C} = \emptyset$, entonces $F \subseteq \bigcup_{i=1}^{n} U_{\alpha_{i}}$. Conclúyase que $F$ es compacto.

### Lema  (Cubo es compacto)
El cubo $[-M,M]^{n} = \{ x \in \mathbb{R}^{n}: -M \leq x_{j} \leq M  \quad \forall j\}$ es compacto. 
La prueba es similar al caso $[a,b]$.

### Teorema (Compacto si y solo si cerrado y acotado) 
En $\mathbb{R}^{n}$, $K$ es compacto si y solo si es cerrado y acotado.
***Prueba:*** ($\implies$): Suponga que $K$ es compacto. Como $K \subseteq \bigcup_{x \in  K} B_{1}(x)$ es un cubrimiento abierto de $K$, existen $x_{1},\dots,x_{m}$ tales que 
$$
K \subseteq \bigcup_{j=1}^{m}B_{1}(x_{j}) \subseteq B_{R}(0),
$$
con $R = \max \{ \lVert x_{1} \rVert, \dots, \lVert x_{m} \rVert \} +1$, pues si $x \in B_1(x_{k})$ entonces 
$$
\lVert x \rVert \leq \lVert x-x_{k}\rVert + \lVert x_{k} \rVert  \leq  1 + \max \{ \lVert x_{1} \rVert, \dots, \lVert x_{m} \rVert \} = R.
$$
Concluimos que $K$ es acotado. Falta ver que $K$ es cerrado, i.e. que $K^{C}$ es abierto. Sea $x \in A^{C}$. Para $a \in K$, sea $\delta_{a} = \frac{\lVert x-a \rVert}{2}$. Tome como cubrimiento abierto $\bigcup_{a \in K} B_{\delta_{a}}(a) \supseteq K$. Como $K$ es compacto, existen $a_{1},\dots,a_{m} \in K$ tales que $K \subseteq \bigcup_{j=1}^{m} B_{\delta_{a_{j}}}(a_{j})$. Tome $0 < \delta < \min \{ \delta_{a_{1}}, \dots \delta_{a_{m}} \}$ y considere $B_{\delta}(x)$. Veamos que $B_{\delta}(x) \cap B_{\delta_{a_{j}}}(a_{j}) = \emptyset$ para todo $j \in \{ 1,\dots,n \}$. Si $y \in B_{\delta_{a_{j}}}(a_{j})$, entonces $\lVert y - a_{j} \rVert < \frac{\lVert x-a_{j} \rVert}{2}$. Luego, 
$$
\begin{aligned}
\lVert x-y \rVert &= \lVert x-a_{j} + a_{j} - y \rVert \\
& \geq \lVert x-a_{j} \rVert + \lVert y-a_{j} \rVert \\
& > \lVert x - a_{j} \rVert - \frac{\lVert x -a_{j} \rVert }{2} \\
&= \frac{\lVert x-a_{j} \rVert }{2} = \delta_{a_{j}} > \delta.
\end{aligned} 
$$
Como $K \subseteq \bigcup_{j=1}^{m} B_{\delta_{a_{j}}}(a_{j})$ y $B_{\delta}(x) \cap B_{\delta_{a_{j}}}(a_{j}) = \emptyset$ para todo $j$, entonces $K \cap B_{\delta}(x) = \emptyset$ y luego $B_\delta(x) \subseteq K^{C}$. Por lo tanto, $K$ es cerrado. 
($\impliedby$): Suponga que $K$ cerrado y acotado. Como $K$ es acotado, existe  $R>0$ tal que $\lVert x \rVert < R$ para todo $x \in K$. Así, $K \subseteq \bar{B}_{R}(0) \subseteq [-R, R]^{n}$, pues $\lVert x \rVert_{\infty} < \lVert x \rVert_{2}$. Por el lema anterior, como $K$ es cerrado y está contenido en un compacto, conclúyase que $K$ es compacto.

## Sucesiones en $\mathbb{R}^{n}$

### Definición (Sucesión)
Generalización de [[Sucesiones]] a $\mathbb{R}^n$. Una sucesión en $\mathbb{R}^{n}$ es una función $\phi: \mathbb{N} \to \mathbb{R}^{n}$. Se denota $\bar{x_{k}} = \phi(k) \in \mathbb{R}^{n}$, y $\phi = (x_{k})_{k \in \mathbb{N}}$.

***Hacer dibujo de convergencia***
### Definición (Convergencia de sucesiones)
Decimos que $(x_{k})_{k \in \mathbb{N}}$ converge a $x \in \mathbb{R}^{n}$ si para todo $\varepsilon>0$, existe $N \in \mathbb{N}$ tal que para todo $k \geq N$, se cumple que 
$$
\lVert x_{k}-x \rVert < \varepsilon \iff x_{k} \in B_{\varepsilon}(x).
$$
Se escribe $\lim_{ n \to \infty } x_{n} = x$ o $x_{n} \underset{n \rightarrow \infty}{\longrightarrow} x$.

#### Ejemplo 
$\bar{x}_{k} = \begin{pmatrix}\frac{(-1)^{k}}{k} \\ \frac{k+1}{k+2} \\ e^{-k}\sin k\end{pmatrix} \underset{k \rightarrow \infty}{\longrightarrow} \begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix}$.

## Notas
1. Basta considerar $\lVert \cdot \rVert_{2}$, pues todas las normas son equivalentes.
2. Si $\bar{x}_{k} = (x_{1}^{(k)}, \dots, x_{n}^{(k)}) \in \mathbb{R}^{n}$, esto es, $(x_{j}^{(k)})_{k\geq 1}$ es la sucesión en $\mathbb{R}$ de la entrada $j$.

### Teorema (Condición de convergencia por entradas)
Sea $(a_{n})_{n \in \mathbb{N}}$ una sucesión en $\mathbb{R}^n$. Entonces $x_{k} \underset{k \rightarrow \infty}{\longrightarrow} x$ si y solo si para todo $j \in \{ 1,\dots,n \}$ se cumple que $x^{(k)}_{j} \underset{n \rightarrow \infty}{\longrightarrow} x_{j}$, donde $x_{k} = (x_{1}^{(k)}, \dots, x_{n}^{(k)})$ y $x = (x_{1}, \dots, x_{n})$.

***Prueba:*** ($\implies$): Suponga que $x_{k} \underset{k \rightarrow \infty}{\longrightarrow} x$. Dado $\varepsilon>0$, por definición de convergencia existe $N \in \mathbb{N}$ tal que para todo $k \geq N$, $\lVert x_{k} - x \rVert < \varepsilon$. Como $\lvert x_{j}^{(k)} - x_{j} \rvert \leq \lVert x_{k}-x \rVert < \varepsilon$, se sigue que $x_{j}^{(k)} \underset{k \rightarrow \infty}{\longrightarrow} x_{j}$.
($\impliedby$): Suponga que $x_{j}^{(k)} \underset{k \rightarrow \infty}{\longrightarrow} x_{j}$ para todo $j \in \{ 1,\dots, n \}$. Luego, para cada $j$, existe $N_{j} \in \mathbb{N}$ tal que $\lvert x_{j}^{(k)} - x_{j} \rvert < \frac{\varepsilon}{n}$. Tome $N = \max \{ N_{1},\dots N_{n} \}$. Luego, para $k \geq N$, note que 
$$
\lVert x_{k}-x \rVert \leq \sum_{j=1}^{n} \lvert x_{j}^{(k)} - x_{j} \rvert < \sum_{j=1}^{n} \frac{\varepsilon}{n} = \varepsilon.
$$
Conclúyase que $x_{k} \underset{k \rightarrow \infty}{\longrightarrow} x$.

### Definición (Sucesión acotada)
$(x_{k})_{k \in \mathbb{N}}$ es acotada si existe $M>0$ tal que para todo $k \in \mathbb{N}$, $\lVert x_{k} \rVert \leq M$.

### Teorema (Convergencia implica acotación)
Toda sucesión convergente es acotada

***Idea de la prueba:*** Usar la definición para algún valor fijo de $\varepsilon$ (p.e. $\varepsilon = 1$) y tomar $M = \max \{ \lVert x_{1} \rVert, \dots, \lVert x_{N-1} \rVert \}$, donde $N$ proviene de la definición de converfencia.

***Hacer dibujo***

#### Nota
En su forma contrapositiva, esto quiere decir que si $(x_{k})_{k \in \mathbb{N}}$ no es acotada entonces no converge.

### Teorema (Operaciones sobre límites)
Sean $(x_{k})_{k \in \mathbb{N}}$ y $(y_{k})_{k \in \mathbb{N}}$ sucesiones tales que $x_{k} \underset{k \rightarrow \infty}{\longrightarrow}x$ y $y_{k} \underset{k \rightarrow \infty}{\longrightarrow} y$ y sea $c \in \mathbb{R}$. Entonces:
1. $x_{k} \pm y_{k} \underset{k \rightarrow \infty}{\longrightarrow} x \pm y$,
2. $c x_{k} \underset{k  \rightarrow \infty}{\longrightarrow} cx$,
3. $\bar{x}_{n} \cdot \bar{y}_{n} \underset{k \rightarrow \infty}{\longrightarrow} \bar{x} \cdot \bar{y}$,
4. Si $(c_{k})_{k \in \mathbb{N}} \subseteq \mathbb{R}$ y $c_{k} \underset{k \rightarrow \infty}{\longrightarrow} c$, entonces $c_{k} x_{k} \underset{k \rightarrow \infty}{\longrightarrow} c x$.
***Prueba:*** Ejercicio.

### Definición (Sucesión de Cauchy)
$(x_{n})_{n \in \mathbb{N}}$ es de Cauchy si para todo $\varepsilon>0$, existe $N \in \mathbb{N}$ tal que para todos $m,n \geq N$, $\lVert x_{n}-x_{m} \rVert < \varepsilon$.

### Teorema (Convergencia si y solo si Cauchy)
Una sucesión $(x_{k})_{k \in \mathbb{N}} \subseteq \mathbb{R}^n$ es convergente si y solo si es de Cauchy

***Prueba:*** La misma idea que en 250, aplicada entrada por entrada.

### Teorema (Conjuntos cerrados y convergencia)
Un conjunto $F \subseteq \mathbb{R}^n$ es cerrado si y solo si toda sucesión $(x_{k})_{k \in \mathbb{N}} \subseteq F$ convergente a $x$ cumple que $x \in F$.

***Prueba:*** ($\implies$): Suponga que $F$ es cerrado. Sea $(x_{k})_{k \in \mathbb{N}} \subseteq F$ con $x_{k} \underset{k  \rightarrow \infty}{\longrightarrow} x$. Suponga por contradicción que $x \not\in F$, i.e. $x \in F^{C}$, y como $F^{C}$ es abierto, entonces existe $\varepsilon>0$ tal que $B_{\varepsilon}(x) \subseteq F^{C}$. Por convergencia de la sucesión, existe $N \in \mathbb{N}$ tal que para todo $k \geq N$, se cumple que $\lVert x_{k}-x \rVert < \varepsilon \iff x_{k} \in B_{\varepsilon}(x)$. Finalmente, como $x_{k} \in B_{\varepsilon}(x) \subseteq F^{C}$, entonces $x_{k} \in F_{C}$, una contradicción, pues asumimos que $x_{k} \in F$ para todo $k \in \mathbb{N}$. Concluimos que $x \in F$.
($\impliedby$): Suponga por contradicción que $F$ no es cerrado, i.e., $F^{C}$ no es abierto. Luego existe $x \in F^{C}$ tal que para todo $\delta>0$, $B_{\delta}(x) \not \subseteq = F^{C}$, i.e., $B_{\delta}(x) \cap F\neq \emptyset$. Para $n \in N^{\ast}$, tome $\delta_{n} = \frac{1}{n} > 0$. Luego, existe $x_{n} \in B_{\delta_{n}}(x) \cap F$. Defina la sucesión $(x_{n})_{n \in \mathbb{N}}$. Así, $x_{n} \in F$ para todo $n \in \mathbb{N}^{\ast}$ y $\lVert x-x_{n} \rVert < \frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} 0$. Así, $x_{n} \underset{n \rightarrow \infty}{\longrightarrow} x \in F$, una contradicción.

#### Ejemplo 
$F = (0,1]$ no es cerrado pues $\left( \frac{1}{k} \right)_{ k\in \mathbb{N}} \subseteq (0,1]$ pero $\frac{1}{k} \underset{k \rightarrow \infty}{\longrightarrow} 0 \not\in F$.

### Definición (Subsucesión)
Cf. [[Subsucesiones]] (MA0350). Dada una sucesión $(x_{k})_{k \in \mathbb{N}} \subseteq \mathbb{R}^n$, una subsucesión de $(x_{k})_{k \in \mathbb{N}}$ es una función $\phi: \mathbb{N} \to \{ x_{k}:k\geq 1 \}$ tal que $\phi (k) = x_{n_{k}}$, con $(n_{k})_{k \in \mathbb{N}} \subseteq \mathbb{N}$ estrictamente creciente.

### Teorema (Bolzano-Weirerstrass)
Toda sucesión acotada tiene una subsucesión convergente

***Prueba:*** Si el rango de la sucesión es finito, al menos un término de la sucesión se repite infinitas veces. Tome esa subsucesión constante. 
Si el rango es infinito, por ser una sucesión acotada sabemos que existe una bola cerrada $B$ tal que $\{ x_{k}:k\geq 1 \} \subseteq B$. Sabemos que $B$ es compacto. Suponga por contradicción que $(x_{k})_{k \in \mathbb{N}}$ no tiene una subsucesión convergente. Así, para todo $x \in \mathbb{R}^n$ existe $\delta_{x}>0$ tal que $B_{\delta_{x}}(x)$ sólo tiene un número finito de términos de $(x_{k})_{k \in \mathbb{N}}$. Como $\{ B_{\delta_{x}}:x \in B \}$ es un cubrimiento por abiertos de $B$ y $B$ es compacto, existen $x_{1},\dots,x_{n} \in B$ tal que $B \subseteq \bigcup_{j=1}^{m} B_{\delta_{x_{j}}}(x_{j})$. Note que el conjunto descrito en el lado derecho de la inclusión tiene finitos puntos de la sucesión, pues es una unión finita de bolas que a su vez contienen finitos puntos de la sucesión. Pero entonces, $B$ tiene puntos finitos de $(x_{k})_{k \in \mathbb{N}}$, una contradicción pues asumimos que la sucesión tenía rango infinito.

### Lema (Compactos encajados)
Sean $K_{1} \supseteq K_{2} \supseteq \dots$ compactos no vaciós. Entonces $\bigcap_{j=1}^{\infty} K_{j} \neq \emptyset$.

***Prueba:*** Como $K_{1}$ es acotado, existe una bola abierta $B$ tal que $K_{1}  \subseteq B$ y por tanto $K_{j} \subseteq B$ para todo $j \in \mathbb{N}^{\ast} \}$. Suponga por contradicción que $\bigcap_{j=1}^{\infty} K_{j} = \emptyset$ y defina para cada $j$ $O_{j} = B \setminus K_{j} = B \cap K_{j}^{C}$. Entonces 
$$
\bigcup_{j=1}^{\infty} O_{j} = \bigcup_{j=1}^{\infty} (B \cap K_{j}^{C}) = B \cap \left( \bigcup_{j=1}^{\infty} K_{j}^{C} \right) = B \cap \left( \bigcap_{j=1}^{\infty} K_{j} \right)^{C} = B \supseteq K_{1}.
$$
Note además que  $O_{j}= B \cap K_{j}^{C}$ es abierto. Así $\{ O_{j} \}_{j=1}^{\infty}$ es un cubrimiento por abiertos de $K_{1}$ y $K_{1}$ es compacto. Luego existen $O_{1}, \dots O_{m}$ tales que $K_{1} \subseteq \bigcup_{j=1}^{m} O_{j} = O_{m} = B \cap K_{m}^{C}$, lo que implica que $K_{1} \subseteq K_{m}^{C}$. Pero como $K_{m} \subseteq K_{1}$, lo que ocurre si y solo si $K_{m} = \emptyset$, una contradicción.

## Conexidad

### Definición (Conjunto disconexo)
Un conjunto $D$ se llama disconexo si existen $A, B$ abiertos no vacíos disjuntos tales que $D \subseteq A \cup B$, $D \cap A \neq \emptyset$ y $D \cap B \neq \emptyset$.
***Hacer dibujo***
#### Ejemplo 
El conjunto $(0,1) \cup (2,3)$ es disconexo.

### Definición (Conjunto conexo)
$D$ es conexo si no es disconexo, i.e., si para todos $A, B$ abiertos, 
$$
(A \cap B = \emptyset \quad \land  \quad D \subseteq A \cup B) \implies (D \subseteq A  \quad\lor  \quad D\subseteq B)
$$

#### Ejemplo 
El intervalo $I = [0,1]$ es conexo.

#### Ejemplos adicionales
1. Cualquier intervalo (abierto, semiabierto o cerrado) es conexo
2. $\{ x_{1} \}$ es conexo
3. $\{ x_{1}, x_{2} \}$ es disconexo
4. Cualquier bola es conexa.
5. $\mathbb{R}^n \setminus\{ 0 \}$ es conexo si $n \geq 2$ y disconexo si $n=1$.