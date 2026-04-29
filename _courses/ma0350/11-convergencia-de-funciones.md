---
layout: chapter
course: ma0350
chapter: 11
title: "Convergencia de funciones"
slug: 11-convergencia-de-funciones
toc:
  sidebar: right
lang: es
fecha: 2025-06-17
---

{% raw %}
### Definición (Convergencia puntual)
Una sucesión de funciones $$f_{n}:A \to \mathbb{R}$$ converge puntualmente a $$f:A \to \mathbb{R}$$. Si para todo $$x \in A$$, se tiene que que $$\lim_{ n \to \infty } f_{n}(x)=f(x)$$.

#### Ejemplo 
Considere $$f_{n}(x) = x^{n}$$ para $$x \in (-1,+\infty)$$.
Note que 


$$
\lim_{ n \to \infty } f_{n}(x) \begin{cases}
0  \quad \text{si } \lvert x \rvert <1 \\
1  \quad \text{si } x=1 \\
\infty  \quad \text{si } x>1
\end{cases}.
$$


Sea 


$$
f(x) = \begin{cases}
0  \quad \text{si } x \in (-1,1) \\
1  \quad \text{si } x=1
\end{cases}.
$$


Entonces $$f_{n}$$ converge punto por punto a $$f$$ en $$(-1,1]$$. ¿Cómo probaríamos esto por definición?

***Prueba:***  Sea $$\varepsilon>0$$. Sea $$N  = \max \left\{  1, \left\lfloor  \frac{\ln(\varepsilon)}{\ln(\lvert x \rvert)}  \right\rfloor -1  \right\}$$. Luego, para $$n\geq N$$,


$$
n > \frac{\ln(\varepsilon)}{\ln\lvert x \rvert } \iff n\ln \lvert x \rvert < \ln \varepsilon \iff \lvert x^{n} \rvert = \lvert x \rvert ^{n} < \varepsilon.
$$


***OJO:*** Note que $$N = N(x, \varepsilon)$$. Si cambia $$x$$, cambia $$N$$. Además, $$\lim_{ x \to 1^{-} } N = +\infty$$. Es decir, no existe $$N$$ tal que $$\lvert x^{n} \rvert < \varepsilon$$ para todo $$n>N$$ y para todo $$x \in (-1, 1])$$

### Definición (Convergencia uniforme) 
Una sucesión de funciones $$f_{n}:A\to \mathbb{R}$$ converge uniformemente a $$f:A\to \mathbb{R}$$ si para todo $$\varepsilon>0$$ existe $$N \in \mathbb{N}$$ tal que para $$n\geq N$$, tenemos que para todo $$x \in A$$, 


$$
\lvert f_{n}(x)-f(x) \rvert < \varepsilon.
$$



#### Ejemplo 
Considere ahora la misma sucesión de funciones del ejemplo anterior pero con $$x \in (0,a)$$, con $$a<1$$. Probaremos que converge uniformemente.

***Prueba:***  Sea $$\varepsilon>0$$. Sea $$N  = \max \left\{  1, \left\lfloor  \frac{\ln(\varepsilon)}{\ln(a)}  \right\rfloor -1  \right\}$$. Luego, para $$n\geq N$$ y para todo $$x \in (0,a)$$


$$
n > \frac{ln(\varepsilon)}{\ln (a)}\geq  \frac{\ln(\varepsilon)}{\ln\lvert x \rvert } \iff n\ln \lvert x \rvert < \ln \varepsilon \iff \lvert x^{n} \rvert = \lvert x \rvert ^{n} < \varepsilon.
$$



### Definición (Norma infinito)
Sea $$f:A\to \mathbb{R}$$ acotada. Defina $$\lVert f \rVert_{\infty} := \sup \{ \lvert f(x) \rvert: x \in A \}$$. Note que si $$\lVert f \rVert_{\infty} = 0$$, entonces $$\lvert f(x) \rvert \leq 0$$ para todo $$x \in A$$, y por lo tanto $$f=0$$.

Por otro lado si $$f:A\to \mathbb{R}$$, $$g:A\to \mathbb{R}$$ son acotadas, entonces 


$$
\sup \{ \lvert f(x) + g(x) \rvert: x \in A \} \leq  \sup \{ \lvert f(x) \rvert + \lvert g(x) \rvert : x \in A  \} \leq  \sup \{ \lvert f(x) \rvert: x \in A  \} + \sup \{ \lvert g(x) \rvert: x \in A  \}.
$$


Luego,  $$\lVert f+g \rVert_{\infty} \leq \lVert f \rVert_{\infty} + \lVert g \rVert_{\infty}$$.
Por lo tanto, $$\lVert  \rVert_{\infty}$$ es una norma sobre el espacio de funciones $$A\to \mathbb{R}$$ acotadas.

### Convergencia uniforme y norma infinito
Sean $$f_{n}:A\to \mathbb{R}$$ convergentes a $$f:A\to \mathbb{R}$$ uniformemente. Luego, dado $$\varepsilon>0$$, existe $$N \in \mathbb{N}$$ tal que si $$n\geq N$$, $$\lvert f_{n}(x) - f(x) \rvert < \varepsilon$$ para todo $$x \in A$$. Luego, 


$$
\sup \{ \lvert f_{n}(x) - f(x) \rvert : x \in A  \} \leq  \varepsilon,
$$


por lo tanto $$\lVert f_{n}-f \rVert_{\infty} \leq \varepsilon$$ para $$n\geq N$$.

#### Ejercicio 
Sean $$f_{n}:A\to \mathbb{R}$$ y $$f:A\to \mathbb{R}$$ tal que $$\lVert f_{n}-f \rVert_{\infty} \underset{n  \rightarrow \infty}{\longrightarrow} 0$$. Entonces $$f_{n}$$ converge uniformemente a $$f$$.

#### Ejemplo 
Considere $$f_{n}(x) = x^{n}(1-x)$$ para $$x \in [0,1]$$. Entonces, $$f_{n} \underset{n  \rightarrow \infty}{\longrightarrow} 0$$ puntualmente. Probaremos que converge uniformemente. 
Sea $$0 < \delta < \min \left\{  \varepsilon,1  \right\}$$. Entonces, en $$[0,1-\delta]$$, tenemos que 


$$
\lvert x \rvert ^{n} \lvert 1-x \rvert < \varepsilon.
$$


Ahora, 


$$
\begin{aligned}
\lvert x^{n} \rvert \lvert 1-x \rvert &\leq \lvert x \rvert ^{n} < \varepsilon \\
\iff n > \left\lfloor  \frac{\ln(\varepsilon)}{\ln(1-\delta)}  \right\rfloor &= N.
\end{aligned}
$$


Luego, para $$n\geq N$$, tenemos que $$\lvert x^{n}(1-x) \rvert < \varepsilon$$ si $$x \in [0,1-\delta]$$.
Por otro lado, si $$x \in [1-\delta,1]$$, entonces $$\lvert x^{n}(1-x) \rvert \leq 1-x \leq \delta < \varepsilon$$.

### Teorema (Acotación de la función límite) 
 Sean $$f_{n}:A\to \mathbb{R}$$ acotadas que convergen uniformemente a $$f:A\to \mathbb{R}$$. Entonces $$f$$ es acotada.
 
***Prueba:*** Sea $$\varepsilon = 1$$. Existe $$N \in \mathbb{N}$$ tal que $$\lvert f_{n}(x) - f(x) \rvert < 1$$ para todo $$n\geq N$$. Entonces 


$$
f_{n}(x) -1 < f(x) < f_{n}(x)+1
$$


Como $$f_{n}$$ es acotada (para cualquier $$n\geq N$$), sabemos que existe $$M \in \mathbb{R}$$ tal que $$-M \leq f_{n}(x) \leq M$$. Luego $$-M-1 \leq f(x) \leq M+1$$.

#### Ejemplo 
Considere $$f_{n}(x) = \frac{1}{x+1/n}$$, entonces $$\lvert f_{n}(x) \rvert \leq n$$ para $$x \in [0,+\infty]$$, pero $$\lim_{ n \to \infty } f_{n}(x) = \frac{1}{x}$$ no es acotada. Por tanto, la convergencia no es uniforme.

#### Ejemplo 
### Teorema (Convergencia uniforme de funciones continuas)
Sean $$f_{n}:A\to \mathbb{R}$$ continuas que convergen uniformemente a $$f:A\to \mathbb{R}$$. Entonces $$f$$ es continua.

***Prueba:*** Sea $$\varepsilon>0$$. Existe $$N \in \mathbb{N}$$ tal que si $$n\geq N$$, 


$$
\lvert f_{n}(x) - f(x) \rvert < \frac{\varepsilon}{3}
$$


para todo $$x \in A$$. Además, existe $$\delta>0$$ tal que si $$\lvert x-x_{0} \rvert < \delta$$, entonces $$\lvert f_{N}(x) - f_{N}(x_{0}) \rvert < \frac{\varepsilon}{3}$$. Luego, si $$\lvert x-x_{0} \rvert < \delta$$


$$
\begin{aligned}
\lvert f(x)-f(x_{0}) \rvert  &\leq \lvert f(x) - f_{N}(x) \rvert  + \lvert f_{N}(x) - f(x_{0}) \rvert  \\
&\leq \lvert f(x) - f_{N}(x) \rvert + \lvert f_{N}(x) - f_{N}(x_{0}) \rvert + \lvert f_{N}(x_{0}) - f_{N}(x) \rvert < \varepsilon.  
\end{aligned}
$$


Concluya que $$f$$ es continua.

#### Ejemplo
Considere $$f_{n}(x) = x^{n}$$, $$x \in [0,1]$$, Note que 


$$
\lim_{ n \to \infty } f_{n}(x) = \begin{cases}
0  \quad \text{si } x \in [0,1) \\
1  \quad \text{si } x = 1
\end{cases}.
$$


Concluya que la convergencia no es uniforme.

### Definición (Cauchy uniformemente)
Sea $$f_{n}:A\to \mathbb{R}$$ una sucesión de funciones. Decimos que $$f_{n}$$ es de Cauchy uniformemente si dado $$\varepsilon>0$$ existe $$N$$ tal que si $$n,m\geq N$$, tenemos que $$\lvert f_{n}(x) - f_{m}(x) \rvert < \varepsilon$$ para todo $$x \in A$$.

### Lema  (Convergencia unidorme si y solo si Cauchy uniformemente)
Sea $$f_{n}:A\to \mathbb{R}$$ una sucesión de funciones y $$f:A\to \mathbb{R}$$. Entonces $$f_{n} \underset{n \rightarrow \infty}{\longrightarrow} f$$ uniformemente si y solo si $$f_{n}$$ es de Cauchy uniformemente.

***Prueba:*** ($$\implies$$): Sea $$\varepsilon>0$$. Entonces existe $$N \in \mathbb{N}$$ tal que para $$n\geq N$$, tenemos que $$\lvert f_{n}(x) - f(x) \rvert < \frac{\varepsilon}{2}$$ para todo $$x \in A$$. Ahora para todo $$n,m\geq N$$, 


$$
\lvert f_{n}(x)-f_{m}(x) \rvert \leq \lvert f_{n}(x) - f(x)\rvert + \lvert f(x) - f_{m}(x) \rvert  < \varepsilon.
$$


Por tanto es Cauchy uniformemente.
($$\impliedby$$): Sea $$\varepsilon>0$$. Entonces existe $$N$$ tal que para todos $$m,n\geq N$$, tenemos que 
$$\lvert f_{n}(x)-f_{m}(x) \rvert < \frac{\varepsilon}{2}$$para todo $$x \in A$$. 
Sea $$x_{0} \in A$$. Entonces $$\{f_{n}(x_{0})\}_{n=1}^\infty$$ es de Cauchy y por tanto convergente, i.e., existe $$\ell \in \mathbb{R}$$ tal que $$f_{n}(x_{0}) \underset{n \rightarrow \infty}{\longrightarrow} \ell$$. Defina $$f(x) = \lim_{ n \to \infty } f_{n}(x)$$. Luego, dado $$x \in A$$, existe $$N_{0}\geq N$$ tal que si $$n \geq N_{0}(x)$$ entonces 


$$
\lvert f(x) - f_{n}(x) \rvert < \frac{\varepsilon}{2}.
$$


Ahora, si $$m\geq N$$., 


$$
\begin{aligned}
\lvert f(x) - f_{m}(x) \rvert &\leq  \lvert f(x) - f_{N_{0}}(x) \rvert + \lvert f_{N_{0}}(x) - f_{m}(x) \rvert \\
& \leq \frac{\varepsilon}{2} + \lvert f_{N_{0}}(x) - f_{m}(x) \rvert < \varepsilon  \quad \text{por ser Cauchy uniformemente.}
\end{aligned}
$$



### Teorema (Convergencia uniforme y Riemann-integrabilidad)
Sean $$f_{n}:[a,b] \to \mathbb{R}$$ Riemann integrables que convergen uniformemente a $$f:[a,b] \to \mathbb{R}$$. Entonces $$f$$ es Riemann integrable y además 


$$
\lim_{ n \to \infty } \int_{a}^{b} f_{n}(x)   \, dx =  \int_{a}^{b} f(x) \, dx. 
$$



***Prueba:***  Dado $$\varepsilon>0$$, existe $$N \in \mathbb{N}$$ tal que para todo $$n\geq N$$, $$\lvert f_{n}(x) - f(x) \rvert < \frac{\varepsilon}{4(b-a)}$$ para todo $$x \in [a,b]$$. Como $$f_{N}$$ es Riemann integrable, existe $$P_{\varepsilon}$$ tal que $$U(f_{N}, P_{\varepsilon}) - L(f_{N},P_{\varepsilon}) < \frac{\varepsilon}{2}$$.
Sea $$P_{\varepsilon} = \{ a_{0}=a < \dots < a_{n} = b \}$$. Entonces 


$$
(a_{i+1}-a_{i}) \sup \{ f(x): a_{i} \leq x \leq a_{i+1} \} \leq \left( \sup \{ f_{N}(x) : a_{i} \leq x \leq  a_{i+1}\} + \frac{\varepsilon}{4(b-a)} \right)(a_{i+1}-a_{i}).
$$


pues $$f_{N}(x) - \varepsilon \leq f(x) \leq f_{N}(x) + \varepsilon$$ para todo $$x \in A$$. De igual forma, 


$$
\sup \{ f_{N}(x):a_{i}\leq x\leq a_{i+1} \} - \frac{\varepsilon}{4(b-a)} \leq \sup \{ f(x):a_{i}\leq x\leq a_{i+1} \}.
$$


Entonces, 


$$
U(f, P_{\varepsilon}) \leq U(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4}
$$


pues 


$$
U(f, P_{\varepsilon}) = \sum_{i=0}^{n-1} \sup\{ f(x):a_{i}\leq x\leq a_{i+1} \} (a_{i+1}-a_{i}).
$$


De igual forma, tenemos que 


$$
U(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4}\leq  U(f, P_{\varepsilon}),
$$


por lo que 


$$
U(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4} \leq U(f, P_{\varepsilon}) \leq U(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4}.
$$


De manera análoga (pero trabajando con ínfimos en lugar de supremos) podemos probar que 


$$
L(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4}\leq L(f, P_{\varepsilon}) \leq L(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4}.
$$


Finalmente, tenemos que 


$$
\begin{aligned}
U(f, P_{\varepsilon}) - L(f, P_{\varepsilon}) &\leq  U(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{4} - \left( L(f_{N}, P_{\varepsilon}) - \frac{\varepsilon}{4} \right) \\
&= U(f_{N}, P_{\varepsilon}) - L(f_{N}, P_{\varepsilon}) + \frac{\varepsilon}{2} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon,
\end{aligned}
$$


de donde se concluye que $$f$$ es Riemann-integrable. Para la prueba del límte de las integrales, dado $$\varepsilon>0$$, existe $$M \in \mathbb{N}$$ tal que para todo $$n\geq M$$ y $$x \in [a,b]$$, $$\lvert f(x) - f_{n}(x) \rvert < \frac{\varepsilon}{b-a}$$ Tome 


$$
\begin{aligned}
\left\lvert  \int_{a}^{b} f_{n}(x) \, dx - \int_{a}^{b} f(x) \, dx    \right\rvert &= \left\lvert  \int_{a}^{b} (f_{n}(x) - f(x)) \, dx   \right\rvert \\
&\leq \int_{a}^{b} \lvert f_{n}(x)-f(x) \rvert  \, dx \\
&< \int_{a}^{b} \frac{\varepsilon}{b-a} \, dx = \varepsilon, 
\end{aligned}
$$


siempre que $$n\geq M$$, de donde se concluye el límite. 

#### Ejemplo 
Para $$n \in \mathbb{N}$$, considere $$f_{n}:[0,1] \to \mathbb{R}$$ tal que 


$$
f_{n}(x) = \begin{cases}
0  \quad\text{si } \frac{1}{n}\leq x\leq 1 \\
n^{2}x  \quad \text{si } 0\leq x < \frac{1}{n}
\end{cases}.
$$


Sea $$x_{0} \in (0,1)$$. Entonces, existe $$n_{0}$$ tal que $$\frac{1}{n_{0}} \leq x_{0}$$. Entonces $$f_{n}(x_{0}) = 0$$ si $$n \geq n_{0}$$. Ahora, 


$$
\int_{0}^{1} f_{n}(x) \, d = \int_{0}^{1/n}  n ^{2}x\, dx + \int_{1/n}^{1} 0  \, dx = \frac{n^{2}x^{2}}{2} \biggr\rvert_{0}^{1/n} = \frac{1}{2}.
$$


Entonces, 


$$
\int_{0}^{1} f_{n}(x)  \, dx = \frac{1}{2} \underset{n \rightarrow \infty}{ \not\longrightarrow} \int_{0}^{1} 0 \, dx = 0.
$$



#### Ejercicio 
Encuentre una sucesicón de funciones  $$f_{n}$$ Riemann integrables tal que 


$$
f_{n} \underset{n \rightarrow \infty}{\longrightarrow} f = \begin{cases}
1  \quad \text{si }x \in \mathbb{Q} \\ \\
0  \quad \text{si }x \in \mathbb{I}
\end{cases},
$$


con $$f_{n}:[0,1]\to \mathbb{R}$$ y $$f : [0,1] \to \mathbb{R}$$.

### Teorema (Derivadas y convergencia uniforme)
Sean $$f_{n}:[a,b]\to \mathbb{R}$$ funciones derivables tales que $$f_{n}' \underset{n \rightarrow \infty}{\longrightarrow} g$$ uniformemente en $$[a,b]$$. Asuma que existe $$x_{0} \in [a,b]$$ tal que $$f_{n}(x_{0})$$ converge.  Entonces $$f_{n}$$ converge uniformemente a una función $$f:[a,b] \to \mathbb{R}$$ tal que  $$f'(x) = g(x)$$ para todo $$x \in [a,b]$$.

***Prueba:*** Sean $$n,m \in \mathbb{N}$$. Tome $$h(x) = f_{n}(x)-f_{m}(x)$$. Entonces, por teorema del valor medio existe $$y$$ entre $$x$$ y $$x_{0}$$ tal que 




$$
\begin{aligned}
\frac{h(x) - h(x_{0})}{x-x_{0}} &= h'(y) \implies h(x) = h(x_{0}) + h'(y)(x-x_{0}) \\
\implies f_{n}(x) - f_{m}(x) &= (f_{n}(x_{0})-f_{m}(x_{0})) + (x-x_{0})(f_{n}'(y)-f_{m}'(y))
\end{aligned}
$$


Como $$f_{n}' \underset{n \rightarrow \infty}{\longrightarrow} g$$, entonces es de Cauchy, i.e., dado $$\varepsilon>0$$, existe $$N \in \mathbb{N}$$ tal que para todos $$n,m\geq N$$ y para todo $$x \in [a,b]$$, $$\lvert f_{n}'(x) - f_{m}'(x)\rvert < \frac{\varepsilon}{2(b-a)}$$. 
Además, como $$f_{n}(x_{0})$$ converge, es de Cauchy, por lo que existe $$M \in \mathbb{N}$$ tal que si $$n,m\geq M$$, $$\lvert f_{n}(x_{0}) - f_{m}(x_{0}) \rvert < \frac{\varepsilon}{2}$$. Luego, si $$n,m\geq N$$ entonces, para todo $$x \in [a,b]$$ 


$$
\begin{aligned}
\lvert f_{n}(x) - f_{m}(x) \rvert &\leq \lvert f_{n}(x_{0}) - f_{m}(x_{0})   \rvert + \lvert x-x_{0} \rvert \lvert f_{n}'(y) - f_{m}'(y) \rvert\\
&< \frac{\varepsilon}{2} + (b-a)\frac{\varepsilon}{2(b-a)} = \varepsilon.
\end{aligned}
$$


Por tanto, $$f_{n}$$ es Cauchy uniformemente y converge. 
**OJO:** Si $$\{f_{n}(x)\}_{n=1}^\infty$$ es de Cauchy, defina $$\ell_{x} = \lim_{ n \to \infty } f_{n}(x)$$. Entonces $$f(x) = \ell_{x}$$.

Probaremos ahora que $$f'(x) = g(x)$$.
Hay que mostrar que 


$$
\lim_{ x \to y } \frac{f(x)-f(y)}{x-y} = g(y).
$$


Considere 


$$
\begin{aligned}
&\left\lvert  \frac{f(x)-f(y)}{x-y} - g(y)  \right\rvert \leq \left\lvert \frac{f(x)-f(y)}{x-y} -\frac{f_{N}(x)-f_{N}(y)}{x-y}  \right\rvert  + \left\lvert \frac{f_{N}(x)-f_{N}(y)}{x-y} - g(y) \right\rvert \\
&\leq  \left\lvert \frac{f(x)-f(y)}{x-y} -\frac{f_{N}(x)-f_{N}(y)}{x-y}  \right\rvert  + \left\lvert \frac{f_{N}(x)-f_{N}(y)}{x-y} - f_{N}'(y) \right\rvert + \lvert f_{N}'(y) - g(y) \rvert .
\end{aligned}
$$


Dado $$\varepsilon>0$$, existe $$N \in \mathbb{N}$$ y $$\delta>0$$ tales que 
1. $$\lvert f_{n}'(x) - g(x) \rvert < \frac{\varepsilon}{3}$$ si $$n\geq N$$ y $$x \in [a,b]$$.
2. Si $$\lvert x-y \rvert < \delta$$ entonces 


$$
\left\lvert \frac{f_{N}(x)-f_{N}(y)}{x-y} - f_{N}'(y) \right\rvert < \frac{\varepsilon}{3}.
$$


Considere ahora 


$$
\begin{aligned}
\frac{f_{m}(x)-f_{m}(y)}{x-y} - \frac{f_{N}(x)-f_{N}(y)}{x-y} &= \frac{(f_{m}(x) - f_{N}(x))- (f_{m}(y)-f_{N}(y))}{x-y} \\
&= f_{m}'(c)-f_{N}'(c)
\end{aligned}
$$


para algún $$c$$ entre $$x$$ y $$y$$ (que existe por el teorema del valor intermedio). Entonces 


$$
\lim_{ m \to \infty } \left\lvert  \frac{f_{m}(x)-f_{m}(y)}{x-y} - \frac{f_{N}(x)-f_{N}(y)}{x-y}\right\rvert = \left\lvert \frac{f(x)-f(y)}{x-y} - \frac{f_{N}(x)-f_{N}(y)}{x-y} \right\rvert < \frac{\varepsilon}{3}.
$$


Finalmente, tenemos que 


$$
\left\lvert  \frac{f(x)-f(y)}{x-y} - g(y)  \right\rvert < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.
$$


#### Ejemplo 
Sean $$f_{n}:[-1,1] \to \mathbb{R}$$ tales que $$f_{n}(x) = \sqrt{ x^{2}+\frac{1}{n} }$$. Entonces $$f_{n}$$ es derivable en $$(0,1)$$ y  $$f_{n}'(x) = \frac{x}{\sqrt{ x^{2}+\frac{1}{n} }}$$. Además $$\lim_{ n \to \infty } f_{n}(x) = \sqrt{ x^{2} } = \lvert x \rvert$$. Vamos a probar que dado $$\varepsilon>0$$, existe $$N \in \mathbb{N}$$ tal que $$\left\lvert  \sqrt{ x^{2}+\frac{1}{n} } - \sqrt{ x^{2} } \right\rvert < \varepsilon$$ para todo $$x \in [-1,1]$$. Dado $$\varepsilon>0$$, sabemos que existe $$N_{0} \in \mathbb{N}$$ tal que $$\frac{1}{\sqrt{ N_{0}}} < \varepsilon$$. Note que, para $$n\geq N_{0}$$


$$
\sqrt{ x^{2}+\frac{1}{n} } - \sqrt{ x^{2} } = \frac{\frac{1}{n}}{\sqrt{ x^{2}+\frac{1}{n} } + \sqrt{ x^{2} }} \leq \frac{\frac{1}{n}}{\sqrt{ \frac{1}{n} }}  = \frac{1}{\sqrt{ n }} < \varepsilon
$$



#### Ejemplo 
 


$$
f_{n}(x) = \sum_{k=0}^{n} \frac{\cos(3^{k}x)}{2^{k}}
$$


 converge uniformemente a una función que no tiene derivada en ningún punto.

### Lema (Convergencia puntual de funciones crecientes)   
Sean $$\{f_{n}(x)\}_{n=1}^\infty$$ continuas tales que $$f_{n}(x) \leq f_{n+1}(x)$$ para todo $$x \in [a,b]$$. Asuma que existe $$f:[a,b] \to \mathbb{R}$$ continua tal que  $$\lim_{ n \to \infty }f_{n}(x) = f(x)$$ puntualmente. Entonces $$f_{n} \underset{n \rightarrow \infty}{\longrightarrow} f$$ uniformemente en $$[a,b]$$.

***Prueba:*** Hay que mostrar que $$M_{n} = \lVert f-f_{n} \rVert_{\infty} \underset{n \rightarrow \infty}{\longrightarrow} 0$$, donde $$\lVert f - f_{n} \rVert_{\infty} = \sup \{ \lvert f(x) -f_{n}(x) \rvert: x \in A \}$$. Note que para todo $$x \in A$$, 


$$
0 \leq f(x) - f_{n+1}(x) \leq  f(x)-f_{n}(x) \implies M_{n+1} \leq  M_{n}.
$$


Como $$f - f_{n}$$ es continua, sabemos que existe $$x_{n}$$ tal que $$f(x_{n}) - f_{n}(x_{n}) = M_{n}$$. En particular, $$\{x_{n}\}_{n=1}^\infty \subseteq [a,b]$$. Por Bolzano-Weirerstrass, existe una subsucesión $$x_{n_{k}} \underset{n_{k} \rightarrow \infty}{\longrightarrow} x \in[a,b]$$. Además, note que $$f_{1}(x_{n_{k}}) \leq f_{{n_{k}}}(x_{n_{k}}) \leq f(x_{n_{k}})$$ . Luego, por BW, existe una subsucesión $$x_{n_{k_{\ell}}}$$ tal que $$f_{n_{k_{\ell}}}(x_{n_{k_{\ell}}})$$ es convergente, ($$f_{n}(x_{n})$$). Sin pérdida de generalidad puedo asumir que ...
{% endraw %}
