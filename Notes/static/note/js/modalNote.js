import postData from "./utils/postData.js";

const svgClose = `<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="16" height="16" viewBox="0 0 30 30">
<path d="M 7 4 C 6.744125 4 6.4879687 4.0974687 6.2929688 4.2929688 L 4.2929688 6.2929688 C 3.9019687 6.6839688 3.9019687 7.3170313 4.2929688 7.7070312 L 11.585938 15 L 4.2929688 22.292969 C 3.9019687 22.683969 3.9019687 23.317031 4.2929688 23.707031 L 6.2929688 25.707031 C 6.6839688 26.098031 7.3170313 26.098031 7.7070312 25.707031 L 15 18.414062 L 22.292969 25.707031 C 22.682969 26.098031 23.317031 26.098031 23.707031 25.707031 L 25.707031 23.707031 C 26.098031 23.316031 26.098031 22.682969 25.707031 22.292969 L 18.414062 15 L 25.707031 7.7070312 C 26.098031 7.3170312 26.098031 6.6829688 25.707031 6.2929688 L 23.707031 4.2929688 C 23.316031 3.9019687 22.682969 3.9019687 22.292969 4.2929688 L 15 11.585938 L 7.7070312 4.2929688 C 7.5115312 4.0974687 7.255875 4 7 4 z"></path>
</svg>`;

// módosított note frissítése a group-ban
const renderNewNote = (newNote) => {
  const note = document.querySelectorAll(`[data-note-id="${newNote.id}"]`);

  note[1].innerText = `${newNote.title}`;
};

const renderNoteWindow = (note, url) => {
  const body = document.querySelector("body");

  const modalWindow = document.createElement("div");
  modalWindow.classList = "modal-window";

  const form = document.createElement("form");
  form.classList = "modal-form note-form";
  form.innerHTML = `
      <a href="${url}/notes/${
    note.id
  }" class="note-anchor">Modify containing group</a>
      <input required type="text" value="${
        note.title
      }" placeholder="Add title..." class="note-form-input">
      <textarea placeholder="Add text..." class="note-form-input note-form-input_text">${
        note.text ? note.text : ""
      }</textarea>
      <div class="note-btn-container">
          <a href="${url}/notes/delete/${
    note.id
  }" class="note-anchor note-anchor_delete">Delete note</a>
          <button type="submit" class="note-form-btn">Save</button>
      </div>
    `;

  const exitBtn = document.createElement("div");
  exitBtn.classList = "modal-exit note-form-btn";
  exitBtn.innerHTML = svgClose;

  form.appendChild(exitBtn);
  modalWindow.appendChild(form);

  // eseményfigyelő a form-ra -> update az elem, ha kell akkor a DOM-ban is
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const title = e.target[0].value;
    const text = e.target[1].value;

    const newNote = { ...note, title, text };
    const updateUrl = `${url}/api/notes/update/${note.id}/`;
    postData(updateUrl, newNote, renderNewNote);

    modalWindow.remove();
  });
  // eseményfigyelő a modal window bezárásához is
  modalWindow.addEventListener("click", (event) => {
    if (modalWindow === event.target) modalWindow.remove();
  });

  exitBtn.addEventListener("click", () => {
    modalWindow.remove();
  });

  body.appendChild(modalWindow);
};

export default renderNoteWindow;
