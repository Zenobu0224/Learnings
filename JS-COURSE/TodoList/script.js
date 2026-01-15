const tasks = ['learn html', 'learn css'];

const addBtn = document.querySelector('.add-task');
const taskContainer = document.querySelector('.task-container');


function addTask(task) {

    if(task) {

        tasks.push(task);
        document.getElementById('text').value = '';
        console.log(tasks);

    } else {
        alert('Please Enter A Task!');
        console.log('Please Enter A Task!');
    }
 
}

function displayTask(tasks) {
    taskContainer.innerHTML = '';

    tasks.forEach((task, index) => {

        const taskDiv = document.createElement('div');
        taskDiv.classList.add('task-added');

        const taskP = document.createElement('p');
        taskP.textContent = task;

        const delTaskBtn = document.createElement('button');
        delTaskBtn.textContent = 'X';

        delTaskBtn.addEventListener('click', () => {

            tasks.splice(index, 1);
            displayTask(tasks);

        });

        taskDiv.appendChild(taskP);
        taskDiv.appendChild(delTaskBtn);
        taskContainer.appendChild(taskDiv);

    });

}


addBtn.addEventListener('click', function() {
    const task = document.getElementById('text').value;

    addTask(task);
    displayTask(tasks);

});

document.body.addEventListener('keydown', (event) => {
    const task = document.getElementById('text').value;

    if(event.key === 'Enter') {
        addTask(task);
        displayTask(tasks);
    }

});


displayTask(tasks);