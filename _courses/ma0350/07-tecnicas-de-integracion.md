---
layout: chapter
course: ma0350
chapter: 7
title: "Técnicas de integración"
slug: 07-tecnicas-de-integracion
toc:
  sidebar: right
lang: es
fecha: 2025-05-20
---

{% raw %}
La siguiente nota muestra algunas técnicas de integración.
## Antiderivadas

Sea $$f:[a,b] \to \mathbb{R}$$ diferenciable. Entonces 


$$
\int_{a}^{b} f'(x) \, d = f(b)-f(a) = f(x)
\biggr\rvert_{a}^{b}.
$$


#### Ejemplos
![Pasted image 20250607000233](/assets/img/courses/ma0350/Pasted%20image%2020250607000233.png)
![Pasted image 20250607231944](/assets/img/courses/ma0350/Pasted%20image%2020250607231944.png)
e
## Integración por partes
Recuerde la fórmula de integración por partes:


$$
\int_{a}^{b} f'(x) g(x) \, dx = f(x)g(x) \biggr\rvert_{a }^{b } - \int_{a}^{b} g'(x) f(x) \, dx  
$$



#### Ejemplos
![Pasted image 20250607000301](/assets/img/courses/ma0350/Pasted%20image%2020250607000301.png)
![Pasted image 20250607000323](/assets/img/courses/ma0350/Pasted%20image%2020250607000323.png)
![Pasted image 20250607000345](/assets/img/courses/ma0350/Pasted%20image%2020250607000345.png)

## Cambio de variable
Recuerde que 


$$
\int_{a}^{b} f(\phi(t)) \phi'(t)  \, dt = \int_{a}^{b} f(u) \, du, 
$$


con $$u = \phi(t)$$ y $$du = \phi'(t) dt$$.

#### Ejemplos
![Pasted image 20250607000450](/assets/img/courses/ma0350/Pasted%20image%2020250607000450.png)
![Pasted image 20250607000516](/assets/img/courses/ma0350/Pasted%20image%2020250607000516.png)
![Pasted image 20250607000556](/assets/img/courses/ma0350/Pasted%20image%2020250607000556.png)
![Pasted image 20250607000624](/assets/img/courses/ma0350/Pasted%20image%2020250607000624.png)


## Sustitución trigonométrica
Las siguientes sustituciones suelen ser útiles si aparecen estas expresiones.


$$
\begin{aligned}
\sqrt{ x^{2} -a^{2}} &\longrightarrow x = a \sec (\theta) \\
\sqrt{ x^{2}+a^{2} } &\longrightarrow x = a \tan (\theta) \\
\sqrt{ a^{2}-x^{2} } &\longrightarrow x = a \sin(\theta).
\end{aligned}
$$


#### Ejemplos
![Pasted image 20250607001402](/assets/img/courses/ma0350/Pasted%20image%2020250607001402.png)
![Pasted image 20250607001527](/assets/img/courses/ma0350/Pasted%20image%2020250607001527.png)



## Identidades trigonométricas
Las siguientes fórmulas suelen ser útiles:
1. $$\cos mx \sin nx = \frac{1}{2}(\sin((m+n)x)) - \sin((m-n)x))$$.
2. $$\cos mx \cos nx = \frac{1}{2} (\cos((m+n)x)+\cos((m-n)x))$$.
3. $$\sin mx \sin nx = \frac{1}{2}(\cos((m+n)x))-\cos((m-n)x)$$.

#### Lista completa de identidades

![Pasted image 20250607001626](/assets/img/courses/ma0350/Pasted%20image%2020250607001626.png)
![Pasted image 20250609153959](/assets/img/courses/ma0350/Pasted%20image%2020250609153959.png)
![Pasted image 20250609153932](/assets/img/courses/ma0350/Pasted%20image%2020250609153932.png)
{% endraw %}
