# Importing necessary libraries
import os

# Define the to-do list class
class ToDoList:
    def __init__(self):
        self.items = []

    # Method to add item to the list
    def add_item(self, item, priority=1):
        """
        Add a new item to the to-do list with an optional priority level (1 is default)

        Parameters:
        item (str): The task to be added to the to-do list
        priority (int, optional): The priority level of the task (default=1)

        Returns:
        None
        """
        self.items.append((item, priority))
        print(f"{item} added to the to-do list with priority {priority}.")

    # Method to remove item from the list
    def remove_item(self, item):
        """
        Remove an item from the to-do list

        Parameters:
        item (str): The task to be removed from the to-do list

        Returns:
        None
        """
        # Check if the item exists in the list
        for task in self.items:
            if task[0] == item:
                self.items.remove(task)
                print(f"{item} removed from the to-do list.")
                return
        # If the item is not in the list
        print(f"{item} is not in the to-do list.")

    # Method to print the list
    def print_list(self):
        """
        Print the to-do list with the priority levels

        Parameters:
        None

        Returns:
        None
        """
        if len(self.items) == 0:
            print("To-do list is empty.")
        else:
            print("To-do list:")
            # Sort the list by priority level
            sorted_items = sorted(self.items, key=lambda x: x[1])
            for i, task in enumerate(sorted_items):
                print(f"{i+1}. {task[0]} (priority {task[1]})")

# Define the main function
def main():
    # Create a to-do list object
    todo = ToDoList()

    while True:
        print("\nPlease select an option:")
        print("1. Add item to the to-do list")
        print("2. Remove item from the to-do list")
        print("3. Print the to-do list")
        print("4. Quit the program")
        choice = input("> ")

        if choice == "1":
            item = input("Enter the item to add: ")
            priority = int(input("Enter the priority level (1 is default): "))
            todo.add_item(item, priority)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            todo.remove_item(item)
        elif choice == "3":
            todo.print_list()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
