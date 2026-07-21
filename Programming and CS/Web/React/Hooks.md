---
title: Hooks
date created: Wednesday, July 15th 2026, 7:02:26 am
date modified: Wednesday, July 15th 2026, 7:48:30 am
---
# Hooks
Under the hood, hook functions like `setState` work by storing data in a sequence of "slots" associated with each component in the Virtual DOM tree. Calling it uses up one slot, and increments an internal "slot number" counter so the next call uses the next slot. React resets this counter before invoking each component, so each hook call gets associated with the same slot when a component is rendered multiple times.

```js
function User() {
	const [name, setName] = useState('Bob');    // slot 0
	const [age, setAge] = useState(42);         // slot 1
	const [online, setOnline] = useState(true); // slot 2
}
```

This ordering of slots is called site ordering, and this is why these hooks must be called in the same order within a component without being in any loops or conditions.

> Explanation: If the order is messed up, React will read the slots and assign them to the wrong things

## `useState()`

## `useRef()`

## `useEffect()`
