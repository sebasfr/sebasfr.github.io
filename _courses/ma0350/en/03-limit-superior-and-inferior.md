---
layout: chapter
course: ma0350
chapter: 3
title: "Limit Superior and Limit Inferior"
slug: 03-limit-superior-and-inferior
toc:
  sidebar: right
lang: en
fecha: 2020-03-25
permalink: /notes/ma0350/03-limit-superior-and-inferior/
---

{% raw %}
What follows introduces the concept of the limit superior and the limit inferior of sequences.

Consider $$x_{n} = (-1)^{n}$$. Note that $$x_{2n} = 1$$ and $$x_{2n+1} = -1$$. In particular, 


$$
\begin{aligned}
\lim_{ n \to \infty } x_{2n} &=1, \\
\lim_{ n \to \infty } x_{2n+1} &= -1.
\end{aligned}
$$


Consider 


$$
\begin{aligned}
a_{n} &= \underset{m \in \mathbb{N}}{\inf}   \{ x_{m}:m\geq n \} \\
b_{n} &= \underset{m \in \mathbb{N}}{\sup} \{ x_{m}:m\geq n \}.
\end{aligned}
$$


Note that $$a_{n} \leq x_{n} \leq b_{n}$$. Moreover, for every $$k \in \mathbb{N}$$, $$a_{n} \leq x_{n+k} \leq b_{n}$$.

## Limits superior and inferior

Let $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$. Define


$$
\begin{aligned}
a_{n} &= \underset{m \in \mathbb{N}}{\inf}   \{ x_{m}:m\geq n \} \\
b_{n} &= \underset{m \in \mathbb{N}}{\sup} \{ x_{m}:m\geq n \}.
\end{aligned}
$$


Note that $$a_{n} \leq x_{n+k} \leq b_{n}$$ for every $$k \in \mathbb{N}$$. Moreover, note that 


$$
a_{n} = \inf \{ x_{m}: m\geq n \} \leq \inf \{ x_{m}:m\geq n+1 \} = a_{n+1},
$$




$$
b_{n+1} = \sup \{ x_{m}:m\geq n+1 \} \leq \sup \{ x_{m}:m\geq n \} = b_{n}.
$$


Assume that the sequence is bounded, that is, that there exist $$N,M \in \mathbb{R}$$ such that $$N \leq x_{n} \leq M$$ for every $$n \in \mathbb{N}$$. Then $$N \leq \inf \{ x_{m}:m\geq n \} = a_{n}$$ and $$b_{n} = \sup \{ x_{m}:m\geq n \} \leq M$$.

### Definition 

Let $$\{x_{n}\}_{n=1}^\infty \subseteq \mathbb{R}$$ be bounded. We define 


$$
\begin{aligned}
\limsup x_{n} &= \lim_{ n \to \infty } b_{n} \\
\liminf x_{n} &= \lim_{ n \to \infty } a_{n}.
\end{aligned}
$$


Since $$b_{n+1}\leq b_{n}$$, note that, by the monotone convergence theorem,


$$
\limsup x_{n} =\lim_{ n \to \infty } b_{n} = \underset{n}{\inf} b_{n} = \underset{n}{\inf} \underset{m}{\sup} \{ x_{m} : m\geq n\}.
$$


In the same way, 


$$
\liminf x_{n} = \lim_{ n \to \infty } a_{n} = \underset{n}{\sup} a_{n} = \underset{n}{\sup} \underset{m}{\inf} \{ x_{m}: m\geq n \}.
$$



### Lemma (Bounds on limits of subsequences)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a bounded sequence and let $$\{x_{n}\}_{n=1}^\infty$$ have a subsequence $$\{x_{k_{n}}\}_{n=1}^\infty$$ converging to $$L.$$Then $$\liminf x_{n} \leq L \leq \limsup x_{n}$$.

***Proof:***  Consider a subsequence $$\{x_{k_{n}}\}_{n=1}^\infty$$. Note that $$x_{k_{n}} \leq b_{n}$$ since $$k_{n} \geq n$$. In the same way, $$a_{n} \leq x_{k_{n}}$$. Hence $$a_{n} \leq x_{k_{n}} \leq b_{n}$$. The result follows on taking limits.

### Theorem (Convergence and the limits superior and inferior)

Let $$\{x_{n}\}_{n=1}^\infty$$ be a sequence. Then $$\lim_{ n \to \infty } x_{n} = L$$ if and only if  $$\limsup x_{n} = \liminf x_{n} = L$$.

***Proof:*** ($$\implies$$): Let $$\{x_{n}\}_{n=1}^\infty$$ be such that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow}L$$. Then $$\{x_{n}\}_{n=1}^\infty$$ is bounded. Hence there exist subsequences $$\{x_{k_{n}}\}_{n=1}^\infty$$ and $$\{x_{\ell_{n}}\}_{n=1}^\infty$$ such that $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \liminf x_{n}$$ and $$x_{\ell_{n}} \underset{n \rightarrow \infty}{\longrightarrow} \limsup x_{n}$$ (exercise). Conclude that $$\limsup x_{n} = \liminf x_{n} = L$$, since every subsequence must converge to $$L$$.
($$\impliedby$$): Let $$\{x_{k_{n}}\}_{n=1}^\infty$$ be a fixed and arbitrary subsequence. We know that $$a_{n} \leq x_{k_{n}} \leq b_{n}$$. Then, by the squeeze theorem, conclude that $$x_{k_{n}} \underset{n \rightarrow \infty}{\longrightarrow} L$$. Since every subsequence converges to $$L$$ (because we took a fixed and arbitrary one), conclude that $$x_{n} \underset{n \rightarrow \infty}{\longrightarrow} L$$.

A very common trick is to use the definitions of $$\limsup$$ and $$\liminf$$, and to note that:



$$
\inf x_{n} \leq \\\liminf x_{n} \leq  \limsup x_{n} \leq \sup x_{n}.
$$


If $$m$$ is a lower bound of $$x_{n}$$ for every $$n\geq k$$ and $$M$$ is an upper bound of $$y_{n}$$ for every $$n \geq k$$, then by the definitions of $$\sup y_{n}$$ and $$\inf x_{n}$$ we have that $$m \leq \underset{n\geq k}{\inf} x_{n}$$ and that $$M \geq \underset{n\geq k}{\sup} y_{n}$$.
{% endraw %}
