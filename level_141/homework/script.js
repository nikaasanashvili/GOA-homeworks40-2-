// 1)
// let scores = [45, 67, 32, 89, 54, 71, 38, 90];

// .forEach()-ის გამოყენებით:

// დაბეჭდე თითოეული ქულა;
// თუ ქულა 50-ზე ნაკლებია, დაბეჭდე "Failed";
// თუ 50 ან მეტია, დაბეჭდე "Passed".

// 2)let names = ["goga", "nika", "luka", "ana", "giorgi"];

// .forEach()-ის გამოყენებით დაბეჭდე თითოეული სახელი ასე:

// 1. GOGA
// 2. NIKA
// 3. LUKA
// ...

// გამოიყენე .toUpperCase().

// 3)let prices = [20, 35, 50, 80, 120, 200];

// .map()-ით შექმენი ახალი მასივი, სადაც ყველა ფასი გაზრდილი იქნება 20-ით.

// // 4)დავალება 7 — რიცხვების გაფილტვრა
// let numbers = [12, 45, 7, 89, 23, 56, 91, 34, 18];
// // .filter()-ის გამოყენებით დატოვე მხოლოდ ის რიცხვები, რომლებიც:
// // 20-ზე მეტია და 80-ზე ნაკლები.
// let num = numbers.filter(function(ricxvebi) {
//     return ricxvebi > 20 && ricxvebi < 80
// })


// // 5)
// let names = ["Giorgi", "Ana", "Alexander", "Nika", "Gabriel", "Luka"];
// // .filter()-ით დატოვე მხოლოდ ის სახელები, რომელთა სიგრძეც 5 ან მეტია.
// let meti = names.filter(function(saxeleb){
//     return saxeleb.length >= 5
// })
// console.log(meti)


// // 6)
// let words = ["apple", "banana", "avocado", "orange", "apricot", "grape"];
// // .filter()-ის გამოყენებით დატოვე მხოლოდ ის სიტყვები, რომლებიც იწყება "a" ასოთი.
// let startsA = words.filter(function(saxelebi){
//     return saxelebi.startsWith('a')
// })
// console.log(startsA)


// // 7)
// let numbers = [12, 18, 25, 31, 45, 60, 72];
// // .findIndex()-ით იპოვე პირველი რიცხვის ინდექსი, რომელიც 40-ზე მეტია.
// let indeqsi = numbers.findIndex(function(ricxvebi){
//     return ricxvebi > 40
// })



// 8)let names = ["Nika", "Giorgi", "Ana", "Luka", "Saba", "Goga"];
// .findIndex()-ის გამოყენებით იპოვე "Saba"-ს ინდექსი.
// დამატებითი პირობა: თუ ასეთი სახელი არ არსებობს, დაბეჭდე:
// Name not found

// 9)let numbers = [15, 22, 8, 4, -3, 17, -9, 30];
// .findIndex()-ით იპოვე პირველი უარყოფითი რიცხვის ინდექსი.