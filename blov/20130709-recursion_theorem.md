# The recursion theorem (Enderton appendix)

If $\mathcal{F} = \{f, g\}$ where $f: U^2 \rightarrow U$, $g: U \rightarrow U$, a set $S$ is *closed under $\mathcal{F}$ if $\forall s, t \in S$, $f(s,t) \in S$ and $g(s) \in S$.

A set $S \subseteq U$ is $(B, \mathcal{F})$-inductive if $B \subseteq S$ and $S$ is closed under $\mathcal{F}$.

$C^{\ast} := \bigcap \{S : S is (B, \mathcal{F})\text{-inductive}\}$.

A $(B, \mathcal{F})$ construction sequence for $u \in U$ is a tuple $(u_0, \ldots, u_n)$ with all $u_i \in U$, where $u_n = u$, such that for all $i \leq n$, we must have one of these:

 - $u_i \in B$
 - $u_i = f(u_j, u_k)$ for $j, k < i$
 - $u_i = g(u_j)$ for $j < i$

We notate by $C_{\ast}$ the set of elements in $U$ which have construction sequences.

It can be proved without much difficulty that $C_{\ast} = C^{\ast}$. We will call this unique set $C$, the **set generated from $B$ by $\mathcal{F}$**

