class students  {
    constructor(name, age, skills){
        this.name = name;
        this.age = age;
        this.skills = skills;
    }
    speak(){
       console.log(`${this.name} can speak!`)
    }
    walk(){
       console.log(`${this.name} can walk!`)
    }
    details(){
        console.log(` Hello my name is ${this.name} And my age is ${this.age} And my Skills are ${this.skills} `)
    }
}

const student1 = new students("Moheathraam", 14, "Html, Css, js")
student1.details();
student1.speak();
student1.walk();
console.log("\nOn to the Next Student!")

const student2 = new students("Utik", 14, "Academics")
student2.details();
student2.speak();
student2.walk();

//Animal Class

class Animals{
    constructor(name){
        this.name = name
    }
    speak(){
        console.log(`${this.name} Makes a sound`)
    }
}

class Dog extends Animals{
    speak(){
        console.log(`${this.name} Barks`)
    }
}

const pal = new Dog("Buddy")
pal.speak()

class Cat extends Animals{
    speak(){
        console.log(`${this.name} Meows`)
    }
}

const Gingercat = new Cat("Ginger")
Gingercat.speak()