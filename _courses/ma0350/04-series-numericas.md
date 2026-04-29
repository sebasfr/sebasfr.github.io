---
layout: chapter
course: ma0350
chapter: 4
title: "Series numéricas"
slug: 04-series-numericas
toc:
  sidebar: right
lang: es
fecha: 2025-03-25
---

{% raw %}
En esta nota, definimos las series a partir de sumas parciales de Sucesiones. Ver también: Criterios de convergencia de series, Series de funciones.

Considere la sucesión $$\{x_{n}\}_{n=0}^\infty$$, donde $$x_{n} = a^{n}$$. Considere la siguiente sucesión:


$$
\begin{aligned}
S_{0} &= 1 \\
S_{1} &= 1+a \\
S_{2} &= 1+a+a^{2} \\
 &  \quad  \quad \vdots \\
S_{n} &= 1+a+\dots+a^{n}.\\
&= \frac{1-a^{n+1}}{1-a} \quad\text{para $a \neq 1$.}
\end{aligned}
$$



Entonces, si $$\lvert a \rvert < 1$$, tenemos que $$\lim_{ n \to \infty } S_{n} = \frac{1}{1-a}$$. Por lo tanto, $$\sum_{n=0}^\infty a^{n} = \frac{1}{1-a}$$ para $$a \in (-1,1)$$. 

## Series numéricas y convergencia
### Definición (Sumas parciales)

Dada una sucesión $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$, definimos la sucesión de sumas parciales $$\{S_{n}\}_{n=0}^\infty$$ de la siguiente manera 


$$
\begin{aligned}
S_{0} &= a_{0} \\
S_{1} &= a_{0}+a_{1} \\
S_{2} &= a_{0}+a_{1}+a_{2} \\
 &  \quad  \quad \vdots \\
S_{n} &= a_{0}+a_{1}+\dots+a_{n}.\\
&= \sum_{k=1}^{n} a_{k}
\end{aligned}
$$




### Definición (Convergencia de series)

Dada $$\{x_{n}\}_{n=0}^\infty$$ una sucesión, decimos que la serie $$\sum_{n=0}^\infty x_{n}$$ converge si $$\lim_{ n \to \infty } S_{n} = \lim_{ n \to \infty } \sum_{k=0}^{n} x_{n} = L \in \mathbb{R}$$ existe, en cuyo caso, decimos que $$\sum_{n=0}^\infty x_{n} = L$$. 
 
### Ejemplo 1: Serie geométrica

Tal y como vimos al inicio, si $$x_{n} = a^{n}$$, entonces $$S_{n} = \frac{1-a^{n+1}}{1-a}$$. La serie converge a $$\frac{1}{1-a}$$ si y solo si $$\lvert a \rvert < 1$$.

### Ejemplo 2: Series telescópicas

Dada $$\{a_{n}\}_{n=0}^\infty$$, defina $$x_{0} := a_{0}$$ y $$x_{n+1} := a_{n+1}-a_{n}$$, para $$n \geq 1$$. Entonces


$$
\begin{aligned}
S_{n} &= x_{0}+x_{1}+\dots x_{n} \\
&= a_{0}+(a_{1}-a_{0}) + (a_{2}-a_{1}) + \dots + (a_{n}-a_{n-1}) \\
&= a_{n}.
\end{aligned}
$$


Note que $$\sum_{n=0}^\infty x_{n} = \lim_{ n \to \infty } S_{n} = \lim_{ n \to \infty } a_{n}$$. La serie converge si y solo si $$\{a_{n}\}_{n=0}^\infty$$ converge, en cuyo caso convergen al mismo valor.

En general, es difícil calcular el valor de convergencia de una serie que no es geométrica o telescópica. No obstante, existen algunos criterios que permiten determinar si la serie converge o no sin conocer necesariamente el valor de convergencia. En general, si $$\{a_{n}\}_{n=1}^\infty$$ es una sucesión, entonces 


$$
\sum_{n=k}^\infty (a_{n}-a_{n+1}) = a_{k} - \lim_{ n \to \infty } a_{n+1}.
$$


La serie converge si la sucesión converge.
{% endraw %}
