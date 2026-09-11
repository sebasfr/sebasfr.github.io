---
layout: chapter
course: ma0561
chapter: 14
title: "Teoremas de Sylow"
slug: 14-teoremas-de-sylow
toc:
  sidebar: right
lang: es
permalink: /notes/ma0561/es/14-teoremas-de-sylow/
---

{% raw %}
## Teoremas de Sylow

### Definición (Subgrupo de Sylow)

Sea $$p$$ un primo y $$G$$ un grupo. Decimos que $$H\leq G$$ es un $$p-$$subgrupo de Sylow si $$\lvert H \rvert = p^{e}$$ y $$p^{e}$$ es la mayor potencia de $$p$$ que divide a $$\lvert G \rvert$$.

### Ejemplo (Sylow en $$S_{4}$$)

Considere $$S_{4}$$. Note que $$\lvert S_{4} \rvert=4! = 2^{3} \cdot 3$$. Un $$2-$$subgrupo de Sylow tiene tamaño $$2^{3}$$. Un $$3-$$subgrupo de Sylow tiene tamaño $$3$$. Un $$5$$-subgrupo de Sylow es $$\{ e \}$$.

### Teorema (Primer teorema de Sylow)

Si $$p$$ es primo y $$G$$ es finito, existe un $$p-$$subgrupo de Sylow.

***Prueba:*** Sea $$\lvert G \rvert = p^{e}k$$ tal que $$p \not\mid k$$. Sea $$\Omega:=\{ T \subseteq G: \lvert T \rvert=p^{e} \}$$. Considere la acción $$\alpha$$ de $$G$$ en $$\Omega$$ tal que $$\alpha _g(T) = gT$$. (queda como ejercicio ver que es una acción). Tenemos que $$\lvert \Omega \rvert = \binom{p^{e}k}{p^{e}} \equiv k \mod p$$. Como $$p$$ no divide a $$k$$, tenemos que $$p\ \not\mid \Omega$$. Sabemos que

$$
\Omega = \dot{\bigcup}_{i \in I} \mathcal{O}_{i},
$$

donde $$\mathcal{O}_{i}$$ son las órbitas distintas. Luego $$\lvert \Omega \rvert = \sum_{i \in I} \lvert \mathcal{O}_{i} \rvert$$. Por lo tanto, existe una órbita $$\mathcal{O}_{i}$$ tal que $$p \not\mid \lvert \mathcal{O}_{i} \rvert$$. Luego, existe $$H \in \Omega$$ tal que $$p \not\mid \mathcal{O}_{H}$$ (tomando $$H$$ como un representante de la clase de $$\mathcal{O}_{i}$$) . Tenemos que $$\lvert \mathcal{O}_{H} \rvert = [G:G_{H}] = \frac{\lvert G \rvert}{\lvert G_{H} \rvert} = \frac{p^{e}k}{\lvert G_{H}. \rvert}$$ De aquí, tenemos que $$\lvert \mathcal{O}_{H} \rvert \mid p^{e}k \implies \lvert \mathcal{O}_{H} \rvert \mid k$$. Sea $$A = \bigcup_{T \in \mathcal{O}_{H}} T = \bigcup_{g \in G} gH$$. Probaremos que $$G=A$$. Es claro que $$A \subseteq G$$.
Vamos a mostrar primero que $$A$$ es estable por traslaciones izquierdas. Sea $$g \in G$$, $$T \in \mathcal{O}_{H}$$. Hay que mostrar que $$gA \subseteq A$$. Dado $$x \in A$$, existe $$T \in \mathcal{O}_{H}$$ tal que $$x \in T$$ y por tanto, $$gx \in gT \subseteq A$$, de donde concluimos el resultado. Finalmente, tome $$h_{0} \in H$$ (existe pues $$H \neq \emptyset$$); entonces $$1_{G} \in h_{0}^{-1}H \in \mathcal{O}_{H}$$, de modo que $$1_{G} \in A$$. Dado cualquier $$g \in G$$, la estabilidad por traslaciones da $$g = g \cdot 1_{G} \in gA \subseteq A$$. Concluya que $$G \subseteq A$$ y por tanto $$G=A$$. Así, tenemos que

$$
p^{e}k = \lvert G \rvert = \lvert A \rvert =\left\lvert  \bigcup_{T \in \mathcal{O}_{H}}T  \right\rvert \leq \sum_{T \in \mathcal{O}_{H}}  \lvert T \rvert = \lvert \mathcal{O}_{H} \rvert \cdot \lvert T \rvert = \lvert \mathcal{O}_{H} \rvert \cdot p^{e},
$$

y por tanto, $$k\leq \lvert \mathcal{O}_{H} \rvert$$. Pero $$\lvert \mathcal{O}_{H} \rvert \mid k$$, de donde $$\lvert \mathcal{O}_{H} \rvert = k$$. Finalmente, como

$$
\lvert \mathcal{O}_{H} \rvert \cdot \lvert G_{H} \rvert = p^{e} \cdot k \implies \lvert G_{H} \rvert = \frac{p^{e}k}{k} = p^{e}.
$$

Así, $$\lvert G_{H} \rvert = p^{e}$$ y es un grupo.

### Teorema (Segundo teorema de Sylow)

Sea $$G$$ un grupo finito y $$p$$ primo. Si $$P$$ y $$Q$$ son $$p-$$grupos de Sylow, entonces son conjugados, i.e., existe $$g \in G$$ tal que $$gPg^{-1} = Q$$.

***Prueba:*** Ejercicio.
**Sugerencia:** Considere la acción $$\alpha:P \times G / Q \to G / Q$$ tal que $$\alpha_{g}(hQ) = ghQ$$.

### Teorema (Tercer teorema de Sylow)

Sea $$G$$ finito y $$p$$ primo y $$n_{p}$$ el número de $$p-$$grupos de Sylow. Entonces $$p \mid n_{p}-1$$.

***Prueba:*** **Sugerencia:** Definir $$\Lambda_{p}: \{ H \subseteq G: H \text{ es un }p-\text{subgrupo de Sylow} \}$$. Considerar la acción $$\alpha: G \times\Lambda_{p} \to \Lambda_{p}$$ tal que $$\alpha_{g}(P) = gPg^{-1}$$.
{% endraw %}
