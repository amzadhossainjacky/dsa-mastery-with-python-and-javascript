/*There are three type of variable in js var, let, const, */
var a = "Emon";
console.log(a);

let b = "Jacky vai";
console.log(b);

const c = "shakil vai";
console.log(c);

/*---var---
1.Function-scoped.
2.Can be redeclared.
3Can be reassigned.
*/

var name = "Emon";
var name = "John"; // Allowed
name = "David"; //  Allowed

console.log(name);

/*--let---
1.Block-scoped.
2.Cannot be redeclared in the same scope.
3.Can be reassigned.
*/

let city = "Dhaka";

city = "Gazipur"; //Allowed

// let city = "Rajshahi"; Error


if (true) { // scope ex
    let age = 35;
}
console.log(age);
// ReferenceError


/*----const----
1.Block-scoped.
2.Cannot be redeclared.
3.Cannot be reassigned.
4.Must be initialized when declared.

*/

//swap two variables

let a = 10;
let d = 20;

[a, d] = [d, a];

console.log(a); //20
console.log(d); //10

// type in js 

let age = 25;
let isStudent = true;

console.log(typeof age);
console.log(typeof isStudent);


