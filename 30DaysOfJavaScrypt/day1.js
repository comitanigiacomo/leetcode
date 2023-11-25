var createHelloWorld = function() {
    return function() {
        return "Hello World";
    }
}

var helloWorldFunction = createHelloWorld();
var result = helloWorldFunction();
console.log(result);