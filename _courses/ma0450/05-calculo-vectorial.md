---
layout: chapter
course: ma0450
chapter: 5
title: "Cálculo vectorial"
slug: 05-calculo-vectorial
toc:
  sidebar: right
lang: es
---

{% raw %}
## Curvas

### Definición (Curva de clase $$C^{p}$$)
1. Dado un intervalo $$I \subseteq \mathbb{R}$$, una función $$\gamma:I \to \mathbb{R}^n$$ es de clase $$C^{p}(I)$$ si existe un abierto $$J$$ con $$I \subset J$$ y $$\tilde{\gamma}: J\to \mathbb{R}^n$$ tal que $$\tilde{\gamma} \in C^{p}(J)$$ (definición usual para intervalos abiertos) con $$\tilde{\gamma}(t) = \gamma(t)$$ para todo $$t \in I$$.
2. $$\mathcal{C} \subseteq \mathbb{R}^n$$ se llama curva de clase $$C^{p}$$ si existe $$\gamma:I \to \mathbb{R}^n, \gamma \in C^{p}(I)$$ tal que $$\mathcal{C} = \{ \gamma(t): t \in I \}.$$ Decimos que $$(\gamma, I)$$ es la parametrización de $$\mathcal{C}$$.

#### Ejemplo 

**completar notas del lunes 10 e inicio del jueves 13**


### Lema (Conservatividad implica simetría en derivadas)
Si $$F: \mathbb{R}^n\to \mathbb{R}^{n}$$ es conservativo y $$F=(F_{1},\dots,F_{n}) \in C^{1}$$, 


$$
\frac{ \partial F_{j} }{ \partial x_{i} } = \frac{ \partial F_{i} }{ \partial x_{j} } \quad \forall i,j \in \{ 1,\dots,n \}.
$$



***Prueba:*** Como $$F$$ es conservativo, existe $$f:\mathbb{R}^n \to \mathbb{R}$$ tal que 


$$
\nabla f = \left( \frac{ \partial f }{ \partial x_{1} }, \dots, \frac{ \partial f }{ \partial x_{n} }   \right) = (F_{1},\dots,F_{n}) = F.
$$


Así, 


$$
\frac{ \partial F_{j} }{ \partial x_{i} } = \frac{ \partial f }{ \partial x_{i} } \left( \frac{ \partial f }{ \partial x_{j} }  \right) =_{f \in C^{2}} \frac{ \partial f }{ \partial x_{j} } \left( \frac{ \partial f }{ \partial x_{i} }  \right) = \frac{ \partial F_{i} }{ \partial x_{j} }. 
$$


La implicación conversa es también cierta.

#### Ejemplo 
Considere $$F(x,y,z) = (3y^{2}z+ye^{x}, 6xyz+e^{x},3xy^{2})$$. Calculando las derivadas parciales, verificamos que
1. $$\frac{ \partial F_{1} }{ \partial y } = 6yz+e^{x} = \frac{ \partial F_{2} }{ \partial x }$$,
2. $$\frac{ \partial F_{1} }{ \partial z } = 3y^{2}= \frac{ \partial F_{3} }{ \partial x }$$,
3. $$\frac{ \partial F_{2} }{ \partial z } = 6xy = \frac{ \partial F_{3} }{ \partial y }$$.
Si $$f$$ es conservativo, note que $$f(x,y,z) = 3xy^{2}z + y e^{x}$$ ($$\nabla f = f$$).

## Integrales de superficie

### Definición (Regiones y superficies)
1. $$R \subseteq \mathbb{R}^n$$ si existe un conjunto $$K$$ de Jordan tal que $$R = \bar{K}$$ (conexo y no vacío).
2. S $$S\subseteq \mathbb{R}^n$$ se llama superficie de clase $$C^{p}$$ si existe una parametrización $$(\sigma, R)$$ con $$R$$ región en $$\mathbb{R}^{2}$$ tal que $$\sigma:R \to \mathbb{R}^n$$ es de clase $$C^{p}(R)$$, inyectiva en $$R^{\circ}$$ tal que $$\sigma(R) = S$$.

***Ver ejemplos en notas de clase***

##  Área de superficie

### Lema (Existencia del plano tangente)
Sea $$S = (\sigma, R) \subseteq \mathbb{R}^{3}$$. Suponga que existe $$(u_{0},v_{0}) \in R$$ tal que 


$$
\frac{ \partial \sigma }{ \partial u } (u_{0},v_{0}) \neq 0 \neq \frac{ \partial \sigma }{ \partial v } (u_{0},v_{0}).
$$


Entonces, $$S$$ tiene un plano tangente en $$(u_{0},v_{0})$$. Su normal es $$N_{\sigma}(u_{0},v_{0}):=\frac{ \partial \sigma }{ \partial u } (u_{0},v_{0}) \times \frac{ \partial \sigma }{ \partial v } (u_{0},v_{0})$$.

#### Nota
El vector normal es independiente de $$\sigma$$.

### Área de una superficie
Considere una superficie $$S = (\sigma,R)$$. Sea $$C = [a, b] \times [c,d]$$ una caja que contiene a $$R$$ .
![Area sobre una superficie](/assets/img/courses/ma0450/Area%20sobre%20una%20superficie.svg)
Cada subcaja de $$C$$ que interseca a $$\bar{R}$$ se mapea a un trozo pequeño de la superficie. Sean $$\{ a_{0}<a_{1}< \dots < a_{m}\}$$ partición de $$[a,b]$$ y $$\{ c_{0} < c_{1} < \dots < c_{m} \}$$ partición de $$[c,d]$$. Para $$(a_{i},c_{j}) \in R$$, defina las curvas $$\sigma_{a_{i}}:[c,d]\to S$$ y , $$\sigma_{c_{i}}:[a,b]\to S$$ tal que $$\sigma_{a_{i}}(v) = \sigma(a_{i},v)$$ y $$\sigma_{c_{i}}(u) = \sigma(u,c_{i})$$. Esas curvas tienen tangentes 


$$
\sigma_{a_{i}}'(v) = \frac{ \partial \sigma }{ \partial v } (a_{i}, c_{j}), \quad \sigma_{c_{i}}' = \frac{ \partial \sigma }{ \partial u } (a_{i},c_{i}).
$$


Si consideramos la subcaja contenida en los puntos $$(a_{i},c_{j})$$, $$(a_{i+1},c_{j})$$, $$(a_{i},c_{j+1})$$,$$(a_{i+1},c_{j+1})$$, entonces, el área de la superficie puede ser aproximada por el área del paralelogramo formado por el plano tangente:


$$
\begin{aligned}
A_{S} &\approx \lVert (\sigma(a_{i+1},c_{j}) - (\sigma(a_{i},c_{j})) \times ((\sigma(a_{i},c_{j+1}) - \sigma(a_{i}, c_{j})) \rVert \\
&=_{TVM} \left\lVert  (a_{i+1}-a_{i}) \frac{ \partial \sigma }{ \partial u }(u_{i},c_{j})\times (c_{j+1} - c_{j}) \frac{ \partial \sigma }{ \partial v }(a_{i},v_{j}) \right\rVert  \\
&= (a_{i+1} - a_{i})(c_{j+1}-c_{j}) \left\lVert \frac{ \partial \sigma }{ \partial u }(u_{i},c_{j}) \times\frac{ \partial \sigma }{ \partial v }(a_{i},v_{j})  \right\rVert 
\end{aligned}
$$


con $$u_{i} \in [a_{i},a_{i+1}], v_{j} \in [c_{j},c_{j+1}]$$. Sumando sobre las subcajas y tomando límite cuando $$m \to \infty$$: 


$$
\begin{aligned}
\implies A_{S} &\approx \sum_{i,j=1}^{m} \underbrace{ (a_{i+1}-a_{i})(c_{j+1}-c_{j})  }_{ v(C) } \left\lVert \frac{ \partial \sigma }{ \partial u }(u_{i},c_{j}) \times\frac{ \partial \sigma }{ \partial v }(a_{i},v_{j})  \right\rVert \\
&\underset{m \rightarrow \infty}{\longrightarrow} \iint_{R} \left\lVert \frac{ \partial \sigma }{ \partial u }(u,v) \times\frac{ \partial \sigma }{ \partial v }(u,v)  \right\rVert \, du \,dv = \iint_{R} \lVert N_{\sigma}(u,v) \rVert \, du \, dv. 
\end{aligned}
$$



### Definición (Integral de superficie) 
Dada $$g:S\to R$$ continua, con $$S$$ superficie, se define la integral de superficie como 


$$
\iint_{S} g \, dS := \iint_{R} g(\sigma(u,v)) \lVert N_{\sigma} (u,v) \rVert \, du \, dv.
$$


Nota, si $$g \equiv 1$$, $$\iint_{S} dS = \iint_{R} \lVert N_{\sigma}(u,v) \rVert \,du \,dv$$ da el área de $$S$$.

#### Ejemplo (Esfera de radio 1)
En coordenadas esféricas, tenemos $$\rho=1$$. La parametrización viene dada por:
$$\sigma(\theta, \phi) = (\sin \phi \cos \theta, \sin \phi \sin \theta, \cos \phi)$$, con $$\theta \in [0,2\pi], \phi \in [0,\pi]$$.

1. Para calcular el área, obtenemos el vector normal: 


$$
\begin{aligned}
\sigma_{\theta}(\theta, \phi) &= (-\sin \phi \sin \theta, \sin \phi \cos \theta, 0) \\
\sigma_{\phi}(\theta, \phi) &= (\cos \phi \cos \theta, \cos \phi \sin \theta, -\sin \phi) \\
\implies N_{\sigma}(\theta,\phi) &= (-\sin ^{2} \phi \cos \theta, -\sin ^{2} \phi \sin \theta, -\sin \phi \cos \theta) \\
&=-(\sin \phi) \, \sigma(\theta, \phi) \\
\implies \lVert N_{\sigma}(u,v) \rVert &= \lvert \sin \phi \rvert \underbrace{ \lVert \sigma(u,v) \rVert   }_{ =1 } = \lvert \sin \phi \rvert.
\end{aligned}
$$


Así, 


$$
A = \int_{0}^{2 \pi} \int_{0}^{\pi} \lvert \sin \phi \rvert  \, d\phi  \, d \theta = \int_{0}^{2\pi}  \, d \theta \int_{0}^{\pi } \sin \phi \, d \phi = 4 \pi.  
$$



2. Calculemos ahora el plano tangente en $$(\theta, \phi) = (\frac{\pi}{4}, \frac{\pi}{2})$$. Obtenemos primero un punto del plano evaluando la superficie en el punto dado: 


$$
\sigma\left( \frac{\pi}{4}, \frac{\pi}{2} \right) = \left( \frac{\sqrt{ 2 }}{2}, \frac{\sqrt{ 2 }}{2}, 0 \right) =P.
$$


Ahora, obtenemos el vector normal 


$$
N = -\sin \frac{\pi}{2} \left( \frac{\sqrt{ 2 }}{2}, \frac{\sqrt{ 2 }}{2},0  \right) =\left( \frac{-\sqrt{ 2 }}{2}, \frac{-\sqrt{ 2 }}{2}, 0\right).
$$


Luego, el plano tangente es 


$$
\Pi: \left( \frac{-\sqrt{ 2 }}{2}, \frac{-\sqrt{ 2 }}{2},0 \right) \cdot \left( x - \frac{\sqrt{ 2 }}{2}, y - \frac{\sqrt{ 2 }}{2}, z\right) = 0.
$$



***Ver más ejemplos en las notas de clase***

## Superficies orientadas

#### Ejemplo 
Ver ejemplo de la cinta de Mobius.

### Definición (Superficie orientable)
1. Un vector unitario normal para $$S$$ en $$(x_{0},y_{0},z_{0}) = \sigma(u_{0},v_{0})$$ 


$$
n_{\sigma}(x_{0},y_{0},z_{0}) = \frac{N_{\sigma}(u_{0},v_{0})}{\lVert N_{\sigma}(u_{0},v_{0}) \rVert }.
$$


2. $$S$$ es orientable si posee $$(\sigma, R)$$ tal que si $$\sigma (u_{0},v_{0}) = \sigma(u_{1},v_{1})$$, entonces $$n_{\sigma}(u_{0},v_{0}) = n_{\sigma}(u_{1},v_{1})$$. 
3. 
### Definición (Integral de superficie orientada)
Sea $$S$$ una superficie orientada con parametrización $$(\sigma, R)$$ de clase $$C^{1}$$ con vector normal unitario $$n$$. Sea $$F:S\to \mathbb{R}^{3}$$ continua. Se define 


$$
\iint_{S} F \cdot n \, dS = \iint_{R} F(\sigma(u,v)) \cdot N_{\sigma}(u,v) \, du \, dv
$$



#### Nota
Dadas $$(\sigma_{1}, R_{1}), (\sigma_{2}, R_{2})$$ de $$S$$, entonces 


$$
\iint_{R_{1}} F(\sigma_{1}(u,v)) N_{\sigma_{1}} (u,v) \, du \, dv = \pm \iint_{R_{2}} F(\sigma_{2}(u,v)) N_{\sigma_{2}} (u,v) \, du \, dv.
$$



***Ver ejemplos en notas de clase***

## Teoremas de Green, Gauss y Stokes

### Definición (Orientación positiva en curvas)
Sea $$R \subseteq \mathbb{R}^{2}$$ región, $$\partial R$$ suave a trozos. Se dice que $$\partial R$$ tiene orientación positiva si tiene la orientación inducida al considerar $$R$$ como superficie en $$\mathbb{R}^{3}$$ ($$S =\{(x,y,0), (x,y) \in \mathbb{R}\}$$) con orientación positiva (normal paralela a eje $$z^{+}$$).

### Teorema (Green)
Sea $$R \subseteq \mathbb{R}^{2}$$ región (como en la definición). Sea $$F = (F_{1}, F_{2}):\mathbb{R}^{2} \to \mathbb{R}^{2}$$ de clase $$C_{1}$$. Entonces 


$$
\int_{\partial R} F \cdot T \, dS = \iint_{R} \left( \frac{ \partial F_{2} }{ \partial x } -\frac{ \partial F_{1} }{ \partial y }\right) \, dy \, dx  .
$$



***Ver ejemplos en notas de clase***

### Definición (Orientación positiva en superficies y divergencia)
1. Sea $$R \subseteq \mathbb{R}^{3}$$ región con $$\partial R = S$$ orientable, suave a trozos. S está orientada de forma positiva si su vector normal unitario $$n(x)$$ apunta lejos del interior $$R^{\circ}$$ para todo $$x$$.
2. Dada $$F=(F_{1},F_{2},F_{3}):\mathbb{R}^{3}-.\mathbb{R}^{3}$$ de clase $$C^{1}$$, su divergencia es 


$$
\nabla \cdot F = \mathrm{div} F = \frac{ \partial F_{1} }{ \partial x }  + \frac{ \partial F_{2} }{ \partial y } + \frac{ \partial F_{3} }{ \partial z }. 
$$



### Teorema (Gauss)
Sea $$R \subseteq \mathbb{R}^{3}$$ región orientada positiva. Si $$F:\mathbb{R}^{3} \to \mathbb{R}^{3}$$ de clase $$C^{1}$$, entonces 


$$
\iint_{\partial R} F \cdot n \, dS = \iiint_{R} \mathrm{div} F \, dz \,dy \,dx
$$



***Ver ejemplos en notas de clase***

### Definición (Rotacional)
Dada $$F:\mathbb{R}^{3}\to \mathbb{R}^{3}$$ de clase $$C^{1}$$, se define su rotacional 


$$
\mathrm{rot F} = \nabla \times F = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{ \partial  }{ \partial x }  & \frac{ \partial  }{ \partial y }  & \frac{ \partial  }{ \partial z }  \\
F_{1} & F_{2} & F_{3}
\end{vmatrix} =
\left( \frac{ \partial F_{3} }{ \partial y } - \frac{ \partial F_{2} }{ \partial z }, -\frac{ \partial F_{3}}{ \partial x } + \frac{ \partial F_{1} }{ \partial z }, \frac{ \partial F_{2} }{ \partial x } - \frac{ \partial F_{1} }{ \partial y }     \right)
$$



### Teorema (Stokes)
Sea $$S$$ una superficie orientable de clase $$C^{2}$$, suave a trozos, y con normal $$n$$. Suponga que "$$\partial S$$" es una curva cerrada de clase $$C^{1}$$, suave a trozos y con orientación positiva. Si $$F:\mathbb{R}^{3}\to \mathbb{R}^{3}$$ es de clase $$C^{1}$$, entonces 


$$
\iint_{\partial S} F \cdot T \, dS = \iint_{S} \mathrm{rot} F \cdot n \, dS.
$$


#### Nota
En este caso, la "frontera de $$S$$" no se refiere a su frontera topológica, (pues todos los puntos satisfacen la definición). Nos referimos más bien al mapeo de  $$\partial R$$, donde $$S = (\sigma, R)$$.

***Ver ejemplos en notas de clase***
{% endraw %}
