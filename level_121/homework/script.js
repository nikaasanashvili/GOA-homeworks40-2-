// 1)შექმენი ფუნქცია analyzeTemperature(temp) რომელიც:
// თუ ტემპერატურა 30-ზე მეტია, დააბრუნებს "Hot".
// თუ 15-30 შუალედშია, დააბრუნებს "Normal".
// თუ 15-ზე ნაკლებია, დააბრუნებს "Cold".
// ternary

// function analyzeTemperature(temp){
//     return temp > 30 ? 'hot' : temp > 15 ? 'normal' : 'cold'
// }
// console.log(analyzeTemperature(1))


// 2)შექმენი ფუნქცია:
// calculateSalary(hoursWorked, hourlyRate = 20)
// რომელიც დააბრუნებს მთლიან ხელფასს.
// მაგალითად:
// calculateSalary(8) // 160
// calculateSalary(10, 30) // 300

// function calculateSalary(hoursWorked , hourlyRate = 20){
//     return hoursWorked * hourlyRate
// }


// 3)შექმენი ფუნქცია numberType(num) რომელიც დააბრუნებს:
// "Positive"
// "Negative"
// "Zero"
// .sign()




// 4)ბილეთის ფასი
// შექმენი ფუნქცია:
// ticketPrice(age, isStudent = false)
// წესები:
// 12 წლამდე → 5 ლარი.
// 12-დან 60 წლამდე → 15 ლარი.
// 60+ → 8 ლარი.

// function ticketPrice(age, isStudent = false){

// }

// 5)შექმენი ფუნქცია:
// grade(score)
// რომელიც აბრუნებს:
// 90-100 → "A"
// 80-89 → "B"
// 70-79 → "C"
// 60-69 → "D"
// 0-59 → "F"
// switch()



function grade(score){
    switch(true){
        case score >= 90:
            return 'A';
            break
        case score >= 80:
            return 'B';
            break
        case score >= 70:
            return 'C'
            break
        case score >= 60:
            return 'D'
            break
        case score >= 0:
            return 'F'
    }
}
console.log(grade(70))