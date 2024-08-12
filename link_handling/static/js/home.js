const baseURL = "http://127.0.0.1:5000/api/url";

const YOUR_ACCESS_TOKEN = window.localStorage.getItem("authToken") || "";
const YOUR_USERNAME = (document.getElementById("logged_one").innerHTML =
  window.localStorage.getItem("username")
    ? window.localStorage.getItem("username")
    : "");

function apple() {
  inputURL = document.getElementById("inputData").value;
  username = YOUR_USERNAME;
  fetch(baseURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json", // Specify content type as JSON
      Authorization: `Bearer ${YOUR_ACCESS_TOKEN}`, // Optional: include an authorization header if needed
    },
    body: JSON.stringify({ inputURL, username }),
  })
    .then((response) => {
      if (!response.ok) {
        // Handle errors, e.g., 4xx or 5xx status codes
        throw new Error("Network response was not ok");
      }
      return response.json(); // Parse the JSON response
    })
    .then(({ data }) => {
      console.log(data);
      // Handle the data received from the server
      document.getElementById("inputData").value = "";
      document.getElementById("generated_url").innerHTML = data.shortURL;
      document.getElementById("generated_url").href = data.shortURL;
      document.getElementById("copyButton").hidden = false;
    })
    .catch((error) => {
      // Handle any errors that occurred during the fetch
      console.error("Error:", error);
    });
}

document.getElementById("url-form").addEventListener("submit", function (e) {
  e.preventDefault();
  apple();
});

document.getElementById("copyButton").addEventListener("click", () => {
  const textToCopy = document.getElementById("generated_url").textContent;

  // Use the Clipboard API to copy the text
  navigator.clipboard
    .writeText(textToCopy)
    .then(() => {
      // Success feedback
      alert("Text copied to clipboard!");
    })
    .catch((err) => {
      // Error handling
      console.error("Failed to copy text: ", err);
    });
});

function logout_call() {
  window.localStorage.clear();
  window.location.href = "/auth";
}

window.onload = function () {
  if (!localStorage.getItem("loggedIn") && !localStorage.getItem("authToken")) {
    window.location.href = "/auth";
  }
};
