# Notes on Logic and Structure (Van Dalen)

The **propositional language** consists of the *proposition symbols* $P = \{ p_0, p_1, p_2, \ldots \}$, the *connective symbols* $\{ \vee, \wedge, \rightarrow, \leftrightarrow, \bot, \neg \}$, and the *auxiliary symbols* $\{ (, ) \}$. We call the set $B = \{ \vee, \wedge, \rightarrow, \leftarrow \}$ the *binary connectives*. The set $A = P \cup \{ \bot \}$ is called the *atomic propositions*, or *atoms*.

**Propositional sentences:** The set of propositional sentences, denoted $\Phi$, is the smallest set $X$ satisfying:

 1. $A \subseteq X$
 2. $\phi, \psi \in X$ implies for all $\Box \in B$, $(\phi \Box \psi) \in X$
 3. $\phi \in X$ implies $(\neg \phi) \in X$

This is an *inductive* definition of the set of valid propositional sentences.

**Induction on $\Phi$:** If $S$ is some set satisfying conditions (1)-(3) in the definition of $\Phi$, then $\Phi \subseteq S$. This is immediate from the definition of $\Phi$ as the *smallest* set satisfying these conditions.

If it's hard to see the significance of the induction principle, recall what a **proposition** is: intuitively, it is a statement about some class of objects which *holds* (i.e. is *true*) for some subset of all the objects. For instance, "X is bald" is a proposition which can be defined for all human males. It is only true for some males, for instance, "Clay Shirky is bald" is true. Formally, a proposition can be be represented in a few ways (one way would be a function from some set $X$ to the set $\{True, False\}$), but perhaps the easiest way of representing it is simply as the set of things for which it is true. The induction principle for $\Phi$ then states that if some property (1) is true for all atoms, and (2) if whenever it is true for $\phi$ and $\psi$, then it is also true for $(\phi \Box \psi)$, and (3) if whenever it is true for $\phi$, it is true for $(\neg \phi)$, then the property will be true for all propositional sentences.

A **formation sequence** of $\phi \in \Phi$ is a tuple $(\phi_0, \ldots, \phi_n)$ such that $\phi_n = \phi$ and for all $i \leq n$ one of these is true:

 1. $\phi_i \in A$
 2. $\phi_i = (\phi_j \Box \phi_k)$ for $0 \leq j, k < i$
 3. $\phi_i = (\neg \phi_j)$ for $0 \leq j < i$

Informally, we might like to think of some collection of propositional sentences as nodes in a digraph, with an arrow from node i to node j if the sentence at node j depends on the sentence at i being valid. We would need to prove things like that there aren't any cycles in this graph, but if so we could say that a formation sentence is just a topological sorting of the digraph of sentences.
