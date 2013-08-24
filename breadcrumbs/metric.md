# Notes on metric spaces.

In a metric space, we can assign a non-negative real number between any two points, and the assignment function obeys certain properties:

 - A point is always zero distance from itself, and distinct points are always a greater distance apart.

 - The triangle inequality holds: $d(x, z) \leq d(x, y) + d(y, z)$

An **open ball** around some point $x$ in a metric space is the set of all points that are within some $\epsilon \geq 0$. A set is **open** if every point in it has some open ball contained in the set.

We can make a **subspace** from some metric space $X$ by taking any $Y \subseteq X$ and restricting the metric to $Y$.

Subspaces introduce the potential for confusion since a subset of $X$ can either be considered open with respect to the metric space $X$ or with respect to a subspace $Y$ of $X$. With this in mind, we introduce the notation

$$B_Y(x, \epsilon)$$

for the open ball of radius $\epsilon$ around $x$ in subspace $Y$.

**Proposition:** For metric space $X$, $Y \subseteq X$, $a \in Y$, $\epsilon > 0$, then $B_Y(a, \epsilon) = B_X(a, \epsilon) \cap Y$.

*Idea:* $B_X(a, \epsilon)$ is obtained by starting with $B_Y(a, \epsilon)$ and filling in all the points in $X$ that are within $\epsilon$ of $a$ but missing from $Y$. $\Box$

We can turn this into an understanding of what the open sets of a subspace are:

A set $U$ is open in $Y$ iff $U = Y \cap V$ for some $V$ open in $X$.

*Idea:* $U$ open in $Y$ is a union of some open balls in $Y$. By the previous proposition, we can "fill in" these open balls with points from $X - Y$ to obtain open balls in $X$. The union of all of these open balls of $X$, call it $B$, is an open set which, when intersected with $Y$, gives $U$. The converse works by the reverse trick of turning an open set $V$ into a collection of open balls, throwing away the elements $X - Y$ to obtain a set open in $Y$. $\Box$

