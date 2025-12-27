# Bounds

What is the smallest $n$ such that the probability of getting a messy polygon mosaic is atleast $\frac{1}{2}$? Call this $n^*$.

How many ways to place $1$, $2 \times 2$ square in an $n \times n$ grid?
$$f(n) = (n-1)^2$$

How many ways to place $1$, $2 \times 3$ square (regardless of orientation) in an $n \times n$ grid?
$$f_2(n) = 2(n-1)(n-2)$$

How many ways to place $2$, $2 \times 2$ squares such that they don't overlap in an $n \times n$ grid?
$$g(n) = (n-2)(n-3)((n-1)^2 + 3n -5)\frac{1}{2}$$

How many ways to place $2$, $2 \times 2$ squares such that they don't overlap in an $n \times (n-1)$ grid?
$$g_2(n) = 1+\frac{3}{2}n-4n^2+n^3+\frac{1}{2}n^4$$

Then the $n$ such that 

$$6^8f(n) + 6^6 f_2(n) - 6^4 g(n) - 2 \cdot 6^2 g_2(n) - g(n-1) \geq 3 \cdot 6^{11},$$

is an upper bound for $n^*$, which gives that $n^*$ is less than or equal to $33$.
