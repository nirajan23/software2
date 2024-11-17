
const targetElement = document.getElementById('target');

const items = ['First item', 'Second item', 'Third item'];

items.forEach((itemText, index) => {
    const listItem = document.createElement('li');

    listItem.textContent = itemText;

    if (index === 1) {
        listItem.classList.add('my-item');
    }

    targetElement.appendChild(listItem);
});
