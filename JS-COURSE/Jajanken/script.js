const rockBtn = document.querySelector('.rock');
const paperBtn = document.querySelector('.paper');
const scissorBtn = document.querySelector('.scissor')
const resetScoreBtn = document.querySelector('.reset-score-btn');
let result = '';
let randomNumber = 0;
let botMove;

let score = JSON.parse(localStorage.getItem('score')) || {
    win : 0,
    loss : 0,
    tie : 0
};

// if (!score) {
//     score = {
//         win : 0,
//         loss : 0,
//         tie : 0
//     };
// }

document.querySelector('.winners').innerHTML = `Wins : ${score.win}`;
document.querySelector('.losses').innerHTML = `Losses : ${score.loss}`;
document.querySelector('.ties').innerHTML = `Ties : ${score.tie}`;


function pickComputerMove() {
    let computerMove = '';
    randomNumber = Math.random();

    if(randomNumber >= 0 && randomNumber < 1/3) {
        computerMove = 'Rock';
    } else if (randomNumber >= 1/3 && randomNumber < 2/3) {
        computerMove = 'Paper';
    } else if (randomNumber >=2/3 && randomNumber < 1) {
        computerMove = 'Scissor';
    }

    return computerMove;

}

function moveCha(computerMove, yourMove) {

    if (yourMove === 'Rock') {
        if (computerMove === 'Rock') {
            result = 'Tie';
            score.tie++;

            document.querySelector('.game-result').innerHTML = 'Its a Tie.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;

            document.querySelector('.ties').innerHTML = `Ties : ${score.tie}`;
        } else if(computerMove ==='Paper') {
            result = 'You Lose';
            score.loss++;

            document.querySelector('.game-result').innerHTML = 'You Loss.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.losses').innerHTML = `Losses : ${score.loss}`;
        } else {
            result = 'You win';
            score.win++;

            document.querySelector('.game-result').innerHTML = 'You Win.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.winners').innerHTML = `Wins : ${score.win}`;
        }

        localStorage.setItem('score', JSON.stringify(score));

        console.log(score);

//         alert(`You pick ${yourMove}.
// Computer pick ${botMove}.
// ${result}.
//             Win : ${score.win}        Loss : ${score.loss}        Tie : ${score.tie}`);
    } else if (yourMove === 'Paper') {
        if (botMove === 'Rock') {
            result = 'You Win';
            score.win++;

            document.querySelector('.game-result').innerHTML = 'You Win.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.winners').innerHTML = `Wins : ${score.win}`;
        } else if(botMove ==='Paper') {
            result = 'Tie';
            score.tie++;

            document.querySelector('.game-result').innerHTML = 'Its a Tie.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.ties').innerHTML = `Ties : ${score.tie}`;
        } else {
            result = 'You Lose';
            score.loss++;

            document.querySelector('.game-result').innerHTML = 'You Loss.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.losses').innerHTML = `Losses : ${score.loss}`;
        }

        localStorage.setItem('score', JSON.stringify(score));

        console.log(score);

//         alert(`You pick ${yourMove}.
// Computer pick ${botMove}.
// ${result}.
//             Win : ${score.win}        Loss : ${score.loss}        Tie : ${score.tie}`)
    } else if (yourMove === 'Scissor') {
        if (botMove === 'Rock') {
            result = 'You Lose';
            score.loss++;

            document.querySelector('.game-result').innerHTML = 'You Loss.';
            ddocument.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.losses').innerHTML = `Losses : ${score.loss}`;
        } else if(botMove ==='Paper') {
            result = 'You Win';
            score.win++;

            document.querySelector('.game-result').innerHTML = 'You Win.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.winners').innerHTML = `Wins : ${score.win}`;
        } else {
            result = 'Tie';
            score.tie++;

            document.querySelector('.game-result').innerHTML = 'Its a Tie.';
            document.querySelector('.referee-opinion').innerHTML = `(You) &nbsp;: &nbsp;<img src="imgs/${yourMove}.png"> &nbsp;&nbsp;&nbsp;vs &nbsp;&nbsp;&nbsp;(Bot) &nbsp;: &nbsp;<img src="imgs/${computerMove}.png">`;
            // document.querySelector('.referee-opinion').innerHTML = `You  :  ${yourMove}  --  Opponent  :  ${computerMove}`;

            document.querySelector('.ties').innerHTML = `Ties : ${score.tie}`;
        }

        localStorage.setItem('score', JSON.stringify(score));

        console.log(score);

//         alert(`You pick ${yourMove}.
// Computer pick ${botMove}.
// ${result}.
//             Win : ${score.win}        Loss : ${score.loss}        Tie : ${score.tie}`);
    } else {
        alert('Invalid Move');
    }

}

resetScoreBtn.addEventListener('click', function() {
    score.win = 0;
    score.loss = 0;
    score.tie = 0;

    localStorage.removeItem('score');
    console.log('Score Reset');
    console.log(score);

    document.querySelector('.game-result').innerHTML = '...';
    document.querySelector('.referee-opinion').innerHTML = '...';

    document.querySelector('.winners').innerHTML = `Wins : ${score.win}`;
    document.querySelector('.losses').innerHTML = `Losses : ${score.loss}`;
    document.querySelector('.ties').innerHTML = `Ties : ${score.tie}`;
}); 

rockBtn.addEventListener('click', function() {
    botMove = pickComputerMove();

    moveCha(botMove, 'Rock');
});

paperBtn.addEventListener('click', function() {
    botMove = pickComputerMove();

    moveCha(botMove, 'Paper');
});

scissorBtn.addEventListener('click', function() {
    botMove = pickComputerMove();

    moveCha(botMove, 'Scissor');
});