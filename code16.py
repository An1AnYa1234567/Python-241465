# Write a program to demostrate object Persistence Engine via Serialization.
import pickle
import shelve

# Define a class
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Create an object
s1 = Student("Annu", 101, 85)

# 1. Save object using pickle
with open("student.pkl", "wb") as file:
    pickle.dump(s1, file)

print("Object saved using pickle.")

# Restore object using pickle
with open("student.pkl", "rb") as file:
    restored_student = pickle.load(file)

print("\nRestored Object:")
restored_student.display()

# 2. Save object using shelve
with shelve.open("student_data") as db:
    db["student1"] = s1

print("\nObject saved using shelve.")

# Restore object using shelve
with shelve.open("student_data") as db:
    restored = db["student1"]

print("\nObject restored using shelve:")
restored.display()