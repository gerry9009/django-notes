import renderNoteWindow from "./modalNote.js";
import postData from "./utils/postData.js";

const $addNoteForms = document.querySelectorAll(".js-add-note");
const $addGroupForm = document.querySelector(".js-add-group");
const $groupsContainer = document.querySelector(".js-groups-container");
const $notes = document.querySelectorAll(".js-notes");

const localUrl = "http://127.0.0.1:8000";

const svg = `<svg stroke-width="1.5" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M21 3L15 3M21 3L12 12M21 3V9" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"/> <path d="M21 13V19C21 20.1046 20.1046 21 19 21H5C3.89543 21 3 20.1046 3 19V5C3 3.89543 3.89543 3 5 3H11" stroke="currentColor" stroke-linecap="round"/> </svg>`;

// group elemek kezelése
const createGroup = (group, url) => {
  const divElement = document.createElement("div");
  divElement.classList = "group";
  divElement.innerHTML = `
          <h2 class="group-title">${group.name}</h2>
          <a href="${url}/delete/group/${group.id}" class="group-delete">Delete Group</a>
          <div id="${group.id}" class="notes-container">
          </div>
      `;

  // add-note form hozzáadása
  const form = document.createElement("form");
  form.classList = "js-add-note add-note";
  form.innerHTML = `
            <input data-group="${group.id}" type="text" placeholder="Add new note..." class="add-note-input">
            <button type="submit" class="add-note-btn">+</button>
        `;

  form.addEventListener("submit", (e) => handleNoteFormSubmit(e));

  divElement.appendChild(form);

  return divElement;
};

const renderGroup = (group) => {
  const newGroup = createGroup(group, localUrl);

  $groupsContainer.insertBefore(newGroup, $addGroupForm);
};

const handleGroupFormSubmit = (event) => {
  event.preventDefault();

  const newGroup = {
    name: event.target[0].value,
  };

  const url = `${localUrl}/api/groups/create/`;

  postData(url, newGroup, renderGroup);

  event.target[0].value = "";
};

// NOTE elemek kezelése
const createNote = (note) => {
  const noteElement = document.createElement("div");
  noteElement.classList = "note js-notes";
  noteElement.draggable = true;

  noteElement.dataset.noteId = note.id;

  const anchor = document.createElement("a");
  anchor.href = `${localUrl}/notes/${note.id}`;
  anchor.innerHTML = `${svg}`;
  anchor.classList = "js-note-anchor note-anchor";

  const noteTop = document.createElement("div");
  noteTop.classList = "note-bottom";
  noteTop.appendChild(anchor);

  noteElement.innerHTML += `
        <div class="note-top">
            <h3 data-note-id=${note.id}>${note.title}</h3>
        </div>
  `;

  noteElement.appendChild(noteTop);

  noteElement.addEventListener("click", (e) => handleClickNote(e));

  return noteElement;
};

const renderNewNote = (note) => {
  const container = document.getElementById(`${note.group}`);
  const noteElement = createNote(note);

  container.appendChild(noteElement);
};

const handleNoteFormSubmit = (event) => {
  event.preventDefault();

  if (event.target[0].value) {
    const newNote = {
      title: event.target[0].value,
      group: event.target[0].dataset.group,
    };

    const url = `${localUrl}/api/notes/create/`;

    postData(url, newNote, renderNewNote);

    event.target[0].value = "";
  }
};

const handleClickNote = (e) => {
  const noteId = e.target.dataset["noteId"];

  fetch(`${localUrl}/api/notes/${noteId}/`)
    .then((resp) => resp.json())
    .then((data) => renderNoteWindow(data, localUrl));
};

$notes.forEach((note) => {
  note.addEventListener("click", (e) => handleClickNote(e));
});

// az összes renderelt csoportban lévő new note formnak hozzáadja az eseményfigyelőt
$addNoteForms.forEach((note) => {
  note.addEventListener("submit", (e) => handleNoteFormSubmit(e));
});

// az add group form-nak hozzáadja az eseményfigyelőt
$addGroupForm.addEventListener("submit", (e) => handleGroupFormSubmit(e));
