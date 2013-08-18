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

We similarly define a **closed ball** of radius r around x to be:

  $$ B_r[x_0] = \{ x : d(x, x_0) \leq r \}$$

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

**Lemma:** If $S \subseteq X$ is a subspace of metric space $X$, then $U$ is open in $S$ iff $U = A \cap S$ for an open subset $A$ of $X$.

*Proof:* TODO: define the notation $B_X(\epsilon, s)$. The key fact is that for any $s \in S$, $B_S(\epsilon, s) = B_X(\epsilon, s) \cap S$. Since any open set is a union of open balls, if $U$ open in $S$, take the open balls that make it up and fill them in so that they're open balls in $X$. Their union is now an open set in $X$, which when intersected with $S$ yields $U$ (since we didn't add any new points of $S$ when expanding). Conversely, for open $A$ in $X$, the intersection of $A$ with $S$ is the same thing as "shrinking" $A$'s open balls to open balls of $S$. $\Box$.

A **neighborhood** of $x$ is an open set that contains $x$. We will use $\mathcal{N}_x$ to notate the set of all neighborhoods of a point $x$.

A set $S$ is **closed** in metric space $X$ if its complement $X - S$ is open. An result analogous to the topology lemma for open sets can be proved:

**Topology Lemma for Closed Sets:** In a metric space $(X, d)$:

 1. $\emptyset$, $X$ are both closed.
 2. If $\mathcal{S}$ is an arbitrary collection of closed sets in $X$, then $\bigcap \mathcal{S}$ is closed.
 3. If $U_1$ and $U_2$ are closed subsets of $X$, then $X_1 \cup X_2$ is closed.

*Proof:* (1) is immediate. The rest can be proved using DeMorgan's law [$X - (A \cup B) = (X-A) \cap (X-B)$] and the TLFOS. $\Box$

**Proposition:** Closed balls are closed.

*Proof:* TODO $\Box$

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

**Proposition:** If $f: X \rightarrow Y$ and $g: Y \rightarrow Z$ are continuous at $c \in X$ and $f(c) \in Y$, respectively, then $g \circ f$ is continuous at $c$.

*Proof:* TODO $\Box$


If $A \subseteq X$ and $c$ is a limit point of $A$, then the function $f: A \rightarrow Y$ has a **limit of $L$ at $c$** if $\forall \epsilon > 0 \exists $\delta > 0$ such that for all $x \in A - c$, if $d(x, c) < \delta$, $d(fx, L) < \epsilon$. We denote this situation as

$$ \lim_{x \to c} f(x) = L$$

Two things to note about this definition:

 1. functional limits are defined for points that are not in the domain of the function, provided that they are limit points of the domain

 2. functional limits are not necessarily defined for all the points in the domain, because isolated points of the domain do not have a limit.


**Lemma:** For $f: X \rightarrow Y$ with $c \in X$ a limit point of $X$, $f$ is continuous at $c$ iff $\lim_{x \to c} f(x) = f(c)$.

*Proof:* TODO? $\Box$

## Sequences

A sequence in a metric space $X$ is a function $f: \mathbb{N} \rightarrow X$. In other words, it's an indexed family of elements of $X$ where the indexing set is the natural numbers. We notate sequences as $(x_n)$, where it is understood that this represents a sequence $n \mapsto x_n$ for all $n \in \mathbb{N}$.

A sequence $(x_n)$ **converges** to an element $c \in X$ if for every $\epsilon > 0$ there is a $N \in \mathbb{N}$ such that whenever $n \geq N$, $d(x_n, c) < \epsilon$. In other words, for any given $epsilon$, there are only finitely many terms of the sequence that are not within the $\epsilon$-ball around $c$.

If $(x_n)$ converges to $c$, we sometimes write $(x_n) \rightarrow c$.

A set S in a metric space $(X,d)$ is **bounded** if for some $x \in X$, $S \subseteq B_\epsilon(x)$ for some $\epsilon > 0$. A sequence $(x_n)$ is bounded if the set of its terms is bounded.

**Proposition:** A convergent sequence is bounded.

*Proof:* If $(x_n) \rightarrow c$, then for any $\epsilon > 0$, all but finitely many terms are contained in the $\epsilon$-ball around $c$. So setting $\delta = max{\epsilon, d(c, x_1) + 1, \ldots, d(c, x_n) + 1}$, all terms are contained within the $\delta$ ball around $c$. $\Box$

A function $f: X \rightarrow Y$ between two metric spaces is **sequentially continuous at $c$** (for $c \in X$) if, for any sequence $(x_n) \rightarrow c$ in $X$, the sequence $(f x_n)$ converges to $f(c)$.

**Lemma:** $f: X \rightarrow Y$ is continuous at $c$ iff it's sequentially continuous at $c$.
*Proof:* If $f$ is continuous and $(x_n) \rightarrow c$, then for any $\epsilon > 0$, there's some $\delta$-ball around $c$ such that all points there get mapped to points in the $\epsilon$-ball around $f(c)$. But there are only finitely many terms of $(x_n)$ that aren't within that $\delta$-ball around $c$, so there are only finitely many terms $f(x_n)$ that aren't within the $\epsilon$-ball around $f(c)$.

Conversely, if $f$ isn't continuous, some $\epsilon > 0$ is such that we can construct a sequence $(z_n)$ in $X$ that converges to $c$, but for which $(f z_n)$ lies entirely outside the $\epsilon$-ball around $f(c)$. Hence $(f z_n)$ does not converge to $f(c)$. $\Box$


And now, a sequential characterization of functional limits:

**Proposition:** First, for metric space $X$ and $c \in X$, we define an *approximation sequence of $c$ in $X$* to be a sequence in $X$ for which every term $x_i \neq c$, but $(x_n) \rightarrow c$.

Now, if $A \subseteq X$, $f: A \rightarrow Y$, $c$ is a limit point of $A$, then $\lim_{x \to c} f(x) = L$ iff every approximation sequence $(x_n)$ of $c$ in $A$ is such that $(f x_n) \rightarrow L$.


*Proof:* TODO $\Box$


## Compactness

A subset $S$ of some metric space is **compact** if for every collection $\mathcal{U}$ of open sets whose union contains $S$, there's a finite subcollection $\{U_1, \ldots, U_n\}$ whose union also contains $S$. We call any collection of open sets whose union contains $S$ an **open cover** of $S$, and the finite subcollection is called a **finite sub-cover**. Restated, a subset is compact if every open cover has a finite subcover.

The following allows us to speak simply of a *compact space*, not merely of compact subsets of some metric space.

**Lemma:** If $X$ is a metric space, and $K \subseteq Y \subseteq X$, then $K is compact in $Y$ iff $K$ is compact in $X$.

*Proof:* If $K$ compact in $X$, and $\mathcal{S}$ is an open cover in $Y$ of $K$, then each $S_i \in \mathcal{S}$ has some $U_i \subseteq X$ such that $U_i \cap Y = S_i$. So the family $\{U_i\}$ is an open cover of $K in $X$, and it has a finite subcover $U_1, \ldots, U_n$. Intersecting these with $Y$ we get a finite subcover in $Y$, so $K$ is compact in $Y$ as well.

The same trick works when we start with $K$ compact in $Y$: an open cover in $X$ can have its elements intersected with $Y$ to obtain an open cover in $Y$, which has a finite subcover in $Y$. Each element of this finite subcover is the intersection of an open set of $X$ with $Y$, and the open sets are elements of the original cover in $X$. $\Box$.


**Lemma:** A compact set $S$ in a metric space is bounded.

*Proof:* Suppose $S$ is compact and non-empty (empty sets are clearly bounded). Fix a point $x \in S$. The set of all open balls of $x$ covers $S$ (it covers the whole metric space, actually). This is an open cover of $S$, so there's at least one finite subcover $\{ B_{r_1}(x), \ldots, B_{r_n}(x) \}$. The union of these is just the biggest open ball, $B_N(x)$ where $N := max\{r_1, \ldots, r_n\}$. Hence this open ball contains $S$, meaning $S$ is bounded. $\Box$

**Lemma:** A compact subset $S$ of some metric space $X$ is closed.

*Proof:* Let $y$ be any point in $X-S$. For any $x \in S$ there is at least one pair of open balls around $x$ and $y$ that are disjoint (take $\epsilon_x = d(x,y)$). Then the collection of all such balls $B_{\epsilon_x}(x)$  is an open cover of $S$, which, being compact, implies the existence of a finite number of them that cover $S$. These open balls $B_{\epsilon_1}(x_1), \ldots, B_{\epsilon_n}(x_n)$ have corresponding open balls $D_{\delta_i}(y)$ around $y$ that are disjoint from the $B_{\epsilon_i}(x_i)$'s. The smallest ball $D_{\delta_i}(y)$ is disjoint from the whole union of $B_{\epsilon_k}(x_k)$'s, so it's disjoint from $S$, meaning contained in $X-S$. So $X-S$ is open. $\Box$

**Lemma:** If $K$ is a compact metric space, $f: K \rightarrow Y$ is a continuous function, with $Y$ arbitrary, then the image $f(K)$ is compact in $Y$.

*Proof:* Let $\mathcal{U}$ be an open cover of in $img(f)$, define $\mathcal{U}^{pre} = \{f^{pre}(A) : A \in \mathcal{U}\}$. Then $\mathcal{U}^{pre}$ covers $K$ since every $k \in K$ is mapped by $f$ to some $f(k) \in img(f)$, and $\mathcal{U}$, covering all of $img(f)$, has some $A_k$ containing $f(k)$, so $f^{pre}(A_k)$ contains $k$. But $K$ is compact, so $\mathcal{U}^{pre}$ has a finite subcover $\mathcal{F}$. All the sets in the subcover are the pre-images of sets in $img(f)$, i.e. of the form $f^{pre}(S)$ for some $S$. So $\mathcal{F} = \{ f^{pre}(S_1), \ldots, f^{pre}(S_n)\}$, and the $S_i$ form an open cover of $img(f)$ (since $f(f^{pre}(X)) = X$. Furthermore, the $S_i$'s are a subcollection of $\mathcal{U}$ by definition of $\mathcal{F}$. So $f(K)$ is compact. $\Box$

**Lemma:** If $K$ is a compact metric space, then every sequence $(x_n)$ has a convergent subsequence.

*Proof:* Suppose not, so some $(x_n)$ in $K$ doesn't have any convergent subsequence. That means for all $x \in K$, $x$ is not the limit of any subsequence $(x_{n_k})$. This is the same as saying that only finitely many terms of $(x_n)$ are in some $\epsilon_x$ ball around $x$ (otherwise you could make a convergent subsequence), i.e. that there is some $n_x \in \mathbb{N}$ for which $n \geq n_x$ all have $x_n$ not in the $\epsilon_x$ ball around $x$. $\Box$

Now, the set of all such $\epsilon_x$ balls (remember, there is one for each $x \in K$ since *every* element isn't the limit of a convergent subsequence) is an open cover of $K$, and by compactness there are finitely many points $y_1, \ldots, y_n$ such that the balls $\epsilon_{y_i}$ cover $K$. But each of these balls contains only finitely many terms of the sequence, which is nonsense since the sequence was supposed to be contained in $K$.

A metric space is said to be **sequentially compact** if every sequence in the metric space has a convergent subsequence. The last lemma says that every compact metric space is sequentially compact. We now endeavor to prove the converse, and hence their equivalence, for metric spaces.

It will require an intermediate step and some definitions:

A metric space is **complete** if every Cauchy sequence in the space converges in the space. (TODO: define "Cauchy sequence", lol).

If $X$ is a metric space and $\epsilon > 0$, then an **$\epsilon$-net** is a subset $A$ of $X$ such that $X = \bigcup_{y \in A} B(\epsilon, y)$. In words, its subset for which the collection of $\epsilon$-balls around $y \in A$ covers $X$.

A metric space $X$ is **totally bounded** if for every $\epsilon > 0$, $X$ has a finite $\epsilon$-net.

**Proposition:** A metric space is totally bounded iff every sequence has a Cauchy subsequence.

*Proof:* Let $X$ be a metric space. If $X$ isn't totally bounded, let $\epsilon > 0$ be such that it has no finite $\epsilon$-net. Then we can pick an arbitrary $x_1 \in X$. Having picked $x_1, \ldots, x_k$, pick $x_{k+1}$ not in $\bigcup_1^k B(\epsilon, x_i)$. We can always do this, because otherwise we would have a finite $\epsilon$-net of $X$.

Now for all $x_m, x_n$ with $m \neq n$, $d(x_m, x_n) \geq \epsilon$ by construction, so no subsequence is Cauchy. 

Conversely, suppose $X$ is totally bounded. For any $\epsilon > 0$ and any sequence $(z_n)$, we can obtain a subsequence $(z_{n_k})$ contained entirely within one of the $\epsilon$-balls, since either (a) the sequence takes on finitely many different values, or (b) it takes on infinitely many values, and there are only finitely many balls. In particular, we can obtain subsequence $(x_{n_k}^{(1)})$ contained within some $\frac{1}{2}$-ball, and (proceeding inductively now) applying the same proposition again to $(x_{n_k}^{(k)})$, some subsequence $(x_{n_k}^{(k+1)})$ is contained entirely within a $\frac{1}{2(k+1)}$-ball.

Note that for every $(x_n^{(k)})$, every pair of terms in this sequence is such that $d(x_n^{(k)}, x_m^{(k)}) < \frac{1}{k}$.

Now, the sequence $(x_k^{(k)})$ is a subsequence of $(x_n)$ by definition, and for all $m, n \geq N$, $d(x_m^{(m)}, x_n^{(n)}) < \frac{1}{N}$ since both are terms in the sequence $(x_N^{(N)})$. We can certainly make the distance between terms arbitrarily small; this is a Cauchy subsequence. $\Box$.


**Proposition:** For a metric space $K$, these are equivalent:

 1. $K$ is compact
 2. $K$ is complete and totally bounded.
 3. $K$ is sequentially compact 

*Proof:* We have established that (1) implies (3). We now prove (3) implies (2) implies (1).

Let $(x_n)$ be a Cauchy sequence in $K$. By hypothesis $K$ is sequentially compact, so there is a subsequence $(x_{n_k})$ which converges to a $c \in K$. Now for any $m, n \in \mathbb{N}$,

$$d(x_n, c) \leq d(x_n, x_m) + d(x_m, c)$$

Let $\epsilon > 0$. We can find an $N$ such that all $m, n \geq N$ are within $\epsilon/2$ of each other. But there's also a point in the subsequence after which all terms of the subsequence are within an $\epsilon/2$ of $c$. So just pick the max of $N$ and the point for the subsequence. Then all terms $x_n$ after this point have $d(x_n, c) < \epsilon$. So $(x_n)$ converges to $c$. This establishes that $K$ is complete.

$K$'s completeness and its sequential compactness establishes that every sequence in $K$ has a Cauchy subsequence, and by a previous proposition $K$ must be totally bounded.


TODO: Prove (complete and totally bounded) implies compact.

$\Box$


## Connectedness

A metric space $X$ is **disconnected** if there are two non-empty, open subsets $S$ and $T$ of $X$ that are disjoint and such that $S \cup T = X$. $X$ is **connected** if its not disconnected.

**Lemma:** If $X$ is connected and $Y$ is an arbitrary metric space and $f: X \rightarrow Y$ is continuous, then $f(X)$ is a connected subspace of $Y$.

*Proof:* If not, $f(X) = A \cup B$, where $A = S \cap f(X)$ and $B = T \cap f(Y)$, $S$ and $T$ open in $Y$. So by continuity, the pre-images of $S$ and $T$ are also open in $X$. Since $S$ and $T$ cover the image of $f$, their pre-images cover $X$. They have to be disjoint as well, by the definition of a function. We've just proved that $X$ is disconnected, contrary to hypothesis. $\Box$


## Products

If $(X_i, d_i)$, $i \in [n]$ is some finite number of metric spaces, we can form the **product space** $(\prod_i^n X_i, d)$ where $d$ is defined by:

$$d[(x_1, \ldots, x_n), (y_1, \ldots, y_n)] := max{d_1(x_1, y_1), \ldots, d_n(x_n, y_n)}$$

There are actually a few choices we can make for the product metric, but this choice, the *sup metric*, is fairly simple to work with.

It's clearly always a nonnegative real, and is zero iff each $d(x_i, y_i)$ is zero, which is true iff $x_i = y_i$. Hence $d$ is positive definite. Symmetry holds because it holds in each $d_i$.

So for $(x_1, \ldots, x_n)$, $(y_1, \ldots, y_n)$, $(z_1, \ldots, z_n)$, for each $i$ we have $d(x_i, z_i) \leq d(x_i, y_i) + d_i(y_i, z_i)$. So letting $M = d(x, z)$, and letting $i \Diamond x y$ stand for $d_i(x_i, y_i)$ and $i \Diamond y z$ stand similarly, we have:

$$M \leq max{1 \Diamond x y + 1 \Diamond y z, \ldots, n \Diamond x y + n \Diamond y z}$$

Calling the right hand side of that $N$, we know that $N = i \Diamond x y + i \Diamond y z$ for some $i$. But $d(x, y)$ is bigger than $j \Diamond x y$ for every $j$, and ditto for $d(y, z)$ and every $j \Diamond y z$. This is the triangle inequality we seek, so the product space over a sup metric is a metric space. $\Box$

**Proposition:** If $(x_n^i) is a sequence in $(X_i, d_i)$ for each $i \in [k]$, then the product sequence $(x_n^1, \ldots, x_n^k)$ converges to $(c_1, \ldots, c_k)$ iff each $(x_n^i)$ converges to $c_i$.

*Proof:* If the product sequence converges, for all $\epsilon$ there's a $N$ such that for all $n \geq N$, $d(x_n, c) < \epsilon$. By definition, each $d_i(x_n^i, c_i) < \epsilon$, so $(x_n^i)$ converges to $c_i$. Conversely, since there exist $N_i$ that will get each $(x_n^i)$ within an epsilon of $c_i$, taking the max of them will get the product sequence within an $\epsilon$ of $(c_1, \ldots, c_k)$. $\Box$

**Proposition:** If $K_1, \ldots, K_m$ are compact metric spaces, then the product space $\prod_1^m K_i$ (defined by the sup metric) is compact as well.

*Proof:* TODO $\Box$
