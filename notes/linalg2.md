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

Since each vector space can be considered as a group, linear maps are also group homomorphisms. This leads us to define kernels for vector spaces as we did for groups: the **kernel** of a linear map is the kernel of the map considered as a group homomorphism, i.e. is the set of all elements of $V$ mapping to the additive unit of $W$.

**Kernel is a subspace:** The kernel of a linear map $\phi$ is clearly a subgroup. $\phi(av) = a \phi(v) = a 0 = 0$, so the kernel is closed over scalar multiplication as well. $\Box$.

**Image of a linear map is a subspace:** It's clearly a subgroup, and $c \cdot \phi(v) = \phi(c \cdot v)$ for any $v$, so the image is closed under scalar multiplication also. $\Box$

## Quotient spaces
Recall from group theory that a subgroup is normal iff each left coset is a right coset. Since this latter condition is true for any abelian group, all subgroups of an abelian group are normal. A subspace $W$ is, in part, a subgroup of $V$, hence $W$ is a normal subgroup, and we can define a quotient group on $V$. What's more, the quotient $V/W$ is an abelian group since

$$(u + W) + (v + W) = (u + v) + W = (v + u) + W = (v + W) + (u + W)$$

So the quotient group is abelian as well. Recall that for rings we built *quotient rings*, so our abelian quotient group is not quite sufficient here. We would actually like a quotient vector space. The following definition of scalar multiplication gives us what we want:

$$ a \ast (v + W) := a \cdot v + W$$

Verifying that $(V/W, \mathbb{F}, +, \ast)$ is a vector space is routine.

We are not quite finished, since we would like to prove the *quotient map* assigning $v \mapsto v + W$ is linear. But $(a \cdot u + b \cdot v) + W$ = $a \ast (u + W) + b \ast (v + W)$ is an easy consequence of our definitions, so the quotient map is linear. This establishes (after a little bit of work):

**Subspace induces a quotient space:** If $W$ is a subspace of $V$, then $W$ is the kernel of the quotient map $V \rightarrow V/W$ defined by $v \mapsto v + W$. $\Box$

Of course, if $\phi: V \rightarrow W$ is an existing linear map between vector spaces, then the kernel of $\phi$, call it $N$ gives us a quotient space since $N$ is a subspace. What's more, $f: V/N \rightarrow W$ defined by $v+N \mapsto \phi(v)$ is well-defined and is a linear map. [To prove?]. So analagously to the case for groups, we have

**First isomorphism theorem for vector spaces:** If $\phi: V \rightarrow W$ is a linear map and $N$ is the kernel of $\phi$, then $V/N$ is isomorphic to the image of $\phi$. $\Box$
