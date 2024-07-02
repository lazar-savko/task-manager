from flask import Flask, render_template, request, redirect, url_for
from storage import JsonStorage
from util.util_package import get_picture

app = Flask(__name__)

my_storage = JsonStorage('data/tasks.json')

@app.route("/")
def homepage():
    tasks = my_storage.load_tasks()
    for task in tasks:
        task['image'] = get_picture(task['task'])
    return render_template("template.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
