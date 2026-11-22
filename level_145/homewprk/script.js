// 1)ექმენი ობიექტი student, რომელსაც ექნება შემდეგი properties:
// name: "Nika"
// age: 20
// course: "JavaScript"
// city: "Tbilisi"
// შემდეგ:

let student = {
    name: 'nika',
    course: 'javasqript',
    city: 'tbilisi'
}

// name გამოიტანე dot notation-ით.
console.log(student.name)
// age გამოიტანე bracket notation-ით.
console.log(student['age'])
// დაამატე ახალი property email მნიშვნელობით "nika@gmail.com".
student.email = 'nnika@gmail.com';
// დაამატე ახალი property grade მნიშვნელობით 95.
student.grade = 95;
// city შეცვალე "Batumi"-თ.
student.city = 'batumi'
// წაშალე age.
delete student.age
// ბოლოს console.log()-ით გამოიტანე მთელი ობიექტი.
console.log(student)





// 2)შექმენი ობიექტი product:
// {
//     name: "Laptop",
//     price: 2500,
//     brand: "Lenovo",
//     category: "Electronics"
// }

// შეასრულე შემდეგი:

// გამოიტანე name dot notation-ით.
// გამოიტანე price bracket notation-ით.
// შეცვალე price და გახადე 2200.
// შეცვალე brand და გახადე "Asus".
// დაამატე stock property მნიშვნელობით 15.
// დაამატე "product color" property მნიშვნელობით "Black".
// გამოიტანე "product color" მხოლოდ bracket notation-ით.
// წაშალე category.
// ბოლოს გამოიტანე მთელი product ობიექტი.


// 3)შექმენი ობიექტი car შემდეგი მონაცემებით:

// {
//     brand: "BMW",
//     model: "X5",
//     year: 2020,
//     price: 45000
// }

// შემდეგ:

// გამოიტანე brand dot notation-ით.
// გამოიტანე model bracket notation-ით.
// year შეცვალე 2024-ით.
// price შეცვალე 50000-ით.
// დაამატე color property მნიშვნელობით "Black".
// დაამატე "engine type" property მნიშვნელობით "Diesel".
// გამოიტანე "engine type" bracket notation-ით.
// წაშალე price.
// დაამატე ახალი property isNew მნიშვნელობით true.
// საბოლოოდ გამოიტანე მთელი ობიექტი.


// 4)შექმენი ობიექტი character:

// {
//     name: "Knight",
//     level: 10,
//     health: 100,
//     weapon: "Sword"
// }

// შეასრულე:

// გამოიტანე პერსონაჟის name.
// გამოიტანე health bracket notation-ით.
// პერსონაჟის level გაზარდე 1-ით.
// health შეცვალე 80-ით.
// დაამატე armor property მნიშვნელობით "Steel Armor".
// დაამატე "favorite weapon" property მნიშვნელობით "Sword".
// გამოიტანე "favorite weapon" bracket notation-ით.
// წაშალე weapon.
// დაამატე ახალი weapon მნიშვნელობით "Axe".