# Linear algebra notes

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

Note that we disallow scaling by $0$, meaning that not all linear combinations are permissible. The reason is that we want to ensure that elementary row operations have an inverse:

### Elementary row operations have inverses that are elementary row operations.

### Row equivalence
Two matrices are **row equivalent** if some number of elementary row operations takes one to the other.

A consequence of elementary row operations being invertible is that row equivalence is a bona fide equivalence relation.


## Row reduction
 - some number of saxpy's gives a "Stage 1" reduction, each column has only one nonzero element in it.
 - applying scalings to a "Stage 1" matrix gives a "Stage 2" matrix, what Hoffman & Kunze call a "row reduced matrix". In addition to each column having only one nonzero, the first nonzero in each row, if it exists, is 1.
 - By applying only swaps to a "Stage 2" matrix, we can get a "Stage 3" matrix. This is commonly called row reduced echelon form. In addition to the above two criteria, all the zero rows appear below the non-zero rows and the pivots go from left to right.


## Matrix multiplication
It's associative and distributes both ways over addition. The are multiplicative identities. (These properties ensure that the set of $n \times n$ matrices over a field form a ring with identity under matrix multiplication and addition)
