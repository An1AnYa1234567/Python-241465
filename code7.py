# Write a program to demonstrate robust file management and directory navigation utility.
import os
import sys

print("===== SYSTEM UTILITY TOOL =====")

# Current directory
print("\n1. Current Directory:")
print(os.getcwd())

# List directory contents
print("\n2. Directory Contents:")
for item in os.listdir():
    print(item)

# Create workspace
folder = "Workspace"

print("\n3. Creating Workspace:")
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Workspace created successfully.")
else:
    print("Workspace already exists.")

# Find text files
print("\n4. Text Files:")
for item in os.listdir():
    if item.endswith(".txt"):
        print(item)

# Create and read log file
log_path = os.path.join(folder, "log.txt")

print("\n5. Writing Log:")
with open(log_path, "w") as f:
    f.write("System utility executed successfully.\n")
    f.write("Directory inspection completed.\n")
print("Log written successfully.")

print("\n6. Reading Log:")
with open(log_path, "r") as f:
    print(f.read())

print("===== PROGRAM ENDED =====")