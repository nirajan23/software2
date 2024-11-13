function getParticipants() {
    let numParticipants = parseInt(prompt("Enter the number of participants:"));

    let participants = [];

    for (let i = 1; i <= numParticipants; i++) {
        let name = prompt(`Enter the name of participant ${i}:`);
        participants.push(name);
    }

    participants.sort();

    let participantListDiv = document.getElementById("participantList");
    participantListDiv.innerHTML = "<h3>Participants (Alphabetical Order):</h3><ol>";
    for (let i = 0; i < participants.length; i++) {
        participantListDiv.innerHTML += `<li>${participants[i]}</li>`;
    }
    participantListDiv.innerHTML += "</ol>";
}
