async function loadComputers() {
    try{
        let response = await fetch('http://localhost:5000/api/get_target_machines_list');
        let computers = await response.json();
        console.log(computers.machines);
        
        let mainDiv = document.getElementById('computers');
        
        computers.machines.forEach(computer => {
            let computerDiv = document.createElement('div');
            let computerName = document.createElement('h2');
            computerName.innerText = `${computer}`;
            computerDiv.appendChild(computerName);
            mainDiv.appendChild(computerDiv);
        });
    }catch(err){
        console.log(err);
    }
}

loadComputers();