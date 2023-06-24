function getTokenExpiration(token) {
  const decodedToken = JSON.parse(atob(token.split(".")[1]));
  if (decodedToken && decodedToken.exp) {
    return new Date(decodedToken.exp * 1000); // Convert expiration time from seconds to milliseconds
  }
  return null;
}

function getTokenFromCookie(cookieName) {
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(`${cookieName}=`)) {
      return cookie.substring(cookieName.length + 1);
    }
  }
  return null;
}

/////AUTHOR
async function getAuthors() {
  const loginUrl = "/new/login";

  let accessToken = localStorage.getItem("accessToken");
  console.log(accessToken);
  const accessTokenExpTime = getTokenExpiration(accessToken);
  console.log("accessTokenExpTime:", accessTokenExpTime);

  if (accessTokenExpTime) {
    const currentTime = new Date();
    if (currentTime < accessTokenExpTime) {
      console.log("Access token is still valid.");
    } else {
      console.log("Access token has expired.");
      const refreshToken = getTokenFromCookie("refreshToken");
      console.log("refreshToken:", refreshToken);
      const refreshTokenExpTime = getTokenExpiration(refreshToken);
      console.log("refreshTokenExpTime: ", refreshTokenExpTime);
      if (refreshTokenExpTime) {
        const currentTime = new Date();
        if (currentTime < refreshTokenExpTime) {
          console.log("Refresh token is still valid.");
          accessToken = await authorRefreshTokenFunc(refreshToken);
          console.log("NewAccessToken:", accessToken);
        } else {
          console.log("Refresh token has expired.");
          return window.location.replace(loginUrl);
        }
      } else {
        console.log("Invalid access token format.");
      }
    }
  } else {
    console.log("Invalid access token format.");
  }

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

async function authorRefreshTokenFunc() {
  return fetch("http://localhost:3000/author/refresh", {
    method: "POST",
    credentials: "include",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (response.ok) {
        console.log("Refreshed successful");
        return response.json();
      } else {
        console.error("Refreshing failed");
      }
    })
    .then((tokens) => {
      console.log(tokens.accessToken);
      localStorage.setItem("accessToken", tokens.accessToken);
      return tokens.accessToken;
    })
    .catch((error) => {
      console.error("Error:", error);
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


/////Dictionary
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
