const student1 = {
    name : "Moheathraam",
    age : 14,
    skills : "HTML, CSS and Javascript"
}



const student2 = {
    name : "Michael",
    age : 13,
    skills : "Football, Basketball and athletics"
}

//function for obj 
function DetailPrinter(obj){
    console.log("\nStudent's name is: " + obj.name )
    console.log("Student's age is: " + obj.age)
    console.log("Student's skills is: " + obj.skills)
}

DetailPrinter(student1)
DetailPrinter(student2)

//Date, Time, Year, Timezone
let currentDate = new Date();
console.log("\nCurrent date and time: ",currentDate);
console.log("\nCurrent date: ",currentDate.getDate());
console.log("\nYear: ",currentDate.getFullYear());

console.log("\nRandom Number between 0-1: ",Math.random())
