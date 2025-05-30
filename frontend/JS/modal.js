'use strict'

// Предположим, что мы храним текст письма прямо здесь
const letterText =
	'Это письмо отправлено из прошлого. Получатель - ты. Время изменилось, ты изменилась…В рамках спецификации современных стандартов, независимые государства, вне зависимости от их уровня, должны быть заблокированы в рамках своих собственных рациональных ограничений. Ясность нашей позиции очевидна: консультация с широким активом не оставляет шанса для своевременного выполнения сверхзадачи. Лишь независимые государства освещают чрезвычайно интересные особенности картины в целом, однако конкретные выводы, разумеется, ограничены исключительно образом мышления.'

// Получаем элементы DOM
const readBtn = document.querySelector('.read-btn')
const modal = document.getElementById('modal')
const closeBtn = document.querySelector('.close-btn')
const letterParagraph = document.getElementById('letter-text')

// Функция открытия модального окна
readBtn.addEventListener('click', () => {
	console.log('Кнопка нажата')
	letterParagraph.textContent = letterText
	modal.style.display = 'block'
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
