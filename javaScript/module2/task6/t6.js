
function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

function main() {
    const target = document.getElementById("target");
    let rollResult;
    let rolls = [];

    do {
        rollResult = rollDice();
        rolls.push(rollResult);
    } while (rollResult !== 6);


    for (let roll of rolls) {
        document.querySelector('#target').innerHTML += `<li>${roll}</li>`;
    }


}



main();
