#Mate #MA0350
Fecha: 2025-04-01

A continuación, se presentan algunos criterios de convergencia de [[Series numéricas]]. Ver también: [[Tópicos importantes y ejemplos]], [[Series de funciones]].
Sea $\{x_{n}\}_{n=0}^\infty$ una sucesion. Considere 
$$
S_{n} = \sum_{i=1}^{n}  x_{k} = x_{1} + x_{2} +\dots+x_{n}
$$
Decimos que $\sum_{k=0}^{\infty} x_{k}$ converge si $\lim_{ n \to \infty } S_{n}$ existe

### Condición de Cauchy

La serie $\sum_{n=1}^\infty x_{n}$ si y solo si  para todo $\varepsilon > 0$, existe $N \in \mathbb{N}$ tal que 
$$
\lvert S_{n} - S_{m} \rvert < \varepsilon \quad \text{para todos \quad$n,m \geq N$}  
$$
$$
\iff \lvert x_{n+1} + x_{n+2} + \dots + x_{m} \rvert < \varepsilon  \quad \text{si  \quad$m > n$}
$$
La serie converge si y solo si es de Cauchy.

#### Ejemplo 

Considere $x_{n} = \frac{1}{n}, n\geq 1$. Probaremos que $S_{2n} - S_{n} \geq \frac{1}{2}$.  Note que 
$$
\begin{aligned}
S_{2n} - S_{n} &= \left( 1+\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{2n} \right) -\left( 1+\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{n} \right) \\
&= \frac{1}{n+1} + \frac{1}{n+2} +\dots +\frac{1}{2n-1} + \frac{1}{2n} \\
&\geq \frac{1}{2n} + \frac{1}{2n} + \dots +\frac{1}{2n} + \frac{1}{2n} = \frac{n}{2n} = \frac{1}{2}.
\end{aligned}
$$
Luego, la condición de Cauchy se rompe para $\varepsilon < \frac{1}{2}$.

Considere el caso $x_{n} \geq 0$. Entonces 
$$
S_{n+1} = S_{n} + x_{n+1}\geq S_{n}
$$
$$
\implies S_{n+1} - S_{n} = x_{n+1}.
$$

### Lema (Acotación de sumas parciales):

Sea $\{x_{n}\}_{n=1}^\infty$ tal que $x_{n} \geq 0$ \. Entonces
1. $\sum_{n=0}^{\infty}x_{n}$  converge si existe $M$ tal que $\lvert S_{n} \rvert \leq M$ para todo $n$.
2. En caso contrario, las $S_{n}$ no son acotadas, i.e., $\lim_{ n \to \infty }S_{n} = \infty$.

### Criterio de las p-series

#### Ejemplo 

Considere
$$
\sum_{n=1}^{\infty} \frac{1}{n} = +\infty 
$$
***Prueba:*** Si $x_{n} \geq 0$, entonces los $S_{n}$ son crecientes. Luego, $S_{n}$ converge si y solo si es acotada. Tome $M > 0$, existe $N$ tal que $S_{N} > M$. Luego, para $n\geq N$, 
$$
S_{n} \geq S_{N} > M.
$$

#### Ejemplo 

Considere $x_{n} = \frac{1}{n^2}$, es decir,
$$
\sum_{n=1}^{\infty}  \frac{1}{n^2}.
$$
Sabemos que $\lim_{ n \to \infty }S_{n} = \infty$ o $\lim_{ n \to \infty } S_{n} = l \in \mathbb{R}$.
Note que:
$$
\begin{aligned}
S_{1} =& 1 \\
S_{2} =& 1 + \frac{1}{2^2} \\
S_{3} =& 1 + \frac{1}{2^2} + \frac{1}{3^2} \leq 1 + \frac{1}{2^2} + \frac{1}{2^2} = 1+\frac{1}{2} \\
S_{7} =& 1 + \frac{1}{2^2} + \frac{1}{3^2} + \dots + \frac{1}{7^2} \leq 1 + \frac{1}{2} + \frac{1}{4^{2}} + \frac{1}{4^{2}} + \frac{1}{4^{2}} + \frac{1}{4^{2}} \\
=&1 + \frac{1}{2} + \left( \frac{1}{2} \right)^2.
\end{aligned}
$$
Considere 
$$
S_{2^j -1} = S_{n_{j}}.
$$
Probaremos que $S_{n_{j}} \leq \sum_{n=0}^{j-1} \left( \frac{1}{2} \right)^n \quad \text{(*)}$.
El caso base ya lo hicimos. Para el paso inductivo, suponga que $\text{(*)}$ se cumple. Hay que mostrar que 
$$
S_{n_{j+1}} \leq \sum_{n=0}^{j+1} \left( \frac{1}{2} \right)^n.
$$
Note que 
$$
\begin{aligned}
S_{n_{j+1}} &= S_{n_{j}} + x_{2^j} + x_{2^{j}+1} + \dots + x_{2^{j+1}-1} \\
&\leq  \sum_{n=0}^{j} \left( \frac{1}{2} \right)^n + \frac{2^j}{(2^j)^{2}}  = \sum_{n=0}^{j-1} \left( \frac{1}{2} \right)^n + \left( \frac{1}{2} \right)^j = \sum_{n=1}^{j} \left( \frac{1}{2} \right)^n 
\end{aligned}
$$
Como 
$$
\sum_{n=0}^\infty \left( \frac{1}{2} \right)^n = \frac{1}{1-\frac{1}{2}}.
$$

entonces es acotada, luego $S_{2^{j+1} - 1} \leq M$, y por lo tanto converge. 

Sabemos que 
$$
\sum_{n=1}^\infty \frac{1}{n} = +\infty
$$
$$
\sum_{n=1}^\infty \frac{1}{n^{2}} \quad \text{converge}.
$$
Sea $0<p<1$. Entonces 
$$
n > n^p \implies \frac{1}{n^p} > \frac{1}{n} \implies \sum_{k=0}^\infty \frac{1}{k^p} > \sum_{k=0}^\infty \frac{1}{k} \rightarrow \infty
$$
Por lo tanto, diverge hacia infinito. Si $p>2$, entonces 
$$
\frac{1}{n^2} > \frac{1}{n^p},
$$
entonces $\sum_{n=1}^\infty \frac{1}{n ^p}$ converge. 

En general, si $p > 1$, la serie $\sum_{n=1}^\infty \frac{1}{n^p}$ converge.

### Ejercicio: 

Sea $x_{n} = \frac{1}{n^{p}}$, con $p > 1$. Muestre que 
$$
S_{2^j - 1} \leq \sum_{i=0}^{j-1} \frac{1}{2^{j-1}} 
$$

### Teorema (Comparación)

Sean $\{x_{n}\}_{n=0}^\infty$ y $\{z_{n}\}_{n=0}^\infty$ tales que $0\leq x_{n}\leq z_{n}$ para todo $n\geq 1$. Entonces
- Si $\sum_{n=1}^\infty z_{n}$ converge, entonces $\sum_{n=1}^\infty x_{n}$ converge.
- Si $\sum_{n=1}^\infty x_{n}$ diverge, entonces $\sum_{n=1}^\infty z_{n}$ diverge.

### Ejemplo 

Considere 
$$
x_{n} = \frac{1}{\sqrt{ n^{3}+1 }} \leq \frac{1}{\sqrt{ n^{3} }} = \frac{1}{n^\frac{3}{2}}
$$
Por lo tanto, $\sum_{n=0}^\infty x_{n}$ converge.

### Lema (Comparación al límite) 

Sean $\{x_{n}\}_{n=1}^\infty$ y $\{z_{n}\}_{n=1}^\infty$ sucesiones tales que $x_{n} \geq 0$ y $z_{n} \geq 0$. para $n\geq1$.
1. Si $\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = l \neq 0$, entonces ambas convergen o ambas divergen a infinito.
2. Si $\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = 0$, 
	 - entonces $\sum_{n=0}^\infty x_{n}= +\infty$ implica  $\sum_{n=0}^\infty z_{n}= +\infty$.
	 - entonces, si $\sum_{n=0}^\infty z_{n}$ converge entonces $\sum_{n=0}^\infty x_{n}$ converge
3. Si $\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = \infty$, 
	 - entonces $\sum_{n=0}^\infty z_{n}= +\infty$ implica  $\sum_{n=0}^\infty x_{n}= +\infty$.
	 - entonces, si $\sum_{n=0}^\infty x_{n}$ converge entonces $\sum_{n=0}^\infty z_{n}$ converge

***Prueba de (a):*** Asuma que 
$$
\lim_{ n \to \infty } \frac{x_{n}}{z_{n}} = l > 0.
$$
Dado $\varepsilon > 0$, existe $N \in \mathbb{N}$ tal que para todo $n \geq N$ 
$$
l - \varepsilon < \frac{x_{n}}{z_{n}} < l + \varepsilon \implies (l-\varepsilon) z_{n} < x_{n} < (l+\varepsilon) z_{n}. 
$$
Tomando $\varepsilon$ tal que $0<\varepsilon< \frac{l}{2}$, entonces $0 \leq (l-\varepsilon) z_{n} < x_{n}$.
Note que 
$$
0 \leq (l - \varepsilon) \sum_{k=1}^\infty z_{k} \leq \sum_{k=1}^\infty x_{k} \leq (l+\varepsilon) \sum_{n=0}^\infty z_{n}
$$
Si $\sum_{k=0}^\infty x_{k}$ converge, por comparación $\sum_{k=0}^\infty z_{k}$  

### Ejemplo 

$\sum_{n=0}^\infty \frac{1}{n^{5}-n^{3}+1}$ se comporta como $\sum_{n=1}^\infty \frac{1}{n^{5}}$ pues 
$$
\lim_{ n \to \infty } \frac{\left( \frac{1}{n^{5}-n^{3}+1} \right)}{\left( \frac{1}{n^{5}} \right)} = \lim_{ n \to \infty } \frac{n^{5}}{n^{5}-n^{3}+1} = 1
$$

### Ejemplo 

$\sum_{n=0}^\infty \frac{2^{3n}+n^{5}}{10^{n}}$ se comporta como $\sum_{n=1}^\infty \left( \frac{8}{10} \right)^{n}$ pues 
$$
\lim_{ n \to \infty } \frac{\frac{2^{3n}+n^{5}}{10^{n}}}{\left( \frac{8}{10} \right)^{n}} = 1
$$

### Lema (Criterio de la raiz)

Sea $\{x_{n}\}_{n=1}^\infty$ una sucesión. Considere 
$$
\lim_{ n \to \infty } \sqrt[n]{ \lvert x_{n} \rvert  }.
$$
- Si $\lim_{ n \to \infty }  \sqrt[n]{ \lvert x_{n} \rvert  } = l < 1$, entonces $\sum_{n=0}^\infty \lvert x_{n} \rvert$ converge.
***Prueba:*** Sea $\varepsilon > 0$ tal que $0 < l+\varepsilon < 1$. Entonces existe $N \in \mathbb{N}$ tal que para todo $n \geq \mathbb{N}$ 
$$
l-\varepsilon <  \sqrt[n]{ \lvert x_{n} \rvert  } < l + \varepsilon \implies \lvert x_{n} \rvert <(l+\varepsilon)^n
$$
para $n \geq N$. Luego, la serie converge por comparación. 

- Si $\lim_{ n \to \infty }  \sqrt[n]{ \lvert x_{n} \rvert  } = l > 1$, entonces $\sum_{n=0}^\infty \lvert x_{n} \rvert +\infty.$

### Ejemplo

Para $a>0$ sea $x_{n}=\frac{a^{n}}{n^{n}}$, con $n\geq{1}$. Entonces, 
$$
\lim_{ n \to \infty } \sqrt[n]{\frac{a^{n}}{n^{n}}} = \frac{a}{n} = 0.
$$
Por lo tanto, $\sum_{n=1}^\infty \frac{a^{n}}{n^{n}}$ converge.

### Lema (Criterio del cociente)

Sea $\{x_{n}\}_{n=1}^\infty$ una sucesión. Considere 
$$
\lim_{ n \to \infty } \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert}
$$
Si $\lim_{ n \to \infty }   \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert} = l < 1$, entonces $\sum_{n=0}^\infty \lvert x_{n} \rvert$ converge.

Si $\lim_{ n \to \infty } \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert} = l >1$, entonces $\sum_{n=0}^\infty \lvert x_{n} \rvert = +\infty$ .
***Prueba:*** Sea $\varepsilon > 0$ tal que $l-\varepsilon > 1$. Entonces existe $N \in \mathbb{N}$ tal que para todo $n \geq \mathbb{N}$ 
$$
l-\varepsilon <  \frac{\lvert x_{n+1} \rvert}{\lvert x_{n} \rvert}  \implies (l-\varepsilon) \lvert x_{n} \rvert < \lvert x_{n+1} \rvert 
$$
Luego, iterando 
$$
\lvert x_{N+k} \rvert \geq (l-\varepsilon)^k \lvert x_{N} \rvert 
$$
Como $(l-\varepsilon) > 1$, $\sum_{k=1}^\infty(l-\varepsilon)^k = +\infty$. Luego por comparación, $\sum_{n=0}^\infty \lvert x_{n} \rvert = +\infty$.

### Ejemplo 

Considere $x_{n} = \frac{a^n}{n!}$ con $a>0$. Note que 
$$
\lim_{ n \to \infty } \left\lvert  \frac{a_{n+1}}{a_{n}}  \right\rvert = \lim_{ n \to \infty } \frac{a}{n+1} = 0.
$$
Luego, $\sum_{n=0}^\infty x_{n}$ converge.


### Teorema (Convergencia absoluta):

Sea $\{x_{n}\}_{n=1}^\infty$ una sucesión. Si $\sum_{n=1}^\infty \lvert x_{n} \rvert$ converge, entonces $\sum_{n=1}^\infty x_{n}$ converge.
***Prueba:*** Sea $\{x_{n}\}_{n=1}^\infty$ una sucesión. Entonces 
$$
\lvert x_{n} \rvert - x_{n} \leq 2 \lvert x_{n} \rvert
$$
para todo $n \geq 1$. Asuma que $\sum_{n=0}^\infty \lvert x_{n} \rvert$ converge a L. Entonces, 
$$
\sum_{n=0}^\infty 2 \lvert x_{n} \rvert = 2L.
$$
Concluimos entonces que $\sum_{n=0}^\infty \lvert x_{n} \rvert - x_{n}$ converge.
Sean
$$
S_{n} = \sum_{k=0}^n \lvert x_{k} \rvert - x_{k},
$$

$$
\hat{S}_{n} = \sum_{k=0}^{n} \lvert x_{k} \rvert  
$$
Entonces $\hat{S}_{n} - S_{n} = \sum_{k=0}^{n} x_{k}$. Por lo tanto, $\sum_{n=0}^\infty x_{n}$ converge.

### Teorema (Convergencia del producto de series) 

Considere $\{x_{n}\}_{n=0}^\infty$ y $\{y_{n}\}_{n=0}^\infty$ dos sucesiones. Si
1. $\lvert y_{k} \rvert \leq M$ para $k \geq 1$.
2. $\sum_{k=1}^\infty \lvert x_{k} \rvert$ converge,
entonces $\sum_{k=1}^\infty \lvert x_{k} y _{k} \rvert$ converge.

***Prueba:*** Considere $\{x_{n}\}_{n=1}^\infty$ y $\{y_{n}\}_{n=1}^\infty$ dos sucesiones. Queremos estudiar la convergencia de $\sum_{n=1}^\infty x_{n} y_{n}$. Asuma que $\lvert y_{k} \rvert \leq M$ para $k \geq 1$ y $\sum_{k=1}^\infty \lvert x_{k} \rvert$ converge. Note que 
$$
\sum_{k=1}^\infty \lvert x_{k}y_{k} \rvert \leq \sum_{k=1}^\infty M \lvert x_{k} \rvert = M \sum_{k=1}^\infty \lvert x_{k} \rvert 
$$
Conclúyase que $\sum_{k=1}^\infty \lvert x_{k}y_{k} \rvert$ converge, luego $\sum_{k=1}^\infty x_{k} y_{k}$ converge.

### Ejemplo

$x_{k} = \frac{\sin k}{k^2}$. Note que $\lvert \sin k \rvert \leq 1$ y $\sum_{k=1}^\infty \frac{1}{k^{2}}$ converge

**Truco más general**: Considere $\sum_{k=1}^{n} x_{k} y_{k}$. Tome $S_{k} = \sum_{k=1}^{n} y_{n}$. Entonces $y_{k} = S_{k} - S_{k-1}$. Desarrollando:
$$
\sum_{k=1}^{n} x_{k} y_{k} =  \sum_{k=1}^{n} x_{k} (S_{k} - S_{k-1}) = \sum_{k=1}^{n} x_{k} S_{k} - \sum_{k=0}^{n} x_{k+1} S_{k} = \sum_{k=1}^{n-1} S_{k}(x_{k} - x_{k+1}) + x_{n} S_{n} - x_{1}S_{0}.
$$
De hecho, para $m \leq n$, tenemos que
$$
\sum_{k=m}^{n} x_{k}y_{k} = \sum_{k=m}^{n} (x_{k}-x_{k+1}) S_{k} + x_{n}S_{n} - x_{m}S_{m-1}.
$$


### Teorema (Criterio de Dirichlet)

Sean $\{x_{n}\}_{n=1}^\infty$ y $\{y_{n}\}_{n=1}^\infty$ tales que 
1. $x_{n} \geq x_{n+1}$ para todo $n \in \mathbb{N}$,
2. $\lim_{ n \to \infty } x_{n} = 0$,
3. existe $M \in \mathbb{R}$ tal que para todo $n \in \mathbb{N}$, $\lvert  \sum_{k=1}^n y_{k} \rvert \leq M$ para todo $n  \in \mathbb{N}$.
Entonces, $\sum_{n=1}^\infty x_{n}y_{n}$ converge.
***Prueba:*** Sea $k \leq l$, entonces 
$$
\begin{aligned}
\left\lvert  \sum_{n=k}^{l} x_{n}y_{n}   \right\rvert &\leq  \sum_{n=k}^{l-1} \lvert x_{n}-x_{n+1} \rvert \lvert S_{n} \rvert +\lvert x_{l} \rvert \lvert S_{l} \rvert + \lvert x_{k} \rvert \lvert S_{k-1} \rvert \\
&\leq \sum_{n=k}^{l-1} (x_{n}-x_{n+1}) M + \lvert x_{l} \rvert M + \lvert x_{k} \rvert M \\
&=M(x_{k}-x_{l}) + Mx_{l} + Mx_{k} = 2Mx_{k}
\end{aligned}
$$
pues $x_{n}\geq_{0}$. Además, como $\lim_{ n \to \infty } x_{n} = 0$, entonces existe $N \in \mathbb{N}$ tal que $\lvert x_{k} \rvert < \frac{\varepsilon}{2M}$ si $k \geq N$, para un $\varepsilon > 0$ fijo y arbitrario. Luego, si $l \geq l \geq N$, tenemos que 
$$
\left\lvert  \sum_{n=k}^{l}  x_{n} y_{n} \right\rvert  < \varepsilon.
$$
Por tanto, la serie es de Cauchy y converge.

#### Ejemplo 

Considere $\sum_{n=1}^\infty \frac{(-1)^{n}}{n}$. Tome $x_{n} = \frac{1}{n}$, $y_{n} = (-1)^{n}$. A Entonces 
$$
S_{n} = \sum_{k=1}^{n} y_{k},\quad \text{En particular, }S_{1} =-1, S_{2} = 0 , S_{3} = -1,\dots
$$
Luego $S_{n}$ es acotada. Por tanto, $\sum_{n=1}^\infty \frac{(-1)^{n}}{n}$ converge. 

### Lema (Convergencia alternante)  

Sea $\{x_{n}\}_{n=1}^\infty$ tal que $\lim_{ n \to \infty } x_{n} = 0$ y $x_{n+1} \leq x_{n}$ para todo $n\geq1$. Entonces $\sum_{n=1}^{\infty} (-1)^{n} x_{n}$ converge.

### Ejemplo 
$x_{n} = \frac{1}{\sqrt{ n }}$, $x_{n}=\frac{1}{\ln(n+1)}$.

Considere $y_{n} = \cos(nx)$, con $x \in [0,2\pi)$. Queremos acotar $\sum_{k=1}^\infty \cos(nx)$ para $x \neq 0$ y $x \neq \pi$. Note que 
$$
\begin{aligned}
\sin\left( \left( k-\frac{1}{2} \right)x \right) - \sin\left( \left( k+\frac{1}{2} \right)x \right) &= 2 \cos(kx) \sin\left( \frac{x}{2} \right) \\
\iff \cos(kx) &= \frac{1}{2\sin\left( \frac{x}{2} \right)}\left[ \sin\left( \left( k+\frac{1}{2} x \right) \right) - \sin\left( \left( k-\frac{1}{2} \right) x \right) \right]
\end{aligned}
$$
Entonces,
$$
\begin{aligned}
\left\lvert  \sum_{k=1}^{n} \cos(kx)  \right\rvert &= \frac{1}{\left\lvert  2 \sin\left( \frac{x}{2} \right)  \right\rvert } \left\lvert  \sum_{k=1}^{n} \left[ \sin\left( \left( k+\frac{1}{2} \right) x \right) - \sin\left( \left( k-\frac{1}{2} \right) x \right)\right]  \right\rvert \\
&=\frac{1}{\left\lvert  2 \sin\left( \frac{x}{2} \right)  \right\rvert } \underbrace{ \left\lvert  \sin\left( \left( n+\frac{1}{2} \right)x \right) -\sin\left( \frac{1}{2} x \right) \right\rvert }_{ \leq 2 \text{ pues }-1 \leq \sin(x) \leq 1 } \\
&\leq \frac{1}{\lvert \sin\left( \frac{x}{2} \right) \rvert }.
\end{aligned}
$$

### Teorema (Criterio de Abel)

Sean $\{x_{n}\}_{n=1}^\infty$ y $\{y_{n}\}_{n=1}^\infty$ sucesiones tales que
1. $\{x_{n}\}_{n=1}^\infty$ es monótona y convergente.
2. $\sum_{n=1}^\infty y_{n}$ converge.
Entonces $\sum_{n=1}^\infty x_{n} y_{n}$ converge.

***Prueba:*** Considere los siguientes casos:

**Caso 1:** Los $x_{n}$ son decrecientes. Sea $L = \lim_{ n \to \infty } x_{n}$. Defina $z_{n} = x_{n} - L$. Entonces, $z_{n}$ es decreciente y $\lim_{ n \to \infty }z_{n} = 0$. Por tanto, $\sum_{n=1}^\infty y_{n} z_{n}$ converge. Note que 
$$
\sum_{n=1}^{m} y_{n} z_{n} + \underbrace{ \sum_{n=1}^{m} y_{n} L }_{\text{convergente} } = \sum_{n=1}^{m} y_{n} x_{n}.
$$
Conclúyase que $\sum_{n=1}^\infty x_{n} y_{n}$ converge.

**Caso 2:** Los $x_{n}$ son crecientes. Sea $L = \lim_{ n \to \infty } x_{n}$. Defina $z_{n} = L -x_{n}$. Entonces, $z_{n}$ es decreciente y $\lim_{ n \to \infty }z_{n} = 0$. Por tanto, $\sum_{n=1}^\infty y_{n} z_{n}$ converge. Note que 
$$
- \sum_{n=1}^{m} y_{n} z_{n} + \underbrace{ \sum_{n=1}^{m} y_{n} L }_{\text{convergente} }  = \sum_{n=1}^{m} y_{n} x_{n}.
$$
Conclúyase que $\sum_{n=1}^\infty x_{n} y_{n}$ converge. 
 
#### Ejemplo 

$$
\sum_{n=2}^\infty \frac{1}{n^{2}} \ln\left( 1-\frac{1}{n} \right)
$$
Tome $y_{n} = \frac{1}{n^{2}}$ y $x_{n} = \ln\left( 1-\frac{1}{n} \right)$. Sabemos que $\sum_{n=2}^\infty \frac{1}{n^{2}}$ converge. Además 
$$
\lim_{ n \to \infty } x_{n} = \ln(1) = 0.
$$
Como $1-\frac{1}{n}$ es creciente, $x_{n}$ es creciente. Conclúyase por Abel que la serie converge. 
 
#### Ejemplo 

Considere $\sum_{n=1}^\infty (-1)^{n} \frac{\ln(n)}{n}$. Note que $\left( \frac{\ln(n)}{n} \right)' =\frac{1-\ln(x)}{x^{2}} \leq 0$ si $x \geq e$. Entonces $\frac{\ln(n)}{n}$ es decreciente para $n \geq 3$ (solo necesitamos que sea eventualmente decreciente). Por lo tanto, $\sum_{n=2}^\infty (-1)^{n} \frac{\ln(n)}{n}$ converge. 

### Teorema (Criterio de Raabe)

Sean $\{x_{n}\}_{n=1}^\infty$ una sucesión tal que $x_{n}\neq_{0}$ para todo $n \in \mathbb{N}$. Considere 
$$
\lim_{ n \to \infty } n\left( 1 - \frac{\lvert x_{n+1}\rvert}{\lvert x_{n} \rvert } \right) = L.
$$
Entonces 
1. $\sum_{n=1}^{\infty} \lvert x_{n} \rvert$ converge si $L >1$.
2. $\sum_{n=1}^\infty \lvert x_{n} \rvert$ diverge si $L < 1$.

***Prueba:*** Dado $\varepsilon > 0$, existe $N \in \mathbb{N}$ tal que 
$$
L - \varepsilon \leq n\left( 1 - \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert \right) \leq L +\varepsilon 
$$
para $n \geq N$.
Asuma $L > 1$. Tome $\varepsilon>0$ tal que $L -\varepsilon > 1$. Ahora 
$$
\begin{aligned}
\frac{L-\varepsilon}{n} &\leq 1 - \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert \\
\iff \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert &\leq 1 - \frac{l-\varepsilon}{n} \\
\iff n \left\lvert  \frac{x_{n+1}}{x_{n}}  \right\rvert  &\leq  n - (l -\varepsilon) \\
\iff n \lvert x_{n+1} \rvert &\leq n \lvert x_{n} \rvert -(l-\varepsilon) \lvert x_{n} \rvert \\
\iff n \lvert x_{n+1} \rvert &\leq (n-1) \lvert x_{n} \rvert -(L - \varepsilon - 1) \lvert  x_{n} \rvert 
\end{aligned}
$$
Entonces, para $n\geq2$,
$$
0 \leq (l-\varepsilon - 1) \lvert x_{n} \rvert \leq  (n-1) \lvert x_{n} \rvert  - n \lvert x_{n+1} \rvert. 
$$
Luego, si $S =\sum_{n=1}^\infty (n-1) \lvert x_{n} \rvert - n \lvert x_{n+1} \rvert$ converge entonces $\sum_{n=1}^\infty\lvert x_{n} \rvert$ converge. Ahora, $\sum_{n=1}^{k} (n-1) \lvert x_{k} \rvert - n \lvert x_{n+1} \rvert = -k \lvert x_{k+1} \rvert$. Entonces, S converge si $\lim_{ n \to \infty } k \lvert x_{k+1} \rvert$ existe.
Pero $(n-1) \lvert x_{n} \rvert  - n \lvert x_{n+1} \rvert$, i.e., la sucesión es decreciente y acotada inferiormente (pues es positiva). Por lo tanto, conclúyase que $\sum_{n=1}^\infty \lvert x_{n} \rvert$ converge.

#### Ejemplo 

Considere $x_{n} = \frac{1\cdot 3 \cdot 5 \cdot \dots (2n+1)}{2 \cdot 4 \cdot 6 \cdot... \cdot (2n+2)}$. Note que 
$$
\frac{x_{n+1}}{x_{n}} = \frac{\frac{1\cdot 3 \cdot 5 \cdot \dots (2n+3)}{2 \cdot 4 \cdot 6 \cdot... \cdot (2n+2)}}{ \frac{1\cdot 3 \cdot 5 \cdot \dots (2n+4)}{2 \cdot 4 \cdot 6 \cdot... \cdot (2n+2)}} = \frac{2n+3}{2n+4}  \underset{n\rightarrow \infty}{\longrightarrow} 1.
$$
Aplicando el criterio de Raabe:

$$
n\left( 1-\frac{x_{n+1}}{x_{n}} \right) = n\left( 1 - \frac{2n+3}{2n+4} \right) = n\left( \frac{1}{2n+4} \right) \underset{n \rightarrow  \infty}{\longrightarrow} \frac{1}{2}.
$$
Por lo tanto, diverge. 
 
### Teorema (Condensación de Cauchy)

Sea $\{a_{n}\}_{n=1}^\infty$ decreciente y positiva. Entonces $\sum_{n=1}^\infty a_{n}$ converge si y solo si $\sum_{n=1}^\infty 2^{n} a_{2^{n}}$ converge

***Prueba:*** Sea $\{a_{n}\}_{n=1}^\infty$ una sucesión decreciente y positiva. Note que 
$$
\begin{aligned}
2a_{2} &\leq a_{1}+a_{2} &&\leq 2a_{1} \\
2a_{4} &\leq a_{3}+a_{4} &&\leq 2a_{3} \\
2^{2} a_{8} &\leq a_{5}+a_{6}+a_{7}+a_{8} &&\leq 2^{2} a_{5} \\
2^{3} a_{16} &\leq a_{9} + a_{10} + \dots + a_{16} &&\leq 2^{3}a_{9} \\
&   \vdots && \\\
2^{n-1} a_{2^{n}} &\leq a_{2^{n-1}+1}  + \dots + a_{2^{n}} &&\leq  2^{n-1} a_{2^{n-1}+1}.
\end{aligned}
$$
Queremos que $S_{n} = \sum_{k=1}^{n} a_{k}$ converge si $\{a_{k}\}_{k=1}^\infty$ es decreciente y positiva. Como $S_{n}$ es creciente, pues $\{a_{k}\}_{k=1}^\infty$ es positiva, entonces hay 2 posibilidades:
1. $S_{n}$ converge si es acotada.
2. $\lim_{ n \to \infty } S_{n} = +\infty$ si no lo es.

Considere $S_{2^{n}} = a_{1} + a_{2} + a_{4} + \dots + a_{2^{n}}$. Sabemos que al ser creciente, $S_{n}$ converge si y solo si $S_{2^{n}}$ converge. Ahora, note que 
$$
\begin{aligned}
S_{2^{n}} &= a_{1}+a_{2}+\dots+a_{2^{n}} \\
&= (a_{1}+a_{2}) + (a_{3} + a_{4}) + (a_{3} + \dots+a_{8}) + \dots+(a_{2^{n-1}+1} + \dots + a_{2^{n}}),
\end{aligned}
$$
que por el desarrollo anterior, tenemos que 
$$
\begin{aligned}
2a_{2} + 2a_{4}+2^{2} a_{8} + \dots +2^{n-1} a_{2^{n}} &= \frac{1}{2} \sum_{k=2}^{n} 2^{k} a_{2^{k}} + 2a_{2} \\
&\leq S_{2^{n}} \\
& \leq 2a_{1} + 2a_{3} + 2^{2} a_{5} + \dots +2^{n-1} a_{2^{n-1}+ 1} \\
&\leq 2a_{1} + 2a_{2} + 2^{2} a_{4} + \dots + 2^{n-1} a_{2^{n-1}} \\
&= 2a_{1} + \sum_{k=1}^{n-1} 2^{k} a_{2^{k}}.
\end{aligned}
$$

Este criterio es útil para tratar con logarítmos dentro de las series.

#### Ejemplo 

Considere $\sum_{n=2}^\infty \frac{1}{n(\ln n)^{2}}$. Tome $\sum_{n=2}^\infty 2^{n} \left(\frac{1}{2^{n}} \frac{1}{(\ln2^{n})^{2}} \right) = \sum_{n=1}^\infty \frac{1}{(n\ln 2)^{2}} = \frac{1}{(\ln 2)^{2}} \sum_{n=2}^\infty \frac{1}{n^{2}}$, que converge por p-series.

### Teorema (Convergencia absoluta y permutaciones)

Sea $\{a_{n}\}_{n=1}^\infty$ tal que $\sum_{n=0}^\infty \lvert a_{n} \rvert$ converge y sea $\phi: \mathbb{N} \to \mathbb{N}$. Entonces $\sum_{n=0}^\infty a_{\phi(n)}$ converge y además $\sum_{n=0}^\infty a_{\phi(n)} = \sum_{n=0}^\infty a_{n}$.

 ***Prueba:***  Defina $S_{k} =\sum_{n=0}^{k} a_{n}$ , $\tilde{S_{k}} = \sum_{n=0}^{k} \lvert a_{n} \rvert$ y $u_{k} = \sum_{n=0}^{k}. a_{\phi(n)}$. Sabemos que $\sum_{n=0}^\infty \lvert a_{n} \rvert$ converge, i.e., al ser de Cauchy tenemos que, dado $\varepsilon > 0$ existe $N \in \mathbb{N}$ tal que para todos $n,m\geq N$ 
$$
\lvert \tilde{S_{n}} - \tilde{S_{m}} \rvert  < \varepsilon.
$$
Entonces, $\lvert a_{n+1} \rvert + \lvert a_{n+2} \rvert + \dots + \lvert a_{m} \rvert < \varepsilon$
Sea $\ell = \lim_{ n \to \infty } S_{n}$. 
Ahora, tome $N_{1}$ tal que $\lvert S_{k} - \ell \rvert < \varepsilon$ COMPLETAR.
### Ejemplo completo 1

Considere la serie $\sum_{n=1}^\infty \frac{1}{\sqrt{ n(n+1) }}$. Note que $\frac{1}{\sqrt{ n(n+1) }} \approx \frac{1}{\sqrt{ n \cdot n }} = \frac{1}{n}$. Como 
$$
\lim_{ n \to \infty } \frac{\frac{1}{\sqrt{ n(n+1) }}}{\frac{1}{n}} = 1
$$
y $\sum_{n=1}^\infty \frac{1}{n}$ diverge, entonces la serie dada diverge. 
 

### Ejemplo completo 2

Considere la serie $\sum_{n=1}^\infty \sin\left( \frac{1}{n^{p}} \right)$ para $p>1$. Note que $0 \leq \sin(x) \leq x$ para todo $x\geq 0$. Como $0 \leq \frac{1}{n^{p}}$, tenemos que $0\leq \sin\left( \frac{1}{n^{p}} \right) \leq \frac{1}{n^{p}}$. Por tanto la serie converge por comparación. 
 

### Ejemplo completo 3
 
Considere la serie $\sum_{n=1}^{\infty} \frac{n^{n}}{(n+1)^{n+1}}$. Note que 

$$
\frac{n^{n}}{(n+1)^{n+1}} = \frac{1}{n+1} \frac{1}{\left( 1+\frac{1}{n} \right)^{n}} \approx \frac{1}{n+1}
$$
Ahora, $\lim_{ n \to \infty } (1+\frac{1}{n})^{n} = e$. Luego,  
$$
\lim_{ n \to \infty } \frac{\frac{n^{n}}{(n+1)^{n+1}}}{\frac{1}{n+1}} = e
$$

por lo que la serie dada diverge. 
 

### Ejemplo completo 4

Considere la serie $\sum_{n=1}^\infty \frac{\sqrt{ n } - \sqrt{ n+1 }}{\sqrt{ n(n+1) }} = \sum_{n=1}^\infty \frac{1}{\sqrt{ n+1 }} - \frac{1}{\sqrt{ n }}$. Esta serie converge pues es telescópica y $\lim_{ n \to \infty } \frac{1}{\sqrt{ n }} = 0$. En particular, la serie converge a $-1$. 
 

### Ejemplo completo 5

Calcule el siguiente límite: 
$$
\lim_{ n \to \infty } n\left( 1-\left( 1-\frac{1}{2n} \right)^{p} \right).
$$


