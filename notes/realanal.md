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

**Nested interval lemma:** If (I_n) is a sequence of non-empty closed intervals $[a_n, b_n]$ such that $a_n \leq a_{n+1}$ and $b_{n+1} \leq b_n$ for all $n$, then $\bigcap_1^{\infty} I_j$ is non-empty.

*Proof:* Any $b_k$ is an upper bound of the set $A = \{a_n : n \in \mathbb{N}\}$, so $A$ must have a least upper bound $c$. This $c$ must be a lower bound on $B = \{a_n : n \in \mathbb{N}\}$, otherwise it would not be the least upper bound. So since $a_n \leq b_n$, we have $a_n \leq c \leq b_n$. $\Box$

A sequence $(x_n)$ is **bounded** if there is some $M \in \mathbb{R}$ such that $|x_n| < M$ for all $n$. You can check that this definition meshes with the general definition for bounded sequences in metric spaces.

A sequence $(x_n)$ is **monotonically nondecreasing** if for all $n$, $x_n \leq x_{n+1}$, and **monotonically nonincreasing** if $x_n \geq x_{n+1}$. It's called **monotone** if its either of these.

**Monotone convergence theorem:** If $(x_n)$ is a bounded monotonically [nonincreasing | nondecreasing] sequence, it converges and its limit is the [infimum | supremum] of the set of terms.

*Proof:* [We prove this for the nondecreasing case. You can fill in the blanks for the other case.] The statement of the theorem pretty much gives away the secret. By boundedness the set of terms has a least upper bound $c$, and by the properties of the LUB we can find terms arbitrarily close to $c$. By monotonicity, once the sequence is within an $\epsilon$ of $c$, it never goes any farther away. So it converges to $c$. $\Box$

**Bolzano-Weierstrass theorem:** Every bounded sequence has a convergent subsequence.

*Proof:* Let $(x_n)$ be bounded. We will find a monotone subsequence and use the monotone convergence theorem to establish our result.

We ask the question: how many indices $k$ are there such that for all $m > k$ $x_k \geq x_m$, i.e. how many terms are greater than every term that comes after it in the sequence? Call each such term a *peak*. If there are infinitely many, then these terms give us a monotonically nonincreasing subsequence. Otherwise, the are finitely many. Suppose $x_j$ is the last one. So starting at $k_0 = j+1$, there is some $k_1 > k_0$ such that $x_{k_1} > x_{k_0}$. We can continue in this way since no terms after $k_0$ are peaks. This furnishes a monotonically increasing subsequence.

In either case, we have a monotone subsequence, so by the monotone convergence theorem it converges. $\Box$


**Proposition:** Any closed, bounded subset of $\mathbb{R}$ is compact.

*Proof:* If $S$ is bounded, any sequence in $S$ is bounded, so by the Bolzano-Weierstrass theorem it has a convergent subsequence. The limit of this subsequence must be in $S$ because, supposing not, it would be a limit point of $S$ and $S$ contains all of its limit points. This establishes that $S$ is sequentially compact, but this is equivalent to $S$ being compact in any metric space. $\Box$
