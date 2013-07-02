# Exercise 2.2.5 of Mac Lane and Birkhoff's Algebra, 3rd ed.

*If $(S, \Box)$ is such that $\Box$ is an associative binary operation on $S$ that obeys the cancellation law $a \Box b = a \Box c \implies b = c$ and $r \Box s = t \Box s \implies r = t$, then prove that if $S$ is finite, $(S, \Box)$ is a group, and that if $S$ is infinite it is not necessarily a group.*

The first thing to notice is that cancellation implies that left multiplication by $a$ for any $a \in S$ is an injective function. Any injective function from a finite set to itself must be a bijection, so thinking in terms of the multiplication table of $(S, \Box)$, each row gives us a bijection on $S$. In particular, there is some $x \in S$ such that $a \Box x = a$

We can use this to prove that, for any $g \in S$, $a \Box g = (a \Box x) \Box g = a \Box (x \Box g)$, which cancellation implies that $g = x \Box g$. Restated, $x$ is a left unit for $S$.

The same argument can be used to show that if $y \Box b = b$ for some $b$ and $y$, then $y$ is a right unit for $S$. But we just proved that $x$ is a left unit for $S$, so in particular $x \Box a = a$, proving that $x$ is a right unit as well, hence it is a two-sided unit.

Because left (right) multiplication is bijection, for every $g$ there's some $h$ such that $g \Box h = x$, as well as some $j$ such that $j \Box g = x$. From this we have:

$$j = x \Box j = (g \Box h) \Box j = g \Box (h \Box j) = g$$

So every element in fact has a two-sided inverse, which completes the proof that $S$ is a group under $\Box$.

For an example of an infinite $S$ that is not a group, just take $\mathbb{N}$ under addition. It's clearly associative, and in fact if $m + n = m + p$, then $n = p$ by the injectivity of the successor function that the defines the natural numbers (see: Peano postulates).
