function addRedClassToHeader() {
    const headerElement = document.querySelector('header');
    headerElement.classList.add('red');
}

const redHeaderEl = document.getElementById('red_header');

redHeaderEl.addEventListener('click', addRedClassToHeader);
