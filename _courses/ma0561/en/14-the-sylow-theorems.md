---
layout: chapter
course: ma0561
chapter: 14
title: "The Sylow Theorems"
slug: 14-the-sylow-theorems
toc:
  sidebar: right
lang: en
permalink: /notes/ma0561/14-the-sylow-theorems/
---

{% raw %}
## Sylow theorems

### Definition (Sylow subgroup)

Let $$p$$ be a prime and $$G$$ a group. We say that $$H\leq G$$ is a Sylow $$p-$$subgroup if $$\lvert H \rvert = p^{e}$$ and $$p^{e}$$ is the largest power of $$p$$ dividing $$\lvert G \rvert$$.

### Example (Sylow in $$S_{4}$$)

Consider $$S_{4}$$. Note that $$\lvert S_{4} \rvert=4! = 2^{3} \cdot 3$$. A Sylow $$2-$$subgroup has size $$2^{3}$$. A Sylow $$3-$$subgroup has size $$3$$. A Sylow $$5$$-subgroup is $$\{ e \}$$.

### Theorem (First Sylow theorem)

If $$p$$ is prime and $$G$$ is finite, there exists a Sylow $$p-$$subgroup.

***Proof:*** Let $$\lvert G \rvert = p^{e}k$$ be such that $$p \not\mid k$$. Let $$\Omega:=\{ T \subseteq G: \lvert T \rvert=p^{e} \}$$. Consider the action $$\alpha$$ of $$G$$ on $$\Omega$$ such that $$\alpha _g(T) = gT$$. (it is left as an exercise to check that it is an action). We have that $$\lvert \Omega \rvert = \binom{p^{e}k}{p^{e}} \equiv k \mod p$$. Since $$p$$ does not divide $$k$$, we have that $$p\ \not\mid \Omega$$. We know that

$$
\Omega = \dot{\bigcup}_{i \in I} \mathcal{O}_{i},
$$

where the $$\mathcal{O}_{i}$$ are the distinct orbits. Hence $$\lvert \Omega \rvert = \sum_{i \in I} \lvert \mathcal{O}_{i} \rvert$$. Therefore, there exists an orbit $$\mathcal{O}_{i}$$ such that $$p \not\mid \lvert \mathcal{O}_{i} \rvert$$. Hence, there exists $$H \in \Omega$$ such that $$p \not\mid \mathcal{O}_{H}$$ (taking $$H$$ as a representative of the class of $$\mathcal{O}_{i}$$) . We have that $$\lvert \mathcal{O}_{H} \rvert = [G:G_{H}] = \frac{\lvert G \rvert}{\lvert G_{H} \rvert} = \frac{p^{e}k}{\lvert G_{H}. \rvert}$$ From this, we have that $$\lvert \mathcal{O}_{H} \rvert \mid p^{e}k \implies \lvert \mathcal{O}_{H} \rvert \mid k$$. Let $$A = \bigcup_{T \in \mathcal{O}_{H}} T = \bigcup_{g \in G} gH$$. We shall prove that $$G=A$$. It is clear that $$A \subseteq G$$.
We shall first show that $$A$$ is stable under left translations. Let $$g \in G$$, $$T \in \mathcal{O}_{H}$$. We must show that $$gA \subseteq A$$. Given $$x \in A$$, there exists $$T \in \mathcal{O}_{H}$$ such that $$x \in T$$ and therefore $$gx \in gT \subseteq A$$, from which the result follows. Finally, take $$h_{0} \in H$$ (it exists since $$H \neq \emptyset$$); then $$1_{G} \in h_{0}^{-1}H \in \mathcal{O}_{H}$$, so that $$1_{G} \in A$$. Given any $$g \in G$$, stability under translations gives $$g = g \cdot 1_{G} \in gA \subseteq A$$. Conclude that $$G \subseteq A$$ and therefore $$G=A$$. Thus, we have that

$$
p^{e}k = \lvert G \rvert = \lvert A \rvert =\left\lvert  \bigcup_{T \in \mathcal{O}_{H}}T  \right\rvert \leq \sum_{T \in \mathcal{O}_{H}}  \lvert T \rvert = \lvert \mathcal{O}_{H} \rvert \cdot \lvert T \rvert = \lvert \mathcal{O}_{H} \rvert \cdot p^{e},
$$

and therefore $$k\leq \lvert \mathcal{O}_{H} \rvert$$. But $$\lvert \mathcal{O}_{H} \rvert \mid k$$, whence $$\lvert \mathcal{O}_{H} \rvert = k$$. Finally, since

$$
\lvert \mathcal{O}_{H} \rvert \cdot \lvert G_{H} \rvert = p^{e} \cdot k \implies \lvert G_{H} \rvert = \frac{p^{e}k}{k} = p^{e}.
$$

Thus, $$\lvert G_{H} \rvert = p^{e}$$ and it is a group.

### Theorem (Second Sylow theorem)

Let $$G$$ be a finite group and $$p$$ prime. If $$P$$ and $$Q$$ are Sylow $$p-$$groups, then they are conjugate, i.e., there exists $$g \in G$$ such that $$gPg^{-1} = Q$$.

***Proof:*** Exercise.
**Hint:** Consider the action $$\alpha:P \times G / Q \to G / Q$$ such that $$\alpha_{g}(hQ) = ghQ$$.

### Theorem (Third Sylow theorem)

Let $$G$$ be finite and $$p$$ prime and $$n_{p}$$ the number of Sylow $$p-$$groups. Then $$p \mid n_{p}-1$$.

***Proof:*** **Hint:** Define $$\Lambda_{p}: \{ H \subseteq G: H \text{ is a Sylow }p-\text{subgroup} \}$$. Consider the action $$\alpha: G \times\Lambda_{p} \to \Lambda_{p}$$ such that $$\alpha_{g}(P) = gPg^{-1}$$.
{% endraw %}
