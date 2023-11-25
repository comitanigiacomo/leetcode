Write a function createHelloWorld. It should return a new function that always returns "Hello World".

```js
var createHelloWorld = function() {
    return function() {
        return "Hello World";
    }
}
var helloWorldFunction = createHelloWorld();
var result = helloWorldFunction();
console.log(result);
```
