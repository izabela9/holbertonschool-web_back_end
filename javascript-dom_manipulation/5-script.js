function updateHeaderText() {
	const headerEl = document.querySelector('header');
	headerEl.textContent = 'New Header!!!';
}
const updateHeaderEl = document.getElementById('update_header');
updateHeaderEl.addEventListener('click', updateHeaderText);
