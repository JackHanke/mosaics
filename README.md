# The Mosaic Problem

Consider the following 6 tiles. 

![](./images/tiles.png "Tiles")

Imagine placing these tiles in an $n \times m$ rectangular grid, like so.

![](./images/mosaic.png "Mosaic")

How many of these tilings, or *mosaics*, contain atleast one enclosed region for a given $n,m$? 

![](./images/mosaic2.png "Mosaic")

This questions turns out to be difficult for general $n,m$. Bounds on a similar problem were given by Hong and Oh in [this](https://arxiv.org/abs/1806.09717) paper. This work focuses on the $m=2$ and $m=3$ cases.

Let $t_{n,m}$ be the number of mosaics that contain atleast one enclosed region. Then

$$\sum_{n \geq 2}t_{n,2}x^n = \frac{x^2}{(1-36x)(1-37x+37x^2)}.$$

This gives for $n \geq 2$, that

$$t_{n,2}= 6^{2n} - \frac{1}{\beta-\alpha}((36\beta-35)\beta^{-n+1} - (36\alpha - 35)\alpha^{-n+1}),$$

where $\alpha = \frac{1}{2} + \frac{1}{2}\sqrt{\frac{33}{37}}$ and $\beta = \frac{1}{2} - \frac{1}{2}\sqrt{\frac{33}{37}}$. Finally,

$$\sum_{n \geq 2}t_{n,3}x^n = \frac{(73-414x)x^2}{(1-216x)(1-228x+2699x^2-7758x^3)}.$$

A video summarizing this work can be found [here](https://www.youtube.com/watch?v=D3dp5RBmPcs&t=921s). This video won an honorary mention in the [2023 Summer of Math Exposition](https://www.youtube.com/watch?v=6a1fLEToyvU&list=PLctYr3TOAdIE7MNyc8ejPUvda-g7VVVNt) contest.


