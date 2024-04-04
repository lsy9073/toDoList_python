class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{new_task}' added.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] += " (Completed)"
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")


def main():
    todo = ToDoList()
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo.display_tasks()
        elif choice == "2":
            new_task = input("Enter the new task: ")
            todo.add_task(new_task)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            todo.remove_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo.mark_completed(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()