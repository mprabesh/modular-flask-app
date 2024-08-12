const baseURL = "http://127.0.0.1:5000/api/users";

async function loginAPICall(credentials) {
  const response = await fetch(`http://127.0.0.1:5000/api/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });
  const data = await response.json();
  return data;
}

async function apple() {
  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  let errorText = document.getElementById("error-text");
  if (username && password) {
    console.log("prabesh");
    const loginResponse = await loginAPICall({ username, password });
    if (loginResponse.status === "success") {
      errorText.hidden = true;
      localStorage.setItem("loggedIn", "true");
      localStorage.setItem("username", loginResponse.data.userid);
      localStorage.setItem("authToken", loginResponse.data.token);
      window.location.href = "/urlshort";
    }
    if (loginResponse.status === "fail") {
      document.getElementById("password").value = "";
      document.getElementById("username").value = "";
      errorText.hidden = false;
    }
  } else {
    errorText.hidden = false;
  }
}

document
  .getElementById("go-to-register")
  .addEventListener("click", function () {
    window.location.href = "/auth/register"; // Replace with your target URL
  });

window.onload = function () {
  if (localStorage.getItem("loggedIn") === "true") {
    window.location.href = "/urlshort"; // Redirect if already logged in
  }
};
