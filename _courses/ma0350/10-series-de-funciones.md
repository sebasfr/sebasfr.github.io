---
layout: chapter
course: ma0350
chapter: 10
title: "Series de funciones"
slug: 10-series-de-funciones
toc:
  sidebar: right
lang: es
fecha: 2025-06-24
---

{% raw %}
Sea $$f_{n}:A\to \mathbb{R}$$ una sucesión de funciones. Considere $$S_{n}(x) = \sum_{i=1}^{n} f_{i}(x)$$. Note que $$S_{n}(x)$$ es una sucesión de funciones 

### Definición (convergencia de serie de funciones)
Decimos que $$\sum_{n=1}^\infty f_{n}(x)$$ converge:
1. puntualmente si $$S_{n}(x)$$ convergen puntualmente.
2. uniformemente si $$S_{n}(x)$$ convergen uniformemente
3. absolutamente si $$\sum_{i=1}^{\infty} \lvert f_{i}(x) \rvert$$ convergen (puntual o uniformemente). 
### Lema (Cauchy si y solo si convergencia uniforme) 
Sea $$f_{n}:A\to \mathbb{R}$$ funciones. Entonces $$\sum_{n=1}^\infty f_{n}$$ converge uniformemente si y solo si para todo $$\varepsilon>0$$ existe $$N$$ tal que para todo $$x  \in A$$ 


$$
\lvert S_{n}(x) - S_{m}(x) \rvert < \varepsilon
$$


si $$n,m \geq N$$. Equivalentemente, si $$n>m\geq N$$, entonces para todo $$x \in A$$ 


$$
\lvert f_{m+1}(x) + f_{m+2}(x) + \dots + f_{n}(x) \rvert < \varepsilon.
$$



### Lema (M-test de Weirerstrass) 
Sean $$f_{n}:A\to \mathbb{R}$$ una sucesión de funciones y $$\{a_{n}\}_{n=1}^\infty$$ una sucesión convergente tal que 
1. $$\sum_{n=1}^\infty a_{n}$$ converge, 
2. $$\lvert f_{n}(x) \rvert \leq a_{n}$$ para todo $$x \in A$$. 

Entonces $$\sum_{n=1}^\infty \lvert f_{n}(x) \rvert$$ converge uniformemente.

***Prueba:*** Dado $$\varepsilon>0$$ existe $$N$$ tal que para todos $$n,m\geq N$$ 


$$
\begin{aligned}
\lvert a_{m}+a_{m+1}+\dots+a_{n} \rvert < \varepsilon \iff &a_{m} + a_{m+1} + \dots + a_{n} < \varepsilon \\
\implies \lvert f_{m}(x) \rvert + \lvert f_{m+1}(x) \rvert + \dots+ \lvert f_{n}(x) \rvert <  \quad  &a_{m} + a_{m+1} + \dots + a_{n} < \varepsilon
\end{aligned}
$$


para todo $$x \in A$$, $$n,m\geq N$$. 
#### Ejemplo 
Considere $$\sum_{k=1}^\infty \frac{\sin(kx)}{k^{2}}$$. Note que $$\left\lvert  \frac{\sin(kx)}{k^{2}}  \right\rvert \leq \frac{1}{k^{2}}$$. Como $$\sum_{k=1}^\infty \frac{1}{k^{2}}$$ converge, entonces por el M-test, $$\sum_{k=1}^\infty \frac{\sin(kx)}{k^{2}}$$ converge uniformemente. 

#### Ejemplo 
Considere $$\sum_{k=1}^\infty x^{k}$$ para $$\lvert x \rvert<1$$. En esos casos converge puntualmente. Sea $$0<a<1$$. Si $$\lvert x \rvert \leq a$$, entonces $$f_{n}(x) = \lvert x \rvert^{n} \leq a^{n} = a_{n}$$. Como $$a<1$$, la serie $$\sum_{n=1}^\infty a^{n}$$ converge. Entonces por el M-test , $$\sum_{n=1}^\infty x^{n}$$ converge uniformemente en $$\lvert x \rvert \leq a$$.

### Lema (Continuidad, integrabilidad y diferenciabilidad)
Sea $$f_{n}:A\to \mathbb{R}$$ una sucesión de funciones tal que $$\sum_{n=1}^\infty f_{n}(x)$$ converge uniformemente a una función $$f(x)$$.
1. Si $$f_{n}(x)$$ es continua entonces $$f(x)$$ es continua.
2. Si $$f_{n}$$ son R-integrables, entonces $$f$$ es R-integrable. Además 


$$
\int_{a}^{b} \left( \sum_{n=1}^\infty f_{n}(x) \right) \, dx = \int_{a}^{b} f(x) \, dx = \sum_{n=1}^\infty \int_{a}^{b} f_{n}(x) \, dx 
$$


3. Si $$f_{n}:A \to \mathbb{R}$$ es derivable y se cumple que 
1.  $$\sum_{n=1}^\infty f_{n}'(x)$$ converge uniformemente
2. $$\sum_{n=1}^\infty f_{n}(x_{0})$$ converge para un $$x_{0} \in A$$.   
Entonces $$\sum_{n=1}^\infty f_{n}(x)$$ converge uniformemente una función $$f(x)$$ y $$f'(x) = \sum_{n=1}^\infty f_{n}'(x)$$.

#### Ejemplo 
Sea $$f_{n}(x) = \frac{x^{n}}{n^{3}}$$. ¿$$\sum_{n=1}^\infty \frac{x^{n}}{n^{3}}$$ converge uniformemente en $$[-1,1]$$? Como $$\left\lvert  \frac{x^{n}}{n^{3}}  \right\rvert \leq  \frac{1}{n^{3}}$$ y $$\sum_{n=1}^\infty \frac{1}{n^{3}}$$ converge, la serie converge uniformemente por el M test.

Sea $$f(x) = \sum_{n=1}^\infty \frac{x^{n}}{n^{3}}$$, entonces $$f$$ es continua y R-integrable. Por otro lado, $$f_{n}'(x) = \frac{nx^{n-1}}{n^{3}} = \frac{x^{n-1}}{n^{2}}$$, que converge uniformemente por el M-test, pues 


$$
\frac{x^{n-1}}{n^{2}} \leq  \frac{1}{n^{2}} \quad \text{y} \quad \sum_{n=0}^\infty \frac{1}{n^{2}} \text{ converge.}
$$


Además, $$f'(x) = \sum_{n=1}^\infty \frac{x^{n-1}}{n^{2}}$$.

### Teorema (Criterio de Dirichlet)
Sea $$f_{n}:A\to \mathbb{R}$$ una sucesión de funciones tales que 
1. existe $$M \in \mathbb{R}$$ tal que 


$$
\underset{x \in A}{\sup} \left\{  \sum_{k=1}^{n} f_{k}(x)  \right\} = \underset{x \in A}{\sup} \left\{  S_{n}(x)  \right\} \leq  M.
$$


Asuma además que $$g_{n}:A\to \mathbb{R}$$ es tal que 
2. $$g_{n} \geq 0$$ ,
3. $$g_{n}(x)\geq g_{n+1}(x)$$ para todo $$x \in A$$ (decreciente en $$n$$) ,
4. $$\lim_{ n \to \infty } g_{n}(x) = 0$$ uniformemente. 

Entonces $$\sum_{n=1}^\infty f_{n}(x)g_{n}(x)$$ converge uniformemente.

***Prueba:*** 
Considere 


$$
\sum_{k=n}^{m} f_{k}(x) g_{k}(x) = g_{m}(x)S_{m}(x) - g_{n}(x) S_{n-1}(x) + \sum_{j=n}^{m-1} (g_{j}-g_{j+1}) S_{j} (x),
$$


donde $$S_{m}(x) = \sum_{i=1}^{m} f_{i}(x)$$. Dado $$\varepsilon>0$$, existe $$N$$ tal que para todo $$x \in A$$, $$\lvert g_{n}(x) \rvert < \frac{\varepsilon}{2M}$$ si $$n\geq N$$. Ahora, 


$$
\begin{aligned}
\left\lvert  \sum_{j=n}^{m-1} (g_{j}(x) - g_{j+1}(x))S_{j}(x)  \right\rvert &\leq \sum_{j=n}^{m-1} \lvert g_{j}(x) - g_{j+1}(x) \rvert   \lvert S_{j}(x) \rvert \\
& \leq M \sum_{=}^\infty (g_{j}(x)-g_{j+1}(x)) \\
& = M(g_{n}(x)-g_{m}(x)).
\end{aligned}
$$


Por lo tanto 


$$
\begin{aligned}
\left\lvert  \sum_{k=n}^{m} f_{k}(x) g_{k}(x)  \right\rvert &\leq  \lvert g_{n}(x) \rvert \lvert S_{m}(x) \rvert + \lvert g_{n}(x) \rvert \lvert S_{n-1}(x)\rvert + M (g_{n}(x)-g_{m}(x)) \\
&\leq g_{m}(x) M + g_{n}(x) M + M(g_{n}(x) - g_{m}(x)) = 2M g_{n}(x) < \varepsilon.
\end{aligned}
$$



#### Ejemplo 
Considere $$\sum_{k=1}^{\infty} \frac{\sin(kx)}{k}$$. Note que 


$$
\left\lvert  \sum_{k=1}^{n} \sin(kx)  \right\rvert =\frac{\left\lvert  \cos\left( \frac{x}{2} \right) - \cos\left( \left( n-\frac{1}{2} \right) x\right)  \right\rvert}{2 \sin\left( \frac{x}{2} \right)} \leq \frac{2}{2\sin(x^{2})} < M 
$$


para todo $$x \in [\delta, 2\pi-\delta$$, con $$0 < \delta <n - \delta$$.

### Teorema (Criterio de Abel)
Sea $$f_{n}:A\to \mathbb{R}$$ una sucesión de funciones tales que 
1. $$\sum_{n=1}^{\infty} f_{n}(x)$$ converge uniformemente.
2. $$g_{n}:A\to \mathbb{R}$$ es monótona,
3. existe $$K \in \mathbb{R}$$ tal que $$\underset{x \in A}{\sup}\{ \lvert g_{n}(x) \rvert \} \leq k$$ para todo $$n \in \mathbb{N}$$.
Entonces $$\sum_{n=1}^{\infty} f_{n}(x) g_{n}(x)$$ converge uniformemente.

***Prueba:*** 
Sean $$S = \sum_{n=1}^\infty f_{n}(x)$$ y  $$S_{n}(x) = \sum_{k=1}^{n} f_{k}(x)$$. Note que 


$$
\begin{aligned}
\sum_{j=n}^{m} f_{j}(x)g_{j}(x) &= g_{m} S_{m} - g_{n} S_{n-1} + \sum_{j=n}^{m-1} (g_{j}-g_{j-1}) S_{j} \\
&= g_{m}(S-S_{m}) - g_{n}(S-S_{n-1}) + \sum_{j=n}^{m-1} (g_{j}-g_{j+1})(S-S_{j})
\end{aligned}
$$


Dado $$\varepsilon>0$$, existe $$N \in \mathbb{N}$$ tal que para todo $$\ell\geq N$$ y para todo $$x \in A$$, 


$$
\lvert S(x)-S_{\ell}(x) \rvert < \frac{\varepsilon}{3K} 
$$


para $$\ell\geq N$$ y $$x \in A$$. Entonces, 


$$
\begin{aligned}
\lvert g_{n}(x) \rvert \lvert S(x) - S_{n-1}(x) \rvert &< \frac{\varepsilon}{4} \\
\lvert g_{n}(x) \rvert \lvert S(x) - S_{m}(x) \rvert &< \frac{\varepsilon}{4}, 
\end{aligned}
$$


si $$n-1,m\geq N$$.
Por otro lado, 


$$
\begin{aligned}
\left\lvert  \sum_{j=n}^{m-1} (g_{j}(x) - g_{j+1}(x))(S(x)-S_{j}(x)) \right\rvert &\leq \sum_{j=n}^{m-1} \lvert g_{i}(x) - g_{i+1}(x) \rvert \lvert S(x) - S_{j}(x) \rvert  \\
&< \frac{\varepsilon}{4k} \sum_{j=n}^{m-1} \lvert g_{j}(x) - g_{j-1}(x) \rvert  
\end{aligned}
$$


#### Ejemplo 
Considere $$S(x) = \sum_{n=1}^\infty \frac{(-1)^{n}}{n}e^{-xn}$$ para $$x \in [1,+\infty)$$. Note que $$\lvert g_{n}(x) \rvert = \left\lvert  \frac{1}{n}  \right\rvert \leq 1$$. Ahora, $$\lvert (-1)^{n} \exp(-xn) \rvert \leq \exp(-n)$$ y $$\sum_{n=1}^\infty \exp(-n)$$ converge, por lo que tenemos que la serie estudiada converge uniformemente.

# Series de potencias

Considere $$f_{n}(x) = a_{n} x^{n}$$ y $$S_{n}(x) = \sum_{k=0}^{n} a_{n} x^{n}$$, donde $$\{a_{n}\}_{n=0}^\infty$$ es una sucesión.

Consideremos $$\sqrt[n]{\lvert a_{n} \rvert \lvert x^{n} \rvert} = \lvert x \rvert \sqrt[n]{\lvert a_{n} \rvert}$$. Para aplicar el criterio de la raíz necesito estudiar $$\sqrt[n]{\lvert a_{n} \rvert}$$. Vamos a probar que hay convergencia uniforme en $$[-p,p]$$, con $$p < R$$ y que hay convergencia puntual en $$(-R,R)$$.


$$
p + \varepsilon < R =\frac{1}{\limsup \sqrt[n]{\lvert a_{n} \rvert}} \iff \limsup \sqrt[n]{\lvert a_{n} \rvert } < \frac{1}{p+\varepsilon}.
$$

 
Si $$\limsup \sqrt[n]{\lvert a_{n} \rvert} = \underset{n\geq 1}{\inf} \underset{k\geq n}{\sup} \{ \sqrt[k]{\lvert a_{k} \rvert } \} < \frac{1}{p+\varepsilon}$$, luego existe $$n_{0}$$ tal que 


$$
\underset{k\geq n_{0}}{\sup} \{ \sqrt[k]{\lvert a_{k} \rvert } \} < \frac{1}{p+\varepsilon}.
$$


Entonces $$\sqrt[k]{\lvert a_{k} \rvert} \leq \frac{1}{p + \varepsilon}$$ para todo $$k\geq n_{0}$$. Ahora, 


$$
\begin{aligned}
\sqrt[n]{\lvert a_{k} \rvert } < \frac{1}{p+\varepsilon} &\iff \lvert a_{k} \rvert < \frac{1}{(p+\varepsilon)^{k}} \\ 
&\implies \lvert x^{k}  \rvert \lvert a_{k} \rvert < \left( \frac{\lvert x \rvert }{p+\varepsilon}  \right)^k \leq \left( \frac{p }{p+\varepsilon}  \right)^k  
\end{aligned}
$$


para $$\lvert x \rvert \leq p$$. Como $$\sum_{k=1}^\infty \left( \frac{p}{p+\varepsilon} \right)^{k}$$ converge, concluimos que $$\sum_{k=1}^\infty a_{k} x^{k}$$ converge uniformemente por M-Test.

Entonces, la serie converge puntualmente en $$(-R, R)$$ con $$R = \frac{1}{\limsup \sqrt[n]{ \lvert a_{n} \rvert}}$$ y converge uniformemente en $$[-p,p]$$ con $$p < R$$. Lo mismo aplica para $$\hat{S}(x) = \sum_{k=1}^\infty a_{k}(x-x_{0})^{k}$$, la cual converge **puntualmente** si $$-R < x-x_{0} < R$$.

#### Ejercicio 
Sean $$\{a_{n}\}_{n=1}^\infty$$ y $$\{b_{n}\}_{n=1}^\infty$$ dos sucesiones tales que $$b_{n} \underset{n \rightarrow \infty}{\longrightarrow}b$$. Entonces
1. $$\limsup(a_{n}+b_{n}) = (\limsup a_{n}) + b$$.
2. $$\limsup(a_{n} b_{n}) = b \limsup a_{n}$$.

### Lema (Diferenciación y radio de convergencia)
Sea $$f_{n}(x) = a_{n} x^{n}$$ y $$f_{n}'(x) = n a_{n} x^{n}$$. Entonces las series de potencias $$S(x) = \sum_{n=0}^\infty f_{n}(x)$$ y $$S'(x) = \sum_{n=0}^\infty n a_{n} x^{n-1}$$ tienen el mismo radio de convergencia.

***Prueba:***  Considere $$\sum_{n=0}^\infty a_{n} n x^{n-1}$$, que tiene radio de convergencia $$\frac{1}{\limsup \sqrt[n]{n \lvert a_{n} \rvert}}$$. Desarrollando: 


$$
\limsup \sqrt[n]{n \lvert  a_{n} \rvert } = \limsup \sqrt[n]{n} \sqrt[n]{\lvert a_{n} \rvert } = \limsup \sqrt[n]{a_{n}},
$$


en donde usamos el hecho de que 


$$
\lim_{ n \to \infty } \sqrt[n]{n} = \lim_{ n \to \infty } \exp\left( \frac{\ln(n)}{n} \right) = \exp(0) = 1.
$$


Luego, las series 


$$
\sum_{n=0}^\infty n a_{n} x^{n-1} = \frac{1}{x}\sum_{n=0}^\infty n a_{n} x^{n} \quad \text{y} \quad \sum_{n=0}^\infty a_{n}x^{n}
$$


tienen el mismo radio de convergencia.

### Lema (R-integración y radio de convergencia)

***Prueba:***  Si $$S(x) = \sum_{n=0}^\infty a_{n} x^{n}$$ converge uniformemente en $$[-p,p]$$ con $$p <R$$, entonces


$$
\int_{0}^{x} S(y) \, dy = \sum_{n=0}^\infty \int_{0}^{x} a_{n} y^{n} \, dy = \sum_{n=0}^\infty a_{n} \frac{x^{n+1}}{n+1}.
$$


Analizando el radio de convergencia, note que 


$$
\limsup \sqrt[n]{\frac{\lvert a_{n} \rvert }{n+1}} = \limsup \frac{\sqrt[n]{\lvert a_{n} \rvert }}{\sqrt[n]{n+1}} = \limsup \sqrt[n]{\lvert  a_{n} \rvert, }
$$


pues $$\limsup \sqrt[n]{n+1} = \lim_{ n \to \infty } \sqrt[n]{n+1}$$. Concluimos entoces que 


$$
\sum_{n=0}^\infty a_{n} \frac{x^{n+1}}{n+1} \quad \text{y} \quad \sum_{n=0}^\infty a_{n}x^{n}
$$


tienen el mismo radio de convergencia.

## Series de Taylor

#### Ejemplo 
Sea $$\lvert x \rvert < 1$$ y considere $$\sum_{n=0}^\infty x^{n} = \frac{1}{1-x}$$. Como $$\limsup \sqrt[n]{1} = 1$$, tenemos convergencia uniforme en $$[-p,p]$$, con $$0<p<1$$. Entonces 


$$
\begin{aligned}
\int_{0}^{x} \frac{1}{1-y} \, dy  &= \int_{0}^{x} \sum_{n=0}^\infty y^{n} \, dy \\
\iff -\ln(1-x) &= \sum_{n=0}^\infty \frac{x^{n+1}}{n+1}.
\end{aligned}
$$


Manipulando la expresión resultante, para $$\lvert x \rvert < 1$$ tenemos que


$$
\begin{aligned}
-\ln(1+x) &= \sum_{n=0}^{\infty} \frac{(-x)^{n+1}}{n+1} \\
\iff \ln(1+x) &= \sum_{n=0}^\infty (-1)^{n} \frac{x^{n+1}}{n+1}.
\end{aligned}
$$


¿Podría ser que para dos sucesiones distintas, la serie de potencias asociadas converja a la misma función? Note que 


$$
S^{(n)}(x) = \left( \sum_{k=0}^\infty a_{k} x^{k}  \right)^{(n)} = \sum_{k=n}^\infty a_{k} k(k-1) \dots (k-n+1) x^{k-n}.
$$


Evaluando, 


$$
S^{(n)}(0) =  n(n-1)(n-2)\dots \cdot 2 \cdot 1 \cdot a_{n} = n! a_{n} \iff \frac{S^{(n)}(0)}{n!} = a_{n},
$$


por lo que la sucesión $$a_{n}$$ es única para cada función.

### Teorema (Taylor)
Sea $$f:[a,b] \to \mathbb{R}$$ una función tal que $$f',f'',\dots,f^{(n)}$$ son continuas en $$[a,b]$$. Si $$f^{(n+1)}$$ existe en $$[a,b]$$ y $$x_{0} \in (a,b)$$, existe $$c$$ entre $$x_{0}$$ y $$x$$ tal que 


$$
f(x) = f(x_{0}) + f'(x_{0})(x-x_{0}) + \dots+f^{(n)}(x_{0}) \frac{(x-x_{0})^{n}}{n!} + R_{n}(x),
$$


con $$R_{n}(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-x_{0})^{n+1}$$.

Considere la serie de potencias.


$$
S(x) = \sum_{n=0}^\infty a_{n}(x-x_{0})^{n}, \quad \text{con }a_{n} = \frac{f^{(n)}(x_{0})}{n!}
$$


¿Será cierto que $$S(x) = f(x)$$? Considere la suma parcial $$S_{k}(x) = \sum_{n=0}^{k} a_{n}(x-x_{0})^{n}$$. Entonces, 


$$
\lvert f(x) - S_{k}(x) \rvert = \lvert R_{k}(x) \rvert = \left\lvert  \frac{f^{(n+1)}(c)}{n+1} (x-x_{0})^{n+1}  \right\rvert \overset{?}{\underset{n \rightarrow \infty}{ \longrightarrow}}  0.
$$


Si el resto converge a cero, la serie de Taylor converge a la función.

#### Ejemplo 
Considere $$f(x) = \sin(x)$$. Entonces 


$$
\begin{aligned}
f'(x) &= \cos(x) \\
f''(x) &= -\sin(x) \\
f'''(x) &= -\cos(x) \\
f^{(4)}(x) &= \sin(x).
\end{aligned}
$$


En general, para $$x_{0}=0$$ tenemos que 


$$
f^{(2n)}(x) = 0,  \quad f^{(2n+1)}(0) = (-1)^{n}.
$$


Considerando la serie de Taylor $$\sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{(2n+1)!}$$, note que $$\limsup \sqrt[2n+1]{\frac{1}{(2n+1)!}} = 0$$. Luego, la serie converge en $$\mathbb{R}$$ y uniformemente en $$[-p,p]$$ para cualquier $$p>0$$. Por otro lado, 


$$
\begin{aligned}
\lvert \sin(x) - S_{n}(x) \rvert &= \left\lvert  \frac{f^{(n+1)}(c)}{(n+1)!} x^{n+1}  \right\rvert.
\end{aligned}
$$


Como 


$$
f^{(n+1)}(c) \begin{cases}
= \lvert \sin(c) \rvert \\ \\
= \lvert \cos(cazx  \quad) \rvert 
\end{cases} \leq  1,
$$


Entonces $$\lvert \sin(x) - S_{n}(x) \rvert \leq \frac{\lvert x^{n+1} \rvert}{(n+1)!}$$. Ahora, para $$\lvert x \rvert < p$$, entonces 


$$
\lvert \sin(x) - S_{n}(x) \rvert \leq \frac{\lvert \rho^{n+1} \rvert }{(n+1)!} < \varepsilon
$$


para  $$n\geq N_{0}$$, por el criterio del cociente para límites.

#### Ejemplo 
Considere $$f(x) = \exp(x)$$. Entonces $$f^{(n)}(x) = \exp(x)$$. Luego, para $$x_{0}=0$$, la serie de Taylor viene dada por 


$$
\sum_{n=0}^\infty \frac{x^{n}}{n!}, \quad \text{con } R = +\infty.
$$


Note que 


$$
S'(x) = \sum_{n=1}^\infty n \frac{x^{n-1}}{n!} = \sum_{n=1}^\infty \frac{x^{n-1}}{(n-1)!} = \sum_{n=0}^\infty \frac{x^{n}}{n!}. 
$$


Probaremos que $$S(x)S(y) = S(x+y)$$. Sea $$c \in \mathbb{R}$$ y $$h(x) = S(x)S(c-x)$$. Entonces 


$$
h'(x) = S'(x)S(c-x) - S(x)S'(c-x) =S(x)S(c-x) - S(x)S(c-x) = 0,
$$


por lo que $$h(x)$$ es constante. Luego, 


$$
h(x) = S(x) S(c-x) = S(c) S(0) = S(c).
$$


Evaluando $$c = x+y$$, entonces $$S(x)S(y) = S(x+y)$$.

Ahora, 


$$
\begin{aligned}
\lvert \exp(x) - S_{k}(x) \rvert = \left\lvert  \frac{f^{(n+1)}(c)}{(n+1)!} x^{n+1}  \right\rvert = \left\lvert  \frac{e^{c}}{(n+1)!} x^{n+1}  \right\rvert \leq  \frac{e^{p}}{(n+1)!} p^{n+1} \underset{n \rightarrow \infty}{\longrightarrow} 0
\end{aligned}
$$


para $$x \in [-p,p]$$ con $$c$$ entre 0 y $$x$$.

##### Ejercicio 
Pruebe que $$\exp(x) \geq 0$$ para cualquier $$x$$.
#### Ejemplo 
Considere $$f(x) = \cos(x)$$. Entonces


$$
\cos(x) = \sum_{n=0}^\infty (-1)^{n} \frac{x^{2n}}{(2n)!}, \quad \sin(x) = \sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{(2n+1)!}.
$$


Entonces 


$$
\begin{aligned}
\cos'(x) &= \sum_{n=1}^\infty (-1)^{n} (2n) \frac{x^{2n-1}}{(2n)!} \\
&= \sum_{n=1}^\infty (-1)^{n} \frac{x^{2n-1}}{(2n-1)!} \\
&= \sum_{n=0}^\infty (-1)^{n+1} \frac{x^{2n+1}}{(2n+1)!} \\
&= - \sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{(2n+1)!} = -\sin(x).
\end{aligned}
$$


De manera análoga, podemos probar que $$\sin'(x) = \cos(x)$$. 

Note que $$\sin(0)=0$$, $$\cos(0)=1$$. Además, 


$$
(\sin^{2}(x)+\cos ^{2}(x))' = 2\sin x\cos x + 2 \sin x \cos x + 2 \cos x(-\sin x) = 0.
$$


Luego, $$\sin ^{2}(x)+\cos^{2}(x) = \sin ^{2}(0)+\cos^{2}(0) = 1$$.

##### Ejercicio 
Probar que $$\sin(x+y)=\sin(x)\cos(y) + \cos(x)\sin(y)$$ y que $$\cos(x+y) = \cos(x)\cos(y) - \sin(x)\sin(y)$$.

Ahora, note que 


$$
\cos(x) = \sum_{n=}^\infty (-1)^{n} \frac{x^{2n}}{(2n)!} = \left( 1-\frac{x^{2}}{2}  \right) + \left( \frac{x^{4}}{4!} - \frac{x^{6}}{6!}\right) + \cdots,
$$


por lo que $$\cos(x)\geq 0$$ si 


$$
\begin{aligned}
\frac{x^{2n}}{(2n)!} - \frac{x^{2n+2}}{(2n+2)!} &\geq 0 \\
\iff {x^{2n}}{(2n)!} &\geq \frac{x^{2n+2}}{(2n+2)!} \\
\iff (2n+1)(2n+2) \geq  x^{2},
\end{aligned}
$$


lo cual se cumple para $$0\leq x\leq 1$$. Note que si $$\cos(x)\geq 0$$ entonces $$\sin'(x) \geq 0$$ y entonces $$\sin$$ es creciente. Por tanto, sin $$\cos(x)\geq 0$$ para todo $$x \in [0,p]$$, $$\sin$$ es creciente en $$[0,p]$$. Además, como $$\sin(0) = 0$$, tenemos que $$\sin(x) \geq 0$$ para $$x \in [0,p]$$. Luego, $$\cos(x)$$ es decreciente.

Probaremos ahora que existe $$c \in \mathbb{R}$$ tal que $$\cos(c) < 0$$. Sabemos que $$\cos(0) = 1$$ y $$\sin(0) = 0$$. Usando la serie de Taylor del coseno, tenemos que 


$$
\cos(y) \leq  1 \iff \int_{0}^{x} \cos(y) \, dy \leq  \int_{0}^{x} 1 \, dy \iff \sin(x) \leq  x.
$$


Luego, 


$$
\int_{0}^{x} \sin(y) \, dy \leq  \int_{0}^{x} y \, dy = \frac{x^{2}}{2} \iff 1-\cos(x) \leq \frac{x^{2}}{2} \iff 1-\frac{x^{2}}{2} \leq  \cos(x).
$$


Integrando a ambos lados en esta última desigualdad, tenemos que $$\sin(x)\geq x - \frac{x^{3}}{6}$$, e integrando una vez más, tenemos que 


$$
\cos(x) \leq 1-\frac{x^{2}}{2}+\frac{x^{4}}{4!},
$$


de donde si evaluamos $$x = \sqrt{ 3 }$$, obtenemos un valor negativo al lado derecho y por tanto probamos que $$\cos(\sqrt{ 3 }) \leq 0$$, i.e., existen valores en donde el coseno es negativo.

Por continuidad, tenemos que existe algún cero de la función. Sea $$p$$ el primer cero. 

Analizaremos ahora el periodo de $$\sin$$ y $$\cos$$. Como $$\cos(p) = 0$$, tenemos que 


$$
\begin{aligned}
\sin(2p) = \sin(p)\cos(p) + \sin(p) \cos(p) &= 0, \\
\sin ^{2}(p) +\cos ^{2}(p) = \sin ^{2}(p) &= 1 \implies \sin(p) = \pm 1.
\end{aligned}
$$


Note que 


$$
\begin{aligned}
\sin(x+4p) &= \sin(x) \cos(4p) + \cos(x) \sin(4p),\\
\sin(4p) &= \sin(2p)\cos(2p) + \sin(2p)\cos(2p) = 0 \\
\cos(4p) &= \cos(2p)^{2} - \sin(2p)^{2} = 1  \quad \text{pues } \cos(2p) =\pm 1,
\end{aligned}
$$


De donde concluimos que $$\sin(x+4p) = \sin(x)$$. 

#### Ejemplo 
Habíamos visto que 


$$
\ln(1+x) = \sum_{n=0}^\infty (1)^{n+1} \frac{x^{n+1}}{n+1}.
$$


Observando que 


$$
\frac{(\ln(1+x))^{(n)}}{n!} \biggr\rvert_{x=0} = \frac{(-1)^{n+1}}{n+1},
$$


tenemos que la serie de Taylor converge a a la función.

![Pasted image 20250708163347](/assets/img/courses/ma0350/Pasted%20image%2020250708163347.png)

## Trucos
1. Si $$\lim_{ n \to \infty } \sqrt[n]{a_{n}}$$ es muy dificil, usar que $$\lim_{ n \to \infty } \frac{a_{n+1}}{a_{n}}$$ tiene que valer lo mismo.
2. Calcular el supp siempre que estemos mal
{% endraw %}
