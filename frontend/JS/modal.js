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

document.addEventListener('DOMContentLoaded', function () {
	const archiveButtons = document.querySelectorAll('.btn-archive')

	archiveButtons.forEach(button => {
		button.addEventListener('click', function (e) {
			e.preventDefault()

			const year = button.dataset.year

			// Пример текста для писем — можно позже заменить на запрос к серверу
			const letters = {
				2018: 'Дорогая Мария, это письмо из 2018 года. Мы тогда только начинали наш путь...',
				2019: 'Мария, вспоминаю 2019 год с теплотой. Тогда всё было иначе...',
				2020: 'Письмо из 2020 года. Год перемен и размышлений.',
				2021: 'Это послание из 2021 года — время надежды и восстановления.',
				2022: 'Письмо из 2022 года. Мы стали ближе и сильнее.',
				2023: '2023 год был богат событиями. Вот что я тогда чувствовала...',
			}

			const letterText = letters[year] || 'Письмо не найдено.'

			const letterHTML = `
				<!DOCTYPE html>
				<html lang="ru">
				<head>
					<meta charset="UTF-8">
					<title>Письмо из ${year} года</title>
					<style>
						body {
							font-family: 'Lora', serif;
							padding: 2rem;
							background-color: #fffaf0;
							color: #250524;
							line-height: 1.6;
						}
						h2 {
							color: #380835;
						}
					</style>
				</head>
				<body>
					<h2>Письмо из ${year} года</h2>
					<p>${letterText}</p>
				</body>
				</html>
			`

			const letterWindow = window.open('', '_blank', 'width=600,height=400')
			letterWindow.document.write(letterHTML)
			letterWindow.document.close()
		})
	})
})
