---
tags: [web/react, web/js, web]
title: React 2 — Components
date created: Saturday, February 28th 2026, 9:18:57 am
date modified: Thursday, July 9th 2026, 7:47:56 am
parent: React
nav_order: 3
---
# React 2 — Components
## Basic Components 
Components allow us to essentially save some space when declaring our [[React 1 — Virtual DOM and Events|Virtual DOM tree]], they allow us to put different HTML elements inside and group them together, allowing us to reuse them. E.g.

```jsx
const Greeter = (props) => {
    return <button onClick={console.log(`Hello! ${props.name}.`)}>Click to get greeted!</button>;
}
```

So that button is called "Greeter", and we've essentially created a `<Greeter/>` tag that when you pass a `name` property to, will `console.log` "`Hello, NAME`".

Components can be nested within one another, so

```jsx
const Greeters = () => {
    return (
	    <div>
	        <Greeter name='React'/>
	        <Greeter name='Preact'/>
	    </div>
    );
}
```

Obviously our new `<Greeters/>` component can have props of its own.

### Component Children
A `children` prop when declaring the component allows you to access and use the children inside your component.

## Class Components
You create these kinds of components with the `Component` base class.

```jsx
class Greeter extends Component {
	render(props) {
		return <button class="greeter">{props.children}</button>;
	}
}

render(<MyButton>Click Me!</MyButton>, document.body);
```

Class components allow you to track the lifecylcle of the component, and as the app updates the UI and the Virtual DOM tree is compared to one another, it will create another 

#web/react #web/js #web