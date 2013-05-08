# Equivalence relations and partitions

Wherein we dissect the equivalence between partitions and equivalence relations.

If $R \subseteq A \times A$ is a binary relation on $A$, let

$$aR- := \{b \in A : aRb\}$$

Similarly:

$$-Rb := \{a \in A : aRb\}$$

I haven't come up with a good name for these, so we'll just refer to them symbolically.

We will be concerned, here, with taking the collection of all sets $aR-$ (alternatively: $-Rb$) for $a \in A$. Specifically, what do properties of the relation determine about properties of the set?

If the relation $R$ isn't reflexive, then we have no guarantee that the set of $aR-$ for all $a$ covers $A$. For example, if $A = \{a,b,c\}$, and $R = \{(a,a), (b,a), (c,a), (b,c)\}, then $aR- = \{a\}$, $bR- = \{a, c\}$, $cR- = \{a\}$. The union of these three sets is missing $b$. Whereas, if $R$ were reflexive, then at least every $x \in A$ would belong to $xR-$.

Notice also that the collection of $xR-$ is different from the $-Rx$: $-Ra = \{a,b,c\}$, $-Rb = \emptyset$, $-Rc = \{b\}$.

*Lemma:* Every $aR-$ equals $-Ra$ iff $R$ is symmetric.
*Proof*: If $R$ is symmetric and $b \in aR-$, then $aRb$, so $bRa$ by symmetricity, implying $b \in -Ra$. If $R$ not symmetric, $\exists a, b$ such that $aRb$ and it is not the case that $bRa$. so $b \in aR-$ but not in $-Ra$. $\Box$

With symmetric $R$'s, we can just define $[a] = \{b : aRb\}$

$\{(a,a), (a,b), (b,a), (b,c), (c,b), (c,a)\}$
