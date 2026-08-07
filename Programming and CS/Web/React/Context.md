---
title: Context
date created: Monday, July 27th 2026, 10:32:50 am
date modified: Monday, August 3rd 2026, 7:31:31 am
---
# Context
Context allows for information (context) to be passed down through the Virtual DOM tree *automatically*, without the need for props to receive and use them.

1. Create the context
`
```jsx
// you can put the default value in the ()s, but it's undefined here
const Ctx = createContext();
```

2. Create a `Provider`

> [!NOTE]
> Context uses a `Context.Provider` and `Context.Consumer` syntax; the former sets the value for the children in it (the provider of context), the latter can access the values set in the context

```jsx
function FooContext(children) {
    return (
        <Ctx.Provider value="Bar">
            {children}
        </Ctx.Provider>
    );
}

// not common (usually things are plugged in)
function FooContext(children) {
    return (
        <Ctx.Provider value="Bar">
            <Ctx.Consumer>
                {/* 
                    v is "Bar"
                    the function captures that value set in the context 
                */}
                {v => <span>{v}</span>}
            </Ctx.Consumer>
        </Ctx.Provider>
    );
}
```

3. (If not using `Context.Consumer`) In another component that is going to be a child of your context

```jsx
function FooChild() {
    const BarValue = useContext(Ctx);
    return <b>{BarValue}</b>;
}
```

4. (If nesting contexts) Nest providers within providers and they will override the context value in their part in the Virtual DOM tree

#web #web/js #web/react 