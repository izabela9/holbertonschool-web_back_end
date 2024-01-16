# Javascript ES6 Basics

ECMAScript 2015, also known as ES6, is a major update to the JavaScript language. It introduces several new features and syntax enhancements to make code more concise and expressive. Some of the basic features are below.

### let and const

ES6 introduces let and const for variable declarations. let allows for the declaration of variables with block scope, while const declares constants.
```
// Using let
let x = 10;
{
  let x = 5;
  console.log(x); // 5
}
console.log(x); // 10

// Using const
const pi = 3.14;

```
### Arrow Functions

Arrow functions provide a more concise syntax for writing function expressions.

```
// Regular function
function add(a, b) {
  return a + b;
}

// Arrow function
const add = (a, b) => a + b;
```

### Template Literals

Template literals allow for easy string interpolation and multiline strings.

```
const name = "John";
const greeting = `Hello, ${name}!`;
console.log(greeting);
```

### Classes

ES6 introduces a more convenient syntax for creating classes and working with inheritance.

```
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks.`);
  }
}

const myDog = new Dog("Buddy");
myDog.speak(); // Buddy barks.
```

### Modules

ES6 supports the use of modules for better code organization and encapsulation.

```
// math.js
export const sum = (a, b) => a + b;

// main.js
import { sum } from "./math.js";
console.log(sum(5, 3)); // 8
```

These are just a few of the many features introduced in ES6. Familiarizing yourself with these basics will help you write more modern and efficient JavaScript code. Explore further to harness the full power of ES6 in your projects.