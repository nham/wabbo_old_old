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

## Sums of subspaces

**Intersection of subspaces is a subspace:** If $\mathcal{W}$ is a collection of subspaces of vector space $V$, then $\bigcap \mathcal{W}$ is a subspace. $\Box$

For any subset $S$ of vector space $V$, we define the **span of $S$** to be intersection of all subspaces containing $S$. This is a subspace by the previous result, and is in fact the *smallest* subspace containing $S$ by definition.

If $v_1, \ldots, v_n$ are distinct vectors in a vector space $(V, \mathbb{F})$, then a **linear combination** of the vectors is the sum $a_1 \cdot v_1 + \cdots + a_n \cdot v_n$, where each $a_i \in \mathbb{F}$. This is often simply notated $\sum_1^n a_i v_i$.

**Span is the set of all linear combinations:** If $S$ is a subset of vector space $V$, we denote by $L(S)$ the set of all linear combinations of vectors in $S$. Then $\text{span}(S) = L(S)$. $\Box$

The intersection of any number of subspaces is a subspace. Do we have a similar result for unions of subspaces? The answer is no, but we can take the span to make it into a subspace. The **sum** of a collection $\mathcal{W}$ of subspaces is defined to be $\text{span}(\bigcup \mathcal{W}$. That is, the sum of a collection of subspaces is the smallest subspace containing every subspace. We notate the sum as $+ \mathcal{W}$.

If we stipulate that for every $W \in \mathcal{W}$, $+ \mathcal{W} - W \cap W = \{0\}$, then each $v \in + \mathcal{W}$ must have a unique representation as a linear combination of $v_1, \ldots, v_n$ where $v_i \in W_i \in \mathcal{W}$. Otherwise, we could find a linear combination $\sum_1^n a_i v_i = 0$, where not all $a_i = 0$. Assuming $a_1$ is not zero (we could re-order as necessary), then $v_1 = -\frac{1}{a_1} \Sum_2^n a_i v_i$, so $v_1$ is in both $W_1 and $\mathcal{W} - W_1$.

Upon reflection, it shouldn't be too hard to see that the converse is true as well. So each element in the sum of a collection of subspaces has a unique linear combination yielding that vector iff $+(\mathcal{W} - W)$ and $W$ have only trivial intersection for every subspace $W$ in $\mathcal{W}$. We record this condition in a definition: the sum $+(\mathcal{W})$ is a **direct sum** if it is true.
