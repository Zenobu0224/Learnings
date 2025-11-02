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

    for(let i = 0; i < tasks.length; i++) {

        const taskDiv = document.createElement('div');
        taskDiv.classList.add('task-added');

        const taskP = document.createElement('p');
        taskP.textContent = tasks[i];

        const delTaskBtn = document.createElement('button');
        delTaskBtn.textContent = 'X';

        delTaskBtn.addEventListener('click', function() {

            tasks.splice(i, 1);
            displayTask(tasks);

        });

        taskDiv.appendChild(taskP);
        taskDiv.appendChild(delTaskBtn);
        taskContainer.appendChild(taskDiv);

    }

}


addBtn.addEventListener('click', function() {

    const task = document.getElementById('text').value;

    addTask(task);
    displayTask(tasks);

});


displayTask(tasks);