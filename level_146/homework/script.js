// // 8)შექმენი:
// let movie = {
//   title: "Interstellar",
//   genre: "Sci-Fi",
//   year: 2014,
//   rating: 9,

//   showInfo: function() {
//     console.log("Title: " + this.title);
//     console.log("Genre: " + this.genre);
//     console.log("Year: " + this.year);
//     console.log("Rating: " + this.rating);
//   }
// };
// showInfo() მეთოდმა უნდა დაბეჭდოს ფილმის ყველა ძირითადი ინფორმაცია:
// Title: Interstellar
// Genre: Sci-Fi
// Year: 2014
// Rating: 9



// 9)მოცემულია:
let product = {
  name: "Headphones",
  price: 200,
  inStock: true,

  checkProduct: function() {
    if (product.inStock === true){
        console.log("Headphones is available.")
    }else if(product.inStock === false){
        console.log("Headphones is not available.")
    }
  }
};

// checkProduct() მეთოდმა უნდა შეამოწმოს:
// თუ inStock არის true, დაბეჭდოს:
// Headphones is available.
// თუ inStock არის false, დაბეჭდოს:
// Headphones is not available.
// გამოიძახე მეთოდი




// 10)
let character = {
  name: "Knight",
  health: 100,
  power: 30,

  attack: function() {
    if (character.health > 0){
        console.log("Knight is alive!")
    }else{
        console.log("Knight is defeated!")
    }
  },

  showInfo: function() {
    console.log('name: ' + character.name)
    console.log("Health: " + character.health);
    console.log("Power: " + character.power);
  }
};
character.health = 0

character.attack

// showInfo() აჩვენებს პერსონაჟის ინფორმაციას.
// attack()-მა უნდა შეამოწმოს health:
// თუ health მეტია 0-ზე → დაბეჭდოს "Knight is alive!"
// წინააღმდეგ შემთხვევაში → "Knight is defeated!"
// შემდეგ ხელით შეცვალე health 0-ზე და კიდევ ერთხელ გამოიძახე attack()




