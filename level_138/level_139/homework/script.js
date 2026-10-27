// // 1)შექმენი ფუნქცია greet, რომელიც ბეჭდავს "Hello!".
// // შექმენი ფუნქცია process, რომელსაც პარამეტრად გადაეცემა ფუნქცია და შიგნით გამოიძახებს მას.

// function greet(){
//     console.log("hallo")
// }

// function process(callback){
//     callback()
// }
// process(greet)


// // 2)შექმენი:
// // sayHello()
// // sayBye()
// // process ფუნქციას(პირველ დავალებაში შექმნილი) გადაეცი ერთ-ერთი მათგანი და გამოატანინე შესაბამისი ტექსტი.
// // მაგალითად:
// // process(sayHello);

// function sayHello(){
//     console.log('hallo')
// }

// function sayBye(){
//     console.log('bye')
// }

// function process(callback){
//     callback()
// }
// process(sayBye)
// process(sayHello)




// // 3)შექმენი ფუნქცია showNumber, რომელსაც პარამეტრად გადაეცემა რიცხვი და ბეჭდავს მას.
// // შექმენი processNumber, რომელსაც გადაეცემა:
// // რიცხვი
// // callback ფუნქცია
// // და შიგნით callback-ს გადასცეს ეს რიცხვი.
// // მაგალითად:
// // processNumber(10, showNumber);

// function showNumber(number){
//     console.log(number)
// }

// function processNumber(number, Callback){
//     Callback(number)
// }
// processNumber(10, showNumber)





// 4)საშუალო — Callback + მონაცემის გადაცემა
// 4. ორი მოქმედება რიცხვზე
// შექმენი ორი ფუნქცია:
// double(number)
// square(number)
// პირველმა რიცხვი გააორმაგოს, მეორემ კვადრატში აიყვანოს.
// შექმენი:
// calculate(number, callback)
// რომელიც მიღებულ რიცხვზე შეასრულებს callback-ს.
// მაგალითად:
// calculate(5, double);
// calculate(5, square);

// function double(number){
//     console.log(number * 2)
// }


// function square(number){
//     console.log(number * number)
// }


// function calculate(number, callback){
//     callback(number)
// }
// calculate(5, double)





// // 5)შექმენი ორი ფუნქცია:
// // toUpper(text)
// // toLower(text)
// // ერთი ტექსტს გადაიყვანს დიდ ასოებში, მეორე — პატარა ასოებში.
// // შემდეგ შექმენი:
// // processText(text, callback)
// // და გამოიყენე ორივე callback-თან.

// function toUpper(text){
//     console.log(text.toUpperCase())
// }

// function toLower(text){
//     console.log(text.toLowerCase())
// }

// function processText(text, callback){
//     callback(text)
// }
// processText('nika', toLower)
// processText('nika', toUpper)






// // 6)შექმენი:
// // formal(name)
// // friendly(name)
// // formal უნდა აბრუნებდეს:
// // Good evening, Goga
// // friendly:
// // Hey Goga!
// // შემდეგ შექმენი:
// // greetUser(name, callback)
// // რომელიც callback-ის საშუალებით განსაზღვრავს, როგორ მივესალმოთ მომხმარებელს.

// function formal(name){
//     console.log(`Good evening, ${name}`)
// }

// function friendly(name){
//     console.log(`Hey ${name}!`)
// }

// function greetUser(name, callback){
//     callback(name)
// }








