async function get_user_tasks() {
  try {
    let response = await fetch("http://localhost:7000/tasks");
    let data = await response.json();
    return data;
  } catch (err) {
    console.log(err);
  }
}

let g_user_task_data;
let user_id;
get_user_tasks().then((data) => {
  const user_task_data = data.map((e) => {
    const obj = {};
    obj.id = e[0];
    obj.task_name = e[1];
    obj.task_start_date = e[2];
    obj.task_due_date = e[3];
    return obj;
  });

  for (list_data in user_task_data) {
    create_task(user_task_data[list_data]);
  }
  g_user_task_data = user_task_data;
});

function create_task(task_obj) {
  const task_table = document.getElementById("task-list")
  const task_row = document.createElement("tr")
  for (task_data in task_obj) {
    createListItem(task_row, task_obj[task_data])
  }
  const edit_link = createEditLink(task_obj['id'])
  task_row.appendChild(edit_link)


  task_table.appendChild(task_row)
}

function createDeleteBtn() {
  const delete_div = document.createElement("div");
  const delete_button = document.createElement("a");
  delete_button.classList = "delete_btn";
  delete_div.classList = "delete_btn_container";
  delete_button.innerText = "X";
  delete_div.appendChild(delete_button);

  return delete_div;
}

function createListItem(task_row, task_data) {
  const task_td = document.createElement("td");
  task_td.textContent = task_data
  task_row.appendChild(task_td)
}

function createEditLink(task_id) {
  const task_td = document.createElement("td")
  const edit_link = document.createElement("a")
  edit_link.href = `http://localhost:7000/edit_task/${task_id}`
  edit_link.innerHTML = "Edit"
  task_td.appendChild(edit_link)
  return task_td

}


