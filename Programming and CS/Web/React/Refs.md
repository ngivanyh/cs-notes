---
title: Refs
date created: Monday, July 27th 2026, 10:54:08 am
date modified: Monday, July 27th 2026, 10:55:10 am
---
# Refs
A plain object w/ a `.current` property you can access to manipulate the thing stored in it, you can store anything in it, but when you put in a DOM element, well you can then use it to modify the DOM.

```jsx
<input ref={ourRef} />;
```

An example to explain things:

```jsx
import { render } from 'preact';
import { useRef } from 'preact/hooks';

function App() {
  const input = useRef();
  const onClick = () => { input.current.focus(); }

  return (
    <div>
      {/* Set the ref.current to this input tag/component */}
      <input defaultValue="Hello World!" ref={input} />
      <button onClick={onClick}>Focus input</button>
    </div>
  );
}

render(<App />, document.getElementById('app'));
```

A React `document.getElementById()` or `document.querySelector()` if you'd like. You directly modify the DOM using them, but for the most part, you should use `useState()` or props. Refs should be used for things like focusing or blurring, animations, etc.

#web #web/js #web/react 