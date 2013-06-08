# Linear algebra

Please don't read these awful notes. Go get a real linear algebra book. I'm a fan of Hoffman and Kunze, as you can probably tell.

## Systems of linear equations

$\mathbb{P}$ denotes the set of all positive integers. If $m \in \mathbb{P}$, $[m]$ is defined to be the set $\{1, ..., m\}$ of the first m positive integers. A *field* is a non-trivial commutative ring with non-zero elements all having multiplicative inverses.

A **system of linear equations** is a pair $(A, y)$ where 

 1. $A$ is a function $[m] \times [n] \rightarrow \mathbb{F}$ for $m, n \in \mathbb{P}$ and $\mathbb{F}$ is a field. 
 2. $y \in \mathbb{F}^m$

The function $A$ is called a **matrix**. The image elements of the matrix are often arranged in a rectangular array of scalars. You should have seen it before. An $m \times n$ matrix is said to have $m$ rows and $n$ columns, and $A[i,j]$ refers to the scalar element in row $i$, column $j$. We notate the $1 \times n$ matrix of row $i$ by $A[i, :]$, as well as the $n \times 1$ matrix of row $j$ by $A[:, j]$. We will also call $m$ the **height** of the system. We will refer to pair $(A[i, :], y_i)$ as an *equation* of the system $(A, y)$.

We can also view $1 \times n$ and $n \times 1$ matrices as **vectors**, that is, elements of $\mathbb{F}^n$. For two vectors $x, y \in \mathbb{F}^n$, we define the **dot product of $x$ and $y$ by:

  $$ x \cdot y := \sum_1^n x_i y_i$$

Associated with any system of linear equations $(A,y)$ is a subset $\text{sol}(A,y)$ of $\mathbb{F}^n$ called the **solutions** of the system. This is defined:

  $$\text{sol}(A,y) := \{x \in \mathbb{F}^n : A[i, :] \cdot x = y_i$$

The typical presentation begins with some collection of equations and poses the question of how we can solve this collection of equations, later introducing matrices as a notational convenience. Here we cut to the chase.

A **homogeneous system** is a system $(A,y)$ where $y = 0$ (the $m \times 1$ matrix of zeroes).

A **linear combination** of a system $(A, y)$ is a system $(B, z)$ of height 1 such that for some $c_1, \ldots, c_m \in \mathbb{F}$

 - $B = \sum_1^m c_i A[i, :]$
 - $z = \sum_1^m c_i y_i$

**Lemma:** If $(B,z)$ is a linear combination of $(A,y)$ then $\text{sol}(A,y) \subseteq \text{sol}(B,z)$. $\Box$

**Corollary:** If $(B,z)$ is a system, all of whose equations are linear combinations of $(A,y)$, then $sol(A,y) \subseteq sol(B,z)$.
*Proof:* The solutions of $(B,z)$ are those that are solutions of each individual equation in the system. Each individual equation's solution set is a superset of the solutions of $(A,y)$, hence the solution set of the whole system is. $\Box$

**Corollary:** If $(A,y)$ and $(B,z)$ are systems such that each equation of $(A,y)$ is a linear combination of $(B,z)$ and each equation of $(B,z)$ is a linear combination of $(A,y)$, then $sol(A,y) = sol(B,z)$. $\Box$

This last corollary inspires a definition: systems $(A,y)$ and $(B,z)$ are **equivalent** if each equation in each system is a linear combination of the other. By the last corollary, equivalent systems have the same solution set. Hence if our interest is in determining the solution set for a given system, we might look for transformations that turn said system into an equivalent but easier to solve system.

It should be noted (and can probably be inferred by our use of the word "equivalent") that the previous definition does define an equivalence relation. Every system is trivially a linear combination of itself, the definition is inherently symmetric, and if $A$ equivalent to $B$ and $B$ equivalent to $C$, then by distributivity, commutativity and associativity of $\mathbb{F}$,  $A$ and $C$ are equivalent as well.


## Row-equivalence

We define an **elementary row operation**, $LC_{i,j,c,d}$ which are functions $\mathbb{F}^{m \times n} \rightarrow \mathbb{F}^{m \times n}$ defined, for $i,j \in [m]$ and $c, d \in \mathbb{F}$ with $c \neq 0$, by:

$$[LC_{i,j,c,d}(A)]_{rs} := \cases{
    c A_{rs} + d A_{js} & \text{if } r = i \cr
    A_{rs} & \text{otherwise}}$$

This function replaces row $i$ with a linear combination of rows $i$ and $j$. 

A critical property of this operation is that it has an *inverse*:

**Lemma:** Any elementary row operation $LC_{i,j,c,d}$ has an inverse elementary row operation.

*Proof:* Since $c \neq 0$, $c^{-1}$ exists in $\mathbb{F}$ we can form the operation $LC_{i,j,c^{-1}, -d c^{-1}}$. Saying the original matrix is $A$, the result of the first elementary row operation is $B$, and the result of the second elementary row operation is $C$, every element $C_{is}$ has:

$$\begin{align}
C_{is} & = c^{-1} B_{is} - d c^{-1} B_{js} \\
& = c^{-1} (c A_{is} + d A_{js}) + -d c^{-1} A_{js}
& = A_{is}
\end{align}$$

$\Box$

Clearly any finite sequence of elementary row operations on some linear system $(A, y)$ will result in a system $(B,z)$ whose equations are linear combinations of $(A,y)$. The fact that every elementary row operation has an inverse operation means that applying the same sequence of operations to both $A$ and $y$ will give us an *equivalent system* $(B, z)$.

A quick definition will help: $m \times n$ matrices $A$ and $B$ are called **row-equivalent** if there is some sequence of elementary row operations $e_1, \ldots, e_n$ such that $(e_n \circ \cdots \circ e_1)(A) = B$.

The following is a consequence of elementary row operations being invertible.

**Corollary:** $A$ is row-equivalent to $B$ iff $B$ is row-equivalent to $A$.

**Theorem:** If $(A,y)$ is a linear system with $A \in \mathbb{F}^{m \times n}$ and $e_1, \ldots, e_n$ are elementary row operations, then letting $f = e_n \circ \cdots \circ e_1$, we have that $(f(A), f(y)$ is equivalent to $(A,y)$

*Restated:* If $(A,y)$ and $(B,z)$ are two linear systems with $A$ row-equivalent to $B$ and $y$ row-equivalent to $z$ by the same sequence of elementary row operations, then $(A,y)$ and $(B,z)$ are equivalent.

(*Note:* There is an abuse of notation here in that the same $f$ could not be a function on both an $m \times n$ and a $m \times 1$ matrix. Clearly we mean that there is an appropriate elementary row operation for each different width.)

*Proof:* Given an elementary row operation $e$, the system $(e(A), e(y))$ is equivalent to $(A,y)$ since 1) every row of $(e(A), e(y))$ is a linear combination of $(A,y)$ and 2) there is an inverse row operation, showing that every row of $(A, y)$ is a linear combination of $(e(A), e(y))$. The result extends to arbitrary finite sequences of elementary row operations since linear systems equivalence is an equivalence relation. $\Box$

**Corollary:** If $(A,0)$ and $(B,0)$ are homogeneous systems, then they are equivalent iff $A$ and $B$ are row-equivalent.

Next we introduce a computational convenience: **augmented matrices**. If we have some system $(A,y)$, where $A \in \mathbb{F}^{m \times n}$ and $y \in mathbb{F}^{m \times 1}$, instead of applying row operations separately to each, we can form a new $m \times (n+1)$ matrix $B$ with $y$ as the $n+1$-th column and just apply the row operations to the this new matrix. This works because the row operations do the same thing on each row, so it really doesn't matter how long each row is. Note that if the system is homogeneous, there's really no point in forming the augmented matrix: the last column will always be zero.

## Row-reduced matrices
A matrix $A \in \mathbb{F}^{m \times n}$ is **row-reduced** if

 - for every row $i$, if there is a $j$ such that $A[i,j] \neq 0$, the smallest such $j$ must have $A[i,j] = 1$. Each such cell is called a **pivot**
 - for every pivot $(i,j)$, all non-pivot cells A[k,j]$ in column $j$ must be zero.

**Theorem:** Every matrix is row-equivalent to a row-reduced matrix.

*Proof:* We give an algorithm and prove its correctness.

```
def RowReduce(A):
    for i in [1 to m]:
        j <-- 1
        while A[i,j] == 0 and j <= m:
            j <-- j + 1
        
        if j <= m:
            A <-- LC[i,i, A[i,j], 0](A)

            for k in [1 to m]:
                if k != i and A[k,j] != 0:
                    A <--- LC[k,i,1, - A[k,j]](A)
```

````python
def hello():
    print('sup')
````


Prior to the start of the algorithm, we have that for $k = 1$, then for all rows $i$ with $1 \leq i \leq k-1$, if there is a $p_i$ such that $A[i, p_i] \neq 0$, then $A[i, p_i] = 1$ and if $p_1$ exists, all $j \neq i$ have $A[j, p_i] = 0$. 

Assuming it is true after the $k$-th iteration, during the $(k+1)$-th iteration we set some $A[k+1,p_{k+1}]$ to 1 if possible and zero out the other terms in the $p_{k+1}$-th column (if there is such a column). So the property will be true again after the $k+1$-th iteration. Hence, after the $m$-iteration, the matrix will be row-reduced. $\Box$

(Yeah, that was a bit silly, but hey, now you know how to prove the correctness of algorithms if you didn't already!)

This computational tool allows us to quickly find solutions to systems. We simply row-reduce the augmented matrix of the system. After doing so, we have two possibilities

 1. There are pivots in the last column. This means there are no solutions to the system, because we have an equation that says $0 = 1$. No set of scalars can solve this equation.

 2. No pivots in the last column. Then we will have some set of $k$ pivots $(i, p_i)$. We simply have to find the solutions to the set of $k$ equations where each equation is $x_{p_i} = - B[i,n+1] + \sum_1^{m-k} c_i u_i$, where the $u_i$'s are the $x$'s that don't correspond to pivot points and $b_{n+1}$ is the value of the row-reduced augmented matrix in the last column. The point is that we can assign arbitrary values to the variables that don't correspond to pivots and we will obtain a solution of the system.

