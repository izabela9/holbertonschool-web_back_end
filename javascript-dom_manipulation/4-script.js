function addItemToList() {
    const newLiEl = document.createElement('li');
    newLiEl.textContent = 'Item';

    const myListElement = document.querySelector('.my_list');
    myListEl.appendChild(newLiEl);
}
const addItemEl = document.getElementById('add_item');
addItemEl.addEventListener('click', addItemToList); 
