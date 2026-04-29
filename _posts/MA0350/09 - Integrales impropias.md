#Mate #MA0350
Fecha:  2025-06-03

Sabemos [[Integral de Riemann|integrar]] funciones sobre intervalos $[a,b]$. Ver también: [[Criterios de convergencia de series|criterios de convergencia]] (analogía con series). Se puede definir $\int_{a}^{\infty}  f(x)\, dx$. 
### Definición (Convergencia de integral impropia)
Sea $f:[a,+\infty] \to \mathbb{R}$ Riemann integrable en $[a,b]$ para todo $b>a$. Decimos que $\int_{a}^{\infty} f(x) \, dx$ converge si $\lim_{ b \to \infty } \int_{a}^{b} f(x)  \, dx$ existe. 

#### Ejemplo 
Considere $\int_{1}^{\infty}  \, \frac{1}{x^{p}}dx$ . Como 
$$
\int_{1}^{b} x^{-p} \, dx = \frac{x^{1-p}}{1-p} \biggr\rvert_{1}^{b } = \frac{b^{1-p}}{1-p} - \frac{1}{1-p}.
$$
Note que 
$$-\frac{1}{1-p} \quad \text{si }p>1  
\lim_{ b \to \infty } \frac{b^{1-p}}{1-p} - \frac{1}{1-p} = \begin{cases}
-\frac{1}{1-p} \quad \text{si }p>1 \\
+\infty  \quad \text{si }p <1
\end{cases}
$$
Además, si $p=1$
$$
\int_{1}^{b} \frac{1}{x} \, dx = \ln b \to \infty.
$$

### Lema (Convergencia hacia cero de la función) 
Sea $f:[a,+\infty) \to \mathbb{R}$. Si $\lim_{ x \to \infty } f(x) = L \neq 0$, entonces $\int_{a}^{\infty} f(x) \, dx$ diverge.

***Prueba:***  Asuma que $\lim_{ x \to \infty } = \ell \neq 0$. Sabemos que dado $\varepsilon>0$, existe $M>0$ tal que si $x>M$ entonces $\lvert f(x)-L \rvert < \varepsilon$. Luego, si $x>M$, tenemos que $L - \varepsilon <f(x)<L+\varepsilon$. 
Si $L >0$, tome $\varepsilon>0$ tal que $L - \varepsilon > 0$. Entonces $L - \varepsilon < f(x)$ si $x>M$. Integrando, 
$$
\int_{M}^{b} (l - \varepsilon) \, dx = (b-M)(L-\varepsilon) \leq \int_{M}^{b} f(x) \, dx.
$$
Luego, 
$$
\lim_{ b \to \infty } \int_{a}^{b} f(x) \, dx = \lim_{ b \to \infty } \left( \int_{a}^{M} f(x)  \, dx  + \int_{M}^{b} f(x) \, dx + (l-\varepsilon)(b-M)  \right) = +\infty,
$$
Si $\ell<0$, entonces el razonamiento es análogo pero hacia $-\infty$.

Asuma que $\lim_{ b \to \infty } \int_{a}^{b} f(x) \, dx = I \in \mathbb{R}$. Dado $\varepsilon>0$ existe $M>0$ tal que si $b>M$, entonces 
$$
\left\lvert  \int_{a}^{b} f(x) \, dx -I  \right\rvert < \frac{\varepsilon}{2}.
$$
Tome $b_{2} > b_{1} > M$. Ahora, 
$$
\begin{aligned}
\left\lvert  \int_{b_{1}}^{b_{2}} f(x)  \, dx   \right\rvert &=  \left\lvert  \int_{a}^{b_{2}} f(x) \, dx - \int_{a}^{b_{1}} f(x)  \, dx    \right\rvert \\
&\leq \left\lvert  \int_{a}^{b_{1}} f(x) \, dx - I \right\rvert  + \left\lvert  \int_{a}^{b_{2}} f(x) \, dx - I   \right\rvert  < \varepsilon.
\end{aligned} 
$$
Concluimos que $\lvert  \int_{a}^{b_{1}} f(x) \, dx  \rvert < \varepsilon$.
### Lema  (Reducción a sucesiones)
$\int_{0}^{\infty}  f(x)\, dx$ converge a $L$ si dada $\{ x_{n} \}_{n=1}^{\infty} \subseteq [a,+\infty]$ tal que $x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$, tenemos que 
$$
\lim_{ n \to \infty } \int_{a}^{x_{n}}f(x)  \, dx = F(x_{n})\text{ existe y converge a } L.
$$
### Lema (Condición  de Cauchy de la integral impropia) 
Si dado $\varepsilon>0$, existe $M>0$ tal que $\left\lvert  \int_{c}^{d}  f(x)\, dx  \right\rvert < \varepsilon$, si $c,d > M$, entonces $\int_{0}^{\infty} f(x)  \, dx$ converge.

***Prueba:*** Sea $\{ x_{n} \}_{n=1}^{\infty} \subseteq [a,+\infty]$ tal que $x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$. Tome $z_{n} = \int_{a}^{x_{n}}  f(x)\, dx$. Sea $\varepsilon>0$, entonces existe $M \in \mathbb{N}$ tal que $\left\lvert  \int_{c}^{d}  f(x)\, dx  \right\rvert < \varepsilon$ para todos $c>d\geq M$. Ahora,  si tomamos $x_{n} < x_{m}$, entonces
$$
\lvert z_{n}-z_{m} \rvert = \left\lvert   \int_{x_{n}}^{x_{m}} f(x) \, dx   \right\rvert < \varepsilon.
$$
Sea $N \in \mathbb{N}$ tal que $x_{k}\geq M$ para todo $k\geq N$, que sabemos que existe porque $x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$.
Luego, si $n,m \geq N$, $\left\lvert  \int_{x_{n}}^{x_{m}} f(x) \, dx  \right\rvert < \varepsilon$. Entonces, $z_{n}$ es de Cauchy y converge.
Probaremos ahora que todas convergen al mismo límite. Sea $\{ y_{n} \}_{n=1}^{\infty} \subseteq [a, +\infty]$ tal que $y_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$. Hay que mostrar que 
$$
\int_{a}^{x_{n}} f(x) \, dx  - \int_{a}^{y_{n}}  f(x)  \, dx = \int_{\min\{ x_{n}, y_{n}\}}^{\max \{ x_{n},y_{n} \}} f(x)  \, dx   \underset{n \rightarrow \infty}{\longrightarrow} 0.
$$
Tome $N_{1}$ tal que $x_{n}, y_{n} \geq M$, entonces para $n\geq N_{1}$,
$$
\left\lvert  \int_{\min\{ x_{n},y_{n} \}}^{\max\{ x_{n},y_{n} \}} f(x)\, dx   \right\rvert < \varepsilon.
$$
 Conclúyase que cualesquiera dos sucesiones convergen al mismo valor.

### Teorema (Convergencia absoluta)
Si $\int_{a}^{\infty} \lvert f(x) \rvert \, dx$ converge, entonces $\int_{a}^{\infty} f(x) \, dx$ converge.

***Prueba:*** $\int_{0}^{\infty} f(x) \, dx$ existe si y solo si dado $\varepsilon>0$, existe $M>0$ tal que $\left\lvert\int_{c}^{d} f(x) \, dx \right\rvert < \varepsilon$ si $c,d \geq M$. Note que 
$$
\left\lvert  \int_{c}^{d} f(x) \, dx   \right\rvert < \int_{c}^{d} \lvert f(x) \rvert  \, dx.
$$
Luego, si $\int_{c}^{\infty} \lvert f(x) \rvert \, dx$ converge, dado $\varepsilon>0$, existe $M > 0$ tal que $\int_{c}^{d} \lvert f(x) \rvert \, d < \varepsilon$ si $c,d \geq M$. Por lo tanto, 
$$
\left\lvert  \int_{c}^{d} f(x) \, dx   \right\rvert \leq  \int_{c}^{d} \lvert f(x) \rvert  \, dx < \varepsilon.
$$
Entonces $\int_{a}^{\infty} f(x) \, dx$ converge. 

### Teorema (Comparación)
Si existe $c \in [a, \infty)$ tal que $0 \leq f(x) \leq g(x)$ para todo $x \geq c$, entonces:
1. $\int_{a}^{\infty} g(x) \, dx$ converge si  $\int_{a}^{\infty} f(x) \, dx$ converge.
2. $\int_{a}^{\infty} f(x) \, dx$ diverge si  $\int_{a}^{\infty} g(x) \, dx$ diverge.

***Prueba de (1):***  Asuma que $0 \leq f(x) \leq g(x)$ para todo $x \geq c$, con $a < c$.
Entonces 
$$
0\leq \int_{c}^{d} f(x) \, dx \leq \int_{c}^{d} g(x) \, dx. 
$$
Si $\int_{a}^{\infty} g(x) \, dx$ converge. Entonces existe $M\geq 0$ tal que para todos $\ell,q \geq M$ ,
$$
0 < \int_{\ell}^{q} g(x) \, dx < \varepsilon
$$
Luego $0<\int_{\ell}^{q} f(x) \, dx < \varepsilon$ y por tanto es de Cauchy y converge.
La prueba de 2 se deja como ejercicio. Una sugerencia es notar que $F(x) = \int_{a}^{u} f(u) \, du$ es creciente si $f(x)\geq_{0}$.

### Teorema (Comparación en el límite)
Sean $f:[a,\infty) \to \mathbb{R}$ y $g:[a,+\infty] \to \mathbb{R}$ tales que $0\leq f(x)\leq g(x)$ para $x\geq c$, donde $c>a$.
1. En caso de que $\lim_{ n \to \infty } \frac{f(x)}{g(x)} = \ell \neq 0$, $\int_{a}^{\infty} f(x) \, dx$ si y solo si $\int_{a}^{\infty} g(x)\, dx$ converge.
2. En caso de que $\lim_{ n \to \infty } \frac{f(x)}{g(x)} = \infty$, tenemos que 
	1. $\int_{a}^{\infty} g(x) \, dx$ converge si  $\int_{a}^{\infty} f(x) \, dx$ converge.
	2. $\int_{a}^{\infty} f(x) \, dx$ diverge si  $\int_{a}^{\infty} g(x) \, dx$ diverge.
***Prueba:*** Asuma que $\lim_{ n \to \infty } \frac{f(x)}{g(x)} = \ell \neq 0$. Dado $\varepsilon>0$, existe $M>0$ tal que para todo $x \geq M$, 
$$
\ell - \varepsilon < \frac{f(x)}{g(x)} < \ell + \varepsilon.
$$
Luego, si tomamos $\varepsilon < \ell$, entonces 
$$
0 \leq  (l-\varepsilon) g(x) \leq  f(x) \leq (l+\varepsilon) g(x).
$$
El resultado se sigue por el teorema de comparación. 
Por otro lado, si $\lim_{ n \to \infty } \frac{f(x)}{g(x)} = +\infty$. Dado $M>0$, existe $N>0$ tal que $\frac{f(x)}{g(x)} \geq M$ si $x>N$. Entonces, $f(x) \geq Mg(x)$ si $x\geq N$.

En el caso de integrales de otras especies calcular el limite hacia el punto problemático.
#### Ejemplo 
Sea $\Gamma(\alpha) = \int_{0}^{\infty} e^{-x} x^{\alpha-1} \, dx$ para $\alpha \geq 1$. Note que 
$$
\lim_{ x \to \infty } \frac{e^{-x}x^{\alpha-1}}{e^{-x/2}} = \lim_{ x \to \infty } e^{-x/2} x^{\alpha-1} = 0.
$$
Como 
$$
\int_{0}^{a} e^{x/2} \, dx = -\frac{1}{2} e^{-x/2} \biggr\rvert_{a}^{0} = \frac{1}{2} - \frac{1}{2} e^{-a/2} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{2},
$$
es decir, $\int_{0}^{\infty} e^{-x/2} \, dx$ converge y se concluye por comparación al límite que $\int_{0}^{\infty} e^{-x} x^{\alpha-1} \, dx$ converge.

### Ejercicio 
Muestre que $\Gamma(1) = 1$ y que $\Gamma(\alpha) = \alpha\Gamma(\alpha-1)$ para $\alpha \geq 2$.

### Teorema (Dirichlet)
Sean $f:[a,+\infty) \to \mathbb{R}$ y $g:[a, +\infty) \to \mathbb{R}$ funciones tales que 
	1. Existe $M>0$ tal que $\int_{a}^{b} f(x) \, dx \leq M$ para todos $a<b \in \mathbb{R}$.
	2. $g$ es decreciente y $\lim_{ x \to \infty } g(x) = 0$.
Entonces, $\int_{a}^{\infty} f(x)g(x) \, dx$ converge.

***Prueba:*** Dado $\varepsilon>0$, existe $K$ tal que $0\leq g(x) < \frac{\varepsilon}{M}$ para $x\geq K$. Además, dados $c,d\geq K$, tenemos que existe $c_{1} \in \mathbb{R}$ tal que 
$$
\int_{c}^{d} f(x)g(c) \, dx = g(c) \int_{c}^{c_{1}} f(x) \, dx,
$$
donde $c\leq c_{1} \leq d$. Entonces, para todos $d\geq c\geq k$
$$
\left\lvert  \int_{c}^{d} f(x)g(x) \, dx   \right\rvert =  g(c) \left\lvert  \int_{c}^{d} f(x) \, dx   \right\rvert < \frac{\varepsilon}{M} \cdot M = \varepsilon,
$$
y por tanto la integral converge.

#### Ejemplo 
Considere $\int_{0}^{\infty} \frac{\sin x}{x^{p}}\, dx$ para $p>0$. Note que $\lim_{ n \to \infty } \frac{1}{x^{p}} = 0$ y $\frac{1}{x^{p}}$ es decreciente. Además, 
$$
\left\lvert  \int_{a}^{b} \sin x \, dx   \right\rvert = \left\lvert -\cos x \biggr\rvert_{a}^{b }  \right\rvert = \lvert \cos b-\cos a \rvert \leq 2.
$$
Por lo tanto, converge.

#### Ejemplo 
Recordemos que $\int_{1}^{\infty} \frac{\sin x}{x} \, dx$ converge por Dirichlet. ¿Qué pasa con $\int_{\pi}^{\infty} \left\lvert  \frac{\sin x}{x}  \right\rvert  \, dx$?
Considere 
$$\int_{\pi}^{k \pi} \left\lvert  \frac{\sin x}{x}  \right\rvert \, dx = \sum_{j=1}^{k-1} \int_{j \pi}^{(j+1)\pi}  \left\lvert  \frac{\sin x}{x}
\right\rvert  \, dx. $$
Ahora, 
$$
\begin{aligned}
\frac{2}{\pi(j+1)} =\frac{1}{(j+1)\pi} \int_{j \pi}^{(j+1) \pi} \left\lvert  \sin x \right\rvert  \, dx &\leq  \int_{j \pi}^{(j+1)\pi} \left\lvert  \frac{\sin x}{x}  \right\rvert  \, dx \\
&\leq \frac{1}{j\pi} \int_{j \pi}^{(j+1) \pi} \left\lvert \sin x \right\rvert  \, dx = \frac{2}{j \pi}.
\end{aligned}
$$
Entonces, 
$$
\sum_{j=1}^{k-1} \frac{2}{\pi} \frac{1}{j+1} \leq  \int_{\pi}^{k \pi} \frac{1}{(j+1)\pi} \int_{j \pi}^{(j+1) \pi} \left\lvert  \frac{\sin x}{x}  \right\rvert  \, dx \leq  \sum_{j=1}^{k-1} \frac{2}{\pi} \frac{1}{j}.
$$
Como $\sum_{k=1}^\infty \frac{1}{n} = +\infty$ entonces $\lim_{ k \to \infty } \int_{0}^{k \pi} \left\lvert  \frac{\sin x}{x}  \right\rvert \, dx = \infty$.

### Lema (Criterio de Abel)
Sea $f:[a,+\infty) \to \mathbb{R}$ tal que 
1. $\int_{a}^{\infty} f(x) \, dx$ converge. 

Asuma además que $g:[a,+\infty) \to \mathbb{R}$ 
2. es monótona,
3. $\lim_{ x \to \infty } g(x) = \ell$. 

Entonces $\int_{0}^{\infty} f(x)g(x) \, dx$ converge.


***Prueba:*** Sea $\varepsilon>0$. Sean $c,d \geq M$. Entonces existe $c_{1} \in [c,d]$ tal que
$$
\int_{c}^{d} f(x)g(x) \, dx = g(c) \int_{c}^{c_{1}} f(x) \, dx + g(d) \int_{c_{1}}^{d} f(x)  \, dx,
$$
donde $M$ es tal que $\ell-\varepsilon <  g(x) < \ell+\varepsilon$ si $x\geq M$. Entonces, existe $K$ tal que $\lvert g(x) \rvert \leq K$ para $x \geq M$. Sea $M_{1}$ tal que 
$$
\left\lvert  \int_{p}^{q} f(x) \, dx   \right\rvert < \frac{\varepsilon}{2K}
$$
para $p,q \geq M_{1}\geq M$. Entonces, 
$$
\left\lvert  \int_{c}^{d} f(x)g(x) \, dx   \right\rvert \leq  \lvert g(c) \rvert \left\lvert  \int_{c}^{c_{1}} f(x) \, dx   \right\rvert + \lvert g(d) \rvert \left\lvert  \int_{c_{1}}^{d} f(x) \, dx   \right\rvert \leq  K \frac{\varepsilon}{2K} + K \frac{\varepsilon}{2K} = \varepsilon.
$$
Conclúyase que es de Cauchy y por tanto converge.

#### Ejemplo 
Para $\int_{1}^{\infty} \frac{\sin x \arctan x}{x} \, dx$, tome $g(x) = \arctan x$ y $f(x)=\frac{\sin x}{x}$. Como $g(x)$ es monótona y $\lim_{ x \to \infty } \arctan x = \frac{\pi}{2}$ y $\int_{1}^{\infty} \frac{\sin x}{x} \, dx$ converge, entonces la integral dada converge.

## Otros tipos de integrales impropias

### De -$\infty$ a $b$
Sean  $f:(-\infty,b] \to \mathbb{R}$ tal que $f:[a,b] \to \mathbb{R}$ es Riemann integrable para todo $a<b$. Si $\lim_{ a \to -\infty } \int_{a}^{b} f(x) \, dx$ existe, decimos que $\int_{-\infty}^{b} f(x) \, dx$ converge $\int_{0}^{1}  \, dx$

Note que $\int_{a}^{b} f(x)  \, dx = \int_{-b}^{-a}  f(u)  \, du$, por lo que $\int_{-\infty}^{b}f(x)  \, dx$ converge si y solo si $\int_{-b}^{\infty}  f(-x) \, dx$ converge.

### De $-\infty$ a $+\infty$
Sean $f:(-\infty,+\infty) \to \mathbb{R}$. Entonces $\int_{-\infty}^{+\infty} f(x) \, dx$ converge si y solo si $\int_{0}^{+\infty}  f(x)\, dx$ y $\int_{-\infty}^{0} f(x) \, dx$ convergen. 

#### Ejemplo 
Considere la siguiente integral impropia: $\int_{-\infty}^{+\infty} x^{2}e^{-\lvert x \rvert} \, dx$.
Note que 
$$
\int_{0}^{+\infty} x^{2}e^{-\lvert x \rvert }  \, dx = \int_{0}^{+\infty}  x^{2}e^{-x}\, dx.
$$
Por otro lado, 
$$
\int_{-\infty}^{0} x^{2} e^{-\lvert x \rvert }  \, dx = \int_{-\infty}^{0} x^{2} e^{x}  \, dx = \int_{+\infty}^{0} (-u)^{2}e^{-u} - \, du = \int_{0}^{+\infty} (-u)^{2} e^{-u}  \, du.  
$$
Ahora,  
$$
\lim_{ x \to \infty } \frac{ x^{2}e^{-x}}{e^{-x/2}} = 0.
$$
Como $\int_{0}^{+\infty} e^{-x/2} \, dx = -\frac{1}{2} e^{-x/2} \biggr\rvert_{0}^{+\infty } = \frac{1}{2}$, tenemos que $\int_{0}^{\infty} x^{2} e^{-x} \, dx$ converge.

#### Ejemplo 
Considere $\int_{\alpha}^{1} \frac{1}{x^{p}} \, dx$ con $\alpha>0$. Esta función no es Riemann-Integrable en $[0,1]$ si $p>0$, pero ¿$\lim_{ \alpha \to 0^{+} } \int_{\alpha}^{1} \frac{1}{x^{p}} \, dx$ existe?

Note que 
$$\int_{\alpha}^{1} \frac{1}{x^{p}} \, dx = \begin{cases}
\frac{1}{1-p} x^{1-p} \biggr\rvert_{\alpha}^{1} \quad\text{si } p\neq 1, \\
\ln x \biggr\rvert_{\alpha}^{1} = \ln(1) - \ln(\alpha) \quad \text{si }p=1. 
\end{cases}$$
Entonces
$$ \lim_{ \alpha \to 0^{+} } \int_{\alpha}^{1} \frac{1}{x^{p}} \, dx = \begin{cases}
\frac{1}{1-p} \quad\text{si } 0<p<1, \\
+\infty \quad \text{en otros casos}. 
\end{cases}$$
Haciendo el cambio de variable $x = \frac{1}{u} \implies dx = -\frac{du}{u^{2}}$, tenemos que 
$$
\int_{\alpha}^{1} \frac{1}{x^{p}} \, dx = \int_{1}^{1/\alpha}  \frac{1}{\left( \frac{1}{u} \right)^{p}}\, \frac{du}{u^{2}} = \int_{1}^{1/\alpha} \frac{1}{u^{2-p}}  \, du .  
$$
Entonces $\int_{\alpha}^{1} \frac{1}{x^{p}}  \, dx$ converge si y solo si $\int_{1}^{+\infty} \frac{1}{u^{2-p}} \, dx$ converge.