---
layout: chapter
course: ma0450
chapter: 3
title: "Differentiation"
slug: 03-differentiation
toc:
  sidebar: right
lang: en
fecha: 2025-09-08
permalink: /notes/ma0450/03-differentiation/
---

{% raw %}
## Partial derivatives

### Definition (Partial derivative)
Let $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$ with $$D$$ a neighbourhood of $$a$$. For $$j \in \{ 1,\dots,n \}$$, the partial derivative of $$f$$ at $$a = (a_{1},\dots,a_{n})$$ with respect to the $$j$$-th entry is defined as 


$$
D_{j}f(a) = \lim_{ h \to 0} \frac{f(a_{1},\dots,a_{j-1}, a_{j}+h, a_{j+1},\dots,a_{n}) - f(a)}{h}.
$$



#### Note:
1. If $$y=f(x)$$, then $$f'(a) = \lim_{ h \to 0 } \frac{f(a+h)-f(a)}{h}$$.
2. We write $$D_{j}f(a) = \frac{\partial f}{\partial x_{j}}(a) = f_{x_{j}}(a)$$.
3. The variables $$x_{i} \neq x_{j}$$ for every $$i$$ are treated as constants.
4. If I define $$g(x_{j}) = f(a_{1},\dots,a_{j-1}, x_{j}, a_{j+1},\dots, a_{n})$$, then $$D_{j}f(a) = g'(a_{j})$$.

#### Example 
If $$f(x,y,z) = e^{xy^{2}} + \sin(xyz)$$ then $$D_{1}f(x,y,z) = e^{xy^{2}}y^{2} + \cos(xyz) \cdot yz$$.

### Definition (Higher-order partial derivatives)
Given $$f$$ such that $$D_{j} f(a)$$ exists for every $$j \in \{ 1,\dots n \}$$, we define $$D_{ij}f(a) = D_{i} (D_{j} f(a))$$.
We write $$D_{ij} f(a) = \frac{\partial}{\partial  x_i}(\frac{\partial f}{\partial  x_{j}})(a) = f_{x_{j}x_{i}}(a)$$.

#### Note:
The notation extends, e.g., $$\frac{\partial^{4} f}{\partial x_{1} \partial x_{2} \partial x_{4} \partial x_{3}}(a)$$.

### Theorem (Schwarz)
Let $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, with $$a \in D$$. Suppose that $$f$$ is continuous on $$B_{r}(a)$$ and that $$D_{1}f$$, $$D_{2} f$$ and $$D_{21} f$$ exist and are continuous at $$a$$. Then $$D_{21} f(a)$$ exists and $$D_{21}f(a) = D_{12}f(a)$$.

***Proof:*** For $$n = 2$$, let $$a = (x_{0},y_{0})$$. There exist $$h,k > 0$$ such that 


$$
\underbrace{ [x_{0}-h,x_{0}+h] }_{I } \times \underbrace{ [y_{0}-k,y_{0}+k] }_{ J } \subseteq B_{r}(x_{0},y_{0}) \subseteq D.
$$


Define $$\phi(x) = f(x, y_{0}+k) - f(x,y_{0})$$. By hypothesis $$\phi$$ is continuous and differentiable on $$I$$. By the mean value theorem, there exists $$c \in (x_{0}, x_{0}+h)$$ such that $$\phi(x_{0}+h) - \phi(x_{0}) = \phi'(c) \cdot h$$. Then 


$$
\phi(x_{0}+h) - \phi(x_{0}) = h(D_{1}f(c, y_{0}+k) - D_{1}f(c,y_{0})).
$$


Define $$\psi(y) = D_{1}f(x,y)$$ with $$y \in [y_{0},y_{0}+k]$$. By the mean value theorem, there exists $$d \in (y_{0},y_{0}+k)$$ such that $$\psi(y_{0}+k) - \psi(y_{0}) = \psi'(d) \cdot k$$. Hence 


$$
\begin{aligned}
& D_{1} f(c,y_{0}+k) - D_{1} f(c,y_{0}) = D_{21} f(c,d) \cdot k \\
\implies & \phi(x_{0}+h) - \phi(x_{0}) = D_{21} f(c,d) \cdot k \cdot h \\
\implies & \frac{f(x_{0}+h,y_{0}+k) - f(x_{0}+h,y_{0})}{k} - \frac{f(x_{0},y_{0}+k)-f(x_{0},y_{0})}{k} = h \cdot D_{21} f(c, d) \\
\end{aligned} 
$$


Taking the limit as $$k \to 0$$ and dividing by $$h$$:


$$
\frac{D_{2}f(x_{0}+h,y_{0}) - D_{2}f(x_{0},y_{0})}{h} = D_{21} f(c,y_{0}) \quad \text{since }d \in (y_{0},y_{0}+k.
$$


Taking the limit as $$h \to 0$$ 


$$
D_{1}(D_{2}f) (x_{0}, y_{0}) = D_{12} f (x_{0},y_{0}) = D_{21} f(x_{0},y_{0}),
$$


from which the result follows.

#### Note
For $$f:\mathbb{R}^{2} \to \mathbb{R}$$, $$D_{121} f(a,b) = D_{112} f(a,b) = D_{211} f(a,b)$$.  If $$f \in \mathbb{R}^{n} \to \mathbb{R}$$, the result still holds and the intuition of the proof is the same, but the proof is more tedious.

### Theorem (Mean value theorem)
Cf. The Riemann integral (MA0350, MVT in one variable). Let $$f: B_{\delta}(a) \subseteq \mathbb{R}^n \to \mathbb{R}$$. Suppose that $$f$$ is continuous and that for every $$j \in \{ 1,\dots,n \},$$ $$D_{j}(f)$$ exists and is continuous. Then, for every $$x \in B_{\delta}(a)$$, there exist $$\xi_{1}, \dots \xi_{n} \in B_{\delta}(a)$$ such that, if $$x = (x_{1},\dots, x_{n})$$ and $$a = (a_{1}, \dots, a_{n})$$, then


$$
f(x) - f(a)= \sum_{j=1}^{n} D_{j} f(\xi_{j}) (x_{j} - a_{j}).
$$


***Proof:*** For $$n=2$$, note that 


$$
f(x) - f(a) = f(x_{1},x_{2}) - f(a_{1}, x_{2}) + f(a_{1},x_{2}) - f(a_{1},a_{2}).
$$


Let $$g(t) = f(t,x_{2})$$ and $$h(t) = f(a_{1},t)$$. Then 


$$
\begin{aligned}
\implies f(x)-f(a) &= g(x_{1}) - g(a_{1}) + h(x_{2}) - h(a_{2}) \\
&\underset{TVM}{=} g'(t_{1}) (x_{1}-a_{1}) + h'(t_{2})(x_{2}-a_{2}) \\
&= D_{1}f(\underbrace{ t_{1},x_{2} }_{ \xi_{1} })(x_{1}-a_{1}) + D_{2} f(\underbrace{ a_{1}, t_{2} }_{ \xi_{2} })(x_{2}-a_{2}),
\end{aligned}
$$


with $$t_{i}$$ between $$x_{i}$$ and $$a_{i}$$. The argument is analogous for $$n>2$$.

#### Example 
Consider 


$$
f(x,y) = \begin{cases}
\frac{xy}{x^{2}+y^{2}} \quad \text{if }(x,y) \neq  (0,0) \\
0  \quad  \quad  \quad \text{if }(x,y) = (0,0)
\end{cases}.
$$


Note that 
1. $$f$$ is not continuous at $$(0,0)$$.
2. $$\frac{\partial f}{\partial x} (0,0) = \lim_{ h \to 0 } \frac{f(h,0)-f(0,0)}{h} = \lim_{ h \to 0 } \frac{\frac{0 \cdot h}{h^{2}+0^{2}} - 0}{h} = 0$$.
3. Now, if $$(a,b) \neq (0,0)$$, then 


$$
\frac{\partial f}{\partial x}(a,b) = \frac{(x^{2}+y^{2})y - xy \cdot 2x}{(x^{2}+y^{2})^{2}} \biggr\rvert_{(x,y)=(a,b)} = \frac{b(b^{2}-a^{2})}{(a^{2}+b^{2})^{2}}.
$$


So 


$$
\frac{\partial f(x,y)}{\partial x} = \begin{cases}
\frac{y(x^{2}-y^{2})}{(x^{2}+y^{2})^{2}} \quad \text{if }(x,y) \neq (0,0) \\
0  \quad  \quad  \quad \text{if }(x,y) = (0,0)
\end{cases}
$$


We can prove that this function is continuous at $$(0,0)$$, which tells us that in several dimensions differentiability of the partials does not imply continuity. Note that the derivative is not continuous at $$(0,0)$$.


### Theorem (Partial derivatives and continuity)
Let $$f:D\subseteq \mathbb{R}^n \to \mathbb{R}$$ be such that $$\frac{\partial f}{\partial x_{i}}(x)$$ exists and is continuous on $$D$$ (open) for every $$i \in \{ 1,\dots,n \}$$. Then $$f$$ is continuous on $$D$$.

***Proof:*** Let $$a \in D, \varepsilon>0$$. Then there exists $$r>0$$ such that $$B:=\bar{B}_{r}(a) \subseteq D$$. Since $$B$$ is compact and the $$\frac{\partial f}{\partial x_{i}}(x)$$ are continuous, there exist $$M_{i} > 0$$ for every $$i \in \{ 1,\dots,n \}$$ such that $$\left\lvert   \frac{\partial f}{\partial x_{j}} (x) \right\rvert \leq M_{j}$$ for every $$x \in B$$. Let $$M = \max \{ M_{1}, \dots, M_{n} \}>0$$. Take $$\delta < \min \left\{  \frac{\varepsilon}{Mn},1  \right\}$$.  Suppose that $$\lVert x-a \rVert<\delta$$. So $$\lvert x_{j}-a_{j} \rvert < \delta$$ for every $$j$$. Then, by the mean value theorem, $$f(x)-f(a) = \sum_{j=1}^{n} \frac{\partial f}{\partial x_{j}}(\xi_{j})(x_{j}-a_{j})$$, with $$\xi_{1}, \xi_{2},\dots,\xi_{n} \in B$$. Then 


$$
\begin{aligned}
\lvert f(x)-f(a) \rvert &\leq \sum_{j=1}^{n} \left\lvert \frac{\partial f}{\partial x_{j}}(\xi_{j}) \right\rvert \lvert x_{j}-a_{j} \rvert \\
&\leq \sum_{j=1}^{n} M\delta = nM\delta < \varepsilon 
\end{aligned}
$$



### Theorem (Extrema and derivatives)
Given $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, suppose that $$f$$ attains a relative extremum at $$c \in D^{\circ}$$. If $$\frac{\partial f}{\partial x_{j}}(c)$$ exists, then $$\frac{\partial f}{\partial x_{j}}(c) = 0$$.

***Proof:*** Define $$g(x) = f(c_{1},c_{2},\dots,c_{j-1},x,c_{j+1},\dots,c_{n})$$ with $$c = (c_{1},\dots,c_{n})$$. Then $$g'(c) = \frac{\partial f}{\partial x_{j}}(c)$$. We know that $$g$$ has a relative extremum at $$c$$, so $$g'(c) = \frac{\partial f}{\partial x_{j}}(c) = 0$$.

#### Note 
Let $$f:\mathbb{R} \to \mathbb{R}$$. If $$f'(a) = \lim_{ x \to a } \frac{f(x)-f(a)}{x-a} = \frac{\lim_{ h \to 0 }f(a+h)-f(a)}{h}$$. This is the notion of having a derivative, but is this notion the same as differentiability?

## Differentiability

#### Note
In one dimension, $$f'(a)$$ exists if and only if $$\lim_{ h \to 0 } \frac{f(a+h)-f(a)-f'(a)h}{h} = 0$$.

### Definition (Differentiability)
Given $$f:D \subseteq \mathbb{R}^n\to \mathbb{R}^{m}$$, with $$D$$ a neighbourhood of $$a$$. We say that $$f$$ is differentiable at $$a$$ if there exists a linear transformation $$T:\mathbb{R}^n\to \mathbb{R}^{m}$$ such that 


$$
\lim_{ \vec{h} \to 0 } \frac{\lVert f(a+\vec{h}) - f(a) - T(\vec{h}) \rVert_{m}}{\lVert \vec{h} \rVert_{n}}  = 0
$$


#### Notes
1. $$\frac{\partial f}{\partial x_{j}}(c) = \lim_{ h \to 0 } \frac{f(c+h e_{j})-f(c)}{h}$$, where $$e_{j}$$ is the $$j$$-th standard basis vector.
2. If the function is differentiable at $$a$$, we write $$D_{f}(a)=T$$
3. Evaluating $$D_{f}$$ is written $$D_{f}(a)(x) = T(x)$$.

#### Example 
Consider $$f:\mathbb{R}^n\to \mathbb{R}^{m}$$, with $$f(x) = c \in \mathbb{R}^{m}$$. If $$T(x) = 0$$, then $$D_{f}(a) = 0$$, since 


$$
\lim_{ h \to 0} \frac{\lVert c-c-0 \rVert }{\lVert h \rVert }  = 0
$$



#### Example 
If $$f:\mathbb{R}\to \mathbb{R}$$ is differentiable at $$a$$, then $$D_{f}(a)(h) = f'(a) h$$. The differential can be used to make approximations, for instance Taylor's: $$f(a+h) \approx f(a) + hf'(a)$$.

#### Example 
Consider $$f:\mathbb{R}^{2}\to \mathbb{R}$$ with $$f(x,y) = x^{2}+3y$$. What is $$D_{f}(a,b)$$? 
Let $$(h,k)$$ be the increment in the limit. Note that 


$$
\begin{aligned}
&  \lim_{ (h,k) \to (0,0) } \frac{\lvert (a+h)^{2}+3(b+k) - a^{2}-3b-T(h,k) \rvert }{\lVert (h,k)\rVert } \\
&= \lim_{ (h,k) \to (0,0) } \frac{\lvert 2ah+h^{2}+3k-T(h,k) \rvert }{ \sqrt{h^{2}+k^{2}}}=L
\end{aligned}
$$


Take $$T(h,k) = 2ah + 3k$$. Clearly $$T$$ is linear and moreover, if $$(h,k) \longrightarrow (0,0)$$ then $$T(h,k)\longrightarrow 0$$. So 


$$
L=\lim_{ (h,k) \to (0,0)} \frac{h^{2}}{\sqrt{ h^{2}+k^{2} }} = 0 
$$


since 


$$
0 \leq  \frac{h^{2}}{\sqrt{ h^{2}+k^{2} }} \leq \frac{h^{2}}{\sqrt{ h^{2} }} = h \underset{(h,k) \rightarrow (0,0)}{\longrightarrow} (0,0),
$$


and therefore $$D_{f}(a,b)(h,k) = 2ah+3k =\begin{pmatrix}2a & 3\end{pmatrix} \begin{pmatrix}h \\ k\end{pmatrix}$$.

 ### Theorem (Uniqueness of the differential)
If $$f$$ is differentiable at $$a$$, its differential is unique.

***Proof:*** Suppose there exist linear $$T, S: \mathbb{R}^n \to \mathbb{R}^{m}$$ both satisfying the definition. Then 


$$
\begin{aligned}
\frac{\lVert T(h)-S(h) \rVert }{\lVert h \rVert } \leq  \frac{\lVert T(h) - f(a+h) + f(a) \rVert }{\lVert h \rVert } + \frac{\lVert f(a+h) - f(a) - S(h)  \rVert }{\lVert h \rVert } \underset{h \rightarrow 0}{\longrightarrow} 0. 
\end{aligned}
$$


I need $$T(x) =  S(x) \quad \forall x \in \mathbb{R}^n$$. So, if $$x \in \mathbb{R}^n\setminus \{ 0 \}$$, $$t \in \mathbb{R}$$, take $$h = tx$$. Then


$$
0 = \lim_{ t \to 0 } \frac{\lVert T(tx) - S(tx) \rVert }{\lVert tx \rVert } = \lim_{ t \to 0 } \frac{\lVert T(x) - S(x) \rVert }{\lVert x \rVert } = \frac{\lVert T(x) - S(x) \rVert }{\lVert x \rVert },
$$


so $$T(x) = S(x)$$ for every $$x \in \mathbb{R}^n\setminus \{ 0 \}$$ (equality at zero holds trivially since they are linear transformations), and therefore $$S = T$$.


### Theorem (Differentiability implies continuity)
If $$f$$ is differentiable at $$a$$, then it is continuous at $$a$$. So $$f$$ is continuous at $$a$$.

***Proof:*** Let $$\varepsilon>0$$. By differentiability there exists $$\delta_{1}>0$$ such that if $$\lVert h \rVert < \delta_{1}$$ then 


$$
\frac{\lVert f(a+h) - f(a) - D_{f}(a)(h) \rVert }{h} < \varepsilon. \ \tag{1}
$$


Since $$D_{f}(a)$$ is linear, it is continuous. There exists $$\delta_{2}>0$$ such that 
$$\lVert x-a \rVert<\delta_{2} \implies \lVert D_{f}(a)(x) - D_{f}(a)(a) \rVert < \frac{\varepsilon}{2}. $$
Take $$\delta = \min \left\{  \delta_{1}, \delta_{2}, \frac{1}{2}  \right\}$$. Suppose that $$\lVert x-a \rVert < \delta$$. Then 


$$
\begin{aligned}
\lVert f(x)-f(a) \rVert &\leq \lVert f(x) - f(a) - D_{f}(a)(x-a) \rVert + \lVert D_{f}(a)(x-a) \rVert  \\
&\leq \varepsilon \lVert x-a \rVert + \frac{\varepsilon}{2} \quad  \quad  \text{taking } h =x-a \text{ in (1)}\\
&< \varepsilon \delta + \frac{\varepsilon}{2} \leq \varepsilon.
\end{aligned}
$$


We conclude that $$f$$ is continuous at $$a$$. 

### Definition (Directional derivative)
Given $$f:\mathbb{R}^n\to \mathbb{R}$$, $$\vec{u} \in \mathbb{R}^n$$, $$\lVert \vec{u} \rVert = 1$$, the directional derivative along $$\vec{u}$$ is defined as 


$$
D_{\vec{u}}f(a) = \lim_{ h \to 0 } \frac{f(a+h \vec{u}) - f(a)}{h}.
$$



#### Note
If $$\vec{u} = e_{j}$$, then $$D_{\vec{u}}f(a) = \frac{\partial f(a)}{\partial x_{j}}$$, since $$a+h \vec{u} = a+h e_{j}$$. 

### Theorem (Differentiability and directional derivatives)
Let $$f:D \subseteq \mathbb{R}^n\to \mathbb{R}$$, $$a \in D$$ open. If $$f$$ is differentiable at $$a$$, then $$D_{\vec{u}}f(a)$$ exists for every $$\vec{u} \in \mathbb{R}^n$$, and $$D_{\vec{u}}f(a) = D_{f}(a)(u)$$.

***Proof:*** Note that 


$$
\begin{aligned}
D_{\vec{u}}f(a) &= \lim_{ h \to 0 }\underbrace{  \frac{f(a+h \vec{u}) - f(a)-D_{f}(a)(hu)}{h} }_{ \longrightarrow 0 } + \frac{D_{f}(a)(\cancel{ h }u)}{\cancel{ h }} \\
&= D_{f}(a)(u),
\end{aligned}
$$


from which the result follows. 

#### Corollary
Under the same hypothesis, $$\frac{\partial f}{\partial x_{1}}, \dots, \frac{\partial f}{\partial x_{xn}}$$ exist and $$D_{f}(a)(y) = \sum_{i=1}^{n} \frac{\partial f(a)}{\partial x_{i}} y_{i}$$ with $$y = (y_{1}, \dots, y_{n})$$.

***Proof:*** The partial derivatives exist by the previous theorem, taking $$u$$ to be each of the standard basis vectors. Moreover, 


$$
\begin{aligned}
D_{f}(a)(y) &= D_{f}(a)\left( \sum_{i=1}^{n} e_{i} y_{i} \right) \\
&= \sum_{i=1}^{n} y_{i} D_{f}(a)(e_{i}) \\
&= \sum_{i=1}^{n} y_{i} \frac{\partial f(a)}{\partial x_{i}}.
\end{aligned}
$$



#### Note
In vector notation, 


$$
D_{f}(a)(y) = \underbrace{ \begin{pmatrix}
\frac{ \partial f(a) }{ \partial x_{1}}  \\
\vdots \\
\frac{ \partial f(a) }{ \partial x_{n} } 
\end{pmatrix} }_{ \text{gradient of } f \text{ at } a \text{: }\nabla f(a)} \cdot  \quad
\begin{pmatrix}
y_{1} \\
\vdots \\
y_{n}
\end{pmatrix}
\implies D_{f}(a) = \nabla f(a).
$$



#### Example 
Consider $$f:\mathbb{R}^{3} \to \mathbb{R}$$ with $$f(x,y,z)= x^{2}++yz$$. Then 


$$
\nabla f (x,y,z) = \begin{bmatrix}
\frac{ \partial f }{ \partial x }(x,y,z)  \\
\frac{ \partial f }{ \partial y }(x,y,z)  \\
\frac{ \partial f }{ \partial z }(x,y,z) 
\end{bmatrix} = \begin{bmatrix}
2x \\
z \\
y
\end{bmatrix}.
$$


If $$a = (1,-1,0)$$, then $$\nabla f(a) =\begin{bmatrix}2 & 0 & -1\end{bmatrix}^{T}$$ and so 


$$
D_{f}(a)(x,y,z) = \begin{bmatrix}
2 \\
0 \\
-1
\end{bmatrix} \cdot
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} = 2x-z.
$$



### Theorem (Differentiability componentwise)
Let $$f:\mathbb{R}^n \to \mathbb{R}^{m}$$, $$f =\begin{pmatrix}f_{1} \\ \vdots \\ f_{m}\end{pmatrix}$$, $$f_{j}:\mathbb{R}^n\to \mathbb{R}$$. Then $$f$$ is differentiable at $$a$$ if and only if $$f_{j}$$ is differentiable at $$a$$ for every $$j \in \{ 1,\dots ,n \}$$. Moreover, 


$$
D_{f}(a) = \begin{bmatrix}
D_{f_{1}}(a) \\
\vdots \\
D_{f_{n}}(a)
\end{bmatrix}.
$$


***Proof:*** ($$\impliedby$$): We know that for every $$x \in \mathbb{R}^{n}$$ and every $$j \in \{ 1,\dots,n \}$$, $$\lvert x_{j} \rvert \leq \lVert x \rVert \leq \sum_{j=1}^{n} \lvert x_{j} \rvert$$. So we have that 


$$
\begin{aligned}
0 \leq  \frac{\lvert f_{j}(a+h) - f_{j}(a) - T_{j}(h) \rvert }{\lVert h \rVert } &\leq \frac{\lVert f(a+h) -f(a) - T(h) \rVert }{\lVert h \rVert } \\
&\leq \sum_{j=1}^{m} \frac{\lvert f_{j}(a+h) -f_{j}(a) - T_{j}(h)\rvert}{\lVert h \rVert }.
\end{aligned}
$$


$$(\implies)$$: If $$f$$ is differentiable at $$a$$, then $$f_{j}$$ is differentiable at $$a$$ (by the inequality above), and so $$D_{f_{j}}(a) = T_{j}$$.

### Definition (Jacobian matrix)
Let $$f$$ be differentiable at $$a$$. Since $$D_{f}(a):\mathbb{R}^n \to \mathbb{R}^{m}$$, define $$J_{f}(a)$$ (the Jacobian matrix of $$f$$ at $$a$$) to be the matrix associated with $$D_{f}(a)$$ in the standard bases.

#### Corollary
If $$f:\mathbb{R}^n\to \mathbb{R}^{m}$$, $$f = \begin{pmatrix}f_{1} & \dots & f_{m}\end{pmatrix}^{T}$$ is differentiable at $$a$$ then $$\frac{ \partial f_{i}(a) }{ \partial x_{j} }$$ exists for all $$j \in \{ 1,\dots n \}$$, $$i \in \{ 1,\dots,m \}$$. Moreover, $$[J_{f}(a)]_{ij} =  \frac{ \partial f_{i}(a) }{ \partial x_{j} }$$. That is 


$$
J_{f}(a) = \begin{bmatrix}
\frac{ \partial f_{1}(a) }{ \partial x_{1} } & \frac{ \partial f_{1}(a) }{ \partial x_{2} } & \dots & \frac{ \partial f_{1}(a) }{ \partial x_{n} } \\
\frac{ \partial f_{2}(a) }{ \partial x_{1} } & \frac{ \partial f_{2}(a) }{ \partial x_{2} }  & \dots  & \frac{ \partial f_{2}(a) }{ \partial x_{n} } \\
\vdots & \vdots & \ddots & \vdots \\
\frac{ \partial f_{m}(a) }{ \partial x_{1} } & \frac{ \partial f_{m}(a) }{ \partial x_{2} } & \dots & \frac{ \partial f_{m}(a) }{ \partial x_{n} }
\end{bmatrix}_{m \times n}
$$



#### Example
Consider $$f(x,y,z) = \begin{pmatrix}x^{2}\sin y - z \\ e^{xy} + zx\end{pmatrix}$$. Then 


$$
J_{f}(x,y,z) = \begin{bmatrix}
2x\sin y & x^{2}\cos y & -1 \\
y e^{xy}+z & xe^{xy} & x
\end{bmatrix}.
$$


If $$(a,b,c) = (1,0,\pi)$$, 


$$
\begin{aligned}
\implies J_{f}(a,b,c) &= \begin{bmatrix} 
0 & 1 & -1 \\
\pi & 1 & 1 
\end{bmatrix} \\
\implies D_{f}(a,b,c)(x,y,z) &= \begin{bmatrix}
0 & 1 & -1 \\
\pi & 1 & 1 
\end{bmatrix} \begin{bmatrix} 
x \\ 
y \\ 
z 
\end{bmatrix} = \begin{bmatrix} 
y-z \\
\pi x+y+z
\end{bmatrix}.
\end{aligned}
$$



### Theorem (Jacobian and gradient)
Let $$f:A\subseteq \mathbb{R}^n \to \mathbb{R}$$. Suppose that $$f$$ is continuously differentiable at $$a$$; that is, $$f$$ and its first-order derivatives are continuous at $$a$$. Then $$f$$ is differentiable at $$a$$ and $$J_{f}(a) = \nabla f(a)$$.

***Proof:*** Let $$\varepsilon>0$$. By continuity there exist $$\delta_{1},\dots,\delta_{n}$$ such that for every $$1\leq j\leq n$$, if $$\lVert x-a \rVert <\delta_{j}$$ then $$\left\lVert  \frac{ \partial f }{ \partial x_{j} }(x) - \frac{ \partial f }{ \partial x_{j} }(a)  \right\rVert < \frac{\varepsilon}{n}$$. Let $$T:\mathbb{R}^n\to \mathbb{R}$$ be a linear transformation with $$T(x_{1},\dots,x_{n}) = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(a) \cdot x_{i}$$. Take $$\delta = \min\{ \delta_{1},\dots,\delta_{n} \}$$ and let $$h = (h_{1},\dots, h_{n}) \in B_{\delta}(a)$$. By the mean value theorem, there exist $$\xi_{1}, \dots, \xi_{n} \in B_{\delta}(a)$$ such that  


$$
f(a+h)-f(a) = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(\xi_{i}) \cdot h_{i}.
$$



So, using this expression in the definition of differentiability: 


$$
\begin{aligned}
\frac{\lvert f(a+h) - f(a) \rvert }{\lVert h \rVert } &= \frac{1}{\lVert h \rVert } \left\lvert  \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} }(\xi_{i}) \cdot h_{i} \right\rvert \\
&<  \sum_{i=1}^{n} \frac{\varepsilon}{n} \underbrace{ \frac{\lvert h_{i} \rvert }{\lVert h \rVert } }_{ \leq 1 } < \varepsilon,
\end{aligned}
$$


from which we conclude that $$D_{f}(a) = T$$.

### Theorem (Jacobian and gradients for functions into $$\mathbb{R}^{m}$$)
Let $$f:A \subseteq \mathbb{R}^n \to a \in A$$. Suppose that $$f$$ is continuously differentiable at $$a$$. Then $$f$$ is differentiable at $$a$$ and $$J_{f}(a) = [\nabla f_{1}(a), \nabla f_{2}(a),\dots, \nabla f_{n}(a)]$$,

***Proof:*** By hypothesis, for all $$1 \leq i \leq n$$, $$1 \leq j \leq m$$, $$D_{i} f_{j}(x)$$ exists and is continuous at $$a$$. By the previous theorem, $$f_{j}$$ is differentiable at $$a$$, $$J_{f_{j}}(a) = \nabla f_{j}(a)$$. Then, since $$f_{j}$$ is differentiable at f for every $$j$$, we conclude that $$f = (f_{1},\dots,f_{n})$$ is differentiable at $$a$$. Finally, $$J_{f}(a) = [\nabla f_{1}(a), \nabla f_{2}(a),\dots, \nabla f_{n}(a)]'$$.

### Definition (Classes of functions)
We say that $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}^{m}$$ is of class $$C^{k}$$ ($$f \in C^{k}(D)$$) if its $$k$$-th order derivatives exist and are continuous. Similarly, we say that $$f \in C^{\infty}(D)$$ if for every $$k \in \mathbb{N}$$, $$f \in C^{k}(D)$$. If $$f:D\to B$$, we write the definition as $$f \in C^{k}(D,B)$$.

### Theorem (Zero gradient)
Let $$f \in C^{1}(D, \mathbb{R}^{m})$$ with $$D \subseteq \mathbb{R}^{m}$$ open and connected. If $$\nabla f(x) = 0$$ for every $$x \in D$$, then $$f$$ is constant on $$D$$.

***Proof:***  It is enough to prove it for $$m =1$$. Let $$a \in D$$. Since $$D$$ is open, there exists $$\delta > 0$$ such that $$B_{\delta}(a) \subseteq D$$. Let $$x \in B_{\delta}(a)$$. Moreover, by the MVT, there exist $$\xi_{1},\dots,\xi_{n} \in B_{\delta}(a)$$ such that $$f(x)-f(a) = \sum_{j=1}^{n} \underbrace{ \frac{ \partial f }{ \partial x_{j} }(a) }_{ =0 } \cdot (x_{j}-a_{j}) = 0$$. Hence $$f(x) = f(a)$$ for every $$a \in B_{\delta}(a)$$.
Now let $$A = \{ x \in D:f(x) = f(a) \}$$. Note that $$A \neq \emptyset$$ since $$a \in A$$. Let us see that $$A$$ is open. Given $$y \in A$$, there exists $$\delta_{y} > 0$$ with $$f(y) = f(x)$$ for every $$y \in B_{\delta_{y}}(y)$$. Then note that the set $$B=\{ x \in D: f(x)\neq f(a) \} = f^{-1}[(-\infty,a) \cup(a, \infty)]$$ is open, being the preimage under a continuous function of an open set. 
Since $$D = A \cup B$$, $$A \cap B \neq \emptyset$$, but $$D$$ is connected. Then, since $$A \neq \emptyset$$, it follows that $$B = \emptyset$$. Hence $$A = D$$, and therefore $$f$$ is constant on $$D$$.

## Differentiation rules
### Theorem (Differentiation rules)
Given $$f,g:D\subseteq \mathbb{R} \to \mathbb{R}^{m}$$ differentiable at $$a$$:
1. $$D_{f\pm g}(a) = D_{f}(a) \pm D_{g}(a)$$,
2. $$D_{fg}(a) = D_{f}(a) \cdot g(a) + f(a) D_{g}(a)$$,
3. If $$g:D\to \mathbb{R}$$, 


$$
D_{\frac{f}{g}}(a) = \frac{D_{f}(a)g(a)-f(a)D_{g}(a)}{[g(a)]^{2}}.
$$


***Proof:*** Exercise

### Theorem (Chain rule)
Let $$D \subseteq \mathbb{R}^n$$, with $$D$$ a neighbourhood of $$a$$. Suppose that $$f:D \to \mathbb{R}^{m}$$ is differentiable at $$a$$. Let $$E \subseteq \mathbb{R}^{m}$$ be a neighbourhood of $$f(a)$$ and $$G:E \to \mathbb{R}^{p}$$ differentiable at $$f(a)$$. Then $$g \circ f:D \subseteq \mathbb{R}^n\to \mathbb{R}^{p}$$ is differentiable at $$a$$ and moreover $$D_{g \circ f}(a) = D_{g}(f(a)) \cdot D_{f}(a)$$, that is, $$J_{g \circ f} = J_{g}(f(a)) \cdot J_{f}(a)$$.

***Proof:*** We know the following:
1. By differentiability of $$g$$ at $$f(a)$$, given $$\varepsilon>0$$, there exists $$\delta_{1} > 0$$ such that if $$\lVert h_{1} \rVert<\delta_{1}$$, then 


$$
\lVert g(f(a)+h) - g(f(a)) - S(h_{1}) \rVert < \varepsilon \lVert h_{1} \rVert  \quad \text{with }S = D_{g}(f(a)).
$$


2. By continuity of $$f$$ at $$a$$, there exists $$\delta>0$$ such that if $$\lvert h \rvert<\delta$$, then $$\lVert f(a+h) - f(a) \rVert < \delta_{1}$$.T
3. By differentiability of $$f$$, there exists $$\delta_{2}>0$$ such that if $$\lVert h \rVert < \delta_2$$ then $$\lVert f(a+h)-f(a)-T(h) \rVert < \varepsilon \lVert  h \rVert$$ with $$T=D_{f(a)}$$.
4. By linearity of $$T$$, there exists $$M>0$$ such that $$\lVert T(x) \rVert < M \lVert x \rVert$$ for every $$x$$.

We must prove that $$D_{g \circ f}(a) = S$$. Note that 


$$
\begin{aligned}
\lim_{ h \to 0 } &\frac{\lVert (g \circ f)(a+h) - (g \circ f)(a) - S T (h) \rVert }{\lVert h \rVert } \\
\leq &\lim_{ h \to 0 } \underbrace{ \frac{\lVert g(f(a+h)) - g(f(a)) - S_{0}(f(a+h)-f(a))\rVert }{\lVert h \rVert } }_{ A } \\ + &\lim_{ h \to 0 }\underbrace{ \frac{\lVert S(f(a+h)-f(a)) - S(T(h))\rVert }{\lVert h \rVert } }_{ B }.
\end{aligned}
$$


Note that $$B = \left\lVert  S\left( \frac{f(a+h)-f(a) - T(h)}{\lVert  h \rVert} \right)  \right\rVert\underset{h \rightarrow 0}{\longrightarrow} 0$$, since $$S$$ is continuous and the argument tends to zero by differentiability of $$f$$.
For $$A$$, take $$h_{1} = f(a+h)-f(a)$$ in condition (1). Then, for $$h < \tilde{\delta} < \min \{ \delta, \delta_{1},\delta_{2} \}$$, we have that 


$$
\begin{aligned}
\frac{\lVert (g(f(a+h))-g(f(a)) - S(f(a+h)-f(a))  \rVert}{\lVert h \rVert } &<  \frac{\varepsilon \lVert f(a+h) - f(a) \rVert}{\lVert h \rVert } \\
&\leq \frac{\varepsilon \lVert f(a+h) - f(a) - T(h) \rVert + \varepsilon \lVert T(h) \rVert}{\lVert h \rVert } \\
& \leq  \frac{\varepsilon^{2} \lVert h \rVert + M \varepsilon \lVert h \rVert}{\lVert h \rVert } = \varepsilon^{2} + M \varepsilon,
\end{aligned}
$$


from which we conclude that $$A \underset{h \rightarrow 0}{\longrightarrow} 0$$, and hence the result.

### Theorem (Chain rule and partial derivatives)
Let $$g=(g_{1},\dots,g_{m}):\mathbb{R}^n\to \mathbb{R}^{m}$$ be of class $$C^{1}$$ at $$a$$ and $$f:\mathbb{R}^{m}\to \mathbb{R}^{p}$$ of class $$C^{1}$$ at $$g(a)$$. Then $$h = f \circ g:\mathbb{R}^n\to \mathbb{R}^{p}$$ is $$C^{1}$$ at $$a$$. Moreover, for $$i \in \{ 1,\dots,n \}$$, $$j \in \{ 1,\dots,p \}$$ 


$$
\frac{ \partial h_{j} }{ \partial x_{i} }(a) = \sum_{k=1}^{n} \frac{ \partial f_{j} }{ \partial x_{k} } (g(a)) \cdot \frac{ \partial g_{k} }{ \partial x_{i} } (a).
$$


***Proof:*** We know that $$g$$ is differentiable at $$a$$ and $$f$$ is differentiable at $$g(a)$$. So, by the previous theorem, $$h$$ is differentiable at $$a$$ and $$J_{h}(a) =J_{f}(g(a)) J_{g}(a)$$. Hence 


$$
\begin{aligned}
\frac{ \partial h_{j} }{ \partial x_{i} }(a) = (J_{h}(a))_{ji} &= (J_{f}(g(a))J_{g}(a))_{ji}\\
&= \sum_{k=1}^{n} (J_{f}(g(a)))_{jk}(J_{g}(a))_{ki} \\
&= \sum_{k=1}^{n} \frac{ \partial f_{j} }{ \partial x_{k} } (g(a)) \cdot \frac{ \partial g_{k} }{ \partial x_{i} } (a).
\end{aligned}
$$



#### Example 
Let $$f>\mathbb{R}^{2} \to \mathbb{R}$$ be of class $$C^{1}$$ and $$g:\mathbb{R}^{2}\to \mathbb{R}^{2}$$ given by $$g(r, \theta) = (r\cos \theta, r \sin \theta)$$. In this case, $$h = f \circ g:\mathbb{R}^{2}\to \mathbb{R}$$ is $$h(r, \theta) = f(g_{1}, g_{2})$$, with $$g_{1} = r \cos \theta$$ and $$g_{2} = r \cos \theta$$.

In matrix form 


$$
\begin{aligned}
\begin{bmatrix}
\frac{ \partial h }{ \partial r } \frac{ \partial h }{ \partial \theta }  \\
\end{bmatrix} \biggr\rvert_{(r, \theta)}  &= \begin{bmatrix} 
\frac{ \partial f }{ \partial x }  & \frac{ \partial f }{ \partial y }   \\
\end{bmatrix} \biggr\rvert_{(g_{1},g_{2})}  
\begin{bmatrix}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta \\
\end{bmatrix} \\
&= \begin{bmatrix}
\cos \theta \frac{ \partial f }{ \partial x } + \sin \theta \frac{ \partial f }{ \partial y } & -r \sin \theta \frac{ \partial f }{ \partial x } + r \cos \theta \frac{ \partial f }{ \partial y }.
\end{bmatrix}
\end{aligned}
$$


Another way to write it is


$$
D_{1} h(r, \theta) = \cos \theta \cdot D_{1} f(r \cos \theta, r \sin \theta) + \sin \theta \cdot D_{2}f(r \cos \theta, r \sin \theta).
$$


The tree diagram for $$f$$ and $$f_{x}$$ is the following:
![Arbol 1](/assets/img/courses/ma0450/Arbol%201.svg)
The second derivative with respect to $$r$$ is given by 


$$
\begin{aligned}
\frac{ \partial^{2} h }{ \partial r^{2} } &= \frac{ \partial }{ \partial r }\left( \frac{ \partial f }{ \partial x } \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial y } \frac{ \partial g_{2} }{ \partial r }  \right)  \\
&= \frac{ \partial  }{ \partial r }\left( \frac{ \partial f }{ \partial x }  \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial x } \frac{ \partial^{2} g_{1} }{ \partial r^{2} } + \frac{ \partial  }{ \partial r }\left( \frac{ \partial f }{ \partial y }  \right) \frac{ \partial g_{2} }{ \partial r } + \frac{ \partial f }{ \partial y } \frac{ \partial^{2} g_{2} }{ \partial r^{2} } \\
&= \left( f_{xx} \frac{ \partial g_{1} }{ \partial r } + f_{xy} \frac{ \partial g_{2} }{ \partial r }   \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial x } \underbrace{ \frac{ \partial^{2} g_{1} }{ \partial r^{2} } }_{ 0 } \\
&  \quad + \left( f_{yx} \frac{ \partial g_{1} }{ \partial r } 
+ f_{yy} \frac{ \partial g_{2} }{ \partial r }   \right) \frac{ \partial g_{1} }{ \partial r } + \frac{ \partial f }{ \partial y } \underbrace{ \frac{ \partial^{2} g_{2} }{ \partial r^{2} } }_{ 0 } \\
&=f_{xx} \cos^{2} \theta + 2f_{xy} \sin \theta \cos \theta + f_{yy} \sin^{2} \theta \\
&=D_{11}f(r \cos \theta, r\sin \theta) \cos ^{2} \theta+ 2 D_{12} f(r \cos \theta, r \sin \theta) \sin \theta \cos \theta \\
&  \quad+ D_{22} f(r \cos \theta, r \sin \theta) \sin ^{2} \theta
\end{aligned}
$$



#### Example 
Let $$f:\mathbb{R}^{3}\to \mathbb{R}$$, $$g,h: \mathbb{R}^{2}\to \mathbb{R}$$, $$w:\mathbb{R}^{3}\to \mathbb{R}$$ with 


$$
w(x,y,z) = f(g(x,z),h(g(x,z),y),z) = f(u,v,z)
$$


with $$u=g(x,z)$$, $$v=h(r,y)$$ and $$r = g(x,z)$$. If $$h = f \circ g \implies J_{h}(a) = J_{f}(g(a)) \cdot J_{g}(a)$$.
![Arbol 2](/assets/img/courses/ma0450/Arbol%202.svg)
Computing the first-order partial derivatives: 


$$
\begin{aligned}
\frac{ \partial w }{ \partial y } &= \frac{ \partial f }{ \partial v} \cdot \frac{ \partial h }{ \partial y }  \\
\frac{ \partial w }{ \partial x } &= \frac{ \partial f }{ \partial u } \cdot \frac{ \partial g }{ \partial x } +  \frac{ \partial f }{ \partial v } \cdot \frac{ \partial h }{ \partial r } \cdot \frac{ \partial g }{ \partial x } \\
\frac{ \partial w }{ \partial z } &= \frac{ \partial f }{ \partial u } \cdot \frac{ \partial g }{ \partial z }  + \frac{ \partial f }{ \partial v } \cdot \frac{ \partial h }{ \partial r } \cdot \frac{ \partial g }{ \partial z }.
\end{aligned}
$$



## Taylor expansions
A generalisation of Taylor in one variable (MA0350). Let $$f \in C^{n+1}(V)$$, $$V$$ a neighbourhood of $$a$$. Then the Taylor expansion of $$f$$ is given by: 


$$
f(x)  = f(a) + f'(a)(x-a) + \dots \frac{f^{(n)}(a)}{n!}(x-a)^{n} + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n}
$$


with $$\xi$$ between $$x$$ and $$a$$. Can this be generalised to functions of several variables? 

### Theorem (Taylor)
Let $$f:D \to \mathbb{R}$$, $$f \in C^{d+1}(D)$$, $$D \subseteq \mathbb{R}^n$$, $$D$$ open and connected. For $$a \in D$$, there exists $$\delta>0$$ such that for every $$x \in B_{\delta}(a)$$ we have that 


$$
\begin{aligned}
f(x) &= f(a) + \sum_{j=1}^{n} D_{j} f(a) \cdot (x_{j}-a_{j}) + \frac{1}{2!} \sum_{j_{1}=1}^{n} \sum_{j_{2}=1}^{n} D_{j_{1},j_{2}} f(a) (x_{j_{1}} - a_{j_{1}})(x_{j_{2}} - a_{j_{2}}) \\
&+ \frac{1}{3!} \sum_{j_{1},j_{2},j_{3}=1}^{n} D_{j_{1},j_{2}, j_{3}} f(a) (x_{j_{1}} - a_{j_{1}})(x_{j_{2}} - a_{j_{2}})(x_{j_{3}} - a_{j_{3}}) + \dots \\
&+ \frac{1}{d!} \sum_{j_{1},\dots,j_{d} = 1} D_{{j_{1},\dots,j_{d}}}f(a)(x_{j_{1}}-a_{j_{1}})\dots(x_{j_{d}}-a_{j_{d}}) + \\
&+ \frac{1}{(d+1)!} \sum_{j_{1},\dots,j_{d+1} = 1} D_{{j_{1},\dots,j_{d},j_{d+1}}}f(\xi)(x_{j_{1}}-a_{j_{1}})\dots(x_{j_{d}}-a_{j_{d}})(x_{j_{d+1}}-a_{j_{d+1}}),
\end{aligned}
$$


with $$\xi$$ on the segment joining $$a$$ and $$x$$.
#### Note
Define the Hessian of $$f$$ at $$a$$ as the matrix of second derivatives, i.e., 


$$
H_{f}(a) = \begin{pmatrix}
D_{11}f(a) & D_{12}f(a) & \dots & D_{1n}f(a) \\
D_{21}f(a) & D_{22}f(a) & \dots & D_{2n}f(a) \\
\vdots & \vdots & \ddots & \vdots \\
D_{n1}f(a) & D_{n_{2}}f(a) & \dots & D_{nn}f(a) 
\end{pmatrix}_{n \times n}.
$$


This matrix is symmetric if $$f \in C^{2}(D)$$. The second-order term of Taylor's theorem can conveniently be written as 


$$
(x-a)^{T}_{} H_{f}(a) (x-a).
$$



***Proof:*** Let $$a \in D$$. Take $$B_{\delta}(a) \subseteq D$$. For $$x \in B_{\delta}(a)$$, define $$g:[0,1] \to \mathbb{R}$$ with $$g(t) = f(\underbrace{ a+t(x-a) }_{ \in \mathbb{R}^n }) \in \mathbb{R}$$. Intuitively, this function generates any point on the segment between $$a$$ and $$x$$. Note that $$g \in C^{d+1}$$, so Taylor's theorem in one variable applies, and therefore 


$$
g(1) = g(0) + g'(0)t + \frac{g''(0)}{2!}t^{2}+\dots + \frac{g^{(d)}(0)}{d!}t^{d} + \frac{g^{(d+1)}(0)}{(d+1)!}t^{d+1}.
$$


Note now that $$g(1) = f(x), g(0) = f(a)$$. Let $$v_{i} = a_{i}+t(x_{i} - a_{i})$$. Expanding the derivatives with the chain rule


$$
\begin{aligned}
g(t) &= f(a+t(x-a)) = f\big(a_{1}+t(x_{1}-a_{1}), \dots, a_{n}+t(x_{n}-a_{n})\big)\\
\implies g'(t) &= \frac{ \partial f }{ \partial v_{1} } \cdot \frac{ \partial v_{1} }{ \partial t } + \frac{ \partial f }{ \partial v_{2} } \cdot \frac{ \partial v_{2} }{ \partial t } + \dots + \frac{ \partial f }{ \partial v_{n} } \cdot \frac{ \partial v_{n} }{ \partial t }  \\
&= \sum_{j=1}^{n} D_{1}f(v_{1}) (x_{j}-a_{j}) = \sum_{j=1}^{n} D_{1}f(a) (x_{j}-a_{j}).
\end{aligned}
$$


We can proceed in an analogous way, and inductively, for higher-order terms.
Finally, for the remainder take $$\xi= a + \lambda(x-a)$$.

## Maxima and minima
Recall:
1. If $$c \in D^{0}$$ is a relative extremum, $$\nabla f(c) = 0$$.
2. $$f:K \subseteq \mathbb{R}^n \to \mathbb{R}$$, $$K$$ compact. $$f$$ has absolute maximum and minimum.

### Definition (Critical point)
Given $$f:D \subseteq \mathbb{R}^n \to \mathbb{R}$$, we say that $$c$$ is a critical point if $$f$$ is not differentiable at $$c$$ or if $$\nabla f(c) = 0$$. 
#### Note
Recall that being a critical point does not imply being a relative extremum. For example, $$f:\mathbb{R} \to \mathbb{R}$$ with $$f(x)=x^{3}$$ has a critical point at $$0$$ but it is not a relative extremum. Also, $$f:\mathbb{R}^{2} \to \mathbb{R}$$ with $$f(x,y) = x^{2}-y^{2}$$.  One can check that $$\nabla f(0,0) = 0$$ but $$(0,0)$$ is a saddle point. We have $$f(x,0) =x^{2}\geq 0 = f(0,0)$$ and $$f(0,y) = -y^{2} \leq 0 = f(0,0)$$.

### Definition (Maxima, minima and saddle points)
Given $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}$$, with $$A$$ open and $$x_{0} \in A$$:
1. $$f(x_{0})$$ is a local maximum (<font color="#fbd5b5">minimum</font>) on $$A$$ if there exists $$\rho>0$$ such that $$f(x) \leq f(x_{0})$$ <font color="#fbd5b5">(</font>$$f(x_{0}) \leq f(x)$$<font color="#fbd5b5">)</font>
2. The critical point is global if the inequality holds for every $$x \in A$$.
3. $$f(x_{0})$$ is a saddle point if $$\nabla f(x_{0})$$ and for every $$r>0$$ with $$B_{r(x)} \subseteq A$$ there exist $$x_{1}, x_{2} \in B_{r}(x)$$ such that $$f(x_{1}) < f(x_{0}) < f(x_{2})$$.

### Definition (Positive/negative definite and semidefinite matrices)
Let $$A \in \mathbb{R}^{n \times n}$$ be a symmetric matrix. We say that $$A$$ is:
1. positive definite if for every $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax > 0$$;
2. positive semidefinite if for every $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax \geq 0$$;
3. negative definite if for every $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax < 0$$;
4. positive semidefinite if for every $$0 \neq x \in \mathbb{R}^n$$, $$x^{T}Ax \leq 0$$;
5. indefinite if there exist $$0 \neq x_{1},x_{2} \in \mathbb{R}^n$$ such that $$x_{1}^{T}Ax_{1}>0$$ and $$x_{2}^{T} A x_{2} < 0$$.

### Theorem (Hessian test)
Given $$f:D \subseteq \mathbb{R}^n\to \mathbb{R}$$, $$f \in C^{2}(D)$$, define the Hessian matrix as 


$$
H_{f} = \begin{bmatrix}
D_{11}f & \dots &  D_{1n}f  \\
\vdots & \ddots & \vdots \\
D_{n_{1}}f & \dots & D_{nn}g
\end{bmatrix}.
$$


If $$\nabla f(c) = 0$$ ($$c$$ is a critical point), then
1. there is a relative minimum at $$c$$ if $$H_{f}(c)$$ is positive definite;
2. there is a relative maximum at $$c$$ if $$H_{f}(c)$$ is negative definite;
3. there is a relative saddle point at $$c$$ if $$H_{f}(c)$$ is indefinite;
4. otherwise, the test is inconclusive.

***Proof:*** By Taylor's theorem, for $$x \in B_{\delta}(c)$$ with $$\delta>0$$:


$$
\begin{aligned}
f(x) &= f(c) + \nabla f(c) (x-c) + \frac{1}{2} (x-c)^{T} H_{f}(\xi) (x-c)\\
f(x) - f(c) &= \frac{1}{2} (x-c)^{T} H_{f}(\xi) (x-c).
\end{aligned}
$$


Since $$f \in C^{2}(D)$$, by continuity, if $$(x-c)^{T} H_{f}(c)(x-c)>0$$, then there exists $$\alpha > 0$$ such that $$(x-c)^{T} H_{f}(\xi) (x-c) > 0$$ if $$\lVert x-c \rVert < \alpha$$, since $$\xi$$ lies on the segment joining $$c$$ and $$x$$. We conclude that $$f(x) - f(c) > 0$$ for every $$x \in B_{\alpha}(c)$$, from which we conclude that $$f(c)$$ is a relative minimum. (The other cases are analogous.)

### Theorem (Characterisation of definite and semidefinite matrices)
The following are equivalent
1. $$A$$ is positive definite <font color="#fbd5b5">(negative)</font>
2. The eigenvalues of $$A$$ are all positive<font color="#fbd5b5"> (negative)</font>
3. The determinants of the leading principal minors are all positive <font color="#fbd5b5">(they alternate -,+,-,+,...)</font>.
Moreover, the following are equivalent for indefinite matrices
4. $$A$$ is indefinite.
5. $$A$$ has both negative and positive eigenvalues.
 
#### Example 
Consider $$f(x,y) = x^{3}-3xy^{2}+y^{2}$$. First, we find the critical points.

Note that $$\nabla f(x,y) = (3x^{2}-3y^{2}, -6xy+2y) = (0,0)$$


$$
\implies \begin{cases}
x ^{2} = y^{2}  \\
-3xy+y=0
\end{cases}.
$$


We have $$(0,0), \left( \frac{1}{3}, \frac{1}{3} \right), \left( \frac{1}{3}, -\frac{1}{3} \right)$$ as critical points. The Hessian of $$f$$ is 


$$
H_{f}(x,y) = \begin{bmatrix}
6x & -6y \\
-6y & -6x+2
\end{bmatrix}.
$$


Finally, we compute the determinants of the minors in each case: 


$$
\begin{aligned}
H_{f}\left( \frac{1}{3}, \frac{1}{3} \right) &= \begin{bmatrix}
2 & -2 \\
-2 & 0
\end{bmatrix} \implies \Delta_{1} = 2 > 0, \ \Delta_{2} = -4 < 0  \quad \text{(indefinite)}, \\
H_{f}\left( \frac{1}{3}, \frac{-1}{3} \right) &= \begin{bmatrix}
2 & 2 \\
2 & 0
\end{bmatrix} \implies \Delta_{1} = 2 > 0, \ \Delta_{2} = -4 <0  \quad \text{(indefinite)}.
\end{aligned}
$$


For the point $$(0,0)$$, we use the definition of positive semidefinite (since the determinants of the minors are all zero and the test in this form is inconclusive). Note that $$(x,y)H_{f}(0,0) (x,y)^{T} = 2y^{2} \geq 0$$, so $$f(x,y) - f(0,0) \geq 0$$ near $$(0,0)$$ and therefore $$(0,0)$$ is a local minimum.

**See more examples in the class notes**

## Differentiation of inverses and the implicit function theorem

#### Example 
If $$f:\mathbb{R}\to \mathbb{R}$$ is invertible, we know that for $$g=f^{-1}$$, $$g(f(x))= x$$. By the chain rule, $$g'(f(x)) f'(x) = 1$$ and so $$g'(y)=\frac{1}{f'(f^{-1}(y))}$$, where $$y = f^{-1}(x)$$ and $$f'(x) \neq 0$$.

#### Example 
To compute $$g'$$ for $$g(x)=\arcsin x \in \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$$: we know that $$\sin(g(x)) = 1$$ and so $$\cos(g(x)) g'(x) = 1$$. Thus 


$$
g'(x) = \frac{1}{\cos(g(x))} = \frac{1}{\sqrt{ 1 - \sin^{2}(g(x)) }} = \frac{1}{\sqrt{ 1-x^{2} }}.
$$


It is enough to know that $$(\sin x)' = \cos x \neq 0$$ for every $$x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$$ to know that it is locally invertible.

### Theorem (Inverse function theorem)
Let $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}^n$$,  $$f \in C_{1}(A)$$ with $$A$$ open. Let $$a \in A$$ with $$\det J_{f}(a) \neq 0$$. Then:
1. there exist open $$V,W  \subseteq\mathbb{R}^n$$ such that $$a \in V$$, $$f(a) \in W$$ and $$f:V\to W$$ is invertible with $$f^{-1}:W\to V$$ differentiable.
2. $$J_{f^{-1}}(y)= [J_{f}(f^{-1}(y))]^{-1}$$ for every $$y \in W$$.

***Proof:*** Supplementary video

**See examples in the class notes**

### Theorem (Implicit function theorem)
Let $$f:\mathbb{R}^n \times \mathbb{R}^{m} \to \mathbb{R}^{m}$$ be of class $$C_{1}$$ on an open set containing $$(a,b)$$, with $$a \in \mathbb{R}^n$$, $$b \in \mathbb{R}^{m}$$, $$f(a,b)=0$$. Let $$M \in \mathbb{R}^{m \times m}$$ with $$M_{ij} = D_{n+j}f_{i}$$, $$1\leq i,j\leq m$$. If $$\det M(a,b) \neq 0$$, there exist $$A \subseteq \mathbb{R}^n$$, $$B \subseteq \mathbb{R}^{m}$$ with $$a \in A$$, $$b \in B$$ such that 


$$
\forall x \in A  \quad \exists ! y \in B  \quad (f(x,y)=0).
$$


That is, there exists $$g :A\to B$$ with $$f(x, g(x)) = 0$$. Moreover, $$g$$ is differentiable on $$A$$ and $$J_{g}(x) = -[M(x,y)]^{-1}[D_{j}f_{i}]_{1\leq i\leq m, \hspace{1mm} 1\leq j\leq n}$$.

***Idea of the proof:*** 
We can write the Jacobian of $$f$$ as


$$
\begin{aligned}
J_{f} &= \begin{bmatrix} N & M \\
\end{bmatrix}_{m \times (n+m)}, \\ \\
\text{with }N &= \begin{bmatrix} 
D_{1}f_{1} & \dots & D_{n}f_{1} \\
\vdots & \ddots & \vdots \\ 
D_{1}f_{m} & \dots & D_{n}f_{m} \\
\end{bmatrix}_{m \times n} \text{and }
M = \begin{bmatrix} 
D_{n+1}f_{1}  & \dots & D_{n+m} f_{1} \\ 
\vdots & \ddots & \vdots \\
D_{n+1}f_{m} & \dots & D_{n+m}f_{m}
\end{bmatrix}_{m \times m}.
\end{aligned}
$$


Let $$h:\mathbb{R}^n \to \mathbb{R}^{n+m}$$ with $$h(x) = (x,g(x))$$; we have that $$J_{h} = \begin{bmatrix}I_{n\times n} \\ J_{g}\end{bmatrix}$$. Since $$f \circ h = 0$$, we have that 


$$
0 = \begin{bmatrix}
N & M
\end{bmatrix} \begin{bmatrix}
I \\
J_{g}
\end{bmatrix} = N+MJ_{g} \implies J_{g} = -M^{-1}N.
$$


#### Example 
Consider the region defined by $$x^{2}+y^{2} = 1$$. Locally, a function can be defined around any point except $$(-1,0)$$ and $$(1,0)$$, where it is no longer a function since we have two images for the same preimage. We can differentiate implicitly with respect to $$y$$, thinking of $$y = y(x)$$ as a function of $$x$$.

#### Special case 
For $$n=m=1$$, we have $$f:\mathbb{R} \times \mathbb{R} \to \mathbb{R}$$, so $$N = \frac{ \partial f }{ \partial x }$$ and $$M = \frac{ \partial f }{ \partial y }$$. If $$\det\left( \frac{ \partial f }{ \partial y } \right) \neq 0$$, $$\frac{dy}{dx} = -\frac{\frac{ \partial f }{ \partial x }}{\frac{ \partial f }{ \partial y }}$$.

#### Example
Consider $$f(x,y) = \ln x+2\ln y+xy-1$$, $$(a,b)=(1,1)$$. Take $$(a,b)=(1,1)$$. Note that $$f(1,1) = 0$$ and that $$M = \frac{2}{y} + x \implies M(1,1) = 3 \neq 0$$.  By the implicit function theorem, there exist open subsets $$A,B$$ of $$\mathbb{R}$$, with $$1 \in A$$, $$1 \in B$$, such that $$f(x,g(x)) = 0$$.

**See more examples in the class notes**

## Closing remarks

### Directional derivative and gradient

Given $$u \in \mathbb{R}^n$$ with $$\lVert u \rVert_{2} = 1$$, $$f:\mathbb{R}^n\to \mathbb{R}$$, then 


$$
\begin{aligned}
\lvert D_{u} f(x_{0}) \rvert &= \lvert \nabla f(x_{0}) \cdot u \rvert \\
&= \lVert \nabla f(x_{0}) \rVert \cdot \lVert u \rVert \lvert \cos \theta \rvert = \lVert \nabla f(x_{0}) \rVert \cdot \lvert \cos \theta \rvert  \\
&\leq  \lVert \nabla f(x_{0}) \rVert,
\end{aligned}
$$


where $$\theta$$ is the angle between $$\nabla f(x_{0})$$ and $$u$$. If $$u, \nabla f(x_{0})$$ are parallel, equality holds, since $$\theta = 0 \implies \cos \theta = 1$$.

If I take $$u = \frac{\nabla f(x_{0})}{\lVert \nabla f(x_{0} \rVert}$$, then $$D_{u} f(x_{0})$$ is maximal, i.e., $$\nabla f(x_{0})$$ is the direction of greatest vertical change at $$x_{0}$$.

### Higher-order differentials.

Given $$f:A \subseteq \mathbb{R}^n \to \mathbb{R}$$, we define $$D_{f}(x_{0}):\mathbb{R}^n\to \mathbb{R}^{m}$$. So $$D_{f}(x_{0})(h) \in \mathbb{R} \in R$$. We may write $$D_{f}: A \to \mathcal{L}(\mathbb{R}^n, \mathbb{R}^{m})$$. We saw that $$D_{f}(x)$$ has $$J_{f}(x)$$ as its associated matrix. So 


$$
D_{f}(x_{0}) (h) = J_{f}(x_{0}) h = \sum_{i=1}^{n} \frac{ \partial f }{ \partial x_{i} } (x_{0}) h_{i}.
$$


It makes sense to define $$D(D_{f}(x_{0}))$$ if $$f \in C^{2}(A)$$.

If $$x = (x_{1},\dots,x_{n})$$, it is usual to define projections $$dx_{i}:\mathbb{R}^n\to \mathbb{R}$$ with $$dx_{i}(x) = x_{i}$$. So $$D_{f}(x_{0}) = \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}$$. Evaluating, $$D_{f}(x_{0})(h) = \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}(h)$$. So 


$$
\begin{aligned}
\implies D(D_{f}(x_{0})) &= \sum_{j=1}^{n} \frac{ \partial }{ \partial x_{j} }(D_{f}(x_{0})) dx_{j} \\
&= \sum_{j=1}^{n} \frac{ \partial }{ \partial x_{j} } \left( \sum_{i=1}^{n} \frac{ \partial f(x_{0}) }{ \partial x_{i} } dx_{i}(h) \right) dx_{j} \\
&= \sum_{i,j=1}^{n} \frac{ \partial^{2} f }{ \partial x_{j} \partial x_{i} }  dx_{i} dx_{j}, \quad \text{with } dx_{i} dx_{j}: \mathbb{R}^n \times \mathbb{R}^n \\
\implies D_{f}^{2}(x_{0})(u,v) &= \sum_{i,j=1}^{n} \frac{ \partial^{2} f }{ \partial x_{j} \partial x_{i} }(x_{0}) u_{i} v_{j} \quad= u^{T} H v.
\end{aligned}
$$



### Definition (Higher-order differential)
Let $$B_{2}(\mathbb{R}^n,\mathbb{R}) = \{ f:D\to \mathbb{R} \text{ bilinear}\}$$, with $$D = \{ (x,x): x \in \mathbb{R}^n \}$$. Define $$D^{2}f:A \subseteq \mathbb{R}^n \to B_{2}(\mathbb{R}^n, \mathbb{R})$$ by


$$
(D^{2}f(x_{0}))(x) = x^{T} H_{f}(x_{0}) x = \sum_{i,j=1}^{n} x_{i} x_{j} \frac{ \partial f }{ \partial x_{i} \partial x_{j} }.
$$


Analogously, $$D^{3}f:A \subseteq \mathbb{R}^n \to B_{3}(\mathbb{R}^{m}, \mathbb{R})$$ given by 


$$
(D^{2}f(x_{0}))(x) = \sum_{i,j,k=1}^{n} x_{i} x_{j} x_{k} f_{x_{k}x_{j}x_{i}}(x_{0}), 
$$


where $$B_{3}$$ is the set of trilinear functions restricted to $$(x,x,x)$$ with $$x \in \mathbb{R}^n$$.

#### Note 
Taylor can be rewritten as 


$$
f(x) = f(x_{0}) + \sum_{k=1}^{p} \frac{1}{k!} (D^{k}_{f}(x_{0}))(x-x_{0}) + \frac{1}{(p+1)!}(D^{p+1}_{f}(\xi))(x-x_{0}).
$$


**See examples in the notes**
{% endraw %}
