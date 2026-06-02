// მომხმარებელს შემოაყვანინეთ რაიმე სტრინგი
// შემდეგ შეამოწმეთ --> თუ ეს სტრინგი იწყება ასო "g" ზე --> და <-- ამ სტრინგის სიგრძე
// არის 6 ზე მეტიანტოლი დააკონსოლლოგე --> "იწყება გ ასოზე და არის გრძელი სიტყვა" 
// თუ ეს სტრინგი იწყება ასო "a" ზე და მისი გირძე ნაკლებია 6 ზე დააკონსოლლოგე ---> 
// "იწყება ა ასოზე და არის მოკლე სიტყვა"
// სხვა შემთხვევაშ დაუკონსოლლოგე --> "ამოუცნობი სიტგვა"

let name = prompt("enter your name: ")

if(name.startsWith("g") && name.length >= 6){
    console.log('iwyeba g-ze da aris grdzeli sityva')
}

else if(name.startsWith('a') && name.lenght < 6){
    console.log("iwyeba a-ze da aris mokle sityva")
}

else{
    console.log('amoucnobi sityva')
}


let txt = prompt("enter txit: ")

if (txt.startsWith("a")  || txt.length > 6){
    console.log("kk")
}

else if(txt.startsWith('g') || txt.length < 6){
    console.log("bb")
}