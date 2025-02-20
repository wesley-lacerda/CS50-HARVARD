# Yearly Goals Map - Final Project CS50s - Wesley Lacerda

from datetime import datetime

goals = []  # List to store goals

def add_goal(description, due_date):
    """
    Adds a new goal to the goals list with a due date.
    """
    try:
        due_date = datetime.strptime(due_date, "%d-%m-%Y")  # Convert string to datetime
        goal = {"description": description, "due_date": due_date, "completed": False, "progress": 0}
        goals.append(goal)
        return f"Goal added: {description} (Due: {due_date.strftime('%d-%m-%Y')})"
    except ValueError:
        return "Invalid date format! Please enter the date in the format DD-MM-YYYY."

def list_goals():
    """
    Returns a list of all goals.
    """
    if not goals:
        return "No goals added yet."

    goal_list = []
    for i, goal in enumerate(goals):
        status = "Completed" if goal["completed"] else "Not Completed"
        goal_list.append(f"{i+1}. {goal['description']} (Due: {goal['due_date'].strftime('%d-%m-%Y')}) - {status} - Progress: {goal['progress']}%")
    return "\n".join(goal_list)

def mark_as_completed(index):
    """
    Marks a goal as completed.
    """
    if 0 <= index - 1 < len(goals):
        goals[index - 1]["completed"] = True
        return f"Goal {index} marked as completed."
    return "Invalid goal number."

def update_progress(index, progress):
    """
    Updates the progress of a goal.
    """
    if 0 <= index - 1 < len(goals):
        if 0 <= progress <= 100:
            goals[index - 1]["progress"] = progress
            return f"Goal {index} progress updated to {progress}%."
        return "Progress must be between 0 and 100."
    return "Invalid goal number."

def time_until_due():
    """
    Returns the time remaining until the due date of each goal.
    """
    if not goals:
        return "No goals added yet."

    time_list = []
    for i, goal in enumerate(goals):
        remaining_time = goal["due_date"] - datetime.now()
        time_list.append(f"{i+1}. {goal['description']} - Time until due: {remaining_time.days} days")
    return "\n".join(time_list)

def save_goals_to_file(user_name):
    """
    Saves the goals to a text file with the user's name in the filename.
    """
    file_name = f"{user_name}_goals.txt"
    with open(file_name, "w") as file:
        for goal in goals:
            status = "Completed" if goal["completed"] else "Not Completed"
            file.write(f"{goal['description']} (Due: {goal['due_date'].strftime('%d-%m-%Y')}) - {status} - Progress: {goal['progress']}%\n")
    return f"Goals saved to {file_name}"

def get_non_empty_input(prompt):
    """
    Ensures the user enters a non-empty value.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please enter a valid value.")

def get_valid_date(prompt):
    """
    Ensures the user enters a valid date in DD-MM-YYYY format.
    """
    while True:
        date_str = get_non_empty_input(prompt)
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            print("Invalid date format! Please enter the date in the format DD-MM-YYYY.")

def main():
    """
    Main function of the program.
    """
    print("Welcome to Yearly Goals Map!")
    print("\nIt's time to define your goals for this year.")
    print("\nThink SMART.")
    print("\nS - Specific")
    print("\nM - Measurable")
    print("\nA - Achievable")
    print("\nR - Relevant")
    print("\nT - Time-bound")

    user_name = get_non_empty_input("Enter your name: ")

    print(f"\nWelcome, {user_name}!")

    while True:
        print("\n--- My Yearly Goals ---")
        print("\n1. Add Goal")
        print("2. List Goals")
        print("3. Mark Goal as Completed")
        print("4. Update Goal Progress")
        print("5. View Progress")
        print("6. Show Time Until Due")
        print("7. Exit")

        option = get_non_empty_input("\nChoose an option: ")

        if option == "1":
            description = get_non_empty_input("Enter the goal description: ")
            due_date = get_valid_date("Enter the due date (DD-MM-YYYY): ")
            print(add_goal(description, due_date))

        elif option == "2":
            print(f"\nYour Goals, {user_name}!")
            print(list_goals())

        elif option == "3":
            index = int(get_non_empty_input("Enter the goal number to mark as completed: "))
            print(mark_as_completed(index))

        elif option == "4":
            index = int(get_non_empty_input("Enter the goal number to update progress: "))
            progress = int(get_non_empty_input("Enter the progress percentage (0-100): "))
            print(update_progress(index, progress))

        elif option == "5":
            print(time_until_due())

        elif option == "6":
            print(time_until_due())

        elif option == "7":
            save = get_non_empty_input("Do you want to save your goals to a text file before exiting? (yes/no): ").lower()
            if save == "yes":
                print(save_goals_to_file(user_name))
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
