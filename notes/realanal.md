% Notes on real analysis

## Single-variable

The real numbers, $\mathbb{R}$, are an ordered field with the least upper bound property. If you don't know what that means, these are not the real analysis notes you're looking for. I think there's a proof that such a field is unique, but I'm not particularly concerned with it. There are ways of building the reals from the rationals (via Dedekind cuts or via Cauchy sequences of rationals) but again we are not too concerned with that here.

$\mathbb{R}$ can be made a metric space by defining $d(x,y) = |x - y|$.

**Nested interval lemma:** If (I_n) is a sequence of non-empty closed intervals $[a_n, b_n]$ such that $a_n \leq a_{n+1}$ and $b_{n+1} \leq b_n$ for all $n$, then $\bigcap_1^{\infty} I_j$ is non-empty.

*Proof:* Any $b_k$ is an upper bound of the set $A = \{a_n : n \in \mathbb{N}\}$, so $A$ must have a least upper bound $c$. This $c$ must be a lower bound on $B = \{a_n : n \in \mathbb{N}\}$, otherwise it would not be the least upper bound. So since $a_n \leq b_n$, we have $a_n \leq c \leq b_n$. $\Box$


A sequence $(x_n)$ is **bounded** if there is some $M \in \mathbb{R}$ such that $|x_n| < M$ for all $n$. You can check that this definition meshes with the general definition for bounded sequences in metric spaces.


**Algebraic limit theorem for sequences:** If $(x_n)$, $(y_n)$ are sequences that converge to $c$ and $d$, respectively, then

 1. $(x_n + y_n) \rightarrow c + d$
 2. $(a x_n) \rightarrow ac$ for all $a \in \mathbb{R}$
 3. $(x_n y_n) \rightarrow cd$

*Proof:* (1) for $\epsilon_1, \epsilon_2 > 0$, there exist $M and $N$ such that for $j \geq M$, $x_j$ is within $\epsilon_1$ of $c$ and for $k \geq N$, $y_k$ is within $\epsilon_2$ of $d$. In particular, we can find such $M$ and $N$ for $\epsilon_1 = \epsilon_2 = \frac{\epsilon}{2}$. This means that 

$$|x_n + y_n - (c + d)| \leq |x_n - c| + |y_n - d| < \epsilon$$

for $n \geq max{M, N}$.

(2) suppose $a \in \mathbb{R}$ and $a \neq 0$. (If $a = 0$, the sequence is a constant sequence of zeroes, which surely converges to $0$). There is an $N$ such that $n \geq N$ implies that $|x_n - c| < \frac{\epsilon}{|a|}. So

$$|a x_n - ac| = |a| |x_n - c| < \epsilon$$

for $n \geq N$.

For (3), we note

$$|x_n y_n - cd| = |x_n y_n - x_n d + x_n d - cd| \leq |x_n| |y_n - d| + |d| |x_n - c|$$

The obvious strategy is to find a point $N$ after which both terms are individually less than $\frac{\epsilon}{2}$. We can make $|x_n - c|$ and $|y_n - d|$ as near zero as we like and $|d|$ is fixed, but the $|x_n|$ seems problematic.

In fact it is not, since every convergent sequence is bounded. So we can find some $M \in \mathbb{R}$ such that $|x_n| < M$ for all $n$. This establishes the result. $\Box$


A sequence $(x_n)$ is **monotonically nondecreasing** if for all $n$, $x_n \leq x_{n+1}$, and **monotonically nonincreasing** if $x_n \geq x_{n+1}$. It's called **monotone** if its either of these.

**Monotone convergence theorem:** If $(x_n)$ is a bounded monotonically [nonincreasing | nondecreasing] sequence, it converges and its limit is the [infimum | supremum] of the set of terms.

*Proof:* [We prove this for the nondecreasing case. You can fill in the blanks for the other case.] The statement of the theorem pretty much gives away the secret. By boundedness the set of terms has a least upper bound $c$, and by the properties of the LUB we can find terms arbitrarily close to $c$. By monotonicity, once the sequence is within an $\epsilon$ of $c$, it never goes any farther away. So it converges to $c$. $\Box$

**Bolzano-Weierstrass theorem:** Every bounded sequence has a convergent subsequence.

*Proof:* Let $(x_n)$ be bounded. We will find a monotone subsequence and use the monotone convergence theorem to establish our result.

We ask the question: how many indices $k$ are there such that for all $m > k$ $x_k \geq x_m$, i.e. how many terms are greater than every term that comes after it in the sequence? Call each such term a *peak*. If there are infinitely many, then these terms give us a monotonically nonincreasing subsequence. Otherwise, the are finitely many. Suppose $x_j$ is the last one. So starting at $k_0 = j+1$, there is some $k_1 > k_0$ such that $x_{k_1} > x_{k_0}$. We can continue in this way since no terms after $k_0$ are peaks. This furnishes a monotonically increasing subsequence.

In either case, we have a monotone subsequence, so by the monotone convergence theorem it converges. $\Box$


**Proposition:** Any closed, bounded subset of $\mathbb{R}$ is compact.

*Proof:* If $S$ is bounded, any sequence in $S$ is bounded, so by the Bolzano-Weierstrass theorem it has a convergent subsequence. The limit of this subsequence must be in $S$ because, supposing not, it would be a limit point of $S$ and $S$ contains all of its limit points. This establishes that $S$ is sequentially compact, but this is equivalent to $S$ being compact in any metric space. $\Box$

Since every compact metric space is closed and bounded, we have the following corollary:

**Corollary:** A subset of $\mathbb{R}$ is compact iff it is closed and bounded. $\Box$

**Corollary:** A nonempty closed interval $[a,b]$ in $\mathbb{R}$ is compact.
A closed interval is clearly bounded. Note also that closed intervals are the closed balls in the metric space $\mathbb{R}$, so they're actually closed sets, not just objects with the word "closed" in their name. $\Box$


**Extreme vaue theorem:** If $[a, b]$ is a non-empty closed interval in $\mathbb{R}$ and $f: [a, b] \rightarrow \mathbb{R}$ is continuous, then $f$ takes on minimum and maximum values.

*Proof:* $[a, b]$ is compact, so $f$'s image is compact (since the image of a continuous function defined on a compact metric space is compact). Hence, the image is closed and bounded, so it has both a supremum and an infimum. If the supremum isn't in the image, it's a limit point of image, and hence must be in the image, a contradiction. The same holds for the infimum, so f takes on maximum and minimum values at some point in the interval. $\Box$.

**Intermediate value theorem:** If $[a,b]$ is non-empty and $f: [a, b] \rightarrow \mathbb{R}$ is continuous, then assuming $f(a) \leq f(b)$, for all $c \in [f(a), f(b)]$ there is an $x \in [a, b]$ such that $f(x) = c$. Also, if $f(a) > f(b)$, for all $c \in [f(b), f(a)]$, there's a $x \in [a, b]$ such that $f(x) = c$.

*Proof:* WLOG we can prove for the $f(a) \leq f(b)$ case. (In the other case, negate the function). Now $[a, b]$ is connected, and the image of a continuous function on any connected space is connected as well. So the image must be an interval, and we can indeed find some $x \in [a, b]$ which maps to any $c \in [f(a), f(b)]$. $\Box$


**Algebraic continuity theorem:** If $X$ is a metric space and $f, g: X \rightarrow \mathbb{R}$ are continuous at $x \in X$, then

 1. $f + g$ is continuous at $x$
 2. for all $c \in \mathbb{R}$, $cf$ is continuous at $x$
 3. $fg$ is continuous at $x$

*Proof:* TODO $\Box$


An **interval** of $\mathbb{R}$ is a subset $I$ such that for all $x, y \in I$, for all $z \in \mathbb{R}$ such that $x < z < y$, then $z \in \mathbb{R}$.


**Proposition:** A subspace $S$ of $\mathbb{R}$ is connected iff $S$ is an interval.

*Proof:* Note first that for the empty interval, it can't possibly be disconnected, so it is connected. The degenerate interval ${a}$ for some $a \in \mathbb{R}$ similarly cannot be disconnected. So we assume $S$ has at least two elements.

If $S \subseteq \mathbb{R}$ is not an interval, then let $x, y \in S$ and without loss of generality suppose $x < y$. By hypothesis there is some $z$ not in $S$ such that $x < z < y$. $(- \infty, z)$ and $(z, \infty)$ are open in $\mathbb{R}$, so $A = S \cap (- \infty, z)$ and $B = S \cap (z, \infty)$ are open in $S$, disjoint and union to $S$. I.e., $S$ is disconnected.

Conversely, if $S$ is a disconnected interval, then $S = A \cup B$, for $A$ and $B$ non-empty, open and disjoint. We have some $x \in A, y \in B$ and without loss of generality we assume $x < y$. Consider

$$s := \text{inf}\{b \in B : x < b\}$$

which exists (by the least upper bound property) since we know $x < y$. $s \geq x$ since $x$ is itself a lower bound. Suppose $s > x$. There are no elements of $B$ smaller than $s$ but greater than $x$, so $(x, s)$ is entirely contained in $A$ since it is a subset of $S$ ($S$ is an interval).

The problem is that for all $\epsilon > 0$, there is some $b \in B$ such that $s < b < s + \epsilon$. So all $\epsilon$-balls around $s$ intersect both $A$ and $B$. This is an issue since $s \in S$, meaning it must be in $A$ or in $B$, which are both supposed to be open. So after all, $s = x$. But this is still a problem, because every $\epsilon$-ball around $x$ intersects $B$ and $A$ is open.

So $S$ must not be disconnected after all. $\Box$



## Multivariable real analysis

First note that every normed vector space $V$ with norm $\| \cdot \|$  induces a metric space by:

$$d(x, y) := \|x - y\|$$

We start with the standard inner product space over $\mathbb{R}^n$, which induces a norm via:

$$\| x \| = \sqrt{x \cdot x}$$

This is the standard euclidean distance. It turns $\mathbb{R}^n$ into a normed vector space, and hence into a metric space. We call this metric the **euclidean metric**. 

There is another metric that is easier to work with, which is induced by an alternative norm, the **sup norm:**

$$|x| := max{|x_1|, \ldots, |x_n|}$$

This metric induced by this norm is called the **sup metric**.

These are different metric spaces over $\mathbb{R}^n$, and accordingly the open balls of these metric spaces are different. We call an open ball in the euclidean metric an **open ball in $\mathbb{R}^n$** (it's confusing, I'm aware, but since we are working almost exclusively in \mathbb{R}^n the context should be clear). It is notated:

$$B(x, \epsilon) := \{y \in \mathbb{R}^n : \| y - x \| < \epsilon\}$$

An open ball in the sup metric is called a **open cube in $\mathbb{R}^n$**, as is notated:

$$C(x, \epsilon) := \{y \in \mathbb{R}^n : |y - x| < \epsilon\}$$

Even though the open balls are different, the two spaces are topologically equivalent (luckily for us!), meaning $U$ is open under one metric iff it's open under the other.

We use this lemma:

**Lemma:** For all $\textbf{x} \in \mathbb{R}^n$, $| \textbf{x} | \leq \| \textbf{x} \| \leq \sqrt n | \textbf{x} |$.

*Proof:* $|\textbf{x}| = |x_i|$ for some $i$, and each $i$ is such that $|x_i|^2 \leq \| \textbf{x} \|^2$, which establishes that $| \textbf{x} | \leq \| \textbf{x} \|$. Now, $\| \textbf{x} \| \leq \sqrt{\sum_1^n | \textbf{x} |} = \sqrt{n | \textbf{x} |^2} = \sqrt n | \textbf{x} |$. $\Box$

**Proposition:** For all $x \in \mathbb{R}^n$, $B(x, \epsilon) \subseteq C(x, \epsilon) \subseteq B(x, \epsilon \sqrt n)$

*Proof:* If $y \in B(x, \epsilon)$, each $|x_i - y_i| < \epsilon$, since otherwise $\| x - y \|$ could not be less than $\epsilon$. Hence $| \textbf{x - y} | < \epsilon$, so $y \in C(x, \epsilon)$.

Now let $z \in C(x, \epsilon)$. Then $| x_i - z_i | < \epsilon$ for all $i$. This implies that $\| x - z \| < \sqrt{ n \epsilon^2} = \sqrt n \epsilon$. $\Box$

Now if $U$ is open in the euclidean metric, every $x \in U$ has an open ball around $x$ contained in $U$. The last proposition implies that an open cube around $x$ is contained in $U$, so $U$ is open in the sup metric. The converse similarly holds.

So all topological properties of the sup metric hold in the euclidean metric, and vice versa. That is, the two spaces share the same open and closed sets, the same compact and connected sets, the same continuous functions (continuity does not, in fact, rely on open balls in the metric space. It can be characterized entirely in terms of open sets).

**Proposition:** If $[a_i, b_i] \subseteq \mathbb{R}$ for $i \in [n]$, then $\prod_1^n [a_i, b_i]$ is a compact subset of $\mathbb{R}^n$.

*Proof:* Each $[a_i, b_i]$ is compact, and the finite product of compact spaces is compact. $\Box$

This is technically a compact subspace of $\mathbb{R}^n$ over the sup metric, but the euclidean metric and the sup metric are topologically equivalent, so $S$ is compact in one iff it's compact in the other.


Define the $i$-th projection function $\pi_i: \mathbb{R}^n \rightarrow \mathbb{R}$, by $\pi_i (\textbf{x}) = x_i$. If $A \subseteq \mathbb{R}^n$, $f: A \rightarrow \mathbb{R}^m$, we can define $f_i: A \rightarrow \mathbb{R}$ by $f_i(\textbf{x}) = pi_i \circ f (\textbf{x}) for all $\textbf{x} \in A$. Such functions $f_i$ are called the **component functions** of $f$.

From this, we have $f(\textbf{x}) = (f_1(\textbf{x}), \ldots, f_m(\textbf{x}))$ for all $\textbf{x}$.

**Proposition:** Each projection function $\pi_i$ on $\mathbb{R}^n$ is continuous.

*Proof:* It suffices to prove it holds in the sup metric. If $\textbf{x} \in \mathbb{R}^n$, then for every $\epsilon > 0$, any $y$ in the open cube of radius $\epsilon$ around $\textbf{x}$ will have $\pi_i(\textbf{y})$ within an $\epsilon$ of $\pi_i(\textbf{x})$. $\Box$

**Corollary:** For $A \subseteq \mathbb{R}^n$, any continuous $f: A \rightarrow \mathbb{R}^m$ has continuous component functions.

*Proof:* Each component is the composition of continuous functions. $\Box$
