const coinflipScore = JSON.parse(localStorage.getItem('coinflipScore')) || {
    wins : 0,
    loss : 0
}

let guess = '';

const headsBtn = document.querySelector('.headsBtn');
const tailsBtn = document.querySelector('.tailsBtn');

function playGame(guess) {
    const randomNumber = Math.random();
    const result = randomNumber < 0.5 ? 'Heads' : 'Tails';

    if(guess === 'Heads') {
        if(result === 'Heads') {
            coinflipScore.wins++;

            alert('You guess it right.')
        } else if(guess === 'Tails') {
            coinflipScore.loss++;

            alert('You guess it wrong.');
        } else {
            alert('Error');
        }
    } else if(guess === 'Tails') {
        if(result === 'Heads') {
            coinflipScore.loss++;

            alert('You guess it wrong.');
        } else if(guess === 'Tails') {
            coinflipScore.wins++;

            alert('You guess it right.');
        }
    } else {
        alert('Error');
    }

    localStorage.setItem('coinflipScore', JSON.stringify(coinflipScore));

};

headsBtn.addEventListener('click', function() {
    guess = 'Heads';

    playGame(guess);

    console.log(coinflipScore);
});

tailsBtn.addEventListener('click', function() {
    guess = 'Tails';

    playGame(guess);

    console.log(coinflipScore);
});