// 1)მომხმარებელს შემოატანინე სახელი prompt-ით.
// თუ სახელი იწყება "A" ასოზე, კონსოლში გამოიტანე "სახელი იწყება A-ზე", სხვა შემთხვევაში "სახელი არ იწყება A-ზე".
// let name = prompt("enter your name: ")
// if (name.startsWith('A')){
//     console.log("saxeli iwyeba A-ze")
// }

// else {
//     console.log("ar iwyeba A-ze")
// }

// // 2)მომხმარებელს შემოატანინე პაროლი.
// // თუ პაროლის სიგრძე 8-ზე მეტია, გამოიტანე "ძლიერი პაროლი", სხვა შემთხვევაში "სუსტი პაროლი". გამოიყენე property რომელიც იგებს სტრინგის სიგრძეს
// let pass = prompt("enter pas:")
// if(pass.length > 8){
//     console.log("paroli dzlieria")
// }
// else{
//     console.log("susti paroli")
// }

// 3)მომხმარებელს შემოატანინე ტექსტი.
// trim() გამოიყენე და თუ ტექსტის სიგრძე 0 გამოვიდა, დაწერე "ცარიელი ტექსტია", სხვა შემთხვევაში "ტექსტი შევსებულია".

// let txt = prompt("enter txt: ")
// txt = txt.trim()
// if(txt.length === 0){
//     console.log("carieli teqstia")
// }
// else{
//     console.log("teqsti shevsebulia")
// }

// 4)მომხმარებელს შემოატანინე რაიმე სახელი
//  თუ სახელი იწყება ასო "ა" ზე გამოიტანე კონსოლში ცვლადში შენახული მნშვნელკობა ოღონდ დიდი ასოებით
// სხვა შემთხვევაში გამოიტანე ცვლადში შენახული მნიშვნელობა პატარა ასოებში

// let name = prompt("enter your name: ")

// if(name.startsWith('a')){
//     console.log(name.toUpperCase())
// }
// else{
//     console.log(name)
// }

// 5)შექმენი ცვლადი სადაც შეინახავ რაიმე სტრინგს
// შეამოწმე თუ სახელი იწყება ასო"კ" ზე კონსოლში გამოიტანე ამ ცვლადში შენახულიმნიშვნელობის სიგრძე
// სხვა შემთხვევაში დაუკონსოლლოგე __> "error"

// let txt = 'knika'

// if(txt.startsWith("k")){
//     console.log(txt.length)
// }
// else{
//     console.log(txt)
// }