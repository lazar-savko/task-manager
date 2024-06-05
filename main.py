from util.util_package import TaskApp
from storage.storage import JsonStorage


def main():
  my_storage = JsonStorage('tasks.json')
  my_task_app = TaskApp(my_storage)

  my_task_app.show_setup()


if __name__ == "__main__":
  main()
