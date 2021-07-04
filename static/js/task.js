async function get_task() {
    try {
        let href = window.location.href;
        let response = await fetch(`${href}/edit`);
        let data = await response.json();

        return data;
    } catch (err) {
        console.log(err);
    }
}

get_task().then((data) => {
    task_data = data[0]
    const task_obj = {}
    task_obj.task_name = task_data[1]
    task_obj.task_start_date = task_data[2]
    task_obj.task_end_date = task_data[3]
    let inputs = Array.from(document.getElementsByTagName('input'))
    for (input in inputs) {
        const current_input = inputs[input]
        const current_key = Object.keys(task_obj)[input]
        current_input.value = task_obj[current_key]
    }
})


