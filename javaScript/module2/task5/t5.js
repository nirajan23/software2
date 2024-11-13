
function getNumbers() {
    const numbers = [];
    while (true) {
        let input = prompt("Enter a number:");

        let num = Number(input);

        if (isNaN(num)) {
            alert("Please enter a valid number.");
            continue;
        }

        if (numbers.includes(num)) {
            alert(`The number ${num} has already been given. Stopping input.`);
            break;
        }

        numbers.push(num);
    }

    return numbers;
}

function displayNumbersInAscendingOrder(numbers) {
    numbers.sort((a, b) => a - b);
    target.textContent = `Numbers in ascending order: ${numbers.join(", ")}`;
}


const numbers = getNumbers();
displayNumbersInAscendingOrder(numbers);