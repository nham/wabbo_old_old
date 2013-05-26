# Let's Get $\mathbb{R}$

The real numbers are defined thusly: a pair $(\mathbb{R}, \leq)$ where 

 1. $\mathbb{R}$ is a non-trivial ($1 \neq 0$) commutative ring and all non-zero elements have multiplicative inverses $(i.e. a *field*)$
 2. $(\mathbb{R}, \leq)$ is a total order
 3. $a \leq b$ implies $a + c \leq b + c$ for all $a,b,c \in \mathbb{R}$
 4. $0 \leq a$, $0 \leq b$ implies $0 \leq ab$
 5. every $S \subseteq \mathbb{R}$ bounded above has a least upper bound.

Points 1-4 mean that the real numbers are an *ordered field*. The fifth postulate is more popularly known as the **axiom of completeness** or, more specifically, the **least upper bound property**, and it endows $\mathbb{R}$ with most of the properties we look for in analysis.

The reals, in part being an abelian group over addition, have the familar properties of basic groups, including 1) the cancellation laws, 2) uniqueness of additive identity (zero), 3) uniqueness of additive inverses, and 4) the inverse of the inverse being equal to the original element.

These four properties also hold over field multiplication for the non-zero elements, as the non-zero elements of a field form an abelian group as well.

We also have that for any $x$, $0x = 0 = x0$, that $(-x)y = -(xy) = x(-y)$, and $(-x)(-y) = xy$, as these are true in any ring.

A particularly important property of fields is that they have no zero divisors. Formally: for any $x$ and $y$, $xy = 0$ implies $x = 0$ or $y = 0$. *Proof:* Assuming $x \neq 0$, it has a multiplicative inverse $\frac{1}{x}$. hence $ \frac{1}{x} x y = \frac{1}{x} 0 = 0$, or $y = 0$.

I will zoom in on these following properties not because they are harder than the above statements that I glossed over, but because they are less familiar to me. I'm not writing this for you at all, dear reader, unless you are future me. Which, in that case, hello!

If $(F, \sqsubseteq)$ is an ordered field, we define $x \sqsubset y$ if $x \sqsubseteq y$ holds and $x \neq y$. The following propositions hold:

 1. $x \sqsupseteq 0$ implies $-x \sqsubseteq 0$
 2. $x \sqsupseteq 0$ and $y \sqsubseteq z$ implies $xy \sqsubseteq xz$
 3. $x \sqsubseteq 0$ and $y \sqsubseteq z$ implies $xy \sqsupseteq xz$
 4. For all $x$, $x^2 \sqsupseteq 0$.
 5. $0 \sqsubset x \sqsubset y$ implies $ 0 \sqsubset \frac{1}{y} \sqsubset \frac{1}{x}$

*Proof:* (1) $0 \sqsupseteq x$ implies $-x + 0 \sqsupseteq -x + x$, or $-x \sqsupseteq 0$. (2) If $x \sqsupseteq 0$ and $z \sqsupseteq y$, then $z-y \sqsupseteq 0$, so $x(z-y) \sqsupseteq 0$, or $xz \sqsupseteq xy$. (3) If $x \sqsubseteq 0$, $-x \sqsupseteq 0$, so $z \sqsupseteq y$, implies $z-y \sqsupseteq 0$ as before, and $-x(z-y) \sqsupseteq 0$, so $xy \sqsupseteq xz$. (4) If $x \sqsupseteq 0$, we use (2) to get $x^2 \sqsupseteq 0$. If $x \sqsubset 0$, $-x \sqsupset 0$, and we again use (2) to obtain $0 \sqsubset (-x)^2 = x^2$

To  prove (5), note that a corollary to (4) is that $1^2 = 1 \sqsupset 0$. So $1 = x \frac{1}{x} > 0 = x0$. This means that if $x \sqsupset 0$, then by the converse to (2), \frac{1}{x} \sqsupset 0$. So If $0 \sqsubset x \sqsubset y$, then both $\frac{1}{x} and $\frac{1}{y}$ are greater than $0$. Hence $\frac{1}{xy} \sqsupset 0$, so $\frac{1}{xy} x \sqsubset \frac{1}{xy} y$, or $\frac{1}{y} \sqsubset \frac{1}{x}$. $\Box$

Lastly, we prove a property that is dual to LUB property of the reals.

**Proposition:** If $(S, \leq)$ is any total order with the LUB property (all non-empty sets that are bounded above have least upper bounds), then all sets that are bounded below have *greatest lower bounds*.

*Proof:* If $X \subseteq S$ and there's some $b \in S$ that is a lower bound of $X$, let

$$L := \{ l \in X : \forall x \in X l \leq x \}$$

This set $L$ is non-empty and every $x \in X$ is an upper bound of $L$ by definition, so $L$ has a supremum in $X$, call it $c$. Being a supremum of $L$, if $a < c$ then there's some $z \in L$ such that $a < z \leq c$, so that no $x \in X$ could be less than $c$. This means $c \in L$. All lower bounds must be $\leq c$ as well, since otherwise it's not an upper bound of $L$. So $c$ is the greatest lower bound. $\Box$

There are a couple of ways to construct the reals from the rationals. I've seen both approaches before in the past, but I'm skipping this at the moment. I will note that Rudin uses Dedekind cuts to construct them in PMA. Here we will simply postulate their existence.
