// t4.js

const target = document.getElementById("target");

function getNumbers() {
    const numbers = [];
    while (true) {
        let input = prompt("Enter a number (0 to stop):");

        let num = Number(input);

        if (num === 0) break;

        if (!isNaN(num)) {
            numbers.push(num);
        } else {
            alert("Please enter a valid number.");
        }
    }
    return numbers;
}

function displaySortedNumbers(numbers) {
    numbers.sort((a, b) => b - a);

    for (let number of numbers) {
        document.querySelector('#target').innerHTML += `<li>${number}</li>`;
    }
}

const numbers = getNumbers();
displaySortedNumbers(numbers);
