//Normall Function
function name(a, b){
    console.log(a + b)
}

// Anonymous Function

let sum = function(a, b){
    console.log(a - b)
}

    


//arrow function

let divide = (a, b) => {
    console.log(a / b)
}

let mul = (a, b) => console.log(a * b)

//calling
name(10, 6)
sum(14, 5)
divide(14, 7)
mul(2, 10)

// Try and Catch
try{
     console.log(HelloMohit)
}
catch(error)
{
  console.log("Oh uh U made an error: " + error.message )
}

try{
    let a = 13
    let b = 12
    let sum = a - b;
    console.log(sum)
}
catch(error){
       console.log("Uh Oh You made an error again!:  " + error.message )
}

//Advanced 
try{
    let json = `{"name" : "Christopher"}`
    let user = JSON.parse(json)
    console.log(user.name)

    //ERROR
    let invjson = "{`name` : `Harold`}"
    let invuser = JSON.parse(invjson)
    console.log(invuser.name)
}
catch(error){
     console.log("U made an error again: " + error.message)
}

//Check if theres are some specific characters in the variables
let value = "I want some 1ceCre@m"
let regex = /\d/
console.log(regex.test(value))