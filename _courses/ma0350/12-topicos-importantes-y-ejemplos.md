---
layout: chapter
course: ma0350
chapter: 12
title: "Tópicos importantes y ejemplos"
slug: 12-topicos-importantes-y-ejemplos
toc:
  sidebar: right
lang: es
fecha: 2025-04-10
---

{% raw %}
Se presentan algunas herramientas útiles para evaluar convergencia de series. Ver también: Series de funciones (series de Taylor).
### Ejemplo 

Sea $$\alpha \in \mathbb{R}$$, entonces


$$
\begin{aligned}
\lim_{ n \to \infty } \frac{\ln(n^{\alpha})}{n}  &= \alpha \lim_{ n \to \infty } \frac{\ln (n)}{n}   \\
&\overset{\text{L'H}}{=} \alpha \lim_{ n \to \infty } \frac{1}{n} \\
&= 0.
\end{aligned}
$$



## Desarrollos limitados

![Pasted image 20250428210634](/assets/img/courses/ma0350/Pasted%20image%2020250428210634.png)

Algunos ejemplos son:
![WhatsApp Image 2025-04-29 at 16.01.57_39813150](/assets/img/courses/ma0350/WhatsApp%20Image%202025-04-29%20at%2016.01.57_39813150.jpg)

Podemos aproximar funciones usando polinomios de Taylor con desarrollos limitados. Por ejemplo, $$(1+x)^{\alpha} = 1+\alpha x+o(x)$$, donde tratamos el resto como la $$o$$ *pequeña de Landau*, tal que $$\lim_{ x \to 0} \frac{o(x)}{x} = 0$$. De igual forma, 


$$
(1+x)^{\alpha} = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2} x^{2} + o(x^{2}).
$$


Ahora, $$o(x) + o(x^{2}) = o(x)$$, pues 


$$
\lim_{ x \to 0 } \frac{o(x^{2})}{x^{2}} x = 0.
$$



#### Ejemplo:


$$
\sqrt{ n^{2}+1 } -\sqrt[3]{n^{3}+1} = \underbrace{ n\left( \left( 1+\frac{1}{n^{2}} \right)^{1/2} - \left( 1+\frac{1}{n^{3}} \right)^{1/3} \right) }_{ \ast }.
$$


Aplicando desarrollos limitados, note que 


$$
\left( 1+\frac{1}{n^{2}} \right)^{1/2} = 1+\frac{1}{2} \cdot \frac{1}{n^{2}} + o\left( \frac{1}{n^{2}} \right),
$$




$$
\left( 1+\frac{1}{n^{3}} \right)^{1/3} = 1 + \frac{1}{3} \cdot\frac{1}{n^{3}} + o\left( \frac{1}{n^{3}} \right).
$$


Entonces, sustituyendo en la expresión inicial, 


$$
\ast = n\left(\frac{1}{2n^{2}} - \frac{1}{3n^{3}} + o\left( \frac{1}{n^{2}} \right)\right) = \frac{1}{2n} + \frac{1}{3n^{2}} + no\left( \frac{1}{n^{2}} \right) = \frac{1}{2n} + \frac{1}{3n^{2}} + o\left( \frac{1}{n} \right).
$$


***OJO:*** $$o(x^{2}) = x o(x)$$ y $$o(x^{n}) = x o(x^{n-1})$$. 

Entonces $$\lim_{ n \to \infty } \frac{\frac{1}{2n} - \frac{1}{3n^{2}} + o\left( \frac{1}{n} \right)}{\frac{1}{n}} = \frac{1}{2}$$, luego por comparación al límite $$\sum_{n=1}^\infty \sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}$$ diverge. 
 
#### Ejemplo 
Considere $$\sum_{n=1}^\infty \frac{\sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}}{n^{p}}$$. ¿Para que valores de $$p$$ converge? Note que, por el desarrollo limitado anterior, 


$$
\frac{\sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}}{n^{p}} \approx \frac{1}{n^{p}},
$$


pues, 


$$
\lim_{ n \to \infty } \frac{\frac{\sqrt{ n^{2}+1 } - \sqrt[3]{n^{3}+1}}{n^{p}}}{\frac{1}{n^{p+1}}} = \lim_{ n \to \infty } \frac{\frac{1}{2n} - \frac{1}{3n^{2}} + o\left( \frac{1}{n} \right)}{\frac{1}{n}} = \frac{1}{2}.
$$



Por lo tanto, la serie converge si y solo si $$\sum_{n=q}^\infty \frac{1}{n^{p+1}}$$ converge, i.e., si $$p>0$$. 
 
#### Ejemplo 
Considere la serie $$\sum_{n=1}^\infty \frac{\left( 1-\frac{1}{n} \right)^{n}}{n}$$. En primer lugar, note que 


$$
\left( 1-\frac{1}{n^{2}} \right)^{n} = e^{\ln(1-1/n^{2})^{n}} = e^{n\ln(1-1/n^{2})}.
$$


Recordamos que 


$$
\ln(1+x) = x + o(x) = x - \frac{x^{2}}{2} + o(x). 
$$


Entonces, en un primer orden, tenemos que 


$$
\ln\left( 1-\frac{1}{n^{2}} \right) = -\frac{1}{n^{2}} + o\left( \frac{1}{n^{2}} \right).
$$


Luego, tenemos que 


$$
n \ln\left( -\frac{1}{n^{2}}+o\left( \frac{1}{n^{2}} \right) \right) = n\left( -\frac{1}{n^{2}}+o\left( \frac{1}{n^{2}} \right) \right) = -\frac{1}{n} + o\left( \frac{1}{n} \right).
$$


Entonces $$\left( 1-\frac{1}{n^{2}} \right)^{n} \underset{n \rightarrow \infty}{\longrightarrow} 1$$, entonces, por comparación al límite, $$\frac{\left( 1-\frac{1}{n} \right)^{n}}{n} \approx \frac{1}{n}$$. Luego, la serie diverge. 
 
#### Ejemplo 
Considere $$\sum_{n=1}^\infty (-1)^{n} e^{-pn}$$. ¿Para que valores de $$p$$ converge? 
Note que la serie converge absolutamente si $$p>0$$. Si $$p\leq 0$$, entonces $$(-1)^{n} e^{-pn} \underset{n \rightarrow \infty}{\cancel{ \longrightarrow }}$$ 0, i.e, diverge. 
 
#### Ejemplo 
Considere $$\sum_{n=1}^\infty \frac{n^{n}}{n! 2^{n}}$$. Aplicando el criterio del cociente, note que 


$$
\lim_{ n \to \infty } \frac{\frac{(n+1)^{n+1}}{(n+1)!2^{n+1}}}{\frac{n^{n}}{n! 2^{n}}} = \lim_{ n \to \infty } (\frac{(n+1)^{n+1}}{2(n+1)n^{n}} = \frac{1}{2}\lim_{ n \to \infty } \left( \frac{n+1}{n} \right)^{n} = \frac{e}{2} > 1.
$$


Luego, la serie diverge.

## Fórmula de Stirling


$$
\lim_{ n \to \infty } \frac{n!}{\left( \frac{n}{e} \right)^{n} \sqrt{ 2 \pi n }} = 1 \implies n! \approx \left( \frac{n}{e} \right)^{n} \sqrt{ 2 \pi n }.
$$


 
#### Ejemplo
En el ejemplo anterior, 


$$
\frac{n^{n}}{2^{n}n!} \approx \left( \frac{e}{2} \right)^{n} \frac{1}{\sqrt{ 2\pi n }}
$$



#### Ejemplo 
Sea $$a_{n}\geq_{0}$$ tal que $$\sum_{n=1}^\infty a_{n}$$ converge. ¿La serie $$\sum_{n=1}^\infty a_{n}^{3}$$ converge?. Note que 


$$
\lim_{ n \to \infty } \frac{a_{n}^{3}}{a_{n}} = \lim_{ n \to \infty } a_{n}^{2} = 0. 
$$


Otra forma de verlo es que $$a_{n}^{3} \leq a_{n}$$ siempre que $$a_{n} < 1$$. 
 
#### Ejemplo 
Considere $$\sum_{n=1}^\infty (-1)^{n} (1+\frac{1}{n})$$. Note que los términos no convergen a cero, pues $$\lim_{ n \to \infty } (-1)^{n}\left( 1+\frac{1}{n} \right) = 1$$. Por tanto, la serie diverge. 
 
#### Ejemplo 
Considere $$\sum_{n=1}^\infty \sinh(n) = \sum_{n=1}^\infty \frac{e^{n} - e^{-n}}{2}$$.  La serie diverge, pues $$\sum_{n=1}^\infty \frac{e^{n}}{2}$$ diverge y $$\sum_{n=1}^\infty e^{-n}$$ converge.
![Pasted image 20250428212044](/assets/img/courses/ma0350/Pasted%20image%2020250428212044.png)

#### Ejemplo 
Calcule el valor de convergencia de la serie $$\sum_{n=0}^\infty n(n-1)x^{n}$$ con $$\lvert x \rvert < 1$$. 

## Fórmula de arcotangente

Esta fórmula es útil para calcular series con arcotangente. 


$$
\arctan\left( \frac{x-y}{1+xy} \right) = \arctan(x) - \arctan(y).
$$



## Desigualdades trigonométrica.

Para todo $$x \in \mathbb{R}$$, tenemos que 


$$
\lvert \sin(x) \rvert \leq \lvert x \rvert \leq  \lvert \tan(x) \rvert .
$$



Si $$x < \frac{\pi}{2}$$ 


$$
\sin(x) > \frac{x}{2}
$$


## Definición de supremo e ínfimo
![Pasted image 20250430225646](/assets/img/courses/ma0350/Pasted%20image%2020250430225646.png)

![Pasted image 20250430225732](/assets/img/courses/ma0350/Pasted%20image%2020250430225732.png)
![Pasted image 20250430225747](/assets/img/courses/ma0350/Pasted%20image%2020250430225747.png)
{% endraw %}
