---
layout: chapter
course: ma0350
chapter: 1
title: "Sucesiones"
slug: 01-sucesiones
toc:
  sidebar: right
lang: es
fecha: 2025-03-11
---

{% raw %}
Sea $$0<x<1$$, entonces


$$
x = 0,\bar{a_{1}}\bar{a_{2}}\bar{a_{3}}\dots
$$


Sea $$x_{1} = 10x$$, entonces $$0<x_{1} <10$$. Si $$0 \leq x_{1} <1$$, entonces tenemos que el primer decimal viene dado por $$a_{1} = 0$$. Si no, itere para encontrar el natural $$0 \leq n_{1} \leq 9$$ tal que $$n_{1} \leq x_{1} < n_{1} + 1.$$ Entonces $$0 \leq a_{1}=n_{1} \leq 9 \quad \text{(1)}$$. 

Ahora, tome $$x_{2} = 10(x_{1}-n_{1})$$. Note que $$0\leq x_{2} < 10$$.  Tome $$a_{2} = n_{2}$$, donde $$n_{2}$$ es tal que $$n_{2}\leq x_{2} \leq n_{2}+1.$$  De (1), tenemos que 


$$
\begin{aligned}
n_{1} &\leq 10x < n_{1} + 1\\
\implies \frac{n_{1}}{10} &\leq  x < \frac{n_{1}}{10}+\frac{1}{10} \\
\implies 0 &\leq x-\frac{n_{1}}{10} < \frac{1}{10}.
\end{aligned}
$$


Además, 


$$
\begin{aligned}
&n_{2} \leq 10(x_{1}-n_{1}) < n_{2} + 1\\
\implies & \frac{n_{2}}{10} \leq  x_{1}-n_{1} < \frac{n_{2}}{10}+\frac{1}{10} \\
\implies & n_{1}+\frac{n_{2}}{10} \leq x_{1} < n_{1} + \frac{n_{2}}{10} + \frac{1}{10}  \\
\implies & n_{1}+\frac{n_{2}}{10} \leq 10x < n_{1} + \frac{n_{2}}{10} + \frac{1}{10}  \\
\implies & \frac{n_{1}}{10}+\frac{n_{2}}{100} \leq x < \frac{n_{1}}{10} + \frac{n_{2}}{100} + \frac{1}{100}  \\
\implies&  0\leq x -\frac{n_{1}}{10} -\frac{n_{2}}{100} < \frac{1}{10^{2}}.
\end{aligned}
$$


Iterando el proceso, obtenemos 


$$
0\leq n_{1},n_{2},n_{3},...,n_{k} \leq 9,
$$


con 


$$
\frac{n_{1}}{10} +\frac{n_{2}}{10^{2}}+\frac{n_{3}}{10^{3}} + \dots + \frac{n_{k}}{10^{k}} \leq x \leq \frac{n_{1}}{10} +\frac{n_{2}}{10^{2}}+\frac{n_{3}}{10^{3}} + \dots + \frac{n_{k}}{10^{k}} + \frac{1}{10^{k}}.
$$



Sea $$x_{k+1} = 10(x_{k}-n_{k})$$. Entonces existe $$n_{k+1} \in \mathbb{N}$$ tal que $$n_{k+1} \leq x_{k+1} < n_{k+1} +1,$$ con $$0\leq n_{k+1} \leq 9.$$ Como 


$$
0 \leq \underbrace{ x-\frac{n_{1}}{10}-\frac{n_{2}}{10^{2}} - \frac{n_{3}}{10^{3}} - \dots - \frac{n_{k}}{10^{k}} }_{ y_{1} } < \frac{1}{10^{k}},
$$


tenemos que $$0 \leq 10^{k+1} y_{1} < 10$$. Entonces, $$x_{k+1} = 10^{k+1}y_{1}$$. Sabemos que $$n_{k+1} \leq x_{k+1} < n_{k+1} +1,$$, entonces 


$$
\begin{aligned}
& n_{k+1} \leq 10^{k+1}\left( x-\frac{n_{1}}{10}-\frac{n_{2}}{10^{2}}-\frac{n_{3}}{10^{3}}-\dots-\frac{n_{k}}{10^{k}} \right) < n_{k+1}+1\\
\implies & 0 \leq x-\frac{n_{1}}{10}-\frac{n_{2}}{10^{2}}-\frac{n_{3}}{10^{3}}-\dots-\frac{n_{k}}{10^{k}} - \frac{n_{k+1}}{10^{k+1}} < \frac{1}{10^{k+1}}.
\end{aligned}
$$


Conclúyase por inducción que $$x - \left( \frac{n_{1}}{10} + \frac{n_{2}}{10^{2}} +\frac{n_{3}}{10^{3}} +\dots+ \frac{n_{k}}{10^{k}} \right) < \frac{1}{10^{k}}$$. Las sucesiones nacen para aproximar números.

## Suceciones 

### Definición (Sucesión real-valuada)

Una sucesión en $$\mathbb{R}$$ (denotada $$\{x_{n}\}_{n=1}^\infty$$), es una función $$\underset{n \to x_{n}}{f:\mathbb{N} \to \mathbb{R}}$$.

### Definición (Convergencia)

Decimos que una sucesión $$\{x_{n}\}_{n=1}^\infty$$ converge a $$L$$ $$(\lim_{ n \to \infty } x_{n} = L)$$, denotado por $$x_{n} \underset{n \rightarrow  \infty}{\longrightarrow} L$$, si para todo $$\varepsilon > 0$$, existe $$N \in \mathbb{N}$$ tal que para todo $$n \geq N$$, $$\lvert x_{n}-L \rvert < \varepsilon$$. 
 
#### Ejemplo 

Dado $$x \in (0,1)$$, existe $$x_{m} = \sum_{i=1}^{m} \frac{n_{i}}{10^{i}}$$ que satisface $$\lvert x-x_{m} \rvert < \frac{1}{10^{m}}$$. Sea $$\varepsilon > 0$$ fijo y arbitrario. Tome $$N = \left\lceil  \log_{10}\left( \frac{1}{\varepsilon} \right)  \right\rceil$$. Sea $$n \geq N$$ fijo y arbitrario. Note que 


$$
\log_{10} \left( \frac{1}{\varepsilon} \right) \leq M \leq n
$$




$$
\implies\quad\frac{1}{\varepsilon} \leq 10^{n}
$$




$$
\implies \frac{1}{10^{n}} \leq \varepsilon
$$




$$
\implies \lvert x_{n} - x \rvert < \frac{1}{10^{n}} \leq \varepsilon. 
$$


 Conclúyase que $$\lim_{ n \to \infty } x_{n} = x$$.

### Teorema (Unicidad del límite) 

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión tal que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{1}$$ y $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{2}$$. Entonces, $$\ell_{1} = \ell_{2}$$.

***Prueba:*** Suponga por contradicción que $$\ell_{1} \neq \ell_{2}$$. Considere 


$$
0 < \lvert \ell_{2} - \ell_{2} \rvert \leq \lvert \ell_{1}-x_{n} \rvert + \lvert x_{n}-\ell_{2} \rvert.
$$


Tome $$\varepsilon = \frac{\lvert \ell_{1}-\ell_{2} \rvert}{2}$$. Entonces existe $$N \in \mathbb{N}$$ tal que $$\lvert \ell_{1}-x_{n} \rvert < \varepsilon$$ y que $$\lvert x_{n} - \ell_{2} \rvert < \varepsilon$$. para $$n \geq N$$. Luego, 


$$
0 < \lvert \ell_{1} - \ell_{2} \rvert \leq  \lvert x_{n}-\ell_{1} \rvert + \lvert x_{n} - \ell_{2} \rvert < 2\varepsilon = \lvert \ell_{1} - \ell_{2} \rvert. \quad (\Rightarrow\!\Leftarrow)
$$



### Teorema (Acotación)

Sea $$\{x_{n}\}_{n=1}^\infty$$ tal que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Entonces, $$\{x_{n}\}_{n=1}^\infty$$ es acotada.

***Prueba:*** Tome $$\varepsilon = 1$$. Entonces existe $$N \in \mathbb{N}$$ tal que $$\lvert x_{n}-1 \rvert < 1$$ para $$n \geq N$$, es decir, 


$$
L -1 < x_{n} <L+1 \implies \lvert x_{n} \rvert < \max\{\lvert L+1 \rvert , \lvert L-1 \rvert \}.
$$


Tome $$M = \max \{\lvert x_{1} \rvert\ , \lvert x_{2} \rvert,\dots,\lvert x_{N} \rvert, \lvert L-1 \rvert, \lvert L+1 \rvert\}$$. Entonces $$\lvert x_{n} \rvert \leq M$$ para todo $$n \in \mathbb{N}$$. 

#### Corolario 

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión no acotada. Entonces $$\{x_{n}\}_{n=1}^\infty$$ es divergente. 
***Prueba:*** Se sigue directamente de la contrapositiva del teorema.

#### Ejemplo 

Sea $$b>1$$ y sea $$y_{n} = b^{n}$$ para $$n \geq 0$$. Asuma que existe $$M \in \mathbb{R}$$ tal que $$b^{n} \leq M$$ para todo $$n \in \mathbb{N}$$. Por desigualdad de Bernoulli, tenemos que $$1 + n(b-1) \leq b^{n} \leq M$$. Pero esto implica que $$n \leq \frac{M-1}{b-1}$$ para todo $$n \in \mathbb{N}$$, es decir,  que la sucesión $$\{n_{}\}_{n=1}^\infty$$ es acotada $$(\Rightarrow\!\Leftarrow)$$. 

### Definición (Sucesión de Cauchy)

Sea $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$. Decimos que la sucesión es de Cauchy si para todo $$\varepsilon>0$$ existe $$N_{0} \in \mathbb{N}$$ tal que $$\lvert x_{n}-x_{m} \rvert < \varepsilon$$ para todos $$n,m \geq N_{0}$$. 

### Teorema (Convergencia implica Cauchy)

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión tal que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L \in \mathbb{R}$$. entonces $$\{x_{n}\}_{n=1}^\infty$$ es de Cauchy. 

***Prueba:*** Asuma que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Entonces, dado $$\varepsilon > 0$$, existe $$N_{0} \in \mathbb{N}$$ tal que $$\lvert x_{n} - L \rvert > \frac{\varepsilon}{2}$$ para todo $$n \geq N_{0}$$. Sean $$n,m \geq N_{0}$$ fijos y arbitrarios. Entonces 


$$
\lvert x_{n} - x_{m} \rvert \leq \lvert x_{n} - L \rvert + \lvert x_{m} - L \rvert < \varepsilon.
$$


Conclúyase que $$\{x_{n}\}_{n=1}^\infty$$ es de Cauchy. 
#### Corolario 
Si $$\{x_{n}\}_{n=1}^\infty$$ no es de Cauchy, entonces no converge. 
 
#### Ejemplo 

Sea $$z_{n} = (-1)^{n}$$.  Note que 


$$
z_{n} =
\begin{cases}
1  \quad\text{si $n$ es par} \\
-1  \quad\text{si $n$ es impar}
\end{cases}
$$


Sea $$0 < \varepsilon <2$$ y $$N_{0} \in \mathbb{N}$$. Tome $$n = 2N_{0} > N_{0}$$ y $$m = 2N_{0}+1>N_{0}$$. Entonces $$\lvert x_{n} - x_{m}\rvert = 2 > \varepsilon$$. Por tanto $$\{z_{n}\}_{n=1}^\infty$$ no es de Cauchy y diverge. 

### Definición (Divergencia hacia infinito)

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión. Decimos que diverge a infinito, y lo denotamos por $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \infty$$ ($$\lim_{ n \to \infty } x_{n} = \infty$$) si para todo $$\alpha > 0$$ existe $$N \in \mathbb{N}$$ tal que $$x_{n} > \alpha$$ para todo $$n \geq N$$. De la misma manera, $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} -\infty$$ si para todo $$\beta >0$$, existe $$N \in \mathbb{N}$$ tal que $$x_{n} < -\beta$$ para todo $$n \geq N$$. 
 
#### Ejemplo 

Si $$b>1$$ y $$y_{n} = b^{n}$$, entonces $$y_{n} \underset{n \rightarrow \infty}{\longrightarrow}\infty$$.  $$\underset{}{\sup}$$

### Teorema (Convergencia monótona)

Sea $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$.
1. Si $$\{x_{n}\}_{n=1}^\infty$$ es decreciente y acotada inferiormente, entonces $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \underset{n \in \mathbb{N}}{\inf} x_{n}$$.
2. Si $$\{x_{n}\}_{n=1}^\infty$$ es creciente y acotada superiormente, entonces $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \underset{n \in \mathbb{N}}{\sup} x_{n}$$. 

***Prueba de 2:*** Asuma que $$\{x_{n}\}_{n=1}^\infty$$ es creciente y acotada superiormente. Tome $$L = \underset{n \in \mathbb{N}}{\sup} x_{n}$$ y $$\varepsilon >0$$ fijo y arbitrario. Por definición de supremo, existe $$N \in \mathbb{N}$$ tal que $$L - \varepsilon < x_{N} \leq L$$. Tome $$n \geq N$$, entonces $$x_{n} \geq x_{N}$$. Luego $$L - \varepsilon < x_{N} \leq x_{n} \leq L$$. Por tanto, conclúyase que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}L$$. La prueba de 1. es análoga. 
 
#### Ejemplo 

Considere $$z_{n} = a^{n}$$ con $$0<a<1$$. Note que $$a < 1$$, entonces $$a^{n+1} < a^{n}$$. Sea $$L = \underset{n \in \mathbb{N}}{\inf} z_{n}$$. Tome $$\varepsilon>0$$. Por definición de ínfimo, sabemos que existe $$N_{1} \in \mathbb{N}$$ tal que $$L \leq a^{N_{1}} < L + \varepsilon$$. Sea $$n \geq N_{1}$$. Entonces $$L \leq a^{n} < a^{N_{1}} < L + \varepsilon$$, i.e. $$\lvert a^{n}-L \rvert < \varepsilon$$. Por tanto, $$z_{n} \underset{n \rightarrow \infty}{\longrightarrow}L$$. Probaremos ahora que $$L = 0$$. Para ello, suponga por contradicción que $$L>0$$, es decir, que para todo $$n \in \mathbb{N}$$, $$0 < L < a^{n}$$. Entonces, $$\left( \frac{1}{a} \right)^{n} < \frac{1}{L}$$, una contradicción pues $$\frac{1}{a} > 1$$ y en dado caso las sucesión diverge a $$\infty$$. 

### Teorema (Propiedades algebraícas del límite)

Sean $$\{x_{n}\}_{n=1}^\infty$$ y $$\{y_{n}\}_{n=1}^\infty$$ sucesiones en $$\mathbb{R}$$ tales que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}\ell_{1}$$ y $$y_{n} \underset{n \rightarrow \infty}{\longrightarrow}\ell_{2}$$. Entonces:
1. $$x_{n} + y_{n} \underset{n \rightarrow \infty}{\longrightarrow} \ell_{1} + \ell_{2}$$.
2. $$x_{n}y_{n} \underset{ \rightarrow \infty}{\longrightarrow} \ell_{1} \ell_{2}$$.
3. Si $$y_{n} \neq 0$$ para todo $$n \in \mathbb{N}$$ y $$\ell_{2} \neq 0$$, $$\frac{1}{y_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{\ell_{2}}$$.

***Prueba de 3:***  Sabemos que $$\ell_{2} \neq 0$$. Sea $$\varepsilon > 0$$ fijo y arbitrario. Entonces, existe $$N_{1} \in \mathbb{N}$$ tal que 


$$
\begin{aligned}
&\lvert y_{n} \rvert - \lvert \ell_{2} \rvert \leq \lvert y_{n}-\ell_2 \rvert < \varepsilon \leq \\
\implies & \lvert l_{2}\rvert - \varepsilon < \lvert y_{n} \rvert.
\end{aligned}
$$


Tomo $$\varepsilon = \frac{\lvert l_{2} \rvert}{2}$$, entonces $$\lvert y_{n} \rvert \geq\lvert l_{2} \rvert - \varepsilon \geq \lvert \ell_{2} \rvert - \frac{\lvert l_{2} \rvert}{2} = \frac{\lvert \ell_{2} \rvert}{2}$$ para $$n \geq N_{1}$$, es decir, $$\frac{1}{\lvert y_{n} \rvert} \leq \frac{2}{\lvert \ell_{2} \rvert}$$. Luego, para $$n\geq N_{1}$$, tenemos que 


$$
\left\lvert  \frac{1}{y_{n}} - \frac{1}{\ell_{2}}  \right\rvert = \frac{\lvert \ell_{2} - y_{n} \rvert }{\lvert y_{n} \rvert \lvert \ell_{2} \rvert } \leq \frac{\lvert \ell_{2}-y_{n} \rvert }{\lvert \ell_{2} \rvert} \frac{2}{\lvert \ell_{2} \rvert }.
$$


Sea $$N_{2} \in \mathbb{N}$$ tal que $$\lvert y_{n} - \ell_{2} \rvert < \frac{\varepsilon \lvert \ell_{2} \rvert}{2}$$. Entonces, para $$n \geq \max\{N_{1}, N_{2}\}$$, tenemos que 


$$
\left\lvert  \frac{1}{y_{n}} - \frac{1}{\ell_{2}}  \right\rvert = \frac{\lvert y_{n}-\ell_{2} \rvert }{\lvert  y_{n} \rvert \lvert \ell_{2} \rvert } \leq \frac{2\lvert y_{n}-\ell_{2} \rvert }{\lvert \ell_{2} \rvert ^{2}} < \frac{\varepsilon \lvert \ell_{2} \rvert ^{2}}{2} \frac{2}{\lvert \ell_{2} \rvert ^{2}} = \varepsilon.
$$


Conclúyase que $$\frac{1}{y_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{\ell_{2}}$$. 

### Teorema (Límites y funciones continuas)

Sea $$\{x_{n}\}_{n=1}^\infty$$ tal que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$ y sea $$f:(a,b) \to \mathbb{R}$$ continua tal que $$L \in (a,b)$$. Entonces $$f(x_{n}) \underset{n \rightarrow \infty}{\longrightarrow} f(L)$$.

***Prueba:*** Dado $$\varepsilon>0$$, existe $$\delta > 0$$ tal que si $$\lvert x-L \rvert < \delta$$ entonces $$\lvert f(x) - f(L)  \rvert < \varepsilon$$. Como $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$, existe $$N_{0}$$ tal que $$\lvert x_{n} - L\rvert < \delta$$ si $$n \geq N_{0}$$. Luego, para todo $$n \geq N_{0}$$, $$\lvert x_{n} - L \rvert < \delta$$ y en consecuencia $$\lvert f(x_{n}) - f(L) \rvert < \varepsilon$$. 
 
#### Ejemplo 

 $$\sqrt{ 1+\frac{2}{1+\frac{1}{n}}} \underset{n \rightarrow \infty}{\longrightarrow} \sqrt{ 3 }$$. 
 Note que: 


$$
\frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} 0
$$





$$
\implies 1+\frac{1}{n} \underset{n \rightarrow \infty}{\longrightarrow} 1
$$


pues $$1+x$$ es continua en $$\mathbb{R}$$, 


$$
\implies \frac{2}{1+\frac{1}{n}} \underset{n \rightarrow \infty}{\longrightarrow} 2
$$


pues $$\frac{2}{x}$$ es continua en $$(0,+\infty)$$, 


$$
\implies \sqrt{ 1 + \frac{2}{1+\frac{1}{n}} } \underset{n \rightarrow \infty}{\longrightarrow} \sqrt{ 3 },
$$


pues $$\sqrt{ 1+x }$$ es continua en $$(0,+\infty)$$. 
 
#### Ejemplo 

Calcule $$\lim_{ n \to \infty } k - \sqrt{ k^{2}-k }$$.

Note que 


$$
\begin{aligned}
x_{k} &= \frac{(k-\sqrt{ k^{2}-k })(k+\sqrt{ k^{2}-k })}{k + \sqrt{ k^{2}-k }} \\
&= \frac{k^{2} - (\sqrt{ k^{2}-k })^{2}}{k + \sqrt{ k^{2}-k }} \\
&= \frac{k}{k+\sqrt{ k^{2}-k }} \\
&= \frac{1}{1 + \sqrt{ 1-\frac{1}{k}}}.
\end{aligned}
$$


Entonces 


$$
x_{k} = \frac{1}{1+\sqrt{ 1-\frac{1}{k} }} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{2}.
$$



#### Ejemplo

Calcule $$\lim_{ n \to \infty } \ln(n^{2}-1) - \ln(n(n-1))$$.

Note que 


$$
\begin{aligned}
\ln(n^{2}-1) - \ln(n(n-1)) &= \ln\left(\frac{n^{2}-1}{n(n-1)}\right) \\
&= \ln\left( \frac{(n+1)(n-1)}{n(n-1)} \right) \\
&= \ln\left( \frac{n+1}{n} \right) \\
&= \ln\left( 1 + \frac{1}{n} \right) \underset{n \rightarrow \infty}{\longrightarrow} \ln(1) = 0.
\end{aligned}
$$



## Sucesiones recursivas

#### Ejemplo 

Sea $$\{a_{n}\}_{n=1}^\infty$$ tal que $$a_{0} = 1$$ y $$a_{n+1} = \sqrt{ 1+a_{n} }$$. Pruebe que converge y calcule su límite.

***Prueba:*** Primeramente, probaremos por inducción que $$\{a_{n}\}_{n=1}^\infty$$ es creciente, i.e., $$a_{n+1} \geq a_{n}$$ para todo $$n \in \mathbb{N}$$.
**Caso base:** Para $$n = 0$$, $$a_{1} = \sqrt{ 2 } \geq 1 = a_{0}$$. Esto prueba el caso base.
**Paso inductivo:** Suponga como hipótesis inductiva que $$a_{m+1} \geq a_{m}$$ para algún $$m \in \mathbb{N}$$ fijo y arbitrario. Hay que mostrar que $$a_{m+2} \geq a_{m+1}$$. A partir de la hipótesis inductiva: 


$$
\begin{aligned}
a_{m+1} &\geq a_{m} \\
1 + a_{m+1} &\geq 1+a_{m} \\
a_{m+2} = \sqrt{ 1 + a_{m+1} } &\geq \sqrt{ 1 + a_{m} } = a_{m+1}.
\end{aligned}
$$


Esto prueba el paso inductivo. Conclúyase que $$\{a_{n}\}_{n=1}^\infty$$ es creciente.
Probaremos ahora que es acotada superiormente. En particular, probaremos por inducción que para todo $$n \in \mathbb{N}$$, $$a_{n} \leq 2$$.
**Caso base:** Para $$n=0$$, $$a_{0} = 1 \leq 2$$. Esto prueba el caso base.
**Paso inductivo:** Suponga como hipótesis inductiva que $$a_{m} \leq 2$$ para algún $$m \in \mathbb{N}$$ fijo y arbitrario. Hay que mostrar que $$a_{m+1} \leq 2$$. A partir de la hipótesis inductiva: 


$$
\begin{aligned}
a_{m} &\leq 2 \\
1 + a_{m} &\leq 3\\
a_{m+1} = \sqrt{ 1 + a_{m} } &\leq \sqrt{3} < 2.
\end{aligned}
$$


Esto prueba el paso inductivo. Conclúyase que $$\{a_{n}\}_{n=1}^\infty$$ es acotada.
Luego, por teorema de convergencia monótona, conclúyase que $$\{a_{n}\}_{n=1}^\infty$$ converge. Sea $$L = \lim_{ n \to \infty } a_{n}$$. Entonces 


$$
\begin{aligned}
a_{n+1} &= \sqrt{ 1 + a_{n} } \\
\implies \lim_{ n \to \infty } a_{n+1} &=\lim_{ n \to \infty } \sqrt{1 + a_{n}} \\
\implies L &= \sqrt{ 1 + L } \\
\implies L^{2}-L-1 &= 0 \\
\implies L &= \frac{1+\sqrt{ 5 }}{2}.
\end{aligned}
$$


 
#### Ejemplo 

Sea $$x_{n} = \frac{x_{n-1}+1}{3} = \frac{x_{n-1}}{3} + \frac{1}{3}$$ para $$n \geq 1$$ y $$x_{0} = x$$. Note que 


$$
\begin{aligned}
x_{1} &= \frac{x}{3}+\frac{1}{3} \\
x_{2} &= \frac{ \frac{x+1}{3}}{3} + \frac{1}{3} = \frac{x}{3^{2}} + \frac{1}{3^{2}} +\frac{1}{3} \\
x_{3} &= \frac{x}{3^{3}} + \frac{1}{3^{3}} + \frac{1}{3^{2}} + \frac{1}{3}.
\end{aligned}
$$


En general, uno puede mostrar por inducción que 


$$
x_{n} = \frac{x}{3^{n}} + \frac{1}{3^{n}} + \frac{1}{3^{n-1}} + \dots + \frac{1}{3}.
$$


Ahora, si $$a \neq 1$$, $$1+a+a^{2}+\dots+a^{n} = \frac{1-a^{n+1}}{1-a}$$. Luego 


$$
x_{n} = \frac{x}{3^{n}} + \frac{ 1-\left( \frac{1}{3} \right)^{n+1} }{\frac{2}{3}} - 1 = \frac{x}{3^{n}} + \frac{3}{2}\left( 1-\left( \frac{1}{3} \right)^{n+1} \right) -1.
$$


Por lo tanto, $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} \frac{1}{2}$$. 
### Teorema (Convergencia de la permutación)
Sea $$\phi: \mathbb{N} \to\mathbb{N}$$ biyectiva y se $$\{a_{n}\}_{n=0}^\infty$$ tal que $$\sum_{n=0}^\infty \lvert a_{n} \rvert$$ converge. Entonces $$\sum_{n=0}^\infty a_{\phi(n)}$$ converge y además $$\sum_{n=0}^\infty a_{\phi_{n}} = \sum_{n=0}^\infty a_{n}$$. 
***Prueba:*** Defina 


$$
S_{k} = \sum_{n=0}^{k} a_{n}, \quad \tilde{S}_{k} = \sum_{n=0}^{k} \lvert a_{n} \rvert, \quad U_{k} = \sum_{n=0}^{k} a_{\phi(n)}.
$$


Sabemos que $$\sum_{n=0}^\infty \lvert a_{n} \rvert$$ converge. Luego, dado $$\varepsilon>0$$, existe $$N$$ tal que $$\lvert \tilde{S}_{n} - \tilde{S}_{m} \rvert < \varepsilon$$ para todos $$m\geq n\geq N$$. Entonces 


$$
\lvert a_{n+1} \rvert + \lvert a_{n+2} \rvert +\dots+ \lvert a_{m} \rvert < \varepsilon.
$$


Hay que mostrar que $$\lim_{ k \to \infty } S_{k} = \ell = \lim_{ k \to \infty } U_{k}$$. Tome $$N_{1}$$ tal que $$\lvert S_{k} - \ell \rvert < \varepsilon$$ si $$k \geq N_{1}$$. Como $$\phi$$ es biyectiva, sabemos que para todo $$m \in \mathbb{N}$$, existe $$n_{m}$$ tal que $$\phi(n_{m})$$. Tome $$M = \max \phi^{-1}[\{ 1,\dots,N \}]$$. Entonces $$\{ 1,\dots,N \} \subseteq \{ \phi(1),\dots,\phi(M) \}$$. Entonces, para $$m\geq M$$, $$k \geq N$$, tenemos que 


$$
\lvert U_{m} - S_{k} \rvert \leq  \lvert a_{N+1} \rvert +\dots+\lvert a_{\ell} \rvert < \varepsilon.
$$
{% endraw %}
