# WAP to demonstrate interactive command-Line task scheduler with lazy evaluation.
tasks = []
while True:
    print("\n1. Add Task")
    print("2. Execute Tasks")
    print("3. Show Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Enter priority (high/low): ")
        ready = input("Is task ready? (yes/no): ")

        if priority == "high" and ready == "yes":
            tasks.append([task, priority, ready])
            print("High priority task added.")

        elif priority == "low" or ready == "yes":
            tasks.append([task, priority, ready])
            print("Task added.")
        else:
            tasks.append([task, priority, ready])
            print("Task added but postponed.")
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            while tasks:
                task, priority, ready = tasks.pop(0)

                if priority == "high" and ready == "yes":
                    print("Executing:", task)

                elif priority == "low" or ready == "yes":
                    print("Executing:", task)

                else:
                    print("Postponed:", task)
    elif choice == "3":
        if tasks:
            print("\nPending Tasks:")
            for task in tasks:
                print(task)
        else:
            print("No pending tasks.")
    elif choice == "4":
        print("Program terminated.")
        break
    else:
        print("Invalid choice.") 