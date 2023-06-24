async function getAuthors() {
  localStorage.setItem(
    "accessToken",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0OTI4YjY5ZGE0OGU5MzM4ZmEwNGRiZSIsImlzX2V4cG9ydCI6ZmFsc2UsImV4dXRob3JSb2xlcyI6WyJSRUFEIiwiV1JJVEUiXSwiaWF0IjoxNjg3NTU2MDYyLCJleHAiOjE2ODkzNTYwNjJ9.Z-w2WgzUdt7pZlHeiii2tPU13VbRMRLNQiujXb9Kfno"
  );
  const accessToken = localStorage.getItem("accessToken");

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
      console.log(author);
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

async function getDictionaries() {
  fetch("http://localhost:3000/dictionary", {
    method: "GET",
    headers: {
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
    .then((dict) => {
      console.log(dict);
      displayDictionary(dict.data);
    })
    .catch((error) => {
      console.log("Error", error);
    });
}

function displayDictionary(dict) {
  const listContainer = document.getElementById("dictionary-list");

  listContainer.innerHTML = "";
  dict.forEach((dict) => {
    const listItem = document.createElement("li");
    listItem.textContent = `${dict.term} - ${dict.letter}`;
    listContainer.appendChild(listItem);
  });
}

async function getTopics() {
  fetch("http://localhost:3000/description", {
    method: "GET",
    headers: {
      "Content-type": "application/json",
    },
    mode: "cors",
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        console.log("Request failed with status: ", +response.status);
      }
    })
    .then((topic) => {
      displayTopics(topic.data);
    })
    .catch((error) => {
      console.log("Error", error);
    });
}

function displayTopics(topic) {
  const listContainer = document.getElementById("topic-list");

  listContainer.innerHTML = "";
  topic.forEach((top) => {
    console.log(top);
    const listItem = document.createElement("li");
    listItem.textContent = `${top.description} - ${top.category_id.category_name}`;
    listContainer.appendChild(listItem);
  });
}
