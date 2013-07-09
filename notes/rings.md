# Notes on ring theory

An **associative ring** is a triple $(R, +, \cdot)$ where $(R, +)$ is an abelian group and $\cdot$ is an associative binary operation on $R$ such that $\forall r, s, t \in R$:

 - $r \cdot (s + t) = r \cdot s + r \cdot t$
 - $(r + s) \cdot t = r \cdot t + s \cdot t$

The operation $\cdot$ is often called *multiplication* (as the notation suggests).

A **unital ring** or **ring with unit/identity** is an associative ring which has a multiplicative identity, i.e. there's some element $1 \in R$ such that $r \cdot 1 = 1 \cdot r = r$ for all $r \in R$.

A **commutative ring** is a ring where multiplication is commutative.

A **zero divisor** of a ring $R$ is an element $a \in R$, $a \neq 0$, such that $\exists b \neq 0$ and $ab = 0$.

An **integral domain** is a commutative ring with no zero divisors. (Herstein apparently does not require integral domains to have a unit).

A **division ring** is a ring whose non-zero elements form a group under multiplication.

Note that a division ring has a unit.

A **field** is a commutative division ring. I'm not clear if this excludes the trivial ring. If $F = \{0\}$ with $0+0 = 0$ and $0 \cdot 0 = 0$, then does the set of non-zero elements form a group? Aha, the answer is no, because a group cannot be empty. So it excludes the trivial ring.

**Lemma:** In any ring:

 1. $0a = a0 = 0 \forall a$
 2. $a(-b) = -(ab) = (-a)b$
 3. $(-a)(-b) = ab$

*Proof:* (1) $0a = (0+0)a = 0a + 0a$. (2) a(-b) + ab = a(-b +b) = a0 = 0$. Also, (-a)b + ab = (-a + a)b = 0b = 0b. It follows from cancellation. (3) $(-a)(-b) + -(ab) = (-a)(-b) + (-a)b = -a0 = 0$. $\Box$

**Lemma:** In any ring with unit, 
 1. $(-1)a = -a$
 2. $(-1)(-1) = 1$

*Proof:* $a + (-1)a = 1a + (-1)a = (1 + -1)a = 0a = 0$, which establishes (1). (2) follows because (1) gives us $(-1)(-1) = -(-1)$, which is $1$ since the inverse of an inverse is the original in any group. $\Box$
