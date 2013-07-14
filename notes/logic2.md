# Notes on Rautenberg's *Concise Introduction to Mathematical Logic*

The **boolean alphabet** is the set $\mathcal{B} = \{ \vee, \wedge, \neg, (, ) \} \cup \sigma$, where $\sigma$ is called the **signature**. We often use the standard signature $\pi := \{p_1, p_2, p_3, \ldots\}$.

The set of all strings boolean signals over signature $\sigma$ is denoted $\mathcal{B}_{\sigma}^{\ast}$, or just $\mathcal{B}^{\ast}$ if the signature is known.

The **propositional language** $\mathcal{F}_{\sigma}$ (or just $\mathcal{F}$) is the intersection of all sets such that

 1. $\sigma \subseteq \mathcal{F}$
 2. whenever $\alpha, \beta \in \mathcal{F}$, $(\alpha \vee \beta), (\alpha \wedge \beta), \neg \alpha$ are all in $\mathcal{F}$

Each element of $\mathcal{F}$ is called a **Boolean formula**.

There's an induction principle for Boolean formulas, blah blah.

We have an interest in the following: whether the same Boolean formula could be proved by two different means. For example, if $p_1 \vee$, $\wedge p_1$ are both formulas, then by letting $\alpha = p_1 \vee$, $\beta = p_1$, $\gamma = \wedge p_1$, then

$$(\alpha \wedge \beta) = (p_1 \vee \wedge p_1) = (\beta \vee \gamma)$$

So we obtain the same formula via a $\wedge$ connective and via a $\vee$ connective.
