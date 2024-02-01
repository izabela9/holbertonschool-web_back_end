function changeHeaderColor() {
    const headerElement = document.querySelector('header');
    headerElement.style.color = '#FF0000';
}
const redHeaderEl = document.getElementById('red_header');

redHeaderEl.addEventListener('click', changeHeaderColor);
