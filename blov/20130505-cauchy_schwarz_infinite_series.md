# My struggle with the infinite series version of the Cauchy-Schwarz inequality in $\mathbb{R}$, or why you should not half-ass learning analysis

In Steele's *The Cauchy-Schwarz Master Class*, after proving the basic Cauchy-Schwarz inequality for vectors in $\mathbb{R}^n$, he proves an analog version for infinite series. Step 1 is to establish

**Lemma:** If $\sum_{1}^{\infty} a_k^2$ and $\sum_{1}^{\infty} b_k^2$ both converge for sequences $(a_k)$ and $(b_k)$ then $\sum_{1}^\infty |a_k b_k|$ does too.

In proving this, Steele establishes another inequality: 

$$\sum_{1}^\infty |a_k b_k| \leq \frac{1}{2} \sum_{1}^\infty a_k^2 + \frac{1}{2} \sum_{1}^\infty b_k^2$$

From this he uses a technique he calls "normalization" to establish the infinite series version of CSI:

$$ \sum_{1}^\infty a_k b_k \leq \sqrt \sum_{1}^\infty a_k^2 + \sqrt \sum_{1}^\infty b_k^2 $$

Steele doesn't cross all t's and dot all the i's, however, and in trying to fill in the gaps, I failed to remember certain critical facts about infinite series. Here I will go over the full proofs, explaining in particular the facts I forgot.

*Proof of Lemma*: The goal here was to prove this without invoking the CSI for finite sequences of numbers. The first observation needed is that for any $x, y \in \mathbb{R}$, $(x-y)^2 \geq 0$, which can be rearranged as:

$$ xy \leq \frac{1}{2} x^2 + \frac{1}{2} y^2 $$

In particular, for any $k \in \mathbb{P}$, letting $x = |a_k|$ and $y = |b_k$, we get 

$$ |a_k b_k| \leq \frac{1}{2} a_k^2 + \frac{1}{2} b_k^2 $$

From this, Steele asserts that the infinite series of these terms has similar inequalities. There is of course a gap here: how do we know the first infinite series converges? 

To prove this, let $z_k = |a_k b_k|$ and $d_k = \frac{1}{2} a_k^2 + \frac{1}{2} b_k^2$. These are sequences, and for every $k$-th term we have

$$ 0 \leq z_k \leq d_k $$

By the algebraic limit theorem for infinite series, $\sum_{1}^{\infty} d_k$ exists and equals $D = \frac{1}{2} \sum_{1}^\infty a_k^2 + \frac{1}{2} \sum_{1}^\infty b_k^2$

Since $\sum_{1}^\infty z_k$ is an infinite series on non-negative terms, it is a monotone non-decreasing sequence. By the monotone convergence theorem, we need only prove that it is bounded to prove convergence. But the sequence $\sum_{1}^\infty d_k$ is bounded above by $D$, so each partial sum $\sum_{1}^n d_k \leq D$ (because $(d_k)$ is also monotone). So every partial sum $\sum_{1}^n z_k$ is similarly bounded above by $D$, so the infinite series on $(z_k)$ converges. It must converge to something not greater than $D$, since otherwise every partial sum would eventually be greater than $D$, implying that eventually partial sums of $(d_k)$ would be greater than $D$, which can't happen.

In other words:

$$\sum_{1}^\infty |a_k b_k| \leq \frac{1}{2} \sum_{1}^\infty a_k^2 + \frac{1}{2} \sum_{1}^\infty b_k^2$$ $\Box$

Previously I was missing that part proving that $\sum_{1}^\infty |a_k b_k|$ converged. In *Understanding Analysis* by Abbott, this is called the Comparison Test. He gives an easier proof, but I, having forgotten it, derived the above proof.

The more embarrassing of my mathematical deficiencies follows. Having established the above, Steele goes on to use the following inequality without comment:

$$\sum_{1}^\infty a_k b_k \leq \frac{1}{2} \sum_{1}^\infty a_k^2 + \frac{1}{2} \sum_{1}^\infty b_k^2$$

But where did the absolute value on the left go! You can't just remove those!

A-ha, but you can due to a well-known fact about infinite series: If $(x_k)$ is a series and $\sum_{1}^\infty |x_k|$ converges, then $\sum_{1}^\infty x_k$ converges. The former is called *absolute convergence*, and this proposition says that absolute convergence implies convergence. The proof for this follows quite handily from the Cauchy criterion for series and the triangle inequality. The proof is left as an exercise to the reader (which is code for "I'm feeling too lazy to write it up")

So given that

$$\sum_{1}^\infty a_k b_k \leq \frac{1}{2} \sum_{1}^\infty a_k^2 + \frac{1}{2} \sum_{1}^\infty b_k^2$$

holds for any $(a_k)$ and $(b_k)$ whose associated infinite series $\sum_{1}^\infty a_k^2$ and $\sum_{1}^\infty b_k^2$ converge, we seek to prove the Cauchy-Schwarz inequality for convergent infinite series:

$$ \sum_{1}^\infty a_k b_k \leq \sqrt{\sum_{1}^{\infty} a_k^2} \sqrt{\sum_{1}^{\infty} b_k^2} $$

Steele's trick is to construct new, "normalized" sequences $(\hat{a}_k)$, $(\hat{b}_k)$ defined by

$$\hat{a}_k := \frac{a}{\sqrt{A}}$$
