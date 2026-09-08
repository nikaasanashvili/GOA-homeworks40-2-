// 1)შექმენი Function Expression --> square, რომელიც მიიღებს რიცხვს და დააბრუნებს მის კვადრატს.გამოიყენე Math
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი
// function Expression(namber, num){
//     return Math.pow(namber, num)
// }
// console.log(Expression(5, 3))



// 2)შექმენი Function Expression --> maxNumber, რომელიც მიიღებს ოთხ რიცხვს და დააბრუნებს მათგან დიდს.
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი
// function Expression(numbers){
//     return Math.max(...numbers)
// }
// console.log(Expression([5,34,2,1,6]))



// 3)პაროლის შემოწმება
// შექმენი Function Expression --> checkPassword, რომელიც დააბრუნებს true თუ პაროლი:
// მინიმუმ 8 სიმბოლოა და მთავრდება ასო "a" ზე
// სხვა შემთხვევაში დააბრუნოს false.

// const checkPassword = function(password){
//     if (password.length >= 8 && password.endsWith('a')){
//         return true;
//     }else{
//         return false;
//     }
// }
// console.log(checkPassword("passworda"))


// 4)შექმენი Function Expression --> isLuckyNumber, რომელიც დააბრუნებს true თუ რიცხვი:
// იყოფა 3-ზე
// და იყოფა 5-ზე
// სხვა შემთხვევაში დააბრუნოს false.(use ternary)
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი

// const isluckyNumber = function(num){
//     return num % 3 === 0 && num % 5 === 5 ? true : false;
// }


// 5)შექმენი Function Expression--> checkWord, რომელიც მიიღებს სიტყვას.
// თუ სიტყვა არის "javascript" დააბრუნოს:
// "Access Granted"
// სხვა შემთხვევაში:
// "Access Denied"
// # arrow=======================================
// const checkWord = str =>{
//     return str === 'javascript' ? 'access granted' : 'access denid'
// }

// 6)შექმენი Arrow Function --> isAdult, რომელიც მიიღებს ასაკს და დააბრუნებს:
// "Adult" თუ ასაკი 18 ან მეტია
// "Minor" სხვა შემთხვევაში
// ternary
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი

// const isAdult = age => {
//     return age >= 18 ? 'adult' : 'minor'
// }


// 7)შექმენი Arrow Function --> rectangleArea, რომელიც მიიღებს სიგრძეს და სიგანეს და დააბრუნებს ფართობს.
// გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით და ნახე შედეგი

// const rectangleArea = (sigrdze, sigane) => {
//     return sigrdze * sigane
// }



// 8)შექმენი Arrow Function -->  passwordStrength, რომელიც მიიღებს პაროლს:
// თუ პაროლის სიგრძე 8-ზე ნაკლებია და პაროლი მთავრდება ასო "ი" თი→ "Weak"
// თუ 8 ან მეტია და იწყება ასო "გ" თი → "Strong"
const passwordStrength = pass => {
    return pass.length < 8 && pass.endsWith("ი")? "Weak" : pass.startsWith("გ") && pass.length >= 8? "Strong" : ''
}

// 9)შექმენი Arrow Function -->  startsWith რომელიც მიიღებს რაიმე სტრინგს
// თუ სტრინგი იწყება "გ" თი და მთავრდება "ო" თი და სიგრძე trim() ით მეტია 8 ზე დააბრუნე --> რთული სახელი , სხვა შემთხვევაში მარტივი სახელი
// single line arrow =======================================
