# README

This is me working through the tutorial available at https://reactjs.org/tutorial/tutorial.html

## JSX

React uses a thing called JSX which seems like a JavaScript templating engine. It's not,
more info is at https://jsx.github.io/, but it's actually an extension to JavaScript.

## React Components

If you think of <h1> and <u1> as being components, React components are pretty similar.

Components can be broken down into more specific types. One type is called "pure" and one
type is called "functional".

## Tools

Chrome plugin to expect React component state is available at
https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en

## Immutability

If you normally associate immutable data structures with functional programming, seeing them as
the recommended way in a JavaScript framework might surprise you, but it makes it easier for React
to know when to update components if it can just check if a pointer has changed to tell that the
component needs to be updated.

## Lifting State Up

This was a theme in the tutorial. Having state stored at a high-level and then passing it to
the people who actually display it. It seems sort-of like an MVC thing, but not really.