% Notes on metric space topology

## Notation

In what follows we sometimes notate $f(x)$ by simply $fx$, which helps improve readability when many parentheses are in play.

## Introduction

Metric spaces are an abstract characterization of spaces equipped with a notion of distance. To each pair of elements we assign a number, the *distance*, between the two points. We must employ the real numbers to quantify distance since the length of the diagonal of a unit square is irrational, and it would be silly to lay out a theory of distance that could not account for the euclidean plane. We also only make use of the nonnegative reals, since it's not clear how to interpret *negative* distance.

Let $X$ be a set, and let $X_k$ for $k \leq |X|$ be the set of all subsets of $X$ with cardinality $k$. For example, $X_1$ is the collection of all singletons, and $X_0$ is a set consisting of the empty set.

A **metric space** is a pair $(X, d)$ where $d$ is a function $X_1 \cup X_2 \rightarrow \mathbb{R}$ such that:

  - For all $A \in X_1 \cup X_2$, $d(A) \geq 0$
  - $d(A) = 0$ iff $A$ is a singleton
  - For $A = \{x,y\}$, $B = \{y,z\}$, $C = \{x,z\}$ in $X_2$, $d(C) \leq d(A) + d(B)$ 

The first two just say that distances are nonnegative and distinct points have nonzero distance. Probably the most important property is the third, commonly known as the *triangle inequality*. It says, simply, that there's no way to shorten a trip from point A to point B by visiting some other point C on the way.

The most common formulation of metric spaces (and definitely easier to work with) is this: *d* is a function $X \times X \rightarrow \mathbb{R}$ such that:

  - $d(x,y) \geq 0$ for all $x$, $y$, and $d(x,y) = 0$ iff $x = y$.
  - $d(x,y) = d(y,x)$
  - $d(x,z) \leq d(x,y) + d(y,z)$

A **subspace** of a metric space $X$ is just a subset $S$ of $X$ together with the (set-theoretic) restriction of the metric of $X$ to $S$.

## Open and closed sets

An **open ball** of radius r around x is the set of all points in the metric space that are less than a distance r from x. In symbols:

  $$ B_r(x_0) = \{ x : d(x, x_0) < r \}$$

We will often call an open ball of radius $r$ an **$r$-ball**.

An **open set** is a set $U$ such that every $x \in U$ has an open ball $B_\epsilon(x)$ which is entirely contained in $U$.

Open balls are a kind of "primitive" open set that all other open sets are defined in terms of. We haven't yet proved that open balls are open sets, however. So let's do that.

**Lemma:** Open balls are open.

*Proof:* Let $B_\epsilon(x)$ be any open ball. Then $y$ is some distance $\delta \in \mathbb{R}$ from $x$ where $\delta < \epsilon$ (by definition of an open ball). We need to find some $\xi$-ball around $y$ that fits inside $B_\epsilon(x)$. 

Restating this condition using the definition of open balls, we need to find some $\xi \in \mathbb{R}$ such that every $z \in B_\xi(y)$ is less than $\epsilon$ from x. So we need to ensure that $d(x, z) < \epsilon$.

By the triangle inequality, $d(x, z) \leq d(x, y) + d(y, z)$. By hypothesis, $d(x,y) = \delta$, so if we could ensure that $d(y, z) < \epsilon - \delta$, we would be okay.

That's our $\xi$, then. Set $\xi = \epsilon - \delta$. Every point in the $\xi$-ball will then be in our $\epsilon$-ball.

We can restate the above proof with more words: after traveling from $x$ to $y$, we used up some $\delta$ of distance. If we go $\epsilon - \delta$ more distance from $y$, it is possible that we will get outside of the $\epsilon$-ball. So set $\epsilon - \delta$ as the radius we must stay strictly inside. This is an open ball around $y$ that is contained in the $\epsilon$-ball around $x$. $\Box$

The following lemma is fundamentally important.

**Topology Lemma for Open Sets:** In a metric space $(X, d)$:

 1. $\emptyset$, $X$ are both open.
 2. If $\mathcal{S}$ is an arbitrary collection of open sets in $X$, then $\bigcup \mathcal{S}$ is open
 3. If $U_1$ and $U_2$ are open subsets of $X$, then $X_1 \cap X_2$ is open.

Proof: 

(1) $\emptyset$ is vacuously open. $X$ is open because it contains *every* open ball, so it certainly contains *an* open for every point.

(2) If $x \in \bigcup \mathcal{S}$, then it must be in some open $U \in \mathcal{S}$. So  $\exists B_\epsilon(x) \subseteq U \subseteq \bigcup \mathcal{S}$. The arbitrary union of open sets is thus open.

(3) If $x \in U_1 \cap U_2$, there are open balls $B_\epsilon(x)$, $B_\delta(x)$ contained in $U_1$ and $U_2$, resp. The smaller of these balls is contained in both open sets, so is also in the intersection. $\Box$

A **neighborhood** of $x$ is an open set that contains $x$. We will use $\mathcal{N}_x$ to notate the set of all neighborhoods of a point $x$.

A set $S$ is **closed** in metric space $X$ if its complement $X - S$ is open. An result analogous to the topology lemma for open sets can be proved:

**Topology Lemma for Closed Sets:** In a metric space $(X, d)$:

 1. $\emptyset$, $X$ are both closed.
 2. If $\mathcal{S}$ is an arbitrary collection of closed sets in $X$, then $\bigcap \mathcal{S}$ is closed.
 3. If $U_1$ and $U_2$ are closed subsets of $X$, then $X_1 \cup X_2$ is closed.

*Proof:* (1) is immediate. The rest can be proved using DeMorgan's law [$X - (A \cup B) = (X-A) \cap (X-B)$] and the TLFOS. $\Box$

A **limit point** of a set $S$ in metric space $X$ is a point $p$ such that every open ball around $p$ intersects $S$ in some element of $S - p$. We notate the set of all limit points of $S$ as $\text{limpt}(S)$. An **isolated point** of a $S$ is an $x \in S$ such that there is some open ball around $x$ for which the only element of $S$ contained in it is $x$.

**Lemma:** The set $I$ of all isolated points of a subset $S$ of a metric space can be expressed as $I = S - \text{limpt}(S)$. $\Box$


The **closure** of a set $S$ in $X$, written $\overline{S}$, is defined as the minimal closed set containing $S$. In symbols:

$$ \overline{S} := \bigcap \{ F : S \subseteq F, F \text{ is closed} \}$$ 

**Alternate characterization of closures:** 
$$
\begin{split}
\overline{S} &= \{ x : \forall N \in \mathcal{N}_x N \cap S \neq \emptyset \}\\
&= \{ x : \forall \epsilon > 0 B_\epsilon(x) \cap S \neq \emptyset \}\\
&= S \cup \text{limpt}(S)
\end{split}
$$

*Proof:* TODO: fix this.

Call the first set $N$, the second set $B$. If $x \in N$, all open balls of $x$ are neighborhoods of $x$, so similarly $O \subseteq B$. 

If $x \in B$, then $x$ is in every closed $C$ containing $S$, because it could not possibly be in $X-C$, which is a subset of $X - S$ and is open and must therefore contain an open ball around every point (every open ball around $x$ intersects $S$). So $B \subseteq \overline{S}$.

Finally, $S \subseteq N$ and $N$ must be closed because if $y \in X - N$ then some neighborhood $M$ of $y$ doesn't intersect $S$ (otherwise $y$ would be in $N$), and $M$ contains an open ball of $y$, so that open ball is entirely contained in $X - N$. Thus $X - N$ is open, and $\overline{S} \subset N$ because $\overline{S}$ is defined to be the minimal closed set containing $S$. $\Box$

**Lemma:** A set $S$ is closed iff $\overline{S} = S$

*Proof:* By definition $S \subseteq \overline{S}$. If S is closed, then $\overline{S} \subseteq S$ since $\overline{S}$ is minimal. Conversely, if $\overline{S} = S$, then $\overline{S}$, being an intersection of closed sets, is closed. $\Box$

The **distance** of a point $x$ from a set $S$, written $dist(x,S)$, is defined to be $inf \{ d(x,s) : s \in S\}$.

**Lemma:** $\overline{S} = \{ x \in X : dist(x,S) = 0$

*Proof:* A point $x$ has $dist(x, S) = 0$ iff every open ball around $x$ intersects $S$. $\Box$

The **boundary** of a set $S$, notated $\partial S$, is $\{x \in X : \text{every } B_\epsilon(x) \text{ intersects both } S \text{ and } X-S\}$

**Lemma:** For a set $S$, $\partial S = \overline{S} \cap \overline{X-S}$

*Proof:* If $x$ is in the boundary, every epsilon ball intersects $S$ and $X-S$. So by the characterization lemma of closure, $x$ is in the closures of both $S$ and $X-S$. The converse direction works as well. $\Box$

**Lemma:**

 1. $\partial S$ = $\partial X-S$
 2. $\partial S$ is closed
 3. $\overline{S} = S \cup \partial S$

*Proof:* (1) holds from the definition because $X - (X - S) = S$.

For (2), we could use the previous lemma to say that $\partial S$ is the intersection of two closed sets and be done with it. For fun and profit, let's use the definition. Assume that $y$ is some point for which every open ball intersects $\partial S$. So for every open ball $B$ around $y$, there's some $x \in \partial S$ in $B$. But $B$, being an open ball, is open, so there's some open ball $C$ around x that fits entirely inside $B$. Every open ball of $x$ intersects both $S$ and $X-S$, so $B$, which was an arbitrary open ball of $y$, also intersects both $S$ and $X-S$. 

For (3), if $x \in \overline{S}$, then every open ball around $x$ intersects $S$. If every open ball around $x$ also intersects $X-S$, then $x \in \partial S$. Otherwise one open ball $B$ does not, so $x$ must be in $S$ (because it could not be in $X-S$. Conversely, by definition $S \subseteq \overline{S}$ and $\partial S \subseteq (\overline{S} \cap \overline{X-S}) \subseteq \overline{S}$. $\Box$

The dual notion to the closure of a set is the "interior" of a set, which is the largest open set contained in the set: for a given set $S$, we define the **interior** of $S$, $\mathring{S} := \bigcup \{ U : U \subseteq S, U \text{ is open}\}$.

**Lemma:** $\mathring{S} = X - \overline{X - S}$

*Proof:* Some point $y$ is not in every closed superset of $X-S$, iff it's in some open subset of $S$. $\Box$

## Continuity and limits

A function $f: X \rightarrow Y$ is **continuous at $x$** if for every $\epsilon$-ball around $f(x)$ there is a $\delta$-ball around $x$ that $f$ maps inside the $\epsilon$-ball. In symbols: $\forall \epsilon > 0 \exists \delta > 0 f(B_\delta(x)) \subseteq B_\epsilon(f(x))$.

We can interpret the above definition this way: $f$ allows us to ensure that we can keep the output of $f$ arbitrarily close to $f(x)$ by restricting the input to some range of points sufficiently close to $x$. More briefly: points that are close enough to $x$ get mapped to points close to $f(x)$.

**Lemma:** A function $f:X \rightarrow Y$ is continuous iff every open $V \subseteq Y$ has $f^{pre}(V)$ open in $X$.

*Proof:* If $V \subset Y$ is open in $Y$, then if $f^{pre}(V)$ is non-empty (the empty set is open), then any $x \in f^{pre}(V)$ has $f(x) \in V$, so some $\epsilon$-ball around $f(x)$ fits in $V$. By continuity some $\delta$-ball around $x$ maps into the $\epsilon$-ball around $f(x)$, which shows in particular that $x$ has some open ball around it that is contained in $f^{pre}(V)$. So the set is open.

Conversely if the inverse image of any open set in $Y$ is an open set in $X$, then  for any $x \in X$, any $\epsilon$-ball around $f(x)$ is open in $Y$, so the inverse image of that ball is open. Call that inverse image $A$. Then $A$, being open, contains some open ball around $x$. This open ball is the $\delta$-ball we seek. $\Box$

If $A \subseteq X$ and $c$ is a limit point of $A$, then the function $f: A \rightarrow Y$ has a **limit of $L$ at $c$** if $\forall \epsilon > 0 \exists $\delta > 0$ such that for all $x \in A - c$, if $d(x, c) < \delta$, $d(fx, L) < \epsilon$. We denote this situation as

$$ \lim_{x \to c} f(x) = L$$

Two things to note about this definition:

 1. functional limits are defined for points that are not in the domain of the function, provided that they are limit points of the domain

 2. functional limits are not necessarily defined for all the points in the domain, because isolated points of the domain do not have a limit.


**Lemma:** For $f: X \rightarrow Y$ with $c \in X$ a limit point of $X$, $f$ is continuous at $c$ iff $\lim_{x \to c} f(x) = f(c)$.

*Proof:* TODO? $\Box$

## Compactness

A subset $S$ of some metric space is **compact** if for every collection $\mathcal{U}$ of open sets whose union contains $S$, there's a finite subcollection $\{U_1, \ldots, U_n\}$ whose union also contains $S$. We call any collection of open sets whose union contains $S$ an **open cover** of $S$, and the finite subcollection is called a **finite sub-cover**. Restated, a subset is compact if every open cover has a finite subcover.

A set S in a metric space $(X,d)$ is **bounded** if for some $x \in X$, $S \subseteq B_\epsilon(x)$ for some $\epsilon > 0$.

**Lemma:** A compact set $S$ in a metric space is bounded.

*Proof:* Suppose $S$ is compact and non-empty (empty sets are clearly bounded). Fix a point $x \in S$. The set of all open balls of $x$ covers $S$ (it covers the whole metric space, actually). This is an open cover of $S$, so there's at least one finite subcover $\{ B_{r_1}(x), \ldots, B_{r_n}(x) \}$. The union of these is just the biggest open ball, $B_N(x)$ where $N := max\{r_1, \ldots, r_n\}$. Hence this open ball contains $S$, meaning $S$ is bounded. $\Box$

**Lemma:** A compact subset $S$ of some metric space $X$ is closed.

*Proof:* Let $y$ be any point in $X-S$. For any $x \in S$ there is at least one pair of open balls around $x$ and $y$ that are disjoint (take $\epsilon_x = d(x,y)$). Then the collection of all such balls $B_{\epsilon_x}(x)$  is an open cover of $S$, which, being compact, implies the existence of a finite number of them that cover $S$. These open balls $B_{\epsilon_1}(x_1), \ldots, B_{\epsilon_n}(x_n)$ have corresponding open balls $D_{\delta_i}(y)$ around $y$ that are disjoint from the $B_{\epsilon_i}(x_i)$'s. The smallest ball $D_{\delta_i}(y)$ is disjoint from the whole union of $B_{\epsilon_k}(x_k)$'s, so it's disjoint from $S$, meaning contained in $X-S$. So $X-S$ is open. $\Box$

**Lemma:** If $K$ is a compact metric space, $f: K \rightarrow Y$ is a continuous function, with $Y$ arbitrary, then the image $f(K)$ is compact in $Y$.

*Proof:* Let $\mathcal{U}$ be an open cover of in $img(f)$, define $\mathcal{U}^{pre} = \{f^{pre}(A) : A \in \mathcal{U}\}$. Then $\mathcal{U}^{pre}$ covers $K$ since every $k \in K$ is mapped by $f$ to some $f(k) \in img(f)$, and $\mathcal{U}$, covering all of $img(f)$, has some $A_k$ containing $f(k)$, so $f^{pre}(A_k)$ contains $k$. But $K$ is compact, so $\mathcal{U}^{pre}$ has a finite subcover $\mathcal{F}$. All the sets in the subcover are the pre-images of sets in $img(f)$, i.e. of the form $f^{pre}(S)$ for some $S$. So $\mathcal{F} = \{ f^{pre}(S_1), \ldots, f^{pre}(S_n)\}$, and the $S_i$ form an open cover of $img(f)$ (since $f(f^{pre}(X)) = X$. Furthermore, the $S_i$'s are a subcollection of $\mathcal{U}$ by definition of $\mathcal{F}$. So $f(K)$ is compact. $\Box$


## Connectedness

A metric space $X$ is **disconnected** if there are two open subsets $S$ and $T$ of $X$ that are disjoint and such that $S \cup T = X$. $X$ is **connected** if its not disconnected.

**Lemma:** If $X$ is connected and $Y$ is an arbitrary metric space and $f: X \rightarrow Y$ is continuous, then $f(X)$ is a connected subspace of $Y$.

*Proof:* If not, $f(X) = A \cup B$, where $A = S \cap f(X)$ and $B = T \cap f(Y)$, $S$ and $T$ open in $Y$. So by continuity, the pre-images of $S$ and $T$ are also open in $X$. Since $S$ and $T$ cover the image of $f$, their pre-images cover $X$. They have to be disjoint as well, by the definition of a function. We've just proved that $X$ is disconnected, contrary to hypothesis. $\Box$


## Sequences

A sequence in a metric space $X$ is a function $f: \mathbb{N} \rightarrow X$. In other words, it's an indexed family of elements of $X$ where the indexing set is the natural numbers. We notate sequences as $(x_n)$, where it is understood that this represents a sequence $n \mapsto x_n$ for all $n \in \mathbb{N}$.

A sequence $(x_n)$ **converges** to an element $c \in X$ if for every $\epsilon > 0$ there is a $N \in \mathbb{N}$ such that whenever $n \geq N$, $d(x_n, c) < \epsilon$. In other words, for any given $epsilon$, there are only finitely many terms of the sequence that are not within the $\epsilon$-ball around $c$.

If $(x_n)$ converges to $c$, we sometimes write $(x_n) \rightarrow c$.

A function $f: X \rightarrow Y$ between two metric spaces is **sequentially continuous at $c$** (for $c \in X$) if, for any sequence $(x_n) \rightarrow c$ in $X$, the sequence $(f x_n)$ converges to $f(c)$.

**Lemma:** $f: X \rightarrow Y$ is continuous at $c$ iff it's sequentially continuous at $c$.
*Proof:* If $f$ is continuous and $(x_n) \rightarrow c$, then for any $\epsilon > 0$, there's some $\delta$-ball around $c$ such that all points there get mapped to points in the $\epsilon$-ball around $f(c)$. But there are only finitely many terms of $(x_n)$ that aren't within that $\delta$-ball around $c$, so there are only finitely many terms $f(x_n)$ that aren't within the $\epsilon$-ball around $f(c)$.

Conversely, if $f$ isn't continuous, some $\epsilon > 0$ is such that we can construct a sequence $(z_n)$ in $X$ that converges to $c$, but for which $(f z_n)$ lies entirely outside the $\epsilon$-ball around $f(c)$. Hence $(f z_n)$ does not converge to $f(c)$.
