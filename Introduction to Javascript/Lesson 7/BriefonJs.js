//scopes
function Parentfunction(){
    var parentvar = 12
    function childfunction(){
        var childvar = 45
        childvar = 13
        console.log("This is childvar inside of child function " + childvar)
        parentvar = 15;
        console.log("This is parentvar inside of childfunction " + parentvar)
    }
    childfunction();
    childvar = 98;
    console.log("This is childvar outside of child function " + childvar)
    console.log("This is parentvar outside of childfunction " + parentvar)
}

Parentfunction()

//let and const scopes

if(true){
    let a = 10
     a = 11
     console.log(a)
}

if(true){
    const b = 15
     console.log(b)
}

//while loop
let i = 10
while(i >= 1){
    console.log(i)
    i--;
}