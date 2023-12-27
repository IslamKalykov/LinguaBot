// game.js
let score = 0;

document.addEventListener('DOMContentLoaded', function() {
    getNextWord();
});

document.getElementById('next-button').addEventListener('click', function() {
    getNextWord();
});

document.getElementById('new-round-button').addEventListener('click', function() {
    score = 0;
    document.getElementById('score').textContent = score;
    getNextWord();
});

function getNextWord() {
    fetch('/users/get_random_word/')
        .then(response => response.json())
        .then(data => {
            const currentWordElement = document.getElementById('current-word');
            const answerOptionsElement = document.getElementById('answer-options');

            currentWordElement.textContent = data.word;

            // Очищаем предыдущие варианты ответов
            answerOptionsElement.innerHTML = '';

            // Добавляем новые варианты ответов
            data.options.forEach(option => {
                const button = document.createElement('button');
                button.textContent = option;
                button.addEventListener('click', function() {
                    checkAnswer(option, data.translation);
                });
                answerOptionsElement.appendChild(button);
            });
        })
        .catch(error => {
            console.error('Error fetching next word:', error);
        });
}

function checkAnswer(selectedOption, correctAnswer) {
    const scoreElement = document.getElementById('score');

    if (selectedOption === correctAnswer) {
        score += 1;
        scoreElement.textContent = score;
        console.log('Правильный ответ!');
    } else {
        console.log('Неправильный ответ.');
    }

    // Загружаем следующее слово
    getNextWord();
}