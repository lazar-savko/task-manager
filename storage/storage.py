import json


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


