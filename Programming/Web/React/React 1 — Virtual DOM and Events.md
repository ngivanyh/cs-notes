## It All Starts with Virtual DOM
The Virtual DOM is the core of React, basically, instead of writing how the UI should respond after some input (e.g. `keydown`, `mouseup`, `click`, etc), we declare how the UI should *look* like after some input.

Basically, no more `addEventListeners`

```js
element.addEventListener('click', () => {
	// stuff goes down
});
```

The library will handle rendering that intended result you want by comparing the Virtual DOM tree (it is a tree of elements) to the (regular) DOM.

### Creating Stuff to put inside the Virtual DOM (tree)[^1]
JSX, HTM, or `createElement`.

#### JSX
Requires extra compilation as it's not standard ECMAScript/JS, basically you can declare the elements as HTML inside JS. 

```jsx
let paragraph = <p>Hello world!</p>;
```

But sometimes you need to be able to jump back out into JS, say for calculating stuff or calling functions so you add `{}`s.

```jsx
let paragraph = <p>Hello {String.from(f(64 + 1))}!</p>
```

> Note: Sometimes you see `{{}}`s because they mean they want to jump back to JS AND declare an object, the style prop (property) often uses it:

```jsx
let paragraph = <p style={{ color: 'red', fontSize: '200px'}}>Hello {String.from(f(64 + 1))}!</p>
```

> The inner `{}` declares an Object.
#### HTM
Native in JS you basically write them in JS string templates (akin to Python f-strings).

```js
let paragraph = html`<p>Hello ${String.from(f(64 + 1))}!</p>`
```

To escape back into JS, you use `${}`.

> Note: You have to install a `htm` library alongside your React to use this.

#### `createElement`
Those two above compile into elements generated using `createElement`.

```js
let paragraph = createElement(
	'p', // for <p> tag
	{}, // no "props" (properties)
	`Hello ${String.from(f(64 + 1))}!` // our string
)
```

## Events
As said, we don't have to accommodate for how to change the UI when there is an input, we define *how* it should look like when there is an input.

Events are treated like props (properties) in React so you declare them like such:

```jsx
function clicked() {
  console.log('clicked');
}

let btn = <button onClick={clicked}>;
```

[^1]: Called "tree" as when you layer and nest HTML elements to together, it now has a hierarchy.

#web/react #web/js #web