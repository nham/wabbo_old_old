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

It's a bit easier to understand sums by taking a look at where the union of subspaces fails to be a subspace. It's actually closed under scalar multiplication: if $v \in \bigcup \mathcal{W}$, then $v \in W \in \mathcal{W}$, so clearly any $av \in \bigcup \mathcal{W}$ as well. Similarly, taking two vectors from a single subspace in $\mathcal{W}$, we can (obviously) add them to get another vector in the subspace. The problem is when we take two vectors from *different subspaces*. So the sum of a collection of subspaces can perhaps be thought of as what happens to the unions after you close it under addition of vectors from different subspaces.

Can we formalize that idea? Maybe?

**Necessary & sufficient condition for being in the sum:** $v \in + \mathcal{W}$ iff $v = m_{i_1} + \cdots + m_{i_k}$ for $m_{i_j} \in W_{i_j} \in \mathcal{W}$

*Proof:* Clearly any sum of elements from subspaces of $\mathcal{W}$ is in the sum. Conversely, if $v$ is in the sum, $v$ is a linear combination of vectors drawn from $\bigcup \mathcal{W}$. Say, $v = \sum_1^n a_i u_i$. Group together the vectors that are in the subspaces of $\mathcal{W}$ to obtain your sum $v = \sum_1^t m_{i_k}$ of vectors, each from a subspace in $\mathcal{W}$. $\Box$


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

**Corollary:** If $M$ is a subspace of finite-dimensional $V$, then a basis for $M$ can be extended to a basis for $V$.


**Maximal independent sets, minimal spanning sets:**If $V$ is finite-dimensional, then $S \subseteq V$ is a basis iff $S$ is a maximal linearly independent set (i.e. if adding any vector makes it not LI) iff $S$ is a minimal spanning set (i.e. if removing any element in $S$ makes it not span).

*Proof:* If $S$ is a basis, then it spans $V$, so $S \cup \{v\}$ for $v \notin S$ is a linearly dependent set (let the coefficients of $S$ be such to give $v$, and let coefficient of $v$ be $-1$). So $S$ is a maximal linearly independent set.

If $S$ is a maximal linearly independent set, adding any element (not already in $S$) to $S$ makes it dependent, so by a previous lemma every element not in $S$ is in the span of $S$. That is, $S$ spans $V$. It must be a minimal spanning set as well, since if any proper subset of $S$ spanned $V$, then one of the elements of $S$ not in that subset would be in the span of the subset, implying $S$ is not linearly independent.

Finally, if $S$ is a minimal spanning set, removing any element from $S$ results in a set that does not span. If any $x \in S$ is such that $x \in \text{span}(S - x)$, then $\text{span} S = \text{span}(S - x)$, so $S - x$ would still span $V$. Since that is not true for any $x \in S$, no $x$ is in the span of the other elements. Hence $S$ is not linearly dependent (if it were, one of the elements would be in the span of the others). So $S$ is linearly independent, and hence $S$ is a basis. $\Box$


**Lemma:** If $M$, $N$ are finite dimensional subspaces of some vector space, then $M \subseteq N$ implies 

 1. $dim M \leq dim N$.
 2. if $dim M = dim N$ then $M = N$

*Proof:* Since $M \subseteq N$, $M$ is also a subspace of $N$, so a basis $B$ of $M$ is linearly independent in $N$. By the exchange lemma, $dim M = |B| \leq dim N$. If the dimensions of $M$ and $N$ are the same, any basis for $M$ is linearly independent in $N$, and is maximal by the exchange lemma, so $M = N$. $\Box$

**Sum/intersection dimension theorem:** If $M$, $N$ are finite dimensional subspaces of some vector space, then $M \cap N$ and $M+N$ are finite dimensional as well and

$$dim M+N + dim M \cap N = dim M + dim N$$

*Proof:* $M \cap N$ is a subspace of $M$ and $N$, which are subspaces of $M+N$. Let $[b]$ be a basis of $M \cap N$, $[b] + [c]$ and $[b] + [d]$ are bases for $M$ and $N$, respectively since $[b]$ can be extended to bases for $M$ and $N$. The claim is that $[b] + [c] + [d]$ is a basis for $M+N$. Let 

$$ \alpha_i [b] + \beta_i [c] + \gamma_i [d]$$

be a linear combination of $[b] + [c] + [d]$ yielding 0. Then

$$\alpha_i [b] + \beta_i [c] = - \gamma_i [d] = v$$

so $v \in M \cap N$. This means $v$ is a linear combination of $[b]$ as well, so all $\gamma_i$'s must be zero (else $[b] + [d]$ fails to be independent). Now we have

$$\alpha_i [b] = - \beta_i [c] $$

So we have all coefficients zero because $[b] + [c]$ is independent. So $[b] + [c] + [d]$ is linearly independent in $M+N$. To prove that $[b] + [c] + [d]$ spans, we need only note that $M+N$ can be characterized as all the linear combinations of vectors from $M \cup N$ and that $[b] + [c] + [d]$ contains bases for both $M$ and $N$. $\Box$.

## Coordinate systems

First, we need to know that the set $\mathbb{F}^n$ of all n-tuples of a field $\mathbb{F}$ can be made into a vector space. Hopefully you've seen it. $\mathbb{F}^n$ has a **standard basis** of $\{\epsilon_j = (\epsilon_j1, \ldots, \epsilon_jn) : j \in [n]\}$ where $\epsilon_ij = 1$ if $i = j$ and $0$ otherwise. This is called the **standard basis** of $\mathbb{F}^n$. It should be easy to see that it is, in fact, a basis.

There is a natural ordering to the elements of the standard basis: $(\epsilon_1, \ldots, \epsilon_n)$ (recall that each $\epsilon_i$ is an $n$-tuple of elements of $\mathbb{F}$). Without motivating the generalization, we shall consider what happens when we introduce such an ordering on any basis of a vector space. Call a tuple of basis elements an **ordered basis**. We have implicitly used this idea multiple times in the development so far.

Ordered bases have an essential property:

**Unique representations within bases:** If $B = (b_1, \ldots, b_n)$ is a basis for some vector space $V$ and $v \in V$, then there is a unique tuple $(a_1, \ldots, a_n \in \mathbb{F}^n$ such that $\sum_1^n a_i b_i = v$.

*Proof:* If there's more than one, set them equal to each other and subtract one from both sides. This is a non-trivial combination that yields zero, contrary to $B$ being linearly independent. $\Box$

**Lemma:** If $T: V \rightarrow W$ is a linear map for finite-dimensional $V$, and $B = (u_1, \ldots, u_n)$ is a basis for $V$, then the image of $B$ is a spanning set for the image of $T$. If $T$ is injective, then the image of $B$ is a basis for the image of $T$.

*Proof:* For $w \in \text{img} T$, $w = T(v) = T(\sum_1^n a_i u_i) = \sum_1^n a_i T(u_i)$. If $T$ is injective, the set of $T(u_i)$'s must be linearly independent (if the kernel of $T$ contains anything but zero, injectivity will fail). $\Box$

For a linear map $T$ originating from a finite-dimensional space $V$, then (by linearity) entire map is determined once you specify where the basis elements of $V$ are mapped to. We use this fact to create an isomorphism between any two n-dimensional vector spaces.

If $V$ and $W$ are vector spaces of dimension $n$ and $B = (b_1, \ldots, b_n)$, $C = (c_1, \ldots, c_n)$ are ordered bases for $V$ and $W$, respectively, then if we stipulate that $T: V \rightarrow W$ is linear, we can make $T$ into an isomorphism by mapping each $b_i$ to $c_i$. (Prove it!)

Conversely, if $T: V \rightarrow \mathbb{F}^n$ is an ismorphism, then the set of preimages of the basis of the standard basis must be linearly independent since the kernel of $T$ must be null, and it must span $V$. So $(f^{\text{pre}}(\epsilon_1), \ldots, f^{\text{pre}}(\epsilon_n))$ is an ordered basis for $V$ and is the only ordered basis for which the $i$-th component is mapped to the $i$-component of the standard basis of $\mathbb{F}^n$.

This proves:

**Theorem:**
Every $n$-dimensional vector space $V$ over $\mathbb{F}$ is isomorphic to $\mathbb{F}^n$. Also, for every ordered basis $(b_1, \ldots, b_n)$ of $V$, there is a unique isomorphism sending $b_i \mapsto \epsilon_i$, and for any isomorphism $\phi: V \rightarrow \mathbb{F}^n$ there is a unique ordered basis $(b_1, \ldots, b_n)$ such that $\phi(b_i) = \epsilon_i$. $\Box$

An isomorphism from an $n$-dimensional vector space $V$ to $\mathbb{F}^n$, is called a **coordinate system on $V$**. There is a bijection between coordinate systems on $V$ and ordered bases in $V$.
