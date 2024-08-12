const baseURL = "http://127.0.0.1:5000/api/users";

async function registerAPICall(credentials) {
  const response = await fetch(`${baseURL}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });
  const data = await response.json();
  return data;
}

async function registerUser() {
  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  let email = document.getElementById("email").value;
  let errorText = document.getElementById("error-text");
  if (username && password && email) {
    const registerResponse = await registerAPICall({
      username,
      password,
      email,
    });
    console.log(registerResponse);
    if (registerResponse.status === "success") {
      window.location.href = "/auth";
    }
    if (registerResponse.status === "fail") {
      document.getElementById("password").value = "";
      document.getElementById("username").value = "";
      errorText.innerHTML = registerResponse.data.message;
    }
  } else {
    errorText.hidden = false;
  }
}

window.onload = function () {
  if (localStorage.getItem("loggedIn") === "true") {
    window.location.href = "/urlshort"; // Redirect if already logged in
  }
};
