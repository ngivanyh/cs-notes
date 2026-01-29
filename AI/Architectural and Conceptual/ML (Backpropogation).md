## Prerequisite: Derivatives
Given any function $f(x)$, plugging a value into that function ($f(x)$) tells you something that could be interpreted as:

1. The slope of the tangent line at that point
2. **How much this value is going to change if you nudge it slightly ($+slope$ for values that will go up, $-slope$ for values that will go down)**
3. $\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$    (which is kind of analogous to the interpretation above)

Of which the number 2 is the idea that powers ==backpropogation==, where we tweak each weight and neuron so that the loss function gets closer and closer to zero (a.k.a. making the neural net more accurate/better). 

Mathematically, we can represent the derivative of something with respect to something else as for example: $\frac{dy}{dx}$, which means the derivative of $y$ with respect to $x$. Aka how much $y$ will change when we nudge $x$ a tiny bit. We can interpret this $\frac{dy}{dx}$ as something like this:
> $x$ has a value, and when we set $x$ to some value, what the instantaneous rate of change of $y$ is. Kinda like rise over run ($m=\frac{y_2-y_1}{x_2-x_1}$).
### Chain Rule
Say there are functions $y=g(u)$ and $u=f(x)$. If we want to know how $x$ affects $y$ ($\frac{dy}{dx}$) when we nudge $x$ slightly (the derivative of $y$ with respect to $x$), we can use the **chain rule**. With the chain rule, we can get the conclusion of $\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}$. By cancelling out $du$ from both fractions, we can get $\frac{dy}{dx}=\frac{dy}{dx}$. But that's really not how you prove the chain rule, one way (that is not *the* most rigorous proof of this) is to think about the core meaning of $\frac{dy}{du}$ and $\frac{du}{dx}$. 

$\frac{du}{dx}$ is the instantaneous rate of change of $u$ when we slightly alter $x$; $\frac{dy}{du}$ is the same thing but for $y$ when we nudge $u$. When we add a tiny amount to $x$, $u$ will respond by going up/down a tiny amount but the new value of $u$ is $\frac{du}{dx}$ times of $x$. The same can be said for $y$, it is $\frac{dy}{du}$ times of the **new** $u$ that was altered by $x$. So to know how much our infinitesimally changed $x$ compares to the new $y$, it should be $\frac{dy}{du}\cdot\frac{du}{dx}$ times of $x$.
## Backpropagation
We apply the principle of derivates and chain rule in **backpropagation**, where we see how the weights, inputs, and biases of a neural network affect the final output. 

I.E. we propagate backwards from the output to each and every value that affected the final output. And after calculating the **gradient** (basically derivative) of the neural net's weights and biases, we can alter them in the opposite direction to make the neural net produce more of what we want.

```python
weight = 0.01 * -weight.gradient
```

Above is some pseudocode for modifying the weight to affect the output the way we want.
### The Loss Function
When we train neural nets, we have a loss function, which essentially says how off our neural network is compared to the desired result. We don't just sum all the output and then normalize it. 

#ai #ai/ml #ai/conceptual  