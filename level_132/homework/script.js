// // 1)გაქვს
// const numbers = [2,5,8,10,13,20]
// // for ციკლით შექმენი ახალი მასივი, სადაც მხოლოდ 10-ზე დიდი რიცხვები იქნება.
// let NewLst=[]
// for (let i = 0; i < numbers.length; i++){
//     if (numbers[i] > 10){
//         NewLst.push(numbers[i])
//     }
// }
// console.log(NewLst)



// 



// // 3)შექმენით სახელების სია , ასევე შექმენით ცარიელი სია ,სახელების სიიდან ცარიელ 
// // სიაში გადაიტანეთ ისეთი ელემენტები რომებიც იწყება "g" ზე და ასევე მისი სიგრძე მეტია 5 ზე

// let names = ['nika', 'guka', 'saba', 'giorgi', 'daviti', 'dachi', 'gela']
// let Gnames = []
// for (let i = 0; i < names.length; i++){
//     if (names[i][0] === 'g' && names[i].length > 5){
//         Gnames.push(names[i])
//     }
// }
// console.log(Gnames)




// // 4)შექმენით რიცხვების სია და ასევე ცარიელი სია,შენი დავალებაა რომ სიიდან ამოშალო
// //  ლუწი რიცხვები და დატოვომხოლოდ კენტი რიცხვები , გამოგადგებათ splice() მეთოდი
// let lst = [4, 5, 2, 11, 12, 42, 21, 9]
// let Lnumbers = []

// for (let i = 0; i < lst.length; i++){
//     if (lst[i] % 2 === 0){
//         Lnumbers.push(lst[i])
//     }
//     else if (lst[i] % 2 != 0){
//         lst.splice(i, 1)
//     }
// }
// console.log(lst)
// console.log(Lnumbers)

