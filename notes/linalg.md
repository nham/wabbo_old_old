% Some notes on linear algebra

## Preliminaries

$\mathbb{P}$ denotes the set of all positive integers. If $m \in \mathbb{P}$, $[m]$ is defined to be the set $\{1, ..., m\}$ of the first m positive integers. A *field* is a non-trivial commutative ring with non-zero elements all having multiplicative inverses.

[Insert here: Vector spaces, basic properties, subspaces, spanning sets, linear independence and dependence, bases, dimension (for finite-dimensional vector spaces)] 

## Matrices

A **matrix** is a function $A: [m] \times [n] \rightarrow \mathbb{F}$ for $m, n \in \mathbb{P}$ and field $\mathbb{F}$. The image elements of the matrix are often arranged in a rectangular array of scalars. You should have seen it before. An $m \times n$ matrix is said to have $m$ rows and $n$ columns, and $A[i,j]$ refers to the scalar element in row $i$, column $j$. We notate the $1 \times n$ matrix of row $i$ by $A[i, :]$, as well as the $n \times 1$ matrix of row $j$ by $A[:, j]$.

A matrix is **square** if it is $n \times n$ for some $n \in \mathbb{P}$.

We define an **elementary row operation** on $m \times n$ matrices, $\xi[i,j,c,d]: \mathbb{F}^{m \times n} \rightarrow \mathbb{F}^{m \times n}$ (or just $\xi$ if $i$, $j$, $c$, $d$ are clear) defined, for $i,j \in [m]$ and $c, d \in \mathbb{F}$ with $c \neq 0$, by:

$$[\xi A ]_{rs} := \cases{
    c A_{rs} + d A_{js} & \text{if } r = i \cr
    A_{rs} & \text{otherwise}}$$

This function replaces row $i$ with a linear combination of rows $i$ and $j$. 

A critical property of this operation is that it has an *inverse*:

**Lemma:** Any elementary row operation $\xi$ on $i, j, c, d$ has an inverse elementary row operation.

*Proof:* Since $c \neq 0$, $c^{-1}$ exists in $\mathbb{F}$, we can form the elementary row operation $\phi$ on $i, j, c^{-1}, -d c^{-1}}$. So if $A$ is $m \times n$, then $\phi(\xi A) = A$. $\Box$

$m \times n$ matrices $A$ and $B$ are called **row-equivalent** if there is some sequence of elementary row operations $e_1, \ldots, e_n$ such that $(e_n \circ \cdots \circ e_1)(A) = B$.

The following is a consequence of elementary row operations being invertible.

**Corollary:** $A$ is row-equivalent to $B$ iff $B$ is row-equivalent to $A$. $\Box$


## Row-reduced matrices
A matrix $A \in \mathbb{F}^{m \times n}$ is **row-reduced** if

 - for every row $i$, if there is a $j$ such that $A[i,j] \neq 0$, the smallest such $j$ must have $A[i,j] = 1$. Each such cell is called a **pivot**
 - for every pivot $(i,j)$, all non-pivot cells $A[k,j]$ in column $j$ must be zero.

**Theorem:** Every matrix is row-equivalent to a row-reduced matrix.

*Proof:* We give an algorithm and prove its correctness.

$$ \begin{align}
\text{def } & \text{RowReduce}(A \in \mathbb{F}^{m \times n}): \\
& \text{for } i \in [m]: \\
    & \text{.... } j \leftarrow 1 \\
    & \text{.... } \text{while } A[i,j] = 0 \text{ and } j \leq m: \\
    & \text{........ } j \leftarrow j + 1 \\
    & \text{.... } \text{if } j \leq  m: \\
    & \text{........ } A \leftarrow LC_{i,i, A[i,j], 0}(A) \\
    & \text{........ } \text{for } k \in [m]: \\
    & \text{............ } \text{if } k \neq i \text{ and } A[k,j] \neq 0: \\
    & \text{................ } A \leftarrow LC_{k,i,1, - A[k,j]}(A) \\
\end{align}$$

Prior to the start of the algorithm, we have that for $k = 1$, then for all rows $i$ with $1 \leq i \leq k-1$, if there is a $p_i$ such that $A[i, p_i] \neq 0$, then $A[i, p_i] = 1$ and if $p_1$ exists, all $j \neq i$ have $A[j, p_i] = 0$. 

Assuming it is true after the $k$-th iteration, during the $(k+1)$-th iteration we set some $A[k+1,p_{k+1}]$ to 1 if possible and zero out the other terms in the $p_{k+1}$-th column (if there is such a column). So the property will be true again after the $k+1$-th iteration. Hence, after the $m$-iteration, the matrix will be row-reduced. $\Box$

(Yeah, that was a bit silly, but hey, now you know how to prove the correctness of algorithms if you didn't already!)


## Row-reduced echelon matrices
We can extend the concept of row reduction by adding a few more properties. This will allow us to easily extract more information than mere row-reduction allows.

But first we need a lemma and some notation. We will notate the $n \times n$ identity matrix as $I_n$.

**Lemma:** The operation $\text{swap}_{i,j}$ defined on $m \times n$ matrices and defined by

$$[swap_{i,j}(A)]_{rs} := \cases{
    A_{js} & \text{if } r = i \cr
    A_{is} & \text{if } r = j \cr 
    A_{rs} & \text{otherwise}}$$

can be implemented by a series of $LC$ operations.

*Proof:* Peform the following:

 1. $\xi[i,j,-1,1]$
 2. $\xi[j,i,1,-1]$
 3. $\xi[i,j,1,1]$

This performs $r_i \leftarrow - r_i + r_j$, $r_j \leftarrow r_j - r_i$, $r_i \leftarrow r_i + r_j$, in that order. It is an easy verification. $\Box$


A matrix $A \in \mathbb{F}^{m \times n}$ is in **row-reduced echelon form** if

 - $A$ is row-reduced
 - every row of all zeroes in $A$ is below every non-zero row.
 - if $(i, p_i)$ and $(j, p_j)$ are pivots with $i < j$, then $p_i < p_j$.

Note that the last two stipulations can be rephrased as follows: if there are $k$ pivots, then the set $\{(i, p_i)\}$ of pivots is a monotonically increasing function on $[k] \rightarrow [n]$.

It might be intuitively clear that all we need to turn a row-reduced matrix into a row-reduced echelon (RRE) matrix is swap some rows around. It is this fact that allows us to prove the following theorem:

**Theorem:** Every matrix is row-equivalent to a row-reduced echelon matrix.

*Proof:* First row-reduce the matrix, then swap the rows so that the criteria for echelon form are met. $\Box$

If $A \in \mathbb{F}^{m \times n}$ is row-equivalent to a row reduced matrix $B$ with $k$ pivots, then we say that $A$ **has $k$ pivots**.


## Matrix multiplication
I may fill in the details later, but for now I just note that matrix multiplication is a thing you can do on matrices $A$ and $B$ if $A$ has the same number of columns as $B$ has rows. The intuition here, in light of the presentation up til now, is that each row of $A$ contains a list of scalar coefficients, one for each row in $B$. When use these coefficients to form a linear combination of all the rows of $B$, and stick the result into the first row of $C$, the resulting matrix. Hence if $A \in \mathbb{F}^{k \times n}$ and $B \in \mathbb{F}^{k \times n}$, then the result $C$ will have $m$ rows (because each row of $A$ gives us a linear combination) and $n$ columns (because each linear combination is of rows of $B$, which have $n$ columns).

Here are two theorems about matrix multiplication that I will not prove here:

**Theorem:** If $A, B, C$ are matrices such that $AB$, $BC$ is well-defined, then $(AB)C = A(BC)$ (Matrix multiplication is associative).

**Theorem:** For any $A \in \mathbb{F}^{m \times n}$, $A = A I_n = I_m A$.

This last theorem invites us to consider a "dual" interpretation of matrix multiplication, which is that each column of the result matrix $AB$ is a linear combination of the columns of $A$ by coefficients taken from each column of $B$.

If $A \in \mathbb{F}^{m \times n}$, then $B$ is a **left-inverse** for $A$ if $BA = I_n$. $C$ is a **right-inverse** for $A$ if $AC = I_m$.

**Theorem:** If $B$ is a left inverse for $A \in \mathbb{F}^{m \times n}$ and $C$ is a right inverse for $A$, then $B = C$.

*Proof:* $B = B I_m = B (AC) = (BA) C = I_n C = C$. $\Box$

A $B$ which is both a left and a right inverse for $A$ is called **the inverse** of $A$, on account of its being unique by the previous theorem. If $A$ has such an inverse, then $A$ is said to be **invertible**.


## Elementary matrices
Recall that elementary row operations were functions $\mathbb{F}^{m \times n} \rightarrow \mathbb{F}^{m \times n}$. We should be able to find an $m \times m$ matrix which does the same thing when multiplied on the left.

An **elementary matrix** is defined by:

$$E[i,j,c,d] := \xi[i,j,c,d](I_n)$$

**Proposition:** For $A \in \mathbb{F}^{m \times n}$, $E[i, j, c,d] A = \xi[i, j, c, d] (A)$

*Proof:* By inspection. $\Box$

**Lemma:** Every elementary matrix is invertible, and its inverse is an elementary matrix.

*Proof:* Given an elementary matrix $E = f(I)$, where $f$ is some elementary row operation, we simply use $E^{-1} = f^{-1}(I)$. $\Box$

After the introduction of elementary matrices, "$A$ is row-equivalent to $B$" means there's some sequence $E_1, \ldots, E_k$ such that $E_k \cdots E_1 A = B$.


## Rank of a matrix

In any $m \times n$ matrix $A$, we can consider the columns of $A$ to be elements of the $m$-dimensional vector space $\mathbb{F}^m$. Similarly, the rows are elements of $\mathbb{F}^n$. From this we can consider the subspace of $\mathbb{F}^m$ (resp. $\mathbb{F}^n$) spanned by the columns (resp. rows) of $A$. These will be called the **column space** and the **row space**, respectively, and notated $cs(A)$ and $rs(A)$.

The dimensions of these spaces will be called the **column rank** and **row rank**, denoted $crk(A)$ and $rrk(A)$.

**Theorem:** For any $m \times n$ matrix $A$, $crk(A) = rrk(A)$.

*Proof:* Let $crk(A) = r$. We know $r \leq n$. Let $c_1, \ldots, c_r$ be a basis for $cs(A)$. Then form the matrix $C$ with $C[:, i] = c_i$. We can find some $r \times n$ matrix $R$ such that $CR = A$ (the columns of $C$ are a basis). But this multiplication is also a linear combination of the $r$ rows of $R$ that yields rows of $A$, so $r = rrk(A) \leq rrk(R) \leq crk(A)$.

The same argment on the transpose of $A$ yields that $crk(A) \leq rrk(A)$. $\Box$


## Rank and invertibility

There's gaps in the notes, but I want to build up exactly what is needed to prove this:

**Theorem:** $A \in \mathbb{F}^{m \times n}$ is invertible iff $\text{rank}(A) = m = n$ iff $A$ is the product of elementary matrices.

An $n \times n$ matrix is **singular** if $\text{rank}(A) < n$, and **non-singular** otherwise.











## Systems of linear equations

A **system of linear equations** is a pair $(A, y)$ where 

 1. $A$ is a function $[m] \times [n] \rightarrow \mathbb{F}$ for $m, n \in \mathbb{P}$ and $\mathbb{F}$ is a field. 
 2. $y \in \mathbb{F}^m$

We will call $m$ the **height** of the system. We will refer to pair $(A[i, :], y_i)$ as an *equation* of the system $(A, y)$.


The underlying **augmented matrix** of a system of linear equations is the $m \times n+1$ matrix where $A[i, n+1] = y_i$. The significance of this will be seen later after the introduction of *linear combinations* of systems and *elementary row operations*. Essentially, these transform every column of a matrix in the same way, so that applying them to the augmented matrix yields the same solution as applying them individually to both sides of the equation.

We will often notate the augmented matrix of system $(A,y)$ as $A|y$. If $B$ is an $m \times n+1$ matrix, we will sometimes need to "pull the last column" out of the matrix $B$ and form a system $(B,z)$, where $z$ is an $m \times 1$ matrix with the same values as column $n+1$ of $B$. In fact, it will be convenient to think of $A|y$ *as* the system $(A,y)$. They are formally distinct, but there is a clear correspondence between them.

We can also view $1 \times n$ and $n \times 1$ matrices as **vectors**, that is, elements of $\mathbb{F}^n$. For two vectors $x, y \in \mathbb{F}^n$, we define the **dot product** of $x$ and $y$ by:

  $$ x \cdot y := \sum_1^n x_i y_i$$

Associated with any system of linear equations $(A,y)$ is a subset $\text{sol}(A,y)$ of $\mathbb{F}^n$ called the **solutions** of the system. This is defined:

  $$\text{sol}(A,y) := \{x \in \mathbb{F}^n : A[i, :] \cdot x = y_i\}$$

The typical presentation begins with some collection of equations and poses the question of how we can solve this collection of equations, later introducing matrices as a notational convenience. Here we cut to the chase.

A **homogeneous system** is a system $(A,y)$ where $y = 0$ (the $m \times 1$ matrix of zeroes). Any homogeneous system always has the **trivial solution** $0 \in \mathbb{F}^n$

A **square system** is a system $(A,y)$ where $A$ is $n \times n$.

A **linear combination** of a system $(A, y)$ is a system $(B, z)$ of height 1 such that for some $c_1, \ldots, c_m \in \mathbb{F}$

 - $B|z = \sum_1^m c_i A|y[i, :]$

**Lemma:** If $(B,z)$ is a linear combination of $(A,y)$ then $\text{sol}(A,y) \subseteq \text{sol}(B,z)$. $\Box$

**Corollary:** If $(B,z)$ is a system, all of whose equations are linear combinations of $(A,y)$, then $sol(A,y) \subseteq sol(B,z)$.
*Proof:* The solutions of $(B,z)$ are those that are solutions of each individual equation in the system. Each individual equation's solution set is a superset of the solutions of $(A,y)$, hence the solution set of the whole system is. $\Box$

**Corollary:** If $(A,y)$ and $(B,z)$ are systems such that each equation of $(A,y)$ is a linear combination of $(B,z)$ and each equation of $(B,z)$ is a linear combination of $(A,y)$, then $sol(A,y) = sol(B,z)$. $\Box$

This last corollary inspires a definition: systems $(A,y)$ and $(B,z)$ are **equivalent** if each equation in each system is a linear combination of the other. By the last corollary, equivalent systems have the same solution set. Hence if our interest is in determining the solution set for a given system, we might look for transformations that turn said system into an equivalent but easier to solve system.

It should be noted (and can probably be inferred by our use of the word "equivalent") that the previous definition does define an equivalence relation. Every system is trivially a linear combination of itself, the definition is inherently symmetric, and if $A$ equivalent to $B$ and $B$ equivalent to $C$, then by distributivity, commutativity and associativity of $\mathbb{F}$,  $A$ and $C$ are equivalent as well.


## Row-equivalence

Clearly any finite sequence of elementary row operations on some linear system $(A, y)$ will result in a system $(B,z)$ whose equations are linear combinations of $(A,y)$. The fact that every elementary row operation has an inverse operation means that applying the same sequence of operations to both $A$ and $y$ will give us an *equivalent system* $(B, z)$.


This shows us that applying elementary row operations doesn't change the solution set of a system.

**Theorem:** If $(A,y)$ is a linear system with $A \in \mathbb{F}^{m \times n}$ and $e_1, \ldots, e_n$ are elementary row operations, then letting $f = e_n \circ \cdots \circ e_1$, we have that the associated system of $f(A|y)$ is equivalent to $(A,y)$. 

*Proof:* Given an elementary row operation $e$, the associated system of $e(A|y)$ is equivalent to $A|y$ since 1) every row of $e(A|y)$ is a linear combination of $(A,y)$ and 2) there is an inverse row operation, showing that every row of $A|y$ is a linear combination of $e(A|y)$. The result extends to arbitrary finite sequences of elementary row operations since linear systems equivalence is an equivalence relation. $\Box$

**Corollary:** If $(A,0)$ and $(B,0)$ are homogeneous systems, then they are equivalent iff $A$ and $B$ are row-equivalent.


Row reduction allows us to quickly find solutions to systems. We simply row-reduce the augmented matrix of the system. After doing so, we have two possibilities

 1. There are pivots in the last column. This means there are no solutions to the system, because we have an equation that says $0 = 1$. No set of scalars can solve this equation.

 2. No pivots in the last column. Then we will have some set of $k$ pivots $(i, p_i)$. We simply have to find the solutions to the set of $k$ equations where each equation is $x_{p_i} = - B[i,n+1] + \sum_1^{m-k} c_i u_i$, where the $u_i$'s are the $x$'s that don't correspond to pivot points and $b_{n+1}$ is the value of the row-reduced augmented matrix in the last column. The point is that we can assign arbitrary values to the variables that don't correspond to pivots and we will obtain a solution of the system.



**Underconstrained System Theorem:** If $(A,y)$ is a system with $A \in \mathbb{F}^{m \times n}$ with $k$ pivots and $k < n$, then if $(A,y)$ has a solution, it has at least two solutions.

*Proof:* Some RRE matrix $R$ which is row equivalent to $A$ has $k$ pivots. The remaining $m-k$ rows are all zero. From the augmented matrix with $R$ and $z$ (where $z$ is the RRE version of $y$ formed from the same operations that turned $A$ into $R$), our equations are, for $i \in [k]$, let $p_i$ be the column that the pivot of row $i$ is in, and let $J = [n] - \{p_1, \ldots, p_k\}$. Then $x_{p_i} = -z_i + \sum_{J} r_{ij} x_j$. Since we have some solution, take the values of the $x_{j}, j \in J$ and add one to each of them. This is a new solution. $\Box$

**Corollary:** If $(A,0)$ is a homogeneous system with $A \in \mathbb{F}^{m \times n}$ with $k$ pivots and $k < n$, then it has a non-trivial solution.

This next theorem about square systems is a straightforward consequence of the Underconstrained System Theorem.

**Theorem:** If $A \in \mathbb{F}^{n \times n}$ and $y \in \mathbb{F}^{n \times 1}$, then $A$ is row-equivalent to $I_n$ iff $(A,y)$ has exactly one solution.

*Proof:* If some composition of elementary row ops, $f$, is such that $f(A) = I_n$, then the associated system of $f(A|y)$ is $(I_n, z)$ for some $z$, which clearly has only one solution. Conversely, if $(A,y)$ has only one solution, it could not be row-equivalent to a row-reduced matrix with $k < n$ pivots, for by the Underconstrained System Theorem it would have more than one solution. Any row-reduced echelon matrix which is row-equivalent to $A$ must have $n$ pivots. The only such matrix is $I_n$. $\Box$


**Theorem:** The following 3 conditions are equivalent for square systems (an $A \in \mathbb{F}^{n \times n}$):

 1. $A$ is row-equivalent to $I_n$
 2. $A$ is a product of elementary matrices
 3. $A$ is invertible

*Proof:* (1) means that $E_k \cdots E_1 A = I_n$ for some elementary matrices $E_i$. The previous lemma implies that $A = E_1^{-1} \cdots E_k^{-1} I_n$, establishing (2). Given (2), $A$ is clearly invertible, again by the previously lemma. Finally for (3), if $A$ is invertible, then consider a row-reduced echelon matrix $R$ formed from $A$. There is some sequence of elementary matrices such that $E_k \cdots E_1 A = R$. Since $A$ is invertible, $R$ is invertible (since $R$ is the product of invertible matrices). Since $R$ is $n \times n$, if $R$ does not have full pivots, it could not be invertible since we must have some $n \times n$ X such that $RX = I_n$. This cannot be so, since a zero row in $R$ makes that corresponding row of the resultant matrix zero as well. The only $n \times n$ row-reduced echelon matrix with full pivots is $I_n$, so in fact $R = I_n$, establishing (1). $\Box$

**Corollary:** $A, B \in \mathbb{F}^{m \times n}$ are row-equivalent iff some invertible $P \in \mathbb{F}^{m \times m}$ is such that $A = PB$.

*Proof:* To be tedious about it, by the definitions of row-equivalent and elementary matrices, $A$ is row-equivalent to $B$ iff $A = E_k \cdots E_1 B$ for elementary matrices $E_i$. $\Box$


**Theorem:** For $A \in \mathbb{F}^{n \times n}$ and $y \in \mathbb{F}^{n \times 1}$, $A$ is invertible iff $(A,y)$ has exactly one solution.

*Proof:* By a previous theorem, $A$ is row-equivalent to $I_n$ iff every $(A,y)$ has exactly one solution. By the previous theorem $A$ is invertible iff $A$ is row-equivalent to $I_n$. $\Box$

**Corollary:** An $n \times n$ matrix $A$ with a left inverse or a right inverse is invertible.

*Proof:* If $A$ has a left inverse $B$, then $BA = I_n$. So $\text{sol}(A, 0) \subseteq \text{sol}(BA, 0) = \text{sol}(I_n, 0) \subseteq \text{sol}(A, 0)$. Thus $(A,0)$ has only the trivial solution, and is invertible. A similar proof holds in case that $A$ has a right inverse $C$ once one realizes that $AC = I_n$ means that $C$ is invertible (so that $A$, its inverse, is invertible as well). $\Box$


## Vector spaces, subspaces & all that

The additive group operation will be referred to as *vector addition*, while the operation $F \times V \rightarrow V$ is called *scalar multiplication*. Note that the last two conditions imply that the multiplicative group of the field acts on the abelian group of vectors.

**Exchange algorithm** (for  proving that any two bases of an fdvs have same number of elements)
