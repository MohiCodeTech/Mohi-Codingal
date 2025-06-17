//Json stuff
// student = {
//     name : "Student",
//     age : 14,
//     skills : "Chess, Scrabble"
// }

// let JSONstudent = JSON.stringify(student)
// console.log("This is json format", JSONstudent)

// let objstudent = JSON.parse(JSONstudent)
// console.log("This is object format", objstudent)

// //Callbacks

// function cal2(a, b){
//     return a + b;
// }

// function Calculate(a, b, callback){
//     return callback(a , b);
    
// }

// let ans = Calculate(15, 30 , cal2)
// console.log(ans)

// //Promises
// let alp = new Promise((res , rej)=>{
//     let a = true
//     if(a){
//         res("Data Fetched is positive")
//     }
//     else{
//         rej("Error 404💻 Please try again")
//     }
// })
// alp
// .then((Data)=>{
//     console.log(Data)
// })
// .catch((error)=>{
//     console.log(error)
// })