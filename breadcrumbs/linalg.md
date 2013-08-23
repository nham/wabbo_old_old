# Linear algebra notes

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
