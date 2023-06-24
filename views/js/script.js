async function getAuthors() {
  localStorage.setItem(
    "accessToken",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0OTI4YjY5ZGE0OGU5MzM4ZmEwNGRiZSIsImlzX2V4cG9ydCI6ZmFsc2UsImV4dXRob3JSb2xlcyI6WyJSRUFEIiwiV1JJVEUiXSwiaWF0IjoxNjg3NTU2MDYyLCJleHAiOjE2ODkzNTYwNjJ9.Z-w2WgzUdt7pZlHeiii2tPU13VbRMRLNQiujXb9Kfno"
  );
  const accessToken = localStorage.getItem("accessToken");
  console.log(accessToken);

  fetch("http://localhost:3000/author", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json",
    },
    mode: "cors",
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        console.log("Request failed with status: " + response.status);
      }
    })
    .then((author) => {
      console.log(author.data);
      displayAuthor(author.data);
    })
    .catch((error) => {
      console.error("Error", error);
    });
}

function displayAuthor(authors) {
  const listContainer = document.getElementById("author-list");

  listContainer.innerHTML = "";

  authors.forEach((author) => {
    const listItem = document.createElement("li");
    listItem.textContent = `${author.author_first_name} ${author.author_last_name} \
    - ${author.author_email}`;
    listContainer.appendChild(listItem);
  });
}
