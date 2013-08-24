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

A **compact** subset of a metric space $X$ is some $K \subseteq X$ such that any collection of open sets of $X$ whose union is a superset of $K$ has a finite sub-collection whose union is a superset of $K$.

We don't actually need to talk about the ambient space. Compact subsets stand alone:

**Proposition:** for $K \subseteq Y \subseteq X$, $K$ is compact in $X$ iff $K$ is compact in $Y$.

*Idea:* If $K$ compact in $Y$, for any open cover in $X$ of $K$, we intersect all the sets of the cover with $Y$ to get an open cover $\mathcal{S}$ of $K$. There's a finite subcover of $\mathcal{S}$ by hypothesis, so the original open sets of $X$ associated with the subcover also cover $K$, which yields the finite subcover. We can use the same passage between open sets of $Y$ and open sets of $X$ to prove the converse. $\Box$

We now speak simply of **compact metric spaces** since $K$ being compact means it is compact in any superspace.

In a compact metric space, we can view the compactness condition through complements: for any collection of closed sets with empty intersection, some finite number of them have empty intersection as well.

Any collection $\mathcal{F}$ of subsets of a metric space $X$ is said to have the **finite intersection property** if every finite subcollection of $\mathcal{F}$ has a non-empty intersection. Using this definition, we can rephrase compactness:

**Proposition:** $X$ is compact iff every collection of closed sets that possesses the finite intersection property has a non-empty intersection.

*Idea:* It's the contrapositive of the characterization via complements. $\Box$

A subset of a metric space is **bounded** if there is some number $M$ for which all $x, y$ in the subset have $d(x,y) \leq M$. The set of distances between points of a bounded set is then a subset of $\mathbb{R}$ that is bounded above, so we can (by the least upper bound property) define the **diameter** of a bounded set $A$ to be $diam(A) = sup \{d(x,y) : x, y \in A\}$. $\Box$

**Theorem:** Compact subsets are closed and bounded.

*Idea:* Suppose $K$ is a compact subset of $X$ and let $a \in K$. Just take all possible open balls around $x$. This is an open cover of $K$, so there's a finite subcover. The open balls are nested, so the biggest ball, say of radius $\epsilon$, of the subcover contains all of $K$. Then points in $K$ are no more than $2 \epsilon$ apart, so $K$ is bounded.

To prove that it's closed, pick some point $z \in X - K$. Then for each $k \in K$, construct two open balls, one around $z$, one around $k$, with radius of half of $d(k, z)$. These pairs of open balls are disjoint, and the balls around elements of $K$ are an open cover of $K$, so finitely many of them cover $K$ as well. Taking the smallest of the open balls around $z$ that correspond to the finite subcover, we obtain an open ball of $z$ that is disjoint from each of the sets in the finite subcover, and hence disjoint from $K$. This proves that $X - K$ is open. $\Box$

