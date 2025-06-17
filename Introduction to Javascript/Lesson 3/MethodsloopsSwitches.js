const student = {
    name: "Moheathraam",
    greet: function (){
        console.log(`Hello ${this.name}`)
    }
}

console.log(student.name);
student.greet();

//init : condition ; increment

for(i = 1 ; i <= 5 ; i++){
    console.log(`This is loop iteration number: ${i}`)
}

//While loop
let count = 1
while(count <= 10){
    console.log(`This is while loop: ${count}`)
    count++;
}

//Swithes and cases!

let day = "friday";

switch(day){
    case  "monday":
    console.log("Start of the Week!")
    break;

    case "wednesday":
    console.log("Keep Going! The Middle of the week!")
    break;

    case "friday":
    console.log("End of the week! Ready to have a fun weekend?")
     break;

    default:
        console.log("A reagular day!")
        break;

}
