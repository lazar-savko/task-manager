from util import *


def show_setup():
  print(
      'Oh, you have tasks to do? Good, you’re at the right place to procrastinate!'
  )

  show_tasks(tasks)
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
    add_task()
  elif user_choice == "2":
    complete_task()
  elif user_choice == "3":
    delete_task()
  elif user_choice == "4":
    update_task()
  elif user_choice == "5":
    generate_html(tasks)
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
        add_task()
      elif user_choice == "2":
        complete_task()
      elif user_choice == "3":
        delete_task()
      elif user_choice == "4":
        update_task()
      elif user_choice == "5":
        generate_html(tasks)
    elif user_choice == 'N' or user_choice == 'n':
      break
    else:
      print('Select Y for Yes or, N for No')


def main():
  show_setup()


if __name__ == "__main__":
  main()
