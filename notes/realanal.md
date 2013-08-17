% Notes on real analysis

## Single-variable

The real numbers, $\mathbb{R}$, are an ordered field with the least upper bound property. If you don't know what that means, these are not the real analysis notes you're looking for. I think there's a proof that such a field is unique, but I'm not particularly concerned with it. There are ways of building the reals from the rationals (via Dedekind cuts or via Cauchy sequences of rationals) but again we are not too concerned with that here.

$\mathbb{R}$ can be made a metric space by defining $d(x,y) = |x - y|$.

An **interval** of $\mathbb{R}$ is a subset $I$ such that for all $x, y \in I$, for all $z \in \mathbb{R}$ such that $x < z < y$, then $z \in \mathbb{R}$.


**Proposition:** A subspace $S$ of $\mathbb{R}$ is connected iff $S$ is an interval.

*Proof:* Note first that for the empty interval, it can't possibly be disconnected, so it is connected. The degenerate interval ${a}$ for some $a \in \mathbb{R}$ similarly cannot be disconnected. So we assume $S$ has at least two elements.

If $S \subseteq \mathbb{R}$ is not an interval, then let $x, y \in S$ and without loss of generality suppose $x < y$. By hypothesis there is some $z$ not in $S$ such that $x < z < y$. $(- \infty, z)$ and $(z, \infty)$ are open in $\mathbb{R}$, so $A = S \cap (- \infty, z)$ and $B = S \cap (z, \infty)$ are open in $S$, disjoint and union to $S$. I.e., $S$ is disconnected.

Conversely, if $S$ is a disconnected interval, then $S = A \cup B$, for $A$ and $B$ non-empty, open and disjoint. We have some $x \in A, y \in B$ and without loss of generality we assume $x < y$. Consider

$$s := \text{inf}\{b \in B : x < b\}$$

which exists (by the least upper bound property) since we know $x < y$. $s \geq x$ since $x$ is itself a lower bound. Suppose $s > x$. There are no elements of $B$ smaller than $s$ but greater than $x$, so $(x, s)$ is entirely contained in $A$ since it is a subset of $S$ ($S$ is an interval).

The problem is that for all $\epsilon > 0$, there is some $b \in B$ such that $s < b < s + \epsilon$. So all $\epsilon$-balls around $s$ intersect both $A$ and $B$. This is an issue since $s \in S$, meaning it must be in $A$ or in $B$, which are both supposed to be open. So after all, $s = x$. But this is still a problem, because every $\epsilon$-ball around $x$ intersects $B$ and $A$ is open.

So $S$ must not be disconnected after all. $\Box$
