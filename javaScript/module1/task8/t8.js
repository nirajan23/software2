'use strict';

const startYear = prompt('input start year');
const endYear = prompt("enter ending year");


for (let i = startYear; i <= endYear; i ++) {
  if ((i % 4 === 0 && i % 100 !== 0) || (i % 400 === 0)) {
    document.querySelector('#target').innerHTML += `<li>${i}</li>`;
  }
}