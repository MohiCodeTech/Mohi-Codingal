let student1 = {
    name : "Moheathraam",
    age : 14
}

let student2 = {
    name: "Gaurav",
    age: 24
}

let student3 = {
    name: "Ezra",
    age: 14
}

let AllStudents = [student1, student2, student3]
console.log("Name of Student1 is: " + AllStudents[0].name)
console.log("Name of Student2 is: " + AllStudents[1].name)
console.log("Name of Student3 is: " + AllStudents[2].name)

let numbers = [1, 2, 3, 4, 5]

console.log(numbers.length)

numbers.push(6)
console.log(numbers);


numbers.pop()
console.log(numbers);

let fruits = ["Apple", "banana", "Cherry", "Jackfruit"]
console.log(fruits)

fruits[4] = "Mango"
console.log(fruits);

//Call Stacking

function first(){
    console.log("Hello First!")
}

function second(){
    first()
    console.log("Hello second!");
}

function third(){
    second()
    console.log("Hello Third!");

}

third();

//Math Objects
console.log(Math.PI)
console.log(Math.sqrt(16))
console.log(Math.floor(4.5))
console.log(Math.random())
console.log(Math.max(22, 24, 1000))
