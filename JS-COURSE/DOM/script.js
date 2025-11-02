const subscribeBtn = document.querySelector('.subs');
const calculateBtn = document.querySelector('.calculate');



subscribeBtn.addEventListener('click', function() {

    subscribeBtn.classList.toggle('is-subscribe');
    
    if(subscribeBtn.innerText === 'Subscribe') {
        subscribeBtn.innerText = 'Subscribed';

        // subscribeBtn.classList.add('is-subscribe');

    } else {
        subscribeBtn.innerText = 'Subscribe';
    }

});

calculateBtn.addEventListener('click', function() {
    const placeHolder = document.getElementById('text').value;
    const placeHolderInt = parseInt(placeHolder);

    if(placeHolderInt <= 30) {
        document.getElementById('calculate-result').innerHTML = `$${placeHolderInt + 10}`;
    } else {
        document.getElementById('calculate-result').innerHTML = `$${placeHolderInt}`;
    }

});