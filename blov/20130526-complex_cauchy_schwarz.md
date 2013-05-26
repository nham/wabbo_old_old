# The complex Cauchy-Schwarz inequality

Complex numbers $z \in \mathbb{C}$ can be represented as $z = a + bi$ for real numbers $a, b$. There is a way to build this up more rigorously from pairs, but I forego that development here.

The *real part* and *imaginary part* of a complex number $z = a + bi$ is defined by

$$Re(z) := a$$
$$Im(z) := b$$

Note that the set of complex numbers $a + bi$ with $b = 0$ is (isomorphic to) $\mathbb{R}$.

The *complex conjugate* of $z = a + bi$ is defined by

$$ \overline{z} = a - bi $$

Complex conjugation has these properties:

 1. $\overline{w + z} = \overline{w} + \overline{z}$
 2. $\overline{wz} = \overline{w} \overline{z}$
 3. $z + \overline{z} = 2 Re(z)$
 4. $z - \overline{z} = 2i Im(z)$
 5. $z \overline{z} \in \mathbb{R}$ and is nonnegative

*Proof:* Assuming $w + a + bi$, $z = c + di$, we have: (1) $\overline{w + z} = \overline{a + c + bi + di} = a + c -(b+d)i = \overline{w} + \overline{z}$. $\Box$. (2) $\overline{wz} = \overline{ac - bd + i(ad + bc)} = ac - bd -(ad + bc)i = a(c - di) - b(ci + d)$ $= a(c - di) - bi(c - di) = (a - bi)(c - di) = \overline{w} \overline{z}$ $\Box$. For (3), $z + \overline{z} = a + bi + a - bi = 2a = 2 Re(z)$ $\Box$. (4) is similiar: $z - \overline{z} = a + bi - (a - bi) = - 2i b = -2i Im(z)$ $\Box$. Finally, (5) has: $z \overline{z} = (a + bi)(a - bi) = a^2 + b^2$. It's clearly not negative. $\Box$

Part 5 above is reminiscent of the Pythagorean theorem, so that we  might define the *absolute value* of $z \in \mathbb{C}$ by

$$|z| := \sqrt{z \overline{z}} = \sqrt{a^2 + b^2}$$

This exists since square roots exist in $\mathbb{R}$. Note that for real $r$, $\overline{r} = r$, so $|r| = \sqrt{r^2}$.

Here are some properties of the absolute value:

 1. $|z| \geq 0$, $|z| = 0$ iff $z = 0$
 2. $|\overline{z}| = |z|$
 3. $|zw|= |z| |w|$
 4. $Re(z) \leq |z|$
 5. $|z + w| \leq |z| + |w|$

*Proof:* (1) follows because the square root of a nonnegative is nonnegative (by definition. Also $\sqrt{x} = 0$ implies $x = 0$. so $|z| = \sqrt{z\overline{z}} = 0$ implies $z \overline{z} = a^2 + b^2 = 0$. So $a = b = 0$. $\Box$. (2) holds by direct calculation. $\Box$. For (3), $|zw|^2 = (zw)(\overline{zw}) = z \overline{z} w \overline{w} = |z|^2 |w|^2$ $\Box$. (4) For $a, b \in \mathbb{R}$, $a^2 \leq a^2 + b^2$. so $Re(z) = a \leq |a| \leq \sqrt{a^2 + b^2} = |z|$ $\Box$. Finally, for (5) we have

$$\begin{align} |z + w|^2 & = (z + w)(\overline{z} + \overline{w}) = |z|^2 + |w|^2 + z\overline{w} + w\overline{z} \\
& = |z|^2 + |w|^2 + 2 Re(z\overline{w}) \\
& \leq |z|^2 + |w|^2 + 2 |z\overline{w}| = |z|^2 + |w|^2 + 2|w||z| \\
& = (|z| + |w|)^2 \end{align}$$

$\Box$.

Finally, our quarry is before us:

**The Cauchy-Schwarz Inequality (in $\mathbb{C}$)**
For $x_1, \ldots, x_n, y_1, \ldots, y_n$ for any $n \in \mathbb{P}$ and $x_i, y_i \in \mathbb{C}$, we have

$$ \left|\sum_1^n a_j \overline{b_j} \right|^2 \leq \sum_1^n |a_j|^2 \sum_1^n |b_j|^2 $$

We proceed by induction. It clearly holds for $n = 1$. For $n = 2$, it is possible to prove it (exercise to the reader :P). Now assume it holds for all $k$ with $1 \leq k < n$. Then

$$ \begin{align}
\left|\sum_1^n a_j \overline{b_j} \right|^2 & = \left|\sum_1^{n-1} a_j \overline{b_j} + a_n \overline{b_n} \right|^2 \\ 
& \leq \left| \sqrt{\sum_1^{n-1} |a_j|^2} \sqrt{\sum_1^{n-1} |b_j|^2} + a_n \overline{b_n} \right|^2 \\
& \leq \sum_1^n |a_j|^2 \sum_1^n |b_j|^2
\end{align}$$

where the first inequality holds by the induction hypothesis for $n-1$ and the second inequality holds by the $n=2$ case. $\Box$.
