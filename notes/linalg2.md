# Notes on Herstein's linear algebra presentation.

A **vector space** is a quadruple $(V, \mathbb{F}, +, \cdot)$ such that $(V, +)$ is an abelian group, $\cdot$ is a function $\mathbb{F} \ times V \rightarrow V$ such that $

 - $(a+b) \cdot u = a \cdot u + b \cdot u$
 - $a\cdot(u + v) = a \cdot u + a \cdot v$
 - $(ab) \cdot u = a \cdot (b \cdot v)$
 - $1 \cdot u = u$


**Scaling by zero or scaling the zero vector:** For all $v \in V$, $0 \cdot v = 0 \cdot v + 0 \cdot v$, so $0 \cdot v = 0$. Also $a \cdot 0 = a \cdot 0 + a \cdot 0$ so $a \cdot 0 = 0$ for all $a \in \mathbb{F}$ $\Box$.

**Lemma:** $-1 \cdot v = -v$. Also, $(-a) \cdot v = - (a \cdot v)$.

*Proof:* Since $(V, +)$ is a group, $u + v = 0$ has a unique solution. $-1 \cdot v$ is such a solution, by distributivity. Now $(-a) \cdot v = (-1 a) \cdot v = -1 \cdot (a \cdot v) = -(a \cdot v)$ $\Box$

A **subspace** of a vector space $V$ is a subset $W$ of $V$ which is a vector space when the binary operations of vector addition and scalar multiplication are restricted to $W$.

**Lemma:** A subset $W$ of $V$ is a subspace iff $W$ is closed under vector addition and scalar multiplication. $\Box$

A **vector space homomorphism**, also called a **linear map** or **linear transformation**, is a function $T: V \rightarrow W$ where $V$ and $W$ are both vector spaces over the same field $\mathbb{F}$, such that: 

 - $T(u + v) = T(u) + T(v)$
 - $T(a \cdot v) = a \cdot T(v)$
