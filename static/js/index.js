window.addEventListener("click", (e) => {
  const delete_btn = Array.from(
    document.querySelectorAll(".delete_btn_container")
  );

  if (delete_btn.includes(e.target)) {
    const task_id =
      e.target.parentElement.querySelectorAll(".task-id")[0].innerText;
    deleteListItem(task_id);
  }
});

async function deleteListItem(task_id) {
  try {
    const url = "http://localhost:7000/delete_task";
    const response = await fetch(url, {
      method: "DELETE",
      mode: "cors",
      credentials: "same-origin",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(task_id),
    });

    const header = await response;
    window.location.replace("http://localhost:7000/");
  } catch (err) {
    console.log(err);
  }
}
