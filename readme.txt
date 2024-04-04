Explanation:
class ToDoList: Defines a class named ToDoList to encapsulate the functionality of a to-do list.
def __init__(self):: Constructor method. Initializes the tasks attribute as an empty list and calls load_tasks to load tasks from a file.
def load_tasks(self):: Loads tasks from "tasks.txt" file into the tasks list. If the file doesn't exist, it catches the FileNotFoundError.
def save_tasks(self):: Saves tasks from the tasks list to "tasks.txt" file.
def display_tasks(self):: Displays tasks with their indices. If no tasks exist, it prints a message indicating that there are no tasks.
def add_task(self, new_task):: Adds a new task to the tasks list, saves the tasks to the file, and prints a confirmation message.
def remove_task(self, task_index):: Removes a task at the specified index, saves the tasks, and prints a confirmation message. Handles cases where the index is out of bounds.
def mark_completed(self, task_index):: Marks a task as completed by adding " (Completed)" to its description. Saves the tasks and prints a confirmation message. Handles cases where the index is out of bounds.
def main():: Defines the main function to interact with the to-do list.
todo = ToDoList(): Creates an instance of the ToDoList class named todo.
while True:: Initiates an infinite loop for the user menu.
Menu Options:
1. Display Tasks: Calls todo.display_tasks() to show the current tasks.
2. Add Task: Takes user input for a new task and calls todo.add_task(new_task).
3. Remove Task: Takes user input for the task index to remove and calls todo.remove_task(task_index).
4. Mark Task as Completed: Takes user input for the task index to mark as completed and calls todo.mark_completed(task_index).
5. Exit: Prints an exit message and breaks out of the loop.
if __name__ == "__main__":: Checks if the script is run directly and calls the main() function.