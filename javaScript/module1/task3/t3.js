'use strict';
function calculate() {

    const a  = parseInt(prompt("Enter your the first number: "));
    const b = parseInt(prompt("Enter the second number: "));
    const c = parseInt(prompt("Enter the third number: "));

    const sum = a + b + c;
    const product = a * b * c;
    const average = sum / 3;

    document.getElementById("results").innerHTML = `
        Sum: ${sum} <br>
        Product: ${product} <br>
        Average: ${average.toFixed(2)}
    `;


}
