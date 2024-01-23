## JavaScript Promise

Promises in JavaScript are a way to handle asynchronous operations more effectively and with better readability. Promises represent the eventual completion or failure of an asynchronous operation and allow you to write more readable and maintainable asynchronous code compared to using callbacks.

Here's a basic overview of how promises work:

* Creating a Promise:
You create a promise using the Promise constructor. A promise takes a function as its argument, which has two parameters: resolve and reject. resolve is called when the operation is successful, and reject is called when there is an error.
* Consuming a Promise:
You can use the .then() and .catch() methods to handle the result or error of a promise.
The .then() method is called when the promise is resolved, and the .catch() method is called when the promise is rejected.
* Chaining Promises:
You can chain multiple promises together using .then():
```
const myPromise = new Promise((resolve, reject) => {
  // Asynchronous operation
  resolve("First operation completed");
});

myPromise
  .then((result) => {
    console.log(result); // First operation completed
    return "Second operation completed";
  })
  .then((result) => {
    console.log(result); // Second operation completed
  })
  .catch((error) => {
    console.error(error);
  });
```
Each .then() block can return a value or another promise, allowing you to chain asynchronous operations.
* Promise.all:
If you have multiple promises and want to wait for all of them to complete, you can use Promise.all():
```
const promise1 = Promise.resolve("Operation 1 completed");
const promise2 = new Promise((resolve) => setTimeout(() => resolve("Operation 2 completed"), 1000));

Promise.all([promise1, promise2])
  .then((results) => {
    console.log(results); // ["Operation 1 completed", "Operation 2 completed"]
  })
  .catch((error) => {
    console.error(error);
  });
```
Promise.all() takes an array of promises and returns a new promise that resolves with an array of the resolved values.
