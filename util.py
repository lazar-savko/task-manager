import json
import requests


def get_picture(query):
  url = f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id=cmUu9QzXb_UGyMEsdfg33hzLnJXA2JrthRgVJ3Ea5Ww"
  response = requests.get(url)
  img_url = response.json()['results'][0]['urls']['thumb']
  return img_url


class JsonStorage:
  def __init__(self, file_path):
    self.file_path = file_path

  def load_tasks(self):
    with open(self.file_path, 'r') as tasks_file:
      tasks_string = tasks_file.read()
      return json.loads(tasks_string)


  def sync_tasks(self, tasks):
    updated_tasks_string = json.dumps(tasks)
    with open(self.file_path, 'w') as tasks_file:
      tasks_file.write(updated_tasks_string)

my_json_storage = JsonStorage('tasks.json')


class TaskApp:
  def __init__(self, storage):
    self.storage = storage
  def generate_html(self):
    tasks = self.storage.load_tasks()
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


  def show_tasks(self):
    tasks = self.storage.load_tasks()
    print()
    for index, task in enumerate(tasks):
      if task["completed"] == True:
        print(f'{index}. {task["task"].upper()} ✓')
      else:
        print(f'{index}. {task["task"].upper()} ☐')
    print()


  def add_task(self):
    tasks = self.storage.load_tasks()
    user_added_task = input("Please insert a new task: ")
    tasks.append({"task": user_added_task, "completed": False})

    print('You have added a task')
    print()
    my_json_storage.sync_tasks(tasks)
    self.show_tasks()


  def complete_task(self):
    tasks = self.storage.load_tasks()
    while True:
      task_number = int(input('Which task do you want to complete: '))
      if 0 <= task_number < (len(tasks)):
        task = tasks[task_number]
        task["completed"] = True
        break
      else:
        print(f"Please select a task from 0 to {len(tasks) - 1}.")
    my_json_storage.sync_tasks(tasks)
    self.show_tasks()


  def delete_task(self):
    tasks = self.storage.load_tasks()
    print('You have chosen to delete a task')

    while True:
      task_number = int(input('Which task do you want to delete: '))
      if 0 <= task_number < (len(tasks)):
        del tasks[task_number]
        print('Task deleted successfully.')
        break
      else:
        print(f"Please select a task from 0 to {len(tasks) - 1}.")
    my_json_storage.sync_tasks(tasks)
    self.show_tasks()

  def show_setup(self):

    print(
      'Oh, you have tasks to do? Good, you’re at the right place to procrastinate!'
    )
    tasks = self.storage.load_tasks()
    self.show_tasks()
    print()
    print('--------------------------------------')
    print()

    print("1. Add task: ")
    print("2. Complete task: ")
    print("3. Delete task: ")
    print("4. Update task: ")
    print("5. Generate HTML: ")
    print()
    user_choice = input("What do you want to do: ")
    if user_choice == "1":
      self.add_task()
    elif user_choice == "2":
      self.complete_task()
    elif user_choice == "3":
      self.delete_task()
    elif user_choice == "4":
      self.update_task()
    elif user_choice == "5":
      self.generate_html()
    print()
    input("Press Enter to continue...")

    while True:
      print()
      user_choice = input('Do you want to select another option (Y/N)?')
      if user_choice == 'Y' or user_choice == 'y':
        print("1. Add task: ")
        print("2. Complete task: ")
        print("3. Delete task: ")
        print("4. Update task: ")
        print("5. Generate HTML: ")
        user_choice = input("What do you want to do: ")
        if user_choice == "1":
          self.add_task()
        elif user_choice == "2":
          self.complete_task()
        elif user_choice == "3":
          self.delete_task()
        elif user_choice == "4":
          self.update_task()
        elif user_choice == "5":
          self.generate_html()
      elif user_choice == 'N' or user_choice == 'n':
        break
      else:
        print('Select Y for Yes or, N for No')


  def update_task(self):
    tasks = self.storage.load_tasks()
    task_number = int(input('Which task do you want to update: '))
    new_task_name = input('Enter the new name for the task: ')
    tasks[task_number]["task"] = new_task_name
    print('Task updated successfully.')
    my_json_storage.sync_tasks(tasks)
    self.show_tasks()

