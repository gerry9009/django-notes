// DJANGO dokumentáció alapján
// az itt megszerezett adatot szükséges elküldeni
// mikor fetch-elünk egy api adatot
// főleg a POST és DELETE methodusok esetében

/*
const init = {
      method: "POST",
      mode: "same-origin",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newNote),
    };
*/

// ezen felül még szükséges a SessionAuthentication
// használata a Django-nál -> settings.py
// https://gist.github.com/marteinn/3785ff3c1a3745ae955c
/*
# Django rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
    ]
}
*/

// továbbá a views.py-ban a parser_classes dekorátort is be kell importálni, és a JSONParser-t is
/*
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
*/

// majd ezt a dekorátort használni kell a POST és DELETE metódussal érintett függvényeknél
// @parser_classes([JSONParser])

// https://medium.com/@munyaokelvin/how-to-fetch-data-from-an-ajax-fetch-api-in-django-e825a329a36d

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export default getCookie;
