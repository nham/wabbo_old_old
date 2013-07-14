# Notes on an abstract(er) approach to linear algebra

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

**Condition for being in the span:** If $S$ is a subset of vector space $V$, then $v \in \text{span}(S)$ iff there is a linear combination $\sum_1^n a_i s_i = v$ of vectors $s_i \in S$. $\Box$

The intersection of any number of subspaces is a subspace. Do we have a similar result for unions of subspaces? The answer is no, but we can take the span to make it into a subspace. The **sum** of a collection $\mathcal{W}$ of subspaces is defined to be $\text{span}(\bigcup \mathcal{W}$. That is, the sum of a collection of subspaces is the smallest subspace containing every subspace. We notate the sum as $+ \mathcal{W}$.

If we stipulate that for every $W \in \mathcal{W}$, $+ \mathcal{W} - W \cap W = \{0\}$, then each $v \in + \mathcal{W}$ must have a unique representation as a linear combination of $v_1, \ldots, v_n$ where $v_i \in W_i \in \mathcal{W}$. Otherwise, we could find a linear combination $\sum_1^n a_i v_i = 0$, where not all $a_i = 0$. Assuming $a_1$ is not zero (we could re-order as necessary), then $v_1 = -\frac{1}{a_1} \Sum_2^n a_i v_i$, so $v_1$ is in both $W_1 and $\mathcal{W} - W_1$.

Upon reflection, it shouldn't be too hard to see that the converse is true as well. So each element in the sum of a collection of subspaces has a unique linear combination yielding that vector iff $+(\mathcal{W} - W)$ and $W$ have only trivial intersection for every subspace $W$ in $\mathcal{W}$. We record this condition in a definition: the sum $+(\mathcal{W})$ is a **direct sum** if it is true.

## Linear dependence and dimension

A linear combination $\sum_1^n a_i v_i$ is called **trivial** if each $a_i = 0$. A subset $S$ in vector space $V$ is called **linearly dependent** if it contains some finite subset $s_1, \ldots, s_n$ (all necessarily distinct) such that some non-trivial linear combination $\sum_1^n a_i s_i = 0$. A subset is **linearly independent** if it is not linearly dependent. That is, $S$ is linearly independent if for every finite subset of $S$, the only linear combination (of necesssarily distinct vectors) that obtains the zero vector is the trivial combination.

Some edge cases for linear dependence: the empty set is linearly independent because there is no finite subset whose non-trivial linear combination obtains 0 (there are no linear combinations at all, because there are no vectors!). There is only one linearly dependent singleton set: $\{0\}$.

**Lemma:** If $v_1, \ldots, v_n$ is a set of (necessarily distinct) linearly dependent vectors with $n \geq 2$, then any vector with a non-zero coefficient in the non-trivial combination obtaining zero is in the span of the others. 

*Proof:* If $v_1, \ldots, v_n$ is linearly dependent, then $\sum_1^n a_i v_i = 0$ for some $a_i$'s not all zero. If $a_i \neq 0$, then 

$$- \frac{1}{a_i}(a_1 v_1 + \ldots + a_{i-1} v_{i-1} + a_{i+1} v_{i+1} + \ldots + a_n v_n = v_i$$

$\Box$

**Corollary:** If $B = \{v_1, \ldots, v_n\}$ is linearly independent but $B \cup \{v\}$ is linearly dependent, then $v \in \text{span}(B)$

*Proof:* $a v + \sum_1^n a_i v_i = 0$ for some $a$ and $a_i$'s not all zero. If $a = 0$ then we have a non-trivial combination of $B$ resulting in zero, which is contrary to assumption. So $a \neq 0$ and hence $v \in \text{span}(B)$. $\Box$

A **basis** for vector space $V$ is a linearly independent set that spans $V$.

**Lemma:** If $S$ is finite and $\text{span}(S) = V$, then a subset of $S$ is a basis for $V$.

*Proof:* If $S$ spans $V$, then if it's linearly independent, we are done. Otherwise it's linearly dependent, so either $S = \{0\}$ (in which case $V$ is the trivial vector space) or there's more than one vector in $S$, which by the preceding lemma one we have $s \in S$ in the span of the others. Hence $S_1 = S - \{s\}$ also spans $V$. Repeat this procedure until we obtain a linearly independent set (which will happen eventually because we started with only finitely many vectors in $S$). $\Box$

**Exchange Lemma:** If $S$ is finite and spans $V$, and $B$ is any linearly independent subset of $V$, then $|B| \leq |S|$.

*Proof:* The following pseudocode illustrates the procedure. We assume $S = \{s_1, \ldots, s_n\}$.

    l := (s_1, ..., s_n)
    for b in B:
        prepend b to l
        remove an x in l that is in the span of the preceding elements of l

We initially order the elements of $S$. Then we prepend the elements of $B$ one at a time. After each prepend, remove the first element that is in the span of the vectors in the tuple that precede it. The trick here is in grouping all the elements of $B$ together, because this means that we will never remove any element of $B$ ($B$ is linearly independent). So in effect, during each iteration we add an element of $B$, then remove an element of $S$.

The result we desire is obtained after realizing that the algorithm cannot terminate early due to running out of elements of $S$ to remove. If that were to happen, i.e. if, after some iteration of the loop, the tuple contains only elements of $B$, but not all elements of $B$, then some proper subset of $B$ spans $V$, which implies that $B$ is not linearly independent. So there must be at least as many vectors in $S$ as there are in $B$. $\Box$

The exchange lemma has an important corollary:

**Dimension:** If $V$ is any vector space with a finite spanning set, then any two bases for $V$ have the same number of elements.

*Proof:* Say $S$ is finite and spans $V$. First we apply a previous lemma to show that some subset $B$ of $S$ is a basis for $V$. Now let $B_1$ be a basis for $V$. Then $B$ is a finite spanning set for $V$ and $B_1$ is linearly independent, so the exchange lemma yields $|B_1| \leq |B|$. This implies $B_1$ is finite, so since it is also a spanning set, and since $B$ is linearly independent, the exchange lemma yields the reverse: $|B| \leq |B_1|$. This proves that every basis has the same number of vectors as $B$. $\Box$

For vector spaces with a finite spanning set, this allows us to make a definition: the **dimension** of said vector space is the (unique) number of vectors in every basis. We shall call any vector space with a finite spanning set a **finite-dimensional vector space**.

We now give a counterpart to the established fact that every spanning set in a finite dimensional vector space can be trimmed to a basis. We have, in fact, established all the parts needed already, we merely need to tie them together.

**You can extend independent sets to a basis:** If $S$ is a linearly independent set in a finite-dimensional vector space $V$, then we can find elements $\{b_1, \ldots, b_k\}$ such that $S \cup \{b_1, \ldots, b_k\}$ is a basis for $V$.

*Proof:* If $S$ spans $V$, we are done. Otherwise, some $v \in V$ is not in the span of $S$, so $S \cup \{v\}$ is linearly independent. Continue this way until we obtain a set that spans $V$ (and hence a basis). This process must eventually terminate, since by the exchange lemma any linearly independent set has less elements than any spanning set, and $V$, being a finite-dimensional vector space, has a (finite) basis $B$. (Hence, once the set in question has as many elements as $B$ has, adding another element gives us a linearly dependent set, so the set spans $V$ and is a basis). $\Box$
