---
title: Components
date created: Saturday, February 28th 2026, 9:18:57 am
date modified: Monday, August 3rd 2026, 7:38:26 am
---
# Components 
## Components Overview
Components allow us to essentially save some space when declaring our [[Virtual DOM and Events|Virtual DOM tree]], they allow us to put different HTML elements inside and group them together, allowing us to reuse them. E.g.

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

> [!IMPORTANT]
> JSX has `<>` and `</>`, these are called fragments, when you can't bother to wrap your a component which has multiple children with a `<div>`, you can use this. No styles apply to it like `<div>`s, think of it as just a way to indicate you want to group these components in one place but insert them in place without creating an outer layer. `()` for returning components, are simply a JS thing indicating you have a multiline statement
## Class Components
You create these kinds of components with the `Component` base class, contrary to our previous use of only functions to define them in here.

```jsx
class Greeter extends Component {
	render(props) {
		return <button class="greeter">{props.children}</button>;
	}
}

render(<MyButton>Click Me!</MyButton>, document.body);
```

Class components allow you to track the lifecycle of the component, because when React compares the old Virtual DOM with the new one, it will reuse the old class component instance, allowing you to store data in the class component across updates. 

Asides from the `render()` method, they also contain other lifecycle methods such as `componentDidUpdate()` and `componentDidMount()`. Although these advantages that classes have over function components are bridged through [[Hooks|hooks]].

## Why Function > Class (Esp. w/ Hooks)
- Easier reuse of logic (just pass functions, create your own hooks of sorts, etc)
- Clearer code organization (grouping logic together in a hook vs **across** different methods)
- No more `this` and `this` that, better state understanding
- Better dependency management, since you have to declare what hooks you use
- Lighter and smaller

## Managing State
This is how we *actually* update the Virtual DOM tree. Now that we know that both function components and class components can store data, we can use this to change our UI.

### Class Components
Class components have a `state` property, through a function that updates the `state` property, the component can be asked to be re-rendered by the library. (Normal things like function local variable changes don't trigger re-renders, only `useState()` and a few others)

```jsx
class Greeter extends Component {
	state = { clicked: false };

	handleClick = () => {
		this.setState({ clicked: true });
	};

	render() {
		return (
			<button onClick={this.handleClick}>
				{this.state.clicked ? 'Greeting!' : 'Not greeted yet'}
			</button>
		);
	}
}
```

### Function Components
Function components don't have any properties attached to them, so, as alluded, they use [[Hooks|hooks]] like `useState()`, `useEffect()`, and more.

#web/react #web/js #web