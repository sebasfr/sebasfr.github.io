---
layout: chapter
course: ma0350
chapter: 2
title: "Subsucesiones"
slug: 02-subsucesiones
toc:
  sidebar: right
lang: es
---

{% raw %}
En esta nota, definimos y desarrollamos lo relacionado a subsucesiones de Sucesiones. Ver también: Límite superior e inferior.
### Definición 

Dada una sucesión $$\{x_{n}\}_{n=1}^\infty$$ y dada una función $$\phi:\mathbb{N} \to \mathbb{N}$$ estrictamente creciente, definimos la sucesión $$\{x_{\phi(n)}\}_{n=1}^\infty$$ como una subsucesión de $$\{x_{n}\}_{n=1}^\infty$$.

### Lema  

Sea $$\phi:\mathbb{N} \to \mathbb{N}$$ una función estrictamente creciente. Entonces $$\phi(n) \geq n$$ para todo $$n \in \mathbb{N}$$.

***Prueba:*** Se usará inducción sobre n.
**Caso base:** Para $$n = 0$$, note que $$\phi(0) \in \mathbb{N}$$, entonces $$\phi(0) \geq 0$$ trivialmente. Esto prueba el caso base.
**Paso inductivo:** Sea $$m \in \mathbb{N}$$ fijo y arbitrario. Suponga como hipótesis inductiva que $$\phi(m) \geq m$$. Hay que probar que $$\phi(m+1) \geq m+1$$. Note que $$m \leq \phi(m) < \phi(m+1)$$. Luego, como $$\phi(m+1) \in \mathbb{N}$$ y $$\phi(m+1) > m$$, tenemos que $$\phi(m+1) \geq m+1$$. Esto prueba el paso inductivo. Conclúyase que $$\phi(n) \geq n$$ para todo $$n \in \mathbb{N}$$. 

### Lema 

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión tal que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$ y sea $$\{x_{\phi(n)}\}_{n=1}^\infty$$ una subsucesión. Entonces $$x_{\phi(n)} \underset{n \rightarrow \infty}{\longrightarrow} L$$.

***Prueba:*** Dado $$\varepsilon >0$$, existe $$N \in \mathbb{N}$$ tal que $$\lvert x_{n}-L \rvert < \varepsilon$$ si $$n \geq N$$. Ahora, $$\phi(n) \geq n \geq N$$ , entonces $$\lvert x_{\phi(n)} - L \rvert < \varepsilon$$ para $$n \geq N$$.  
 
#### Ejemplo 

Sea $$w_{n} = \cos(n\pi) = (-1)^{n}$$. Entonces $$w_{2n} \underset{n \rightarrow \infty}{\longrightarrow} 1$$ y $$w_{2n+1} \underset{n \rightarrow \infty}{\longrightarrow} -1$$. Por tanto $$w_{n}$$ diverge.

### Teorema (Bolzano-Weirerstrass):

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión acotada. Entonces existe una subsucesión $$\{x_{k_{n}}\}_{n=1}^{\infty}$$ que converge.
***Prueba:*** Suponga que $$a \leq x_{n} \leq b$$ para todo $$n \in \mathbb{N}$$. Sean 


$$
\begin{aligned}
A_{1}^{1} &= \left\{  n: a\leq x_{n} \leq \frac{a+b}{2}  \right\} \\
A_{2}^{1} &= \left\{  n: \frac{a+b}{2} \leq x_{n} \leq b \right\}
\end{aligned}
$$


Entonces $$A_{1}^{1}$$ es infinito o $$A_{2}^{1}$$ es infinito. Si $$A_{1}^{1}$$ es infinito, tome $$a_{1}=a$$ y $$b_{1} = \frac{a+b}{2}$$. Existen infinitos $$x_{n}$$ tales que $$a_{1} \leq x_{n} \leq b_{1}$$. Note que $$a = a_{1}$$, $$b_{1} < b$$. Por otro lado, si $$A_{2}^{1}$$ es infinito, entonces tome $$a_{1} = \frac{a+b}{2}$$ y $$b_{1} = b$$. En este caso, $$a < a_{1}$$ y $$b = b_{1}$$. Note que, en ambos casos, $$b_{1}-a_{1} = \frac{b-a}{2}$$. Concluimos que existen infinitos $$n$$ tal que $$a_{1} \leq x_{n} \leq b_{1}$$. Ahora, sean 


$$
\begin{aligned}
A_{1}^{2} &= \left\{  n: a_{1}\leq x_{n} \leq \frac{a_{1}+b_{1}}{2}  \right\} \\
A_{2}^{2} &= \left\{  n: \frac{a_{1}+b_{1}}{2} \leq x_{n} \leq b_{1} \right\}
\end{aligned}
$$


Entonces $$A_{1}^{2}$$ es infinito o $$A_{2}^{2}$$ es infinito. Si $$A_{1}^{2}$$ es infinito, tome $$a_{2}=a_{1}$$ y $$b_{2} = \frac{a_{1}+b_{1}}{2}$$. Existen infinitos $$x_{n}$$ tales que $$a_{2} \leq x_{n} \leq b_{2}$$. Note que $$a_{1} = a_{2}$$, $$b_{2} < b_{1}$$. Por otro lado, si $$A_{2}^{1}$$ es infinito, entonces tome $$a_{2} = \frac{a_{1}+b_{1}}{2}$$ y $$b_{2} = b_{1}$$. En este caso, $$a_{1} < a_{2}$$ y $$b_{1} = b_{2}$$. Note que, en ambos casos, $$b_{2}-a_{2} = \frac{b_{1}-a_{1}}{2} = \frac{b-a}{2^{2}}$$. Concluimos que existen infinitos $$n$$ tal que $$a_{1} \leq x_{n} \leq b_{1}$$. 

Iterando el proceso, podemos encontrar $$a_{n}$$ y $$b_{n}$$ tales que 
1. Existen infinitos $$m \in \mathbb{N}$$ tales que $$a_{n} \geq x_{m} \leq b_{n}$$.
2. $$a \leq a_{n} \leq a_{n+1} \leq b$$.
3. $$a\leq b_{n+1} \leq b_{n} \leq b$$
4. $$b_{n}-a_{n} = \frac{b-a}{2^{n}}$$

Por teorema de convergencia monótona, como $$\{a_{n}\}_{n=1}^\infty$$ y $$\{b_{n}\}_{n=1}^\infty$$ son acotadas y monótonas, entonces convergen. Suponga que $$a_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{1}$$ y $$b_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{2}$$. Note que 


$$
\ell_{2}-\ell_{1} =\lim_{ n \to \infty } b_{n}-a_{n} = \lim_{ n \to \infty } \frac{b-a}{2^{n}} = 0.
$$


Conclúyase que $$\ell_{2} = \ell_{1}$$. Sea $$x_{k_{1}}$$ tal que $$a_{1} \leq x_{k_{1}} \leq b_{1}$$. Sea $$B_{2} = \{ m:a_{2} \leq x_{m} \leq b_{2} \}$$. Note que, por construcción, $$B_{2}$$ posee infinitos elementos. Tome $$k_{2} \in B -\{ 0,\dots,k_{1} \}$$. 

En general, sea $$B_{n} = \{ m: a_{n} \leq x_{m} \leq b_{n} \}$$. Note que $$B_{n}$$ posee infinitos elementos. Tome $$k_{n} \in B_{n} - \{ 0,\dots,k_{n-1} \}$$. Entonces, tenemos una subsucesión $$\{x_{k_{n}}\}_{n=1}^\infty$$ tal que $$a_{n} \leq x_{k_{n}} \leq b_{n}$$. Luego $$\ell_{1} = \lim_{ n \to \infty } a_{n} \leq \lim_{ n \to \infty } x_{k_{n}} \leq \lim_{ n \to \infty } b_{n} = \ell_{2}$$, en donde concluimos que $$\{x_{k_{n}}\}_{n=1}^\infty$$ converge por teorema del sandwich. 

### Teorema (Cauchy implica acotación)

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión de Cauchy. Entonces es acotada.

***Prueba:*** Tome $$\varepsilon = 1$$. Existe $$N \in \mathbb{N}$$ tal que $$\lvert x_{n} - x_{m} \rvert < 1$$ para todos $$m,n \geq N$$. En particular (tomando $$m = N$$), $$\lvert x_{n} \rvert -\lvert x_{N} \rvert \leq  \lvert x_{n} - x_{N} \rvert < 1$$. Entonces, $$\lvert x_{n} \rvert < 1 + \lvert x_{N} \rvert$$. Sea $$M = \max \{ \lvert x_{1} \rvert, \lvert x_{2} \rvert, \dots, \lvert x_{N-1} \rvert, 1 + \lvert x_{N}  \rvert \}$$. Entonces $$\lvert x_{n} \rvert \leq M$$ para todo $$n \in \mathbb{N}$$.

### Teorema  (Cauchy implica convergencia)

Si $$\{x_{n}\}_{n=1}^\infty$$ es de Cauchy, entonces es converge.

***Prueba:*** Como $$\{x_{n}\}_{n=1}^\infty$$ es de Cauchy, entonces es acotada. Luego, por Bolzano-Weirerstrass, existe una subsucesión $$\{ x_{k_{n}} \}_{n=1}^{\infty}$$ tal que $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Sea $$\varepsilon > 0$$. Entonces existe $$N \in \mathbb{N}$$ tal que $$\lvert x_{n}-x_{m} \rvert < \frac{\varepsilon}{2}$$ si $$n,m \geq N$$. Además, existe $$N_{1} \in \mathbb{N}$$ tal que $$N_{1} \geq N$$ y $$\lvert x_{k_{n}} - L \rvert < \frac{\varepsilon}{2}$$ si $$n \geq N_{1}$$. Luego, para todo $$n \geq N_{1}$$, $$k_{n} \geq n \geq N_{1} \geq N$$, entonces 


$$
\lvert x_{n} - L \rvert \leq \lvert x_{n} - x_{k_{n}} \rvert + \lvert x_{k_{n}} - L \rvert < \varepsilon. 
$$


Conclúyase entonces que $$\{x_{n}\}_{n=1}^\infty$$ converge. 

### Teorema (Criterio secuencial del límite)

Sea $$f:(a,b) \to \mathbb{R}$$ y $$c \in (a,b)$$. Entonces $$\lim_{x \to c } f(x) = L$$ si y solo si para toda sucesión $$\{x_{n}\}_{n=1}^\infty \subseteq (a,b)$$ tal que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}c$$, tenemos que $$\lim_{ n \to \infty } f(x_{n}) = L$$.

***Prueba:*** ($$\impliedby$$): Probaremos la contrapositiva. Asuma que existe $$\varepsilon>0$$ tal que para todo $$\delta > 0$$ existe $$x_{\delta}$$ tal que $$\lvert x- c \rvert < \delta$$ y $$\lvert f(x_{\delta}) - L \rvert \geq \varepsilon$$. Tome $$\delta = \frac{1}{n}$$. entonces, existe $$x_{k_{n}}$$ tal que $$\lvert x_{k_{n}} - c \rvert < \frac{1}{n}$$ y $$\lvert f(x_{k_{n}}) - L \rvert \geq \varepsilon$$. Note que $$\lim_{ n \to \infty } \lvert x_{k_{n}} - c \rvert = 0$$, y por lo tanto $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} c$$, pero $$f(x_{k_{n}}) \underset{n \rightarrow \infty}{\cancel{ \longrightarrow }} L$$. 

La otra dirección ya la habíamos probado.
{% endraw %}
