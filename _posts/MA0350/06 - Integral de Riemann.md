#Mate #MA0350
Fecha: 5/6/25
Ver también: [[Técnicas de integración]], [[Aplicaciones de la integral de Riemann]], [[Integrales impropias]].
Generalización en $\mathbb{R}^n$: [[Integración en Rn]] (MA0450)
(Ver presentación)

### Teorema (Unicidad de la integral de Riemann)
***Prueba:***  Asuma que $I_{1}$ e $I_{2}$ satisfacen la definición. Dado $\varepsilon>0$ existen $P_{\varepsilon_{1}}$ y $P_{\varepsilon_{2}}$ tales que 
$$
\lvert S(f, P_{1}, \xi_{1},\dots, \xi_{n}) - I_{1} \rvert < \varepsilon  \quad \text{(1)}
$$
para todo $P_{1} \supseteq P_{\varepsilon_{1}}$, $a_{i} \leq \xi_{i} \leq a_{i+1}$ y
$$
\lvert S(f, P_{2}, \eta_{1},\dots,\eta_{m}) - I_{2} \rvert < \varepsilon  \quad \text{(2)}
$$
para todo $P_{2} \supseteq P_{\varepsilon_{2}}$, $b_{i} \leq \eta_{i} \leq b_{i+1}$. Tome $P = P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$. Entonces $P \supseteq P_{\varepsilon_{1}}$ y $P \supseteq P_{\varepsilon_{2}}$. Luego, combinando (1) y (2), tenemos que $\lvert I_{1} - I_{2}\rvert < 2\varepsilon$. Como esto se cumple para todo $\varepsilon>0$, conclúyase que $I_{1} = I_{2}$.

### Teorema (Suma de integrales)
Sea $f:[a,b] \to \mathbb{R}$ acotada y $a<c<b$. Asuma que $f$ es Riemann integrable en $[a,c]$ y en $[c,b]$. Entonces es Riemann integrable en $[a,b]$. Además $$\int_{a}^{b} f(x)\, dx = \int_{a}^{c} f(x)  \, dx + \int_{c}^{b} f(x) \, dx.$$
***Prueba:*** Dado $\varepsilon>0$, sabemos que existen $I_{1}$ e $I_{2}$, $P_{\varepsilon_{1}}$ y $P_{\varepsilon_{2}}$ que satisfacen que:
1. $P_{\varepsilon_{1}} = \{ a_{0}=a < a_{1}<...<a_{n} = c \}$ es una partición de $[a,c]$.
2. $P_{\varepsilon_{2}} = \{ d_{0}=c < d_{1}<...<d_{n} = b \}$ es una partición de $[c,b]$.
Además, si $P_{1}$ es una partición de $[a,c]$ tal que $P_{1} \supseteq P_{\varepsilon_{1}}$, entonces
$$
\lvert S(f, P_{1}, \xi_{1},\dots, \xi_{n}) - I_{1} \rvert < \frac{\varepsilon}{2}  \quad \text{(1)}.
$$
Similarmente, si $P_{2}$ es una partición de $[c,b]$ tal que $P_{2} \supseteq P_{\varepsilon_{2}}$.
$$
\lvert S(f, P_{2}, \eta_{1},\dots,\eta_{m}) - I_{2} \rvert < \frac{\varepsilon}{2}  \quad \text{(2)}.
$$
Vamos a probar que $I_{1} + I_{2}$ es la intergral en $[a,b]$. Tome $P_{\varepsilon}=P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$. Sea $P = \{ h_{0} = a<h_{1},\dots,h_{\ell}=b\}$ tal que $P \supseteq P_{\varepsilon}$. Como $c \in P_{\varepsilon}$, existe un $h_{k} = c$ tal que $\{ h_{0}=a < h_{1} <...<h_{k} = c \}$ es una partición de $[a,c]$ más fina que $P_{\varepsilon_{1}}$ y $\{ h_{k}=c < h_{k+1} <...<h_{\ell} = b\}$ es una partición de $[c,b]$ más fina que $P_{\varepsilon_{2}}$. Considere la suma de Riemann 
$$
\sum_{i=1}^{\ell-1} f(\xi_{i})(h_{i+1}-h_{i}) = \sum_{i=1}^{k-1}  f(\xi_{i}) (h_{i+1}-h_{i})U + \sum_{i=k}^{\ell-1}  f(\xi_{i})(h_{i+1}-h_{i})
$$
Finalmente, aplicando (1) y (2) y desigualdad triangular:
$$
\lvert S(f,P, \xi_{1},\dots,\xi_{\ell}) - I_{1}-I_{2}\rvert < \varepsilon.
$$

Sea $\varepsilon>0$ y $f:[a,b] \to \mathbb{R}$ tal que existe $I_{1}$ y $P_{\varepsilon_{1}}$ tal que si $P \supseteq P_{\varepsilon_{1}}$ se cumple que 
$$
\lvert S(f,P, \xi_{1},\dots,\xi_{n}) - I_{1} \rvert < \frac{\varepsilon}{2}
$$
donde $S(f, P, \xi_{1},\dots \xi_{n}) = \sum_{i=0}^{n-1} f(\xi_{i})(a_{i+1}-a_{i})$. Tome $g:[a,b] \to \mathbb{R}$ Riemann integrable. Existen $I_{1}$ y $P_{\varepsilon_{2}}$ tal que si $P' \supseteq P_{\varepsilon_{2}}$,

$$
\lvert S(g,P', \eta_{1},\dots,\eta_{m}) - I_{1} \rvert < \frac{\varepsilon}{2\lvert c \rvert}
$$
Si $\tilde{P} \supseteq P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$. Concluimos que $\tilde{P} \supseteq P_{\varepsilon_{1}} \cup P_{\varepsilon_{2}}$ implica 
$$
	\lvert f+cg, \tilde{P}, \alpha_{1},\dots,\alpha_{\ell} \rvert < \frac{\varepsilon}{2} + \lvert c \rvert \frac{\varepsilon}{2\lvert c \rvert } = \varepsilon.
$$

### Lema (Sumas superiores e inferiores entre particiones) 
Sean $P_{1}$ y $P_{2}$ dos particiones de $[a,b]$ tales que $P_{1} \subseteq P_{2}$. Entonces 
$$
\begin{aligned}
U(f,P_{2}) \leq& U(f, P_{1}) \\
L(f,P_{1}) \leq& L(f, P_{2})
\end{aligned}
$$
***Prueba:***  Sea $P = \{ a_{0}=a<a_{1}<...<a_{n}=b \}$ y sean 
$$
\begin{aligned}
\mathrm{U}(f, P) &= \sum_{i=0}^{n-1} M_{i}(a_{i+1}-a_{i}),\\
\mathrm{L}(f,P) &= \sum_{i=0}^{n-1} m_{i}(a_{i+1}-a_{i}),
\end{aligned}
$$
con $M_{i} = \sup \{ f(x):a_{i}\leq x\leq a_{i+1} \}$ y $m_{i} = \inf \{ a_{i} \leq x \leq a_{i+1} \}$. Sea $\alpha \in [a,b]$ tal que $\alpha \not\in P$. Note que existe $i \in {0,\dots,n-1}$ tal que  $a_{i} < \alpha <a_{i+1}$. Sea $P_{1} = P \cup \{ \alpha \}$. Tome 
$$
\begin{aligned}
M_{i} &= \sup \{ f(x):a_{i}\leq x,=a_{i+1} \} \\
M_{i}' &= \sup \{ f(x): a_{i} \leq  x \leq  \alpha \} \\
M_{i}'' &= \sup \{ f(x): \alpha \leq x \leq a_{i+1}  \}.
\end{aligned}
$$
Note que $M_{i}' \leq M_{i}$ y $M_{i}''\leq M_{i}$. Luego: 
$$
M_{i}(a_{i+1}-a_{i}) = M_{i}(a_{i+1}-\alpha) + M_{i}(\alpha-a_{i} \geq M_{i}''(a_{i+1}-\alpha) + M_{i}'(\alpha-a_{i}).
$$
Entonces $\mathrm{U}(f,P) \geq U(f,P_{1})$, pues son iguales en todos sus términos excepto en los descritos arriba. La prueba para la suma inferior se deja como ejercicio.

### Teorema (Caracterización UL de la integral de Riemann) 
Sea $f:[a,b]$ acotada. Entonces $f$ es Riemann integrable si y solo si para todo $\varepsilon>0$ existe una participación $P_{\varepsilon}$ tal que para toda partición $P \supseteq P_{\varepsilon}$ 
$$
\lvert U(f,P) - L(f,P) \rvert < \varepsilon.
$$
***Prueba:*** ($\implies$): Dado $\varepsilon>0$, existen $I$ y $P_{\varepsilon}$ tal que para todo $P \supseteq P_{\varepsilon}$
$$
\lvert S(f,P,\xi_{1},\dots, \xi_{n}) - I \rvert < \varepsilon.
$$
Tome $P \supseteq P_{\varepsilon}$. Entonces $P = \{ a_{0} = a < a_{1}< \dots < a_{n} = b \}$. Considere $M_{i} = \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \}$. Por ser el supremo, existe $\xi_{i} \in [a_{i},a_{i+1}]$ tal que 
$$
M_{i} - \frac{\varepsilon}{b-a} <  f(\xi_{i}) \leq  M_{i}.
$$
Note que 
$$
\sum_{i=0}^{n-1} f(\xi_{i})(a_{i+1}-a_{i}) \leq  \sum_{i=0}^{n-1} M_{i}(a_{i+1}-a_{i}).
$$
Además, 
$$
\begin{aligned}
S(f, P, \xi_{1},\dots,\xi_{n}) &= \sum_{i=0}^{n-1} f(\xi_{i})(a_{i+1}-a_{i}) \\&> \sum_{i=0}^{n-1} \left( M_{i} - \frac{\varepsilon}{b-a} \right) (a_{i+1}-a_{i}) \\
&= \sum_{i=0}^{n-1}  M_{i}(a_{i+1}-a_{i}) - \frac{\varepsilon}{b-a}\underbrace{ \sum_{i=0}^{n-1} a_{i+1}-a_{i} }_{ = b-a } \\
&= \mathrm{U}(f, P) - \varepsilon.
\end{aligned}
$$
Por lo tanto $\mathrm{U}(f,P) - S(f, P, \xi_{1},\dots,\xi_{n}) < \varepsilon$.
Ahora,  considere $m_{i} = \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \}$. Por ser el ínfimo, existe $\eta_{i} \in [a_{i},a_{i+1}]$ tal que 
$$
m_{i} + \frac{\varepsilon}{b-a} >  f(\eta_{i}) \geq   m_{i}.
$$
Note que 
$$
\sum_{i=0}^{n-1} f(\eta_{i})(a_{i+1}-a_{i}) \geq   \sum_{i=0}^{n-1} m_{i}(a_{i+1}-a_{i}).
$$
Además, 
$$
\begin{aligned}
S(f, P, \eta_{1},\dots,\eta_{n}) &= \sum_{i=0}^{n-1} f(\eta_{i})(a_{i+1}-a_{i}) \\&< \sum_{i=0}^{n-1} \left( m_{i} + \frac{\varepsilon}{b-a} \right) (a_{i+1}-a_{i}) \\
&= \sum_{i=0}^{n-1}  m_{i}(a_{i+1}-a_{i}) + \frac{\varepsilon}{b-a}\underbrace{ \sum_{i=0}^{n-1} a_{i+1}-a_{i} }_{ = b-a } \\
&= \mathrm{L}(f, P) + \varepsilon.
\end{aligned}
$$
Por lo tanto $S(f, P, \eta_{1},\dots,\eta_{n}) - \mathrm{L}(f,P)  < \varepsilon$. Entonces 
$$
\begin{aligned}
&\lvert \mathrm{U}(f, P) - \mathrm{L}(f,P) \rvert \leq  \lvert \mathrm{U}(f,P) - S(f,P, \xi_{1},\dots,\xi_{n}) \rvert + \lvert S(f,P, \xi_{1},\dots,\xi_{n}) - \mathrm{L}(f,P) \rvert \\
&\leq \varepsilon + \lvert S(f,P, \xi_{1},\dots,\xi_{n}) - S(f,P, \eta_{1},\dots,\eta_{n}) \rvert + \underbrace{ \lvert S(f,P, \eta_{1},\dots,\eta_{n}) - \mathrm{L}(f,P)\rvert.   }_{ < \varepsilon } 
\end{aligned}
$$
Finalmente, 
$$
\begin{aligned}
&\lvert S(f,P, \xi_{1},\dots,\xi_{n}) - S(f,P, \eta_{1},\dots,\eta_{n}) \rvert\\
\leq &\lvert S(f,P, \xi_{1},\dots,\xi_{n}) - I) \rvert + \lvert I - S(f,P, \eta_{1},\dots,\eta_{n}) \rvert < 2\varepsilon
\end{aligned}
$$

#### Ejemplo
Considere $f:[0,1] \to \mathbb{R}$ tal que 
$$
f(x) = \begin{cases}
a, x \in \mathbb{Q}\\ \\
0, x \not\in \mathbb{Q}
\end{cases}
$$
para $a >0$. Sea $P$ una partición $\{ a_{0} = 0 < a_{1}<a_{2}<...<a_{n}=1 \}$. Entonces, 
$$
\begin{aligned}
M_{i} &= \sup \{ f(x):a_{i}\leq x\leq a_{i+1} \}  = a \\
m_{i} &= \inf \{ f(x): a_{i} \leq  x a_{i+1} \} = 0.
\end{aligned}
$$
Luego $U(f, P) = \sum_{i=0}^{n-1} a (a_{i+1}-a_{i}) = a$ y $L(f,p) = \sum_{i=1}^{n-1} 0(a_{i+1}-a_{i})=0$. 

Por tanto $U(f,P) - L(f,P) = a$, i.e., no se puede hacer arbitrariamente pequeño. 

### Truco para construir particiones crecientes
Probaremos la [[Integral de Riemann#Teorema (Caracterización UL de la integral de Riemann)|caracterización UL]] usando un truco que permite construir particiones cada vez más finas.

***Prueba:*** ($\impliedby$): Sea $\varepsilon>0$ y $n \in \mathbb{N}$. Entonces existe una partición $P_{n}$ tal que 
$$
\lvert U(f,P_{n}) - L(f, P_{n}) \rvert < \frac{\varepsilon}{n}.
$$
Sea $P_{1}' = P_{1}$ y defina $P_{m}' = \bigcup_{i=1}^{m} P_{i}$. Entonces $P_{n}' \subseteq P_{n+1}'$ y $P_{n} \subseteq P_{n}'$. Sabemos que 
$$
\begin{aligned}
U(f, P_{n}') &\geq U(f, P_{n+1}') \\
L(f, P_{n+1}') &\geq L(f,P_{n}')
\end{aligned}
$$
y que las sucesiones son acotadas. Entonces 
$$
\begin{aligned}
\lim_{ n \to \infty } U(f, P_{n}')  &= L_{1} \\
\lim_{ n \to \infty } L(f, P_{n}') &= L_{2}.
\end{aligned}
$$
Además, note que 
$$
\begin{aligned}
L_{1} &\leq  U(f, P_{n}') \\
L_{2} &\geq L(f, P_{n}') \\
\implies 0 \leq  L_{1} - L_{2} &\leq U(f,P_{n}') - L(f,P_{n}') < \frac{\varepsilon}{n}.
\end{aligned}
$$
Como esto se cumple para todo $\varepsilon>0$, concluimos que $L_{1} = L_{2} = I$.

($\implies$): Sea $P$ una partición tal que $P_{N}' \subseteq P$. Entonces 
$$
S(f, P, \xi_{1},\dots,\xi_{n}) - I \leq  U(f, P) - L_{1} \leq  U(f, P_{N}') - L_{1} < \varepsilon,
$$
donde $N$ es tal que, para $n\geq N$
$$
\begin{aligned}
0 &< U(f, P_{n}) - L_{1} < \varepsilon \\
0 &< L_{2} - L(f, P_{n}) < \varepsilon,
\end{aligned}
$$
Luego, $S(f, P, \xi_{1}, \dots, \xi_{n}) - I< \varepsilon$. Por otro lado,  
$$
S(f, P, \xi_{1}, \dots, \xi_{n}) - I \geq L(f,P) - L_{2} > -\varepsilon.
$$
Concluimos que si $P_{N}' \subseteq P$, entonces 
$$
\lvert S(f,P,\xi_{1},\dots,\xi_{n}) - I \rvert <\varepsilon
$$
> Consejo para trabajar con U y L:
> 1. Construir la [[Sucesiones|sucesión]] de particiones.
> 2. Considerar particiones más finas.
> 3. Acotar por arriba con $U$ y por debajo con $L$.

### Lema (Creciente implica R-integrable)
Sea $f:[a,b] \to \mathbb{R}$ creciente. Entonces $f$ es Riemann integrable

 ***Prueba:*** Sea $f:[a,b] \to \mathbb{R}$ creciente. Tome 
$$
P = \{ a_{0}=a<a_{1}<a_{2}< \dots < a_{n} = b \}.
$$
Entonces, 
$$
U(f,P) = \sum_{i=0}^{n} M_{i}(a_{i+1}-a_{i}),
$$
con $M_{i} = \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \} = f(a_{i+1})$. 
De igual forma, $m_{i} = \inf \{ f(x): a_{i} \leq x \leq a_{i+1} \} = f(a_{i})$. Ahora, 
$$
\begin{aligned}
U(f,P) - L(f,P) &= \sum_{i=0}^{n-1} (M_{i} - m_{i})(a_{i+1}-a_{i}) \\
&= \sum_{i=0}^{n-1}(f(a_{i+1})-f(a_{i}))(a_{i+1}-a_{i}). 
\end{aligned}
$$
Sea $P_{\varepsilon}$ una partición tal que $0<(a_{i+1}-a_{i})< \frac{\varepsilon}{f(b)-f(a)}$. Entonces, 
$$
\begin{aligned}
U(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) &= \sum_{i=0}^{n-1} (f(a_{i+1})-f(a_{i}))(a_{i+1}-a_{i}) \\
&< \sum_{i=0}^{n-1} \frac{\varepsilon}{f(b)-f(a)} (f(a_{i+1})-f(a_{i})) \\
&= \varepsilon,
\end{aligned}
$$
Así, $0 < U(f,P) - L(f,P) < \varepsilon$. Finalmente, si $P \supseteq P_{\varepsilon}$, entonces 
$$
\begin{aligned}
U(f,P_{\varepsilon}) &\geq U(f,P) \\
L(f, P) &\geq L(f, P_{\varepsilon})
\end{aligned} \\
\implies 0 <U(f,P) - L(f,P) \leq u(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) < \varepsilon
$$

### Teorema (Continuidad implica R-integrabilidad)
Si $f:[a,b] \to \mathbb{R}$ continua. Entonces es Riemann integrable.

***Prueba:***  Sean $f:[a,b]\to \mathbb{R}$ acotada. Entonces, si $M_{i} = \sup \{ f(x) : a_{i}\leq x\leq a_{i+1} \}$, y $m_{i} = \inf \{ f(x):a_{i}\leq x<a_{i+1} \}$.
$$
\begin{aligned}
U(f,P) &= \sum_{i=0}^{n-1} M_{i}(a_{i+1}-a_{i}) \\
L(f,P) &= \sum_{i=0}^{n-1} m_{i}(a_{i+1}-a_{i}) \\
U(f,P)-L(f,P) &= \sum_{i=0}^{n-1} (M_{i}-m_{i})(a_{i+1}-a_{i}).
\end{aligned}S
$$
Si $f$ es continua, entonces existen $\xi_{i} ,\eta_{i} \in [a_{i},a_{i+1}]$ tales que $f(\xi_{i}) = M_{i}$, y $f(\eta_{i}) = m_{i}$. Además, como $f$ es continua en un intervalo cerrado, entonces es uniformemente continua, i.e., para todo $\varepsilon>0$ existe $\delta >0$ tal que para todos $x,y \in [a,b]$ si $\lvert x-y \rvert < \delta$ entonces $\lvert f(x) - f(y) \rvert < \varepsilon$. Tome $P_{\varepsilon}$ tal que $\lvert a_{i+1}-a_{i} \rvert < \delta$, entonces $\lvert \xi_{i} - \eta_{i} \rvert < \delta$ y en consecuencia $\lvert f(\xi_{i}) - f(\eta_{i}) \rvert < \varepsilon$. Luego 
$$
U(f,P) - L(f,P) < \sum_{i=0}^{n-1} \varepsilon(a_{i+1}-a_{i}) = \varepsilon(b-a). 
$$

#### Ejemplo 
Muestre que $f:[0,1] \to \mathbb{R}$ tal que 
$$
f(x) \begin{cases}
=a \text{ si } x \in \mathbb{Q} \\
=0 \text{ si } x \not\in \mathbb{Q}
\end{cases}.
$$
no es R-integrable. 

***Prueba:*** Considere una partición $P = \{ a_{0} = a < a_{1} < \dots < a_{n} = b \}$. Note que $M_{i} = a$ y  $m_{i} = 0$ para todo $i \in \{ 0,1,\dots,n-1 \}$. Luego, $U(f,P) - L(f,P) = a$.

### Definición (Norma de una partición). 
Sea $P = \{ a_{0} = a < a_{1} < \dots <a_{n} = b \}$ una partición de $[a,b]$. Defina la norma de la partición como 
$$
\lVert P \rVert = \max \{ \lvert a_{i+1}-a_{i} \rvert: 0\leq i\leq N-1  \}.
$$

### Teorema (Norma y continuidad)
Sea $f:[a,b] \to \mathbb{R}$ acotada. Asuma que para todo $\varepsilon>0$ existe $\delta$ tal que si $\lVert P \rVert < \delta$ entonces $\lvert U(f,P) - L(f,P) \rvert < \varepsilon$. Entonces $f$ es Riemann integrable.

***Prueba:*** Dado $\varepsilon>0$, existe $\delta > 0$ tal que si $\lVert P \rVert < \delta$ entonces $\lvert U(f,P) -  L(f,P) \rvert < \varepsilon$. Sea $P_{\varepsilon}$ tal que $\lVert P_{\varepsilon} \rVert < \delta$. Tome $P \supseteq P_{\varepsilon}$. Entonces 
$$
\begin{aligned}
U(f,P) <& U(f, P_{\varepsilon}),\\
L(f,P_{\varepsilon}) <& L(f,P).
\end{aligned}
$$
Entonces 
$$
0 < U(f,P) - L(f,P) < u(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) < \varepsilon.
$$

### Teorema (Riemann Integrabilidad y composición) 
Sea $f:[a,b] \to \mathbb{R}$ Riemann integrable tal que $f([a,b]) \subseteq [c,d]$. Si $g:[c,d] \to \mathbb{R}$ es continua, entonces $g \circ f: [a,b] \to \mathbb{R}$ es Riemann integrable. 

***Prueba:*** Sea $\varepsilon, \varepsilon_{1} > 0$. Sabemos que existe $\delta>0$ tal que si $\lvert x-y \rvert$ entonces $\lvert g(x) - g(y) \rvert < \varepsilon$. Además existe $P_{\varepsilon_{1}}$ tal que si $P = \{ a_{0} = a <a_{1}<...<a_{n} = b \} \supseteq P_{\varepsilon_{1}}$ entonces
$$
\begin{aligned}
\lvert U(f,P) - L(f,P) \rvert < \varepsilon_{1} \iff 0 \leq  \sum_{i=1}^{n-1} (M_{i}-m_{i}) (a_{i+1}-a_{i}) < \varepsilon_{1}
\end{aligned}
$$
donde $M_{i} = \sup \{f(x):a_{i}\leq x \leq a_{i+1}\}$ y $m_{i} = \inf \{ f(x):a_{i}\leq x\leq a_{i+1} \}$.
Ahora, 
$$
U(g\circ f, P) - L(g \circ f, P) = \sum_{i=0}^{n-1} (\tilde{M_{i}}- \tilde{m_{i}}) (a_{i+1}-a_{i})
$$
con $\tilde{M_{i}} = \sup \{(g \circ f)(x):a_{i}\leq x \leq a_{i+1}\}$ y  $\tilde{m_{i}} = \inf \{(g \circ f)(x):a_{i}\leq x \leq a_{i+1}\}$.

Ahora, considere los siguientes casos:
**Caso 1**: $M_{i} - m_{i} < \delta$, entonces $\lvert f(x)- f(y) \rvert < \delta$ para todo $x,y \in [a_{i},a_{i+1}]$. Entonces, 
$$
\lvert (g \circ f)(x) - (g \circ f)(y) \rvert < \varepsilon.
$$
Así $\tilde{M_{i}} - \tilde{m_{i}} \leq \varepsilon$. Luego, 
$$
\sum_{\text{Caso 1}} (\tilde{M_{i}} - \tilde{m_{i}})(a_{i+1}-a_{i}) \leq \sum_{\text{Caso 1}} \varepsilon(a_{i+1}-a_{i}) \leq  \sum_{i=0}^{n-1} \varepsilon (a_{i+1}-a_{i}) = \varepsilon(b-a).
$$
**Caso 2:** $M_{i} - m_{i} \geq \delta$. Sea $-c < g(f(c)) < c$ para $x \in [a,b]$ (sabemos que es acotada porque es continua en un intervalo cerrado). Entonces $\tilde{M_{i}} \leq c$, $\tilde{m_{i}}\geq - c$, y por tanto $\tilde{M_{i}} - \tilde{m_{i}} \leq 2c$. Entonces 
$$
\begin{aligned}
\sum_{\text{Caso 2}}  (\tilde{M_{i}} - \tilde{m_{i}})(a_{i+1}-a_{i}) &\leq \sum_{\text{Caso 2}} \frac{2c}{\delta} \delta (a_{i+1}-a_{i})  \\
&\leq  \frac{2c}{\delta} \sum_{\text{Caso 2}} (M_{i} - m_{i})(a_{i+1}-a_{i})A \\
&\leq \frac{2c}{\delta}(U(f,P) - L(f,P)) < \frac{2c}{\delta} \varepsilon_{1}.
\end{aligned}
$$

#### Ejemplo 
Sean $f:[a,b] \to \mathbb{R}$, $g:[a,b] \to \mathbb{R}$ Riemann integrables. Entonces las siguientes son Riemann integrables:
1. $\lvert f \rvert$
2. $(f)^{n}, n \in \mathbb{N}$
3. $\lvert f \rvert^{1/n}$
4. $fg = \frac{(f+g)^{2}-f^{2}-g^{2}}{2}$.
 
### Lema (Integrabilidad en sub-intervalos):
Sea $f:[a,b] \to \mathbb{R}$ Riemann integrable. Tome $a<x<b$. Entonces $f$ es Riemann integrable en $[a,x]$.

***Prueba:*** Ejercicio.

Defina la función $F(x) = \int_{a}^{x} f(t) \, dt$. 

### Lema (Acotación de la integral de Riemann) 
Sea $f:[a,b] \to \mathbb{R}$ Riemann integrable. Entonces 
$$
m(b-a) \leq \int_{a}^{b} f(x) \, dx \leq  M(b-a) 
$$
***Prueba:*** Sea $f:[a,b] \to \mathbb{R}$ acotada. Tome $M = \sup\{ f(x): a \leq x \leq b \}$ y $m = \inf\{ f(x): a \leq x \leq b \}$. Considere una partición $P = \{ a_{0}=a<a_{1}<...< a_{n} = b \}$ y considere la suma de Riemann 
$$S(f,P,\xi_{1},\dots,\xi_{n}) = \sum_{i=0}^{n} f(\xi_{i})(a_{i+1}-a_{i}) \leq \sum_{i=0}^{n} M(a_{i+1}-a_{i}) = M(b-a).$$ De igual manera, $m(b-a) \leq S(f,P,\xi_{1},\dots \xi_{n}) \leq M(b-a)$. Además, para todo $\varepsilon>0$, 
$$
I-\varepsilon \leq S(f,P,\xi_{1},\dots,\xi_{n}) \leq I+\varepsilon
$$
En particular, para $\varepsilon$ tal que $m(b-a) \leq I-\varepsilon$ y $I+\varepsilon \leq M(b-a)$,

#### Ejercicio 
Sea $f;[a,b] \to \mathbb{R}$ Riemann integrable. Pruebe que $f:[x,y] \to \mathbb{R}$ es Riemann integrable si $a\leq x\leq y \leq b$ , Entonces $F(x) = \int_{a}^{x} f(t)\, dt$ satisface que si $x<y$, 
$$
\begin{aligned}
F(y) &= \int_{a}^{y} f(t) \, dt = \int_{a}^{x} f(t) \, dt + \int_{x}^{y} f(t) \, dt \\
&= F(x) + \int_{x}^{y} f(t)  \, dt.
\end{aligned}
$$

### Teorema Fundamental del Cálculo

Sea $f:[a,b] \to \mathbb{R}$ continua. SI $F(x) = \int_{a}^{x} f(x)  \, dx$ entonces $F'(x) = f(x)$.

***Prueba:*** Como resultado del ejercicio anterior, $-F(x)+F(y) = \int_{x}^{y} f(t) \, dt$. Además, por el lema de acotación de la integral, si $m = \inf \{ f(x):a\leq x\leq b \}$ y $M = \sup \{ f(x):a\leq x\leq y \}$, 
$$
m(y-x)\leq -F(x)+F(y) \leq M(y-x).
$$
Concluimos que $\lvert F(x)-F(y) \rvert \leq \max \{ \lvert M \rvert, \lvert m \rvert \}(y-x)$.  Sea $x_{0} \in (a,b).$ Probaremos que $\lim_{y \to x_{0}} \frac{F(y)-F(x_{0})}{y-x_{0}} = f(x_{0})$. Note que 
$$ \frac{\int_{x_{0}}^{y} f(x_{0}) \, dx}{y-x_{0}} = \frac{(y-x_{0})f(x_{0})}{y-x_{0}} = f(x_{0}). \tag{1}
$$
Sea $\varepsilon>0$ fijo y arbitrario. Entonces existe $\delta>0$ tal que si $\lvert x-y \rvert < \delta$ entonces $\lvert f(x)-f(y) \rvert < \varepsilon$. Entonces
$$\begin{aligned}
\lim_{ y \to x_{0} } \frac{F(y)-F(x_{0})}{y-x_{0}} - f(x_{0}) &= \lim_{ y \to x_{0} } \frac{\int_{x_{0}}^{y} f(x) \, dx}{y-x_{0}} - \frac{\int_{x_{0}}^{y} f(x_{0}) \, dx}{y-x_{0}}. \\
&=\lim_{ y \to x_{0} } \frac{ \int_{x_{0}}^{y} (f(x)-f(x_{0})) \, dx }{y-x_{0}} = 0.
\end{aligned}
$$
pues si $\lvert y-x_{0} \rvert < \delta$ y $y>x_{0}$ entonces 
$$
\frac{\left\lvert  \int_{x_{0}}^{y} (f(x)-f(x_{0})) \, dx  \right\rvert }{\lvert y-x_{0} \rvert } \leq  \frac{ \int_{x_{0}}^{y} \lvert f(x)-f(x_{0}) \rvert \, dx  }{\lvert y-x_{0} \rvert } \leq \frac{\varepsilon (y-x_{0})}{y-x_{0}} = \varepsilon.
$$
El caso cuando $x_{0}<y$ es análogo.

### Definición (Antiderivada):
 Sea $f:[a,b] \to \mathbb{R}$. Decimos que $F:[a,b]\to \mathbb{R}$ es la antiderivada de $f$ si $F'(x) = f(x)$ para $a<x<b$. 
 
 Acabamos de probar que si $f$ es continua, existe la antiderivada. Asuma ahora que $f:[a,b] \to \mathbb{R}$ es derivable.

### Teorema (Integral de la derivada)
Sea $f:[a,b] \to \mathbb{R}$. Asuma que $f'[a,b] \to \mathbb{R}$ es Riemann integrable. Entonces $\int_{a}^{b} f'(x) \, dx = f(b)-f(a)$

***Prueba:*** Como $f'$ es Riemann integrable, existe $I$ tal que dado $\varepsilon>0$, existe $P_{\varepsilon}$ tal que para toda partición $P = \{ a_{0}=a<a_{1}<...<a_{n}=b \} \supseteq P_{\varepsilon}$ y para todos $a_{i}\leq\eta_{i}\leq a_{i+1}$, se cumple que $\lvert S(f',P, \eta_{1},\dots,\eta_{n}) \rvert < \varepsilon$.  Por el teorema del valor medio, existen $\xi_{i}$ tales que ,$f'(\xi_{i})(a_{i+1}-a_{i}) = f(a_{i+1})-f(a_{i})$. Luego, 
$$
S(f',P, \xi_{1},\dots,\xi_{n}) = \sum_{i=0}^{n-1} f'(\xi_{i})(a_{i+1}-a_{i}) = \sum_{i=0}^{n-1} f(a_{i+1}) - f(a_{i}) = f(b)-f(a). 
$$
Considere ahora $\lvert (f(b)-f(a)) - I \rvert$. Desarrollando 
$$
\lvert (f(b)-f(a)) - I \rvert = \lvert S(f',P, \xi_{1},\dots, \xi_{n}) - I \rvert < \varepsilon.
$$
Luego, $\lvert (f(a) - f(b)) - I \rvert < \varepsilon$ para todo $\varepsilon<0$. Por lo tanto $f(a)-f(b) = I$.

### Lema (Integración por partes)
Sean $f:[a,b] \to \mathbb{R}$ y $g:[a,b] \to \mathbb{R}$ diferenciables tales que $f'$ y $g'$ son ambas Riemann integrables. Entonces $(fg)' = f'g+fg'$ es Riemann integrable. Además 
$$
\begin{aligned}
\int_{a}^{b} (fg)' \, dx &= \int_{a}^{b} (f'(x)g(x)+f(x)g'(x))  \, dx =f(b)g(b) - f(a) g(a) \\
\implies \int_{a}^{b} f'(x) g(x)  \, dx &= f(b)g(b)-f(a)g(a) - \int_{a}^{b} f(x) g'(x)  \, dx .
\end{aligned}
$$

#### Ejercicio 
Sea $f:[a,b]\to \mathbb{R}$ acotada y Riemann integrable. Suponga que existen $m, M \in \mathbb{R}$ una partición $P_{\varepsilon}$ tal que para toda partición $P \supseteq P_{\varepsilon}$ existen $\xi_{1},\dots,\xi_{n}$ tales que 
$$
m\leq S(f,P, \xi_{1},\dots, \xi_{n}) \leq  M.
$$
Entonces $m \leq \int_{a}^{b} f(x)  \, dx \leq M$.

### Teorema (Cambio de variable) 
Asuma que $f:[a,b] \to \mathbb{R}$ es continua y sea $\phi:[c,d] \to [a,b]$ con derivada continua, de modo que $\phi([c,d]) \subseteq [a,b]$. Entonces 
$$
\int_{c}^{d} f(\phi(u)) \phi'(u) \, du = \int_{\phi(c)}^{\phi(d)} f(x)  \, dx. 
$$

***Prueba:*** Considere $F(x) = \int_{\phi(c)}^{x} f(t)  \, dt$. Considere $F(\phi(t))$. Note que 
$$
[F(\phi(t))]' = F'(\phi(t)) \phi'(t)
$$
Luego, 
$$
\begin{aligned}
\int_{c}^{d} F'(\phi(t)) \phi'(t) \, dt &= \int_{c}^{d} [F(\phi(t))]' \, dt  \\
&=F(\phi(d)) - F(\phi(c)) \\
&=\int_{\phi(c)}^{\phi(d)} f(t) \, dt - \int_{\phi(c)}^{\phi(c)} f(t)  \, dt \\
&= \int_{\phi(c)}^{\phi(d)} f(t) \, dt.
\end{aligned}
$$
Finalmente, 
$$
\begin{aligned}
\int_{\phi(c)}^{\phi(d)}f(t)  \, dt &= \int_{c}^{d} F'(\phi(t)) \phi'(t) \, dt \\
&= \int_{c}^{d} f(\phi(t)) \phi'(t) \, dt. 
\end{aligned}
$$

### Teorema (Valor medio de integrales) 

Sea $f:[a,b] \to \mathbb{R}$ continua y Riemann integrable. Entonces existe $c \in [a,b]$ tal que $f(c) = \frac{1}{b-a}\int_{a}^{b} f(x) \, dx$

***Prueba:*** Tome $M = \sup \{ f(x):a\leq x \leq b \}$ y $m =\inf \{ f(x):a\leq x \leq b \}$.
$$
m \leq \frac{1}{b-a} \int_{a}^{b} f(x) \, dx \leq  M
$$
Como $f$ es continua, existen $x_{1}, x_{2} \in [a,b]$ tal que $M = f(x_{2})$ y $m = f(x_{1})$. Luego, 
$$
f(x_{1}) \leq \frac{1}{b-a} \int_{a}^{b} f(x) \, dx \leq  f(x_{2}).
$$
Por el teorema del valor medio, existe $c \in [a,b]$ tal que $f(x) = \frac{1}{b-a}\int_{a}^{b} f(x) \, dx$.

### Teorema (Valor medio de integrales v2)
Sean $f:[a,b] \to \mathbb{R}$ continua y no negativa, $g:[a,b] \to \mathbb{R}$ decreciente, positiva y acotada. Entonces existe $c \in [a,b]$ tal que 
$$
F(c) g(a) = \int_{a}^{b} f(x) g(x) \, dx = g(a) \int_{a}^{c} f(x) \, dx.
$$

***Prueba:*** Sea $f:[a,b] \to \mathbb{R}$ continua y $g:[a,b] \to \mathbb{R}$ Riemann integrable. Recordemos que 
$$
F(x) = \int_{a}^{x} f(t) \, dt \implies F'(x) = f(x). 
$$
Sea $P = \{ a_{0}=a<a_{1}< \dots<a_{n} = b \}$ y tome (por el teorema del valor intermedio)
$$
\begin{aligned}
\frac{F(a_{i+1})-F(a_{i})}{a_{i+1}-a_{i}} &= F'(\xi_{i}) = f(\xi_{i}) \\ 
\iff f(\xi_{i})(a_{i+1}-a_{i}) &= F(a_{i+1}) - F(a_{i}).
\end{aligned}
$$
Considere $$\begin{aligned}
\sum_{i=0}^{n-1} f(\xi_{i}) g(\xi_{i}) (a_{i+1}-a_{i}) &= \sum_{i=0}^{n-1} g(\xi_{i})(F(a_{i+1}-F(a_{i})) \\
&= \sum_{i=0}^{n-1} g(\xi_{i}) F(a_{i+1}) - \sum_{i=0}^{n-1} g(\xi_{i}) F(a_{i}) \\
&=\sum_{i=1}^{n} g(\xi_{i-1}) F(a_{i}) - \sum_{i=0}^{n-1} g(\xi_{i}) F(a_{i}) \\
&= \left( \sum_{i=1}^{n-1} F(a_{i})(g(\xi_{i-1}) - g(\xi_{i}))  \right) + g(\xi_{n-1})F(a_{n})- g(\xi_{0})\underbrace{ F(a_{0}) }_{ =0 } \\
&= \underbrace{ \left( \sum_{i=1}^{n-1} F(a_{i})(g(\xi_{i-1}) - g(\xi_{i}))  \right) + g(\xi_{n-1}) F(b).  }_{ (\ast) }
\end{aligned}$$
Tome $F(z_{1}) = \sup \{ F(x):a\leq x\leq b \}$. Si $g$ es decreciente, entonces 
$$
\begin{aligned}
(\ast) &\leq \left( \sum_{i=1}^{n-1} F(z_{1})(g(\xi_{i-1}) - g(\xi_{i}))  \right) + g(\xi_{n-1}) F(b) \\
&= (g(\xi_{0}) - g(\xi_{n-1}))F(z_{1}) + F(b) g(\xi_{n-1}).
\end{aligned}
$$
 Además, como $g(x)\geq 0$, entonces tenemos que 
$$
\begin{aligned}
(\ast) &\leq (g(\xi_{0}) - g(\xi_{n-1}))F(z_{1}) + F(b) g(\xi_{n-1}) \\
&\leq  (g(\xi_{0}) - g(\xi_{n-1}))F(z_{1}) + F(z_{1}) g(\xi_{n-1}) \\
&= F(z_{1}) g(\xi_{0}),
\end{aligned}
$$
pues $F(b) \leq F(z_{1})$. Como $0\leq F(x)$ para todo $x$ entonces $(\ast) \leq F(z_{1})g(a)$. Concluimos que $\sum_{i=0}^{n-1} f(\xi_{i}) g(\xi_{i})(a_{i+1}-a_{i}) \leq F(z_{1}) g(a)$, donde $F(z_{1}) = \sup \{ F(x): a\leq x\leq b  \}$.

Con un razonamiento análogo, podemos probar que $\sum_{i=0}^{n-1} (a_{i+1}-a_{i}) \geq F(z_{2})g(a)$, donde  $F(z_{2}) = \inf \{ F(x): a\leq x\leq b  \}$. Luego, 
$$
\begin{aligned}
g(a) F(z_{1}) \geq  \int_{a}^{b} f(x) g(x) \, d \geq  g(a) F(z_{2}) \\
\iff F(z_{1}) \geq \frac{1}{g(a)}\int_{a}^{b} f(x)g(x) \, dx  \geq  F(z_{2})
\end{aligned}
$$
Luego, por el teorema del valor medio de integrales, se concluye el resultado.

### Partición de intervalos disjuntos
Considere dos intervalos $[a,c]$ y $[c,b]$ y $f:[a.b] \to \mathbb{R}$. Sean $P_{1}, P_{2}$ particiones de $[a,c]$ y $[c,b]$, respectivamente. Si $P_{1} = \{ a_{0}=a<a_{1}< \dots < a_{m}=c\}$ y $P_{2} = \{ b_{0} = c < \dots <b_{k} = b \}$, entonces $P_{1} \cup P_{2} = \{ a_{0}=a< \dots < a_{m} = b_{0} = c < \dots < b_{k} = b \}$.
Luego, 
$$
\begin{aligned}
U(f, P_{1} \cup P_{2}) &= U(f,P_{1}) + U(f,P_{2}) \\
L(f, P_{1} \cup P_{2}) &= L(f,P_{1}) + L(f,P_{2}),
\end{aligned}
$$
pues por ejemplo, para la suma inferior, 
$$
L(f,P_{1} \cup P_{2}) = \sum_{i=0}^{n-1} m_{i} (a_{i+1}-a_{i}) + \sum_{i=0}^{k-1} m_{i}'(b_{i+1}-b_{i}),
$$
donde $m_{i} = \inf \{ f(x):a_{i}\leq x\leq a_{i+1} \}$, $m_{i}' = \inf \{ f(x): b_{i}\leq x \leq b_{i+1}\}$.

## Discontinuidad evitable en un extremo del intervalo
Sea $f:[a,b] \to \mathbb{R}$ continua en $(a,b]$ tal que $\lim_{ x \to a^{+}} \ell_{1} \in \mathbb{R}$. Entonces, $f$ es Riemann integrable en $[a,b]$.

***Prueba:*** Note que:
1. Si $0<\alpha<b-a$, $f:[a + \alpha, b] \to \mathbb{R}$ es continua, i.e, Riemann integrable. x
2. Dado $\varepsilon>0$, existe $\delta>0$ tal que si $0<x-a<\delta$ entonces $\lvert f(x)-\ell_{1} \rvert< \frac{\varepsilon}{2}$.
Entonces, si $a<x,y<a+\delta$, tenemos que 
$$
\lvert f(x)-f(y) \rvert \leq  \lvert f(x)- \ell_{1} \rvert + \lvert \ell_{1}-f(y) \rvert < \varepsilon.\ \tag{*}
$$
Sea $P_{1} =  \left\{  a_{0}=a < \dots < a_{m} = a+ \frac{\delta}{2}  \right\}$ una partición de $\left[ a, a + \frac{\delta}{2} \right]$,  Entonces 
$$
\begin{aligned}
U(f,P_{1})  - L(f, P_{1}) = \sum_{i=0}^{m-1} (M_{i} - m_{i})(a_{i+1}-a_{i}).
\end{aligned}
$$
Por $(*)$, note que $f(x) - f(y) \leq M_{i} - m_{i} < \varepsilon$. Luego 
$$
\begin{aligned}
U(f, P_{1}) - L(f, P_{1}) \leq \sum_{i=0}^{m-1} \varepsilon(a_{i+1}-a_{i}) = \varepsilon \left( a+\frac{\delta}{2} - a \right) = \frac{\varepsilon \delta}{2}.
\end{aligned}
$$
Recordemos que $f:\left[ a+\frac{\delta}{2},b \right] \to \mathbb{R}$ es continua, i.e. Riemann integrable, entonces existe $P_{\varepsilon} = \left\{  b_{0}=a+\frac{\delta}{2} < \dots < b_{k} = b  \right\}$ tal que para toda partición $P \supseteq P_{\varepsilon}$ entonces 
$$
U(f,P)-L(f,P) < \frac{\varepsilon}{2}.
$$
Necesitamos $P_{\varepsilon}'$ de $[a,b]$. Tome $P_{\varepsilon}' = \left\{  a = c_{0} < c_{1} = a+ \frac{\delta}{2} = b_{0} < \dots < b_{k} = c_{k+1} = b  \right\} = P_{\varepsilon} \cup \left\{  a, a+ \frac{\delta}{2}  \right\}$. Entonces, 
$$
\begin{aligned}
&U(f, P_{\varepsilon}') - L(f, P_{\varepsilon}') \\&= U\left( f,\left\{  a,a+\frac{\delta}{2}  \right\} \right) - L\left( f,\left\{  a,a+\frac{\delta}{2}  \right\} \right) + U(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) \\
& < \frac{\varepsilon \delta}{2} + \frac{\varepsilon}{2}.
\end{aligned}
$$

 > Nota: Tomamos la unión solo con $\left\{  \alpha, \alpha + \frac{\delta}{2}  \right\}$ porque acotamos $U-L$ para toda partición de $[a,a+\delta/2]$N. En particular, tomamos la partición más sencilla posible para construir un refinamiento y conservar las propiedades desarrolladas en ambos subintervalos.

## Otros resultados útiles

![[Pasted image 20250605105619.png]]

## Algunos trucos útiles.
- La unión entre particiones genera refinamientos de todas ellas, lo que es útil si se quiere extender resultados a particiones más finas.
- Cuando se trabaja en torno a un punto problemático $x_{0}$, es útil construir una partición alrededor de este punto, i.e., que incluya los puntos $x_{0}-\delta$ y $x_{0} + \delta$, con $\delta>0$.
- Si se sabe que una función es Riemann integrable, en ocasiones es útil considerar una sucesión de particiones $P_{n}$ que salen de la definición de Riemann-integrabilidad para $\frac{1}{n}$ (o para $\frac{\varepsilon}{n}$ si se busca probar la Riemann integrabilidad de otra función). Usualmente se puede trabajar con algún refinamiento de estas particiones. Usualmente esto sirve para cuando se quiere probar la convergencia a la integral.
- Para probar los teoremas de valor medio, usualmente basta acotar la expresión buscada a una función evaluada en dos extremos de un intervalo.