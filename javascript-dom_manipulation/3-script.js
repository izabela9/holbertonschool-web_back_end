function toggleHeaderClass() {
	const headerEl = document.querySelector('header');

	if (headerEl.classList.contains('red')) {
		headerEl.classList.remove('red');
		headerEl.classList.add('green');
	} else {
		headerEl.classList.remove('green');
		headerEl.classList.add('red');
	}
}

const toggleHeaderEl = document.getElementById('toggle_header');
toggleHeaderEl.addEventListener('click', toggleHeaderClass);
