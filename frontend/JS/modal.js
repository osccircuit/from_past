'use strict'

// Предположим, что мы храним текст письма прямо здесь
const letterText =
	'Здравствуйте! Это пример текста архивного письма. Здесь может быть ваше сообщение.'

// Получаем элементы DOM
const readBtn = document.querySelector('.read-btn')
const modal = document.getElementById('modal')
const closeBtn = document.querySelector('.close-btn')
const letterParagraph = document.getElementById('letter-text')

// Функция открытия модального окна
readBtn.addEventListener('click', () => {
	letterParagraph.textContent = letterText // Подставляем текст письма
	modal.style.display = 'block' // Показываем модальное окно
})

// Функция закрытия модального окна
closeBtn.addEventListener('click', () => {
	modal.style.display = 'none'
})

// Также можно закрывать по клику вне окна
window.addEventListener('click', event => {
	if (event.target === modal) {
		modal.style.display = 'none'
	}
})
