import json
import requests


def load_tasks():
  with open('tasks.json', 'r') as tasks_file:
    tasks_string = tasks_file.read()
    return json.loads(tasks_string)


def sync_tasks():
  updated_tasks_string = json.dumps(tasks)
  with open('tasks.json', 'w') as tasks_file:
    tasks_file.write(updated_tasks_string)


tasks = load_tasks()


def generate_html(tasks):
  with open('template.html', 'r') as file:
    html_content = file.read()

  output = ""

  for task in tasks:
    if task['completed']:
      output += f'<li class="checked"><img src="{get_picture(task["task"].lower())}"/>{task["task"].upper()}</li>'
    else:
      output += f'<li><img src="{get_picture(task["task"].lower())}"/>{task["task"].upper()}</li>'

  updated_html_content = html_content.replace('__SWAP_HERE__', output)

  with open('tasks.html', 'w') as file:
    file.write(updated_html_content)

  print("This HTML file was generated successfully")


def show_tasks(tasks):
  print()
  for index, task in enumerate(tasks):
    if task["completed"] == True:
      print(f'{index}. {task["task"].upper()} ✓')
    else:
      print(f'{index}. {task["task"].upper()} ☐')
  print()


def add_task():
  user_added_task = input("Please insert a new task: ")
  tasks.append({"task": user_added_task, "completed": False})

  print('You have added a task')
  print()
  sync_tasks()
  show_tasks(tasks)


def complete_task():
  while True:
    task_number = int(input('Which task do you want to complete: '))
    if 0 <= task_number < (len(tasks)):
      task = tasks[task_number]
      task["completed"] = True
      break
    else:
      print(f"Please select a task from 0 to {len(tasks) - 1}.")
  sync_tasks()
  show_tasks(tasks)


def delete_task():
  print('You have chosen to delete a task')

  while True:
    task_number = int(input('Which task do you want to delete: '))
    if 0 <= task_number < (len(tasks)):
      del tasks[task_number]
      print('Task deleted successfully.')
      break
    else:
      print(f"Please select a task from 0 to {len(tasks) - 1}.")
  sync_tasks()
  show_tasks(tasks)


def update_task():
  task_number = int(input('Which task do you want to update: '))
  new_task_name = input('Enter the new name for the task: ')
  tasks[task_number]["task"] = new_task_name
  print('Task updated successfully.')
  sync_tasks()
  show_tasks(tasks)

def get_picture(query):
    url = f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id=cmUu9QzXb_UGyMEsdfg33hzLnJXA2JrthRgVJ3Ea5Ww"
    response = requests.get(url)
    img_url = response.json()['results'][0]['urls']['thumb']
    return img_url
