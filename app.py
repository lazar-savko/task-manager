from flask import Flask, render_template, request, redirect, url_for
from storage import JsonStorage
from util import get_picture

app = Flask(__name__)

my_storage = JsonStorage('data/tasks.json')

@app.route("/")
def homepage():
    tasks = my_storage.load_tasks()
    return render_template("template.html", tasks=tasks)


@app.route("/add", methods=['POST'])
def add():
    tasks = my_storage.load_tasks()
    new_task_text = request.form['task']
    picture = get_picture(new_task_text)
    tasks.append({
        'task': new_task_text,
        'completed': False,
        'image': picture
    })
    my_storage.sync_tasks(tasks)
    return render_template("template.html", tasks=tasks)

@app.route("/complete", methods=['POST'])
def complete():
    tasks = my_storage.load_tasks()

    task_number = int(request.form['task_index'])
    task = tasks[task_number]
    task["completed"] = True

    my_storage.sync_tasks(tasks)
    return render_template("template.html", tasks=tasks)

@app.route("/delete", methods=['POST'])
def delete():
    tasks = my_storage.load_tasks()
    index_to_delete = request.form['task_index']
    tasks.pop(int(index_to_delete))
    my_storage.sync_tasks(tasks)
    return render_template("template.html", tasks=tasks)


@app.route("/edit/<task_index>", methods=['GET'])
def edit(task_index):
    tasks = my_storage.load_tasks()
    task = tasks[int(task_index)]
    return render_template("edit-template.html", task_index=task_index, task=task['task'])

if __name__ == "__main__":
    app.run(debug=True)
