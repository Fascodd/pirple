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

function create_task(obj) {
  const task_list_container = document.getElementById("user_task_container");
  const task_container = document.createElement("div");
  task_container.classList = "task-list-container";
  const task_div_container = document.createElement("div");
  const delete_div = createDeleteBtn();
  let obj_iterator = 0;
  for (item_data in obj) {
    createListItem(obj[item_data], task_container, obj_iterator, item_data);
    obj_iterator++;
  }

  task_container.appendChild(task_div_container);
  task_container.appendChild(delete_div);
  task_list_container.appendChild(task_container);
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

function createListItem(e, parentContainer, index, item_data) {
  const element_div = document.createElement("div");
  const element_p = document.createElement("p");
  element_p.textContent = e;
  element_div.appendChild(element_p);
  element_div.classList = `task-item task-width ${item_data}`;
  element_p.classList = "task-text";
  parentContainer.appendChild(element_div);
  index === 0
    ? (element_p.classList += " task-id")
    : element_p.addEventListener("focusin", (e) => {
        console.log(e);
        console.log("i am focused");
      });
}
