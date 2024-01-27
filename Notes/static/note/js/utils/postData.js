import getCookie from "./getToken.js";

// url
// data - POST method-hoz tartozó adat
// callback - kezünkbe kerül a szerver által visszaküldött adatok
const postData = (url, data, callback) => {
  const init = {
    method: "POST",
    mode: "same-origin",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  fetch(url, init)
    .then((resp) => resp.json())
    .then((data) => {
      callback(data);
    });
};

export default postData;
