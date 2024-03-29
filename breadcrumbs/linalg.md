# Linear algebra notes

## Vector spaces
A vector space is a pair $(V, \mathbb{F})$ where $V$ is an abelian group, $\mathbb{F}$ is a field, and

 - $a(u + v) = au + av$
 - $(a + b)u = au + bu$
 - $1u = u$
 - $(ab)u = a(bu)$

If $v_1, \ldots, v_n$ are vectors and $c_1, \ldots, c_n$ are field elements (scalars), then

$$ a_1 v_1 + \cdots + a_n v_n$$

is said to be a **linear combination** of the $v_i$'s.

A **subspace** of vector space $V$ is a subset $S$ of $V$ that forms a vector space when the vector addition and scalar multiplication operations are restricted to $S$. Equivalently, a **subspace** is a subset closed under linear combinations.

The intersection of any collections of subspace is again a subspace, but the union is not, in general. We are forced to define the **sum** of subspaces instead, which is the smallest subspace that contains all the subspaces in the collection. With these two operations, the set of all subspaces of a vector space forms a complete lattice under set containment.

An alternate characterization of the sum of a collection $\mathcal{S}$ of subspaces is $\{x \in V : \exists n \in \mathbb{P} x = s_1 + \cdots + s_n, s_i \in \bigcup \mathcal{S}\}$: on the one hand, it's a subspace containing each $S \in \mathcal{S}$. On the other, if $x = s_1 + \ldots + s_n$ is such that $s_i \in \bigcup \mathcal{S}$, then $x \in \sum \mathcal{S}$ since subspaces are closed under addition.

The **direct sum** of a collection $\mathcal{S}$ of subspaces is the sum $\sum \mathcal{S}$ such that for all $S \in \mathcal{S}$, $S \cap (\sum \mathcal{S} - S)$ is the zero subspace. It is written $\bigoplus \mathcal{S}$.

It's a stronger condition than sayin $S \cap T = \{0\}$ for all $S, T \in \mathcal{S}$. Consider 3 subspaces of $\mathbb{R}^3$ which are coplanar, say the spaces spanned by $e_1, e_2$, and $(1, 1)$. Pairwise intersections are only at the origin, but the sum of $e_1$ and $e_2$ contains the space spanned by $(1, 1)$.

There is a particular direct sum to single out, which is the idea of a **complement:** $T$ is the complement of $S$ in $V$ if $V = S \oplus T$.


The **span** or **subspace generated** by some subset $S$ of a vector space is the intersection of all subspaces containing $S$. Alternatively, it is the set of all linear combinations of vectors in $S$. We notate the span $\langle S \rangle$, and say that $S$ **spans the space $\langle S \rangle$.


A set $S$ is **linearly independent** if every finite subset $\{s_1, \ldots, s_n\}$ is such that the the only linear combination that results in the zero vector is the *trivial combination* of all zero scalars. A set is $S$ linearly dependent if not independent.

Every subset of an independent set is independent, and every superset of a dependent set is dependent.

A set $S$ is linearly independent iff for all $x \in S$, $x \notin \langle S - x \rangle$: $x$ being in the span of its (set-theoretic) complement would yield a non-trivial combination that results in zero, and if $S$ is dependent, one element is a combination of the others, so it can be removed without affecting the span.

If a set is dependent, then for any non-trivial combination resulting in zero, any vector with a non-zero scalar coefficient is in the span of the other vectors in the non-trivial combination.

An independent spanning set is a **basis**. The following characterization is insightful:

**Theorem:** A subset $B$ of vector space $V$ is a basis iff it is a minimal spanning set iff it is a maximal independent set.

*Idea:* Any basis is a minimal spanning set, otherwise you would remove an element without affecting the span, implying the set was dependent. A basis is also a maximal independent set: since it spans, adding any new vector results in a dependent set.

Any minimal spanning set must be independent since you can't remove any element without affecting the span, so minimal spanning sets are bases, and hence maximal independent sets by what we just proved.

Finally, a maximal independent set cannot be added to without making it dependent: if we add a vector, it becomes dependent. But the non-trivial zero-obtaining combination in question must have the new vector with a non-zero coefficient since otherwise we would contradict the independence the original set. So the new vector is in the span of some other vectors in the set, hence the original set spans (and hence is a basis). $\Box$

The following theorem depends on Zorn's lemma, which can be stated as: in any poset $P$, if every chain in $P$ has an upper bound in $P$, then $P$ has a maximal element.

**Theorem:** If $V$ is a vector space, $I$ is an independent subset of $V$, $S$ is a spanning set of $V$, and $I \subseteq S$, then there is a basis $B$ with $I \subseteq B \subseteq S$.

*Proof:* Consider the poset $P$ (under set containment) of all independent sets containing $I$ and contained in $S$. Then any chain $\mathcal{C}$ in $P$ is such that $U = \bigcup \mathcal{C}$ is linearly independent: any finite collection of vectors must be contained in a single independent set $A$ in $\mathcal{C}$, so no finite collection of vectors could be dependent without contradicting that $\mathcal{C}$ is made up of independent sets.

This shows that $U$ is linearly independent and $I \subseteq U \subseteq S$, meaning $\mathcal{C}$ has an upper bound. By Zorn's lemma, $P$ has a maximal element $B$. There's a bit of a subtlety here, because we'd like to use "maximal independent sets are bases" to prove that $B$ is a basis, but we actually have two different notions of "maximal" going on:

 - $B$ is maximal in the poset $P$, which means that among all independent sets containing $I$ and contained in $S$, the only set that contains $B$ is $B$ itself.

 - a maximal independent set in a vector space is any independent set for which adding any other vector to the set creates a set which is no longer independent.

So we'd like the prove that these two notions coincide. Partial progress can be obtained by noting that adding any element of $S - B$ to $B$ would result in a set containing $B$, so any such set must not be independent. Actually, this implies that every element of $S$ is in the span of $B$, so $B$ must span $V$ as well (every element of $V$ can be represented as a linear combination of elements of $S$, each of which can be represented as a linear combination of elements of $B$). So we didn't need to make use of our fact about maximal independent sets after all. $\Box$

The idea behind this last theorem is that any independent set can be expanded to a basis, and every spanning set can be reduced to a basis. Actually my wording is a bit sloppy here, we haven't displayed an *algorithm* for reducing an actual spanning set to a basis, we've just shown that one *exists*. This is because our theorem works for infinite-dimensional vector spaces, so such an algorithm might not ever end. There's a pretty simple one that works for the finite-dimensional case, though: given a spanning set, just find a vector that's in the span of the others and throw it away. If ever you can't do this, you have a basis. For expanding an independent set to a basis in the finite-dimensional case, we have the famous Steinitz exchange lemma, which gives us something more than just an algorithm for expanding independent sets:

**Steinitz exchange lemma:** If $n$ vectors span $V$, then for any independent set $S$ in $V$, $S$ has no more than $n$ vectors.

*Idea:* Let $T$ span $V$ and have $n$ vectors in it. The idea is to replace vectors in $T$ one by one with vectors in $S$, each time preserving the span. If we can do this, then we can't run out of vectors in $T$ before running out of vectors in $S$, otherwise some proper subset of $S$ would span $V$ and $S$ would not be independent. $\Box$


## Matrices
A function from $[m] \times [n]$ into some field $\mathbb{F}$. There are also infinite matrices, but we focus on finite matrices here.

A matrix is **square** if it is $n \times n$ for some $n$.

A square matrix is **diagonal** if it only has non-zero entries at $A[i, i]$. There is a special class of diagonal matrices called **identity** matrices, notated $I_n$, which are $n \times n$ matrices that have all $1$'s on the diagonal.


### Row space, column space
We can consider the rows of an $m \times n$ matrix $A$ as vectors in $\mathbb{F}^n$, and similarly the columns as vectors in $\mathbb{F}^m$. The span of the set of rows is a subspace of $\mathbb{F}^n$, called the **row space**. The **column space** is similarly defined.


## Elementary row operations

 - scaling a row (row i) <-- a * (row i), a != 0
 - saxpy
 - swap

We can also define a *Linear combination* operation:

 - (row i) <--- a * (row i) + c * (row j), a != 0

This is clearly more general than scaling and saxpy (scaling has c = 0, saxpy has a = 1). Also, swap can be obtained by 3 linear combinations:

 1. (Ri), (Rj)
 2. => (Ri - Rj), (Rj)
 3. => (Ri - Rj), (Ri)
 4. => (Rj), (Ri)

The operations in order:

 1. LC[1, i, -1, j]
 2. LC[1, j,  1, i]
 3. LC[-1, i, ,1, j]

In other words, every elementary row operation consists of replacing one row by a linear combination of rows.

If $e_1, \ldots, e_k$ are elementary row operations, then $B = e_k \circ \cdots \circ e_1 (A)$ has a row space that is a subspace of the row space of $A$, since all the rows of $B$ are linear combinations of rows in $A$. Can we say more?

Note that we disallow scaling by $0$, meaning that not all linear combinations are permissible. The reason is that we want to ensure that elementary row operations have an inverse:

### Elementary row operations have inverses that are elementary row operations.

Hence, applying elementary row operations preserves the row space.

### Row equivalence
Two matrices are **row equivalent** if some number of elementary row operations takes one to the other.

A consequence of elementary row operations being invertible is that row equivalence is a bona fide equivalence relation. Also, any two row-equivalent matrices have the same row space. It's not immediately clear whether the converse is true.



## Row reduction
 - some number of saxpy's gives a "Stage 1" reduction, each column has only one nonzero element in it.
 - applying scalings to a "Stage 1" matrix gives a "Stage 2" matrix, what Hoffman & Kunze call a "row reduced matrix". In addition to each column having only one nonzero, the first nonzero in each row, if it exists, is 1.
 - By applying only swaps to a "Stage 2" matrix, we can get a "Stage 3" matrix. This is commonly called row reduced echelon form. In addition to the above two criteria, all the zero rows appear below the non-zero rows and the pivots go from left to right.


## Matrix multiplication
(At least) Three ways to think about $C = AB$:

 - Each column of $C$ is a linear combination of columns of $A$ where the coefficients are a column in $B$

 - Each row of $C$ is a linear combination of the rows of $B$ where the coefficients are a row in $A$.

 - Each cell in $C$ is the dot product of a row in $A$ and a column in $B$

Multiplication is associative and distributes both ways over addition. The are multiplicative identities $I_n$. (These properties ensure that the set of $n \times n$ matrices over a field form a ring with identity under matrix multiplication and addition. Note that you need scalar addition to be commutative for this since ring addition must be commutative, but since we assumed the scalars were in a field we're okay.)

### Inverses
The $m \times n$ matrix $A$ has a **left-inverse** if there is some $n \times m$ matrix $B$ such that $BA = I_n$. DItto **right-inverse**. 

We have the following basic fact:

#### If matrix $A$ has a left-inverse $B$ and a right-inverse $C$, then $B = C$.

So any matrix with both a left-inverse and a right-inverse has a unique matrix which is both a left and a right inverse. We call this a **two-sided inverse** or just an **inverse**, and the matrix in question is said to be **invertible**.


## Transposes
The transpose of $A$ is notated $A^T$ and is defined by $A^T[i, j] = A[j, i]$. That is, the $i$-th row becomes the $i$-th column. Every non-square matrix must change under transposition, since the dimensions are the same. However, note that the elements on the diagonal don't change when transposing. This means in particular that any diagonal matrices are unchanged via transpose.

It shouldn't be difficult to see that 

$$(AB)^T = B^T A^T$$

(In $C = AB$, each column of $C$ is a linear combinatin of columns of $A$ with coefficients from a column of $B$. In $Z = B^T A^T$, each column of $Z$ is a linear combination of columns of $B^T$, with columns of $A^T$ as coefficients. But the columns of $B^T$ are the rows of $B$, and ditto for $A^T$. So each column of $Z$ is a linear combination of rows of $B$ with coefficients from a row in $A$. In other words, a column in $Z$ is a row of $C$. So $Z = C^T$.)

Also clearly $(A^T)^T = A$.

It is a basic fact that $A$ is invertible iff $A^T$ is invertible: If $BA = I_n$ iff $A^T B^T = I_n$ and $AB = I_m$ iff $B^T A^T = I_m$.


## Elementary matrices

Previously we defined elementary row operations as functions which map matrices to matrices. But we can actually find, for every elementary row operation $f$, a matrix $e$ such that $eA = f(A)$, where $A$ is some matrix. So applying row operations can be done entirely via matrix multiplication. Such a matrix $e$ is called an **elementary matrix**.

By using transposes we can also introduce the concept of **elementary column operations**, which is defined by first transposing the matrix we want to operate on, then multiplying via elementary matrices, then transposing the result. Via our basic result on the transpose of multiplication, we have that

$$(e A^T)^T = A e^T$$

The only problem is: what is the transpose of an elementary matrix? Luckily enough, it can be proved that:

### The transposes of elementary matrices are elementary matrices

So applying elementary column operations is the same as multiplying a matrix on the right by some elementary matrix.

Elementary column operations have inverses since they can be obtained by multiplying on the right by elementary matrices. Hence there is a notion of *column-equivalent* matrices that we can define, and column equivalent matrices have the same column space. Similarly, we could define a matrix to be in **column-reduced echelon form** if the transpose is in row-reduced echelon form.


## Rank of a matrix

Here's what we've been working towards: First define the **row rank** of a matrix to be the dimension of the row space (ditto **column rank**). Now consider applying row operations and column operations to some matrix $A$ until it is both in row-reduced echelon form *and* column-reduced echelon form. This would look something like this, for elementary matrices $e_i$ and $f_j$:

$$ e_m \cdots e_1 A f_1 \cdots f_n $$

The result is a matrix which has the same row space and same column space as $A$, and which has a copy of $I_k$ in the top left of the matrix and zeroes everywhere else. (Each row pivot is also a column pivot, so we must have the same number of non-zero rows as non-zero columns). Hence, the row rank and column rank are equal.
