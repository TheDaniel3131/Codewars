var name;
function greet_abe() {
  name = 'Abe';
  return "Hello, " + name + '!';
};


function greet_ben() {
  name = 'Ben'; 
  return "Hello, " + name + '!';
};



var name;
function greet_abe() {
  name = 'Abe';
  return "Hello, " + name + '!';
};


function greet_ben() {
  name = 'Ben'; 
  return "Hello, " + name + '!';
};


const greet_abe = () => 'Hello, Abe!';
const greet_ben = () => 'Hello, Ben!';



function create_greeter(name) {
  return function() {
    return "Hello, " + name + "!";
  }
}

var name = 'Abe';
var greet_abe = create_greeter(name);
name = 'Ben';
var greet_ben = create_greeter(name);