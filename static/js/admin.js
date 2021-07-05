async function get_user_tasks() {
  try {
    let response = await fetch("http://localhost:7000/admin_stats");
    let data = await response.json();
    return data;
  } catch (err) {
    console.log(err);
  }
}
get_user_tasks().then((data) => {
  console.log(data);
  const task_table = document.getElementById("admin-table-body");
  const table_row = document.createElement("tr");

  for (metrics in data) {
    const table_td = document.createElement("td");
    table_td.textContent = data[metrics];
    table_row.appendChild(table_td);
  }
  task_table.appendChild(table_row);
});
