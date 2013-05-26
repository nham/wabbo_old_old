# The Archimedean Property and the Density of the Rationals in $\mathbb{R}$

In this post I prove two crucial properties of the reals.

**The Archimedean Property:** For $x, y \in \mathbb{R}$, there's a $n \in \mathbb{N}$ such that $nx \geq y$.

*Proof:* If not, for all $n \in \mathbb{N}$, $nx < y$. $A = \{nx : n \in \mathbb{N}\}$ being bounded above by $y$ means $c = sup A$ exists. So there's a $m \in \mathbb{N}$ with $c - x < mx < c$. Hence $c < (m + 1)x$, which is a contradiction since $m+1 \in \mathbb{N}$. So $A$ is not bounded above after all. $\Box$


This gives us a tool for proving the next proposition:

**Density of $\mathbb{Q}$ in $\mathbb{R}$:** For all $x, y \in \mathbb{R}$ with $x < y$, there's some $q \in \mathbb{Q}$ such that $x < q < y$.

*Proof:* By AP we can find an $n \in \mathbb{N}$ such that $n(y-x) > 1$, or $\frac{1}{n} < y-x$. Set $A := \{\frac{m}{n} : m \in \mathbb{N}, \frac{m}{n} \leq x\}$. Then $A$ is bounded above, so $c = sup A$ exists, and  hence some $m_0 \in \mathbb{N}$ is such that 1) $\frac{m_0}{n} \leq x$, and 2) $c - \frac{1}{n} < \frac{m_0}{n} \leq c$. 

If $x - \frac{1}{n} \geq \frac{m_0}{n}$, then $x \geq \frac{m_0 + 1}{n} > c$, which is a contradiction since $c$ is an upper bound on $A$. So 

$$x - \frac{1}{n} < \frac{m_0}{n}$$

hence $x < \frac{m_0 + 1}{n}$. We also must have, $\frac{m_0 + 1}{n} \leq x + \frac{1}{n} < y$. So $\frac{m_0 + 1}{n}$ is precisely the droid we're looking for. $\Box$

