let computers = [{
    name: 'Dell',
},
{
    name: 'HP',
},
{
    name: 'Lenovo',
}
]
let mainDiv = document.getElementById('comuters');
computers.forEach(computer => {
    let computerDiv = document.createElement('div');
    let computerName = document.createElement('h2');
    computerName.innerText = `Computer Name: ${computer.name}`;
    computerDiv.appendChild(computerName);
    mainDiv.appendChild(computerDiv);
});