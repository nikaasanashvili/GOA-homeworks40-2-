
const fruits = [["Banana", "Orange"], ["Apple", "Mango" , "Pineapple"], ["Onion" , "Garlic"]];
// პირველ რიგში დაშალეთ ეს პატარა სიები და გააერთიანეთ ერთ დიდ სიად შესაბამისი მეთდის გამოყენებით(შეინახეთ ცვლადში)
// შენი დავალებაა წინა სიიდან რომელიც fruits სიიდან მიიღე და დაშალეთ ->  ახალი სიის სახით მიიღო სია შემდეგი ელემენტებით -> 
//  "Apple", "Mango" , "Pineapple", "Onion"
// გამოიყენე slice() და დააკონსოლლოგე ახალი სია
// ასევე დააკონსოლე ძველი სიაც რადგან ნახოთ რომ ძველ სიას არაფერი მოსდის და იგივე რჩება -->


const allFruits = fruits.flat();
console.log(allFruits);


// slice()-ის გამოყენებით მივიღოთ:
// "Apple", "Mango", "Pineapple", "Onion"

const newFruits = allFruits.slice(2, 6);
console.log(newFruits);

console.log(allFruits);