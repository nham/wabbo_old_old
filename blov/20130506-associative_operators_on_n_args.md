# Proof that an associative binary operator applied to n terms is independent of how they are grouped into pairs

*This not super interesting, in my opinion, but I'm working on my proof chops.*

The idea is to prove that, for an associative binary operatior $\circ$, $a \circ (b \circ (c \circ d) \circ e)$ is equal to $((a \circ b) \circ c) \circ (d \circ e)$ and any other way of grouping $a$, $b$, $c$, $d$, and $e$ into pairs that does not disturb the order. This allows us to dispense with parentheses entirely and talk of the product $a \circ b \circ c \circ d \circ e$.

This is often used implicitly in the group theory chapters of abstract algebra texts, but it is not always proved in my experience.

**Proposition:** Let $\circ$ be a function $A \times A \rightarrow A$ (i.e. a binary operator on $A$) for some set $A$. Then for every $n \in \mathbb{P}$ we can define a unique function $\phi_n: A^n \rightarrow A$ such that the following hold:

 - $\phi_1(a) = a$ for all $a \in A$
 - $\phi_2(a, b) = a \circ b$ for all $a, b \in A$
 - For any tuple $(a_1, \ldots, a_n) \in A^n$, $\phi_n(a_1, \ldots, a_n) = \phi_i(a_1, \ldots, a_i) \circ \phi_{n-i}(a_{i+1}, \ldots, a_n)$ for every $i \in \mathbb{N}$ such that $1 \leq i \leq n-1$.

*Proof:* We shall prove this by induction on $n$. $n = 2$ checks out, and $n = 3$ holds because of associativity:

$$\begin{align} \phi_3(a,b,c) & = \phi_1(a) \circ \phi_2(b,c) \\ &= a \circ (b \circ c) = (a \circ b) \circ c \\ & = \phi_2(a,b) \circ \phi_1(c) \end{align}$$

Now suppose the proposition holds for some $n$. We shall try to prove it holds for $n+1$.

We can assume by strong induction that it holds for all $k \leq n$, so let $i$ and $j$ be such that $1 \leq i < j \leq n$. Then let

$$M = \phi_i(a_1, \ldots, a_i) \circ \phi_{n+1-i}(a_{i+1}, \ldots, a_{n+1})$$

But by the induction hypothesis,

$$\phi_{n+1-i}(a_{i+1}, \ldots, a_{n+1}) = \phi_{j-i}(a_{i+1}, \ldots, a_j) \circ \phi_{n-j+1}(a_{j+1}, \ldots, a_{n+1})$$

So by associativity:

$$M = \phi_j(a_1, \ldots, a_j) \circ \phi_{n+1-j}(a_{j+1}, \ldots, a_{n+1})$$

This proves that $\phi_{n+1}$ is well-defined. To prove uniqueness, we are assuming (again by the induction hypothesis) that $\phi_k$ for all $k \leq n$ is unique. Then, in particular,

$$\phi_{n+1}(a_1, \ldots, a_{n+1}) = \phi_n(a_1, \ldots, a_n) \circ a_{n+1}$$

Since $\phi_n$ is uniquely-defined, and $\circ$ is also uniquely defined for any pair, $\phi_{n+1}$ is uniquely defined. $\Box$
