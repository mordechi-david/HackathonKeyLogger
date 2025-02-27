let userName = document.getElementById('user-name');
let password = document.getElementById('password');
let submit = document.getElementById('submit');

submit.addEventListener('click', function(event) {
    if (userName.value !== 'chaim' && password.value !== '1234') {
        alert('Invalid Username or Password');
        event.preventDefault();
    }
})
