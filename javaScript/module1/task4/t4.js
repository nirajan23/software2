'use strict'
function sortStudent(){
  const name = prompt("Enter your name to be sorted into house:")

  const randomHouse = Math.floor(Math.random() * 4) + 1;

  let house;

  if (randomHouse === 1) {
      house = "Gryffindor";
  } else if (randomHouse === 2) {
      house = "Slytherin";
  } else if (randomHouse === 3) {
      house = "Hufflepuff";
  } else {
      house = "Ravenclaw";
  }


  document.getElementById("result").innerHTML = `${name}, you are in ${house}!!!`;
}