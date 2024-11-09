'use strict'

function calculateSquareRoot(){
  const userConfirmed = confirm("Should I calculate the square root?");

  if (userConfirmed) {
    const number =parseFloat(prompt("Enter a number:"));

    if (number < 0 ) {
      document.getElementById("result").innerText = "The square root of a negative number is not defined.";
    }
    else {
      const SquareRoot = Math.sqrt(number);
      document.getElementById("result").innerText = `The square root of ${number} is ${SquareRoot} .`;
    }
  }
   else{
    document.getElementById("result").innerText = "The square root is not calculated."


  }

}