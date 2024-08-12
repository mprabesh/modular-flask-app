const baseURL = "http://127.0.0.1:5000/api/url/";

const YOUR_ACCESS_TOKEN = window.localStorage.getItem("authToken") || "";
const YOUR_USERNAME = window.localStorage.getItem("username");
// const YOUR_USERNAME = "punit";

function populate_table() {
  const tableBody = document.querySelector("#user-data-table tbody");
  const info = document.querySelector("#no-info-data");
  fetch(`${baseURL}${YOUR_USERNAME}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${YOUR_ACCESS_TOKEN}`,
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not OK");
      }
      return response.json(); // Parse the JSON data
    })
    .then(({ data }) => {
      console.log(data.length);
      if (data.length === 0) {
        const table_data = document.querySelector("#user-data-table");
        table_data.style.display = "none";
      } else {
        info.style.display = "none";
        data.forEach((link) => {
          const row = document.createElement("tr");

          const idCell = document.createElement("td");
          idCell.textContent = link.id;
          row.appendChild(idCell);

          const originalLinkCell = document.createElement("td");
          originalLinkCell.textContent = link.original_url;
          originalLinkCell.classList.add("originalLinkCol");
          row.appendChild(originalLinkCell);

          const shortLinkCell = document.createElement("td");
          shortLinkCell.textContent = link.short_link;
          row.appendChild(shortLinkCell);

          const buttonsSection = document.createElement("td");
          buttonsSection.textContent = "delete";
          buttonsSection.classList.add("link-remove");
          buttonsSection.addEventListener("click", function () {
            delete_link(link.id);
            window.location.reload();
          });
          row.appendChild(buttonsSection);

          tableBody.appendChild(row);
        });
      }
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("logged_one").innerHTML = window.localStorage.getItem(
    "username"
  )
    ? window.localStorage.getItem("username")
    : "";
  populate_table();
});

function logout_call() {
  window.localStorage.clear();
  window.location.href = "/auth";
}

function delete_link(id) {
  fetch(`${baseURL}${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${YOUR_ACCESS_TOKEN}`, // Replace with your actual token if needed
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not OK");
      }
      return response.json(); // Or response.text() if the response doesn't include JSON
    })
    .then((data) => {
      console.log("Item deleted successfully:", data);
      // Add your logic here to remove the item from the DOM, e.g., removing a table row
    })
    .catch((error) => {
      console.error("Error deleting item:", error);
    });
}

window.onload = function () {
  if (!localStorage.getItem("loggedIn") && !localStorage.getItem("authToken")) {
    window.location.href = "/auth";
  }
};
