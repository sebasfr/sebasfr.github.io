---
layout: chapter
course: ma0350
chapter: 3
title: "Límite superior e inferior"
slug: 03-limite-superior-e-inferior
toc:
  sidebar: right
lang: es
fecha: 2020-03-25
---

{% raw %}
A continuación, se presenta el concepto de límite superior y límite inferior de sucesiones.

Considere $$x_{n} = (-1)^{n}$$. Note que $$x_{2n} = 1$$ y $$x_{2n+1} = -1$$. En partícular, 


$$
\begin{aligned}
\lim_{ n \to \infty } x_{2n} &=1, \\
\lim_{ n \to \infty } x_{2n+1} &= -1.
\end{aligned}
$$


Considere 


$$
\begin{aligned}
a_{n} &= \underset{m \in \mathbb{N}}{\inf}   \{ x_{m}:m\geq n \} \\
b_{n} &= \underset{m \in \mathbb{N}}{\sup} \{ x_{m}:m\geq n \}.
\end{aligned}
$$


Note que $$a_{n} \leq x_{n} \leq b_{n}$$. Además, para todo $$k \in \mathbb{N}$$, $$a_{n} \leq x_{n+k} \leq b_{n}$$.

## Límites superiores e inferiores

Sea $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$. Defina


$$
\begin{aligned}
a_{n} &= \underset{m \in \mathbb{N}}{\inf}   \{ x_{m}:m\geq n \} \\
b_{n} &= \underset{m \in \mathbb{N}}{\sup} \{ x_{m}:m\geq n \}.
\end{aligned}
$$


Note que $$a_{n} \leq x_{n+k} \leq b_{n}$$ para todo $$k \in \mathbb{N}$$. Además, note que 


$$
a_{n} = \inf \{ x_{m}: m\geq n \} \leq \inf \{ x_{m}:m\geq n+1 \} = a_{n+1},
$$




$$
b_{n+1} = \sup \{ x_{m}:m\geq n+1 \} \leq \sup \{ x_{m}:m\geq n \} = b_{n}.
$$


Asuma que la sucesión es acotada, es decir, que existen $$N,M \in \mathbb{R}$$ tales que $$N \leq x_{n} \leq M$$ para todo $$n \in \mathbb{N}$$. Entonces $$N \leq \inf \{ x_{m}:m\geq n \} = a_{n}$$ y $$b_{n} = \sup \{ x_{m}:m\geq n \} \leq M$$.

### Definición 

Sea $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$ acotada. Definimos 


$$
\begin{aligned}
\limsup x_{n} &= \lim_{ n \to \infty } b_{n} \\
\liminf x_{n} &= \lim_{ n \to \infty } a_{n}.
\end{aligned}
$$


Como $$b_{n+1}\leq b_{n}$$, note que, por teorema de convergencia monótona,


$$
\limsup x_{n} =\lim_{ n \to \infty } b_{n} = \underset{n}{\inf} b_{n} = \underset{n}{\inf} \underset{m}{\sup} \{ x_{m} : m\geq n\}.
$$


De la misma manera, 


$$
\liminf x_{n} = \lim_{ n \to \infty } a_{n} = \underset{n}{\sup} a_{n} = \underset{n}{\sup} \underset{m}{\inf} \{ x_{m}: m\geq n \}.
$$



### Lema (Acotación de límites de subsucesiones)

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión acotada. y $$\{x_{n}\}_{n=1}^\infty$$ una subsucesión $$\{x_{k_{n}}\}_{n=1}^\infty$$ que converge a $$L.$$Entonces $$\liminf x_{n} \leq L \leq \limsup x_{n}$$.

***Prueba:***  Considere $$\{x_{k_{n}}\}_{n=1}^\infty$$ una subsucesión. Note que $$x_{k_{n}} \leq b_{n}$$ pues $$k_{n} \geq n$$. De igual forma, $$a_{n} \leq x_{k_{n}}$$. Luego $$a_{n} \leq x_{k_{n}} \leq b_{n}$$. El resultado se sigue al tomar límites.

### Teorema (Convergencia y límites superior e inferior)

Sea $$\{x_{n}\}_{n=1}^\infty$$ una sucesión. Entonces $$\lim_{ n \to \infty } x_{n} = L$$ si y solo si  $$\limsup x_{n} = \liminf x_{n} = L$$.

***Prueba:*** ($$\implies$$): Sea $$\{x_{n}\}_{n=1}^\infty$$ tal que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}L$$. Entonces, $$\{x_{n}\}_{n=1}^\infty$$ es acotada. Luego, existen subsucesiones $$\{x_{k_{n}}\}_{n=1}^\infty$$ y $$\{x_{\ell_{n}}\}_{n=1}^\infty$$ tales que $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \liminf x_{n}$$ y $$x_{\ell_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \limsup x_{n}$$ (ejercicio). Conclúyase que $$\limsup x_{n} = \liminf x_{n} = L$$, pues toda subsucesión debe converger a $$L$$.
($$\impliedby$$): Sea $$\{x_{k_{n}}\}_{n=1}^\infty$$ una subsucesión fija y arbitraria. Sabemos que $$a_{n} \leq x_{k_{n}} \leq b_{n}$$. Entonces, por teorema del sandwich, conclúyase que $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Como toda subsucesión converge a $$L$$ (pues tomamos una fija y arbitraria), conclúyase que $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$.

Un truco muy común es usar las definiciones de $$\limsup$$ y $$\liminf$$, y notar que:



$$
\inf x_{n} \leq \\\liminf x_{n} \leq  \limsup x_{n} \leq \sup x_{n}.
$$


Si $$m$$ es cota inferior de $$x_{n}$$ para todo $$n\geq k$$ y $$M$$ es, cota superior de $$y_{n}$$ para todo $$n \geq k$$, por definición de $$\sup y_{n}$$ e $$\inf x_{n}$$, tenemos que $$m \leq \underset{n\geq k}{\inf} x_{n}$$ y que $$M \geq \underset{n\geq k}{\sup} y_{n}$$.
{% endraw %}
