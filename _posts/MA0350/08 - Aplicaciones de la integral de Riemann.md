#Mate #MA0350
Fecha: 2025-05-27 

En estas notas se presentan aplicaciones de la [[Integral de Riemann|integral de Riemann]]
## Área bajo la curva

#### Ejemplo 
Hallar el área comprendida entre las curvas $f(x) = 2x$ + $g(x) = x^{3}$. 
***Solución:*** Primero, debemos graficar las funciones. En particular, debemos hallar los límites de integración. Para ello, igualamos ambas funciones:
![[Pasted image 20250527143919.png]]
Note que $x^{3} = 2x \iff x= \pm \sqrt{ 2 } \quad \lor \quad x=0$. Luego, el área entre las curvas viene dada por 
$$
\int_{-\sqrt{ 2 }}^{0}( x^{3}-2x) \, dx + \int_{0}^{\sqrt{ 2 }} (2x-x^{3})  \, dx  = 2.
$$

#### Ejemplo 
Hallar el área entre las curvas $f(x) = x^{3}, g(x) = 2x$, $h(x) = x$ para $0 \leq x \leq \sqrt{ 2 }$.![[Pasted image 20250527144810.png]]Considere la solución de $x^{3} = x \iff x=\pm 1   \lor   x=0$. Luego, el área viene dada por, 
$$
\int_{0}^{1} (2x-x) \, dx + \int_{1}^{\sqrt{ 2 }}  (2x-x^{3})\, dx.
$$

## Longitud de una curva
Sea $f(x) = \sin(x)$. Queremos conocer la longitud de la curva, i.e, cuánto mediría si la estiramos. Podemos aproximar la longitud usando rectángulos y midiendo los segmentos entre los vértices de los rectángulos. La medida de los segmentos viene dada por 
$$
\sqrt{ (f(a_{i+1})-f(a_{i}))^{2} + (a_{i+1}-a_{i})^{2}}.
$$
Además, si $f$ es derivable, por el teorema del valor medio, existe $\xi_{i}$ tal que $f(a_{i+1})-f(a_{i}) = f'(\xi_{i})(a_{i+1}-a_{i})$. Luego, inyectando en la aproximación del segmento, su valor viene dado por 
$$
(a_{i+1}-a_{i}) \sqrt{ (f'(\xi_{i}))^{2} + 1 }.
$$
Sumando todos los intervalos, los segmentos miden 
$$
\sum_{i=0}^{n-1} (a_{i+1}-a_{i}) \sqrt{ (f'(\xi_{i}))^{2} + 1 } = S(\sqrt{ (f')^{2}+1 }, P, \xi_{1},\dots,\xi_{n}). 
$$
Si la suma converge, la longitud de la curva es 
$$
\int_{a}^{b} \sqrt{ (f'(x))^{2} + 1 } \, dx .
$$
La suma converge siempre que $f'$ sea continua.
