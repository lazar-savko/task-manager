from flask import Flask, render_template, request, redirect, url_for
from storage import JsonStorage

app = Flask(__name__)

my_storage = JsonStorage('data/tasks.json')

@app.route("/")
def homepage():
    tasks = my_storage.load_tasks()
    return render_template("template.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)
