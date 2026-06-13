// // 1)შექმენი ფუნქცია greet(name), რომელიც დაბეჭდავს: Hello, name!
// // გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით

// function greet(name){
//     console.log('hallo' + name + '!')
// }
// greet("nika")
// greet("saba")
// greet("daviti")
// greet(dachi)

// // 2)შექმენი ფუნქცია showAge(age), რომელიც დაბეჭდავს: You are age years old.
// // გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// function showAge(age){
//     console.log("you are" + age + 'years old')
// }
// showAge(17)
// showAge(5)

// // 3)შექმენი ფუნქცია sum(a, b), რომელიც დაბეჭდავს ორი რიცხვის ჯამს.
// // გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// function sum(a, b){
//     console.log(a + b)
// }
// sum(10, 5)
// sum(5, 6)


// // 4)შექმენი ფუნქცია multiply(a, b), რომელიც დაბეჭდავს ორი რიცხვის ნამრავლს.
// // გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// function multiply(a, b){
//     console.log(a * b)
// }
// multiply(10, 5)
// multiply(5, 6)


// 5)შექმენი ფუნქცია fullName(firstName, lastName), რომელიც დაბეჭდავს სრულ სახელს ერთ სტრინგად.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// # medium hard

// function fullName(firstName, lastName){
//     console.log(firstName +" "+ lastName)
// }
// fullName('nika', 'asanashvili')
// fullName('daviti', 'asanashvili')

// 6)შექმენი ფუნქცია isAdult(age).
// თუ ასაკი(პარამეტი) 18 ან მეტია, დაბეჭდოს Adult, სხვა შემთხვევაში Minor.(გამოიყენე ternary)
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
  
// function isAdult(age){
//     console.log(age >= 18 ? 'adult' : 'minor')
// }
// isAdult(10)
// isAdult(28)
// isAdult(11)

// 7)შექმენი ფუნქცია checkNumber(num).
// თუ რიცხვი(პარამეტრი) დადებითია — დაბეჭდოს Positive, უარყოფითია — Negative, ხოლო 0-ზე — Zero , გამოიყენე ternary
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით

// 8)შექმენი ფუნქცია rectangleInfo(width, height), რომელიც დაბეჭდავს მართკუთხედის ფართობს: width * height.
// გამოიძახე ფუნქცია რამდენჯერმე განსხვავებული არგუმენტებით
// # harder
// function rectangleInfo(width, height){
//     console.log(width * height)
// }
// rectangleInfo(5, 10)
// rectangleInfo(3, 5)
// rectangleInfo(7, 3)

// 9)შექმენი ფუნქცია greetUser(name, time).
// თუ time არის "morning", დაბეჭდოს Good morning, ${name}!
// თუ time არის "evening" — Good evening, ${name}!
// სხვა შემთხვევაში — Hello, name!
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

// function greetUser(name, time){
//     if (time === "morning"){
//         console.log(`Good morning, ${name}!`);
//     }

//     else if (time === "evening"){
//         console.log(`Good evening, ${name}!`);
//     }

//     else{
//         console.log(`Hello, ${name}!`);
//     }
// }
// greetUser("Nika", "morning");
// greetUser("Gio", "evening");
// greetUser("Luka", "afternoon");
// greetUser("Ana", "night");

// 10)შექმენი ფუნქცია checkPassword(password).
// თუ პაროლის სიგრძე 8-ზე ნაკლებია, დაბეჭდოს Password is too short, სხვა შემთხვევაში Password accepted.(ternary)
// გამოძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით