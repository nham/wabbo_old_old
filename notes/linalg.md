# Systems of linear equations

$\mathbb{P}$ denotes the set of all positive integers. If $m \in \mathbb{P}$, $[m]$ is defined to be the set $\{1, ..., m\}$ of the first m positive integers. A *field* is a non-trivial commutative ring with non-zero elements all having multiplicative inverses.

A **system of linear equations** is a pair $(A, y)$ where 

 1. $A$ is a function $[m] \times [n] \rightarrow \mathbb{F}$ for $m, n \in \mathbb{P}$ and $\mathbb{F}$ is a field. 
 2. $y \in \mathbb{F}^m$

The function $A$ is called a **matrix**. The image elements of the matrix are often arranged in a rectangular array of scalars. You've probably seen it before. $A[i,j]$ refers to the scalar element in row $i$, column $j$. We notate the $1 \times n$ matrix of row $i$ by $A[i, :]$, as well as the $n \times 1$ matrix of row $j$ by $A[:, j]$. We will also call $m$ the **height** of the system. We will refer to pair $(A[i, :], y_i)$ as an *equation* of the system $(A, y)$.

We can also view $1 \times n$ and $n \times 1$ matrices as **vectors**, that is, elements of $\mathbb{F}^n$. For two vectors $x, y \in mathbb{F}^n$, we define the **dot product of $x$ and $y$ by:

  $$ x \cdot y := \sum_1^n x_i y_i$$

Associated with any system of linear equations $(A,y)$ is a subset $sol(A,y)$ of $\mathbb{F}^n$ called the **solutions** of the system. This is defined:

  $$sol(A,y) := \{x \in \mathbb{F}^n : A[i, :] \cdot x = y_i$$

The typical presentation begins with some collection of equations and poses the question of how we can solve this collection of equations, later introducing matrices as a notational convenience. Here we cut to the chase.

A **linear combination** of a system $(A, y)$ is a system $(B, z)$ of height 1 such that for some $c_1, \ldots, c_m \in mathbb{F}$

 - $B = \sum_1^m c_i A[i, :]$
 - $z = \sum_1^m c_i y_i$

**Lemma:** If $(B,z)$ is a linear combination of $(A,y)$ then $sol(A,y) \subseteq sol(B,z)$. $\Box$

**Corollary:** If $(B,z)$ is a system, all of whose equations are linear combinations of $(A,y)$, then $sol(A,y) \subseteq sol(B,z)$.
*Proof:* The solutions of $(B,z)$ are those that are solutions of each individual equation in the system. Each individual equation's solution set is a superset of the solutions of $(A,y)$, hence the solution set of the whole system is. $\Box$

**Corollary:** If $(A,y)$ and $(B,z)$ are systems such that each equation of $(A,y)$ is a linear combination of $(B,z)$ and each equation of $(B,z)$ is a linear combination of $(A,y)$, then $sol(A,y) = sol(B,z)$. $\Box$

This last corollary inspires a definition: systems $(A,y)$ and $(B,z)$ are **equivalent** if each equation in each system is a linear combination of the other. By the last corollary, equivalent systems have the same solution set. Hence if our interest is in determining the solution set for a given system, we might look for transformations that turn said system into an equivalent but easier to solve system.

It should be noted (and can probably be inferred by our use of the word "equivalent") that the previous definition does define an equivalence relation. Every system is trivially a linear combination of itself, the definition is inherently symmetric, and if $A$ equivalent to $B$ and $B$ equivalent to $C$, then by distributivity, commutativity and associativity of $\mathbb{F}$,  $A$ and $C$ are equivalent as well.


## Row-equivalence

We define two **elementary row operations**, $scale_{r,c}$ and $add_{r,s}$ which are functions $\mathbb{F}^{m \times n} \rightarrow \mathbb{F}^{m \times n}$ defined, for $r,s \in [m]$, $r \neq s$, and $c \neq 0$, $c \in mathbb{F}$, by:

$$[scale_{r,c}(A)]_{ij} := \cases{
    c A_{ij} & \text{if } r = i \cr
    A_{ij} & \text{otherwise}}$$

$$[add_{r,s}(A)]_{ij} := \cases{
    A_{ij} + A_{sj} & \text{if } r = i \cr
    A_{ij} & \text{otherwise}}$$

$scale_{r,c}$ multiplies row $r$ by scalar $c$, while $add{r,s}$ adds row $s$ to row $r$.
