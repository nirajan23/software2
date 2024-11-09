'use strict'

function checkLeapYear() {
  const year = parseInt(prompt("Enter year to check whether leap or not: "));


  let result;
  if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    result = `${year} is a leap year.`;
  } else {
    result = `${year} is not a leap year.`;
  }

  document.getElementById("result").innerHTML = result;
}
