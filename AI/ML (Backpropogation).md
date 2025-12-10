### Prerequisite: Derivatives
Given any function $f(x)$, plugging a value into that function ($f(x)$) tells you something that could be interpreted as:

1. The slope of the tangent line at that point
2. **How much this value is going to change if you nudge it slightly ($+slope$ for values that will go up, $-slope$ for values that will go down)**
3. $\lim_{h \to 0} \frac{f(a+h)-f(x)}{h}$    (which is kind of analogous to the interpretation above)

Of which the number 2 is the idea that powers ==backpropogation==, where we tweak each weight and neuron so that the loss function gets closer and closer to zero (a.k.a. making the neural net more accurate/better).  
### Chain Rule
Say there is are functions $y=g(u)$ and $u=f(x)$. If we want to know how $x$ affects $y$ ($\frac{dy}{dx}$) when we nudge $x$ slightly, we can use the **chain rule**. 

#ai #ai/ml #ai/conceptual 