const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginForm.style.border = '2px solid #ccc';
loginForm.style.padding = '20px';
loginButton.style.backgroundColor = '#007bff';
loginButton.style.border = 'none';
loginButton.style.borderRadius = '5px';
loginButton.style.color = '#fff';
loginButton.style.cursor = 'pointer';
loginButton.style.padding = '10px';
loginButton.style.marginTop = '10px';


function isValidUsername(username) {

	if(username.length < 5) {

	console.log("Username is valid");

	}
	else {

	console.log("Invalid Username");

	}

}

function isValidPassword(password) {

	if(password.length < 7) {

        console.log("Password is valid");

        }
        else {

        console.log("Invalid Password");

        }

}

function showErrorMessage(element, message) {
  const error = element.parentElement.querySelector('.error');
  error.textContent = message;
  error.style.display = 'block';
}

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "siemDev" && password === "california") {
        window.location.href = "/dev1243224123123/devNotes37370.txt";
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})

