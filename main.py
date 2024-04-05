from datetime import datetime, timedelta

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file.readlines():
                    task_data = line.strip().split(',')
                    task_name = task_data[0]
                    task_deadline = datetime.strptime(task_data[1], "%Y-%m-%d")
                    self.tasks.append((task_name, task_deadline))
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task, deadline in self.tasks:
                file.write(f"{task},{deadline.strftime('%Y-%m-%d')}\n")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, (task, deadline) in enumerate(self.tasks, start=1):
                print(f"{idx}. {task} (Due: {deadline.strftime('%Y-%m-%d')})")

    def add_task(self, new_task, deadline):
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            self.tasks.append((new_task, deadline_date))
            self.save_tasks()
            print(f"Task '{new_task}' added with deadline {deadline}.")
        except ValueError:
            print("Invalid deadline format. Please use YYYY-MM-DD.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{removed_task[0]}' removed.")
        else:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{completed_task[0]}' marked as completed.")
        else:
            print("Invalid task index.")

    def check_deadlines(self):
        today = datetime.now().date()
        overdue_tasks = [(task, deadline) for task, deadline in self.tasks if deadline.date() < today]
        if overdue_tasks:
            print("Overdue Tasks:")
            for task, deadline in overdue_tasks:
                print(f"{task} (Due: {deadline.strftime('%Y-%m-%d')})")
        else:
            print("No overdue tasks.")

def main():
    todo = ToDoList()
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Check Overdue Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            todo.display_tasks()
        elif choice == "2":
            new_task = input("Enter the new task: ")
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            todo.add_task(new_task, deadline)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            todo.remove_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo.mark_completed(task_index)
        elif choice == "5":
            todo.check_deadlines()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
