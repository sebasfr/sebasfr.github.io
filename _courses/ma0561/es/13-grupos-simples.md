---
layout: chapter
course: ma0561
chapter: 13
title: "Grupos simples"
slug: 13-grupos-simples
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/13-grupos-simples/
---

{% raw %}
## Grupos Simples

### Definición (Grupo simple)

Sea $$G$$ un grupo no trivial. Decimos que $$G$$ es simple si no tiene subgrupos normales propios, i.e., si $$H \triangleleft G$$, entonces $$H = \{ 1_{G} \}$$ o $$H=G$$.

### Teorema (Abelianos simples son $$\mathbb{Z}_{p}$$)

Sea $$G$$ un grupo abeliano. Entonces $$G$$ es simple si y solo si $$G=\mathbb{Z}_{p}$$ con $$p$$ primo.

***Prueba:*** ($$\impliedby$$): Esta dirección es sencilla, pues basta aplicar Lagrange para notar que $$G$$ no tiene subgrupos propios.
($$\implies$$): Como $$G$$ es abeliano, todo subgrupo es normal. Además, como $$G$$ es simple, $$G \neq \{ 1_{G} \}$$. Entonces, existe $$x \in G$$ tal que $$(x \neq 1_{G})$$. Tenemos que

$$
\langle x \rangle \triangleleft  G \implies \langle x \rangle = G \implies G \text{ es cíclico} \implies G \cong \mathbb{Z} \quad \lor \quad G \cong   \mathbb{Z}_{n}, \text{ para algún } n \in \mathbb{N}.
$$

Como $$G$$ es simple, $$G \not\cong \mathbb{Z}$$, por lo que $$G \cong \mathbb{Z}_{n}$$ para algún $$n \in  \mathbb{N}$$. Además, como $$G$$ es simple, $$n$$ es primo, de donde concluimos el resultado.

### Recordatorio (Signo y grupo alternante)

Si $$\sigma \in S_{n}$$ tal que $$\sigma = \beta_{1} \cdots \beta_{t}$$ es su descomposición en ciclos disjuntos de $$\sigma$$, entonces, $$\operatorname{sgn}( \sigma ) := (-1)^{n-t}$$. Si $$\operatorname{sgn}( \sigma ) = 1$$ decimos que $$\sigma$$ es par y $$A_{n} = \{ \sigma \in S_{n}, \sigma \text{ es par} \}.$$

### Ejercicios (Sobre $$3$$-ciclos)

1. $$A_{n}$$ es generado por los 3-ciclos si $$n\geq {5}$$.
2. En $$S_{5}$$, todos los 3-ciclos son conjugados.
3. En $$A_{5}$$, todos los 3-ciclos son conjugados.

### Teorema ($$A_{5}$$ es simple)

$$A_{5}$$ es simple

***Prueba:*** Sea $$H \neq \{ \mathrm{id}_{S_{5}} \}$$ tal que $$H \triangleleft A_{5}$$. Por los ejercicios anteriores, basta mostrar que $$H$$ contiene un 3-ciclo, pues si $$\sigma \in H$$ es un 3-ciclo, $$\sigma^{A_{5}} \subseteq H$$ pues $$H \triangleleft A_{5}$$, entonces $$\langle \sigma^{A_{5}}  \rangle = \{ \tau: \tau \text{ es 3-ciclo}  \} \subseteq H$$ y por tanto $$H = A_{5}$$.

¿Cuántas configuraciones posibles tengo para la descomposición en ciclos disjuntos?

1. $$\sigma$$ se descompone en 5 1-ciclos, y por tanto $$\sigma \in A_{5}$$.
2. $$\sigma$$ se descompone en un 2-ciclo y 3 1-ciclos, y por tanto $$\sigma \not\in A_{5}$$.
3. $$\sigma$$ se descompone en un 3-ciclo y 2 1-ciclos, y por tanto $$\sigma \in A_{5}$$.
4. $$\sigma$$ se descompone en un 4-ciclo y 1 1-ciclo, y por tanto $$\sigma \not\in A_{5}$$.
5. $$\sigma$$ se descompone en un 5-ciclo, y por tanto $$\sigma \in A_{5}$$.
6. $$\sigma$$ se descompone en dos 2-ciclos y un 1-ciclo, y por tanto $$\sigma \in A_{5}$$.
7. $$\sigma$$ se descompone en un 3-ciclo y un 2-ciclo, y por tanto $$\sigma \not\in A_{5}$$.

Luego, si $$\sigma \in H \setminus \{ 1_{G} \}$$, su factorización es del tipo 3, 5 o 6. Si $$\sigma$$ es del tipo 3, entonces posee un 3-ciclo y por tanto se cumple el resultado.
SI $$\sigma$$ es del tipo 5, suponga sin pérdida de generalidad que $$\sigma = \begin{pmatrix}1 & 2 & 3 & 4 & 5\end{pmatrix}$$. Sea $$\alpha = \begin{pmatrix}1 & 2 & 3\end{pmatrix} \in A_{5}$$. Luego,

$$
w = \begin{pmatrix}
2 & 3 & 1 & 4 & 5
\end{pmatrix} =\alpha \sigma \alpha^{-1} \in H, \text{ pues }H \triangleleft A_{5} \implies w \sigma ^{-1} = \begin{pmatrix}
1 & 2 & 4
\end{pmatrix} \in H.
$$

Si $$\sigma$$ es del tipo 6, suponga sin pérdida de generalidad que $$\sigma = \begin{pmatrix}1 & 2\end{pmatrix}\begin{pmatrix}3 & 4\end{pmatrix}$$. Sea $$\beta = \begin{pmatrix}3 & 4 & 5\end{pmatrix} \in A_{5}$$. Note que $$\delta :=\beta \sigma \beta ^{-1} = \begin{pmatrix}1 & 2\end{pmatrix}\begin{pmatrix}4 & 5\end{pmatrix} \in H$$. Finalmente, $$\sigma \cdot \delta = \begin{pmatrix}3 & 4 & 5\end{pmatrix} \in H$$.
Concluya que $$A_{5}$$ es simple.

### Teorema ($$A_{6}$$ es simple)

$$A_{6}$$ es simple

***Prueba:*** Sea $$H\neq \{ \mathrm{id}_{S_{6}} \}$$ tal que $$H \triangleleft A_{6}$$. Suponga por contradicción que si $$\sigma \in H \setminus \{ \mathrm{id}_{S_{6}} \}$$, entonces $$\sigma$$ mueve todo elemento de $$\{ 1,2,\dots,6 \}$$. ¿Cuántas configuraciones posibles tengo para la descomposición en ciclos disjuntos?

1. $$\sigma$$ se descompone en tres 2-ciclos, y por tanto $$\sigma \not\in A_{6}$$.
2. $$\sigma$$ se descompone en un 2-ciclo y un 4-ciclo, y por tanto $$\sigma \in A_{6}$$.
3. $$\sigma$$ se descompone en dos 3-ciclos, y por tanto $$\sigma \in A_{6}$$.

Si $$\sigma$$ es del tipo 2, considere $$\sigma = \begin{pmatrix}1 & 2\end{pmatrix}\begin{pmatrix}3 & 4 & 5 & 6\end{pmatrix}$$. Como $$H$$ es subgrupo, si $$\sigma \in H$$, $$\sigma^{2} \in H$$. Pero $$\sigma^{2}(1) = 1$$, una contradicción.
Por otro lado, si $$\sigma$$ es del tipo 3, considere $$\sigma=\begin{pmatrix}1 & 2 & 3\end{pmatrix}\begin{pmatrix}4 & 5 & 6\end{pmatrix}$$. Luego, tenemos que $$\sigma ^{-1} = \begin{pmatrix}3 & 2 & 1\end{pmatrix}\begin{pmatrix}6 & 5 & 4\end{pmatrix}$$. Sea $$\gamma = \begin{pmatrix}2 & 3 & 4\end{pmatrix}$$. Como $$H$$ es subgrupo, tenemos que $$\sigma\gamma \sigma ^{-1} \gamma ^{-1} = \begin{pmatrix}1 & 5 & 3 & 2 & 4\end{pmatrix} \in H$$, una contradicción.
Concluya que existen $$\sigma \in H$$ y $$i \in \{ 1,\dots,6 \}$$ tales que $$\sigma(i) = i$$. Sea $$F = \{ \sigma \in A_{6}: \sigma(i)=i \}$$. Note que, $$F \neq \{ 1_{S_{6}} \}$$ y $$F \cap H \neq \{ 1_{S_{6}} \}$$. Es fácil ver que $$F \cong A_{5}$$. Finalmente, como $$F \cap H \triangleleft F \cong A_{5}$$ y $$A_{5}$$ es simple, tenemos que $$F \cap H = F$$, de donde $$F \subseteq H$$. Concluya que $$A_{6}$$ es simple porque contiene un 3-ciclo.

### Teorema ($$A_{n}$$ es simple para $$n \geq 5$$)

$$A_{n}$$ es simple para $$n \geq5$$

***Prueba:*** Considere el caso para $$n>6$$. Sea $$H\neq \{ \mathrm{id}_{S_{n}} \}$$ tal que $$H \triangleleft A_{n}$$ Sea $$\sigma \in H \setminus \{ \mathrm{id}_{Sn} \}$$. Entonces, existe $$i \in \{ 1,\dots,n \}$$ tal que $$\sigma(i) = j \neq i$$. Sea $$\alpha$$ un 3-ciclo tal que $$\alpha(i)=i$$ y $$\alpha(j)\neq j$$. Note que

$$
\alpha(\sigma(i)) = \alpha(j) \neq  j  \quad \land  \quad\sigma(\alpha(i)) = \sigma(i) =j \implies \alpha \sigma \neq \sigma\alpha \implies \alpha\sigma\alpha ^{-1}\sigma ^{-1} \in H \setminus \{1_{S+n}\}.
$$

Sabemos que la conjugación de permutaciones no me cambia la estructura de ciclos. Luego $$\sigma \alpha ^{-1} \sigma ^{-1}$$ es un 3-ciclo y $$\gamma = \alpha\sigma\alpha ^{-1}\sigma ^{-1} \in H$$ es un producto de dos 3-ciclos y por tanto mueve a lo sumo 6 elementos. Sean $$i_{1},\dots i_{k}$$, con $$k \leq 6$$, los elementos que mueve $$\gamma$$. Ahora, sea $$F:=\{ \sigma \in A_{n}: \sigma(\ell) = \ell  \quad \forall \ell \not\in \{ i_{1},\dots,i_{k} \}\}$$. Es fácil ver que $$F \cong S_{6}$$. y $$F \cap H \neq \{ 1_{S_{n}} \}$$. Así, $$F \cap H \triangleleft F \cong A_{6}$$, por lo que $$F \cap H = F$$ y por tanto $$F \subseteq H$$. En particiular, $$\begin{pmatrix}i_{1} & i_{2} & i_{3}\end{pmatrix} \in F \subseteq H$$, de donde concluimos que es simple porque contiene un $$3-$$ciclo..
{% endraw %}
